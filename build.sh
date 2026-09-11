#!/bin/bash
set -euo pipefail
export PATH="/home/hermes/.hermes/node/bin:/home/hermes/.hermes/node/lib/node_modules/.bin:/home/hermes/.local/bin:$PATH"
cd ~/Proyectos/wog-wiki

echo "[1/7] Unzip data..."
unzip -o wog_wiki_data.zip -d .

echo "[2/7] Create package.json manually..."
cat > package.json << 'PKJEOF'
{
  "name": "wogindex",
  "type": "module",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "astro dev",
    "build": "astro build",
    "preview": "astro preview"
  },
  "dependencies": {
    "astro": "^5.16.0"
  },
  "devDependencies": {
    "@astrojs/tailwind": "^6.0.2",
    "tailwindcss": "^3.4.17"
  }
}
PKJEOF

echo "[3/7] Install dependencies..."
npm install 2>&1 | tail -8

echo "[4/7] Configure astro..."
cat > astro.config.mjs << 'ASTROEOF'
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
export default defineConfig({
  site: 'https://wogindex.com',
  integrations: [tailwind()],
});
ASTROEOF

cat > tsconfig.json << 'TSEOF'
{
  "extends": "astro/tsconfigs/base",
  "compilerOptions": {
    "strict": true
  }
}
TSEOF

cat > tailwind.config.mjs << 'TWEOF'
/** @type {import("tailwindcss").Config} */
export default {
  content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
  theme: {
    extend: {
      colors: {
        dark: { bg: "#0f1117", card: "#1a1d29", border: "#2a2d3a" },
        accent: "#3b82f6",
        quality: { common: "#9ca3af", uncommon: "#22c55e", rare: "#3b82f6", epic: "#a855f7", legendary: "#f97316", mythic: "#ef4444" },
      },
    },
  },
  plugins: [],
};
TWEOF

