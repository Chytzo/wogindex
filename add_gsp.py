import sys, os

fp = os.path.expanduser(sys.argv[1])
s = open(fp, encoding="utf-8").read()
old = "const { id } = Astro.params;\nconst heroes = JSON.parse(readFileSync"
new = "export function getStaticPaths() {\n  const heroes = JSON.parse(readFileSync(process.cwd() + '/src/data/' + 'heroes.json', 'utf-8'));\n  return heroes.map((_, i) => ({ params: { id: String(i) } }));\n}\n\nconst { id } = Astro.params;\nconst heroes = JSON.parse(readFileSync"
assert old in s, "pattern not found"
s = s.replace(old, new, 1)
open(fp, "w", encoding="utf-8").write(s)
print("OK getStaticPaths inserted")