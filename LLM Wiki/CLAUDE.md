# LLM Wiki – schéma a pravidla

Tento soubor je „konfigurace“ wiki. Každý agent (Claude, Codex…), který na wiki pracuje, ho čte jako první a řídí se jím. Schéma vyvíjíme společně s Danů – když se nějaký postup osvědčí nebo neosvědčí, uprav tento soubor a zapiš to do logu.

## Účel

Osobní „druhý mozek“ Danů: práce (datová analytika ve fotbale – SK Sigma Olomouc, Yarmill), sportovní věda, trénink, osobní rozvoj a efektivita. Wiki je **trvalý, průběžně rostoucí artefakt** – znalosti se zkompilují jednou při ingestu a pak se jen udržují aktuální, ne se znovu dohledávají při každé otázce.

Role: **Danů** vybírá zdroje, směruje analýzu a klade otázky. **LLM** píše a udržuje celou wiki (souhrny, křížové odkazy, rozpory, index, log). Danů wiki čte v Obsidianu, do `wiki/` ručně nepíše.

## Tři vrstvy

1. **Surové zdroje (LLM je jen čte, nikdy neupravuje)** – dva druhy:
   - **`LLM Wiki/raw/`** – cizí materiál bez jiného domova: články z Web Clipperu, PDF, knihy, studie, přepisy videí. Po uložení se **nemění**. Obrázky do `raw/assets/`.
   - **Vlastní poznámky Danů** ve zbytku vaultu (např. `SK Sigma Olomouc/`, `Meetings/`, `Znalosti/`, `VIF Cycling team 🚴/`, `Osobní rozvoj/`) – meetingy, zadání aplikací, nápady. Jsou **živé**: Danů je průběžně doplňuje, takže se při dalším ingestu mohou změnit → zdrojovou stránku pak aktualizovat, ne zakládat novou.
   - **Vyloučeno z wiki** (neingestovat, na změny nereagovat):
     - `Úkoly/` – kanban a seznamy úkolů se mění denně; wiki nemá sledovat stav úkolů
     - `Markdown – tahák.md`, `.obsidian/`, `.trash/`
     - jakákoli poznámka s `wiki: ne` ve frontmatteru
     Seznam drží i skript `nastroje/nove.py` (proměnná `EXCLUDE`) – při změně upravit obojí.
2. **Wiki (vlastní ji LLM)** – `LLM Wiki/wiki/`
   - `zdroje/` – jedna stránka na zdroj nebo ucelenou skupinu zdrojů (souhrn, klíčová zjištění, co ze zdroje vyplývá pro wiki).
   - `entity/` – organizace, týmy, programy, nástroje a datové platformy (Yarmill, SkillCorner, VALD…).
   - `koncepty/` – metodiky, pojmy, principy (IDP, thresholdy, GPS metriky…).
   - `projekty/` – aplikace a projekty, na kterých Danů pracuje (stav, zadání, otevřené body).
   - `syntezy/` – přehledy, srovnání, analýzy, rozpory, otevřené otázky, uložené odpovědi na dotazy.
3. **Schéma** – tento soubor.

Speciální soubory: `index.md` (katalog obsahu) a `log.md` (chronologický záznam).

## Konvence stránek

- Jazyk: **čeština**. Odborné termíny v originále (ACWR, HID, PSV-99, TIP/OTIP, IDP…).
- Název souboru = název stránky, bez emoji. Typové prefixy: zdroje začínají `Zdroj – `, aplikace `Aplikace – `.
- **Názvy nesmí kolidovat** s žádnou jinou poznámkou ve vaultu (Obsidian odkazuje podle názvu souboru). Před vytvořením stránky ověř: `find . -name "<název>.md"`.
- Každá stránka má YAML frontmatter:

```yaml
---
typ: zdroj | entita | koncept | projekt | synteza
tags: [..]
zdroje: ["[[Zdroj – …]]"]      # z jakých zdrojových stránek stránka čerpá
aktualizovano: RRRR-MM-DD
---
```

  Zdrojové stránky mají navíc `cesta:` (cesta k surovému zdroji) a `ingest:` (datum).