echo "[5/7] Create site structure..."
mkdir -p src/layouts src/pages/heroes src/components public/datos src/data
cp -r datos/* public/datos/
cp -r datos/* src/data/

# Public helpers
cat > public/favicon.svg << 'FAVEOF'
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect width="100" height="100" rx="20" fill="#0f1117"/><path d="M28 74 V44 l12 14 12-24 12 24 12-14 v30" stroke="#3b82f6" stroke-width="6" fill="none" stroke-linecap="round"/></svg>
FAVEOF

cat > public/_headers << 'HEOF'
/*
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
HEOF

# BaseLayout
cat > src/layouts/BaseLayout.astro << 'LAYOUTEOF'
---
const { title = "WoG Index" } = Astro.props;
---
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} — WoG Index</title>
  <meta name="description" content="War of Genesis: Idle Loot database and wiki — heroes, equipment, items, monsters, stages, gacha and more." />
  <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
</head>
<body class="bg-dark-bg text-gray-200 min-h-screen flex flex-col">
  <header class="bg-dark-card/80 backdrop-blur border-b border-dark-border px-4 py-3 sticky top-0 z-50">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
      <a href="/" class="flex items-center gap-2 group">
        <span class="w-8 h-8 rounded-lg bg-accent/20 flex items-center justify-center font-black text-accent group-hover:bg-accent group-hover:text-white transition">W</span>
        <span class="text-xl font-bold text-white">WoG <span class="text-accent">Index</span></span>
      </a>
      <p class="text-xs text-gray-400 hidden md:block">War of Genesis: Idle Loot — Game Database & Wiki</p>
      <input id="global-search" type="text" placeholder="Search..." class="bg-dark-bg border border-dark-border rounded-lg px-3 py-1.5 text-sm w-44 md:w-64 focus:outline-none focus:border-accent focus:ring-1 focus:ring-accent transition" />
    </div>
  </header>
  <div class="flex flex-1">
    <aside class="w-56 bg-dark-card/50 border-r border-dark-border py-4 px-3 hidden md:block shrink-0">
      <nav class="sticky top-[72px] space-y-0.5 text-sm">
        <div class="text-[11px] uppercase tracking-wider text-gray-500 font-semibold px-2 mt-3 mb-1">Heroes & Combat</div>
        <a href="/heroes" class="block px-2 py-1.5 rounded hover:bg-dark-card hover:text-accent transition">Heroes</a>
        <a href="/skills" class="block px-2 py-1.5 rounded hover:bg-dark-card hover:text-accent transition">Skills</a>
        <a href="/passiveskills" class="block px-2 py-1.5 rounded hover:bg-dark-card hover:text-accent transition">Passives</a>
        <a href="/abilities" class="block px-2 py-1.5 rounded hover:bg-dark-card hover:text-accent transition">Abilities</a>
        <a href="/monsters" class="block px-2 py-1.5 rounded hover:bg-dark-card hover:text-accent transition">Monsters</a>
        <div class="text-[11px] uppercase tracking-wider text-gray-500 font-semibold px-2 mt-4 mb-1">Gear & Items</div>
        <a href="/equip" class="block px-2 py-1.5 rounded hover:bg-dark-card hover:text-accent transition">Equipment</a>
        <a href="/weapons" class="block px-2 py-1.5 rounded hover:bg-dark-card hover:text-accent transition">Weapons</a>
        <a href="/items" class="block px-2 py-1.5 rounded hover:bg-dark-card hover:text-accent transition">Items</a>
        <a href="/pets" class="block px-2 py-1.5 rounded hover:bg-dark-card hover:text-accent transition">Pets</a>
        <a href="/machina" class="block px-2 py-1.5 rounded hover:bg-dark-card hover:text-accent transition">Machina</a>
        <div class="text-[11px] uppercase tracking-wider text-gray-500 font-semibold px-2 mt-4 mb-1">Stages & Drops</div>
        <a href="/stages" class="block px-2 py-1.5 rounded hover:bg-dark-card hover:text-accent transition">Stages</a>
        <a href="/drops" class="block px-2 py-1.5 rounded hover:bg-dark-card hover:text-accent transition">Drop Tables</a>
        <a href="/gacha" class="block px-2 py-1.5 rounded hover:bg-dark-card hover:text-accent transition">Gacha</a>
        <div class="text-[11px] uppercase tracking-wider text-gray-500 font-semibold px-2 mt-4 mb-1">Tools & Data</div>
        <a href="/fusion" class="block px-2 py-1.5 rounded hover:bg-dark-card hover:text-accent transition">Fusion</a>
      </nav>
    </aside>
    <main class="flex-1 px-4 md:px-8 py-6 max-w-7xl mx-auto min-w-0 w-full">
      <slot />
    </main>
  </div>
  <footer class="border-t border-dark-border py-4 text-center text-xs text-gray-500">
    WoG Index — Fan-made database for War of Genesis: Idle Loot. Not affiliated with the game developers.
  </footer>
</body>
</html>
LAYOUTEOF

# Homepage
cat > src/pages/index.astro << 'INDEXEOF'
---
import BaseLayout from '../layouts/BaseLayout.astro';
import { readFileSync } from 'node:fs';
const heroes = JSON.parse(readFileSync(new URL('../data/heroes.json', import.meta.url), 'utf-8'));
const equip = JSON.parse(readFileSync(new URL('../data/equip.json', import.meta.url), 'utf-8'));
const items = JSON.parse(readFileSync(new URL('../data/items.json', import.meta.url), 'utf-8'));
const monsters = JSON.parse(readFileSync(new URL('../data/monsters.json', import.meta.url), 'utf-8'));
const stages = JSON.parse(readFileSync(new URL('../data/stages.json', import.meta.url), 'utf-8'));
const qColor = {2:"text-green-400",3:"text-blue-400",4:"text-purple-400",5:"text-orange-400",6:"text-red-400"};
---
<BaseLayout title="Home">
  <h1 class="text-3xl md:text-4xl font-extrabold mb-2">War of Genesis: <span class="text-accent">Idle Loot</span> Database</h1>
  <p class="text-gray-400 mb-8">Complete datamined game database — heroes, equipment, monsters, stages, gacha and drop tables.</p>
  <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
    <a href="/heroes" class="bg-dark-card border border-dark-border rounded-xl p-5 hover:border-accent transition group">
      <div class="text-3xl font-bold text-accent">{heroes.length}</div>
      <div class="text-sm text-gray-400 mt-1 group-hover:text-white">Heroes</div>
    </a>
    <a href="/equip" class="bg-dark-card border border-dark-border rounded-xl p-5 hover:border-accent transition group">
      <div class="text-3xl font-bold text-green-400">{equip.length}</div>
      <div class="text-sm text-gray-400 mt-1 group-hover:text-white">Equipment</div>
    </a>
    <a href="/items" class="bg-dark-card border border-dark-border rounded-xl p-5 hover:border-accent transition group">
      <div class="text-3xl font-bold text-purple-400">{items.length}</div>
      <div class="text-sm text-gray-400 mt-1 group-hover:text-white">Items</div>
    </a>
    <a href="/monsters" class="bg-dark-card border border-dark-border rounded-xl p-5 hover:border-accent transition group">
      <div class="text-3xl font-bold text-red-400">{monsters.length}</div>
      <div class="text-sm text-gray-400 mt-1 group-hover:text-white">Monsters</div>
    </a>
  </div>
  <div class="grid md:grid-cols-2 gap-6">
    <section>
      <div class="flex items-center justify-between mb-3">
        <h2 class="text-xl font-semibold">Heroes</h2>
        <a href="/heroes" class="text-xs text-accent hover:underline">View all →</a>
      </div>
      <div class="grid grid-cols-2 sm:grid-cols-3 gap-3">
        {heroes.map((h, i) => (
          <a href={`/heroes/${i}`} class="bg-dark-card border border-dark-border rounded-lg p-3 hover:border-accent transition group">
            <div class={`font-semibold truncate ${qColor[h.row[2]] || "text-gray-200"}`}>{h.name_en || h.name_es || `Hero #${i}`}</div>
            <div class="text-xs text-gray-500 mt-0.5">ID {h.row[0]}</div>
          </a>
        ))}
      </div>
    </section>
    <section>
      <div class="flex items-center justify-between mb-3">
        <h2 class="text-xl font-semibold">Latest Stages</h2>
        <a href="/stages" class="text-xs text-accent hover:underline">View all →</a>
      </div>
      <div class="space-y-2">
        {stages.slice(-12).reverse().map((s) => (
          <a href="/stages" class="bg-dark-card border border-dark-border rounded-lg p-3 flex justify-between items-center hover:border-accent transition">
            <span class="text-sm font-medium">{s[13] || `Stage ${s[0]}`}</span>
            <span class="text-xs text-gray-500">Group {s[4] || "—"}</span>
          </a>
        ))}
      </div>
    </section>
  </div>
</BaseLayout>
INDEXEOF

# Hero listing
cat > src/pages/heroes/index.astro << 'HEROEINDEX'
---
import BaseLayout from '../../layouts/BaseLayout.astro';
import { readFileSync } from 'node:fs';
const heroes = JSON.parse(readFileSync(new URL('../../data/heroes.json', import.meta.url), 'utf-8'));
const qColor = {2:"text-green-400",3:"text-blue-400",4:"text-purple-400",5:"text-orange-400",6:"text-red-400"};
const qName = {1:"Common",2:"Uncommon",3:"Rare",4:"Epic",5:"Legendary",6:"Mythic"};
---
<BaseLayout title="Heroes">
  <h1 class="text-3xl font-bold mb-2">Heroes <span class="text-gray-500 text-lg font-normal">({heroes.length})</span></h1>
  <p class="text-gray-400 mb-6">All playable and NPC characters in War of Genesis: Idle Loot.</p>
  <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
    {heroes.map((h, i) => (
      <a href={`/heroes/${i}`} class="bg-dark-card border border-dark-border rounded-lg p-4 hover:border-accent transition group relative">
        <div class={`font-semibold text-lg ${qColor[h.row[2]] || "text-gray-200"}`}>{h.name_en || h.name_es || `Hero #${i}`}</div>
        {h.name_es && h.name_en !== h.name_es && <div class="text-xs text-gray-500">{h.name_es}</div>}
        <div class="mt-2 flex items-center gap-2 text-xs">
          <span class="bg-dark-bg border border-dark-border rounded px-2 py-0.5 text-gray-400">{qName[h.row[2]] || `Q${h.row[2]}`}</span>
          <span class="bg-dark-bg border border-dark-border rounded px-2 py-0.5 text-gray-400">ID {h.row[0]}</span>
        </div>
      </a>
    ))}
  </div>
</BaseLayout>
HEROEINDEX

# Hero detail
cat > "src/pages/heroes/[id].astro" << 'HEROEOF'
---
import BaseLayout from '../../layouts/BaseLayout.astro';
import { readFileSync } from 'node:fs';
const { id } = Astro.params;
const heroes = JSON.parse(readFileSync(new URL('../../data/heroes.json', import.meta.url), 'utf-8'));
const equip = JSON.parse(readFileSync(new URL('../../data/equip.json', import.meta.url), 'utf-8'));
const hero = heroes[Number(id)];
if (!hero) return Astro.redirect('/heroes');
const r = hero.row;
const name = hero.name_en || hero.name_es || `Hero #${id}`;
const quality = r[2];
const qColor = {2:"text-green-400",3:"text-blue-400",4:"text-purple-400",5:"text-orange-400",6:"text-red-400"};
const qName = {1:"Common",2:"Uncommon",3:"Rare",4:"Epic",5:"Legendary",6:"Mythic"};
const qBorder = {3:"border-blue-400",4:"border-purple-400",5:"border-orange-400",6:"border-red-400"};
const stats = [
  ["ID", r[0]], ["Base Class", r[1]], ["Quality", qName[quality] || quality],
  ["ATK 1", r[10]], ["ATK 2", r[12]], ["DEF", r[13]], ["HP", r[14]],
  ["Critical", r[15]], ["Speed", r[21]], ["Growth", r[26]], ["Active Skill", r[28]],
  ["Passive Skill", r[30]], ["Portrait", r[34] || "—"],
];
---
<BaseLayout title={name}>
  <div class="mb-4">
    <a href="/heroes" class="text-accent text-sm hover:underline">&larr; All Heroes</a>
  </div>
  <div class={`bg-dark-card border ${qBorder[quality] || "border-dark-border"} rounded-xl p-6 max-w-3xl`}>
    <div class="flex items-start justify-between flex-wrap gap-4">
      <div>
        <h1 class={`text-3xl font-bold ${qColor[quality] || "text-gray-200"}`}>{name}</h1>
        {hero.name_es && hero.name_en !== hero.name_es && <p class="text-gray-500">{hero.name_es}</p>}
        <div class="flex gap-2 mt-3 text-xs flex-wrap">
          <span class="bg-dark-bg border border-dark-border rounded px-2 py-1 text-gray-300">{qName[quality] || `Quality ${quality}`}</span>
          <span class="bg-dark-bg border border-dark-border rounded px-2 py-1 text-gray-300">{r[1] || "Unknown class"}</span>
        </div>
      </div>
      <div class="w-24 h-24 rounded-xl bg-gradient-to-br from-accent/30 to-purple-500/30 flex items-center justify-center text-4xl font-black text-white/80">
        {(name[0] || "?").toUpperCase()}
      </div>
    </div>
    <div class="mt-6 grid grid-cols-2 md:grid-cols-3 gap-3 text-sm">
      {stats.map(([label, val]) => (
        <div class="bg-dark-bg/60 border border-dark-border rounded-lg px-3 py-2">
          <div class="text-[11px] uppercase text-gray-500 tracking-wide">{label}</div>
          <div class="font-medium truncate" title={String(val ?? "")}>{val ?? "—"}</div>
        </div>
      ))}
    </div>
  </div>
</BaseLayout>
HEROEOF

# Equip
cat > src/pages/equip.astro << 'EQUIPEOF'
---
import BaseLayout from '../layouts/BaseLayout.astro';
import { readFileSync } from 'node:fs';
const equip = JSON.parse(readFileSync(new URL('../data/equip.json', import.meta.url), 'utf-8'));
const qColor = {2:"text-green-400",3:"text-blue-400",4:"text-purple-400",5:"text-orange-400",6:"text-red-400"};
const qName = {1:"Common",2:"Uncommon",3:"Rare",4:"Epic",5:"Legendary",6:"Mythic"};
const qBg = {2:"bg-green-400/5",3:"bg-blue-400/5",4:"bg-purple-400/5",5:"bg-orange-400/5",6:"bg-red-400/5"};
---
<BaseLayout title="Equipment">
  <h1 class="text-3xl font-bold mb-2">Equipment <span class="text-gray-500 text-lg font-normal">({equip.length})</span></h1>
  <p class="text-gray-400 mb-6">All equippable gear in the game, with quality and stats.</p>
  <div class="overflow-x-auto rounded-xl border border-dark-border">
    <table class="w-full text-sm">
      <thead>
        <tr class="bg-dark-card text-gray-400 text-left">
          <th class="p-3 font-semibold">Name</th>
          <th class="p-3 font-semibold">Quality</th>
          <th class="p-3 font-semibold">ID</th>
          <th class="p-3 font-semibold">Type</th>
          <th class="p-3 font-semibold">Option</th>
          <th class="p-3 font-semibold">Rarity</th>
        </tr>
      </thead>
      <tbody>
        {equip.map((e) => { const r = e.row; return (
          <tr class={`border-t border-dark-border hover:bg-dark-card/60 transition ${qBg[r[16]] || ""}`}>
            <td class={`p-3 font-medium ${qColor[r[16]] || "text-gray-200"}`}>{e.name_en || e.name_es || `#${r[0]}`}</td>
            <td class="p-3 text-gray-400">{qName[r[16]] || r[16] || "—"}</td>
            <td class="p-3 text-gray-500">{r[0]}</td>
            <td class="p-3 text-gray-300">{r[4] || "—"}</td>
            <td class="p-3 text-gray-400">{r[9] || "—"}</td>
            <td class="p-3 text-gray-500">{r[20] || "—"}</td>
          </tr>); })}
      </tbody>
    </table>
  </div>
</BaseLayout>
EQUIPEOF

# Items
cat > src/pages/items.astro << 'ITEMSEOF'
---
import BaseLayout from '../layouts/BaseLayout.astro';
import { readFileSync } from 'node:fs';
const items = JSON.parse(readFileSync(new URL('../data/items.json', import.meta.url), 'utf-8'));
---
<BaseLayout title="Items">
  <h1 class="text-3xl font-bold mb-2">Items <span class="text-gray-500 text-lg font-normal">({items.length})</span></h1>
  <p class="text-gray-400 mb-6">Consumables, materials and quest items.</p>
  <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
    {items.map((item) => (
      <div class="bg-dark-card border border-dark-border rounded-lg p-4 hover:border-accent transition">
        <div class="font-semibold">{item.name_en || item.name_es || `#${item.row[0]}`}</div>
        {item.name_es && item.name_en !== item.name_es && <div class="text-xs text-gray-500">{item.name_es}</div>}
        <div class="mt-2 flex gap-2 text-xs">
          <span class="bg-dark-bg border border-dark-border rounded px-2 py-0.5 text-gray-400">ID {item.row[0]}</span>
          <span class="bg-dark-bg border border-dark-border rounded px-2 py-0.5 text-gray-400">Price {item.row[5] ?? 0}</span>
        </div>
      </div>
    ))}
  </div>
</BaseLayout>
ITEMSEOF

# Weapons
cat > src/pages/weapons.astro << 'WEOF'
---
import BaseLayout from '../layouts/BaseLayout.astro';
import { readFileSync } from 'node:fs';
const weapons = JSON.parse(readFileSync(new URL('../data/weapons.json', import.meta.url), 'utf-8'));
---
<BaseLayout title="Weapons">
  <h1 class="text-3xl font-bold mb-2">Weapons <span class="text-gray-500 text-lg font-normal">({weapons.length})</span></h1>
  <p class="text-gray-400 mb-6">All weapon data from the weapon table.</p>
  <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3">
    {weapons.map((w) => (
      <div class="bg-dark-card border border-dark-border rounded-lg p-4 hover:border-accent transition">
        <div class="font-semibold truncate">{w.name_en || w.name_es || `#${w.row[0]}`}</div>
        <div class="mt-2 flex gap-2 text-xs">
          <span class="bg-dark-bg border border-dark-border rounded px-2 py-0.5 text-gray-400">ID {w.row[0]}</span>
        </div>
      </div>
    ))}
  </div>
</BaseLayout>
WEOF

# Pets
cat > src/pages/pets.astro << 'PETEOF'
---
import BaseLayout from '../layouts/BaseLayout.astro';
import { readFileSync } from 'node:fs';
const pets = JSON.parse(readFileSync(new URL('../data/pets.json', import.meta.url), 'utf-8'));
---
<BaseLayout title="Pets">
  <h1 class="text-3xl font-bold mb-2">Pets <span class="text-gray-500 text-lg font-normal">({pets.length})</span></h1>
  <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
    {pets.map((p) => (
      <div class="bg-dark-card border border-dark-border rounded-lg p-4 hover:border-accent transition">
        <div class="font-semibold">{p.name_en || p.name_es || `#${p.row[0]}`}</div>
        {p.name_es && p.name_en !== p.name_es && <div class="text-xs text-gray-500">{p.name_es}</div>}
        <div class="mt-2 text-xs text-gray-500">ID {p.row[0]}</div>
      </div>
    ))}
  </div>
</BaseLayout>
PETEOF

# Machina
cat > src/pages/machina.astro << 'MACHEOF'
---
import BaseLayout from '../layouts/BaseLayout.astro';
import { readFileSync } from 'node:fs';
const machina = JSON.parse(readFileSync(new URL('../data/machina.json', import.meta.url), 'utf-8'));
---
<BaseLayout title="Machina">
  <h1 class="text-3xl font-bold mb-2">Machina <span class="text-gray-500 text-lg font-normal">({machina.length})</span></h1>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
    {machina.map((m) => (
      <div class="bg-dark-card border border-dark-border rounded-lg p-4 hover:border-accent transition">
        <div class="font-semibold">{m.name_en || m.name_es || `#${m.row[0]}`}</div>
        {m.name_es && m.name_en !== m.name_es && <div class="text-xs text-gray-500">{m.name_es}</div>}
        <div class="mt-2 text-xs text-gray-500">ID {m.row[0]}</div>
      </div>
    ))}
  </div>
</BaseLayout>
MACHEOF

# Monsters
cat > src/pages/monsters.astro << 'MOBEOF'
---
import BaseLayout from '../layouts/BaseLayout.astro';
import { readFileSync } from 'node:fs';
const monsters = JSON.parse(readFileSync(new URL('../data/monsters.json', import.meta.url), 'utf-8'));
---
<BaseLayout title="Monsters">
  <h1 class="text-3xl font-bold mb-2">Monsters <span class="text-gray-500 text-lg font-normal">({monsters.length})</span></h1>
  <p class="text-gray-400 mb-6">All enemy data, showing the first 300 for build size.</p>
  <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3">
    {monsters.slice(0, 300).map((m) => (
      <div class="bg-dark-card border border-dark-border rounded-lg p-3 hover:border-accent transition">
        <div class="text-sm font-medium truncate">{m[35] ? String(m[35]).replace(/_/g," ") : `Monster #${m[0]}`}</div>
        <div class="text-xs text-gray-500 mt-1">ID {m[0]}</div>
      </div>
    ))}
  </div>
  {monsters.length > 300 && <p class="text-gray-500 mt-4">Showing 300 of {monsters.length} monsters.</p>}
</BaseLayout>
MOBEOF

# Stages
cat > src/pages/stages.astro << 'STAGEEOF'
---
import BaseLayout from '../layouts/BaseLayout.astro';
import { readFileSync } from 'node:fs';
const stages = JSON.parse(readFileSync(new URL('../data/stages.json', import.meta.url), 'utf-8'));
---
<BaseLayout title="Stages">
  <h1 class="text-3xl font-bold mb-2">Stages <span class="text-gray-500 text-lg font-normal">({stages.length})</span></h1>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
    {stages.map((s) => (
      <div class="bg-dark-card border border-dark-border rounded-lg p-4 hover:border-accent transition">
        <div class="font-semibold">{s[13] || `Stage ${s[0]}`}</div>
        <div class="mt-2 flex gap-2 text-xs">
          <span class="bg-dark-bg border border-dark-border rounded px-2 py-0.5 text-gray-400">ID {s[0]}</span>
          <span class="bg-dark-bg border border-dark-border rounded px-2 py-0.5 text-gray-400">Type {s[2]}</span>
          <span class="bg-dark-bg border border-dark-border rounded px-2 py-0.5 text-gray-400">Group {s[4]}</span>
        </div>
      </div>
    ))}
  </div>
</BaseLayout>
STAGEEOF

# Skills
cat > src/pages/skills.astro << 'SKILLEOF'
---
import BaseLayout from '../layouts/BaseLayout.astro';
import { readFileSync } from 'node:fs';
const skills = JSON.parse(readFileSync(new URL('../data/skills.json', import.meta.url), 'utf-8'));
const typeNames = {0:"Unknown",1:"Unknown",2:"Unknown",3:"Melee",4:"Ranged",5:"Magic",6:"Heal",7:"Passive"};
const classNames = {1:"Warrior",2:"Archer",3:"Knight",4:"Priest",5:"Mage",6:"Ninja",7:"Berserker",8:"Templar"};
---
<BaseLayout title="Skills">
  <h1 class="text-3xl font-bold mb-2">Skills <span class="text-gray-500 text-lg font-normal">({skills.length})</span></h1>
  <div class="overflow-x-auto rounded-xl border border-dark-border">
    <table class="w-full text-sm">
      <thead><tr class="bg-dark-card text-gray-400 text-left">
        <th class="p-3 font-semibold">Skill</th><th class="p-3 font-semibold">Class</th><th class="p-3 font-semibold">Type</th><th class="p-3 font-semibold">Slot</th><th class="p-3 font-semibold">Range</th><th class="p-3 font-semibold">Cooltime</th>
      </tr></thead>
      <tbody>
        {skills.map((s) => (
          <tr class="border-t border-dark-border hover:bg-dark-card/60 transition">
            <td class="p-3 font-medium">Skill #{s[0]}</td>
            <td class="p-3 text-gray-400">{classNames[s[1]] || s[1] || "—"}</td>
            <td class="p-3 text-gray-300">{typeNames[s[7]] || s[7] || "—"}</td>
            <td class="p-3 text-gray-500">{s[2] || "—"}</td>
            <td class="p-3 text-gray-400">{(s[9] ?? s[11]) || "—"}</td>
            <td class="p-3 text-gray-400">{s[17] || "—"}</td>
          </tr>
        ))}
      </tbody>
    </table>
  </div>
</BaseLayout>
SKILLEOF

# Passive skills
cat > src/pages/passiveskills.astro << 'PSKEOF'
---
import BaseLayout from '../layouts/BaseLayout.astro';
import { readFileSync } from 'node:fs';
const ps = JSON.parse(readFileSync(new URL('../data/passiveskills.json', import.meta.url), 'utf-8'));
const typeNames = {3:"Melee",4:"Ranged",5:"Magic",6:"Heal"};
---
<BaseLayout title="Passive Skills">
  <h1 class="text-3xl font-bold mb-2">Passive Skills <span class="text-gray-500 text-lg font-normal">({ps.length})</span></h1>
  <div class="grid grid-cols-2 md:grid-cols-3 gap-3">
    {ps.slice(0, 300).map((s) => (
      <div class="bg-dark-card border border-dark-border rounded-lg p-3 hover:border-accent transition">
        <div class="text-sm font-medium">Passive #{s[0]}</div>
        <div class="text-xs text-gray-500 mt-1">{typeNames[s[7]] || "Unknown"} · Lv.{s[2]} · Pos {s[5]}</div>
      </div>
    ))}
  </div>
  {ps.length > 300 && <p class="text-gray-500 mt-4">Showing 300 of {ps.length}.</p>}
</BaseLayout>
PSKEOF

# Abilities
cat > src/pages/abilities.astro << 'ABEOF'
---
import BaseLayout from '../layouts/BaseLayout.astro';
import { readFileSync } from 'node:fs';
const abilities = JSON.parse(readFileSync(new URL('../data/abilities.json', import.meta.url), 'utf-8'));
---
<BaseLayout title="Abilities">
  <h1 class="text-3xl font-bold mb-2">Abilities <span class="text-gray-500 text-lg font-normal">({abilities.length})</span></h1>
  <div class="grid grid-cols-2 md:grid-cols-3 gap-3">
    {abilities.map((a) => (
      <div class="bg-dark-card border border-dark-border rounded-lg p-3 hover:border-accent transition">
        <div class="text-sm font-medium">Ability #{a[0]}</div>
        <div class="text-xs text-gray-500 mt-1">Type {a[6] || "—"}</div>
      </div>
    ))}
  </div>
</BaseLayout>
ABEOF

# Drops
cat > src/pages/drops.astro << 'DROPEOF'
---
import BaseLayout from '../layouts/BaseLayout.astro';
import { readFileSync } from 'node:fs';
const drops = JSON.parse(readFileSync(new URL('../data/drops.json', import.meta.url), 'utf-8'));
const items = JSON.parse(readFileSync(new URL('../data/items.json', import.meta.url), 'utf-8'));
const equip = JSON.parse(readFileSync(new URL('../data/equip.json', import.meta.url), 'utf-8'));
const itemName = (num) => {
  const it = items.find(i => i.row[0] === num);
  if (it) return it.name_en || it.name_es || `Item #${num}`;
  const eq = equip.find(i => i.row[0] === num);
  if (eq) return eq.name_en || eq.name_es || `Equip #${num}`;
  return `#${num}`;
};
---
<BaseLayout title="Drop Tables">
  <h1 class="text-3xl font-bold mb-2">Drop Tables <span class="text-gray-500 text-lg font-normal">({drops.length} entries)</span></h1>
  <p class="text-gray-400 mb-6">Item drop rates by droplist group.</p>
  <div class="overflow-x-auto rounded-xl border border-dark-border">
    <table class="w-full text-sm">
      <thead><tr class="bg-dark-card text-gray-400 text-left">
        <th class="p-3 font-semibold">DropList</th><th class="p-3 font-semibold">Item</th><th class="p-3 font-semibold">Count</th><th class="p-3 font-semibold">Rate</th><th class="p-3 font-semibold">Group</th>
      </tr></thead>
      <tbody>
        {drops.slice(0, 400).map((d) => (
          <tr class="border-t border-dark-border hover:bg-dark-card/60 transition">
            <td class="p-3 text-gray-400">{d[10]}</td>
            <td class="p-3 font-medium">{itemName(d[4])}</td>
            <td class="p-3 text-gray-300">{d[5]}</td>
            <td class="p-3 text-gray-400">{d[6] !== undefined && d[6] !== null && d[6] !== 0 ? `${d[6]}%` : "—"}</td>
            <td class="p-3 text-gray-500">{d[0]}</td>
          </tr>
        ))}
      </tbody>
    </table>
  </div>
  <p class="text-gray-500 mt-4">Showing 400 of {drops.length} entries.</p>
</BaseLayout>
DROPEOF

# Gacha
cat > src/pages/gacha.astro << 'GACHAEOF'
---
import BaseLayout from '../layouts/BaseLayout.astro';
import { readFileSync } from 'node:fs';
const gacha = JSON.parse(readFileSync(new URL('../data/gacha.json', import.meta.url), 'utf-8'));
const list = JSON.parse(readFileSync(new URL('../data/gachalist.json', import.meta.url), 'utf-8'));
const items = JSON.parse(readFileSync(new URL('../data/items.json', import.meta.url), 'utf-8'));
const itemName = (num) => { const it = items.find(i => i.row[0] === num); return it ? (it.name_en || it.name_es || `#${num}`) : `#${num}`; };
---
<BaseLayout title="Gacha">
  <h1 class="text-3xl font-bold mb-2">Gacha <span class="text-gray-500 text-lg font-normal">({gacha.length} pools, {list.length} items)</span></h1>
  <div class="grid md:grid-cols-2 gap-4">
    {gacha.slice(0, 40).map((g) => {
      const poolItems = list.filter(l => l[0] === g[0]);
      return (
      <div class="bg-dark-card border border-dark-border rounded-xl p-4">
        <div class="font-semibold mb-2">Pool #{g[0]}</div>
        <div class="flex gap-2 text-xs mb-3">
          <span class="bg-dark-bg border border-dark-border rounded px-2 py-0.5 text-gray-400">Entries {poolItems.length}</span>
        </div>
        {poolItems.length > 0 && <div class="space-y-1.5">
          {poolItems.slice(0, 8).map((pi) => (
            <div class="flex justify-between items-center text-xs">
              <span class="text-gray-300">{itemName(pi[2] ?? pi[1])}</span>
              <span class="text-gray-500">{(pi[3] !== undefined && pi[3] !== null && pi[3] !== 0) ? `${pi[3]}%` : "—"}</span>
            </div>
          ))}
          {poolItems.length > 8 && <div class="text-[11px] text-gray-600">+{poolItems.length - 8} more</div>}
        </div>}
      </div>);
    })}
  </div>
</BaseLayout>
GACHAEOF

# Fusion
cat > src/pages/fusion.astro << 'FUSIONEOF'
---
import BaseLayout from '../layouts/BaseLayout.astro';
import { readFileSync } from 'node:fs';
const fusion = JSON.parse(readFileSync(new URL('../data/fusion.json', import.meta.url), 'utf-8'));
const equip = JSON.parse(readFileSync(new URL('../data/equip.json', import.meta.url), 'utf-8'));
const eName = (num) => { const e = equip.find(x => x.row[0] === num); return e ? (e.name_en || e.name_es || `#${num}`) : `#${num}`; };
---
<BaseLayout title="Fusion">
  <h1 class="text-3xl font-bold mb-2">Fusion <span class="text-gray-500 text-lg font-normal">({fusion.length} recipes)</span></h1>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
    {fusion.map((f) => (
      <div class="bg-dark-card border border-dark-border rounded-lg p-3 hover:border-accent transition">
        <div class="text-sm font-medium">{eName(f[0])}</div>
        <div class="text-xs text-gray-500 mt-0.5">Result {eName(f[2] ?? f[1])} — Count {f[3] ?? "—"}</div>
      </div>
    ))}
  </div>
</BaseLayout>
FUSIONEOF

# 404
cat > src/pages/404.astro << 'FOUROF'
---
import BaseLayout from '../layouts/BaseLayout.astro';
---
<BaseLayout title="Not Found">
  <div class="text-center py-20">
    <div class="text-6xl font-black text-gray-700 mb-4">404</div>
    <p class="text-gray-400 mb-6">Page not found.</p>
    <a href="/" class="text-accent hover:underline">← Back to home</a>
  </div>
</BaseLayout>
FOUROF

echo "[6/7] Build..."
npm run build 2>&1 | tail -25

echo "[7/7] Deploy to Cloudflare Pages..."
npx wrangler pages deploy dist --project-name=wogindex --branch=main 2>&1 | tail -20

echo "BUILD COMPLETE — deploy attempt finished"