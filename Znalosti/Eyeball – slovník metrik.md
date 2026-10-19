---
datum: 2026-10-19
aktualizovano: 2026-10-19
typ: referenční slovník
zdroj: průzkum portálu portal.eyeball.club (zpracováno s Claude)
projekt: SK Sigma Olomouc – analytika
tags: [eyeball, herni-data, metriky, slovnik, event-data, fyzicka-data, mladez]
aliases: [Eyeball glosář, Eyeball metriky]
---
# Eyeball – slovník metrik

> Český výklad metrik a datových polí platformy [[Eyeball]] — **138 hesel** ve 14 kategoriích: statistiky hráčů a týmů, xG/xA, brankářské metriky, typy a atributy událostí (event data), odvozené metriky profilu hráče (radar, percentily, behaviorální signály) a fyzické metriky. Stav k 19. 10. 2026.

## Kontext a cíl

[[Eyeball]] je platforma pro video a data z mládežnických a amatérských zápasů; zápasy analyzuje externí poskytovatel (event data). Na rozdíl od Wyscoutu a SkillCorneru **nemá veřejný glosář** – definice jsou poskládané z dat, která portál vrací (názvy polí v API), z popisků v aplikaci a z ověření na konkrétních zápasech. Co Eyeball explicitně neuvádí, je označené jako *odhad* nebo *neověřeno*.

Protějšek k [[Wyscout – slovník metrik]] a [[SkillCorner – slovník metrik]]. Přehled platformy, datových oblastí a toho, jak data stahujeme, je v [[Eyeball – platforma, data a metriky]].

Anglický název je klíč, pod kterým metrika přichází v datech portálu (a pravděpodobně i v budoucím API). České názvy jsou pracovní překlady; sloupcové názvy ve staženém Excelu jsou stejné jako anglický klíč. Sekce **Pozor na** je u většiny hesel to nejcennější. Neoficiální dokument.

**Kde se metrika vyskytuje:** souhrn hráčů (na 90 min), statistiky hráče v zápase (absolutně), týmové statistiky zápasu, události zápasu, profil hráče.

## Nejdůležitější nástrahy

1. **Na 90 minut vs. absolutně.** Souhrn hráčů a profil = na 90 min, statistiky zápasu = absolutní počty. Nemíchat bez přepočtu.
2. **Přesnost přihrávek ve dvou formátech:** 0–1 v souhrnu, % v zápase.
3. **Minuty v milisekundách** ve statistikách zápasu a sestavách.
4. **Překlep v API:** góly v zápase jsou `goalsScrored`, v souhrnu `goalsScored`.
5. **`underPressure` u přihrávek je vždy „ne“** – příznak je vyplněný jen u střel, hlaviček a odkopů.
6. **Prázdné metriky:** `controlUnderPressure`, `groundDuels`, `interventions` zatím nemají hodnoty.
7. **Souřadnice jsou 0–1 a otočené** – každý tým útočí zleva doprava. U některých zápasů chybí úplně. U přihrávky není cílové místo.
8. **`blocks` v týmových statistikách dvakrát** (Souhrn a Obrana) s různou hodnotou.
9. **Neanalyzovaný zápas** nemá statistiky ani události, ale sestavu ano. Analýza se po uvolnění ještě může opravit.
10. **Hranice délky přihrávek, směrů a rychlostních zón Eyeball neuvádí** – metriky stejného jména nejsou přímo srovnatelné s [[Wyscout – slovník metrik|Wyscoutem]] ani [[SkillCorner – slovník metrik|SkillCornerem]].
11. **Percentily a „top X %“** se počítají proti celé databázi Eyeballu (různé země a úrovně), ne proti české soutěži.

## Obsah

1. **Základ a metodika** — 11 hesel
2. **Hodnocení** — 5 hesel
3. **Útok a zakončení** — 14 hesel
4. **Očekávané hodnoty (xG, xA)** — 5 hesel
5. **Přihrávky a rozehrávka** — 9 hesel
6. **Standardní situace** — 3 hesel
7. **Obrana a souboje** — 9 hesel
8. **Disciplína** — 3 hesel
9. **Brankář** — 13 hesel
10. **Týmové metriky** — 3 hesel
11. **Události – typy** — 23 hesel
12. **Události – atributy** — 22 hesel
13. **Profil hráče – odvozené metriky** — 12 hesel
14. **Fyzické metriky** — 6 hesel

## Prahy a hranice

Číselné hranice a formáty, na kterých data stojí.

| Pojem | Hodnota | Poznámka |
|---|---|---|
| Souřadnice x, y | 0–1, útok zleva doprava | x = 1 soupeřova branka; my převádíme na 105 × 68 m |
| Sezóna | koncový rok | 2027 = 2026/2027 |
| Rating | cca 0–10 | průměrný výkon kolem 6–7 (pozorování, ne oficiální) |
| Akcelerace / decelerace | ≥ 10,8 / ≤ −10,8 | jednotka v popisu Eyeballu km/h – ověřit |
| Behaviorální signály – min. vzorek | 360 analyzovaných minut | max. 3 sezóny ve snapshotu |
| Behaviorální signály – období | posledních 10 zápasů / sezóna | kohorta pozice jen přes všechny sezóny |
| Délka přihrávky | krátká / střední / dlouhá | hranice neuvedené |
| Rychlostní zóny | stání → sprint (6 zón) | hranice neuvedené |
| Minuty | ms ve statistikách zápasu | 5 406 000 ms = 90,1 min |
| Stránkování API | max. 50 záznamů na dotaz | pole `pages` zaokrouhluje dolů, řídit se `total` |

## Pozice

Eyeball používá francouzské zkratky, v aplikaci s anglickými popisky.

| Kód v datech | Anglicky | Česky |
|---|---|---|
| `G` | GK | brankář |
| `DD` | RB | pravý obránce |
| `DC` | CB | střední obránce |
| `DG` | LB | levý obránce |
| `MDC` | DM | defenzivní záložník |
| `MC` | CM | střední záložník |
| `MOC` | CAM | ofenzivní záložník |
| `MD` | RM | pravý záložník |
| `MG` | LM | levý záložník |
| `AD` | RW | pravé křídlo |
| `AG` | LW | levé křídlo |
| `ATT` | CF | útočník |

