---
typ: zdroj
tags: [zdroj, aplikace, ai, prompty]
cesta: "SK Sigma Olomouc/Aplikace/"
ingest: 2026-10-15
aktualizovano: 2026-10-15
---
# Zdroj – Zadání aplikací

Prompty a zadání aplikací, které Danů staví (většinou „vibe-coding“ s AI) pro klub. Každá aplikace má vlastní projektovou stránku.

| Zdroj | Projekt |
|---|---|
| [[SK Sigma Olomouc/Aplikace/Analýza herních dat/Analýza soupeře kompletní prompt\|Analýza soupeře kompletní prompt]] (velmi dlouhý, několik verzí zadání) | [[Aplikace – Analýza soupeře]] |
| [[SK Sigma Olomouc/Aplikace/Analýza herních dat/Post match report\|Post match report]] | [[Hodnocení utkání a pozápasový report]] |
| [[SK Sigma Olomouc/Aplikace/Zápas app - statistika/Aplikace zápas 🏟️\|Aplikace zápas 🏟️]] | [[Aplikace – Match tracker]] |
| [[SK Sigma Olomouc/Aplikace/Rezervační systém/Rezervační systém 🗓️\|Rezervační systém 🗓️]] | [[Aplikace – Rezervační systém]] |
| [[SK Sigma Olomouc/Aplikace/Analýza audio trenéř/Analýza audio trenéra 🎤 (vzdělávání trenérů)\|Analýza audio trenéra]] | [[Aplikace – Analýza audio trenéra]] |
| [[SK Sigma Olomouc/Aplikace/Klubová app/Strategická aplikace ⚡\|Strategická aplikace ⚡]] | [[Aplikace – Strategická aplikace]] |
| [[SK Sigma Olomouc/Aplikace/Skripty\|Skripty]] | Odkaz na lokální skript pro přepis audia (prepis_mac.sh) |

Související: [[SK Sigma Olomouc/Co platím 💶|Co platím 💶]] – placené služby (Render, Gemini API, AI překlad).

> [!warning] Bezpečnost
> Sekce „MOJE VERZE“ v poznámce *Analýza soupeře kompletní prompt* (a její kopie v *Apple Notes/Sigma Olomouc ⚽*) obsahuje **přihlašovací jméno a heslo k SkillCorner v otevřeném textu**. Vault se zálohuje do gitu. Doporučení: heslo z poznámek odstranit a změnit. Do wiki se nepřepisuje.

## Společné vzory napříč aplikacemi

- Stack: lokální vývoj → nasazení na **Render**; AI přes **Gemini API** (případně Claude).
- Opakující se požadavky: role a přístupová práva po skupinách, export (PDF/CSV/Excel), sdílení přes read-only odkaz, archiv/historie, chatovací okno nad daty, metadata/znalosti jako kontext pro AI.
- Princip „**AI nedostává syrová data**“ – backend agreguje a normalizuje, AI dostane zkomprimovaný JSON souhrn (viz [[Aplikace – Analýza soupeře]]).

## Souvislosti

- [[Normalizace herních dat]] · [[SkillCorner]] · [[Analýza trenérské komunikace]]
