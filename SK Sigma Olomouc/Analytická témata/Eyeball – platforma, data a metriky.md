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

> Souhrn všeho, co víme o datech v Eyeballu (portal.eyeball.club): jaké datové oblasti platforma nabízí, jaké konkrétní metriky a atributy, jak se data dají získat a jak je teď dočasně stahujeme skriptem, než bude k dispozici oficiální API. Zjištěno průzkumem portálu (říjen 2026) – webu, jeho vnitřního rozhraní a dat k vybraným zápasům a hráčům. Obecně platné pro klub, bez konkrétních počtů Sigmy.

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

## 3. Statistiky hráče v zápase – kompletní metriky

Absolutní hodnoty za zápas, pro hráče obou týmů. Minuty jsou v datech v milisekundách. Brankáři mají navíc brankářský blok.

### Základ
| Metrika (EN) | Česky | Význam |
|---|---|---|
| playerName, position, backNumber | hráč, pozice, číslo | pozice v daném zápase |
| minutesPlayed | minuty | v ms (5 406 000 = 90,1 min) |
| rating | hodnocení | známka výkonu cca 0–10 |

### Útok a zakončení
| Metrika (EN) | Česky | Význam |
|---|---|---|
| goalsScrored | góly | (v API s překlepem) |
| goalsOwn | vlastní góly | |
| assists | asistence | poslední přihrávka před gólem |
| shots | střely | všechny pokusy |
| shotsOnTarget / shotsOffTarget / blockedShots | na branku / mimo / zblokované | |
| shotsInsidePa / shotsOutsidePa | z vápna / zpoza vápna | PA = pokutové území |
| nonPenaltyShots | střely bez penalt | |
| totalXg | xG | součet pravděpodobnosti gólu u střel |
| nonPenaltyXg | npxG | xG bez penalt |
| nonPenaltyXgPerShot | npxG na střelu | průměrná kvalita zakončení |
| goalsXgRatio | góly / xG | >1 = proměňuje nad očekávání |
| totalXa | xA | xG střel vzniklých z přihrávek hráče |
| takeOnsSuccessful / takeOnsTotal | úspěšné / všechny kličky | obcházení soupeře 1v1 |
| offsides | ofsajdy | |

### Přihrávky a rozehrávka
| Metrika (EN) | Česky | Význam |
|---|---|---|
| passesSuccess / passesTotal | úspěšné / všechny přihrávky | |
| passAccuracy | přesnost | v % (v souhrnu hráčů jako 0–1) |
| keyPasses | klíčové přihrávky | po nich spoluhráč vystřelil |
| passesInFinalThird* / InMiddleThird* / InDefensiveThird* | přihrávky v útočné / střední / obranné třetině | vždy Success a Total |
| shortPasses* / mediumRangePasses* / longPasses* | krátké / střední / dlouhé | hranice délky Eyeball neuvádí |
| passesForward* / passesSideways* / passesBackward* | dopředu / do strany / dozadu | |
| crossesSuccess / crossesTotal | centry | |
| controlUnderPressure | kontrola míče pod tlakem | zatím prázdné |
| launchPercent | podíl dlouhých nákopů | hlavně u brankářů |

### Standardní situace
| Metrika (EN) | Česky |
|---|---|
| freekicks | rozehrané volné kopy |
| corners | rohy |
| throwIns | auty |

### Obrana
| Metrika (EN) | Česky | Význam |
|---|---|---|
| tacklesSuccess / tacklesTotal | souboje o míč (tackle) | odebrání míče |
| aerialDuelsSuccess / aerialDuelsTotal | hlavičkové souboje | |
| groundDuelsSuccess / groundDuelsTotal | pozemní souboje | zatím prázdné |
| interceptions | zachycené přihrávky | |
| clearances | odkopy / odvrácení | |
| blocks | bloky | střely a přihrávky soupeře |
| recoveries | získané míče | volné a odražené míče |
| interventions | zásahy | zatím prázdné |
| mistakes | chyby | vedoucí k nebezpečí soupeře (odhad definice) |

