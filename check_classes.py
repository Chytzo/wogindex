import json, os

base = os.path.expanduser("~/Proyectos/wog-wiki/src/data")
t = json.load(open(os.path.join(base, "tiers.json"), encoding="utf-8"))

heroes = t["heroes"]
# class derived from id: 100s = ?, 200s = ?, 300s = ?
from collections import Counter
buckets = Counter(h["id"] // 100 for h in heroes)
print("id buckets:", dict(buckets))
for b in sorted(buckets):
    names = [h["name"] for h in heroes if h["id"] // 100 == b]
    print(f"{b}00-range:", names)
# quality values
print("qualities:", Counter(h["quality"] for h in heroes))