## 1. Základ a metodika

*Pojmy, bez kterých se ostatní metriky nedají správně přečíst: kdy jsou data k dispozici, v jakých jednotkách, jak se počítá čas a místo na hřišti.*

### `Analysis finished / approved` — Dokončená a schválená analýza

*isAnalysisFinished, isAnalysisApproved*

Stav zpracování zápasu. Zápas se natočí, externí poskytovatel ho otaguje a Eyeball analýzu uvolní. Teprve pak existují statistiky, události a hodnocení.

- **Metodika:** U zápasu je uveden poskytovatel analýzy (`providerTag`, např. SPORTLOGIQ), úroveň zpracování (`processingLevel`, např. `full`) a zda jsou otagované oba týmy (`teamTagged`).
- **Pozor na:** Neanalyzovaný zápas vrací na statistiky a události „zakázáno“, ale **sestava je dostupná** (bez hodnocení). Data se po uvolnění ještě mohou opravovat – nedávné zápasy je dobré stáhnout znovu.

### `Per 90 vs. absolute` — Na 90 minut vs. absolutně

Eyeball vrací stejné metriky ve dvou podobách: v **souhrn hráčů (na 90 min)** a v profilu hráče přepočtené na 90 minut, ve **statistiky hráče v zápase (absolutně)** jako absolutní počet za zápas.

- **Metodika:** Ověřeno: 2 góly za 1 425 minut = 0,126 na 90 min. Absolutní jsou v souhrnu jen `totalGoals` a `totalAssists`.
- **Pozor na:** Souhrnná čísla a čísla ze zápasu nikdy nemíchej v jedné tabulce bez přepočtu. Malý vzorek minut přepočet na 90 nafukuje.

### `minutesPlayed` — Odehrané minuty

Čas hráče na hřišti.

- **Metodika:** V statistiky hráče v zápase (absolutně) a v sestavách v **milisekundách** (5 406 000 ms = 90,1 min). V souhrnu v minutách, navíc rozdělené na `maleMinutesPlayed` a `femaleMinutesPlayed` (mužské a ženské soutěže).
- **Pozor na:** Délka zápasu je podle kategorie různá (poločasy mají vlastní `formalLength`) a minuty zahrnují nastavení – plný zápas tak bývá o něco víc než 90.

### `gamesCount` — Odehrané zápasy

Počet zápasů hráče ve zvoleném období.

- **Metodika:** V souhrn hráčů (na 90 min). Vrací se jako text, ne jako číslo.
- **Pozor na:** Počítají se zápasy, kde hráč nastoupil – i krátké střídání.

### `Season` — Sezóna

*season*

Sezóna se v datech značí **koncovým rokem**: `2027` = 2026/2027.

- **Metodika:** Filtr sezóny je v souhrnu hráčů, v profilu hráče i u fyzických metrik. „All Seasons“ = bez omezení.
- **Pozor na:** Kluby v různých zemích mají jiný rozsah sezóny (v kódu portálu jsou varianty srpen–červen, červenec–květen, září–červen…).

### `timeRange` — Období od–do

Volitelné období (`start`, `end`) pro souhrn hráčů – odpovídá filtru „Vyberte období“ na webu.

- **Metodika:** Souhrn pak obsahuje jen hráče, kteří v období hráli, a metriky jen z těchto zápasů.
- **Pozor na:** Seznam zápasů klubu filtr data nepřijme (chyba serveru) – zápasy se filtrují až po stažení.

### `Pitch coordinates` — Souřadnice hřiště

*x, y*

Místo události na hřišti jako `x` a `y` v rozsahu **0–1**.

- **Metodika:** Data jsou otočená tak, že **každý tým útočí zleva doprava** – x = 1 je vždy soupeřova branka, bez ohledu na poločas. Pro metry násob rozměry hřiště (my počítáme 105 × 68 m).
- **Pozor na:** U některých zápasů souřadnice **chybí úplně**. Která strana osy y je levá, Eyeball neuvádí. Skutečné rozměry hřiště mládeže se liší.

### `footballTime / halfTime / videoTime` — Čas události

Čas akce v milisekundách: fotbalový čas od začátku zápasu, čas v rámci poločasu a čas ve videozáznamu.

- **Metodika:** 2. poločas začíná na 45:00 (`halfOffset`), nastavení je čas nad oficiální délku poločasu. `videoTime` umožňuje přeskočit ve videu přímo na akci.
- **Pozor na:** Přesnost je na desetiny sekundy, ale navazující události (střela → gól) mají rozdíl jen pár set ms – řaď podle času a ID.

### `Halves` — Poločasy

*formalLength, padding*

Popis poločasů zápasu: oficiální délka, začátek a konec v čase zápasu i ve videu, posun ve videu.

- **Metodika:** Na stránce zápasu je i strana, na které začínal domácí tým (`leftSideStart`).
- **Pozor na:** Oficiální délka poločasu se liší podle kategorie.

### `Game type` — Typ zápasu

*type*

`championnat` = mistrovský, `amical` = přátelský, `coupe` = pohárový.

- **Metodika:** U zápasu je dále kategorie (U13–U19…), domácí a hosté (tým i klub) a skóre.
- **Pozor na:** Přátelské zápasy mají často jiný průběh střídání – při srovnání ratingu je dobré je oddělit.

### `Comparison base` — Srovnávací základna

„Statistiky jsou porovnávány se všemi hráči v naší databázi.“ Percentily a „top X %“ v profilu hráče se počítají proti databázi Eyeballu.

- **Metodika:** Behaviorální signály mají vlastní kohorty (věková kategorie, kategorie + pozice, pozice).
- **Pozor na:** Databáze zahrnuje různé země a úrovně soutěží – percentil není srovnání jen s českou ligou.

## 2. Hodnocení

*Souhrnná hodnocení výkonu – od Eyeballu, trenéra i skautů – a odznaky za zápas.*

