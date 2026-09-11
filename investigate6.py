import json, os

base = os.path.expanduser("~/Proyectos/wog-wiki/src/data")

def load(name):
    with open(os.path.join(base, name), encoding="utf-8") as fh:
        return json.load(fh)

locales = load("locales.json")
print("locales root type:", type(locales).__name__)
if isinstance(locales, dict):
    print("root keys sample:", list(locales.keys())[:5])
    k0 = list(locales.keys())[0]
    print("value of", k0, ":", json.dumps(locales[k0], ensure_ascii=False)[:500])