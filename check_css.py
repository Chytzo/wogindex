import subprocess, re

def curl(url):
    r = subprocess.run(f"curl -s '{url}'", shell=True, capture_output=True, text=True, timeout=20)
    return r.stdout, r.returncode

home, _ = curl("https://chytzo.github.io/wogindex/")
print("=== HOME <link> tags ===")
for m in re.findall(r"<link[^>]*>", home):
    print(m)
print("\n=== HOME <script> tags ===")
for m in re.findall(r"<script[^>]*>", home):
    print(m)
print("\n=== HOME <style> count ===", home.count("<style"))

# check css file
css_urls = re.findall(r'href="([^"]*\.css)"', home)
for cu in css_urls:
    css, ret = curl("https://chytzo.github.io/wogindex" + cu)
    print(f"\n=== CSS {cu}: {ret}, {len(css)} bytes ===")
    print(css[:400])