### `rating` — Hodnocení výkonu

Celková známka výkonu hráče v zápase od Eyeballu.

- **Metodika:** Škála zhruba 0–10, průměrný výkon kolem 6–7. Ve statistiky hráče v zápase (absolutně) a v sestavách za zápas, v souhrn hráčů (na 90 min) jako průměr. Týmová verze: `averageRating`.
- **Pozor na:** Výpočet Eyeball nezveřejňuje. Hodnocení je relativní k výkonu v zápase, ne k úrovni soutěže – mezi kategoriemi a soutěžemi není přímo srovnatelné.

### `averageRating (profil)` — Průměrné hodnocení v profilu

*percentTop, ratingChange*

Průměrný rating hráče, jeho změna a percentil proti databázi.

- **Metodika:** Filtr: celkově, poslední zápas, posledních 5 nebo 10 zápasů.
- **Pozor na:** Percentil závisí na tom, proti komu se srovnává (viz Srovnávací základna).

### `coachRating` — Hodnocení trenéra

Hodnocení hráče za zápas zadané trenérem.

- **Metodika:** U hráče v sestavě zápasu.
- **Pozor na:** Subjektivní – vypovídá hlavně v rámci jednoho trenéra.

### `playerGrading / gradedByScouts` — Hodnocení skautů

Hodnocení hráče skauty Eyeballu.

- **Metodika:** U hráče v sestavě; oprávnění `playerGrading`.
- **Pozor na:** Běžný trenérský účet ho nevidí.

### `Rating badges` — Odznaky za zápas

20 odznaků, které lze hráči udělit za zápas: Mr./Ms. Hustle (pracovitost), Vibes Master (vliv na tým), Level Up (zlepšení), Locked In (soustředění), Team First (týmová rozhodnutí), Big Game Energy, Always Ready, Silent Hero, Unbreakable Focus, Visionary Passer (přihrávky), Game Changer, Golden Heart, Clutch Player (rozhodující momenty), Ball Magnet (čtení hry), Sharp Shooter (zakončení), Captain Energy (vůdcovství), Maestro Move (technika), Brick Wall (obrana), No Quit, Iron Will.

- **Metodika:** Udělují se v portálu (oprávnění `ratingBadgeEdit`).
- **Pozor na:** Kvalitativní, motivační prvek – ne metrika pro srovnání.

## 3. Útok a zakončení

*Góly, asistence, střely a kličky.*

### `goalsScored / goalsScrored` — Vstřelené góly

Počet vstřelených gólů.

- **Metodika:** V souhrn hráčů (na 90 min) jako `goalsScored` na 90 min, ve statistiky hráče v zápase (absolutně) jako `goalsScrored`.
- **Pozor na:** V datech zápasu má API v názvu překlep („Scrored“) – hledej obě varianty.

### `totalGoals` — Góly celkem

Absolutní počet gólů za období.

- **Metodika:** Jen v souhrn hráčů (na 90 min).

### `goalsOwn` — Vlastní góly

Góly do vlastní branky.

- **Metodika:** souhrn hráčů (na 90 min), statistiky hráče v zápase (absolutně).

### `assists` — Asistence

Poslední přihrávka před gólem.

- **Metodika:** souhrn hráčů (na 90 min) (na 90), statistiky hráče v zápase (absolutně); v událostech příznak `assist` u přihrávky.

### `totalAssists` — Asistence celkem

Absolutní počet asistencí za období.

- **Metodika:** Jen v souhrn hráčů (na 90 min).

### `shots` — Střely

Všechny pokusy o střelu – na branku, mimo i zblokované.

- **Metodika:** souhrn hráčů (na 90 min), statistiky hráče v zápase (absolutně), týmové statistiky zápasu.
- **Pozor na:** V týmových statistikách je `shots` ve skupině Souhrn i Útok.

### `shotsOnTarget` — Střely na branku

Střely mířící do rámu branky (gól nebo zákrok brankáře).

- **Metodika:** souhrn hráčů (na 90 min), statistiky hráče v zápase (absolutně), týmové statistiky zápasu.

### `shotsOffTarget` — Střely mimo branku

Střely mimo rám branky.

- **Metodika:** statistiky hráče v zápase (absolutně), týmové statistiky zápasu.

### `blockedShots` — Zblokované střely

Střely hráče, které zblokoval bránící hráč.

- **Metodika:** statistiky hráče v zápase (absolutně).

### `shotsInsidePa` — Střely z vápna

*PA = penalty area*

Střely z pokutového území.

- **Metodika:** souhrn hráčů (na 90 min), statistiky hráče v zápase (absolutně), týmové statistiky zápasu.

### `shotsOutsidePa` — Střely zpoza vápna

Střely z prostoru mimo pokutové území.

- **Metodika:** souhrn hráčů (na 90 min), statistiky hráče v zápase (absolutně), týmové statistiky zápasu.

### `nonPenaltyShots` — Střely bez penalt

Počet střel bez pokutových kopů.

- **Metodika:** statistiky hráče v zápase (absolutně), týmové statistiky zápasu.

### `offsides` — Ofsajdy

Kolikrát byl hráč v postavení mimo hru.

- **Metodika:** statistiky hráče v zápase (absolutně), týmové statistiky zápasu; v událostech typ `offside`.

### `takeOnsSuccessful / takeOnsTotal` — Úspěšné / všechny kličky

*take-ons*

Pokusy obejít soupeře s míčem 1v1.

- **Metodika:** V souhrn hráčů (na 90 min) jako `takeons_success` / `takeons_total` (na 90), ve statistiky hráče v zápase (absolutně) a týmové statistiky zápasu absolutně. V událostech typ `take_on`, protějšek u obránce `take_on_against`.

## 4. Očekávané hodnoty (xG, xA)

*Modelové metriky kvality šancí. Model je od poskytovatele analýzy, Eyeball jeho parametry nezveřejňuje.*

### `totalXg` — xG – očekávané góly

*expected goals*

Součet pravděpodobností, že střely skončí gólem (podle místa, úhlu, části těla, situace).

