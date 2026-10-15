---
typ: koncept
tags: [vizualizace, grafy, design, reporting]
zdroje: ["[[Zdroj – Persuading with Data]]"]
aktualizovano: 2026-10-15
---
# Data-ink ratio a vizuální hierarchie

Dva postupy, jak zjednodušit graf a zesílit sdělení: **maximalizovat data-ink ratio** (Tufte) a **vytvořit informační hierarchii**. Cílem není snížit složitost dat, ale udělat z grafu „dokonale průhledné okno do dat“ ([[Zdroj – Persuading with Data]], Kap. 4).

## Data-ink ratio

| Odstranit (pokud není nezbytné) | Vždy mít (pokud to není pro všechny triviální) |
|---|---|
| 3D a stíny · rámečky · velké mezery mezi sloupci · barvy bez významu · výrazné mřížky · značky bodů na liniích · tick marks · zbytečná desetinná místa | popisky os · název grafu · čitelné písmo · **kritérium výběru dat** („top 6 regionů“) · zdroj · jednotky u hodnot ($1M) |

- Začít „od prázdné stránky“ – každý prvek musí obhájit svou existenci.
- Šikmý text nahradit zkratkami nebo vodorovnými sloupci.
- **Čitelnost písma je nejrychlejší způsob, jak snížit zátěž**; raději větší.
- Sloupce širší než mezery (např. gap width 67 %).
- Zbytečná přesnost klame: průměr „$65 342,17“ budí dojem, že všichni berou přesně tolik.

> [!warning] Pozor: co je pro jednoho nepořádek, je pro druhého důvěryhodnost
> Publikum zvyklé na určitý formát (vědci se statistickým softwarem) může „vyčištěný“ graf číst hůř a analytikovi méně věřit („marketing graphs“). **Když šéf chce data v určité podobě, ukaž mu je tak.**

## Vizuální hierarchie

Sladit **výraznost** prvků s jejich **důležitostí**; nejdůležitější = nejvýraznější, ostatní odstupňovat.

| Prvek | Jak zvýšit výraznost |
|---|---|
| Velikost | důležitější text větší (titulek > podtitulek > osy); stejné prvky stejně velké |
| Typ písma | tučné, kurzíva, barva – střídmě |
| Popisky | **selektivní popisky** jen u klíčových bodů – ale jen když publikum chápe proč (jinak to vypadá jako manipulace nebo urážka těch bez popisku) |
| Zvýraznění | vyšší intenzita barvy u vybraných bodů |
| **Referenční čáry** | průměr, medián, trend, intervaly · **cíle a thresholdy** · události (před/po) · skupiny (laggards vs. stars) |
| Anotace | popsat oblasti, outliery, způsob výpočtu (popsat jeden bod a publikum pochopí všechny) |
| Rozdělení | místo grafu se dvěma osami y dva grafy nad sebou se společnou osou x, nebo hodnoty popsat přímo |

## „Compared to what?“

Každý graf je srovnání. **Když publiku neukážu, s čím srovnávat, srovná data sama se sebou.** Příklad: HDP Ruska vypadá silně vůči zemím se středním příjmem, slabě vůči průměru bohatých zemí – volba srovnání je odpovědnost analytika a publikum podle ní posuzuje jeho důvěryhodnost. Slova **dobře, špatně, rychle, pomalu** vždy vyžadují viditelné srovnání. Je to „investice s vysokým výnosem“, i když data pro srovnání bývá těžké sehnat a Curse of Knowledge zakrývá, že srovnání mám jen v hlavě.

→ Princip, na kterém stojí [[Thresholdy a benchmarky]] (semafor vůči normě postu).

## Další pravidla

- **Neříkat publiku, ať se na něco nedívá** – nejde to. Outliery vysvětlit; zbytečnou složitost odstranit; data, která odporují závěru, poctivě vysvětlit (nebo změnit názor).
- Složitý graf: odkrývat **po vrstvách**; ukázat „stejný“ graf víckrát s jiným zvýrazněním; zvážit report/e-mail místo slidu; vysvětlit WIIFT → [[WIIFT a přesvědčování publika]].
- Nejlepší explanatorní grafy **nejsou znovupoužitelné** – jsou šité na publikum a kontext. Grafy pro „všechny“ se nejsnáz přenesou do špatného kontextu.

## Checklist „Graph design“

Odstranil jsem vše, co jde bez ztráty významu? Vrátil jsem, co publikum potřebuje pro důvěru? Je vše popsané? Je text čitelný? Je nejdůležitější prvek nejvýraznější? Jsou všechna srovnání vizualizovaná? Jsou outliery a výrazné body anotované?

## Souvislosti

[[Principy vizualizace a reportingu]] · [[Vnímání grafů – preattentivní atributy a Gestalt]] · [[Headline a testy slidu]] · [[Thresholdy a benchmarky]]
