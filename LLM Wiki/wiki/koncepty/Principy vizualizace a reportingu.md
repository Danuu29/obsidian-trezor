---
typ: koncept
tags: [vizualizace, reporting, komunikace]
zdroje: ["[[Zdroj – Yarmill poznámky]]", "[[Zdroj – Znalosti]]", "[[Zdroj – Analytická témata Sigma]]", "[[Zdroj – Barça Match Analysis]]", "[[Zdroj – Soccermatics]]", "[[Zdroj – Pořiďte si druhý mozek]]", "[[Zdroj – Persuading with Data]]"]
aktualizovano: 2026-10-15
---
# Principy vizualizace a reportingu

Pravidla, kterými se Danů řídí při stavbě reportů. Hlavní zdroj: [[Apple Notes/Yarmill/Vizualizace dat|Vizualizace dat]] – podle shody příkladů zřejmě výpisky z knihy [[Zdroj – Persuading with Data]] (?), která je tak původním zdrojem části zásad níže.

## Proces

Získat data → analýza (query, pivot) → vizualizace → distribuce.

## Zásady

- **Informace, ne čísla** – trenéři chtějí informace (srov. [[Thresholdy a benchmarky]]).
- Jednoduché vizuály; uživatel musí v co nejkratší chvíli najít, co hledá; co nejméně změn v reportech.
- Report tvořit **s koncovým uživatelem** (neví, co chce vidět; vkus se mění).
- Obrovský pozor na chyby; nikdy si nevymýšlet; barvoslepost.
- Jde-li to, vyprávět příběh; vše shrnout v jedné větě.
- „Pokud to nepomůže pochopit data, nemá ve vizualizaci místo.“
- Kapacita pracovní paměti 7 ± 2, v hlavě reálně 2–3 prvky (Persuading with Data uvádí 3–4 chunky – drobná nesrovnalost, viz [[Rozpory a nesrovnalosti]]).
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

## Taktická mapa (Soccermatics)

Sumpter ([[Zdroj – Soccermatics]], Kap. 7, 15): trenérovi neříkat „Voronoi, pasové sítě, vektorová pole“ – ukázat **problém na jednom obrázku**, vysvětlitelném o poločase. Trenéři jsou zvídaví, ale nemají čas, další otázka je vždy **„so what?“**. Výstup musí: dávat fotbalový smysl, mít pevný statistický základ, dát se vysvětlit **během pár minut**, zlepšovat výsledky. Nezaměňovat prezentaci za obsah (efektní grafika v TV studiu). Vizuály → [[Pasové sítě a prostorové mapy]].

## Report ve vrstvách (Druhý mozek)

Princip [[Postupná sumarizace|postupné sumarizace]] z [[Zdroj – Pořiďte si druhý mozek]] (Kap. 6): adresát je „netrpělivý VIP klient“ – nahoře nejzhuštěnější vrstva (2–3 zjištění + doporučení), pod ní stále podrobnější detail, každá vrstva ≤ 10–20 % předchozí. Odpovídá zásadě „informace, ne čísla“ (*syntéza LLM*).


## Komunikace dat (Persuading with Data)

Podle [[Zdroj – Persuading with Data]] (Kazakoff, MIT Sloan) je vizualizace jen část práce – za ní následuje struktura, přesvědčení a obhajoba. Hlavní doplňky k zásadám výše:
- **Exploring ≠ explaining:** publikum nevodit celou analýzou, „vzít ho rovnou ke zlatu“; Curse of Knowledge → [[Vysvětlování dat – tři výzvy]].
- **Graf jen pro vztah**, vybírat podle vztahu (kategorie, čas, část–celek, distribuce, korelace) → [[Výběr grafu podle vztahu v datech]]; preattentivní atributy a Gestalt → [[Vnímání grafů – preattentivní atributy a Gestalt]].
- **Data-ink ratio, vizuální hierarchie a „compared to what?“** – referenční čáry, anotace, žádné dvě osy y → [[Data-ink ratio a vizuální hierarchie]].
- **Headline místo titulku** (věta se slovesem), jeden bod na slide, testy self-sufficiency a blink → [[Headline a testy slidu]]. Odpovídá Sumpterovu „so what?“ výše.
- **Struktura sdělení shora dolů** (situace → komplikace → doporučení → body → data) → [[Minto pyramida]]; „report ve vrstvách“ výše je totéž z pohledu PKM.
- **WIIFT pro každé publikum** a rámcování (osobní, konkrétní, dřív, ztráta) → [[WIIFT a přesvědčování publika]]. Potvrzuje kontrolní otázku „zvládám přesvědčit uživatele o relevantnosti?“.
- **Prezentace grafu TOP-T** (téma → orient → pointa → přechod) → [[TOP-T – prezentace grafu]]; příprava na odpor → [[Audience Confusion Matrix]].
- Návrhy pro Sigmu → [[Persuading with Data – návrhy pro Sigmu]].

## Souvislosti

[[Yarmill]] · [[Karta hráče – koncept]] · [[Typy sportovních dat a datová architektura]] (matice relevance × frekvence; trenéři uvažují heuristicko-induktivně) · [[Video feedback a komunikace s hráči]] · [[Persuading with Data – návrhy pro Sigmu]] · [[Headline a testy slidu]] · [[Data-ink ratio a vizuální hierarchie]]
