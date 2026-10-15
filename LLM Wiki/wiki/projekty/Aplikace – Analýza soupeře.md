---
typ: projekt
tags: [aplikace, analyza-soupere, ai, skillcorner]
zdroje: ["[[Zdroj – Zadání aplikací]]"]
stav: vývoj
aktualizovano: 2026-10-15
---
# Aplikace – Analýza soupeře

Webová aplikace, která z dat dvou týmů vygeneruje pomocí AI taktickou přípravu na utkání (pracovně přejmenovat na **„Zápasová strategie“**). Výchozí tým SK Sigma Olomouc. Zdroj: [[SK Sigma Olomouc/Aplikace/Analýza herních dat/Analýza soupeře kompletní prompt|Analýza soupeře kompletní prompt]] (několik iterací zadání).

## Vývoj zadání

1. **API verze** – SkillCorner Python SDK, lokální DB (SQLite/Parquet + DuckDB), inkrementální updaty, dimenzní model (Dim_Player, Dim_Match, Dim_Team, Dim_Game_State…) a fact tabulky (Physical, Game Intelligence in/out of possession, Phases of Play, Positional).
2. **Aktualizace 2. 3. 2026** – přechod na **Dynamic Events** agregované po MatchID; výběr sezóny, soupeře, soutěží a období; Sigma stále předzpracovaná s datem aktualizace; možnost nahrát xlsx/CSV pro týmy bez API.
3. **Manuální data** – nahrávání CSV/XLSX/PDF (PlayerPossessions, Physical, PassingOptions, Passes, OnBallEngagements, OffBallRuns, In/OutOfPossession PDF, PlayerStats, TeamStats), sekce Metadata, chat nad daty, archiv, jazykové verze CZ/EN/ES/PL.

## Klíčový architektonický princip

AI nedostává syrová data: backend vyfiltruje, **normalizuje** ([[Normalizace herních dat]]) a spočítá odchylky/percentily → strukturovaný JSON → LLM napíše report.

## Struktura reportu

Základní charakteristika a rozestavení · pasáže utkání a game state · build-up · vedení útoku a finální fáze · presink a hra v bloku · chování ve vlastním vápně · **taktická syntéza** (naši hráči proti jejich) · profily hráčů soupeře.

## Zpětná vazba z používání (k doladění)

- Interpretace musí být podložená; místo kódů metrik srozumitelné názvy, čísla jednoznačně.
- Zohlednit rozestavení a **kdo chybí** (karty, nemoc); fakta a jména.
- Metadata se zdají ignorovaná – musí je brát v potaz.
- Kontext: % zisků bez celkového počtu nic neříká.
- Více prolnout silné/slabé stránky hráčů na pozicích proti sobě.
- Rozdělit na detailní report + krátký **insight report**; pozápasová analýza s vloženým plánem hry; analýza hráčů po utkáních; mazání dat podle zdrojového souboru; zálohování dat při nové verzi.

## Nápady

Skauting v české lize, průměrná a top data na pozicích, standardky, brankářská data.

> [!warning] Bezpečnost
> Zdrojová poznámka obsahuje přihlašovací údaje k SkillCorner v otevřeném textu – viz [[Zdroj – Zadání aplikací]].

## Souvislosti

[[SkillCorner]] · [[Hodnocení utkání a pozápasový report]] · [[Sigma Way]]
