import re, os, glob

ROOT = os.path.expanduser("~/Proyectos/wog-wiki/src/pages")
files = glob.glob(os.path.join(ROOT, "**", "*.astro"), recursive=True)

# new URL('../data/x.json', import.meta.url)  ->  process.cwd() + '/src/data/x.json'
pat = re.compile(r"readFileSync\(new URL\('([^']+)', import\.meta\.url\),\s*'utf-8'\)")

for fp in sorted(files):
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()
    def repl(m):
        return "readFileSync(process.cwd() + '/src/data/' + '{}', 'utf-8')".format(os.path.basename(m.group(1)))
    new = pat.sub(repl, content)
    if new != content:
        with open(fp, "w", encoding="utf-8") as f:
            f.write(new)
        print("fixed", os.path.relpath(fp, ROOT))
    else:
        print("unchanged", os.path.relpath(fp, ROOT))