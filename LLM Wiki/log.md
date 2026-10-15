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
