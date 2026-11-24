#!/usr/bin/env python3
"""Find and measure runnable ground near an address, from open data only.

Built 2026-11-15 after doing this by hand three times in one week (Sacramento,
Denver, Aurora Reservoir). He travels constantly and every new city needs the
same two questions answered before a quality session can be placed:

  1. Where is there continuous car-free ground long enough to hold a rep?
  2. Is it LEVEL ACROSS A REP?

His correction, 2026-11-15, and the reason the second question is phrased that
way: *"i wasnt really minding the elevation going up, it was more that intra
rep elevation should be level."*  Absolute altitude is a pace offset you
absorb once. GRADIENT INSIDE A REP is what breaks a fixed-pace session -- the
2026-11-03 San Francisco 6x6 produced 32 s/km of grade-adjusted spread off a
single pace target. So the headline number here is the worst net rise or fall
inside one rep-length window, not the site's elevation.

Sources, all open, no keys, no scraping of anyone's heatmap:
  - OpenStreetMap via Overpass (ODbL) for paths, surface, names
  - OpenTopoData (USGS NED 10 m in the US, SRTM elsewhere) for elevation,
    BATCHED -- up to 100 points per call. The USGS EPQS point service does
    one lookup per call and is far too slow; it timed out repeatedly.

Two traps already paid for:
  - Overpass public endpoints 502 often. Mirrors + retry, always.
  - Do NOT order a trail's points by latitude or longitude to build a
    profile. On 2026-11-12 that collapsed a 3 km stretch into a 400 m
    cluster of bridge ramps and reported a meaningless 4.7 m of relief.
    Walk the OSM way's own geometry, which is already in order.

Usage:
    python3 -I tools/terrain.py --around 39.713,-104.985 --radius 4000
    python3 -I tools/terrain.py --bbox 39.588,-104.690,39.628,-104.630
    python3 -I tools/terrain.py --bbox ... --name "Perimeter Trail"
    python3 -I tools/terrain.py --bbox ... --rep-km 2.0 --dataset ned10m
"""

import argparse
import json
import math
import sys
import time
import urllib.parse
import urllib.request

UA = {"User-Agent": "personal-trainer-terrain/1.0"}
# Global-coverage mirrors ONLY. A regional instance (overpass.osm.ch covers
# Switzerland) answers 200 with zero elements for anywhere else, which reads as
# "there is no trail here" rather than "wrong server" -- that cost a Denver
# lookup on 2026-11-18. If you add a mirror, check its extent first.
MIRRORS = [
    "https://overpass-api.de/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
    "https://overpass.private.coffee/api/interpreter",
]
RUNNABLE = "path|footway|cycleway|track|pedestrian"


def hav(a, b):
    r = 6371000.0
    p1, p2 = math.radians(a[0]), math.radians(b[0])
    dp = p2 - p1
    dl = math.radians(b[1] - a[1])
    x = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(x))


def fetch(url, timeout=60):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout).read()


def overpass(query, timeout=40):
    """One try per mirror. The public endpoints 502 and hang routinely, and a
    generous retry budget just turns a failure into a hang -- that is exactly
    how the 2026-11-15 smoke test burned two minutes and returned nothing."""
    err = None
    for mirror in MIRRORS:
        try:
            req = urllib.request.Request(
                mirror, data=("data=" + urllib.parse.quote(query)).encode(), headers=UA)
            return json.loads(urllib.request.urlopen(req, timeout=timeout).read())
        except Exception as e:
            err = e
            print("  (%s failed: %s)" % (mirror.split("/")[2], e), file=sys.stderr)
    raise RuntimeError("all Overpass mirrors failed: %s" % err)


def elevations(points, dataset):
    """Batched. OpenTopoData allows 100 locations per call, ~1 call/sec."""
    out = []
    for i in range(0, len(points), 100):
        chunk = points[i:i + 100]
        loc = "|".join("%.6f,%.6f" % p for p in chunk)
        r = json.loads(fetch("https://api.opentopodata.org/v1/%s?locations=%s"
                             % (dataset, urllib.parse.quote(loc))))
        out.extend(x["elevation"] for x in r["results"])
        if i + 100 < len(points):
            time.sleep(1.2)
    return out


def worst_window(profile, window_m):
    """Largest |net change| between two points <= window_m apart. One rep."""
    worst, span = 0.0, None
    for i, (ci, ei) in enumerate(profile):
        for cj, ej in profile[i:]:
            if cj - ci > window_m:
                break
            if cj - ci >= window_m * 0.9 and abs(ej - ei) > worst:
                worst, span = abs(ej - ei), (ci, cj)
    return worst, span


