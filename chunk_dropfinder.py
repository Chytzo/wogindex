import json, os

base = os.path.expanduser("~/Proyectos/wog-wiki/src/data")

def load(name):
    with open(os.path.join(base, name), encoding="utf-8") as fh:
        return json.load(fh)

def dump(name, obj):
    with open(os.path.join(base, name), "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False)
    print("wrote", name, round(os.path.getsize(os.path.join(base, name))/1024/1024, 2), "MB")

clean = load("dropfinder_min.json")
idx = load("dropfinder_index.json")

# chunk every 150 items
CHUNK = 150
chunks = []
cur = {}
for iid, v in sorted(clean.items()):
    cur[iid] = v
    if len(cur) >= CHUNK:
        chunks.append(cur); cur = {}
if cur:
    chunks.append(cur)

# write chunk files and rebuild index with chunk pointers
for ci, ch in enumerate(chunks):
    dump(f"dropfinder_c{ci}.json", ch)

# update index: add chunk number
chunk_of = {}
for ci, ch in enumerate(chunks):
    for iid in ch:
        chunk_of[iid] = ci
for e in idx:
    e["chunk"] = chunk_of[str(e["id"])]

dump("dropfinder_index.json", idx)
print("chunks:", len(chunks), "| total items:", sum(len(c) for c in chunks))