### Disciplína
| Metrika (EN) | Česky |
|---|---|
| fouls / foulsWon | fauly / vybojované fauly |
| yellowCards / redCards | žluté / červené karty |

### Brankář
| Metrika (EN) | Česky | Význam |
|---|---|---|
| goalsConceded | obdržené góly | |
| savePercent | úspěšnost zákroků | % chycených střel na branku |
| catches / punches | chycené / vyboxované míče | |
| aerialClearancesSuccess / Total | zákroky ve vzduchu | vysoké míče |
| crossesFacedTotal / crossesStoppedTotal / crossesStoppedRatio | centry na brankáře / zastavené / podíl | aktivita na centry |
| defensiveActionsOpaTotal | zákroky mimo vápno | OPA = outside penalty area, „sweeper keeper“ |
| averageDefensiveActionDistance | průměrná vzdálenost zákroků | od brankové čáry, vyšší = hraje výš |
| goalsKicksSuccess / Total | odkopy od branky | |
| throwsSuccess / throwsTotal / throwsRatio | výhozy rukou | |
| averagePassLength | průměrná délka rozehrávky | |
| launchPercent | podíl dlouhých nákopů | |

## 4. Týmové statistiky zápasu

62 metrik, vždy domácí vs. hosté, typ hodnoty počet / procento / desetinné / rating.

- **Souhrn:** góly, střely, **držení míče (%)**, střely na branku, fauly, ofsajdy, volné kopy, rohy, průměrné hodnocení týmu.
- **Útok:** střely (na branku, mimo, zblokované, z vápna, zpoza vápna, bez penalt), kličky, xG, npxG, npxG na střelu, góly/xG, xA.
- **Obrana:** souboje (tackle), hlavičkové a pozemní souboje, zachycení, odkopy, zásahy, získané míče, bloky, chyby, vybojované fauly.
- **Rozehrávka:** přihrávky a přesnost, klíčové přihrávky, přihrávky po třetinách, podle délky a směru, centry, kontrola pod tlakem.
- Pozor: `blocks` je v souhrnu i v obraně s **různým** významem (bloky střel týmu vs. obranné bloky).

## 5. Události v zápase (event data) – největší detail

Ke každému analyzovanému zápasu kompletní seznam akcí obou týmů (řádově tisíce na zápas).

### Údaje u každé události
- **čas:** fotbalový čas v ms (`footballTime`), poločas, čas v poločase, nastavení; čas ve videu (`videoTime`) – akce se dá dohledat v záznamu
- **hráč** (jméno, číslo, ID v zápase), **tým**
- **kategorie a typ** události, **úspěch** ano/ne
- **pod tlakem** (`underPressure`) – vyplněné jen u střel, hlavičkových soubojů a odkopů, u přihrávek vždy „ne“
- **místo na hřišti:** `x`, `y` v rozsahu 0–1, otočené tak, že **každý tým útočí zleva doprava** (x = 1 je soupeřova branka); na hřišti 105 × 68 m se násobí. U některých zápasů souřadnice chybí.
- skupiny (`all`, `main` – hlavní momenty, `my`), komentáře, oblíbené, příznak do kolekce

### Typy událostí (24)
| Kategorie | Typy |
|---|---|
| Držení míče | přihrávka (`pass`), převzetí přihrávky (`pass_received`), získaný míč (`recovery`), hlavičkový souboj (`aerial_duel`) |
| Obrana | souboj (`tackle`), odkop (`clearance`), zachycení (`interception`), blok (`block`), míč mimo hru (`ball_out_of_play`), obcházen kličkou (`take_on_against`) |
| Útok | střela (`shot`), klička (`take_on`), technická chyba (`technical_error`) |
| Brankář | zákrok (`save`), inkasovaný gól (`goal_conceded`), zachycení (`catch_interception`), vyboxování (`punch`) |
| Administrativní | gól, faul, karta, střídání, ofsajd, začátek a konec poločasu |