- **Metodika:** statistiky hráče v zápase (absolutně), týmové statistiky zápasu; u každé střely v událostech jako `xg`.
- **Pozor na:** Popisuje kvalitu šancí, ne kvalitu zakončení. Obecně k metrice: [[Expected goals (xG)]].

### `nonPenaltyXg` — npxG – xG bez penalt

Očekávané góly bez pokutových kopů.

- **Metodika:** statistiky hráče v zápase (absolutně), týmové statistiky zápasu.
- **Pozor na:** Pro srovnání hráčů vhodnější než `totalXg` – penalty rozhoduje exekutor, ne tvorba šancí.

### `nonPenaltyXgPerShot` — npxG na střelu

Průměrná kvalita jedné střely: npxG / střely bez penalt.

- **Metodika:** statistiky hráče v zápase (absolutně), týmové statistiky zápasu.
- **Pozor na:** Vyšší = zakončuje z lepších pozic. Při 1–2 střelách v zápase velmi nestabilní.

### `goalsXgRatio` — Poměr góly / xG

Vstřelené góly děleno xG.

- **Metodika:** statistiky hráče v zápase (absolutně), týmové statistiky zápasu.
- **Pozor na:** >1 = proměňuje nad očekávání, <1 = pod. Na malém vzorku (jeden zápas) téměř bez výpovědi.

### `totalXa` — xA – očekávané asistence

*expected assists*

Součet xG střel, které vznikly z přihrávek hráče.

- **Metodika:** statistiky hráče v zápase (absolutně), týmové statistiky zápasu; u přihrávky v událostech jako `xa`.
- **Pozor na:** Hodnotí vytvořenou šanci bez ohledu na to, jestli ji spoluhráč proměnil.

## 5. Přihrávky a rozehrávka

*Objem, přesnost, směr, délka a zóna přihrávek.*

### `passesSuccess / passesTotal` — Úspěšné / všechny přihrávky

Přihrávky, které došly ke spoluhráči, a všechny pokusy.

- **Metodika:** V souhrn hráčů (na 90 min) jako `passes_success` / `passes_total` (na 90), ve statistiky hráče v zápase (absolutně) a týmové statistiky zápasu absolutně.

### `passAccuracy / passesAccuracy` — Přesnost přihrávek

Podíl úspěšných přihrávek.

- **Metodika:** V souhrn hráčů (na 90 min) jako `passesAccuracy` v rozsahu **0–1** (0,736), ve statistiky hráče v zápase (absolutně) a týmové statistiky zápasu jako `passAccuracy` v **%** (68).
- **Pozor na:** Různý formát podle zdroje – před spojením dat sjednoť.

### `keyPasses` — Klíčové přihrávky

Přihrávky, po kterých spoluhráč vystřelil.

- **Metodika:** souhrn hráčů (na 90 min), statistiky hráče v zápase (absolutně), týmové statistiky zápasu; v událostech příznak `key_pass`.

### `passesForward / Sideways / Backward` — Přihrávky dopředu / do strany / dozadu

Přihrávky podle směru, vždy `…Success` a `…Total`.

- **Metodika:** Dopředu v souhrn hráčů (na 90 min), statistiky hráče v zápase (absolutně), týmové statistiky zápasu; do strany a dozadu jen statistiky hráče v zápase (absolutně) a týmové statistiky zápasu. V událostech atribut `direction`.
- **Pozor na:** Hranice úhlů pro směr Eyeball neuvádí.

### `passesInFinalThird / MiddleThird / DefensiveThird` — Přihrávky v útočné / střední / obranné třetině

Přihrávky podle třetiny hřiště, odkud šly; vždy Success a Total.

- **Metodika:** statistiky hráče v zápase (absolutně), týmové statistiky zápasu; v událostech atribut `third`.
- **Pozor na:** Jde o zónu, **odkud** přihrávka šla, ne kam.

### `shortPasses / mediumRangePasses / longPasses` — Krátké / střední / dlouhé přihrávky

Přihrávky podle délky; vždy Success a Total.

- **Metodika:** statistiky hráče v zápase (absolutně), týmové statistiky zápasu; v událostech atribut `length`.
- **Pozor na:** Hranice délky Eyeball neuvádí (orientačně do ~15 m / 15–30 m / nad 30 m – neověřeno).

### `crossesSuccess / crossesTotal` — Centry

Centry do pokutového území; úspěšné našly spoluhráče.

- **Metodika:** V souhrn hráčů (na 90 min) jako `crosses_*`, ve statistiky hráče v zápase (absolutně) a týmové statistiky zápasu. V událostech příznak `cross` u přihrávky.

### `controlUnderPressure` — Kontrola míče pod tlakem

Udržení míče pod tlakem soupeře.

- **Metodika:** souhrn hráčů (na 90 min), statistiky hráče v zápase (absolutně), týmové statistiky zápasu.
- **Pozor na:** V datech je zatím **vždy prázdná**.

### `launchPercent` — Podíl dlouhých nákopů

Kolik procent rozehrávek bylo dlouhým nákopem.

- **Metodika:** statistiky hráče v zápase (absolutně); hlavně u brankářů, objevuje se i u hráčů v poli.

## 6. Standardní situace

*Rozehrané standardky. Detail (co z nich vzniklo) je v událostech – atribut `restart`.*

### `freekicks` — Volné kopy

*freeKicks (tým)*

Počet rozehraných volných kopů.

- **Metodika:** statistiky hráče v zápase (absolutně), týmové statistiky zápasu.

### `corners` — Rohy

Počet rozehraných rohových kopů.

- **Metodika:** statistiky hráče v zápase (absolutně), týmové statistiky zápasu.

### `throwIns` — Auty

Počet vhozených autů.

- **Metodika:** statistiky hráče v zápase (absolutně).

## 7. Obrana a souboje

*Odebrání míče, souboje, zachycení a další obranné akce.*

### `tacklesSuccess / tacklesTotal` — Souboje o míč (tackle)

Zákroky s cílem odebrat soupeři míč; úspěšné = míč odebrán.

