---
typ: koncept
tags: [vizualizace, grafy, reporting]
zdroje: ["[[Zdroj – Persuading with Data]]", "[[Zdroj – Yarmill poznámky]]"]
aktualizovano: 2026-10-15
---
# Výběr grafu podle vztahu v datech

Graf se vybírá podle **vztahu, který má publikum vidět**, ne podle toho, jaká data mám. Nejdřív pojmenovat vztah, pak zvolit graf; přednostně běžné typy – jejich známost je výhoda, ne nedostatek ([[Zdroj – Persuading with Data]], Kap. 3; vychází z Few a Zelazny).

## Pět běžných vztahů

| Vztah | Co ukazuje | Signální slova | Grafy | Zásady |
|---|---|---|---|---|
| **Kategorie** | hodnoty kategorií v jednom okamžiku | míra + kategorie | sloupce, seskupené sloupce | výchozí svislé; vodorovné pro mnoho kategorií / dlouhé názvy; **řadit podle hodnot**, ne abecedně; u seskupených sloupců se dotýkají ty, které jsou hlavním srovnáním |
| **Čas** | jak se kategorie mění v čase | změna, růst, pokles, trend | linie, sloupce | linie = **tvar a trend**, sloupce = **konkrétní okamžiky**; stejné časové intervaly; vhodná **frekvence zobrazení** (moc časté = šum, moc řídké = skryje vzorec; dva body = slope graph) |
| **Část–celek** | jak části tvoří celek | podíl, mix, % z celku | skládané sloupce, waterfall, mosaic (mekko) | koláč jen výjimečně (málo velkých segmentů, publikum nezvyklé na grafy); srovnávané části potřebují **společnou základnu**; waterfall pro + i − složky |
| **Distribuce** | jak se pozorování rozkládají podle hodnoty | frekvence, rozsah, koncentrace | histogram, frequency polygon, box plot | promyšlené biny (i nestejné, když to dává smysl – např. platová pásma); box plot jen pro jednovrcholová data a publikum zvyklé na kvartily |
| **Korelace** | vztah dvou proměnných téže jednotky | roste s, klesá s, souvisí | scatter, bubliny, table lens | trendová čára jen při skutečné souvislosti; **outliery popsat a ztlumit**; neukazovat „nekorelaci“ s trendovou čárou (R² 0,008 + stoupající čára = falešný dojem); pozor na slova kauzality („způsobeno“, „dopad na“) |

Distribuce ≠ část–celek: distribuce dělí **jednu kategorii podle hodnoty** (velikost objednávky), část–celek dělí podle **kategorií** (regiony).

Lidé vidí vzorce i v náhodě (apofenie, pareidolie) → [[Kognitivní zkreslení v hodnocení]].

## Taxonomie grafů

Experception.net (*Which Visualization?*), **FT Visual Vocabulary** (ft.com/vocabulary), *The Graphic Continuum* (PolicyViz), *Chartmaker Directory* (visualisingdata.com).

## Ve fotbale (*návrh LLM*)

| Otázka | Vztah | Graf |
|---|---|---|
| Kdo v týmu naběhal nejvíc HSR v zápase? | kategorie | vodorovné sloupce seřazené podle hodnoty + threshold postu |
| Jak se vyvíjí zátěž hráče v mikrocyklu / sezóně? | čas | linie (trend), u MD−x sloupce (konkrétní dny) → [[Mikrocyklus a značení MD]] |
| Z čeho se skládá celková zátěž / minutáž kádru? | část–celek | skládané sloupce (A-tým, B-tým, U19) |
| Jak jsou rozložené výkony v CMJ v akademii? | distribuce | histogram, box plot podle kategorií → [[Silové testy a normy]] |
| Souvisí xG s body? Věk s minutáží? | korelace | scatter s popsanými outliery → [[Expected goals (xG)]] |

## Souvislosti

[[Principy vizualizace a reportingu]] · [[Vnímání grafů – preattentivní atributy a Gestalt]] · [[Data-ink ratio a vizuální hierarchie]] · [[Pasové sítě a prostorové mapy]]
