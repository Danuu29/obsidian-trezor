---
typ: koncept
tags: [vizualizace, vnimani, grafy, design]
zdroje: ["[[Zdroj – Persuading with Data]]", "[[Zdroj – Yarmill poznámky]]"]
aktualizovano: 2026-10-15
---
# Vnímání grafů – preattentivní atributy a Gestalt

Proč grafy fungují: mozek okamžitě vidí **vztahy**, skládá data do **chunků** a soustředí se na **nejvýraznější (salientní)** prvek. Grafy kódují data **preattentivními atributy** a skupiny vytvářejí **Gestalt principy** ([[Zdroj – Persuading with Data]], Kap. 2). Danůvy výpisky ke stejnému tématu: [[Apple Notes/Yarmill/Vizualizace dat|Vizualizace dat]].

## Co vidíme, když vidíme graf

| Co vidíme | Co to znamená | Co z toho plyne |
|---|---|---|
| **Vztahy** | vzorce a výjimky (Anscombův kvartet: stejné statistiky, jiný tvar) | graf použít jen tehdy, když zkoumám nebo ukazuji vztah; přesné hodnoty → tabulka |
| **Chunky** | vizuální prvky slučujeme do skupin, v hlavě udržíme **3–4** | rozdělit graf do malého počtu skupin (24 čísel v tabulce → 2 linie = 2 chunky) |
| **Salience** | vidíme to nejvýraznější; nejvýraznější může být jen jedna věc | nejdůležitější prvek = nejvýraznější; **když chce vyniknout všechno, nevynikne nic** |

## Preattentivní atributy (gramatika grafů)

| Atribut | Kóduje | Pravidla |
|---|---|---|
| **Velikost** (výška > šířka > plocha) | hodnoty | sloupce **vždy od nuly** (y-axis truncation = typická manipulace); drobný, ale důležitý rozdíl → ukázat inverzní metriku (uptime 99,9 → 99,5 % jako downtime) nebo jiný typ grafu; plochy (bubliny) jen hrubě |
| **Pozice** | hodnoty | publikum předpokládá **nahoru = dobře**; když je nahoru špatně (náklady, chybovost), výslovně to označit |
| **Odstín** (hue) | kategorie | omezená, **barvoslepě bezpečná** paleta (pozor na červená/zelená, modrá/zelená); ne duhové škály |
| **Intenzita** | hodnoty, kategorie, zvýraznění | intenzitou dělit uvnitř kategorie a zvýrazňovat; kvantitativní proměnné spíš intenzitou než odstínem (spojitě, nebo v binech jako známky) |

Příklad škály spokojenosti: tři odstíny (nespokojení = červené, neutrální = šedá, spokojení = modré) s rostoucí intenzitou k extrémům.

## Gestalt principy

| Princip | Příklady | Pravidlo |
|---|---|---|
| **Uzavření** (enclosure) | rámečky, stínované oblasti | nejsilnější a nejrušivější – zvýrazňovat raději intenzitou; rámečky přidávají často nadřízení při revizi |
| **Spojení** (connection) | linie, ukazatele | spojovat jen body, které **spolu koncepčně souvisejí** (čas ano, různé produkty ne) |
| **Blízkost** (proximity) | popisky, anotace | popisky přímo u prvku místo legendy; oko je na blízkost velmi citlivé |
| **Podobnost** (similarity) | barva, tvar | barva popisku = barva linie |

Některé principy přebíjejí jiné (spojení > podobnost, uzavření > vše). Používat **„smallest effective difference“** (Tufte) – nejjemnější prostředek, který stačí. Další Gestalt principy: uzavřenost tvaru (closure), symetrie, kontinuita, společný osud, minulá zkušenost (pozn. 11).

> [!note] Pracovní paměť
> Kniha uvádí **3–4 chunky** (Cowan 2001), Danůva poznámka „2–3 prvky“, starší literatura 7 ± 2 (Miller 1956). Nejde o věcný rozpor – kniha sama říká, že měřit to je obtížné a publikum má na téma vždy méně místa než autor → [[Rozpory a nesrovnalosti]].

## Souvislosti

[[Principy vizualizace a reportingu]] · [[Výběr grafu podle vztahu v datech]] · [[Data-ink ratio a vizuální hierarchie]] · [[Vysvětlování dat – tři výzvy]]