- **Metodika:** V souhrn hráčů (na 90 min) jako `tackles_*` (na 90), ve statistiky hráče v zápase (absolutně) a týmové statistiky zápasu. V událostech typ `tackle` s atributem ve stoje / skluzem.
- **Pozor na:** Počet z událostí a oficiální statistika se mohou drobně lišit (ověřeno: 8 vs. 7).

### `aerialDuelsSuccess / aerialDuelsTotal` — Hlavičkové souboje

Vzdušné souboje; úspěšné = vyhrané.

- **Metodika:** souhrn hráčů (na 90 min), statistiky hráče v zápase (absolutně), týmové statistiky zápasu; v událostech typ `aerial_duel` s třetinou hřiště.

### `groundDuelsSuccess / groundDuelsTotal` — Pozemní souboje

Souboje na zemi.

- **Metodika:** souhrn hráčů (na 90 min), statistiky hráče v zápase (absolutně), týmové statistiky zápasu.
- **Pozor na:** V datech je zatím **vždy prázdná** (nebo 0).

### `interceptions` — Zachycené přihrávky

Přerušení přihrávky soupeře čtením hry.

- **Metodika:** souhrn hráčů (na 90 min), statistiky hráče v zápase (absolutně), týmové statistiky zápasu; v událostech typ `interception`, případně s druhým míčem.

### `clearances` — Odkopy / odvrácení

Odvrácení míče z nebezpečného prostoru bez cílené přihrávky.

- **Metodika:** souhrn hráčů (na 90 min), statistiky hráče v zápase (absolutně), týmové statistiky zápasu; v událostech typ `clearance` s částí těla.

### `blocks` — Bloky

Zblokované střely nebo přihrávky soupeře.

- **Metodika:** souhrn hráčů (na 90 min), statistiky hráče v zápase (absolutně), týmové statistiky zápasu; v událostech typ `block` s typem po přihrávce / po střele.
- **Pozor na:** V týmových statistikách je `blocks` ve skupině Souhrn i Obrana s **různými hodnotami** – nejde o totéž.

### `recoveries` — Získané míče

Získání volného nebo odraženého míče pro svůj tým.

- **Metodika:** souhrn hráčů (na 90 min), statistiky hráče v zápase (absolutně), týmové statistiky zápasu; v událostech typ `recovery`, případně s druhým míčem.

### `interventions` — Zásahy

Obranné zásahy.

- **Metodika:** statistiky hráče v zápase (absolutně), týmové statistiky zápasu.
- **Pozor na:** V datech je zatím **vždy prázdná**.

### `mistakes` — Chyby

Chyby hráče – ztráta míče nebo chybný zákrok, které vedly k nebezpečí soupeře.

- **Metodika:** statistiky hráče v zápase (absolutně), týmové statistiky zápasu.
- **Pozor na:** Přesnou definici Eyeball neuvádí (odhad). V událostech existuje příbuzný typ `technical_error`.

## 8. Disciplína

*Fauly a karty.*

### `fouls` — Fauly

Fauly, kterých se hráč dopustil.

- **Metodika:** statistiky hráče v zápase (absolutně), týmové statistiky zápasu; v událostech typ `foul` s typem fauloval.

### `foulsWon` — Vybojované fauly

Kolikrát byl hráč faulován.

- **Metodika:** statistiky hráče v zápase (absolutně), týmové statistiky zápasu; v událostech typ `foul` s typem vybojovaný.

### `yellowCards / redCards` — Žluté / červené karty

Počet karet.

- **Metodika:** statistiky hráče v zápase (absolutně); v událostech typ `card`.

## 9. Brankář

*Brankářský blok metrik – jen u hráčů, kteří v zápase chytali.*

### `goalsConceded` — Obdržené góly

Góly, které brankář inkasoval.

- **Metodika:** souhrn hráčů (na 90 min), statistiky hráče v zápase (absolutně); v událostech typ `goal_conceded` (po střele, z vápna ano/ne).

### `savePercent` — Úspěšnost zákroků

Podíl chycených střel na branku v %.

- **Metodika:** statistiky hráče v zápase (absolutně).
- **Pozor na:** Na malém počtu střel extrémně kolísá.

### `catches` — Chycené míče

Míče, které brankář chytil do rukou.

- **Metodika:** souhrn hráčů (na 90 min), statistiky hráče v zápase (absolutně).

### `punches` — Vyboxované míče

Míče vyboxované pěstí.

- **Metodika:** souhrn hráčů (na 90 min), statistiky hráče v zápase (absolutně); v událostech typ `punch`.

### `aerialClearancesSuccess / Total` — Zákroky ve vzduchu

Řešení vysokých míčů (chycení nebo vyboxování).

- **Metodika:** souhrn hráčů (na 90 min), statistiky hráče v zápase (absolutně).

### `crossesFacedTotal` — Centry na brankáře

Centry soupeře do vápna.

- **Metodika:** statistiky hráče v zápase (absolutně).

### `crossesStoppedTotal / crossesStoppedRatio` — Zastavené centry / podíl

Centry, které brankář zachytil nebo vyboxoval, a jejich podíl.

- **Metodika:** statistiky hráče v zápase (absolutně).
- **Pozor na:** Ukazuje, jak aktivně brankář vychází na centry.

### `defensiveActionsOpaTotal` — Zákroky mimo vápno

*OPA = outside penalty area*

Obranné akce brankáře mimo pokutové území – „sweeper keeper“.

- **Metodika:** statistiky hráče v zápase (absolutně).

### `averageDefensiveActionDistance` — Průměrná vzdálenost zákroků

Průměrná vzdálenost obranných akcí od brankové čáry.

- **Metodika:** statistiky hráče v zápase (absolutně).
- **Pozor na:** Vyšší = brankář hraje výš.

### `goalsKicksSuccess / Total` — Odkopy od branky

Kopy od branky; úspěšné došly ke spoluhráči.

- **Metodika:** souhrn hráčů (na 90 min), statistiky hráče v zápase (absolutně).

### `throwsSuccess / throwsTotal / throwsRatio` — Výhozy rukou

