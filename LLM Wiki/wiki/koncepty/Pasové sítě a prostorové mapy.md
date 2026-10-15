---
typ: koncept
tags: [herni-data, vizualizace, pasove-site, analyza-soupere, event-data]
zdroje: ["[[Zdroj – Soccermatics]]"]
aktualizovano: 2026-10-15
---
# Pasové sítě a prostorové mapy

Sada vizuálů z event dat, které ukazují **strukturu hry týmu** – kdo s kým kombinuje, kam míč proudí, odkud vznikají šance a kde tým získává míč. Sumpter je řadí do „taktické mapy“: jednoduchý obrázek, který analytik ukáže trenérovi o poločase – ne „Voronoi diagramy a vektorová pole“ ([[Zdroj – Soccermatics]], Kap. 2, 3, 7).

## Pasová síť (passing network)

- Uzly = hráči (průměrná pozice), hrana = dvojice nad prahem přihrávek, tloušťka ∝ počtu přihrávek.
- **Pozor na práh:** v knize se mezi obrázky mění (≥5 až ≥13) → mapy nejsou srovnatelné. *Návrh: jednotný práh, příp. relativní k počtu přihrávek týmu.*
- Příklady: Itálie vs. Anglie (Euro 2012) – „kolo“ kolem Pirla (115 přihrávek); Anglie bez sítě ve středu, nejsilnější dvojice Hart → Carroll. USWNT 2015 – přechod od centralizace na Wambach k decentralizované hře (Lloyd).

## Síťové metriky (Grund 2012)

- **Passing rate** = úspěšné přihrávky / minuty držení (v datech vč. přerušení → hodnoty 3–5/min).
- **Centralizace** = průměrný rozdíl mezi nejvytíženějším hráčem a ostatními / všechny přihrávky (0 = rovnoměrně, 1 = vše přes jednoho).
- PL 2006–08 (283 259 přihrávek): 5/min vs. 3/min ≈ **+20 % gólů**; decentralizované týmy ≈ +8 % (malé efekty). Euro 2012: Španělsko 14,6 % vs. Itálie 19,7 % centralizace, finále 4:0.
- *Využití (návrh):* v analýze soupeře hledat **přetíženého hubu** (koho vypnout).

## Pass flow field a mapa distribuce

- **Flow field hráče:** heat mapa, odkud přihrává, + šipky průměrného směru (dx, dy vyhlazené polynomem přes hřiště; Ranganathan et al. 2014). Pirlo = „klid v oku bouře“ (střed, přenášení hry), Schweinsteiger = „vír“ po celém hřišti. Úskalí: průměr skrývá rozptyl směrů (Kap. 3).
- **Mapa distribuce:** hřiště 25 zón, ze středu zóny čáry směrů (délka ∝ délce přihrávek, odstín ∝ četnosti). Bayern CL 2014/15: střed → křídla → prostory vedle vápna (Kap. 7).
- **Zonální pasová síť:** šipka od průměrné pozice passera při přihrávce k průměrné pozici příjemce při přijetí (≥7 přihrávek). Barcelona 3:0 Bayern 2015 – „stíhačka“ s vyváženými křídly; Bayern „kruhový objezd“ ve středu bez šipek k nebezpečí.

## Šance a bránění

- **Shot mapa + „danger zone“:** všechny góly Realu (Ronaldo, Bale, Benzema) z pole 20 × 20 m před brankou; heat mapa míče **15 s před střelou** z této zóny ukazuje, odkud tým šance staví (Real: levá strana Marcelo–Ronaldo).
- **Defenzivní hull:** body zisku míče hráče (skluzy, interceptions…), ponechat jen ty do 1 SD od průměru v x i y, obalit konvexní obálkou. Juventus vs. Real 2015 – pravá strana Lichtsteiner + Marchisio 32 zisků zavřela levou stranu Realu; vysoké hulls Realu = presink.

## Geometrie za tím

Delaunay triangulace (pasové trojúhelníky) a Voronoi zóny (prostor hráče) jsou duální – kdo dobře pokrývá prostor, má automaticky dobré pasové možnosti. Obránce na hranici dvou zón je v „zemi nikoho“ → [[Half-spaces a taktická geometrie]].

> [!note] Aktualita (poznámka LLM – ověřit)
> Pasové sítě jsou dnes standardní výstup Wyscoutu a StatsBombu; s tracking daty ([[SkillCorner]]) lze místo sítě realizovaných přihrávek kreslit **sítě dostupných přihrávek** (viz [[Pressing a kolektivní pohyb]]).

## Souvislosti

[[Analýza soupeře – metodika]] · [[Aplikace – Analýza soupeře]] · [[Principy vizualizace a reportingu]] · [[Wyscout]] (pass network, PPDA) · [[Plány analýzy (micro, meso, macro)]]
