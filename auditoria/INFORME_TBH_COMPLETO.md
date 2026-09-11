# INFORME COMPLETO: TBH Index vs WOG Index — Catálogo de Features

**Fecha:** 11/09/2026  
**Analista:** ACORAY  
**Contexto:** WOG Index (wogindex.com) es clon de TBH Index (tbhindex.com) para "War of Genesis: Idle Loot"  
**Sitio analizado:** https://tbhindex.com — 4,128 URLs en sitemap, SPA renderizada con JS  

---

## 1. MAPA COMPLETO DE TBH INDEX

### 1.1 Estructura de rutas (del sitemap.xml)

```
/                           → Home (SPA, renderizada con JS)
/market                     → Market de precios en vivo (Steam Market data)
/ranking                    → Rankings globales (4,018 jugadores)
/ranking/power              → Power Rankings
/ranking/stats              → Stats Leaderboards
/builds                     → Build Planner (comunidad)
/community                  → Hub comunitario
/tier-lists                 → Tier lists (crear/compartir)
/guides                     → Guías escritas por players
/supporter-wall             → Muro de patrocinadores
/creators                   → Rastreo de créateurs de contenido
/about / privacy / terms / contact → páginas legales

/wiki                       → Wiki (4,128 páginas de documentación)
/wiki/roadmap               → Hoja de ruta del juego
/wiki/grades                → 10 rangos de rareza (Common→Cosmic)
/wiki/material-effects      → 79 efectos de materiales
/wiki/materials             → Catálogo de materiales
/wiki/unique-modifiers      → 36 modificadores únicos
/wiki/stage-power           → HP de enemigos por etapa
/wiki/stages                → 189 etapas en 4 dificultades
/wiki/monsters              → 78 monstruos con stats
/wiki/pets                  → 8 pets con bonuses
/wiki/runes                 → 241 runas con valores por nivel (242 páginas)
/wiki/sockets               → Sistema de zócalos
/wiki/inscription           → Inscripción (zócalo más raro)
/wiki/extract               → Extracción (recoste de zócalos)
/wiki/chests                → 112 loot tables de cajas
/wiki/chest-cooldown-explained → Cooldowns reales (2.05s es erróneo)
/wiki/chest-tracker         → Cajas por hora (optimizador)
/wiki/corrosion             → Corrosión por grado
/wiki/contamination         → Contaminación (drains reales)
/wiki/offering              → Offering (odds: las tablas públicas erran)
/wiki/cube                  → Sistema del cubo (guía completa)
/wiki/cube-exp              → Cube EXP Calculator
/wiki/synthesis             → Síntesis (odds reales de grade-up)
/wiki/crafting              → Crafting (odds reales por tier)
/wiki/alchemy               → Alquimia (oro + cube EXP exactos)
/wiki/alchemy-ranking       → Ranking de items a fundir para oro
/wiki/alchemy-gold          → Alchemy Gold Calculator
/wiki/drop-finder           → ¿Dónde aparece cada item?
/wiki/combat-lab            → DPS & EHP del héroe
/wiki/skill-priority        → Orden completo de casts por clase
/wiki/popular-skill-tree    → Árbol de habilidades popular
/wiki/farming               → Calculator: mejor etapa para farming
/wiki/stat-caps             → Stat caps (dodge = 75%, no 60%)
/wiki/stats                 → Stats explicados con scaling real
/wiki/buffs                 → 29 buffs & debuffs
/wiki/status-effects        → Status effects (penalizaciones reales)
/wiki/compare               → Compare items: cuál es mejor
/wiki/best-in-slot          → BiS por ranura
/wiki/party-composition     → Combinaciones de héroes más usadas
/wiki/meta-attributes       → Stats más usados en el meta
/wiki/achievements          → Logros con tasas globales de unlock
/wiki/chat                  → Sistema de chat
/wiki/mailbox               → Buzón (donde van compras del market)
/wiki/patrol                → Patrulla
/wiki/decoration            → Decoración
/wiki/trade-ship            → Barco de comercio
/wiki/synthesis             → Síntesis
/wiki/stash                 → Inspector de stash (privado, requiere save)
/wiki/drive                 → Drive (mismo shell que stash, no indexado)
/wiki/mechanics             → Mecánicas generales

/wiki/skills/               → 43 subclases de habilidades con páginas individuales
  /hunter/charge-trap, /crossbow-turret, /explosive-bolt, /frost-bolt, /quick-loader, /shock-bolt
  /knight/aegis-field, /piercing-thrust, /retribution-strike, /sacred-blade, /shield-charge, /unyielding-will
  /priest/blessing-of-might, /blessing-of-warding, /heal, /resurrection, /sanctuary, /wrath-of-heaven
  /ranger/arrow-rain, /piercing-arrow, /rapid-fire, /scatter-shot, /skewer-shot, /swift-surge
  /slayer/axe-spin, /bloodlust, /commander-s-cry, /crushing-blow, /ground-slam, /slam-jump
  /sorcerer/fireball, /flame-hydra, /ice-orb, /lightning, /meteor-strike, /snowstorm

/wiki/gear/                 → 1,577 páginas de gear individual
/wiki/runes/rune-of-...    → 242 páginas de runas individuales
/wiki/materials/           → 134 páginas de materiales
/wiki/chests/              → 115 páginas de chests
/wiki/monsters/            → 75 páginas de monstruos
/wiki/trade-ship           → 1 página
/wiki/synthesis            → 1 página
/wiki/... (varios singulares)

Calculators (herramientas):
  /calculators/crafting         → Calculadora de crafting con odds reales
  /calculators/exp-optimizer    → Cube Planner: optimizar nivel (título "Cube Planner")
  /calculators/soulstone        → Soulstone Calculator: planes de runs de boss
  /calculators/offering         → Offering Calculator: odds de coins
  /calculators/synthesis        → Synthesis Calculator: odds exactas
  /calculators/synthesis-cost   → Synth Cost Calculator: materiales necesarios

Simulators:
  /simulators/cast-speed-simulator → Cast Speed Simulator: combo héroe/habilidad con timer visual
  /simulators/chest-simulator      → Chest Simulator: 114 cajas, click-to-open, live drop feed

MORE CALCULATORS (mostrador dropdown):
  Alchemy Gold Calculator
  Damage Taken Calculator
  Combat Lab
  Farming Calculator
  Best-in-Slot Finder
  Chest Optimizer
  Drop Finder
  Rune Planner
  Meta Sockets
  Meta Gear
  Meta Heroes

Multi-idioma (22): en, pt, es, ru, zh-Hans, ja, ko, fr, de, tr, pl, it, th, uk, zh-TW, id, vi, fil, ms, + x-default
```

---

## 2. ANÁLISIS DETALLADO POR CATEGORÍA

### 2.1 MARKET (/market)

**Qué hace:** Catálogo de precios en vivo de todos los items del juego, actualizado cada pocos minutos. Usa datos de Steam Market (instant-sell / highest buy order). Muestra valor total del mercado (€6.6M+), overview por grade, "best time to buy", y tabla de precios por item con todos los grades.

**Inputs:** Ninguno (datos server-side). Filtros: grade, tipo de item.

**Outputs:** Tabla de precios con steam market data. Busca items individuales en /market/item.

**Datos necesarios:** 
- Lista completa de items del juego
- Precios de Steam Market (requiere scraping/API de Steam — NO tenemos contrapartida en WOG a menos que esté en Steam)
- Grade de cada item

**Nuestros datos JSON:** Tenemos `items` y `gacha`/`gachalist` — suficiente para el catálogo estático.

**Factible en Astro estático:** 
- **SÍ (parcial):** Catálogo de items con precios estáticos es fácil. 
- **PARCIAL:** Precios en vivo requieren servicio externo o scraping; si WOG no está en Steam, hay que crear mecanismo propio (ej: precios de players, mercado interno del juego si existe). Si WOG NO tiene mercado real con precios de players, este feature es irrelevante o hay que replantearlo.

**Verdict:** Si WOG no está en steam ni tiene mercado player-to-player, el market como TBH es irrelevante. Si hay mercado in-game, hacer catálogo estático del valor estimado de cada item.

