---
datum: 2026-10-19
aktualizovano: 2026-10-19
typ: souhrn
zdroj: konverzace s Claude
projekt: SK Sigma Olomouc – analytika
tags: [sigma, eyeball, data, analytika, metriky]
aliases: [Eyeball data, Eyeball metriky]
---
[]()# Eyeball – platforma, data a metriky

> Souhrn všeho, co víme o datech v Eyeballu (portal.eyeball.club): jaké datové oblasti platforma nabízí, jak se data dají získat a jak je teď dočasně stahujeme skriptem, než bude k dispozici oficiální API. Zjištěno průzkumem portálu (říjen 2026) – webu, jeho vnitřního rozhraní a dat k vybraným zápasům a hráčům. Obecně platné pro klub, bez konkrétních počtů Sigmy. Jednotlivé metriky jsou ve [[Eyeball – slovník metrik|slovníku metrik]].

## Kontext a cíl

- Cíl: zjistit, co vše nám Eyeball dokáže dát za data, v jakém detailu, a mít je v tabulkách pro vlastní analýzy (individuální rozvoj hráčů, hodnocení zápasů, skauting, reporting).
- Oficiální cesta k datům je API – jednání s Eyeballem viz [[SK Sigma Olomouc/Meetings/2026-10-19 – Eyeball – Martin Neoral|2026-10-19 – Eyeball – Martin Neoral]]. Do té doby stahujeme data skriptem z portálu (viz [[#Jak data stahujeme teď]]).

## Co je Eyeball z pohledu dat

- Provozovatel: **Eyeball s.r.o.**, Praha (IČ 096 74 454). Rozhraní:
  - **Portal** (`portal.eyeball.club`) – klubová aplikace: hráči, zápasy, statistiky, video. Odsud bereme data.
  - **Discover** (`discover.eyeball.club`) – další aplikace Eyeballu (v portálu se k ní vážou „kredity Discover“).
  - **Hráčská aplikace** (vlastní zásady ochrany osobních údajů).
- Zápasy se natáčejí na video a analýzu (otagování událostí) dělá **externí poskytovatel** – v datech zápasu je uveden (např. `SPORTLOGIQ`) spolu s úrovní zpracování (`processingLevel`, např. `full`) a informací, zda jsou otagované oba týmy.
- Data k zápasu jsou dostupná až po **dokončení analýzy** (`isAnalysisFinished`, `isAnalysisApproved`). Do té doby portál statistiky ani události nevydá (odpoví „zakázáno“); **sestava** je ale k dispozici i u neanalyzovaného zápasu (bez hodnocení).
- Pokrývá mládež (U13–U19) i dospělé; data jsou vždy za **oba týmy** zápasu (i soupeře).

### Role, oprávnění a kredity

- Uživatel má roli (např. `ROLE_COACH` – trenér). Co vidí a smí stahovat, určují **oprávnění u každého zápasu**:
  - zobrazení: statistiky hráčů, týmové statistiky, události, hodnocení (rating), fyzická analýza, datové insighty, komentáře k událostem
  - stažení: události, statistiky hráčů, týmové statistiky, video
  - práce: klipy, oblíbené, úprava skóre, nahlášení chyby v události, nástrojová lišta a tipy pro trenéra
  - AI: AI shrnutí zápasu (funkce / obsah), AI review trenéra, hodnocení hráčů skauty (`playerGrading`) – běžný trenérský účet je nemá
  - omezení na vybrané hráče (`allowedPlayers`)
- Oprávnění týmu v zápase: úprava soupisky, barev dresů, čísel, pohlaví, odebrání hráčů, anonymizace hráčů, úprava odznaků hodnocení a review.
- **Kredity (tokeny):** vlastní měna Eyeballu na účtu klubu/týmu. Pohyby: nákup, dárek, převod z klubu do týmu, vrácení platby, odebrání, **předplatné**, **sdílená analýza**. Spravuje je administrátor klubu / týmu nebo Eyeball – trenérský účet je nevidí. Čtení a stahování dat mezi pohyby kreditů **není** (zjištěno z kódu portálu, ne z vyúčtování).

## Přehled datových oblastí

| Oblast | Úroveň | Co obsahuje |
|---|---|---|
| Databáze hráčů / vyhledávání statistik | hráč za období | profil + ~40 metrik **na 90 min**, filtry, srovnání s databází |
| Seznam zápasů | zápas | datum, kategorie, typ, týmy, skóre, stav analýzy |
| Statistiky hráče v zápase | hráč × zápas | ~80 metrik **absolutně** za zápas, vč. xG/xA a brankářských |
| Týmové statistiky zápasu | tým × zápas | 62 metrik domácí vs. hosté, vč. držení míče |
| Sestavy | hráč × zápas | číslo, pozice, minuty, hodnocení, základ/střídající |
| Události (event data) | jednotlivá akce | čas na desetiny sekundy, místo na hřišti, typ, úspěch, detaily |
| Profil hráče | hráč | výkon, radar, percentily, behaviorální signály, fyzické a tělesné údaje, historie |
| Fyzická data | hráč za sezónu / zápas | rychlosti, vzdálenost, akcelerace, rychlostní zóny; k zápasu PDF report |
| Hodnocení a „měkká“ data | hráč × zápas | rating, hodnocení trenéra, odznaky, AI shrnutí |
| Video a klipy | zápas | stream / stažení videa, klipy, komentáře k událostem |

## 1. Databáze hráčů a vyhledávání statistik

Stránka „Statistiky hráče“ (`/player-stats-search`).

- **Filtry:** název klubu, tým, věková kategorie týmu, jméno hráče, silnější noha, pozice, pohlaví, rok narození (rozsah), **období** (datum od–do) nebo **sezóna**, rozsahy statistik (min. minuty, zápasy, góly…), národnost.
- **Předvolby:** uložené sady sloupců (výchozí „Vše“, „General“) a uložené sady filtrů.
- „Statistiky jsou porovnávány se všemi hráči v naší databázi“ – srovnání v rámci celé databáze Eyeballu.
- **Údaje o hráči:** ID, jméno, příjmení, pohlaví, rok narození, klub, tým (soutěž), věkové kategorie, úroveň týmu, pozice (všechny odehrané), silnější noha, výška, váha, národnost, počet zápasů, minuty (celkem, v mužských a v ženských soutěžích), starty v reprezentaci.
- **Metriky:** stejné oblasti jako ve statistikách zápasu (rating, góly, asistence, střely, přihrávky, centry, souboje, zachycení, odkopy, bloky, získané míče, kličky, brankářské), ale **přepočtené na 90 minut** (ověřeno: 2 góly za 1425 min = 0,126). Absolutní jsou jen `totalGoals` a `totalAssists`.
- Sezóna se v datech značí koncovým rokem: `2027` = sezóna 2026/2027.

## 2. Zápasy

- **Seznam zápasů klubu:** ID, datum, kategorie (U13–U19…), typ (`championnat` mistrovský, `amical` přátelský, `coupe` pohárový), domácí/hosté (tým i klub), skóre, loga, zda je analýza hotová, oblíbené.
- **Detail zápasu:**
  - poločasy: oficiální délka, nastavení, začátek a konec v čase zápasu i ve videu, na které straně začínal domácí tým
  - týmy: klub, soutěž, kategorie, barvy dresů a trenýrek, průměrné hodnocení týmu
  - video: stream, náhled, odkaz ke stažení
  - **sestavy** – u každého hráče: číslo, jméno, ID hráče, ročník, pohlaví, pozice, základ/střídající, odehrané minuty, hodnocení, hodnocení trenéra, hodnocení skautů, fotka, anonymizace
  - nabídka **rozestavení** pro soupisku: 4-3-3 ofenzivní, 4-3-3, 4-3-2-1, 4-3-1-2, 4-4-2 v řadě, 4-4-2 kosočtverec, 4-2-4, 4-4-1-1, 4-5-1, 3-5-2, 3-4-3, 3-4-1-2, 5-3-2, 5-4-1, 5-2-1-2
  - export soupisky: CSV, PDF, XLSX

## 3. Statistiky, týmové metriky a události

Kompletní metriky s definicemi a nástrahami jsou ve [[Eyeball – slovník metrik|slovníku metrik]]. Ve zkratce:

- **Statistiky hráče v zápase** – kolem 80 metrik absolutně za zápas pro hráče obou týmů: rating, góly, asistence, střely, xG/npxG/xA, přihrávky po třetinách, délce a směru, centry, standardky, souboje, zachycení, odkopy, bloky, získané míče, chyby, karty a brankářský blok.
- **Týmové statistiky zápasu** – 62 metrik domácí vs. hosté ve skupinách Souhrn (vč. držení míče), Útok, Obrana, Rozehrávka.
- **Události (event data)** – kompletní seznam akcí obou týmů: 24 typů, čas na desetiny sekundy, čas ve videu, hráč, úspěch, místo na hřišti a detailní atributy (xG, xA, délka a směr přihrávky, místo v bráně, typ souboje…). Z nich jde počítat výkon po časových úsecích, mapy akcí a střel, heatmapy ztrát a zisků, standardky.

## 4. Profil hráče

Sekce profilu (každá s vlastními filtry – sezóna, pozice, posledních N zápasů):

- **Hlavička:** datum narození, výška, váha, pozice a druhá pozice, národnost (i druhá), silnější noha, klub a týmy, reprezentace, poznámky, typ (partnerský / Discover / nepartnerský hráč).
- **Výkon (performance):** metriky na 90 min ve skupinách útok / obrana / rozehrávka / brankář; filtry pozice, sezóna, „Overall“ nebo posledních N zápasů.
- **Radar výkonu:** 6 metrik podle pozice s hodnocením a **percentilem** (např. u stoperů hlavičky, přihrávky, souboje, získané míče, odkopy, bloky).
- **Sezónní statistiky:** zápasy, minuty, góly, asistence po sezónách.
- **Výjimečné metriky (standout):** metriky, ve kterých je hráč nejlepší, s údajem „top X %“; filtr celkově / poslední zápas / 5 / 10 zápasů.
- **Průměrné hodnocení:** průměrný rating, změna, percentil, poslední hodnocení.
- **Klíčové události s videem:** vybrané akce hráče po kategoriích s odkazem na video.
- **Typy událostí s počty:** kolikrát hráč provedl jednotlivé typy akcí (i odvozené: střela na branku, zblokovaná střela, centr, asistence).
- **Zápasy hráče:** seznam se skóre, ratingem, minutami a góly; filtry sezóna, tým, jen analyzované, národní zápasy.
- **Historie klubů** po sezónách.
- **Behaviorální signály** – jak hráč snáší tlak zápasu (tolerance, citlivost, zotavení) proti kohortě; definice ve [[Eyeball – slovník metrik|slovníku metrik]].
- **Behaviorální archetypy:** dominantní a vedlejší archetyp hráče (u běžných hráčů zatím „nedokončeno“).
- **Biometrie a tělesné míry:** sken těla – obvody horní a dolní poloviny těla, celotělové míry, změny tělesného složení, trendy (jen pokud má hráč skeny a jsou sdílené).
- **Fyzické metriky** (viz další sekce).
- **Náborové informace:** zda je hráč otevřen nabídkám.
- **Stínový tým (shadow team)** a oblíbení hráči – skautingové nástroje.

## 5. Fyzická data

- **Na profilu hráče za sezónu:** maximální a průměrná top rychlost, uběhnutá vzdálenost na 90 min, akcelerace a decelerace, rozložení pohybu v šesti rychlostních zónách. Definice ve [[Eyeball – slovník metrik|slovníku metrik]].
- **K zápasu:** jen **PDF report** a video fyzické analýzy; datový soubor za ním je zamčený.
- Fyzickou analýzu nemá každý zápas – zatím jen část zápasů (dle schůzky půjde o placenou nadstavbu nové verze).

## 6. Hodnocení a „měkká“ data

- **Rating** hráče za zápas (cca 0–10, průměrný výkon kolem 6–7) a průměrné hodnocení týmu.
- **Hodnocení trenéra** a **hodnocení skautů** u hráče v zápase.
- **Odznaky (rating badges)** – 20 typů, které jde hráči udělit za zápas (seznam ve [[Eyeball – slovník metrik|slovníku metrik]]).
- **AI:** AI shrnutí zápasu, AI review trenéra, AI vyhledávání hráčů pro skauty („scout search“ s předpřipravenými dotazy) – vyžadují oprávnění.
- **Hráči týdne** podle typu (góly, asistence, střely, kličky, přihrávky dopředu, hlavičky) a zvýraznění hráči.

## 7. Video a klipy

- Video zápasu jako stream, náhled, odkaz ke stažení (při oprávnění).
- Klipy z událostí, klipy přes více zápasů hráče, sdílené klipy (i chráněné heslem), komentáře k událostem, kolekce a oblíbené.

## 8. Exporty přímo v portálu

- Statistiky hráčů / týmu zápasu: **CSV, JSON, XLSX, XML**.
- Události zápasu: export.
- Soupiska: CSV, PDF, XLSX.
- Exporty jsme zatím nepoužili (nevěděli jsme, zda nečerpají kredity – podle kódu ne, ověřit u správce kreditů).

Pozice (francouzské kódy), záludnosti v datech a číselné hranice: viz [[Eyeball – slovník metrik]].

## Co platforma neposkytuje

- cíl přihrávky (kam šla), tracking (polohy všech hráčů v čase), fyzická data zápasu jako data (jen PDF), statistiky neanalyzovaných zápasů, příznak „pod tlakem“ u přihrávek.

## Jak data stahujeme teď

Dočasné řešení, než bude oficiální API.

- **Princip:** portál je webová aplikace nad vlastním (neveřejným) API na `portal-api.eyeball.club`. Skript otevře portál v prohlížeči bez okna, použije uložené přihlášení a stáhne stejná data, která web zobrazuje. Neobchází žádná oprávnění – vidí jen to, co účet.
- **Přihlášení:** přes Microsoft. Při prvním spuštění (a když přihlášení vyprší) se otevře okno, kde se přihlásím ručně; přihlášení se uloží do `browser_profile`. Heslo skript nikde neukládá.
- **Kde:** `~/Desktop/Sigma/eyeball_stats/`, spouštěč **`~/Desktop/Sigma/Spustit Eyeball stahování.command`** (dvojklik). Python + Playwright, vlastní prostředí `.venv`.
- **Průběh:** spouštěč se zeptá na **období** (vše / aktuální sezóna / posledních 7 dní / posledních 30 dní / vlastní od–do) a na **části**:
  1. souhrn hráčů za období (na 90 min)
  2. statistiky hráčů po zápasech
  3. týmové statistiky zápasů
  4. sestavy
  5. události (velký objem)
  6. fyzické metriky hráčů po sezónách
- **Výstupy:** každé stažení do vlastní složky `vystupy/<datum čas> období <od_do>/`: `1_souhrn_hracu.xlsx`, `2_zapasy.xlsx` (listy Zápasy, Hráči v zápasech, Týmové statistiky, Sestavy), `5_udalosti.csv` (oddělovač středník, otevře Excel), `6_fyzicke_metriky.xlsx`. Po skončení se složka otevře.
- **Mezipaměť:** surová data zápasů v `archiv/zapasy/<ID zápasu>/` (události komprimované). Znovu se stahují jen nové zápasy, zápasy z posledních 21 dní a neanalyzované. Opakované stažení je proto rychlé.
- **Bez dotazů z terminálu:** `.venv/bin/python eyeball_stats.py --od 2026-08-01 --do 2026-10-19 --casti 1,2,5`, `--vse`, `--login`.
- Mezi dotazy je pauza 0,3 s. Spouštěč před stažením zkontroluje a případně doinstaluje prohlížeč pro Playwright a brání uspání Macu.
- Log: `eyeball_stats.log`. Doprovodné soubory: `Slovník metrik.xlsx` (EN název – česky – vysvětlení; úplnější verze je [[Eyeball – slovník metrik|slovník metrik]]), ukázka jednoho zápasu s mapou akcí hráče ve `ukazka_zapas_U19/`.

### Hlavní endpointy (pro srovnání s oficiálním API)
| Data | Endpoint |
|---|---|
| vyhledávání hráčů | `POST /portal/player/search` (`timeRange {start, end}` nebo `season`, `pagination`) |
| seznam zápasů klubu | `GET /portal/club/games?clubId=…&page=…&limit=…` |
| statistiky hráčů zápasu | `GET /game/{id}/player-stat` |
| týmové statistiky | `GET /game/{id}/team-stat` |
| detail zápasu a sestavy | `GET /game/{id}/page` |
| události | `GET /game/{id}/page/lazy` |
| fyzická analýza zápasu | `GET /portal/game-analysis-physical/{id}` |
| profil hráče | `GET /player-profile/{id}/…` (header, performance, performance-radar, seasonal-stats, standout-metrics, average-rating, key-events, event-types, games, club-history, behavioral-signals-snapshot, behavioral-archetypes, physical-metrics, body-measurements, recruitment-information…) |

## Rozhodnutí

- **Ruční spouštění, ne automatické** – stahovat jen když chci; týdenní automat byl nastavený a zrušený.
- **Volitelné období a části** – ne pokaždé vše; události jsou objemné.
- **Čtení dat přes stránku portálu** (stejné přihlášení jako web) místo exportních tlačítek – exporty by mohly čerpat kredity (podle kódu ne, neověřeno).
- **Mezipaměť surových dat** – zápasy se nestahují opakovaně; výstupy se dají kdykoli znovu sestavit.
- **Výstupy do samostatných složek** podle času stažení – nic se nepřepisuje ani nemíchá.

## Co nefungovalo

- Vyšší limit než 50 na stránku a filtr data u seznamu zápasů → chyba serveru; filtrujeme až po stažení.
- Datový soubor fyzických metrik zápasu (S3) → přístup odepřen.
- První verze skriptu brala přihlašovací stránku jako přihlášení (adresa obsahovala „player-stats-search“) → teď se čeká, až API skutečně odpoví.
- Pole `pages` zaokrouhlené dolů → chyběli hráči z poslední stránky.
- Prohlížeč Playwright zmizel z mezipaměti Macu (pravděpodobně ho uklidil jiný projekt) → spouštěč ho teď kontroluje.
- Zápas bez souřadnic událostí shodil zápis CSV → chybějící souřadnice teď zůstávají prázdné.

## Pravidla a rizika

- **Obchodní podmínky Eyeballu** (eyeball.club/terms-and-conditions): bod 3.3 zakazuje data mining, roboty a jiné automatizované prostředky přístupu a nadměrné zatěžování; bod 3.1 použití obsahu bez písemného souhlasu; bod 5.1 dovoluje omezit nebo zrušit přístup bez upozornění. Podmínky mluví o „webu“, zda platí i pro portál, je nejasné. Rozhoduje smlouva klubu s Eyeballem.
- Eyeball provoz vidí: každý dotaz jde pod mým účtem, portál má měřicí nástroje (Amplitude, PostHog, LogRocket, Sentry, Intercom) a skript se hlásí jako „HeadlessChrome“.
- Řešení: oficiální API / písemný souhlas – viz schůzka.
- Rozhraní portálu se může bez ohlášení změnit (zvlášť s přechodem na novou verzi platformy do konce 2026) – skript bude třeba upravit.

## Otevřené body a další kroky

- [ ] Oficiální API – scénáře a ceník od Eyeballu (viz [[SK Sigma Olomouc/Meetings/2026-10-19 – Eyeball – Martin Neoral|schůzka]]); po zprovoznění nahradit stahovací část skriptu, analýzy nechat.
- [ ] Ověřit u správce kreditů, že exporty z portálu kredity nečerpají.
- [ ] Doplnit do `Slovník metrik.xlsx` týmové statistiky, fyzické metriky a atributy událostí.
- [ ] Stáhnout události a týmové statistiky i za starší sezóny (volba „Vše“), pokud budou potřeba.
- [ ] Vyzkoušet sekce profilu hráče (radar, behaviorální signály, standout metriky) jako zdroj pro kartu hráče.
- [ ] Analýzy nad daty: profil hráče, výkon po 15 min, mapy akcí, xG pro a proti, ztráty a zisky po třetinách, standardky.

## Souvislosti

- [[Eyeball – slovník metrik]] – všechny metriky a datová pole s definicemi a nástrahami.
- [[SK Sigma Olomouc/Meetings/2026-10-19 – Eyeball – Martin Neoral|2026-10-19 – Eyeball – Martin Neoral]]
- [[LLM Wiki/wiki/entity/Eyeball|Eyeball]] (wiki)
- [[SK Sigma Olomouc/Analytická témata/Karta hráče 🎯|Karta hráče 🎯]]
- [[SK Sigma Olomouc/Analytická témata/⭐ Hodnocení hráčů|⭐ Hodnocení hráčů]]
- [[SK Sigma Olomouc/Analytická témata/🏟️ Hodnocení utkání|🏟️ Hodnocení utkání]]
- [[SK Sigma Olomouc/Analytická témata/🔍 Skauting|🔍 Skauting]]
- [[SK Sigma Olomouc/Analytická témata/Herní analýza dat|Herní analýza dat]]
