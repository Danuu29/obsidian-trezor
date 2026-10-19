---
typ: koncept
tags: [gps, zatizeni, kondice]
zdroje: ["[[Zdroj – Znalosti]]", "[[Zdroj – Yarmill poznámky]]", "[[Zdroj – Úkoly]]", "[[Zdroj – Soccermatics]]", "[[Zdroj – Tréninkový deník (cyklistika)]]"]
aktualizovano: 2026-10-19
---
# GPS metriky a zatížení

Odborné poznatky a požadavky na práci s GPS daty (Catapult) v Sigmě. Hlavní zdroj: [[Znalosti/📡 GPS Data|📡 GPS Data]], doplněk *GPS (Yarmill)* (smazaná poznámka z Apple Notes).

## Pásma a metriky

- Rychlostní zóny: 1 chůze · 2 regenerační výběh · 3 aerobní běh · 4 anaerobní běh · 5 **HID (70–90 % max. rychlosti)** · 6 **sprint (≥ 90 % max. rychlosti)**
- Základní metriky: TD, ACC, DEC, SD, HIR; intenzity (TD/min…); max. akcelerace a decelerace.
- **Player Load** – odhad celkové zátěže; nepřesný (započítává i pohyby nahoru/dolů).
- **ACWR** – lépe počítat z (1) akcelerací a decelerací, (2) Player Load. Námět: EWMA jako alternativa. Obdoba v osobním tréninku: session RPE (RPE × minuty) a poměr akutní/chronické zátěže s pásmem 0,8–1,3 → [[Zdroj – Tréninkový deník (cyklistika)]].
- Rozdíl acc vs. dec do 20 % je v pořádku.

## Pravidla pro interpretaci

- Střídající hráč by měl naběhat za minutu ~1,2× více než hráč ze základu.
- Trénink vs. zápas srovnávat jen po přepočtu na **čistý čas hry** → na minutu hry.
- Malé formy her: poměr hřiště 1,5 : 1, ~320 m² na hráče (ideální minimum 160 m²).
- Sledovat zatížení levé a pravé strany.
- Kontext: vliv držení míče na běžecká data, vztah běžeckých a herních dat, readiness/[[Whoop]], Hooperův dotazník, rozestavení a taktický záměr (tagy aktivit).
- „Trenéři chtějí informace, ne čísla.“ Literatura: Buchheit.

## Reporting – požadavky

- Srovnání s **průměrem top 3 zápasů**, „% odběháno oproti topu“; šedé pole s referencí v indy reportu.
- Report porovnání dvou aktivit; detail aktivity/tréninku; přehled ACWR z předešlého dne.
- Nastavení SET 1 / SET 2 (relativní hodnoty SET 2 pro A, U19+U18, U17+U16); individuální thresholdy a mikrocyklus od Patrika → [[Thresholdy a benchmarky]].
- Upozornění na přetížení (nárůst zatížení); parametry za minutu ve filtru; přepínač absolutní hodnoty / intenzity.
- Zápas: nastavení dalšího mikrocyklu, progres top speed, průměrná pozice týmu v DEF/OFF fázi.

## Kongesce a synchronizace (Soccermatics)

Při 3 dnech mezi zápasy měl tým PL stejné běžecké objemy, ale **nižší týmovou synchronizaci** pohybu než při 6+ dnech → únava se může projevit takticky/kognitivně dřív než v GPS ([[Zdroj – Soccermatics]], Kap. 9) → [[Pressing a kolektivní pohyb]].

## Souvislosti

[[Denní připravenost a wellness]] · [[SkillCorner]] (tracking z videa jako doplněk GPS) · [[Karta hráče – koncept]] · [[Tréninkové zóny a prahy]] (individuální zóny z laboratorního testu – vytrvalostní obdoba) · [[Zdroj – Tréninkový deník (cyklistika)]] (session RPE a A/C v praxi)