---

### 2.2 CALCULADORES

#### 2.2.1 Crafting Calculator (/calculators/crafting)

**Qué hace:** Calcula odds reales de crafting por tier. El jugador elige materiales/grade y la calculadora muestra la probabilidad real de obtener cada grade de salida. "Cómo funciona en Task Bar Hero" — explica el sistema antes de las herramientas.

**Inputs:** Materiales de entrada (tipo, cantidad, grade de sourced materials), grade objetivo

**Outputs:** Odds de cada grade de output por inheritance percentage. Probabilidad real (no las tablas públicas erróneas).

**Datos necesarios:** Tabla de odds de crafting por combinación de materials y grades. Mecánica de inheritance.

**JSON WOG:** Necesitamos datos de crafting (nuestro `fusion` podría ser similar, pero crafting y fusion son distintos). Revisar si tenemos crafting data. `fusion` y `fusionlevel` existen — verificar equivalencia.

**Factible:** SÍ — cálculo estático con datos del juego. Requiere conocer las odds exactas del juego (datamining o pruebas en-game).

---

#### 2.2.2 Cube Exp Optimizer / EXP Planner (/calculators/exp-optimizer)

**Título real:** "Task Bar Hero Cube Planner: Level Fast" — es un planner de nivel para el cubo.

**Qué hace:** Planifica cómo subir de nivel el cubo eficientemente. Calcula cuánto EXP obtienes por acción (cube exp) y optimiza la secuencia de operaciones para level-up rápido.

**Inputs:** Nivel actual del cubo, objetivo de nivel, recursos disponibles (items para usar en cube)

**Outputs:** Secuencia óptima de operaciones, coste en resources, tiempo estimado, EXP total

**Datos necesarios:** Tabla de cube EXP por operación (qué acción da cuánto EXP), scaling de costes, curve de nivel.

**JSON WOG:** Dependiendo de si WOG tiene "cube" o sistema equivalente de mejora de equipo. Nuestro `gacha` puede ser similar. Analizar equivalencia.

**Factible:** SÍ — con datos de la curva de EXP del juego.

---

#### 2.2.3 Soulstone Calculator (/calculators/soulstone)

**Qué hace:** Planifica runs de boss para optimizar uso de soulstone. Calcula cuántas soulstones necesitas para alcanzar un objetivo (mortalidad de boss con odds dadas) y cuándo usarlas.

**Inputs:** Tipo de boss, número de intentos, probabilidad de éxito por run, número de soulstones disponibles

**Outputs:** Probabilidad de éxito con N soulstones, recomendación de cuándo usarlas, expected value

**Datos necesarios:** Odds de defeat por tipo de boss, mecánica de soulstone (cuándo se consume, qué hace)

**JSON WOG:** Necesitamos datos de bosses y mecánica de soulstones. Revisar si WOG tiene sistema equivalente.

**Factible:** SÍ — cálculo probabilístico estático.

---

#### 2.2.4 Offering Calculator (/calculators/offering)

**Qué hace:** Calcula odds reales de offering (coins/ofrendas). Las tablas públicas están equivocadas; TBH usa datos datamined reales. "Offering: how it works in Task Bar Hero" — explica el sistema.

**Inputs:** Número de ofrendas, tipo de offering, recursos disponibles

**Outputs:** Odds de cada resultado, expected value en resources/coins

**Datos necesarios:** Odds reales de cada outcome de offering por nivel/tipo

**JSON WOG:** Dependiendo de si WOG tiene sistema de offering. Revisar.

**Factible:** SÍ — con datos reales.

---

#### 2.2.5 Synthesis Calculator (/calculators/synthesis)

**Qué hace:** Calcula odds exactas de synthesis (grade-up de items). "Synthesis: how it works in Task Bar Hero" con las odds reales.

**Inputs:** Item base, grade actual, materiales de síntesis, tipo de síntesis

**Outputs:** Odds de grade-up, odds de downgrade, odds de failure, expected value

**Datos necesarios:** Tabla de odds de síntesis por combinación

**JSON WOG:** Nuestro `fusion` podría ser equivalente. Verificar.

**Factible:** SÍ.

---

#### 2.2.6 Synthesis Cost Calculator (/calculators/synthesis-cost)

**Qué hace:** Calcula materiales necesarios para una síntesis. "Synth Cost: Synthesis turn" — calcula el coste en materiales de una operación de síntesis.

**Inputs:** Item a sintetizar, grade de origen, grade objetivo

**Outputs:** Materiales exactos necesarios, coste total, si es viable económicamente

**Datos necesarios:** Coste de síntesis por grade level

**JSON WOG:** Necesitamos data de costes de síntesis/fusión.

**Factible:** SÍ.

---

#### 2.2.7 Alchemy Gold Calculator (MORE CALCULATORS)

**Qué hace:** Calcula cuánto oro obtienes al fundir (melt) cada item en alquimia. Ranking de qué items vale la pena fundir.

**Inputs:** Item a fundir, grade, cantidad

**Outputs:** Oro obtenido, comparison con valor de mercado (si es rentable fundir vs vender)

**Datos necesarios:** Oro por melt por item-grade

**JSON WOG:** Si WOG tiene sistema de alquimia/melt.

**Factible:** SÍ.

---

#### 2.2.8 Damage Taken Calculator (MORE CALCULATORS)

**Qué hace:** Calcula cuánto daño absorbe tu héroe con su defensa/estats, y cuánto daño soporta antes de morir (EHP).

**Inputs:** Stats del héroe (HP, defensa, resistencia), stats del monster, buffs/debuffs activos, grade del gear

**Outputs:** Daño por hit, ticks de daño que sobrevives, EHP total, vulnerabilidad a status effects

**Datos necesarios:** Fórmula de cálculo de daño del juego (scaling, caps, resistencias), stats de monsters, buffs/debuffs

**JSON WOG:** Necesitamos: fórmula de daño del juego, `monsters` (lo tenemos), stats de héroes (lo tenemos), `buffs` y `status-effects` (quizá no los tenemos aún), modificadores de gear

**Factible:** SÍ pero requiere modelar la fórmula de daño del juego (puede ser compleja).

---

#### 2.2.9 Combat Lab (/wiki/combat-lab)

**Qué hace:** Mismo que Damage Taken Calculator pero más completo: DPS del héroe + EHP contra un monster específico. Calcula dps de skills + daño del héroe + crit + scaling.

**Inputs:** Héroe, skills equipadas, gear, monster objetivo

**Outputs:** DPS total, tiempo para matar, EHP, vulnerabilidades, recomendaciones de mejora

**Datos necesarios:** Fórmula de daño completa, stats de skills, scaling de habilidades, stats de monsters

**JSON WOG:** `heroes` (lo tenemos), `skills` (lo tenemos), `monsters` (lo tenemos), pero necesitamos la fórmula de daño — es el dato crítico faltante.

**Factible:** SÍ pero difícil sin conocer la fórmula exacta de daño de WOG.

---

#### 2.2.10 Farming Calculator (/wiki/farming)

**Qué hace:** Determina la mejor etapa para farming de un recurso específico. "Task Bar Hero Farming Calculator: Best Stage" — calcula drops por hora por stage.

**Inputs:** Recurso a farming, tipo de stage, difficulty, número de chests (si aplica)

**Outputs:** Mejor stage para ese recurso, drops/hora esperados, tiempo de clear, recomendación

**Datos necesarios:** Drops de cada stage (de `stages` y `droplists` — probablemente tenemos), tiempo para clear cada stage,chest cooldown

**JSON WOG:** `stages` (lo tenemos), `droplists` + `drops` (lo tenemos). Necesitamos tiempo de clear por stage — dato externo o datamined.

**Factible:** SÍ.

---

#### 2.2.11 Chest Optimizer (/wiki/chest-tracker)

**Qué hace:** Calcula cuántas cajas abres por hora en cada stage, y optimiza la secuencia de chests para max boxes/hr.

**Inputs:** Stage, cooldown real (no el erroneo de 2.05s), número de chests disponibles

**Outputs:** Boxes/hr por stage, optimización de secuencia, time invested vs loot

