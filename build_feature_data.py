import json, os, collections

base = os.path.expanduser("~/Proyectos/wog-wiki/src/data")

def load(name):
    with open(os.path.join(base, name), encoding="utf-8") as fh:
        return json.load(fh)

def dump(name, obj):
    with open(os.path.join(base, name), "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=1)
    print("wrote", name, "| entries:", len(obj) if hasattr(obj, "__len__") else "?")

drops = load("drops.json")
droplists = load("droplists.json")
stages = load("stages.json")
equip = load("equip.json")
items = load("items.json")
weapons = load("weapons.json")
locales = load("locales.json")
heroes = load("heroes.json")
pets = load("pets.json")
monsters = load("monsters.json")

# ---------- item name resolver ----------
name_map = {}
for e in equip:
    name_map[e["id"]] = e.get("name_en") or e.get("name_es") or f"Eq #{e['id']}"
for i in items:
    name_map[i["id"]] = (i.get("name_en") or i.get("name_es") or f"Item #{i['id']}")
for w in weapons:
    name_map[w["id"]] = w.get("name_en") or w.get("name_kr") or f"Weapon #{w['id']}"

def iname(num):
    return name_map.get(num, f"#{num}")

# ---------- monster id --> stage mapping (stage.c13 = monster ids per wave)
stage_by_monster = collections.defaultdict(list)
monster_name_map = {}
for s in stages:
    for m in (s[13] or []):
        stage_by_monster[m].append(s[0])
for m in monsters:
    # name in c35 (string) or c39 resolved
    nm = m[35] if len(m) > 35 and isinstance(m[35], str) and m[35] not in ("0", "0.0", "") else None
    if not nm and len(m) > 44 and isinstance(m[44], dict):
        nm = m[44].get("__resolved_name")
    monster_name_map[m[0]] = nm or type_name[m[0]] if False else (nm or f"Monster #{m[0]}")

# ---------- stage names ----------
def stage_name(s):
    key = s[41] if len(s) > 41 and s[41] else None
    if key:
        ent = locales.get(key)
        if isinstance(ent, dict):
            nm = ent.get("_main") or ent.get("en")
            if nm:
                return nm
    return f"Stage {s[0]}"

# ---------- DROP FINDER ----------
# chain: droplist(c1 group, c6 item, c10 peso, c11 denom) ; drop(c1 = stage drop group, c4 = droplist group)
# stage.c32 = normal drop groups, stage.c36 = boss drop groups
# build item -> stages
#
# droplist rows describe chance within a droplist group = c10/c11 (denom usually 1M)
# drop rows link stage-group (c1) -> droplist groups (c4)
# a stage's c32 list = normal drop groups it rolls; c36 = boss drop groups

# group droplists by group
dl_by_group = collections.defaultdict(list)
for dl in droplists:
    dl_by_group[dl[1]].append(dl)

# map each stage drop group -> droplist group sets with weight
# For Drop Finder: per item, list stages + kind + which droplist group + weight
item_sources = collections.defaultdict(list)
seen_sources = set()

for s in stages:
    sid = s[0]
    sname = stage_name(s)
    for kind, group_col in (("normal", 32), ("boss", 36)):
        if len(s) <= group_col:
            continue
        stage_groups = s[group_col] or []
        for sg in stage_groups:
            # find drop rows whose c1 == sg
            dl_groups_with_weight = []
            for d in drops:
                if d[1] == sg:
                    dlg = d[4]
                    # get weight of this droplist group within stage group
                    w = d[10] if len(d) > 10 else 1000000
                    dl_groups_with_weight.append((dlg, w))
            for dlg, w_drop in dl_groups_with_weight:
                for dl in dl_by_group.get(dlg, []):
                    item_id = dl[6]
                    cnt = dl[7] if len(dl) > 7 else 1
                    rate = dl[10] if len(dl) > 10 else 0
                    denom = dl[11] if len(dl) > 11 and dl[11] else 1000000
                    pct = round(rate / denom * 100, 4) if denom else 0
                    key = (item_id, sid, kind)
                    if key in seen_sources:
                        continue
                    seen_sources.add(key)
                    item_sources[item_id].append({
                        "stage": sid,
                        "stage_name": sname,
                        "kind": kind,
                        "rate": pct,
                        "count": cnt,
                    })

# stats
items_with_sources = len(item_sources)
total_sources = sum(len(v) for v in item_sources.values())
print(f"DropFinder: {items_with_sources} items, {total_sources} sources")
# filter to items that have a name
dropindex = {}
for iid, srcs in item_sources.items():
    dropindex[iid] = {"name": iname(iid), "sources": srcs}
dump("dropfinder.json", dropindex)

# ---------- FUSION PLANNER ----------
fusion = load("fusion.json")
fl = load("fusionlevel.json")

mat_names = {9100: "Equipment Synth EXP", 9200: "Accessory Synth EXP",
             9300: "Pet Synth EXP", 9400: "Wings Synth EXP",
             9500: "Rune Synth EXP", 9600: "Jewel Synth EXP"}
cat_names = {1: "Weapon", 2: "Armor", 3: "Wings", 4: "Rune", 5: "Pet", 20: "Jewel/Other"}
# geneologic: c2 = category, c10 = level(1..6), c11 = ??? , c7 gold, c8/c9 costs, c13 material, c14 count
recipes = []
for f in fusion:
    recipes.append({
        "id": f[0],
        "cat": f[2],
        "gold": f[7],
        "cost_a": f[8],
        "cost_b": f[9],
        "step": f[10],      # 1..6
        "tier": f[11],      # 1,10,20,...100
        "n": f[12],
        "mat": f[13],
        "mat_name": mat_names.get(f[13], f"Mat {f[13]}"),
        "need": f[14],
        "from_lo": f[3] or f[5],
        "from_hi": f[4] or f[6],
    })
dump("fusion_planner.json", recipes)

# ---------- FUSIONLEVEL (Synthesis EXP curve) ----------
# curve per material ref (c4) + item category (c2): level (c3) -> exp (c5) * multiplier(c6)
curve = {}
for r in fl:
    cat = r[2]
    if cat not in curve:
        curve[cat] = []
    curve[cat].append({"lvl": r[3], "exp": r[5], "mul": r[6],
                       "reward": (r[7][0] if r[7] else None),
                       "reward_qty": (r[8][0] if r[8] else 0)})
dump("fusion_curve.json", curve)

# ---------- TIER DATA ----------
# heroes ranked by raw power = sum(stats). Use their base stats fields as existing UI does.
hero_rows = []
for i, h in enumerate(heroes):
    r = h["row"]
    hero_rows.append({
        "id": h["id"], "name": h.get("name_en") or h.get("name_es") or f"Hero #{h['id']}",
        "idx": i,
        "atk": r[10], "atk2": r[12], "def": r[13], "hp": r[14],
        "critical": r[15], "speed": r[21], "growth": r[26],
        "quality": r[2], "class": r[4],
        "power": round((r[10] or 0) + (r[12] or 0) + (r[13] or 0) + (r[14] or 0), 1),
    })
hero_rows.sort(key=lambda x: -x["power"])
# tiers: S top 15%, A next 25%, B next 30%, C rest
def tier_for(i, n):
    pct = i / max(n - 1, 1)
    if pct < 0.15: return "S"
    if pct < 0.40: return "A"
    if pct < 0.70: return "B"
    return "C"
for i, h in enumerate(hero_rows):
    h["tier"] = tier_for(i, len(hero_rows))

# pets ranked (quality/grade from row)
pet_rows = []
for p in pets:
    r = p["row"]
    name = p.get("name_en") or p.get("name_es") or (r[-1].get("__resolved_name") if isinstance(r[-1], dict) else f"Pet #{r[0]}")
    pet_rows.append({
        "id": r[0], "name": name, "grade": r[16] if len(r) > 16 else None,
        "sound_rate": r[11][0] if len(r) > 11 and r[11] else None,
    })

dump("tiers.json", {
    "heroes": hero_rows,
    "pets": pet_rows,
    "monsters": monsters,
    "stages": stages,
})

# ---------- STAGE POWER (HP por stage) ----------
# monster row: c10 HP? Actually check monsters col for hp. Use c? monster[0]=id, c9='55', c? 
# monster schema will need another inspection pass; skip for now.
print("DONE")