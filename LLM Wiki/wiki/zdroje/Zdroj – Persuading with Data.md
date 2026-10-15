---
typ: zdroj
tags: [zdroj, kniha, vizualizace, reporting, komunikace, prezentace, presvedcovani]
cesta: "LLM Wiki/raw/Persuading with Data (Kazakoff 2022).pdf"
ingest: 2026-10-15
aktualizovano: 2026-10-15
---
# Zdroj – Persuading with Data

Kniha **Miro Kazakoff: *Persuading with Data – A Guide to Designing, Delivering, and Defending Your Data*** (MIT Press 2022). Učebnice z kurzu *Communicating with Data* na MIT Sloan. Pokrývá **celou cestu od analýzy k rozhodnutí**: jak mozek čte grafy → jak navrhnout graf a slide → jak strukturovat sdělení (Minto pyramida) → jak publikum přesvědčit (WIIFT, framing) → jak data prezentovat (TOP-T) a obhájit (Audience Confusion Matrix).

> [!info] Poznámky ke zdroji
> - PDF (318 s., převod z e-knihy) s textovou vrstvou, přečteno celé. Grafy a ukázkové slidy jsou jen jako popisky – převzaty principy a příklady z textu.
> - Příklady jsou z byznysu (prodeje, IT, nemocnice, konzultace), **ne ze sportu** – přenos do fotbalu je vždy *návrh LLM*.
> - Autor staví na Tufte, Few, Minto, Duarte, Nussbaumer Knaflic (*Storytelling with Data*), Heath (*Made to Stick*), Kahneman.
> - **Danůva poznámka [[Apple Notes/Yarmill/Vizualizace dat|Vizualizace dat]] se s Kap. 1–3 shoduje téměř bod po bodu** (osa y od nuly, inverze 99,0 vs. 99,5, odstín vs. intenzita, Gestalt „uzavření, symetrie, kontinuita, společný osud, minulá zkušenost“, popisky místo legendy, svislé vs. vodorovné sloupce, linie = tvar / sloupce = okamžiky). Jsou to zřejmě výpisky z této knihy (?) – kniha je tedy **původní zdroj** části [[Principy vizualizace a reportingu]].
> - Citace: **Kap. 1–9**; „pozn.“ = autorovy poznámky pod čarou.

## Struktura knihy

| Část | Kap. | Obsah → stránka wiki |
|---|---|---|
| I. Vnímání | 1 Know Your Own Mind | 3 výzvy komunikace (více myslí, Curse of Knowledge, kognitivní zátěž); fáze exploring vs. explaining → [[Vysvětlování dat – tři výzvy]] |
| | 2 See How Graphs Work | vztahy, chunky (3–4), salience; preattentivní atributy, Gestalt → [[Vnímání grafů – preattentivní atributy a Gestalt]] |
| II. Design | 3 Choose the Right Graph | 5 vztahů (kategorie, čas, část-celek, distribuce, korelace) → [[Výběr grafu podle vztahu v datech]] |
| | 4 Simplify to Amplify | data-ink ratio, vizuální hierarchie, referenční čáry („compared to what?“), anotace, dvě osy y → [[Data-ink ratio a vizuální hierarchie]] |
| | 5 Build Effective Slides | headline ≠ titulek; testy self-sufficiency, blink, data podporují headline, jazyk sladěný → [[Headline a testy slidu]] |
| III. Struktura | 6 Structure Your Data | Minto pyramida, situace–komplikace–rozuzlení, MECE, indukce/dedukce, sebeklam → [[Minto pyramida]] |
| | 7 Frame the Data to Persuade | Elaboration Likelihood Model, WIIFT, zdroje důvěryhodnosti, 4 rámce → [[WIIFT a přesvědčování publika]] |
| IV. Prezentace a obhajoba | 8 Present Your Data | TOP-T (Topic, Orient, Point, Transition), „ta-da“, tichý orient → [[TOP-T – prezentace grafu]] |
| | 9 Prepare for Resistance | poměry, ne hodnoty; očekávání; Audience Confusion Matrix; jak zvládnout odpor → [[Audience Confusion Matrix]] |

## Hlavní myšlenky