**Datos necesarios:** Cooldown real del juego, número de chests por stage, drop tables de cada chest (`chests` data)

**JSON WOG:** Si WOG tiene sistema de chests. Necesitamos data de chests + cooldown real.

**Factible:** SÍ.

---

#### 2.2.12 Drop Finder (/wiki/drop-finder)

**Qué hace:** Busca cualquier item y te dice en qué stages, chests, monsters, gacha, o events aparece. "Task Bar Hero Drop Finder: Where Any Item Drops"

**Inputs:** Nombre de item (search)

**Outputs:** Todas las fuentes de drop: stages, chests, monsters, gacha, alchemy, events — con odds por fuente

**Datos necesarios:** Tabla completa de qué dropa cada fuente (stages, chests, monsters, gacha lists). Nuestro `droplists` + `drops` + `gachalist` debería cubrir esto.

**JSON WOG:** `droplists` (lo tenemos), `drops` (lo tenemos), `gachalist` (lo tenemos), `stages` (lo tenemos), `monsters` (lo tenemos). Verificar cobertura.

**Factible:** SÍ — altamente factible con nuestros datos.

---

#### 2.2.13 Rune Planner (MORE CALCULATORS)

**Qué hace:** Planifica qué runas equipar en cada slot para optimizar un build específico. Calcula el valor de cada runa por nivel y quelle combinación maximiza los stats que buscas.

**Inputs:** Stats objetivo (ej: máximo crit rate), runas disponibles, slots disponibles, nivel de las runas

**Outputs:** Combinación óptima de runas por slot, valor total del setup, comparación con alternativas

**Datos necesarios:** Stats de cada runa por nivel (nuestro `runes` si existe — verificar), fórmula de combinación de stats

**JSON WOG:** Verificar si tenemos datos de runas. En `data/` de WOG — revisar.

**Factible:** SÍ si tenemos datos de runas.

---

#### 2.2.14 Meta Sockets / Meta Gear / Meta Heroes (MORE CALCULATORS)

**Qué hace:** Herramientas que muestran qué gear/sockets/héroes son los más usados en el meta actual (basado en builds de la comunidad o datos del juego). "Meta" = lo que la comunidad está usando.

**Inputs:** Filtros por role, stage difficulty, clase de héroe

**Outputs:** N ranking de meta gear, sockets más populares, heroes más usados con % del player base

**Datos necesarios:** O bien datos de la comunidad (builds subidos) o datos datamined de cuáles items son más efectivos. Puede ser calculado estáticamente si conocemos las odds de cada item.

**JSON WOG:** Podríamos calcular meta estáticamente usando los datos de efectividad (DPS/EHP calculados) en lugar de depender de comunidad.

**Factible:** PARCIAL — meta basado en datos del juego (factible), meta basado en comunidad (requiere backend).

---

#### 2.2.15 Best-in-Slot Finder (MORE CALCULATORS)

**Qué hace:** Dado un monster/stage objetivo, te dice qué gear es el best-in-slot para cada ranura.

**Inputs:** Monster/stage objetivo, role del héroe

**Outputs:** BiS por ranura con stats y porqué es el mejor

**Datos necesarios:** Stats de todos los items de gear, fórmula de daño/defensa, conocimiento de qué stats importan más en cada situación

**JSON WOG:** `equipment`, `weapons`, `items` (lo tenemos). Necesitamos fórmula de evaluación.

**Factible:** SÍ — calcular BiS con datos de stats del juego.

---

#### 2.2.16 Cube Exp Calculator (/wiki/cube-exp)

**Qué hace:** Calcula cuánto EXP obtienes del cubo por cada operación. "Cube EXP Calculator: Task Bar Hero Level Match" — matching de nivel con EXP.

**Inputs:** Operación del cubo, item usado, grade, nivel del cubo

**Outputs:** EXP obtenido por operación, curve de EXP, optimal operations para level-up

**Datos necesarios:** Tabla de EXP por operación del cubo

**JSON WOG:** Si WOG tiene sistema equivalente de cube/experimentación de equipo.

**Factible:** SÍ.

---

#### 2.2.17 Stat Caps (/wiki/stat-caps, /wiki/stats)

**Qué hace:** Documenta los stat caps reales del juego (ej: dodge está capado en 75%, no 60% como dicen las tablas). "Task Bar Hero Stat Caps: Dodge Is 75%, Not 60%" y "Stats Explained: Real Caps & Scaling".

**Qué es:** No es calculadora interactiva sino documentación clave que TBH indexa. Aporta credibilidad al sitio.

**Datos necesarios:** Conocimiento de los caps reales del juego + fórmula de scaling de cada stat

**JSON WOG:** Dato que hay que descubrir mediante datamining o pruebas en-game. Cada juego tiene sus caps.

**Factible:** SÍ — es documentación, no calculadora.

---

### 2.3 SIMULADORES

#### 2.3.1 Cast Speed Simulator (/simulators/cast-speed-simulator)

**Qué hace:** Simula visualmente cómo el Cast Speed afecta el tiempo de cast de una habilidad específica. "Fires on a timer, so the game scales its cast with Cast Speed. Only the middle (action) part of the animation is divided — the wind-up..."

**Inputs:** Héroe (Knight, Ranger, Sorcerer, Priest, Hunter, Slayer), Skill (Fireball, Ice Orb, Lightning, etc.), Cast Speed del héroe (slider o input numérico)

**Outputs:** Animación visual del cast dividido en wind-up/action/wind-down, tiempo total del cast, ticks de daño por segundo, comparison con base cast speed

**Datos necesarios:** Base cast time de cada skill por clase, fórmula de scaling con cast speed (wind-up fijo, action scaling)

**JSON WOG:** `skills` (lo tenemos), pero necesitamos la fórmula de cast speed del juego — suele ser específica de cada juego.

**Factible:** SÍ pero con complejidad media — requiere conocer cómo modela el juego el cast speed.

---

#### 2.3.2 Chest Simulator (/simulators/chest-simulator)

**Qué hace:** Simulador interactivo de cajas. "Click the chest to open it" — el jugador hace click en la caja y el simulador hace un roll aleatorio mostrando el drop en tiempo real. "TOTAL ROLLS: 0, ROLLS SINCE LAST RARE+: 0, BEST DROP THIS SESSION: —, COMMON 0.0% (expected 78.0%), UNCOMMON 0.0% (expected 20.6%), RARE 0.0% (expected 1.4%), Live Drop Feed"

**Inputs:** Selección de tipo de caja (Monster Box, Stage Boss Box, Act Boss Box, Normal Monster Box 1, etc. — 114 boxes), click en la caja para abrir

**Outputs:** Drop aleatoria real con odds ponderadas, feed de drops en vivo, estadísticas de sesión (rolls, % observado vs expected, rare+ tracking)

**Datos necesarios:** Drop tables de cada chest (nuestro `chests` si existe — revisar), odds por grade de cada chest

**JSON WOG:** Verificar si tenemos datos de chests. Necesitamos drop table por chest.

**Factible:** SÍ — simulación pura con datos de drop tables. La parte "live drop feed" es solo JS client-side.

---

#### 2.3.3 Cube Simulator (/simulators/cube-simulator)

**Qué hace:** Simulador del sistema del cubo. "Mock inventory" — pon items en el inventario de prueba, y el simulador te dice qué pasa cuando aplicas una operación del cubo. "reset all, Mock inventory, My stash, one at a time, Reset sockets, All, Gear, Accessory, Material, Coins, All grades (Common→Cosmic→Beyond→Celestial→Divine→Cosmic→Divine→...), Lv.90/∞ sliders"

**Inputs:** Inventario de prueba (items con grade,.level), operación del cubo a aplicar

**Outputs:** Resultado de la operación (nuevo item con grade/level stats), odds de cada resultado, visualización del proceso

**Datos necesarios:** Todas las operaciones del cubo, odds de cada resultado, efectos de cada item en el cubo

**JSON WOG:** Dependiendo de si WOG tiene sistema de "cube". Si es similar a gacha mejorar equipo, los datos en `gacha` + `gachalist` podrían servir.

**Factible:** SÍ pero complejo — requiere conocer todas las operaciones y sus odds del juego.

