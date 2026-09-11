import subprocess, re

def curl(url):
    r = subprocess.run(f"curl -s -o /dev/null -w '%{{http_code}}' '{url}'", shell=True, capture_output=True, text=True, timeout=20)
    return r.stdout

def curl_raw(url):
    r = subprocess.run(f"curl -s '{url}'", shell=True, capture_output=True, text=True, timeout=20)
    return r.stdout

# Como se resuelven las rutas en el navegador desde chytzo.github.io/wogindex/
print("1. CSS con base /wogindex/:", curl("https://chytzo.github.io/wogindex/_astro/abilities.D9E89U32.css"))
print("2. CSS sin base (/_astro/):", curl("https://chytzo.github.io/_astro/abilities.D9E89U32.css"))
print("3. heroes con base:", curl("https://chytzo.github.io/wogindex/heroes/"))
print("4. heroes sin base:", curl("https://chytzo.github.io/heroes/"))

home = curl_raw("https://chytzo.github.io/wogindex/")
print("hrefs del home:", re.findall(r'href="([^"]*)"', home)[:12])