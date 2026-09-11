import subprocess

def curl(url):
    r = subprocess.run(f"curl -s '{url}'", shell=True, capture_output=True, text=True, timeout=20)
    return r.stdout

css = curl("https://chytzo.github.io/wogindex/_astro/abilities.D9E89U32.css")

for cls in ["bg-dark-bg", "bg-dark-card", "text-accent", "border-dark-border", "text-gray-200", "font-bold", "rounded-lg", "bg-dark-card/80", "bg-dark-card/50", "hover:border-accent", "from-accent"]:
    print(f"{cls}: {'FOUND' if cls in css else 'MISSING'}")