---

### 2.4 TIER LISTS (/tier-lists)

**Qué hace:** Sistema comunitario de tier lists. Los usuarios crean rankings arrastrando items/héroes/pets/monsters/stages a categorías S/A/B/C/D/F (o T0/T0.5/T1/T2/etc. para héroes). Features:
- "Create a tier list" — crear nuevo
- Subject selector: All / Heroes / Skins / Pets / Items / Materials / Monsters / Stages / Custom
- "Remix this list" — copiar y modificar una tier list existente
- "Share card" — compartir con link
- "Follow" — seguir una tier list
- Comentarios
- Featured tier lists del sitio

**Tier lists destacadas:**
- "Best heroes to endgame" (707 upvotes, 7 comments)
- "Hero Tiers" (T0: Hunter, T0.5: Ranger, T1: Sorcerer/Priest, T2: Knight, T3: Slayer)
- "Best Hero Tierlist (Meme)" (S: Knight, A-D: Priest/Ranger/Sorcer/Hunter/Slayer)
- "69 Materials Tierlist"
- "68 True Tierlist"
- Plus: best pets, best stages to farm, cutest heroes, coolest monsters, etc.

**Datos necesarios:** Para las tier lists preexistentes: ninguno (son contenido generado por usuarios). Para crear tu propia tier list: el catálogo de héroes/items/pets/etc. del juego.

**JSON WOG:** `heroes` (lo tenemos), `pets` (lo tenemos), `items` (lo tenemos), `monsters` (lo tenemos), `stages` (lo tenemos). Cubre todo lo necesario para crear tier lists.

**Factible:**
- **Tier lists estáticas (pre-populated):** SÍ — Astro puede renderizarlas como contenido.
- **Sistema comunitario de crear/compartir/remix:** REQUIRIDO BACKEND (DB de usuarios, auth, creación de contenido). No factible en Astro estático sin backend.
- **Renderizar las tier lists de TBH como curiosidad:** SÍ, pero son content de TBH, no data del juego WOG.

---

### 2.5 RANKINGS (/ranking)

**Qué hace:** Rankings globales de jugadores. "4,018 players ranked. Priced from current Steam Market data. Rankings are priced server-side from current Steam Market data, using each item's instant-sell (highest buy order) value. Items with no active orders keep their last known price."

**Sub-páginas:**
- /ranking → Global Rankings: listado de jugadores con valor de stash calculado
- /ranking/power → Power Rankings: ranking por poder (DPS/EHP calculado?)
- /ranking/stats → Stats Leaderboards: ranking por estats específicos (mayor HP, mayor DPS, etc.)

**Inputs:** Ninguno para ver rankings. Para participar: subir tu stash (/.tbhsave file) — esto requiere el sistema de /stash.

**Outputs:** Tabla de jugadores con rank, valor del stash en euros (o moneda local), avatar, stats clave

**Datos necesarios:** 
- Steam Market prices como fuente de valuation (requiere que el juego esté en Steam)
- Stash de jugadores (upload de .tbhsave)
- Sistema de cálculo de valor del stash

**JSON WOG:** No aplica directamente — depende de infraestructura de rankings (players, saves, pricing).

**Factible:**
- **Ranking estático de "mejores builds teóricos":** SÍ — podemos calcular qué hero+gear+skills es el más poderoso y mostrarlo como ranking estático.
- **Ranking comunitario con submits de jugadores:** REQUIRIDO BACKEND (auth, uploads de saves, cálculo server-side).
- **Precios de mercado:** SÓLO si WOG está en Steam o tiene mercado player-to-player. Si no, no hay pricing data.

---

### 2.6 BUILDS (/builds)

**Qué hace:** Sistema de builds de la comunidad. "Browse team builds, save your own, and share them with a link. Open the planner to create one from scratch or import your save."

**Features:**
- Lista de builds existentes con pagination
- Filtros: "FROM THESE BUILDS: Meta Gear, Meta Sockets, Meta Attributes, Meta Heroes, Meta Skills"
- Categoría: All / General / Campaign / Boss / Farming
- "Create a build" — crear nuevo build
- "Import your save" — importar desde .tbhsave

**Build individual (/builds/1):** Muestra el build con todos los detalles — héroe, gear, skills, stats calculados. (El que probé dio "invalid or corrupted" porque no existe realmente — es un placeholder)

**Datos necesarios:** Para construir: heroes, gear, skills, stats de cada uno. Para importar save: formato de .tbhsave del juego.

**JSON WOG:** Tenemos todos los datos del juego para mostrar builds estáticos. Para sistema comunitario: backend necesario.

**Factible:**
- **Showcase de builds estáticos (ej: "Best farming build", "Best boss build"):** SÍ — Astro renderiza con datos del juego.
- **Planner interactivo con import de save:** REQUIRIDO BACKEND + parser del formato de save del juego.
- **Sistema de "importar tu save":** Requiere backend + formato de save conocido.

---

### 2.7 WIKI — CONTENIDO DE MECÁNICAS (/wiki/*)

La wiki de TBH es enorme (4,128 páginas). No toda es calculadoras — gran parte es documentación. Aquí las secciones más importantes que WOG no tiene:

#### 2.7.1 Sistema de Grades (/wiki/grades)

**Qué:** Documenta los 10 rangos de rareza del juego: Common, Uncommon, Rare, Legendary, Immortal, Arcana, Beyond, Celestial, Divine, Cosmic (y más — el simulador de cube menciona ∞ levels). Explica cómo se obtiene cada grade, odds, valoración.

**Datos necesarios:** Lista de grades del juego, odds de obtención por cada fuente

**JSON WOG:** Nuestro `fusionlevel` probablemente tiene grades. Verificar.

**Factible:** SÍ — documentación estática.

---

#### 2.7.2 Material Effects (/wiki/material-effects)

**Qué:** 79 efectos de materiales documentados. Cada material aplicado a un item confiere un efecto específico. "Which Mat Gives What" — tabla de material → efecto.

**Datos necesarios:** Cada material + su efecto + qué items aceptan ese material

**JSON WOG:** Si WOG tiene sistema de materiales para crafting/gear. Revisar `materials` si existe.

**Factible:** SÍ con datos.

---

#### 2.7.3 Unique Modifiers (/wiki/modifiers)

**Qué:** 36 modificadores únicos documentados. Estos son modificadores especiales que aparecen en items específicos (no los stats normales). "All 36 Indexed".

**Datos necesarios:** Lista de los 36 modificadores únicos + en qué items aparecen

**JSON WOG:** Si WOG tiene modificadores únicos de gear. Revisar `passiveitems` o similar.

**Factible:** SÍ con datos.

---

#### 2.7.4 Stage Power (/wiki/stage-power)

**Qué:** "Enemy HP Per Stage" — tabla de HP de enemigos por stage number. Muestra la curve de escalado de dificultad del juego.

**Datos necesarios:** HP de cada monster en cada stage, fórmula de escalado

**JSON WOG:** `stages` + `monsters` (lo tenemos). Si tenemos HP por stage en los datos, perfecto.

**Factible:** SÍ con datos.

---

#### 2.7.5 Stat Caps (/wiki/stat-caps)

**Qué:** Documenta los caps reales de cada stat. El ejemplo más destacado: "Dodge Is 75%, Not 60%". Muchos sitios recomiendan invertir en dodge hasta 60% pero el cap real es 75%.

**Datos necesarios:** Conocimiento de los caps del juego — dato que hay que dataminear o descubrir por prueba y error en-game.

**JSON WOG:** Dato externo a los JSON — hay que descubrirlo.

**Factible:** SÍ — es documentación.

---

#### 2.7.6 Buffs & Debuffs (/wiki/buffs, /wiki/status-effects)

**Qué:** 29 buffs & debuffs documentados con sus efectos reales. "All 29 Stat Effects" y "Real Penalties".

**Datos necesarios:** Lista de 29 buffs/debuffs con fórmula de efecto (ej: +20% damage, -15% incoming damage, blind, stun, etc.)

**JSON WOG:** Verificar si tenemos `buffs` o `status-effects` en nuestros datos. Revisar.

