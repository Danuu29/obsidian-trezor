---
typ: koncept
tags: [vizualizace, reporting, komunikace]
zdroje: ["[[Zdroj – Yarmill poznámky]]", "[[Zdroj – Znalosti]]", "[[Zdroj – Analytická témata Sigma]]", "[[Zdroj – Barça Match Analysis]]"]
aktualizovano: 2026-10-15
---
# Principy vizualizace a reportingu

Pravidla, kterými se Danů řídí při stavbě reportů. Hlavní zdroj: [[Apple Notes/Yarmill/Vizualizace dat|Vizualizace dat]].

## Proces

Získat data → analýza (query, pivot) → vizualizace → distribuce.

## Zásady

- **Informace, ne čísla** – trenéři chtějí informace (srov. [[Thresholdy a benchmarky]]).
- Jednoduché vizuály; uživatel musí v co nejkratší chvíli najít, co hledá; co nejméně změn v reportech.
- Report tvořit **s koncovým uživatelem** (neví, co chce vidět; vkus se mění).
- Obrovský pozor na chyby; nikdy si nevymýšlet; barvoslepost.
- Jde-li to, vyprávět příběh; vše shrnout v jedné větě.
- „Pokud to nepomůže pochopit data, nemá ve vizualizaci místo.“
- Kapacita pracovní paměti 7 ± 2, v hlavě reálně 2–3 prvky.
- Potvrzuje i Barça kurz: „mít hodně informací neznamená být dobře informován“, „the how determines the how much“; live dashboard [[Mediacoach]] má max. 9 údajů; každé zjištění doplnit doporučením ([[Zdroj – Barça Match Analysis]]).

## Kontrolní otázky před reportem

Je to srozumitelné? Dostane se to k relevantním lidem? Vím, jak s tím pracují, mám zpětnou vazbu? Má report potenciál změnit chování? Jaká jsou rizika neúspěchu?

## Grafy

- Osa y od nuly; drobné, ale důležité rozdíly (99,0 vs. 99,5) → zobrazit inverzi v čase.
- Liniový graf: nahoru = lépe; pokud ne, musí to být na první pohled jasné.
- Barva: odstín pro kategorie, intenzita v rámci kategorie i pro kvantitativní proměnné.
- Gestalt (blízkost, podobnost, uzavření, kontinuita…): popisky u prvků místo legendy.
- Svislé sloupce pro málo kategorií; vodorovné pro mnoho/dlouhé názvy; trend = linie (tvar), konkrétní okamžiky = sloupce.

## Reporting vedení

Týdně (GPS thresholdy, hodnocení trenérů), čtvrtletně (kam se hráč posouvá), půlročně; přehled odtrénováno/odehráno/výkonnost vs. minulá sezóna.

## Komunikace novinek

Přesně popsat, k čemu to je a co to má říct; očekávání, výpočet, zdroje dat. Po dokončení projít a nahlas okomentovat. Lidé přijmou spíš malé kroky v souladu s předchozím.

## Souvislosti

[[Yarmill]] · [[Karta hráče – koncept]] · [[Typy sportovních dat a datová architektura]] (matice relevance × frekvence; trenéři uvažují heuristicko-induktivně) · [[Video feedback a komunikace s hráči]]
