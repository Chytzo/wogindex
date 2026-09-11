import json, os

base = os.path.expanduser("~/Proyectos/wog-wiki/src/data")

def load(name):
    with open(os.path.join(base, name), encoding="utf-8") as fh:
        return json.load(fh)

heroes = load("heroes.json")
monsters = load("monsters.json")
pets = load("pets.json")
items = load("items.json")

print("=== HEROES (id / name_en / name_es) ===")
for h in heroes:
    if isinstance(h, dict):
        print(h["id"], "|", h.get("name_en"), "|", h.get("name_es"))

print()
print("=== PETS sample ===")
for p in pets[:5]:
    print(json.dumps(p, ensure_ascii=False)[:250])

print()
print("=== MONSTER names (c35) ===")
cnt = 0
for m in monsters:
    nm = m[35] if len(m) > 35 else None
    print(m[0], "|", nm)
    cnt += 1
    if cnt >= 15:
        break

print()
print("=== items id 9100, 9200, 1133 etc ===")
for i in items:
    if isinstance(i, dict) and i["id"] in (9100, 9200, 9300, 9400, 9500, 9600, 1133):
        print(i["id"], "|", i.get("name_en"), "|", i.get("name_es"))

print()
print("=== equip ids: derivar nombres de rango fusion (100010..110060) ===")
for e in load("equip.json"):
    if e["id"] in (100010, 101010, 102010, 110010, 201010, 210010, 300010, 400010, 500010, 600010):
        print(e["id"], "|", e.get("name_en"), "|", e.get("name_es"))