**Factible:** SÍ con datos.

---

#### 2.7.7 Alchemy (/wiki/alchemy, /wiki/alchemy-gold, /wiki/alchemy-ranking)

**Qué:** Sistema de alquimia del juego — fundir items para obtener oro y cube EXP. "Exact Gold & Cube EXP" — las odds reales de cuánto oro da cada item al fundir. "Alchemy Item Ranking: Best Melt Gold" — ranking de qué items son más rentables de fundir.

**Datos necesarios:** Oro por melt por item-grade, cube EXP por melt, odds

**JSON WOG:** Si WOG tiene sistema de alquimia/fundir items. Revisar.

**Factible:** SÍ con datos. Ranking de "mejor item para fundir" = cálculo estático con datos de oro por item.

---

#### 2.7.8 Extraction (/wiki/extraction)

**Qué:** "Gold Cost to Reroll Sockets" — cuánto cuesta extraer/re-roll los sockets de un item. Documenta el coste en oro y las odds de obtener cada tipo de socket en el reroll.

**Datos necesarios:** Coste de extracción por grade del item, odds de cada tipo de socket en reroll, tipos de sockets disponibles

**JSON WOG:** Si WOG tiene sistema de sockets y extracción. Revisar.

**Factible:** SÍ con datos.

---

#### 2.7.9 Corrosion & Contamination (/wiki/corrosion, /wiki/contamination)

**Qué:** Mecánicas del juego relacionadas con rarity y risk. "Contamination: How It Really Drains" — cómo funciona el mecanismo de contaminación (degrada items? reduce eficacia?). "Corrosion: Contamination Per Grade" — cuánta contaminación introduce cada grade.

**Datos necesarios:** Mecánica de contaminación, cómo afecta a los items, odds de corrosión por grade

**JSON WOG:** Si WOG tiene estas mecánicas. Revisar.

**Factible:** SÍ con datos.

---

#### 2.7.10 Drop Finder (/wiki/drop-finder)

**Qué:** Ya descrito arriba — herramienta que busca todas las fuentes de un item.

---

#### 2.7.11 Compare (/wiki/compare)

**Qué:** "Item Compare: Which Is Better?" — compara dos items y te dice cuál es mejor para qué situación. Toma dos items, muestra stats lado a lado, y da veredicto.

**Datos necesarios:** Stats de cada item, criterio de comparación (depende del uso: farming vs boss vs meta)

**JSON WOG:** `items`, `equipment`, `weapons` (lo tenemos). Comparador = calcular stats y evaluar según contexto.

**Factible:** SÍ — calculadora de comparación con datos del juego.

---

#### 2.7.12 Best-in-Slot (/wiki/best-in-slot)

**Qué:** BiS por ranura para cada contexto (farming, boss, meta general). Ya descrito arriba en calculadoras.

---

#### 2.7.13 Chest Tracker (/wiki/chest-tracker)

**Qué:** Calcula cajas por hora por stage. "Boxes Per Hour". Ya descrito.

---

#### 2.7.14 Party Composition (/wiki/party-composition)

**Qué:** "Most-Played Hero Pairs" — analiza qué combinaciones de héroes son las más usadas. Data basada en plays reales o_builds de comunidad.

**Datos necesarios:** Data de cuáles héroes se usan juntos — puede ser calculado (héroe A buffa a héroe B) o data de comunidad.

**JSON WOG:** `heroes` (lo tenemos). Sin data de comunidad, podemos calcular synergies teóricas.

**Factible:** SÍ — synergies teóricas calculables + si tenemos data de builds reales.

---

#### 2.7.15 Meta Attributes (/wiki/meta-attributes)

**Qué:** "Most-Used Stats" — qué stats son los più usados en el meta actual. Data de builds de comunidad o análisis de efectividad.

**Datos necesarios:** Data de qué stats importan más en diferentes contextos del juego.

**JSON WOG:** Podemos calcular qué stats son más impactantes usando datos de efectividad del juego.

**Factible:** SÍ.

---

#### 2.7.16 Skill Priority (/wiki/skill-priority)

**Qué:** "Full Cast Order" — el orden óptimo de casts de habilidades para cada clase. "Task Bar Hero Skill Priority: Full Cast Order".

**Datos necesarios:** Optimal cast order por clase (calculado por DPS/efectividad). `skills` (lo tenemos) — podemos calcular el orden óptimo si conocemos la fórmula de daño.

**JSON WOG:** Necesitamos fórmula para calcular optimal order.

**Factible:** SÍ con fórmula de daño.

---

#### 2.7.17 Synthesis (/wiki/synthesis)

**Qué:** Documenta el sistema de síntesis con odds reales. "Synthesis Odds: Real Grade-Up Rates".

**Datos necesarios:** Odds de grade-up por combinación.

**JSON WOG:** Nuestro `fusion` puede ser equivalente.

**Factible:** SÍ con datos.

---

#### 2.7.18 Sockets & Inscription (/wiki/sockets, /wiki/inscription)

**Qué:** Sistema de zócalos del juego — cada item tiene ranuras donde se colocan sockets (runas, inscripciones, etc.). "Inscription: The Rarest Socket Type" — documenta el tipo de socket más raro y cómo obtenerlo.

**Datos necesarios:** Tipos de sockets disponibles, odds de appearance, qué items los aceptan, inscripción como tipo especial

**JSON WOG:** Si WOG tiene sistema de sockets. Revisar.

**Factible:** SÍ con datos.

---

#### 2.7.19 Chat & Mailbox (/wiki/chat, /wiki/mailbox)

**Qué:** Documenta sistemas sociales del juego — chat y mailbox (donde van las compras del market).

**Datos necesarios:** Funcionamiento de chat y mailbox del juego.

**JSON WOG:** Depende de si WOG tiene estas features.

**Factible:** SÍ si existen en el juego (documentación).

---

#### 2.7.20 Achievements (/wiki/achievements)

**Qué:** "Real Global Unlock Rates" — tasas reales de desbloqueo de cada achievement. "Task Bar Hero Achievements: Real Global Unlock Rates".

**Datos necesarios:** Lista de achievements con tasa global de unlock (datamined o Steam API).

**JSON WOG:** Si WOG tiene achievements.

**Factible:** SÍ si existen en el juego.

---

#### 2.7.21 Roadmap (/wiki/roadmap)

**Qué:** "Development Roadmap" del juego — qué viene próximamente. "Task Bar Hero Roadmap 2026: Plaguelands Live". Contenido dinámico que el desarrollador del juego actualiza.

**Datos necesarios:** Roadmap del desarrollador del juego (WOG). Si WOG tiene roadmap público.

**JSON WOG:** No aplica — es contenido de planning del juego, no data del juego.

**Factible:** SÍ si WOG tiene roadmap público.

---

### 2.8 COMMUNITY FEATURES

#### 2.8.1 Tier Lists (ya descrito)

#### 2.8.2 Guides (/guides)

**Qué:** Sistema de guías escritas por la comunidad. "Farming routes, boss strategies, cube math — written by the players who worked it out."

**Features:** Escribir guías con imágenes, tablas, embeds de YouTube. Categorías: All / General / Beginner / Farming / Boss / Meta / Cube / Community. "Write a guide" — crear nuevo.

**Guías destacadas:** "How to make Priest Tanky For Plaguelands" (928 upvotes), varias guías de farming y meta.

**Datos necesarios:** Ninguno para el sistema — es contenido creado por usuarios. Requiere backend (CMS de guías).

**Factible:** BACKEND necesario para sistema comunitario. Para Astro estático: manualmente escribir guías y renderizarlas.

---

#### 2.8.3 Content Creators (/creators)

**Qué:** "The people teaching Task Bar Hero to their communities — on YouTube, Twitch, TikTok and Kick, in a dozen languages. Every creator below is tracked live, so you can see who is streaming right now and what they just uploaded."

**Features:** Lista de creadores con su plataforma, link, "live now" indicator, última video subido. "Featured in your language" — filtro por idioma.

**Datos necesarios:** Lista de creadores con sus datos (nombre, plataforma, link, channel ID). "Live tracking" requiere consultar APIs de Twitch/YouTube para saber si están live.

