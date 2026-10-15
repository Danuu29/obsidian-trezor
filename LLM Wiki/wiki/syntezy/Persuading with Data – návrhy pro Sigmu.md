---
typ: synteza
tags: [navrhy, sigma, yarmill, reporting, komunikace, vizualizace]
zdroje: ["[[Zdroj – Persuading with Data]]"]
aktualizovano: 2026-10-15
---
# Persuading with Data – návrhy pro Sigmu

*Syntéza / návrhy LLM*: co z [[Zdroj – Persuading with Data]] přenést do práce datového oddělení v [[SK Sigma Olomouc]] a do [[Yarmill]]. Nic není rozhodnuté – seznam k probrání. Předchozí knihy řešily **co měřit** (Soccermatics, The Numbers Game) a **jak rozhodovat** (Football Hackers); tato řeší **jak výsledek předat, aby podle něj někdo jednal**. Kniha je z byznysu → přenos do fotbalu je vždy návrh.

## Reporty a aplikace

1. **Headline nad každou sekcí reportu** (věta se slovesem: co z dat plyne), titulek nad grafem (co to je). V Yarmillu / aplikacích generovat headline automaticky z thresholdů nebo AI – a kontrolovat, že nepřestřelí data → [[Headline a testy slidu]], [[Hodnocení utkání a pozápasový report]].
2. **Každý graf odpovídá na „compared to what?“** – referenční čára thresholdu postu, průměr týmu, minulý zápas, plán. Bez srovnání graf nepublikovat → [[Data-ink ratio a vizuální hierarchie]], [[Thresholdy a benchmarky]].
3. **Šablona grafů Sigmy** (jednou nastavit, používat všude): sloupce od nuly, seřazeno podle hodnoty, popisky místo legendy, jedna zvýrazňující barva + šedá, barvoslepě bezpečný semafor (vedle barvy i symbol/text), čitelné písmo pro projektor v kabině i telefon → [[Vnímání grafů – preattentivní atributy a Gestalt]].
4. **Graf podle vztahu**: tabulka „otázka → vztah → graf“ jako součást dokumentace reportů (viz [[Výběr grafu podle vztahu v datech]]).
5. **Hodnoty jako poměry**: v reportech vedle absolutních čísel i per 90 / % / vůči normě – lidé reagují na poměry → [[Normalizace herních dat]], [[Audience Confusion Matrix]].
6. **Test Curse of Knowledge u aplikací**: novou obrazovku ukázat trenérovi, který ji vidí poprvé, bez vysvětlení – co přečte za 5 s? (blink test) → [[Aplikace – Analýza soupeře]], [[Aplikace – Match tracker]].

## Struktura sdělení

1. **Minto šablona pro návrhy vedení** (nákup dat, nový proces, posila): situace → komplikace → doporučení → 2–3 klíčové body → data; jedna strana → [[Minto pyramida]].
2. **Report o soupeři jako pyramida**: „jak ho porazíme“ → 3 oblasti → klipy/data; odpovídá struktuře „co dělají → jak na to“ z Barça kurzu → [[Analýza soupeře – metodika]].
3. **Žádné „intelektuálně prázdné“ shrnutí** („analýza přinesla tři zjištění“) – vždy co z toho plyne.
4. **Metodika až na konec / do přílohy** pro trenéry a vedení; pro kondiční a odborné publikum dřív.

## Publikum a přesvědčování

1. **Mapa publik a jejich WIIFT** (hlavní trenér, asistenti, kondice, medicína, vedení, trenéři mládeže, hráči, rodiče) – co z dat má každá skupina; u každého nového reportu vyplnit → [[WIIFT a přesvědčování publika]].
2. **Rámec ztráty u zátěže a zdraví**: „přicházíme o X hráčodnů“ místo „zlepšíme dostupnost“; konkrétně („Pavel nebude v sobotu fit“) místo abstraktně.
3. **Budovat goodwill a „půjčovat si rank“**: analytik bez trenérské minulosti prezentuje přes asistenta / kondičního trenéra; drobná pomoc štábu dřív, než něco potřebuje → [[Oddělení analýzy – struktura a role]].

## Porady a prezentace

1. **TOP-T na poradách štábu**: u každého grafu orient (osy, metrika, jeden příklad hráče), pak pointa; žádné „ta-da“. U pravidelných reportů, které štáb zná, stačí tichý orient → [[TOP-T – prezentace grafu]].
2. **Před poradou s „nepříjemnými“ daty určit kvadrant** Audience Confusion Matrix; u kvadrantu 4 (zásah nepřinesl efekt – blok tréninku, posila, nový trenér) připravit data do detailu, předem je projít s klíčovou osobou a přinést plán, jak získat chybějící informace → [[Audience Confusion Matrix]].
3. **„Změnila by to rozhodnutí?“** jako standardní odpověď na námitky k datům (citlivostní test) – a závazek k práci navíc tam, kde ano.
4. **Zapisovat očekávání předem** (co čekáme od tréninkového bloku, posily, změny) – usnadní komunikaci výsledku a brání hindsight biasu → [[Kognitivní zkreslení v hodnocení]], „deník rozhodnutí“ v [[The Numbers Game – návrhy pro Sigmu]].

## Pro Yarmill (produkt)

1. Dashboardy s **místem pro headline** nad grafy a s podporou referenčních čar / thresholdů → [[Analytické balíčky Yarmill]].
2. [[Yollanda]] může psát headline a orient ke grafům (TOP-T v textu) – vhodný prompt: „napiš pointu jako větu se slovesem, jen co data ukazují, s porovnáním vůči normě“.

## Souvislosti

[[Principy vizualizace a reportingu]] · [[Football Hackers – návrhy pro Sigmu]] · [[The Numbers Game – návrhy pro Sigmu]] · [[Barça kurz – návrhy pro Sigmu]] · [[Otevřené otázky]] · [[Přehled wiki]]
