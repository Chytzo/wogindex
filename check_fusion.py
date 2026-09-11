import json, os

base = os.path.expanduser("~/Proyectos/wog-wiki/src/data")

def load(name):
    with open(os.path.join(base, name), encoding="utf-8") as fh:
        return json.load(fh)

fc = load("fusion_curve.json")
print("curve cats:", list(fc.keys()))
for cat, rows in fc.items():
    print(f"cat {cat}: {len(rows)} levels; lvl1={rows[0] if rows else None}; lvl50={rows[50] if len(rows)>50 else None}; last={rows[-1] if rows else None}")

print()
fp = load("fusion_planner.json")
print("planner sample:", json.dumps(fp[0], ensure_ascii=False)[:300])
print("planner sample2:", json.dumps(fp[1], ensure_ascii=False)[:300])
# categories present
print("plan cats:", sorted(set(p["cat"] for p in fp)))
print("plan mats:", sorted(set(p["mat"] for p in fp)))
print("plan steps per cat:", {c: sorted(set(p["step"] for p in fp if p["cat"]==c)) for c in sorted(set(p["cat"] for p in fp))})