**JSON WOG:** No aplica — es contenido externo.

**Factible:** 
- **Lista estática de creadores WOG:** SÍ — si Chytzo o la comunidad tiene creadores.
- **Live tracking:** Requiere integración con APIs de Twitch/YouTube — posible pero complejo.

---

#### 2.8.4 Supporter Wall (/supporter-wall)

**Qué:** "Hall of Supporters — These incredible people help keep TBH Index free and running for everyone. Every contribution, big or small, makes a difference. Support on Ko-fi, Become a Patron."

**Features:** Mostrar nombre de 후원자 (backers) con su tier de apoyo. "Every supporter, at any tier, gets their name displayed with a unique [badge/star] on the Global Ranking" — los 후원자 aparecen en los rankings con marca especial.

**Datos necesarios:** Lista de 후원자 con su nivel de apoyo (de Ko-fi/Patreon API).

**JSON WOG:** No aplica — sistema de 후원 de WOG si existe.

**Factible:** SÍ si WOG tiene sistema de 후원 (Ko-fi, Patreon, etc.). Mostrar lista de 후원자 estática o con integración API.

---

#### 2.8.5 Community Hub (/community)

**Qué:** Página de aglutinación de todas las features comunitarias: Tier Lists, Guides, Builds. "Rank anything, write a guide, or plan the perfect team. Made by players, for players."

**Datos necesarios:** Ninguno — es página de aglutinación.

**Factible:** SÍ — página de aglutinación estática.

---

### 2.9 HERRAMIENTAS PRIVADAS (requieren save del jugador)

#### 2.9.1 Inspect Your Stash (/stash)

**Qué:** El jugador sube su archivo de save (.tbhsave) y la herramienta analiza su stash completo — qué items tiene, valor total, qué le falta para un build óptimo, etc.

**Estado:** Bloqueado en robots.txt (`Disallow: /stash`) porque es una ruta privada que requiere upload. No está en el sitemap. "These routes need an uploaded .tbhsave to show anything, so a crawler only ever sees the empty shell."

**Datos necesarios:** Parser del formato de save del juego (.tbhsave). Sistema de upload y procesado.

**JSON WOG:** Requiere conocer el formato de save de WOG — esto es crítico y debe dataminearse.

**Factible:** REQUIRIDO BACKEND + parser de save. No factible en Astro estático. Necesita:
- Parser del formato de save (binario? JSON? - hay que descubrirlo)
- Upload de archivo
- Procesado server-side
- Mostrar resultados

---

#### 2.9.2 Profile (/profile)

**Qué:** Similar al stash — el jugador sube su save y crea un perfil persistente. Seelled en robots.txt como privado: `Disallow: /profile`.

**Datos necesarios:** Mismo que stash + sistema de perfiles de usuarios.

**Factible:** BACKEND necesario.

---

### 2.10 MULTI-IDIOMA

**Qué:** 22 idiomas con rutas separadas: /es, /pt, /ru, /zh, /ja, /ko, /fr, /de, /tr, /pl, /it, /th, /uk, /zh-TW, /id, /vi, /fil, /ms + x-default. Cada página del sitemap tiene sus variantes hreflang.

**Implementación:** TBH tiene el mismo contenido en 22 idiomas. Probablemente usa un CMS de traducción o archivos JSON de localización.

**Datos necesarios:** Traducciones de todo el contenido a 22 idiomas. Gran esfuerzo de localización.

**JSON WOG:** Nuestro `locales` JSON podría ayudar — revisar si tiene las traducciones del juego.

**Factible:**
- **1-2 idiomas (ES + EN):** SÍ — factible en Astro con i18n.
- **22 idiomas:** NO factible manualmente — requeriría automatización o juego con soporte multilingüe nativo.

---

### 2.11 OTRAS RUTAS

- /about — Página "about" del proyecto
- /privacy — Política de privacidad  
- /terms — Términos de servicio
- /contact — Formulario de contacto
- /creators — Ya descrito

---

## 3. RESUMEN: LO QUE TBH TIENE Y WOG NO TIENE

### 3.1 Categoría: CALCULADORAS (FALTANTES EN WOG)

| Calculadora | Dificultad | Datos necesarios | Nuestros datos |
|---|---|---|---|
| Crafting Calculator (odds por tier) | Media | Tabla de odds de crafting | Verificar `fusion` como equivalente |
| Cube Exp Optimizer/Planner | Media | Curve EXP del cubo, operaciones | Si WOG tiene sistema equivalente |
| Soulstone Calculator | Baja-Media | Odds de boss, mecánica soulstone | Revisar si existe en WOG |
| Offering Calculator | Baja-Media | Odds de offering | Revisar si existe en WOG |
| Synthesis Calculator | Media | Odds de synthesis por combinación | `fusion` podría servir |
| Synthesis Cost Calculator | Baja | Coste de síntesis por grade | Revisar datos de fusión |
| Alchemy Gold Calculator | Baja-Media | Oro por melt por item-grade | Si WOG tiene alquimia |
| Damage Taken Calculator | Alta | Fórmula de daño, stats, buffs | Falta fórmula — dato crítico |
| Combat Lab (DPS+EHP) | Alta | Fórmula de daño completa + skills + monsters | Necesitamos fórmula |
| Farming Calculator | Media | Drops por stage, tiempo de clear | Tenemos drops + stages; falta tiempo de clear |
| Chest Optimizer | Media | Cooldown real, chests por stage | Falta data de chests |
| Drop Finder | Media | Drop tables de todas las fuentes | Tenemos `droplists`+`drops`+`gachalist` |
| Rune Planner | Media | Stats de runas por nivel | Verificar si tenemos `runes` |
| Best-in-Slot Finder | Media | Stats de todos los items, criterio de valoración | Tenemos items/equip/weapons |
| Cube Exp Calculator | Media | EXP por operación del cubo | Si WOG tiene sistema equivalente |
| Stat Caps (documentación) | Baja | Conocimiento de caps del juego | Dato externo — hay que descubrir |
| Compare (item compare) | Media | Stats de items + criterio | Tenemos datos de items |

### 3.2 Categoría: SIMULADORES (FALTANTES EN WOG)

| Simulador | Dificultad | Datos necesarios | Nuestros datos |
|---|---|---|---|
| Cast Speed Simulator | Media-Alta | Base cast time, fórmula de scaling | Tenemos skills; falta fórmula |
| Chest Simulator (click-to-open) | Baja-Media | Drop tables de chests | Verificar `chests` en datos |
| Cube Simulator (mock inventory) | Alta | Todas las operaciones + odds del cubo | Si WOG tiene sistema equivalente |

### 3.3 Categoría: TIER LISTS (FALTANTES EN WOG)

| Feature | Dificultad | Backend necesario? | Viable en Astro |
|---|---|---|---|
| Tier lists estáticas (pre-populated) | Baja | No | SÍ — renderizar contenido |
| Sistema de crear/compartir/remix tier lists | Alta | SÍ (DB, auth, users) | No — requiere backend |
| Featured tier lists del sitio | Baja | No | SÍ |

### 3.4 Categoría: RANKINGS (FALTANTES EN WOG)

| Feature | Dificultad | Backend necesario? | Viable |
|---|---|---|---|
| Ranking estático de "mejores builds teóricos" | Media | No | SÍ — calcular DPS/EHP máximo |
| Ranking comunitario con submits de jugadores | Alta | SÍ (auth, saves, calculo) | No sin backend |
| Precios de mercado (Steam Market) | Media | Depende de Steam | Solo si WOG está en Steam |
| Power Rankings / Stats Leaderboards | Media-Alta | SÍ para datos de jugadores | Ranking estático factible |

### 3.5 Categoría: BUILDS (FALTANTES EN WOG)

| Feature | Dificultad | Backend necesario? | Viable |
|---|---|---|---|
| Showcase de builds estáticos (ej: "Best farming build") | Baja-Media | No | SÍ — con datos del juego |
| Build Planner interactivo | Media-Alta | Sí para persistencia | Interactivo en cliente posible |
| Importar save (.wogsave) | Alta | Sí + parser de save | Requiere conocer formato |