Výhozy rukou a jejich úspěšnost.

- **Metodika:** statistiky hráče v zápase (absolutně).

### `averagePassLength` — Průměrná délka rozehrávky

Průměrná délka přihrávek a odkopů brankáře.

- **Metodika:** statistiky hráče v zápase (absolutně).

### `save` — Zákrok brankáře (událost)

Událost zákroku: chytil / vyrazil, s pádem ano/ne, po střele z vápna ano/ne, část těla.

- **Metodika:** události zápasu.

## 10. Týmové metriky

*62 metrik za zápas, vždy domácí vs. hosté. Většina jsou týmové součty hráčských metrik výše; tady jen to, co je specifické pro tým.*

### `possession` — Držení míče

Podíl držení míče v %.

- **Metodika:** Jen týmové statistiky zápasu (skupina Souhrn).
- **Pozor na:** Hráčská obdoba neexistuje.

### `averageRating (tým)` — Průměrné hodnocení týmu

Průměrný rating hráčů týmu.

- **Metodika:** týmové statistiky zápasu; i na stránce zápasu.

### `Categories` — Skupiny týmových metrik

*summary, offensive, defensive, distribution*

Souhrn (góly, střely, držení, střely na branku, fauly, ofsajdy, volné kopy, rohy, průměrné hodnocení), Útok (střely, kličky, xG, npxG, xA), Obrana (souboje, zachycení, odkopy, zásahy, získané míče, bloky, chyby, vybojované fauly), Rozehrávka (přihrávky po třetinách, délce, směru, centry).

- **Metodika:** Každá hodnota má typ: počet, procento, desetinné číslo, rating.
- **Pozor na:** Některé metriky jsou ve dvou skupinách (`shots`, `shotsOnTarget`, `shortPassesSuccess`, `blocks`) – u `blocks` s jinou hodnotou.

## 11. Události – typy

*Event data: kompletní seznam akcí obou týmů v analyzovaném zápase. 24 typů v pěti kategoriích. Každá událost má čas, hráče, tým, úspěch a místo na hřišti.*

### `pass` — Přihrávka

*Kategorie: Držení míče*

Přihrávka hráče.

- **Metodika:** Atributy: délka, směr, třetina, část těla, standardní situace, centr, klíčová přihrávka, asistence, xA, rozehrávka brankáře, ve vápně.
- **Pozor na:** Má jen místo **odkud**, ne kam. Příjemce lze dohledat podle následující události `pass_received`.

### `pass_received` — Převzetí přihrávky

*Kategorie: Držení míče*

Hráč přihrávku převzal.

- **Metodika:** Atribut druhý míč.

### `recovery` — Získaný míč

*Kategorie: Držení míče*

Hráč získal volný nebo odražený míč.

- **Metodika:** Atribut druhý míč.

### `aerial_duel` — Hlavičkový souboj

*Kategorie: Držení míče*

Vzdušný souboj.

- **Metodika:** Atribut třetina hřiště; vyplněný příznak pod tlakem.

### `tackle` — Souboj o míč

*Kategorie: Obrana*

Zákrok s cílem odebrat míč.

- **Metodika:** Atribut ve stoje / skluzem; úspěch = odebráno.

### `clearance` — Odkop / odvrácení

*Kategorie: Obrana*

Odvrácení míče.

- **Metodika:** Atribut část těla; vyplněný příznak pod tlakem.

### `interception` — Zachycená přihrávka

*Kategorie: Obrana*

Přerušení přihrávky soupeře.

- **Metodika:** Atribut druhý míč.

### `block` — Blok

*Kategorie: Obrana*

Zblokovaná přihrávka nebo střela.

- **Metodika:** Atribut po přihrávce / po střele.

### `ball_out_of_play` — Míč mimo hru

*Kategorie: Obrana*

Míč opustil hřiště.

### `take_on_against` — Obcházen kličkou

*Kategorie: Obrana*

Hráč byl obejit kličkou soupeře (protějšek `take_on`).

### `shot` — Střela

*Kategorie: Útok*

Pokus o střelu.

- **Metodika:** Atributy: xG, na branku / mimo / zblokovaná, místo v bráně, část těla, z vápna, standardní situace; vyplněný příznak pod tlakem.

### `take_on` — Klička

*Kategorie: Útok*

Pokus obejít soupeře.

- **Metodika:** Atribut třetina hřiště.

### `technical_error` — Technická chyba

*Kategorie: Útok*

Technická chyba hráče s míčem.

### `save` — Zákrok brankáře

*Kategorie: Brankář*

Zákrok na střelu.

- **Metodika:** Viz kategorie Brankář.

### `goal_conceded` — Inkasovaný gól

*Kategorie: Brankář*

Gól do branky brankáře.

- **Metodika:** Atributy typ (po střele), po střele z vápna.

### `catch_interception` — Brankář zachytil

*Kategorie: Brankář*

Brankář zachytil míč (centr, přihrávku).

- **Metodika:** Atribut část těla.

### `punch` — Brankář vyboxoval

*Kategorie: Brankář*

Brankář míč vyboxoval.

### `goal` — Gól

*Kategorie: Administrativní*

Vstřelený gól (navazuje na střelu).

- **Metodika:** Atribut typ gólu (ze hry).

### `foul` — Faul

*Kategorie: Administrativní*

Faul.

- **Metodika:** Atribut fauloval / vybojovaný.

### `card` — Karta

*Kategorie: Administrativní*

Udělená karta.

- **Metodika:** Atribut žlutá / červená.

### `substitution` — Střídání

*Kategorie: Administrativní*

Střídání hráče.

- **Metodika:** Atribut odchod / příchod.

### `offside` — Ofsajd

*Kategorie: Administrativní*

Postavení mimo hru.

### `start_of_half / end_of_half` — Začátek / konec poločasu

*Kategorie: Administrativní*

Hranice poločasu.

- **Metodika:** Nese oficiální délku poločasu a nastavení.

## 12. Události – atributy

*Údaje u každé události a detailní atributy podle typu.*

### `success` — Úspěch

