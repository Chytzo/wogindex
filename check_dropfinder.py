import json, os

base = os.path.expanduser("~/Proyectos/wog-wiki/src/data")
d = json.load(open(os.path.join(base, "dropfinder.json"), encoding="utf-8"))

# Iron Sword 201001
for iid in (201001, 201002, 1000100, 195000, 9100):
    if str(iid) in d:
        entry = d[str(iid)]
        print(f"== item {iid} '{entry['name']}': {len(entry['sources'])} sources")
        for s in entry["sources"][:12]:
            print("   ", s)
        break
# how many items have >100 sources
counts = collections.Counter()
import collections
for k, v in d.items():
    counts[len(v["sources"])] += 1
print("\nsource-count distribution:", sorted(counts.items())[:15])
# total items
print("total items:", len(d))
# check rates
rates = set()
for k, v in list(d.items())[:500]:
    for s in v["sources"]:
        rates.add(s["rate"])
print("rate values sample:", sorted(rates)[:15])