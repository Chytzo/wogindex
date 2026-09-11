import json, os

base = os.path.expanduser("~/Proyectos/wog-wiki/src/data")
t = json.load(open(os.path.join(base, "tiers.json"), encoding="utf-8"))
print("heroes:", len(t["heroes"]))
for h in t["heroes"][:8]:
    print("  ", h)
print()
print("pets:", len(t["pets"]))
for p in t["pets"][:5]:
    print("  ", p)