Zda akce byla úspěšná (přihrávka došla, souboj vyhrán…).

- **Metodika:** U všech událostí s hráčem.

### `underPressure` — Pod tlakem

Zda byl hráč při akci pod tlakem soupeře.

- **Metodika:** Příznak u události.
- **Pozor na:** Vyplněný jen u střel, hlavičkových soubojů a odkopů. U přihrávek je **vždy „ne“** – nepoužívat pro analýzu přihrávek pod tlakem.

### `category` — Kategorie události

Držení míče, Obrana, Útok, Brankář, Administrativní.

### `groups` — Skupiny

`all` = všechny, `main` = hlavní momenty zápasu, `my` = akce vybraného hráče.

### `length` — Délka přihrávky

krátká / střední / dlouhá.

- **Metodika:** U `pass`.
- **Pozor na:** Hranice neuvedené.

### `direction` — Směr přihrávky

dopředu / do strany / dozadu.

- **Metodika:** U `pass`.

### `third` — Třetina hřiště

obranná / střední / útočná.

- **Metodika:** U `pass`, `aerial_duel`, `take_on`.

### `body_part` — Část těla

pravá noha / levá noha / hlava / ruka / jiné.

- **Metodika:** U `pass`, `shot`, `clearance`, `save`, `catch_interception`.

### `restart` — Standardní situace

ze hry / aut / volný kop / roh / kop od branky.

- **Metodika:** U `pass` a `shot`.

### `cross / key_pass / assist / inside_pa` — Centr / klíčová přihrávka / asistence / ve vápně

Příznaky u přihrávky.

- **Metodika:** U `pass`.

### `xa` — xA přihrávky

Hodnota šance vytvořené přihrávkou.

- **Metodika:** U `pass`.

### `gk_pass` — Rozehrávka brankáře

Typ rozehrávky, např. výkop z ruky.

- **Metodika:** U `pass` brankáře.

### `xg` — xG střely

Pravděpodobnost gólu u střely.

- **Metodika:** U `shot`.

### `on_target` — Výsledek střely

na branku / mimo / zblokovaná.

- **Metodika:** U `shot`.

### `shot_location` — Místo v bráně

nahoře / uprostřed / dole × vlevo / uprostřed / vpravo.

- **Metodika:** U střel na branku.
- **Pozor na:** Pohled je z perspektivy střelce (neověřeno).

### `tackle_type` — Typ souboje

ve stoje / skluzem.

- **Metodika:** U `tackle`.

### `block_type` — Typ bloku

po přihrávce / po střele.

- **Metodika:** U `block`.

### `foul_type` — Typ faulu

fauloval / vybojovaný.

- **Metodika:** U `foul`.

### `second_ball_won` — Druhý míč

Akce získala druhý (odražený) míč.

- **Metodika:** U `pass_received`, `recovery`, `interception`.

### `goal_type / goal_conceded_type` — Typ gólu / inkasovaného gólu

ze hry / po střele.

- **Metodika:** U `goal`, `goal_conceded`.

### `save_type / diving_save / after_shot_inside_pa` — Typ zákroku

chytil / vyrazil, s pádem, po střele z vápna.

- **Metodika:** U `save`.

### `card_type / sub_type` — Karta / střídání

žlutá / červená; odchod / příchod.

- **Metodika:** U `card`, `substitution`.

## 13. Profil hráče – odvozené metriky

*Sekce profilu hráče, které Eyeball počítá nad zápasovými daty. Každá má vlastní filtry (sezóna, pozice, posledních N zápasů).*

### `performance` — Výkon

Metriky na 90 min ve skupinách útok / obrana / rozehrávka / brankář.

- **Metodika:** Filtry pozice, sezóna, celkově / posledních N zápasů.

### `performance-radar` — Radar výkonu

*ratingPercentTop*

6 metrik podle pozice s hodnotou a **percentilem** proti databázi (např. u stopera hlavičky, přihrávky, souboje, získané míče, odkopy, bloky).

- **Metodika:** Filtr pozice.
- **Pozor na:** Sada metrik se mění s pozicí – radary různých pozic nesrovnávej.

### `standout-metrics` — Výjimečné metriky

*percentTop*

Metriky, ve kterých hráč nejvíc vyniká, s údajem „top X %“.

- **Metodika:** Filtr celkově / poslední zápas / 5 / 10 zápasů.

### `seasonal-stats` — Sezónní statistiky

Zápasy, minuty, góly, asistence po sezónách.

### `key-events` — Klíčové události

Vybrané akce hráče po kategoriích s odkazem na video.

### `event-types` — Typy událostí s počty

Kolikrát hráč provedl jednotlivé typy akcí, vč. odvozených (střela na branku, zblokovaná střela, centr, asistence).

- **Metodika:** Filtry sezóna, věková kategorie, klub, pozice.

### `Tolerance` — Tolerance (behaviorální signál)

Kolik tlaku zápasu hráč vydrží, než mu začne klesat výkon.

- **Metodika:** Skóre, pásmo s popisem (např. „stays composed late“), běžný rozsah, porovnání s kohortou v %, trend.
- **Pozor na:** Behaviorální signály vyžadují aspoň 360 analyzovaných minut; mají míru jistoty (`confidence`).

### `Sensitivity` — Citlivost (behaviorální signál)

Jak výrazně výkon klesne, když tlak začne působit.

- **Metodika:** Stejná struktura jako Tolerance.

### `Recovery` — Zotavení (behaviorální signál)

Jak rychle se hráč vrátí na svou úroveň, když ho tlak srazil pod hranici tolerance.

- **Metodika:** Stejná struktura jako Tolerance.

### `Behavioral signals – cohort & period` — Kohorta a období behaviorálních signálů

Kohorty: věková kategorie, věková kategorie + pozice, pozice. Období: posledních 10 zápasů, sezóna (až 3 sezóny).

- **Metodika:** K signálům je slovní shrnutí profilu (nadpis + text).
- **Pozor na:** Kombinace kohorta × období nejsou všechny dostupné (pozice jen přes všechny sezóny).

