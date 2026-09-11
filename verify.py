import subprocess, sys

pages = {
    "home": "https://chytzo.github.io/wogindex/",
    "hero-0": "https://chytzo.github.io/wogindex/heroes/0/",
    "hero-10": "https://chytzo.github.io/wogindex/heroes/10/",
    "hero-list": "https://chytzo.github.io/wogindex/heroes/",
    "equip": "https://chytzo.github.io/wogindex/equip/",
    "items": "https://chytzo.github.io/wogindex/items/",
    "monsters": "https://chytzo.github.io/wogindex/monsters/",
    "stages": "https://chytzo.github.io/wogindex/stages/",
    "skills": "https://chytzo.github.io/wogindex/skills/",
}

checks = {
    "hero-0": ["Iyolin Pendragon", "Iyolin"],
    "home": ["Iyolin", "33", "1872"],
    "equip": ["Iron Sword"],
    "items": ["Gold"],
    "skills": ["Melee", "Ranged"],
}

for name, url in pages.items():
    r = subprocess.run(f"curl -s '{url}'", shell=True, capture_output=True, text=True, timeout=15)
    html = r.stdout
    ok = []
    fail = []
    for check in checks.get(name, []):
        if check in html:
            ok.append(check)
        else:
            fail.append(check)
    status = "OK" if not fail else f"FAIL: {fail}"
    print(f"{name}: {status} (found: {ok})")
