---
typ: projekt
tags: [projekt, pkm, druhy-mozek, wiki, obsidian, llm]
zdroje: ["[[Zdroj – Pořiďte si druhý mozek]]"]
stav: v provozu
aktualizovano: 2026-10-15
---
# Druhý mozek – LLM Wiki

Tato wiki jako projekt: osobní „druhý mozek“ Danů ve složce `LLM Wiki/` v Obsidian vaultu, který **píše a udržuje LLM** a Danů do něj vybírá zdroje a klade otázky. Pravidla jsou ve schématu [[CLAUDE]], historie v [[log]].

## Stav (k 2026-10-15)

- Založena 15. 10. 2026; **14 zdrojových stránek** – 9 ze stávajících poznámek ve vaultu a 5 externích (Barça kurz, Soccermatics, Football Hackers, The Numbers Game, Pořiďte si druhý mozek).
- Těžiště: datová analytika a rozvoj hráčů v [[SK Sigma Olomouc]]; od tohoto ingestu i **osobní efektivita a práce se znalostmi**.
- Workflow: Danů ukládá zdroje do `raw/` (web přes **Obsidian Web Clipper**, PDF ručně) a **ingest spouští sám** v novém chatu projektu – bez plánovaného automatického ingestu.

## Wiki optikou metody CODE (*syntéza LLM*)

| Krok [[Metoda CODE|CODE]] | Kdo | Ve wiki |
|---|---|---|
| **C – zaznamenat** | Danů | výběr zdrojů do `raw/`, poznámky ve vaultu (surové zdroje, neměnné) |
| **O – uspořádat** | LLM | třídění do `zdroje/ entity/ koncepty/ projekty/ syntezy/`, [[index]], odkazy |
| **D – zhustit** | LLM | zdrojové stránky („Hlavní myšlenky“ = vrstva 4), koncepty, [[Přehled wiki]] |
| **E – vyjádřit** | Danů (+ LLM návrhy) | syntézy „návrhy pro Sigmu“, odpovědi na dotazy, reálné výstupy (reporty, aplikace) |

Oproti knize se mění dělba práce: kroky O a D, které Forte popisuje jako ruční a časově náročné, dělá LLM; člověku zůstává výběr (C) a výstup (E). Proto ingest probíhá **předem** (just-in-case), ne až při potřebě, jak radí kniha → napětí popsané v [[Druhý mozek – návrhy pro wiki a práci]].

## Otevřené body

- Chybí vrstva **oblastí** a **archivu** ve smyslu [[PARA – organizace podle akčnosti|PARA]] – zatím jen projekty (aplikace) a syntézy.
- Vlastní výstupy Danů (reporty, prompty, prezentace) se do wiki zatím nevracejí → [[Dílčí balíčky a znovuvyužití práce]].
- Kandidáti na ingest z vaultu: *4.0 Kondiční koncepce*, *DATOVÉ PARAMETRY POSTŮ*, *Analýza koučinku Lausman* (viz [[index]]).
- Rytmus údržby (ingest `raw/`, lint, revize přehledu) není stanovený → [[Revize a návyky druhého mozku]].

## Souvislosti

[[Druhý mozek – návrhy pro wiki a práci]] · [[Metoda CODE]] · [[Aplikace – Strategická aplikace]] · [[Přehled wiki]] · [[Otevřené otázky]]