### `behavioral-archetypes` — Behaviorální archetypy

Dominantní a vedlejší archetyp hráče se shrnutím.

- **Pozor na:** U běžných hráčů zatím stav „nedokončeno“ – dle schůzky s Eyeballem placená nadstavba nové verze.

### `body-measurements` — Tělesné míry (sken těla)

Obvody horní a dolní poloviny těla, celotělové míry, změny tělesného složení, trendy.

- **Metodika:** Jen pokud má hráč skeny a jsou sdílené (`biometrics-availability`).

## 14. Fyzické metriky

*Fyzická data z video analýzy. Na profilu hráče za sezónu nebo všechny sezóny; k zápasu jen jako PDF report.*

### `highestTopSpeed` — Maximální rychlost

Nejvyšší naměřená rychlost (km/h) a zápas, kde padla.

- **Metodika:** Příznak, zda maximum padlo ve vybrané sezóně.
- **Pozor na:** Jedno měření – citlivé na chybu. Pro srovnání stabilnější je průměrná top rychlost.

### `averageTopSpeed` — Průměrná top rychlost

Součet maximálních rychlostí ze zápasů děleno počtem zápasů v sezóně.

- **Metodika:** Se změnou proti minulé sezóně (`changeVsPreviousSeason`).

### `averageDistanceCovered` — Uběhnutá vzdálenost na 90 min

Celková vzdálenost za zápas přepočtená na 90 minut, průměr přes zápasy sezóny (km).

- **Pozor na:** Přepočet na 90 u krátkých výkonů nadhodnocuje.

### `accelerations / decelerations` — Akcelerace / decelerace na 90 min

Počet akcelerací a decelerací za zápas přepočtený na 90 minut.

- **Metodika:** Práh podle popisu v portálu ≥ 10,8 km/h (resp. ≤ −10,8).
- **Pozor na:** Jednotka prahu je v popisu Eyeballu uvedená jako km/h – u akcelerací nezvyklé, ověřit.

### `movementDistribution` — Rozložení pohybu v zónách

Podíl času (%) a minuty na 90 v šesti zónách: stání, chůze, klus, běh, rychlý běh, sprint.

- **Metodika:** Zóny řazené od nejpomalejší.
- **Pozor na:** Rychlostní hranice zón Eyeball neuvádí – nesrovnávat přímo se SkillCornerem ani GPS.

### `Physical report (PDF)` — PDF report fyzické analýzy zápasu

Report fyzických metrik k zápasu a video fyzické analýzy.

- **Metodika:** Na stránce zápasu a v dokumentech profilu hráče.
- **Pozor na:** Datový soubor za reportem je zamčený – data k zápasu jsou jen v PDF. Fyzickou analýzu nemá každý zápas.

## Poznámky ke zdroji

**Bez oficiálního glosáře:** definice vycházejí z názvů polí v datech portálu, z popisků aplikace a z ověření na zápasech (počty z událostí sedí s oficiálními statistikami hráče, drobné odchylky u soubojů). Výpočet ratingu, modelu xG/xA ani behaviorálních signálů Eyeball nezveřejňuje.

**Nová verze platformy:** do konce roku 2026 přechází Eyeball na novou verzi s placenými nadstavbami (fyzické a behaviorální metriky, AI reporting) – názvy i dostupnost metrik se mohou změnit. Viz [[SK Sigma Olomouc/Meetings/2026-10-19 – Eyeball – Martin Neoral|schůzka s Eyeballem]].

**Lokální soubor:** stejné metriky v Excelu (EN – česky – vysvětlení) jsou v `~/Desktop/Sigma/eyeball_stats/Slovník metrik.xlsx`; tahle poznámka je úplnější (události, týmové, profil, fyzické).

## Souvislosti

- [[Eyeball – platforma, data a metriky]] – přehled platformy: datové oblasti, oprávnění, jak data stahujeme, pravidla. Tenhle slovník je jeho detailní metrikový protějšek.
- [[Eyeball]] – wiki stránka o Eyeballu jako zdroji.
- [[SK Sigma Olomouc/Meetings/2026-10-19 – Eyeball – Martin Neoral|2026-10-19 – Eyeball – Martin Neoral]] – schůzka o API, nové verzi a placených nadstavbách.
- [[Wyscout – slovník metrik]] – stejný typ slovníku pro Wyscout. Pozor: Wyscout má přesně definované prahy (dlouhá přihrávka, progresivní přihrávka), Eyeball je neuvádí – metriky stejného jména nejsou zaměnitelné.
- [[SkillCorner – slovník metrik]] – tracking a fyzická data. Pozor: Eyeball fyzické zóny nemají zveřejněné hranice, SkillCorner ano (HSR 20–25 km/h, sprint nad 25 km/h).
- [[Expected goals (xG)]] – koncept xG obecně; Eyeball dává xG, npxG, npxG na střelu, góly/xG a xA.
- [[Normalizace herních dat]] – přepočty na 90 minut; Eyeball souhrn je per 90, zápas absolutně.
- [[📊 Fotbalová zápasová data]] – pohledy na zápasová data.
- [[📡 GPS Data]] – fyzická data z GPS; Eyeball měří z videa, jiné prahy.
- [[🥅 Brankářská data]] – Eyeball má vlastní brankářský blok (zákroky mimo vápno, vzdálenost zákroků, centry).
- [[Karta hráče 🎯]] – kam mohou metriky, radar a behaviorální signály vstupovat.
- [[Datový skauting – metriky a úskalí]] – proč metriky samy nestačí.

## Otevřené body

- [ ] Získat od Eyeballu oficiální definice (rating, xG model, hranice délky přihrávek a rychlostních zón, behaviorální signály) – nejlépe spolu s dokumentací API.
- [ ] Ověřit jednotku prahu akcelerací (10,8 km/h?).
- [ ] Po přechodu na novou verzi platformy zkontrolovat, jestli se nezměnily názvy a dostupnost metrik.
- [ ] Rozhodnout, které Eyeball metriky vstupují do [[Karta hráče 🎯]] a v jaké podobě (per 90 / percentil).
