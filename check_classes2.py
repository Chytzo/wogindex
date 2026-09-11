import json, os

base = os.path.expanduser("~/Proyectos/wog-wiki/src/data")
heroes = json.load(open(os.path.join(base, "heroes.json"), encoding="utf-8"))
from collections import Counter
c = Counter(h["row"][1] for h in heroes)
print("class (r[1]) distribution:", dict(c))
for v in sorted(c):
    names = [h.get("name_en") or h.get("name_es") for h in heroes if h["row"][1] == v]
    print(v, "->", names)

# also r[2] quality
c2 = Counter(h["row"][2] for h in heroes)
print("\nquality r[2]:", dict(c2))
# r[4]?
c4 = Counter(h["row"][4] for h in heroes)
print("r[4]:", dict(c4))