import json, os, sys

p = os.path.expanduser("~/Proyectos/wog-wiki/data/resolved_tables.json")
with open(p, encoding="utf-8") as fh:
    data = json.load(fh)

for tbl in ["fusion", "fusionlevel", "drop", "droplist", "gacha", "gachalist", "item", "hero", "equip", "config"]:
    if tbl not in data:
        print(f"== {tbl}: NOT FOUND"); continue
    d = data[tbl]
    if isinstance(d, list):
        n = len(d)
        sample = d[0] if d and isinstance(d[0], dict) else d[:3]
        print(f"== {tbl}: list[{n}]")
        print("   sample keys:", list(sample.keys()) if isinstance(sample, dict) else sample)
        print("   sample:", json.dumps(sample, ensure_ascii=False)[:300])
    elif isinstance(d, dict):
        n = len(d)
        k0 = next(iter(d))
        v0 = d[k0]
        print(f"== {tbl}: dict[{n}]")
        print("   sample key:", k0, "->", json.dumps(v0, ensure_ascii=False)[:200])
    print()