### Detailní atributy podle typu
| Atribut | Hodnoty |
|---|---|
| délka přihrávky | krátká / střední / dlouhá |
| směr přihrávky | dopředu / do strany / dozadu |
| třetina hřiště | obranná / střední / útočná (u přihrávek, hlaviček, kliček) |
| část těla | pravá noha / levá noha / hlava / ruka / jiné |
| standardní situace | ze hry / aut / volný kop / roh / kop od branky |
| centr, klíčová přihrávka, asistence, přihrávka ve vápně | ano |
| **xA** | u přihrávky – hodnota vytvořené šance |
| rozehrávka brankáře | výkop z ruky |
| **xG** | u střely |
| výsledek střely | na branku / mimo / zblokovaná |
| místo v bráně | nahoře / uprostřed / dole × vlevo / uprostřed / vpravo |
| střela z vápna | ano / ne |
| typ souboje | ve stoje / skluzem |
| typ bloku | po přihrávce / po střele |
| typ faulu | fauloval / vybojovaný |
| druhý míč | u převzetí, získání a zachycení |
| typ gólu | ze hry |
| zákrok brankáře | chytil / vyrazil, s pádem ano/ne, po střele z vápna |
| inkasovaný gól | po střele, z vápna ano/ne |
| karta | žlutá / červená |
| střídání | odchod / příchod |

**Co z toho jde spočítat:** výkon po časových úsecích (např. 15 min), mapy akcí a střel, heatmapy ztrát a zisků po třetinách, kdy dáváme a dostáváme góly, výkon před a po střídání, standardní situace a jejich výsledek, řetězení přihrávka → převzetí.

## 6. Profil hráče

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
- **Behaviorální signály** – jak hráč snáší tlak zápasu:
  - **Tolerance** – kolik tlaku vydrží, než mu začne klesat výkon
  - **Sensitivity (citlivost)** – jak výrazně výkon klesne, když tlak začne působit
  - **Recovery (zotavení)** – jak rychle se vrátí na svou úroveň
  - každý signál má skóre, pásmo s popisem (např. „stays composed late“), porovnání s kohortou v %, trend; k tomu slovní shrnutí a míra jistoty
  - kohorty: věková kategorie, věková kategorie + pozice, pozice; období: posledních 10 zápasů, sezóna (až 3 sezóny); minimum 360 analyzovaných minut
- **Behaviorální archetypy:** dominantní a vedlejší archetyp hráče (u běžných hráčů zatím „nedokončeno“).
- **Biometrie a tělesné míry:** sken těla – obvody horní a dolní poloviny těla, celotělové míry, změny tělesného složení, trendy (jen pokud má hráč skeny a jsou sdílené).
- **Fyzické metriky** (viz další sekce).
- **Náborové informace:** zda je hráč otevřen nabídkám.
- **Stínový tým (shadow team)** a oblíbení hráči – skautingové nástroje.

## 7. Fyzická data

- **Na profilu hráče za sezónu** (nebo všechny sezóny):
  - **maximální rychlost** (km/h) a zápas, kde ji dosáhl; zda padla v této sezóně
  - **průměrná top rychlost** (průměr maxim ze zápasů) se změnou proti minulé sezóně
  - **uběhnutá vzdálenost** na 90 min (km)
  - **akcelerace a decelerace** na 90 min (práh podle popisu v portálu 10,8 km/h)
  - **rozložení pohybu** – podíl času a minuty na 90 v zónách: stání, chůze, klus, běh, rychlý běh, sprint
  - pozice, počet zápasů a minut, ze kterých se počítá
  - dokumenty – PDF reporty k zápasům
- **K zápasu:** jen **PDF report** (desítky MB) a video fyzické analýzy; datový soubor za ním je zamčený.
- Fyzickou analýzu nemá každý zápas – zatím jen část zápasů (dle schůzky půjde o placenou nadstavbu nové verze).

## 8. Hodnocení a „měkká“ data

