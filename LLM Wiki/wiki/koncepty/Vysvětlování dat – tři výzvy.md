---
typ: koncept
tags: [komunikace, vizualizace, reporting, psychologie]
zdroje: ["[[Zdroj – Persuading with Data]]"]
aktualizovano: 2026-10-15
---
# Vysvětlování dat – tři výzvy

Komunikace = **zakódovat** myšlenku do slov a obrazů → přenést → **dekódovat** v hlavě někoho jiného. Tento proces je zdrojem všech komunikačních problémů. Při vysvětlování dat působí tři výzvy, které při samotné analýze „spí“ ([[Zdroj – Persuading with Data]], Kap. 1).

## Tři výzvy

| Výzva | Co znamená | Co z toho plyne |
|---|---|---|
| **Více myslí** (multiple minds) | různé hlavy dekódují totéž různě – kontext, předchozí zkušenost, zkratky (ASP), kultura (červená = ztráta, jinde zisk), kanál (písmo na projektoru), biologie (barvoslepost), mluvčí (přízvuk) | co je jasné mně, není jasné ostatním |
| **Curse of Knowledge** (prokletí znalosti) | když něco pochopím, zapomenu, jaké to bylo nevědět; experti trpí víc než nováčci („once you see the dolphin, you can't unsee it“) | vysvětlit data je samostatná dovednost a jiné myšlení |
| **Kognitivní zátěž** | mozek se vyhýbá námaze; věříme víc tomu, co se snáz čte | data musí být **čitelná, aby byla věrohodná**; nejde o „zjednodušení obsahu“, ale o odstranění všeho, co překáží pochopení |

Příklad zátěže: analytik stráví nad grafem ≥ 100 s (často hodiny), publikum 5–10 s → minimálně 10× víc času s daty.

## Exploring vs. explaining

| | Exploratorní fáze („answer stage“) | Explanatorní fáze („telling others stage“) |
|---|---|---|
| Publikum | já | někdo jiný |
| Žádoucí složitost | vysoká (vidět všechny možnosti) | nízká (soustředit se na odpověď) |
| Cíl | pochopit, co data znamenají | vysvětlit jejich význam ostatním |
| Odpověď je | výstup mé práce | **vstup do rozhodnutí někoho jiného** |

Typická chyba: **provést publikum celým průzkumem** (všechny grafy, slepé uličky). Pro analytika hrdinský příběh, pro publikum zátěž. „Vezmi je rovnou ke zlatu.“ Metodiku ukazovat jen v míře nutné pro důvěryhodnost → [[Minto pyramida]].

## Checklist „Explaining data to others“

- **Více myslí:** Znám kontext a zázemí publika? Vím, jaké analýzy běžně čte a jak často?
- **Curse of Knowledge:** Vysvětlil jsem analýzu někomu jinému? Někomu se **stejnou úrovní znalostí**, jakou má publikum?
- **Kognitivní zátěž:** Odstranil jsem složitost, která není nutná k pochopení? Mluvím o výsledcích, ne o postupu?

## Ve fotbale (*návrh LLM*)

- Publikum Sigmy je velmi různorodé: hlavní trenér, asistenti, kondiční trenér, vedení, hráči, trenéři mládeže, rodiče – každá skupina dekóduje jinak (zkratky jako HID, PSV-99, ACWR, TIP/OTIP nejsou samozřejmé) → glosář / „manual of metrics“ v [[Oddělení analýzy – struktura a role]].
- Curse of Knowledge je silný u vlastních aplikací ([[Aplikace – Analýza soupeře]], [[Aplikace – Match tracker]]): autor ví, co který prvek znamená, uživatel ne → testovat na trenérovi, který aplikaci vidí poprvé.

## Souvislosti

[[Principy vizualizace a reportingu]] · [[Vnímání grafů – preattentivní atributy a Gestalt]] · [[Kognitivní zkreslení v hodnocení]] · [[TOP-T – prezentace grafu]]
