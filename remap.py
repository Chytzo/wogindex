import os, glob

ROOT = os.path.expanduser("~/Proyectos/wog-wiki/src")
files = glob.glob(os.path.join(ROOT, "layouts", "*.astro")) + glob.glob(os.path.join(ROOT, "pages", "**", "*.astro"), recursive=True)

REPL = [
    # texto secundario gris -> beige/mud
    ("text-gray-600", "text-mud/70"),
    ("text-gray-500", "text-mud"),
    ("text-gray-400", "text-mud"),
    ("text-gray-300", "text-cream/80"),
    ("text-gray-200", "text-cream"),
    # texto blanco -> crema
    ("text-white/80", "text-cream/80"),
    ("text-white", "text-cream"),
    # hover blanco -> dorado
    ("group-hover:text-white", "group-hover:text-gold"),
    # bordes grises -> marrón
    ("border-gray-800", "border-dark-border"),
    ("border-gray-700", "border-dark-border"),
    ("border-gray-600", "border-dark-border"),
    ("bg-gray-800", "bg-dark-card"),
    ("bg-gray-900", "bg-dark-card"),
]

changed = []
for fp in sorted(files):
    s = open(fp, encoding="utf-8").read()
    orig = s
    for a, b in REPL:
        s = s.replace(a, b)
    if s != orig:
        open(fp, "w", encoding="utf-8").write(s)
        changed.append(os.path.relpath(fp, ROOT))

print("changed:", len(changed))
for c in changed:
    print("  ", c)