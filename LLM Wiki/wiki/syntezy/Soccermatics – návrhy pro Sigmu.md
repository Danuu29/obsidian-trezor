---
typ: synteza
tags: [navrhy, sigma, yarmill, analytika, soccermatics]
zdroje: ["[[Zdroj – Soccermatics]]"]
aktualizovano: 2026-10-15
---
# Soccermatics – návrhy pro Sigmu

*Syntéza / návrhy LLM*: co z [[Zdroj – Soccermatics]] lze přenést do práce v [[SK Sigma Olomouc]] a [[Yarmill]]. Nic není rozhodnuté – seznam k probrání. Navazuje na [[Barça kurz – návrhy pro Sigmu]] (metodika) – Soccermatics přidává kvantitativní nástroje a validaci.

## [[Aplikace – Analýza soupeře]]

1. **Pasová síť + centralizace** soupeře (jednotný práh) → najít hub, přes kterého jde hra, a navrhnout, jak ho vypnout → [[Pasové sítě a prostorové mapy]].
2. **Danger zone mapa**: odkud je míč 15 s před střelou z prostoru 20 × 20 m před brankou → kde soupeř staví šance.
3. **Defenzivní hulls** hráčů soupeře (zisky míče, 1 SD) → kde vyhrává míč, kudy ho obejít.
4. Pre-match **W/D/L z kurzů** (normalizovaných) jako úvodní kontext; pravidlo „bránit jen pokud l > 2w“ jako diskusní podnět → [[Predikce a pravděpodobnostní modely]].
5. Dribling profil klíčových útočníků soupeře (kam obchází obránce, na jakou vzdálenost) ze [[SkillCorner]] dat.

## [[Hodnocení utkání a pozápasový report]]

1. Vždy **výsledek vs. xG** a krátká věta o roli náhody; nehodnotit formu z 2–3 zápasů.
2. Sledovat **udržitelnost konverze** (góly − xG) u týmu i hráčů.
3. Hodnotit akce podle **přínosu** (xThreat ze SkillCorneru, packing) místo počtu přihrávek / přesnosti → [[Possession value a Markovovy řetězce]].

## Pressing a tracking (A-tým)

1. KPI represinku: **1. hráč u míče do ~2,5 s, 2. do ~5,5 s** po ztrátě (zpřesnění pravidla 6 s v [[Sigma Way]]); u hlubokého bránění „jeden napadá, ostatní blokují kanály“ → [[Pressing a kolektivní pohyb]]. Ověřit na aktuálních datech.
2. Sledovat **týmovou synchronizaci** při kongesci zápasů vedle GPS objemů → [[GPS metriky a zatížení]].

## Skauting a recruitment

1. Pořadí: **styl hry → profil → algoritmický shortlist → skaut / video sestřih** (Campbell, Atlanta) → [[Skauting – proces a reporting]].
2. Defenzivní metriky **upravit na čas bez míče** (per 30 OTIP) – Kanté efekt → [[Normalizace herních dat]].
3. U každého skóre / radaru v Yarmillu explicitně popsat **váhy a jejich autora** („každý index navrhují lidé“).
4. **Recruitment meeting:** nezávislá písemná hodnocení před diskusí, medián; vést **záznam doporučení a jejich výsledků** (validace, false positives/negatives).
5. Zvážit test **executive functions** (design fluency) jako doplněk [[Vstupní diagnostika hráče]] – ověřit literaturu.

## Datové oddělení

1. Leicester vs. Villa: **důvěra štábu a analytiků > model** – zavádět metriky postupně, se štábem, „fotbalovým jazykem“ → [[Oddělení analýzy – struktura a role]].
2. Dva adresáti: **vedení** (dlouhodobá rozhodnutí, „mythbusting“) a **trenéři** („so what?“ do pár minut).
3. Workflow „video → měření → ověření, zda jde o vzorec“.
4. **Validační kultura:** back-testy, naivní benchmark (loňská tabulka / průměr), malé vzorky hlásit.
5. Talent pipeline: otevřená data / hackathon pro studenty (UP Olomouc?) po vzoru #HackMCFC – *nápad*.

## Souvislosti

[[Barça kurz – návrhy pro Sigmu]] · [[Otevřené otázky]] · [[Přehled wiki]]