### 3.6 Categoría: WIKI DE MECÁNICAS (FALTANTES EN WOG)

| Wiki page | Dificultad | Tipo | Necesario |
|---|---|---|---|
| Grades (10 rangos) | Baja | Documentación | Data de grades (`fusionlevel`) |
| Material Effects (79) | Media | Documentación | `materials` + efectos |
| Unique Modifiers (36) | Media | Documentación | Datos de modificadores |
| Stage Power (HP por stage) | Baja | Documentación + tabla | `stages` + `monsters` |
| Stat Caps | Baja | Documentación | Conocimiento externo |
| Buffs & Debuffs (29) | Media | Documentación | Verificar si tenemos `buffs` |
| Status Effects | Media | Documentación | Verificar si tenemos |
| Alchemy (oro + cube EXP) | Media | Documentación + calc | Si WOG tiene alquimia |
| Extraction (reroll sockets) | Media | Documentación | Si WOG tiene sockets |
| Corrosion & Contamination | Media | Documentación | Si WOG tiene estas mecs |
| Drop Finder | Media | Herramienta | Tenemos datos relevantes |
| Compare (item compare) | Media | Herramienta | Tenemos datos |
| Best-in-Slot | Media | Herramienta | Tenemos datos |
| Chest Tracker | Media | Herramienta | Falta data de chests |
| Party Composition | Media | Documentación | Podemos calcular synergies |
| Meta Attributes | Media | Documentación | Podemos calcular |
| Skill Priority | Media | Documentación | Falta fórmula de daño |
| Synthesis (odds reales) | Media | Documentación | `fusion` puede servir |
| Sockets & Inscription | Media | Documentación | Si WOG tiene sockets |
| Achievements | Media | Documentación | Si WOG tiene achievements |
| Chat & Mailbox | Baja | Documentación | Si WOG tiene estas features |
| Roadmap | Baja | Contenido externo | Roadmap de WOG |

### 3.7 Categoría: COMUNIDAD (FALTANTES EN WOG)

| Feature | Dificultad | Backend necesario? | Viable |
|---|---|---|---|
| Guides escritas por usuarios | Alta | SÍ (CMS) | Manualmente: escribir guías en Astro |
| Content Creators tracking | Media | Sí para live (APIs) | Lista estática factible |
| Supporter Wall | Baja | Sí para actualización automática | Lista estática factible |
| Community Hub | Baja | No | SÍ |

---

## 4. DATA GAP ANALYSIS — QUÉ NOS FALTA DE LOS JSON DEL JUEGO

### Tenemos (check):
- `heroes` ✓
- `equip` ✓
- `items` ✓
- `weapons` ✓
- `machina` ✓
- `pets` ✓
- `monsters` ✓
- `stages` ✓
- `skills` ✓
- `passiveskills` ✓
- `abilities` + `abilityactions` ✓
- `drops` + `droplists` ✓
- `gacha` + `gachalist` ✓
- `fusion` + `fusionlevel` ✓
- `passiveitems` ✓
- `locales` ✓

### Necesitamos descubrir (data gap):
1. **Fórmula de daño del juego:** Crítico para Combat Lab, Damage Taken Calculator, Cast Speed Simulator, Skill Priority, Best-in-Slot, Meta Attributes, Farming Calculator. Sin esto, las calculadoras de daño no son precisas.
2. **Sistema de grades completos:** Si `fusionlevel` tiene los grades del juego o necesitamos datos separados.
3. **Sistema de crafting:** Si existe y cómo funciona (o si `fusion` es el equivalente).
4. **Sistema de sockets/inscripciones:** Si existe en WOG.
5. **Sistema de alquimia/fundición:** Si existe.
6. **Sistema de extracción/reroll:** Si existe.
7. **Sistema de runas:** Si existe y sus datos (`runes` en JSON?).
8. **Sistema de chests:** Si existe y sus drop tables.
9. **Sistema de offering:** Si existe.
10. **Sistema de soulstone:** Si existe.
11. **Sistema de cube:** Si existe (equivalente al cubo de TBH).
12. **Cooldowns reales de chests:** Dato específico que hay que medir.
13. **Tiempo de clear por stage:** Para Farming Calculator.
14. **Mecánicas de corrosión/contaminación:** Si existen.
15. **Stat caps reales:** Para documentación.
16. **Formato de save del juego (.wogsave):** Para stash inspection + build import.
17. **Material Effects (79):** Si WOG tiene sistema de materiales para crafting/gear.
18. **Unique Modifiers (36):** Si WOG tiene modificadores únicos de gear.

---

## 5. TOP 10 FEATURES MÁS VALIOSAS/VIABLES PARA WOG INDEX

### RANKING DE IMPLEMENTACIÓN

#### #1 — Drop Finder (buscador de fuentes de drop)
**Prioridad:** CRÍTICA  
**Dificultad:** Baja-Media  
**Datos necesarios:** `droplists`, `drops`, `gachalist`, `stages`, `monsters` — TODOS TIENEN  
**Viabilidad:** SÍ — altamente factible. Es una de las herramientas más útiles para jugadores.  
**Qué construir:** Página `/drops` con buscador de item → muestra todas las fuentes (stage, chest, monster, gacha, alchemy) con odds por fuente.  
**Valor:** Inmediato — jugadores siempre quieren saber dónde farmear un item específico.

---

#### #2 — Crafting/Synthesis Calculator (calculadora de odds de crafting/fusión)
**Prioridad:** ALTA  
**Dificultad:** Media  
**Datos necesarios:** Tabla de odds de crafting/fusión por combinación. Verificar si `fusion` + `fusionlevel` tiene estos datos.  
**Viabilidad:** SÍ — cálculo estático.  
**Qué construir:** `/calculators/crafting` o `/calculators/fusion` — inputs: materiales de entrada, grade objetivo → outputs: odds de cada resultado.  
**Valor:** Los jugadores invierten recursos en crafting/fusión; saber las odds reales es valioso.

---

#### #3 — Farming Calculator + Drop Tables por Stage
**Prioridad:** ALTA  
**Dificultad:** Media  
**Datos necesarios:** `stages`, `droplists`, `drops`, tiempo de clear por stage (descubrir)  
**Viabilidad:** SÍ — calculable estáticamente.  
**Qué construir:** `/calculators/farming` o sección en `/wiki/stages` — para cada stage: drops/hora estimados por recurso, mejor stage para cada item.  
**Valor:** Jugadores farming constantemente — esta herramienta les ahorra tiempo.

---

#### #4 — Best-in-Slot + Compare (BiS por situación + comparador de items)
**Prioridad:** ALTA  
**Dificultad:** Media  
**Datos necesarios:** `equipment`, `weapons`, `items` — todos TIENEN. Necesitamos criterio de evaluación (qué stats importan más en cada contexto).  
**Viabilidad:** SÍ — con datos de stats del juego.  
**Qué construir:** 
- `/bis` — BiS por ranura para cada contexto (farming, boss, meta)
- `/compare` — comparador de dos items con stats lado a lado

**Valor:** Jugadores constantemente preguntan "qué gear es mejor" — esto responde la pregunta.

---

#### #5 — Wiki de Mecánicas del Juego (documentación depth)
**Prioridad:** ALTA (para credibilidad del sitio)  
**Dificultad:** Baja (documentación) / Media (datos faltantes)  
**Datos necesarios:** Depende de cada sección — ver gap analysis arriba.  
**Viabilidad:** SÍ — Astro maneja documentación estática perfectamente.  
**Qué construir:** Extender las páginas wiki existentes con las secciones de TBH que aplican a WOG:
- `/wiki/grades` — grades del juego
- `/wiki/materials` — materiales y sus efectos
- `/wiki/modifiers` — modificadores únicos
- `/wiki/stage-power` — HP por stage
- `/wiki/stat-caps` — caps reales
- `/wiki/buffs` — 29 buffs/debuffs
- `/wiki/status-effects` — status effects
- `/wiki/alchemy` — alquimia (si existe)
- `/wiki/extraction` — extracción (si existe)
- `/wiki/corrosion` + `/wiki/contamination` — (si existen)
- `/wiki/compare` — comparador
- `/wiki/synthesis` — síntesis (si existe)
- `/wiki/sockets` + `/wiki/inscription` — (si existen)