1. **Vysvětlit data je jiná dovednost než je analyzovat.** Exploratorní fáze slouží mně (složitost je výhoda), explanatorní fáze slouží publiku (složitost je nepřítel). „Vezmi publikum rovnou ke zlatu, ne na prohlídku všech míst, kde jsi nic nenašel.“ (Kap. 1)
2. **„Once you see the dolphin, you can't unsee it.“** Curse of Knowledge: analytik tráví s daty řádově víc času než publikum (graf ≥ 100 s práce vs. 5–10 s čtení) a zapomene, jaké to je data neznat. Nejlepší zbraň: ukázat to jiným lidem (Kap. 1, 6).
3. **Graf má smysl jen tehdy, když ukazuje vztah.** Graf vybírat podle vztahu, ne podle dat; přednost mají běžné typy grafů – známost snižuje zátěž (Kap. 2, 3).
4. **Když chce vyniknout všechno, nevynikne nic.** Jeden nejvýraznější prvek = nejdůležitější prvek; „smallest effective difference“ (Tufte) (Kap. 2, 4).
5. **„Compared to what?“** Hodnotící slova (dobře, špatně, rychle) vyžadují v grafu viditelné srovnání – cíl, průměr, threshold. Jinak publikum porovnává data samo se sebou (Kap. 4, 5).
6. **Každý slide = jeden bod napsaný jako headline** (věta se slovesem), ne titulek. Headline je nejdůležitější věc pro snížení zátěže publika (Kap. 5).
7. **Struktura shora dolů:** hlavní myšlenka → klíčové body → důkazy (Minto). Hlavní myšlenka vzniká jako rozuzlení příběhu situace → komplikace (Kap. 6).
8. **Lidé hodnotí víc než data.** Většinu času zpracovávají periferně (kdo mluví, jak), centrálně jen když jde o ně → **WIIFT** (What's In It For Them) je nejsilnější nástroj; pro každé publikum jiný (Kap. 7).
9. **Data nemluví sama za sebe – musíš jim dát hlas.** U každého grafu: téma → orientace v grafu → pointa → přechod. Pointu až po orientaci, žádné „ta-da“ (Kap. 8).
10. **Odpor znamená, že to publikum zajímá.** Lidé reagují na **změny poměrů** a na **rozpor s očekáváním**; nejtěžší je situace „čekali jsme změnu a nepřišla“ (Kap. 9).

## Klíčová čísla a fakta (výběr)

- Pracovní paměť: **3–4 chunky** naráz (Cowan 2001; Miller 7 ± 2 jako starší odhad) (Kap. 2, pozn. 4).
- Poruchy barvocitu: ~**4,5 %** populace, ale **1 z 12 mužů** a 1 z 200 žen; v publiku nad 20 lidí je téměř jistě někdo s CVD (Kap. 1, 2).
- Čtení ~**400 slov/min** → headline o 10 slovech místo titulku o 4 stojí publikum ~1 s (Kap. 5).
- Sladění obrazu a mluveného slova zlepší zapamatování a použití informace až o **30 %** (Mayer, median effect size 1,3) (Kap. 8).
- Framing poplatku: „penalizace za pozdní registraci“ → 93 % doktorandů se registrovalo včas, „sleva za včasnou“ → jen 63 % (Gächter et al. 2009) (Kap. 7).
- Text psaný tučně / čitelněji působí věrohodněji (Kahneman) → „data musí být čitelná, aby byla věrohodná“ (Kap. 1).
- Anscombův kvartet: 4 sady se stejným průměrem, SD i R² (0,82), ale zcela jiným tvarem (Kap. 2).

## Rámce a checklisty

Každá kapitola končí checklistem: *Explaining data to others* (Kap. 1), *Graph design* (Kap. 4), *Slide impact* (Kap. 5), *Minto pyramid* (Kap. 6), *Persuasion* (Kap. 7), *Graph presentation* (Kap. 8), *Defusing resistance* (Kap. 9). Převzaty na jednotlivé stránky konceptů.

> [!note] Aktualita (poznámka LLM)
> Kniha je z roku 2022 a cílí na **statické grafy ve slidech** (PowerPoint). Interaktivní dashboardy (Yarmill, BI nástroje) a AI generované reporty řeší jen okrajově – principy (headline, srovnání, salience) se ale přenášejí. Výzkum vizualizace nejistoty (Hullman, Kay) byl v roce 2022 v začátcích.

## Co z toho plyne pro wiki / Danů

Kniha je **teoretická páteř komunikace dat** – doplňuje [[Principy vizualizace a reportingu]] (které z ní zřejmě částečně vycházejí) o strukturu sdělení, přesvědčování a obhajobu. Pro datové oddělení Sigmy je relevantní hlavně: headline v reportech a aplikacích, referenční čáry/thresholdy, WIIFT pro trenéry vs. vedení vs. hráče, TOP-T při prezentaci štábu a Audience Confusion Matrix před poradami s „nepříjemnými“ daty. Návrhy → [[Persuading with Data – návrhy pro Sigmu]].

## Lidé a díla zmíněná v knize

Edward Tufte (data-ink, smallest effective difference), Stephen Few (*Show Me the Numbers*), Gene Zelazny (*Say It with Charts*), Barbara Minto (*The Pyramid Principle*, MECE), Nancy Duarte (*DataStory*, situace–komplikace–rozuzlení), Cole Nussbaumer Knaflic (*Storytelling with Data*), Chip & Dan Heath (*Made to Stick* – Curse of Knowledge, „answer stage“ vs. „telling others stage“), Daniel Kahneman, Alberto Cairo (*The Truthful Art*), Kaiser Fung (self-sufficiency test, Junk Charts), Robert Cialdini, Petty & Cacioppo (ELM), Richard Mayer (multimediální učení), Allen Telio (spoluautor Audience Confusion Matrix).

## Souvislosti

[[Přehled wiki]] · [[Principy vizualizace a reportingu]] · [[Persuading with Data – návrhy pro Sigmu]] · [[Kognitivní zkreslení v hodnocení]] · [[Zdroj – Pořiďte si druhý mozek]]
