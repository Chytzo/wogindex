# WoG Index — Build Instructions

## Goal
Build a wiki site like tbhindex.com for **War of Genesis: Idle Loot**.
Static site with Astro 7 + Tailwind, deploy to Cloudflare Pages as **wogindex**.

## Data (already in ./data/ after `unzip wog_wiki_data.zip`)
- `datos/*.json` — 20 category JSONs: heroes, items, equip, weapons, machina, pets, monsters, stages, skills, passiveskills, abilities, abilityactions, drops, droplists, gacha, gachalist, fusion, fusionlevel, passiveitems, locales
- `locales.json` — 3,479 localized strings (17 languages: ko/en/ru/fr/es/it/pl/de/pt/id/th/ja/vi/zh/tr/uk/zh_TW). Key `"1"` = English, `"4"` = Spanish.
- `schema.md` — first-row dump of every table with column types

## Key Data Structures
- **heroes**: 33 rows. `row[37]` = locale key, `{name_en, name_es}` resolved. `row[34]` = portrait filename.
- **items**: 207 rows. `row[18]` = locale key. `row[5]` = price.
- **equip**: 1,872 rows. `row[23]` = locale key. `row[16]` = quality.
- **weapons**: 482 rows. `row[6]` = locale key guess (verify against locales).
- **machina**: 5 rows. `row[13]` = locale key.
- **pets**: 90 rows. `row[24]` = locale key.
- **monsters**: 1,800 rows. Names are literal strings in data, not locale keys.
- **stages**: 400 rows. Names are literal strings.
- **skills**: 1,160 rows. No locale text. `row[7]` = SkillType (3=melee, 4=ranged, 5=magic, 6=heal). `row[11]` = MaxCastRange, `row[17]` = MaxCooltime.
- **passiveskills**: 1,679 rows. `row[7]` = SkillType. `row[5]` = SkillPosition.
- **abilities**: 159 rows. `row[6]` = AbilityType.
- **drops**: 12,000 rows. `row[10]` = DropListID (links to droplists). `row[4]` = ItemNumber. `row[5]` = Count.
- **droplists**: 1,232 rows. `row[0]` = DropListID.
- **gacha**: 684 rows. Gacha pools.
- **gachalist**: 1,658 rows. Gacha items.
- **fusion**: 150 rows. `row[0]` = EquipNumber.
- **fusionlevel**: 600 rows. `row[0]` = FusionNumber.

## Tech Stack
- **Framework**: Astro 7 (`npm create astro@latest`)
- **Styling**: Tailwind CSS (dark theme like TBH)
- **Data**: Static JSONs in `public/datos/` loaded at build + runtime
- **Build**: `npm run build` → `dist/`
- **Deploy**: `npx wrangler pages deploy dist --project-name=wogindex --branch=main`

## Site Structure (mirror TBH format)
### Header
- Logo "WoG Index" + subtitle "War of Genesis: Idle Loot Wiki"
- Search bar (client-side fuzzy search over all entities by name_en/name_es)

### Sidebar Nav (4 sections)
1. **Heroes & Combat** → /heroes, /skills, /monsters, /abilities
2. **Gear & Items** → /equip, /items, /weapons, /machina, /pets
3. **Stages & Drops** → /stages, /drops, /gacha
4. **Tools & Data** → /fusion, /passiveskills

### Pages
- `/` — Homepage with hero grid + quick stats (33 heroes, 1,872 equip, 207 items, etc.)
- `/heroes` — Grid of hero cards with portrait, name, quality
- `/heroes/[id]` — Hero detail: stats, skills, equipment, portrait
- `/equip` — Filterable table: name, quality, type, stats
- `/items` — Item list with type icons
- `/monsters` — Monster grid with stats
- `/stages` — Stage progression tree
- `/drops` — Drop table viewer by stage/group
- `/gacha` — Gacha pool rates and items
- `/fusion` — Fusion recipes
- `/skills` — Skill list filtered by class

### UI Details
- Dark theme (background #0f1117, cards #1a1d29, accent #3b82f6 blue)
- Quality colors: Common=gray, Uncommon=green, Rare=blue, Epic=purple, Legendary=orange, Mythic=red
- Responsive grid layouts
- Client-side filtering/sorting on every list page
- Stats bars for numerical values

## Implementation Steps (Hermes, follow this order)
1. `cd ~/Proyectos/wog-wiki && mkdir -p datos && unzip wog_wiki_data.zip`
2. `npm create astro@latest . -- --template minimal --typescript strict --no-git --no-install` (answer prompts)
3. `npm install && npm install tailwindcss @astrojs/tailwind`
4. Configure astro.config.mjs with `site: 'https://wogindex.com'` and tailwind integration
5. Create `src/layouts/BaseLayout.astro` — dark theme, sidebar nav, header with search
6. Create `src/pages/index.astro` — homepage with hero grid + stats
7. Create `src/pages/heroes/index.astro` — hero card grid
8. Create `src/pages/heroes/[id].astro` — hero detail with dynamic routing
9. Create `src/pages/equip.astro` — equipment table with filters
10. Create `src/pages/items.astro` — items grid
11. Create `src/pages/monsters.astro` — monster grid
12. Create `src/pages/stages.astro` — stage progression
13. Create `src/pages/drops.astro` — drop table viewer
14. Create `src/pages/gacha.astro` — gacha pools
15. Create `src/pages/fusion.astro` — fusion recipes
16. Create `src/pages/skills.astro` — skill list
17. Create `src/components/SearchBar.astro` — fuzzy search component
18. Create `src/components/DataTable.astro` — reusable sortable/filterable table
19. `npm run build` — verify no errors
20. `npx wrangler pages deploy dist --project-name=wogindex --branch=main` — deploy
21. Verify at https://wogindex.pages.dev (Cloudflare Pages preview URL)

## Notes
- All locale lookups use `locales[key]["1"]` for English as default language
- Monster/stage names are hardcoded strings, not locale lookups
- The 37MB resolved_tables.json contains ALL data; use the smaller per-category JSONs in datos/ for the site
- Equipment has 1,872 entries — use virtual scrolling or pagination
- Hero portraits are referenced by filename in `row[34]` but actual images are not extracted (use placeholder silhouettes or extract from game assets separately)