- **Rating** hráče za zápas (cca 0–10, průměrný výkon kolem 6–7) a průměrné hodnocení týmu.
- **Hodnocení trenéra** a **hodnocení skautů** u hráče v zápase.
- **Odznaky (rating badges)** – 20 typů, které jde hráči udělit za zápas: Mr./Ms. Hustle, Vibes Master, Level Up, Locked In, Team First, Big Game Energy, Always Ready, Silent Hero, Unbreakable Focus, Visionary Passer, Game Changer, Golden Heart, Clutch Player, Ball Magnet, Sharp Shooter, Captain Energy, Maestro Move, Brick Wall, No Quit, Iron Will.
- **AI:** AI shrnutí zápasu, AI review trenéra, AI vyhledávání hráčů pro skauty („scout search“ s předpřipravenými dotazy) – vyžadují oprávnění.
- **Hráči týdne** podle typu (góly, asistence, střely, kličky, přihrávky dopředu, hlavičky) a zvýraznění hráči.

## 9. Video a klipy

- Video zápasu jako stream, náhled, odkaz ke stažení (při oprávnění).
- Klipy z událostí, klipy přes více zápasů hráče, sdílené klipy (i chráněné heslem), komentáře k událostem, kolekce a oblíbené.

## 10. Exporty přímo v portálu

- Statistiky hráčů / týmu zápasu: **CSV, JSON, XLSX, XML**.
- Události zápasu: export.
- Soupiska: CSV, PDF, XLSX.
- Exporty jsme zatím nepoužili (nevěděli jsme, zda nečerpají kredity – podle kódu ne, ověřit u správce kreditů).

## Pozice

Eyeball používá francouzské zkratky (v portálu s anglickými popisky):

| Kód | Anglicky | Česky |
|---|---|---|
| G | GK | brankář |
| DD / DC / DG | RB / CB / LB | pravý / střední / levý obránce |
| MDC | DM | defenzivní záložník |
| MC | CM | střední záložník |
| MOC | CAM | ofenzivní záložník |
| MD / MG | RM / LM | pravý / levý záložník |
| AD / AG | RW / LW | pravé / levé křídlo |
| ATT | CF | útočník |

## Záludnosti v datech

- **Jednotky:** souhrn hráčů = na 90 min, statistiky zápasu = absolutně. Přesnost přihrávek 0–1 v souhrnu, % v zápase. Minuty v ms.
- Prázdné metriky: `controlUnderPressure`, `groundDuels`, `interventions`.
- `underPressure` jen u části typů událostí.
- U některých zápasů chybí souřadnice událostí.
- U přihrávky je jen místo odkud – **ne cíl**.
- Stránkování: limit max. 50 na dotaz (víc vrací chybu), pole `pages` zaokrouhluje dolů – řídit se podle `total`.
- Neanalyzovaný zápas: statistiky a události „zakázáno“, sestava dostupná.
- Hodnoty se po zápase mohou ještě měnit (opravy analýzy) – nedávné zápasy stahovat znovu.
- Počty z událostí sedí s oficiální statistikou hráče (ověřeno na jednom zápase), drobné rozdíly možné (souboje 8 vs. 7).

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
- Log: `eyeball_stats.log`. Doprovodné soubory: `Slovník metrik.xlsx` (EN název – česky – vysvětlení, zatím bez týmových, fyzických a událostí), ukázka jednoho zápasu s mapou akcí hráče ve `ukazka_zapas_U19/`.

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

- [[SK Sigma Olomouc/Meetings/2026-10-19 – Eyeball – Martin Neoral|2026-10-19 – Eyeball – Martin Neoral]]
- [[LLM Wiki/wiki/entity/Eyeball|Eyeball]] (wiki)
- [[SK Sigma Olomouc/Analytická témata/Karta hráče 🎯|Karta hráče 🎯]]
- [[SK Sigma Olomouc/Analytická témata/⭐ Hodnocení hráčů|⭐ Hodnocení hráčů]]
- [[SK Sigma Olomouc/Analytická témata/🏟️ Hodnocení utkání|🏟️ Hodnocení utkání]]
- [[SK Sigma Olomouc/Analytická témata/🔍 Skauting|🔍 Skauting]]
- [[SK Sigma Olomouc/Analytická témata/Herní analýza dat|Herní analýza dat]]