**Valor:** TBH es la referencia por su profundidad de documentación. WOG necesita llegar a ese nivel para ser la referencia en el nicho de WOG.

---

#### #6 — Chest Simulator (click-to-open, drop feed en vivo)
**Prioridad:** MEDIA-ALTA  
**Dificultad:** Baja-Media  
**Datos necesarios:** Drop tables de chests (`chests` si existe en datos; si no, chests data del juego)  
**Viabilidad:** SÍ — simulación con JS client-side.  
**Qué construir:** `/simulators/chest` — seleccionar tipo de chest, click para abrir, drop aleatoria con odds ponderadas, feed de sesión.  
**Valor:** Diversión interactiva + utilidad para entender odds reales de chests. Muy shareable.

---

#### #7 — Cast Speed Simulator
**Prioridad:** MEDIA  
**Dificultad:** Media-Alta  
**Datos necesarios:** Base cast time de cada skill, fórmula de scaling con cast speed (wind-up fijo, action escala)  
**Viabilidad:** SÍ pero requiere conocer la fórmula del juego.  
**Qué construir:** `/simulators/cast-speed` — selector de héroe + skill, slider de cast speed → animación visual + stats.  
**Valor:** Herramienta técnica para optimizar builds de cast speed — nicho pero valioso.

---

#### #8 — Rune Planner + Meta Gear/Sockets/Heroes
**Prioridad:** MEDIA  
**Dificultad:** Media  
**Datos necesarios:** `runes` si existe en datos. Si no, está bloqueado.  
**Viabilidad:** SÍ si tenemos datos de runas.  
**Qué construir:** 
- `/calculators/rune-planner` — planifica combinación óptima de runas
- `/meta` — meta gear/sockets/heroes (calculado estáticamente por efectividad, no por comunidad)

**Valor:** Si WOG tiene runas, es una herramienta clave. Si no, descartar.

---

#### #9 — Tier Lists estáticas (pre-populated)
**Prioridad:** MEDIA  
**Dificultad:** Baja  
**Datos necesarios:** `heroes`, `pets`, `items`, `monsters`, `stages` — TODOS TIENEN  
**Viabilidad:** SÍ — Astro renderiza contenido estático.  
**Qué construir:** `/tier-lists` — crear 3-4 tier lists de ejemplo: "Best heroes to endgame", "Materials tierlist", "Best pets", "Best stages to farm".  
**Valor:** Contenido viral + referencia rápida para jugadores. No requiere backend.

---

#### #10 — Build Showcase + Build Planner (estática + interactiva client-side)
**Prioridad:** MEDIA  
**Dificultad:** Media  
**Datos necesarios:** `heroes`, `equipment`, `weapons`, `items`, `skills` — todos TIENEN  
**Viabilidad:** SÍ — interactivo en cliente con JS. Para persistencia: backend necesario.  
**Qué construir:** 
- `/builds` — showcase de builds destacados (calculados por DPS/EHP)
- `/builds/planner` — planner interactivo para armar un build ( seleccionar heroe, gear, skills → ver stats)

**Valor:** Jugadores quieren planificar sus builds — el planner interactivo da utilidad inmediata.

---

## 6. FEATURES QUE REQUIEREN BACKEND (descartar para Astro estático por ahora)

Estas NO son viables en un sitio estático sin backend. Marcar como "fase 2" o "si llegamos a tener backend":

| Feature | Por qué requiere backend |
|---|---|
| Inspect Your Stash (/stash) | Upload de save + parser server-side |
| Profile (/profile) | Auth + perfiles de usuarios |
| Ranking comunitario | Auth + submits de jugadores + cálculo server-side |
| Sistema de crear/compartir tier lists | DB + users + creación de contenido |
| Sistema de guías de comunidad | CMS de guías con auth |
| Build Planner con import de save | Parser de save + persistencia |
| Content Creators live tracking | APIs de Twitch/YouTube externas |
| Supporter Wall automático | API de Ko-fi/Patreon |
| Market prices en vivo | Scraping/API de Steam o mercado externo |
| Rankings basados en Steam Market | Depende de Steam + pricing data |

---

## 7. RESUMEN EJECUTIVO

### Qué implementar ahora (fase 1 — sin backend, solo Astro + datos JSON):

1. **Drop Finder** — `/drops` — buscador de item → fuentes de drop. CRÍTICO. Datos: tenemos casi todo.
2. **Crafting/Fusion Calculator** — `/calculators/crafting` o `/calculators/fusion` — odds de crafting/fusión. ALTA prioridad. Verificar datos de `fusion`.
3. **Farming Calculator** — `/calculators/farming` — mejor stage para cada recurso. ALTA. Tenemos drops+stages.
4. **Best-in-Slot + Compare** — `/bis` + `/compare` — BiS por contexto + comparador de items. ALTA. Tenemos datos de gear.
5. **Wiki profundidad** — extender las páginas wiki existentes con las secciones de TBH que aplican a WOG (grades, material effects, modifiers, stage power, stat caps, buffs, alchemy, etc.). ALTA. Documentación estática.
6. **Chest Simulator** — `/simulators/chest` — click-to-open con drop feed. MEDIA-ALTA. Verificar data de chests.
7. **Tier Lists estáticas** — `/tier-lists` — 3-4 tier lists de ejemplo (héroes, materiales, pets, stages). MEDIA. Contenido estático.
8. **Build Planner interactivo** — `/builds/planner` — armar un build y ver stats. MEDIA.
9. **Cast Speed Simulator** — `/simulators/cast-speed` — si conocemos la fórmula. MEDIA.
10. **Rune Planner + Meta** — si WOG tiene runas. MEDIA.

### Qué requiere descubrir primero (data gaps críticos):

- **Fórmula de daño del juego** — necesaria para Combat Lab, Cast Speed Simulator, Skill Priority, Best-in-Slot calibrado, Farming Calculator calibrado. Sin esto, las calculadoras de daño son estimaciones a lo loco.
- **Formato de save del juego (.wogsave)** — para futurasfeatures de stash inspection y build import.
- **Sistema de sockets, runas, alquimia, extracción, offering, soulstone** — verificar cuáles existen en WOG y tener sus datos.
- **Cooldowns reales de chests** — dato específico a medir.
- **Tiempo de clear por stage** — para Farming Calculator preciso.

### Qué descartar o posponer (requiere backend o no aplica):

- Inspect Your Stash / Profile — Fase 2, necesita backend + parser de save.
- Ranking comunitario — Fase 2, necesita backend + jugadores registrados.
- Sistema de tier lists comunitario — Fase 2, necesita backend.
- Guides comunitarias — Manualmente podemos escribir guías; sistema comunitario es Fase 2.
- Market prices en vivo — Solo si WOG está en Steam o tiene mercado player-to-player.
- Content Creators live tracking — Lista estática factible; live tracking es Fase 2.
- 22 idiomas — Empezar con ES + EN. 22 idiomas es esfuerzo de localización masivo.

---

## 8. PRÓXIMOS PASOS RECOMENDADOS

1. **Data audit 완료:** Revisar cada uno de los JSON del juego para confirmar qué datos tenemos realmente (especialmente `fusion`, `passiveitems`, `materials` si existe, `runes` si existe, `chests` si existe, `buffs`/`status-effects` si existen).

2. **Descubrir fórmula de daño:** Esta es la pieza crítica faltante. O bien datamineando el código del juego, o bien haciendo pruebas en-game, o bien preguntando a la comunidad. Sin esta, las calculadoras de daño no son fiables.

3. **Priorizar implementación:** Empezar por Drop Finder + Crafting Calculator + Farming Calculator (bajo hanging fruit con alto valor), luego BiS + Compare, luego wiki depth, luego simuladores.

4. **Definir alcance de "calculadoras":** Cada calculadora es un archivo .astro separado con su lógica client-side. El patrón es: inputs (formulario/selector/slider) → cálculo JS → outputs (tabla/valor/visualización).

---

*Informe generado por ACORAY. Analista técnico senior. 11/09/2026.*
