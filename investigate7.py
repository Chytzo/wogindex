import json, os

base = os.path.expanduser("~/Proyectos/wog-wiki/src/data")

def load(name):
    with open(os.path.join(base, name), encoding="utf-8") as fh:
        return json.load(fh)

locales = load("locales.json")
# show a character name entry
print("Base_Character_Name_01:", json.dumps(locales.get("Base_Character_Name_01"), ensure_ascii=False))
print("keys containing Stage_Area:", [k for k in locales if "Stage_Area" in k][:8])
print("sample UI_Stage_Area_Name_01_01:", json.dumps(locales.get("UI_Stage_Area_Name_01_01"), ensure_ascii=False)[:300])
# how stages reference locale keys: c41
print()
stages = load("stages.json")
print("stage c41 sample:", [s[41] for s in stages[:5]])
# unique c41 keys
keys = set(s[41] for s in stages if s[41])
print("distinct c41 keys:", len(keys))
for k in sorted(keys)[:10]:
    pass
# check the '_main' langs present
sample = locales.get("UI_Stage_Area_Name_01_01")
if sample:
    print("langs:", sample.keys())
    print("_main:", sample.get("_main"))
    print("en:", sample.get("en"))
    print("ko:", sample.get("ko"))