def main():
    p = argparse.ArgumentParser()
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--bbox", help="south,west,north,east")
    g.add_argument("--around", help="lat,lon (use with --radius)")
    p.add_argument("--radius", type=int, default=4000)
    p.add_argument("--name", help="only ways whose name matches (case-insensitive)")
    p.add_argument("--rep-km", type=float, default=2.0,
                   help="rep length in km; the headline window (default 2.0)")
    p.add_argument("--dataset", default="ned10m",
                   help="ned10m (US, 10 m) or srtm30m (global). Default ned10m")
    p.add_argument("--include-unnamed", action="store_true",
                   help="include UNNAMED footways/paths. Lakeside loops, park paths and levee\n                        tops are often unnamed; without this they are invisible. Keep the bbox tight.")
    p.add_argument("--top", type=int, default=5)
    p.add_argument("--timeout", type=int, default=40,
                   help="per-mirror HTTP timeout in seconds (default 40)")
    a = p.parse_args()

    if a.bbox:
        area = "(%s)" % a.bbox
    else:
        lat, lon = (float(x) for x in a.around.split(","))
        area = "(around:%d,%f,%f)" % (a.radius, lat, lon)
    # Keep the query cheap: a name filter already excludes sidewalks, and
    # stacking a negative regex on top of it is what makes Overpass hang.
    if a.name:
        q = ('[out:json][timeout:60];way%s[highway~"%s"][name~"%s",i];out body geom;'
             % (area, RUNNABLE, a.name))
    elif a.include_unnamed:
        # The best running ground is often an UNNAMED footway -- lakeside loops,
        # park paths, levee tops. Requiring [name] silently drops them, which is
        # how a Brunnsviken search returned nothing but 400 m side streets on
        # 2026-11-23. Costs more noise, so keep the bbox tight.
        q = ('[out:json][timeout:60];way%s[highway~"%s"]'
             '[footway!~"^(sidewalk|crossing)$"];out body geom;' % (area, RUNNABLE))
    else:
        q = ('[out:json][timeout:60];way%s[highway~"%s"][name]'
             '[footway!~"^(sidewalk|crossing)$"];out body geom;' % (area, RUNNABLE))

    try:
        data = overpass(q, a.timeout)
    except RuntimeError as e:
        sys.exit(str(e))

    ways = []
    for e in data["elements"]:
        geom = e.get("geometry") or []
        if len(geom) < 2:
            continue
        pts = [(g["lat"], g["lon"]) for g in geom]
        length = sum(hav(pts[i], pts[i + 1]) for i in range(len(pts) - 1))
        tags = e.get("tags") or {}
        ways.append((length, pts, tags.get("name", "(unnamed)"),
                     tags.get("surface", "?"), tags.get("lit", "?")))
    if not ways:
        sys.exit("Overpass answered but returned NOTHING for this area.\n"
                 "  Either the filter is too narrow (widen the area or drop --name),\n"
                 "  or the mirror that answered does not cover this part of the world.\n"
                 "  An empty 200 is not evidence that the ground isn't there.")
    ways.sort(reverse=True, key=lambda w: w[0])

    print("%d ways, %.1f km of runnable path in the area\n" % (
        len(ways), sum(w[0] for w in ways) / 1000))
    print("%-42s %8s %-10s %s" % ("name", "length", "surface", "lit"))
    for length, _, name, surface, lit in ways[:a.top]:
        print("%-42s %7.2fkm %-10s %s" % (name[:42], length / 1000, surface, lit))

    window = a.rep_km * 1000
    length, pts, name, surface, lit = ways[0]
    print("\nprofiling the longest continuous way: '%s' (%.2f km, %s)"
          % (name, length / 1000, surface))
    if length < window:
        print("  NOTE: shorter than one %.1f km rep -- it cannot hold a rep unbroken."
              % a.rep_km)

    step = max(100.0, length / 98)
    sel, acc = [pts[0]], 0.0
    for i in range(len(pts) - 1):
        acc += hav(pts[i], pts[i + 1])
        if acc >= step:
            sel.append(pts[i + 1])
            acc = 0.0
    sel = sel[:99]
    try:
        ev = elevations(sel, a.dataset)
    except Exception as e:
        sys.exit("elevation lookup failed: %s" % e)

    cum = [0.0]
    for i in range(len(sel) - 1):
        cum.append(cum[-1] + hav(sel[i], sel[i + 1]))
    profile = [(c, e) for c, e in zip(cum, ev) if e is not None]
    if len(profile) < 3:
        sys.exit("too few elevation samples came back")

    lo = min(e for _, e in profile)
    hi = max(e for _, e in profile)
    print("  %d samples over %.2f km: %.0f-%.0f m, total relief %.1f m"
          % (len(profile), profile[-1][0] / 1000, lo, hi, hi - lo))
    worst, span = worst_window(profile, window)
    if span:
        grade = 100.0 * worst / window
        print("  WORST NET CHANGE ACROSS A %.1f km REP: %.1f m  (%.2f%% average grade)"
              % (a.rep_km, worst, grade))
        print("  for scale: his flat Sacramento 6x6 strip is ~3 m over 2.2 km (0.14%)")


if __name__ == "__main__":
    main()