- Struktura těla: 1–2 věty shrnutí nahoře → obsah v sekcích → `## Souvislosti` (odkazy na související stránky) → u konceptů a entit `## Otevřené otázky`, pokud nějaké jsou.
- **Odkazy:** na wiki stránky `[[Název]]`; na surové zdroje **plnou cestou** `[[SK Sigma Olomouc/Analytická témata/Předsezóní testování|Předsezóní testování]]` (ve vaultu jsou duplicitní názvy). Na stránky FIFA Talent ID Guide lze odkazovat přímo názvem (např. `[[Biologické zrání]]`), jsou unikátní. Obsidian má zapnuté „Vždy aktualizovat interní odkazy“ – když Danů poznámku přesune, odkazy přepíše sám (i na kratší tvar); lint pak hlídá jen nejednoznačnost. Frontmatter `cesta:` u zdrojových stránek ale aktualizuj ručně.
- Tvrzení podložit zdrojem (odkaz na zdrojovou stránku nebo surovou poznámku). Vlastní syntézu LLM označit jako *syntéza* nebo *návrh*.
- **Rozpory** mezi zdroji nemazat ani tiše nesjednocovat – na stránce je označit callout `> [!warning] Rozpor` a zapsat do [[Rozpory a nesrovnalosti]].
- Nejistá místa (zkomolené přepisy) značit „(?)“.

## Soukromí a citlivé údaje

- **Nikdy do wiki nekopírovat přihlašovací údaje, hesla, API klíče** (i když jsou ve zdroji). Na jejich výskyt ve zdroji Danů upozornit.
- Zdravotní údaje konkrétních hráčů/závodnic (zranění, nemoci, vyšetření) do wiki nepsat – jen obecné procesy.
- Konkrétní (často nezletilí) hráči: nezakládat jim vlastní stránky; zmínit jen tam, kde jde o modelový případ procesu, a odkazovat na zdroj.

## Workflow

### Ingest (nový zdroj)
1. Danů vloží zdroj do `raw/` (nebo ukáže na poznámku ve vaultu) a řekne „ingestuj“. Na pokyn **„ingestuj vše nové“** nejdřív spusť `python3 "LLM Wiki/nastroje/nove.py"` (z kořene vaultu) – vypíše nové/změněné vlastní poznámky od posledního ingestu (podle git hashe v logu), smazané poznámky a nezpracované soubory v `raw/`. Seznam ukaž Danů a zpracuj.
2. LLM zdroj přečte celý (obrázky/PDF zvlášť), krátce s Danů probere klíčová zjištění a na co klást důraz.
3. Vytvoří `wiki/zdroje/Zdroj – <název>.md`.
4. Aktualizuje nebo založí dotčené entity, koncepty, projekty (typicky 5–15 stránek). Doplní obousměrné odkazy.
5. Zkontroluje rozpory se stávající wiki → callout + [[Rozpory a nesrovnalosti]]. Nové otevřené otázky → [[Otevřené otázky]].
6. Aktualizuje `index.md` a [[Přehled wiki]], pokud se změnil obraz celku.
7. Připíše záznam do `log.md`. **Záznam ingestu vlastních poznámek musí obsahovat řádek `- git: <hash>`** = výstup `git rev-parse --short HEAD` v okamžiku čtení zdrojů (podle něj `nove.py` pozná, co je nového příště).
8. Změněná živá poznámka: aktualizuj existující zdrojovou stránku (`aktualizovano:`) a dotčené stránky; co už neplatí, přepiš a v logu uveď, co se změnilo. Smazaná poznámka: odkazy na ni nahraď textem a zmiň v logu.

### Dotaz (query)
1. Přečti `index.md`, pak relevantní stránky (případně surové zdroje).
2. Odpověz s odkazy na stránky wiki.
3. Pokud je odpověď hodnotná (srovnání, analýza, nové propojení), nabídni ji uložit do `wiki/syntezy/` a zapiš do indexu a logu.

### Lint (kontrola zdraví)
Na pokyn „udělej lint“: rozbité odkazy, sirotci (stránky bez příchozích odkazů), kolize názvů s vaultem, stránky bez frontmatteru, zastaralá tvrzení, rozpory, pojmy zmíněné bez vlastní stránky, chybějící křížové odkazy, mezery v datech (návrh webového dohledání). Mechanickou část dělá skript: `python3 "LLM Wiki/nastroje/lint.py"` (spouštět z kořene vaultu). Obsahovou část (rozpory, zastaralost, mezery) dělá LLM čtením. Výsledek do logu, opravy po odsouhlasení.

## Log

`log.md` je append-only. Každý záznam začíná hlavičkou:

```
## [RRRR-MM-DD] ingest | Název zdroje
## [RRRR-MM-DD] dotaz | Otázka
## [RRRR-MM-DD] lint | Shrnutí
## [RRRR-MM-DD] schéma | Co se změnilo
```

Posledních 5 záznamů: `grep "^## \[" "LLM Wiki/log.md" | tail -5`.

## Git

Vault je git repozitář (obsidian-git dělá automatické zálohy). Wiki tak má historii verzí zdarma – před velkým refaktorem wiki stačí počkat na zálohu nebo commitnout.
