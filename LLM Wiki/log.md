# Log LLM Wiki

Chronologický, append-only záznam. Formát hlavičky: `## [RRRR-MM-DD] typ | název`. Posledních 5: `grep "^## \[" log.md | tail -5`.

## [2026-10-15] schéma | Založení wiki

- Vytvořena struktura `LLM Wiki/` (raw/, wiki/zdroje|entity|koncepty|projekty|syntezy), schéma [[CLAUDE]], [[index]], tento log.
- Rozhodnutí: osobní „druhý mozek“, česky; stávající poznámky ve vaultu = neměnné surové zdroje (čtou se na místě, nekopírují se); `Apple Notes/Sigma Olomouc ⚽/` jsou duplikáty → neingestovat.

## [2026-10-15] ingest | Počáteční ingest celého vaultu

- 9 zdrojových stránek (≈ 95 poznámek), 13 entit, 17 konceptů, 6 projektů, 4 syntézy.
- Zjištěné rozpory: normy VALD (Nordic, ISO PRONE, asymetrie, AB/AD, flexe/extenze), škála hodnocení → [[Rozpory a nesrovnalosti]].
- Bezpečnost: v poznámce *Analýza soupeře kompletní prompt* (a kopii v Apple Notes) je heslo k SkillCorner v otevřeném textu – nepřeneseno, doporučeno odstranit a změnit.
- PDF a obrázky zatím neingestovány (jen odkazy v indexu).

## [2026-10-15] ingest | Barça Match Analysis (kurz, 16 PDF)

- Zdroj: 16 PDF kurzu match analysis od Barça Innovation Hub, uloženo do `raw/Barca Match Analysis/`. Skeny bez textu → OCR + vizuální kontrola tabulek; nejistá místa „(?)“.
- Nové: [[Zdroj – Barça Match Analysis]]; entity [[Barça Innovation Hub]], [[Mediacoach]]; 17 konceptů (plány analýzy, IFP, obranná linie, herní cyklus, analýza soupeře, operativní strategie, mikrocyklus MD, standardky, pre-match, live a poločas, video feedback, sezónní hodnocení, analýza tréninku, taktická komunikace, oddělení analýzy, typy dat, tagging); syntéza [[Barça kurz – návrhy pro Sigmu]].
- Aktualizováno: Hodnocení utkání a pozápasový report, Aplikace – Analýza soupeře, Aplikace – Match tracker, Analýza trenérské komunikace, Postové profily, Sigma Way, Skauting, Principy vizualizace, Normalizace herních dat, Wyscout, StatsBomb, SK Sigma Olomouc, Mapa datových zdrojů, Otevřené otázky, Přehled wiki, index.
- Rozpory: žádné věcné. Terminologická nesrovnalost – španělské číslování postů (P2 = krajní obránce) vs. značení v Postových profilech → zapsáno do Otevřených otázek, ne do Rozporů.
- Ingest proběhl bez úvodní diskuse o důrazech (Danů zadal „zapracuj“) – důrazy lze doladit zpětně.

## [2026-10-15] ingest | Soccermatics (D. Sumpter, 2016)

- Zdroj: kniha *Soccermatics – Mathematical Adventures in the Beautiful Game* (Pro-Edition, 293 s.), uložena do `raw/Soccermatics (Sumpter 2016).pdf`. PDF s textovou vrstvou; čtení po částech (I–IV), vzorce z obrázků chybí → dopočty označeny.
- Nové: [[Zdroj – Soccermatics]]; entity [[Opta]], [[Brentford a FC Midtjylland]]; 7 konceptů ([[Expected goals (xG)]], [[Possession value a Markovovy řetězce]], [[Pasové sítě a prostorové mapy]], [[Pressing a kolektivní pohyb]], [[Half-spaces a taktická geometrie]], [[Predikce a pravděpodobnostní modely]], [[Datový skauting – metriky a úskalí]]); syntéza [[Soccermatics – návrhy pro Sigmu]].
- Aktualizováno: StatsBomb, SkillCorner, Wyscout, Sigma Way, Normalizace herních dat, Principy vizualizace, Skauting, Oddělení analýzy, Typy dat, Hodnocení utkání, GPS metriky, Aplikace – Analýza soupeře, Mapa datových zdrojů, Otevřené otázky, Přehled wiki, index.
- Rozpory: žádné věcné. Zpřesnění, ne rozpor: represink „do 6 s“ (Sigma Way) vs. data Prozone 2,5 s / 5,5 s. Napětí: „herní dominance“ vs. zjištění, že držení míče samo góly nepředpovídá (poznamenáno na Sigma Way).
- Kniha je z let 2016–17 → zastaralá tvrzení (firmy, role lidí, stav tracking analýzy) označena calloutem „Aktualita“ jako poznámka LLM k ověření.
- Ingest bez úvodní diskuse o důrazech (Danů zadal „zpracuj“); důraz dán na přenositelnost do klubové analytiky, analogie mimo fotbal (biologie, davy) vynechány.
