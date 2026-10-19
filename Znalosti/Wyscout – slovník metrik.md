---
datum: 2026-10-19
aktualizovano: 2026-10-19
typ: referenční slovník
zdroj: dataglossary.wyscout.com (zpracováno s Claude)
projekt: SK Sigma Olomouc – analytika
tags: [wyscout, herni-data, metriky, slovnik, event-data, skauting]
aliases: [Wyscout glosář, Wyscout metriky, Wyscout Data Glossary]
---
# Wyscout – slovník metrik

> Kompletní český výklad oficiálního [Wyscout Data Glossary](https://dataglossary.wyscout.com/) — **320 hesel** ve 14 kategoriích: 90 pojmů a eventů (definice, API identifikátory, atributy, nástrahy) a 230 metrik v katalogu (názvy sloupců tak, jak se objevují v exportech). Stav ke 17. 8. 2026.

## Kontext a cíl

[[Wyscout]] je v Sigmě zdroj zápasových (event) dat a videa, ale jeho oficiální glosář je anglicky, roztříštěný do 93 samostatných stránek a definice metrik jsou schované ve třech přehledových tabulkách. Cílem bylo dostat všechno na jedno místo v češtině, a navíc doplnit to, co v glosáři explicitně nestojí: kde jsou v definicích pasti, které metriky spolu nejsou srovnatelné a kde má zdroj chyby.

Vzniklo jako protějšek ke slovníku [[SkillCorner – slovník metrik]] (127 hesel) — dohromady pokrývají oba hlavní zdroje herních dat, se kterými pracujeme. Navazuje na pohledy na data shrnuté v [[📊 Fotbalová zápasová data]] a na přepočty v [[Normalizace herních dat]].

Anglický název je ten, který najdeš v aplikaci, v API a v exportech — používej ho jako klíč. České názvy jsou pracovní překlady. Údaj `API` uvádí `eventId`, `subeventId` a vztah k nadřazenému typu. Sekce **Pozor na** je u většiny hesel to nejcennější. Neoficiální dokument.

## Nejdůležitější nástrahy

Výtah toho, na co se v praxi naráží nejčastěji:

1. **PPDA jde obráceně.** Nižší hodnota = intenzivnější presink. `Challenge intensity` měří velmi podobnou věc opačnou logikou (vyšší = aktivnější). Do jednoho grafu je nedávej bez upozornění. Průměr top 5 lig 2018/19 byl 11,01, nejlepší Eibar 6,72.
2. **„Úspěšná přihrávka“ je definovaná jen tím, kdo se míče dotkl příště** — ne záměrem. Nepřesná přihrávka, kterou náhodou zpracoval spoluhráč, se počítá jako přesná.
3. **„Úspěšná střela“ = na branku, ne gól.** Střela do tyče je neúspěšná, což systematicky sráží `Shots on target %` hráčům, kteří střílí přesně k tyčím.
4. **`Minutes played` zahrnuje nastavení.** Celý zápas s 5 minutami nastavení = 95 minut, takže přepočet na 90 minut hodnoty mírně stlačuje proti poskytovatelům, kteří počítají 90 fixně. Viz [[Normalizace herních dat]].
5. **Souřadnice jsou v procentech, ne v metrech,** a jsou perspektivní — tentýž event má pro každý ze dvou týmů jiné souřadnice.
6. **Progresivní přihrávka má tři různé prahy** (30 / 15 / 10 m podle poloviny), takže stopeři a záložníci nejsou v téhle metrice srovnatelní bez rozpadu podle zóny.
7. **Rohy, auty, rozehrání od branky a centry ze standardek se nepočítají do přihrávek.** Přesnost přihrávek brankáře tedy nezahrnuje jeho rozehrávky od branky.
8. **xG penalty je fixně 0,76.** Tým s hodně penaltami má xG nadhodnocené vůči skutečné kvalitě šancí z otevřené hry. Obecně k metrice [[Expected goals (xG)]].
9. **Čtyři eventy existují jen ve videu, ne v API:** Covering teammate, Defensive positioning, Off the ball movement, Pressing duel. Kdo pracuje výhradně přes API, o tuhle vrstvu přichází.
10. **Dvě chyby přímo v oficiálním katalogu:** `Progressive runs / 90` je popsáno jako „number of progressive passes“ a `Shot assists / 90` jako „number of dribbles“. U pojmu `Ball out` má zdroj zaměněné touchline a byline.

## Obsah

1. **Základ a metodika** — 5 záznamů
2. **Držení míče a fáze hry** — 3 záznamů
3. **Přihrávky** — 19 záznamů
4. **Střelba a góly** — 4 záznamů
5. **Duely** — 10 záznamů
6. **Obranné akce a přechody** — 7 záznamů
7. **Brankář** — 6 záznamů
8. **Fauly, karty a ofsajd** — 12 záznamů
9. **Standardní situace** — 9 záznamů
10. **Pohyb, běhy a doteky** — 8 záznamů
11. **Modely a odvozené metriky** — 7 záznamů
12. **Katalog — fyzické metriky** — 14 záznamů
13. **Katalog — hráčské metriky** — 78 záznamů
14. **Katalog — zápasové a týmové metriky** — 138 záznamů

## Prahy a hranice

Numerické hranice, na kterých stojí definice. Nejčastější zdroj chyb při srovnávání.

| Pojem | Hranice | Poznámka |
|---|---|---|
| Long pass | pozemní nad 45 m NEBO vysoká nad 25 m | Podtypy: Launch (84), High pass (83), Long ground pass (85). |
| Short/medium pass | obecně pod 40 m | Definováno negativně — vše, co není dlouhá přihrávka. |
| Lateral pass | nad 12 m | Kratší příčné přihrávky se do forward/backward/lateral nepočítají. |
| Progressive pass / run | 30 m ve vlastní polovině | Oba body ve vlastní polovině. |
| Progressive pass / run | 15 m přes půlicí čáru | Body v různých polovinách. |
| Progressive pass / run | 10 m v polovině soupeře | Oba body v polovině soupeře. |
| Acceleration (event) | aspoň 10 m | Hráč se musí dotknout míče, jinak jde o off the ball move. |
| Deep completion / cross | do 20 m od branky | Zóna definovaná vzdáleností, ne vápnem. |
| Cross — flank | 23 m od postranní čáry | Fixní pás, nezávislý na rozměrech hřiště. |
| Counterpressing recovery | držba soupeře pod 5 s | Čistě časová definice. |
| Shot after corner | do 14 s od rohu | Stejné okno platí pro Corners with shots a Free kicks with shots. |
| Loss leading to opponent shot | do 20 s | Atribut ztráty. |
| Danger zone (střely) | x ≥ 84,29 a y mezi 36,29 a 63,71 | Souřadnice v % (viz Pitch coordinates). |
| xG penalty | fixně 0,76 | Nezávisle na exekutorovi i brankáři. |
| PPDA — zóna | posledních 60 % hřiště | Obranné akce: fauly, zachycení, vyhrané def. duely, skluzy. |
| Possession-adjusted | referenčních 60 min | Wyscout vzal 60 min jako čistý čas hry; přepočet na držení 50/50. |
| Open play possession | 0–10 / 10–20 / 20–45 / 45+ s | Short / Medium / Long / Very long. |
| Duel — hranice typu | úroveň loktů | Pod = pozemní duel, nad = vzdušný duel. |
| Count HSR (fyzické) | 20–25 km/h, aspoň 1 s | Advanced Search, jen vybrané soutěže. |
| Count Sprint (fyzické) | nad 25 km/h, aspoň 1 s | Advanced Search. |
| Running distance (fyzické) | 15–20 km/h | Advanced Search. |
| HI distance (fyzické) | nad 20 km/h | Součet HSR a sprintu. |
| High / Medium Acceleration | nad 3 / 1,5–3 m/s², aspoň 1 s | Decelerace zrcadlově v negativních hodnotách. |
| Fyzické metriky — dostupnost | aspoň 60 min aktivní hry | Jen vybrané soutěže; napříč všemi zápasy. |

## 1. Základ a metodika

*Pojmy, bez kterých se ostatní definice nedají správně přečíst: souřadnicový systém, odehrané minuty, jak Wyscout počítá držení míče, co znamená normalizace na 90 minut a possession-adjusted.*

### `Pitch coordinates` — Souřadnice hřiště

Souřadnice eventu závisí na subjektu, ke kterému se vztahuje. Branka, kterou subjekt brání, je vždy x = 0 %, směr jeho útoku je vždy x = 100 %. Všechny hodnoty jsou procenta ve formátu (x, y).

- **Detaily a metodika:** Systém je perspektivní, ne absolutní: pro každý tým se orientace normalizuje tak, aby jeho vlastní branka byla na nule. Díky tomu se dá analyzovat kterýkoli tým bez ohledu na to, na kterou stranu v dané půli útočil.
- **Pozor na:** Souřadnice jsou v procentech, ne v metrech. Když chceš vzdálenosti v metrech, musíš je přepočítat rozměry hřiště — a ty se mezi stadiony liší. Zároveň si dej pozor, že tentýž event má pro každý ze dvou týmů jiné souřadnice.

### `Minutes played` — Odehrané minuty

Každému hráči se přiřadí skutečně odehrané minuty včetně nastavení. Když hráč odehraje celý zápas, ve kterém byly ve první půli nastaveny 2 minuty a ve druhé 3 minuty, jeho odehrané minuty pro tento zápas jsou 95.

- **Detaily a metodika:** Normalizace na 90 minut vychází právě z tohoto čísla. Když hráč v takovém zápase vystřelil 10× a časový rámec tvoří jen tento zápas, jeho Shots/90 je 9,47 — ne 10.
- **Pozor na:** Tohle je zdroj systematického rozdílu proti poskytovatelům, kteří počítají 90 minut fixně. Čím delší nastavení, tím víc přepočet na 90 minut hodnoty stlačí. U hráčů s malým počtem minut je přepočet nestabilní.

### `Ball possession` — Držení míče

Metrika, která kvantifikuje, jak dlouho tým skutečně drží míč. Dostupná jako čistý čas nebo jako procento držení v porovnání se soupeřem.

- **Detaily a metodika:** Wyscout počítá procento držení z čistého času s míčem. Držba je sekvence eventů s míčem téhož týmu. Čas, kdy je míč mimo hru (v zámezí nebo když se rozehrává standardka), se nepočítá ani jednomu týmu. Akce soupeře, které netvoří smysluplné držení míče — prohrané duely, minuté míče, odrazy okamžitě zpracované zpět — držbu nepřeruší.
- **Atributy:** Otevřená hra (open play possessions): držby, které nezačínají standardkou. Dělí se podle délky na short (0–10 s), medium (10–20 s), long (20–45 s) a very long (nad 45 s).
- **Pozor na:** Jiní poskytovatelé používají jednodušší algoritmus, který bere jen přesné přihrávky obou týmů. Wyscout to explicitně považuje za méně přesné, protože ne každá přihrávka trvá stejně dlouho. Prakticky to znamená, že procento držení z Wyscoutu se nemusí shodovat s číslem odjinud — a rozdíl není chyba.

### `Possession-adjusted` — Upraveno na držení míče

*PAdj · Opp30*

Metoda přepočtu obranných statistik tak, aby brala v úvahu držení míče. Logika: obranný přínos můžeš tvořit jen tehdy, když nemáš míč.

- **Detaily a metodika:** Průměrná délka zápasu mírně roste každý rok a v roce 2019 byla 95 minut 30 sekund, ale čistý čas hry klesá a bývá mezi 50 a 60 minutami podle ligy. Wyscout vzal jako referenci 60 minut. Hodnoty se přepočítají, jako kdyby se zápas hrál s držením 50 % / 50 %.
- **Pozor na:** Bez této úpravy najdeš v žebříčcích obranných akcí skoro výhradně obránce slabších týmů — jsou dominovaní, takže musí dělat víc akcí. Obránci týmů založených na držení míče dělají přirozeně méně akcí. Přepočet tuhle systematickou zaujatost odstraňuje, ale nesmíš pak surová a upravená čísla míchat v jednom srovnání.

### `Player reports` — Hráčské reporty

Wyscout organizuje parametry hodnocení hráče podle pozice — každá pozice má vlastní sadu metrik odpovídající jejím úkolům.

- **Detaily a metodika:** Brankáři: obdržené góly, čelené střely, zákroky, xG saved, zisky, defenzivní duely, vzdušné duely, přihrávky, průměrná délka přihrávky. Krajní obránci: zisky, counterpressing zisky, defenzivní a ofenzivní duely, kličky, přihrávky, centry, průměrná délka přihrávky, progresivní běhy a přihrávky, deep completions, deep completed crosses, góly, xG, asistence, xA, střely, xG na střelu, shot assists. Střední obránci: jako krajní, navíc vzdušné duely, bez ofenzivních výstupů. Záložníci: góly, xG, asistence, xA, střely, xG na střelu, přihrávky, centry, shot assists, všechny typy duelů, kličky, progresivní běhy a přihrávky, deep completions, zisky. Útočníci: góly, xG, asistence, xA, střely, xG na střelu, přihrávky, centry, shot assists, second assists, doteky ve vápně, přijaté přihrávky, přijaté dlouhé přihrávky, ofenzivní duely, kličky, progresivní běhy a přihrávky, zisky v útočné třetině, counterpressing zisky.
- **Pozor na:** Sady se mezi pozicemi liší, takže report jedné pozice se nedá přímo porovnávat s reportem jiné. Zároveň platí, že hráč zařazený na jinou pozici, než na které reálně hraje, dostane nevhodnou sadu metrik.


## 2. Držení míče a fáze hry

*Jak Wyscout krájí hru na držby a útoky: otevřená hra vs. standardky, brejky, poziční útoky, přechodové fáze.*

### `Attack` — Útok

Útok je držba míče týmu. Wyscout ji dělí do čtyř kategorií.

- **Detaily a metodika:** Open play attack — držba, která nezačíná standardkou (Free Kick Cross, Free Kick Shot, Corner, Throw In nebo Penalty). Aby se kvalifikovala jako útok, musí mít aspoň jednu úspěšnou akci v útočné třetině soupeře. Counterattack — po zisku míče tým rychle přechází z obrany do útoku a snaží se zastihnout soupeře mimo obranné rozestavení. Positional attack — útok z otevřené hry, který není brejk. Set piece attack — jakákoli držba, která začíná rohem nebo centrem ze standardní situace.
- **Pozor na:** Podmínka „aspoň jedna úspěšná akce v útočné třetině“ znamená, že držba zakončená ztrátou ve středu hřiště se jako útok vůbec nepočítá. Počet útoků proto není počet držeb.

### `Counterattack` — Brejk

Přechod držení míče od soupeře, kdy tým rychle přechází z obranné do útočné fáze a snaží se zastihnout soupeře mimo obranné rozestavení.

- **Pozor na:** Poziční útok je definován negativně — jako útok z otevřené hry, který není brejk. Hranice mezi nimi je proto určena klasifikací brejku, ne vlastní definicí pozičního útoku.

### `Transition` — Přechodová fáze

Event, ve kterém jeden tým ztrácí nebo získává držení míče.

- **Detaily a metodika:** Má dva podtypy: Loss (ztráta) a Recovery (zisk).
- **Pozor na:** Ztráta a zisk jsou dvě strany téže věci, ale nejsou vždy párové: držby, které začínají po zámezí nebo po faulu, se za zisk nepočítají, i když předtím byla ztráta.


## 3. Přihrávky

*Nejrozsáhlejší skupina eventů. Klíčové je vědět, které typy se do statistiky přihrávek počítají a které ne — a že „úspěšná“ přihrávka je definována jen tím, kdo se dotkl míče příště.*

### `Pass` — Přihrávka

*eventId 8 · subeventId 85*

Pokus přihrát míč spoluhráči.

- **Detaily a metodika:** Do statistiky přihrávek se počítají: centry, hlavičkové přihrávky, přihrávky rukou, smart passes a dlouhé přihrávky. Nepočítají se: rozehrání od branky, rohy, centry ze standardek a auty. Přihrávky se klasifikují jako forward, backward a lateral, přičemž laterální přihrávka musí být delší než 12 metrů.
- **Atributy:** Successful: Yes (tagId 1801) / No (tagId 1802) — přihrávka je úspěšná, pokud se míče příště dotkne spoluhráč. Interception (tagId 1401): Yes / No. Link-up play: Yes / No.
- **Související metriky:** Passes / 90 · Pass accuracy
- **Pozor na:** Dvě pasti. (1) Součet dopředných, zpětných a laterálních přihrávek může být menší než celkový počet přihrávek — laterální se počítají jen nad 12 metrů, takže krátké příčné přihrávky nepadnou nikam. (2) „Úspěšná“ je definována jen tím, kdo se dotkl míče příště, ne záměrem — nepřesná přihrávka, kterou náhodou zpracoval spoluhráč, se počítá jako přesná.

### `Cross` — Centr

*eventId 8 · subeventId 80 · podtyp Pass*

Míč zahraný z útočných křídelních prostorů směrem na spoluhráče do prostoru před brankou soupeře.

- **Detaily a metodika:** Obsahuje jen centry z otevřené hry, ne ze standardních situací (rohy, volné kopy).
- **Atributy:** Height: high (tagId 801) nad úrovní pasu / low (tagId 802) pod úrovní pasu / blocked (tagId 2101) — zblokované centry se podle výšky nerozlišují. Successful: Yes (1801) / No (1802) — úspěšný, pokud je další dotek spoluhráče. Foot: Left (401) / Right (402). Flank: Left / Right — levé křídlo je nejlevějších 23 metrů, pravé nejpravějších 23 metrů.
- **Související metriky:** Crosses / 90 · Cross accuracy · Crosses from left/right flank per 90 · Cross accuracy from left/right flank (%) · Crosses to six-yard box per 90 · Cross accuracy to six-yard box (%)
- **Pozor na:** Definice křídla 23 metrů je fixní pás, ne relativní k rozměrům konkrétního hřiště. „Přesný centr“ znamená jen, že se míče dotkl spoluhráč — ne že z toho byla šance.

### `Long pass` — Dlouhá přihrávka

*eventId 8 · subeventId 83 · podtyp Pass*

Pozemní přihrávka delší než 45 metrů nebo vysoká přihrávka delší než 25 metrů.

- **Detaily a metodika:** Tři podtypy: Launch (subeventId 84) — přihrávka, která nemá zjevný konkrétní cíl. High pass (subeventId 83) — nad úrovní ramen a delší než 25 metrů. Long ground pass (subeventId 85) — delší než 45 metrů. Definice dlouhé přihrávky zahrnuje všechny tři. 75 % dlouhých přihrávek je cílených a asi 50 % úspěšných.
- **Atributy:** Successful: Yes (1801) / No (1802). Through Pass (tagId 901): Yes / No.
- **Související metriky:** Long passes / 90 minutes · Accurate long passes (%)
- **Pozor na:** Prahy jsou různé pro pozemní a vysokou přihrávku (45 vs. 25 m), takže „dlouhá přihrávka“ není jedna vzdálenostní kategorie. Nízká úspěšnost dlouhých přihrávek je normou, ne slabinou — 50 % je průměr.

### `Short/medium pass` — Krátká/středně dlouhá přihrávka

*podtyp Pass*

Přihrávka, která není explicitně označená jako dlouhá. Obecně to znamená přihrávku kratší než 40 metrů.

- **Detaily a metodika:** Přibližně 2,5 % z nich se kvalifikuje jako smart pass a asi 16 % jako progresivní přihrávka. V průměru je 86 % z nich úspěšných.
- **Atributy:** Successful: Yes / No
- **Související metriky:** Short/medium passes / 90 · Short/medium passes %
- **Pozor na:** Definice je negativní (co není dlouhé), takže hranice „obecně 40 metrů“ nesouhlasí s prahy dlouhé přihrávky (45 m pozemní, 25 m vysoká). Mezi 25 a 45 metry proto o zařazení rozhoduje výška, ne délka.

### `Smart pass` — Kreativní průnikovka

*eventId 8 · subeventId 86 · podtyp Pass*

Kreativní a průniková přihrávka, která se snaží prolomit obranné linie soupeře a získat výraznou výhodu v útoku.

- **Detaily a metodika:** Obvykle jde o krátké nebo středně dlouhé přihrávky, ale může zahrnovat i dlouhé pozemní přihrávky.
- **Atributy:** Successful: Yes (1801) / No (1802). Interception (1401): Yes / No. Link-up play (tagId 7): Yes / No. Through pass (901): Yes / No.
- **Související metriky:** Smart passes / 90 · Accurate smart passes (%)
- **Pozor na:** Je to hodnocení záměru a kvality od taggera, ne geometrická definice. Mezi poskytovateli nemá ekvivalent, takže smart passes nelze srovnávat s ničím zvenčí. Tvoří jen ~2,5 % krátkých a středních přihrávek, takže vzorky jsou malé.

### `Through pass` — Průniková přihrávka

*podtyp Pass*

Přihrávka zahraná do prostoru za obrannou linii, o kterou se má spoluhráč utkat.

- **Detaily a metodika:** Průniková přihrávka může být zároveň smart pass.
- **Atributy:** Successful: Yes (1801) / No (1802) — úspěšná, pokud je další dotek spoluhráče.
- **Související metriky:** Through passes / 90 · Accurate through passes (%)
- **Pozor na:** „O kterou se má spoluhráč utkat“ znamená, že přihrávka nemusí být přesná v běžném smyslu. Nízká úspěšnost je vlastností typu, ne chybou hráče.

### `Head pass` — Hlavičková přihrávka

*eventId 8 · subeventId 82 · podtyp Pass*

Pokus přihrát míč spoluhráči hlavou.

- **Detaily a metodika:** Používá se v situacích, kdy nejsou poblíž soupeři nebo kdy má hráč jasnou výhodu ve vzduchu a soupeř nepředstavuje žádnou hrozbu.
- **Atributy:** Successful: Yes (1801) / No (1802).
- **Pozor na:** Hlavičková přihrávka proto nikdy nemůže být vzdušný duel. Když se o míč ve vzduchu bojuje, jde o duel, ne o přihrávku — což znamená, že hlavičky pod tlakem v počtu přihrávek chybí.

### `Hand pass` — Přihrávka rukou

*eventId 8 · subeventId 81 · podtyp Pass*

Pokus brankáře přihrát míč spoluhráči rukama.

- **Detaily a metodika:** Provést ji může jen hráč označený jako brankář, jinak by šlo o porušení pravidel. Auty jsou z této kategorie výslovně vyloučeny. Fauly rukou včetně pokusů o přihrávku se za přihrávku rukou nepočítají.
- **Atributy:** Successful: Yes / No
- **Pozor na:** Přihrávka rukou se počítá do celkové statistiky přihrávek. U brankářů to nadhodnocuje počet přihrávek proti brankářům z lig, kde se víc rozehrává nohou.

### `Key pass` — Klíčová přihrávka

*podtyp Pass*

Přihrávka, která okamžitě vytvoří jasnou gólovou příležitost pro spoluhráče.

- **Detaily a metodika:** Klíčové přihrávky zahrnují jen akce typu přihrávka. Pokud je klíčová přihrávka zároveň shot assist, dostane hodnotu xA. Klíčová přihrávka může zároveň být asistence.
- **Atributy:** Successful: Yes / No — úspěšná, pokud je další dotek spoluhráče.
- **Související metriky:** Key passes / 90 — v reportech a v Advanced Search tato metrika zahrnuje i asistence.
- **Pozor na:** Historická past: ve starším endpointu v2/match/wyId/events znamenal Key Pass (tagId 302) jakoukoli akci (nejen přihrávku), která vytvořila jasnou šanci, kterou spoluhráč neproměnil — klíčové přihrávky tedy tehdy nikdy nebyly asistence. Dnes to platí naopak. Při práci se staršími daty tuhle změnu ověř.

### `Progressive pass` — Progresivní přihrávka

*podtyp Pass*

Přihrávka vpřed, která se snaží posunout tým výrazně blíž k branc soupeře.

- **Detaily a metodika:** Prahy podle umístění: minimálně 30 metrů posunu, když jsou začátek i konec ve vlastní polovině; minimálně 15 metrů, když přihrávka překračuje půlicí čáru; minimálně 10 metrů, když jsou oba body v polovině soupeře.
- **Atributy:** Successful: Yes (1801) / No (1802).
- **Související metriky:** Progressive passes / 90 · Accurate progressive passes (%)
- **Pozor na:** Tři různé prahy znamenají, že „progresivní přihrávka“ ve vlastní polovině je třikrát náročnější než v útočné. Stopeři a záložníci proto nejsou v této metrice srovnatelní bez ohledu na zónu.

### `Pass into final third` — Přihrávka do finální třetiny

*podtyp Pass*

Přihrávka, která začíná mimo finální třetinu a další dotek míče proběhne uvnitř finální třetiny.

- **Detaily a metodika:** Jen přihrávky — auty se nepočítají.
- **Atributy:** Successful: Yes (1801) / No (1802).
- **Související metriky:** Passes to final third / 90 · Passes to final third %
- **Pozor na:** Rozhoduje místo dalšího doteku, ne cíl přihrávky. Přihrávka mířená do třetiny, kterou soupeř zachytí před ní, se nepočítá.

### `Pass into penalty area` — Přihrávka do vápna

*podtyp Pass*

Přihrávka, která začíná mimo pokutové území soupeře a další dotek míče proběhne uvnitř pokutového území soupeře.

- **Detaily a metodika:** Jen přihrávky. Centry do této kategorie patří, auty a kličky ne. Kontrolované vstupy do vápna během nebo kličkou jsou vyloučené.
- **Atributy:** Successful: Yes (1801) / No (1802).
- **Související metriky:** Passes to penalty area / 90 · Passes to penalty area %
- **Pozor na:** Protože se vstupy vedením míče nepočítají, metrika podhodnocuje hráče, kteří do vápna vozí míč sami. Pro celkový obrázek ji čti spolu s Penalty area entries (týmová metrika, která běh zahrnuje).

### `Deep completion` — Hluboká dokončená přihrávka

*podtyp Pass*

Necentrovaná přihrávka mířená do zóny do 20 metrů od branky soupeře.

- **Detaily a metodika:** Centry jsou z této klasifikace vyloučené — pro ně existuje Deep completed cross.
- **Související metriky:** Deep completions passes / 90
- **Pozor na:** Zóna je definována vzdáleností od branky (20 m), ne vápnem. Zabírá tedy i prostor vedle vápna a nezabírá celý jeho vršek.

### `Deep completed cross` — Hluboký dokončený centr

*podtyp Cross*

Centr mířený do zóny do 20 metrů od branky soupeře.

- **Související metriky:** Deep completed crosses / 90
- **Pozor na:** Doplňkový k Deep completion — obě metriky se vzájemně vylučují, takže pro celkový obrázek finálních přihrávek do nebezpečné zóny je potřeba je sečíst.

### `Assist` — Asistence

*podtyp Shot assist*

Poslední akce hráče skórujícího týmu před gólem vstřeleným spoluhráčem nebo před vlastním gólem soupeře.

- **Detaily a metodika:** Protože gól je vždy střela, každá asistence je podle definice shot assist. Počet asistencí v jednom zápase je zaručeně menší nebo rovný počtu gólů.
- **Související metriky:** Assists / 90
- **Pozor na:** Čtyři vylučující podmínky: mezi poslední akcí a gólem nesmí míč kontrolovat žádný soupeř; pokud mezi poslední akcí spoluhráče a gólem střelec kličkuje nebo výrazně běží s míčem, není to asistence; způsobený faul na penaltu se za asistenci nepočítá, ani když penaltu proměnil tentýž hráč nebo spoluhráč.

### `Second assist` — Druhá asistence

*podtyp Pass*

Poslední akce hráče skórujícího týmu před asistencí spoluhráče.

- **Detaily a metodika:** Počet druhých asistencí nemůže v žádném zápase přesáhnout počet asistencí. Mezi druhou asistencí a asistencí se nesmí míče dotknout žádný soupeř. Pokud asistující hráč po přijetí míče provede smysluplnou akci (kličku nebo běh), předchozí přihrávka se za druhou asistenci nepočítá.
- **Atributy:** Successful: Yes (1801) — druhé asistence jsou vždy úspěšné.
- **Související metriky:** Second assists / 90
- **Pozor na:** Podmínka „žádná smysluplná akce mezi tím“ metriku výrazně zužuje. Nízké číslo nemusí znamenat, že hráč nezakládá akce — může znamenat, že jeho spoluhráči si míč zpracují a vezmou ho dál.

### `Third assist` — Třetí asistence

*podtyp Pass*

Poslední akce hráče skórujícího týmu před druhou asistencí spoluhráče.

- **Detaily a metodika:** Počet třetích asistencí je zaručeně menší nebo rovný počtu druhých asistencí. Mezi třetí a druhou asistencí nesmí míč kontrolovat žádný soupeř.
- **Atributy:** Successful: Yes (1801) — třetí asistence jsou vždy úspěšné.
- **Související metriky:** Third assists / 90
- **Pozor na:** Velmi malá čísla. Pro srovnávání hráčů v jedné sezóně je vzorek většinou nedostatečný.

### `Shot assist` — Přihrávka před střelou

*podtyp Pass · nadtyp pro Assist*

Poslední akce hráče před střelou spoluhráče.

- **Detaily a metodika:** Každá shot assist má zaručeně jednu (a právě jednu) odpovídající střelu. Ne každá střela je ale asistovaná.
- **Atributy:** Successful: Yes (1801) — shot assist je vždy úspěšná. xA: číslo — hodnota xG střely, kterou tato přihrávka asistovala.
- **Související metriky:** Shot assists / 90 · xA / 90 · xG + xA / 90
- **Pozor na:** Hráč nemusí mít jasný záměr asistovat — stačí, že jeho akce byla poslední před střelou. Pro jasně zamýšlené přihrávky vedoucí ke střele (ale ne ke gólu) slouží Key pass. Shot assist je tedy širší a „hloupější“ kategorie než klíčová přihrávka.

### `Fairplay` — Fair play přihrávka

*podtyp Pass*

Odkop míče, když hráč potřebuje lékařské ošetření, nebo přihrávka, kterou se míč vrací soupeři poté, co byl v duchu fair play vykopnut ze hry.

- **Detaily a metodika:** Fair play akce jsou ze statistik vyloučené — neovlivňují ani počet přihrávek a odkopů, ani přesnost přihrávek.
- **Pozor na:** Užitečné vědět při ručním dopočítávání: součet typů přihrávek nemusí sedět s celkem, protože fair play akce jsou z obojího odečtené.


## 4. Střelba a góly

*Střely, góly, vlastní góly a šance. Pozor na to, že gól je vždy střela (kromě vlastního) a že úspěšná střela znamená na branku, ne do branky.*

### `Shot` — Střela

*eventId 10 · subeventId 100*

Pokus směrem k branc soupeře se záměrem skórovat.

- **Detaily a metodika:** Zblokované střely, penalty a přímé volné kopy se také považují za střely.
- **Atributy:** Successful: Yes / No — střela je úspěšná, pokud skončí na brance (viz Zone). Střely, které trefí konstrukci branky, se za úspěšné nepovažují. Goal (tagId 101): Yes / No. Opportunity (tagId 201): Yes / No. Body part: Left foot (401) / Right foot (402) / Head or body (403) — pokud je do střely zapojeno víc částí těla, použije se poslední. Zone (tagIds 1201–1223) — střely do tyče se označují jako plt, kde p nahrazuje o odpovídajícího úhlu; střely do tyče, které skončily gólem, se označují rohem branky, kam dopadly. Zblokované střely se označují jako bc (tagId 2101). xG: číslo.
- **Související metriky:** Shots, total · Shots / 90 · Shots on target % · Shots from danger zone (x ≥ 84,29 a y mezi 36,29 a 63,71) · xG, Total · xG / 90 · Goal conversion (%)
- **Pozor na:** „Úspěšná střela“ = na branku, ne gól. Střela do tyče je neúspěšná, i když byla o centimetr od gólu — to systematicky snižuje Shots on target % hráčům, kteří střílí přesně k tyčím. Zblokovaná střela se počítá do celkových střel, takže Shots / 90 zahrnuje i pokusy, které se nikdy nedostaly ke brance.

### `Goal` — Gól

*podtyp Shot*

Gól vstřelený podle pravidla 10.1 pravidel IFAB.

- **Detaily a metodika:** V kontextu hráče nezahrnuje vlastní góly; v kontextu týmu zahrnuje vlastní góly soupeře. Zahrnuje proměněné penalty (kromě metriky Non-penalty goals). Pokud to není vlastní gól, je gól vždy střela.
- **Související metriky:** Goals · Goals / 90 · Non-penalty goals total a per 90 · Head goals total a avg per 90
- **Pozor na:** Nezahrnuje góly vstřelené po přezkoumání VARem, které vedlo k odpískání faulu nebo ofsajdu. Pro srovnávání zakončovatelů používej Non-penalty goals — penalty jinak zvýhodní určeného exekutora.

### `Own goal` — Vlastní gól

*podtyp Goal*

Gól vstřelený hráčem inkasujícího týmu.

- **Detaily a metodika:** V kontextu hráče se nezapočítává do žádné gólové metriky. V kontextu týmu se počítá do počtu gólů vstřelených soupeřem.
- **Pozor na:** Asymetrie hráč/tým je tady důležitá: součet gólů hráčů týmu se nemusí rovnat gólům týmu.

### `Shot after corner` — Střela po rohu

*podtyp Shot*

Střela týmu, která proběhne do 14 sekund po rohovém kopu přiznaném stejnému týmu.

- **Pozor na:** Okno 14 sekund je volné — zahrne i střelu po druhé nebo třetí fázi, kdy už s původním rohem nemá akce moc společného. Nečti to jako „střela z rohu“.


## 5. Duely

*Wyscout eviduje duely vždy párově: ke každému ofenzivnímu existuje defenzivní. Definice „vyhráno“ se u každého typu duelu liší.*

### `Duel` — Duel

Zápas dvou hráčů o získání kontroly nad míčem, o postup s míčem nebo o změnu jeho směru.

- **Detaily a metodika:** Duel je vždy párový event — ke každému ofenzivnímu duelu existuje defenzivní duel jiného hráče. Podtypy: Offensive duel — hráč s kontrolovaným držením míče (pod úrovní loktů) se snaží obejít soupeře, který se ho snaží připravit o míč. Defensive duel — opak ofenzivního. Loose ball duel — dva hráči soupeřících týmů s rovnou příležitostí soupeří (pod úrovní loktů) o získání míče nebo o jeho odehrání ve výhodném směru. Aerial duel — dva a více hráčů soupeří o dotek míče nad úrovní loktů (typicky hlavou). Sliding tackle — skluz.
- **Atributy:** Když o vzdušný míč soupeří víc než dva hráči, označí se samostatná sada vzdušných duelů pro každého zapojeného hráče z obou týmů. Všechny duely lze vyhrát nebo prohrát, ale definice výhry se u každého typu liší. Může se stát, že jednoho ze dvou hráčů operátor nedokáže identifikovat — pak se jednomu z párových eventů přiřadí playerId = 0.
- **Pozor na:** Hranice mezi typy je určena úrovní loktů: pod ní jde o pozemní duel, nad ní o vzdušný. To znamená, že souboj o míč v úrovni hrudi se klasifikuje jako pozemní.

### `Offensive duel` — Ofenzivní duel

*eventId 1 · subeventId 11 · podtyp Duel*

Pozemní duel hráče, který drží míč.

- **Detaily a metodika:** Když útočník použije dovednost ve snaze obejít soupeře, jde o kličku (Dribble). Když si hráč míč chrání tělem, zůstává to ofenzivní duel, ale není to klička. Ofenzivní duely mohou nastat kdekoli na hřišti, včetně vlastního pokutového území.
- **Atributy:** Successful: Yes / No — úspěch nastane, když další akce ofenzivního hráče směřuje blíž k branc soupeře; nebo když duel obsahuje kličku a následuje dotek útočícího spoluhráče blíž k branc; nebo když se defenzivní hráč dopustí faulu. Outcome: Clearly won (703) / Clearly lost (701) / Neutral (702) — jednodušší algoritmus podle toho, zda následující akci provede jeden z dueluijících hráčů. Beaten to the ball (601): jestli obránce dosáhl míče první díky lepšímu postavení.
- **Související metriky:** Offensive duels / 90 · Offensive duels %
- **Pozor na:** Dvě různé definice výsledku (Successful a Outcome) dávají různá čísla. Ujisti se, kterou používá tvůj export — „% vyhraných ofenzivních duelů“ může znamenat dvě věci.

### `Defensive duel` — Defenzivní duel

*podtyp Duel*

Situace, kdy se hráč snaží připravit soupeře o míč, aby zastavil postup útoku.

- **Detaily a metodika:** Defenzivní duel je vždy spárovaný s ofenzivním duelem hráče druhého týmu.
- **Atributy:** Successful: Yes / No — když obránce zastaví postup útočníka bez faulu, defenzivní duel je vyhraný (a spárovaný ofenzivní prohraný). Příklady: obránce připraví útočníka o míč, vykopne míč ze hry, nebo donutí útočníka jít zpět. Pokud útočník s míčem postoupí, je to prohraný defenzivní duel. Outcome: Clearly won (703) / Clearly lost (701) / Neutral (702). Anticipation (tagId 20): Yes / No — obránce se postaví tak, aby byl u míče první.
- **Související metriky:** Defensive duels / 90 minutes · Defensive duels won (%)
- **Pozor na:** Faul obránce znamená prohraný defenzivní duel. Hráč, který často taktikou faulu zastaví útok, bude mít nízké procento vyhraných duelů, přestože útok zastavil.

### `Aerial duel` — Vzdušný duel

*eventId 1 · subeventId 10 · podtyp Duel*

Situace, kdy dva nebo více hráčů soupeřících týmů vyskočí, aby se utkali o míč.

- **Detaily a metodika:** Vzdušné duely se v současnosti nedělí na ofenzivní a defenzivní. Pokud o míč soupeří víc než dva hráči zároveň, zaznamená se vzdušný duel pro všechny hráče soupeřících týmů.
- **Atributy:** Successful: Yes (703) / No (701); v beta API match_events jako first_touch. Vzdušný duel se považuje za vyhraný ve prospěch hráče, který se míče dotkne první, bez ohledu na to, co následuje. Vzdušný duel, který skončí faulem, se považuje za vyhraný ve prospěch hráče, na kterém byl faul.
- **Související metriky:** Aerial duels / 90 minutes · Aerial duels won (%)
- **Pozor na:** „Vyhraný = dotkl se první“ je velmi mechanická definice. Hráč, který se míče dotkne první, ale odehraje ho soupeři, má duel jako vyhraný. Absence dělení na ofenzivní a defenzivní znamená, že vzdušné duely stopera a útočníka jsou v jednom čísle.

### `Loose ball duel` — Duel o volný míč

*eventId 1 · subeventId 13 · podtyp Duel*

Duel o volný míč, kdy žádný tým nemá jasné držení míče.

- **Detaily a metodika:** Ani jeden zapojený hráč nemá jasnou výhodu v tom, kdo bude u míče první — jinak by se situace klasifikovala jako ofenzivní nebo defenzivní duel. Duely o volný míč soupeřících týmů jsou vždy spárované.
- **Atributy:** Sliding tackle (tagId 1601): Yes / No — ve vzácných případech může být duel o volný míč zároveň skluz.
- **Související metriky:** Loose ball duels / 90 minutes
- **Pozor na:** Klasifikace závisí na posouzení „rovné příležitosti“ operátorem, což je subjektivní hranice mezi tímto a ostatními typy duelů.

### `Sliding tackle` — Skluz

*podtyp Duel*

Agresivní skluz po zemi do nohou soupeře s jasným záměrem připravit ho o míč nebo míč odehrát ze hry.

- **Detaily a metodika:** Tvoří podkategorii duelu — konkrétně buď pozemního defenzivního duelu, nebo duelu o volný míč. Když pokus o skluz skončí faulem, dostane dvojí klasifikaci: skluz i faul.
- **Atributy:** Successful: Yes / No — určení úspěchu se řídí stejnou metodikou jako u defenzivních duelů.
- **Související metriky:** Sliding tackles / per 30 minutes of opponent possession
- **Pozor na:** Skluz se v Advanced Search nabízí primárně jako possession-adjusted metrika (na 30 minut držení soupeře), ne per 90. Míchat obě normalizace v jednom srovnání nelze.

### `Dribble` — Klička

*podtyp Offensive duel*

Pokus obejít soupeře při současné snaze udržet míč.

- **Detaily a metodika:** Hráč držící míč používá svou dovednost ve snaze obejít soupeře nebo najít volný prostor pro další akci. Když si hráč míč chrání a kryje ho tělesnou silou, není to klička, ale zůstává to ofenzivní duel.
- **Atributy:** Successful: Yes / No — klička je vyhraná, pokud další akci provede tentýž útočník blíž k branc; nebo pokud následuje dopředná přihrávka útočícího spoluhráče blíž k branc; nebo pokud skončila faulem obránce. Všechny ostatní výsledky = prohraná klička. Side: Left (502, 503) / Right (501, 504). Type: Take-on (503, 504) / Space (501, 502) — Space znamená vytvoření prostoru pro další akci, Take-on striktnější pokus obejít soupeře.
- **Související metriky:** Dribbles / 90 · Dribbles %
- **Pozor na:** Rozdělení na Take-on a Space je zásadní pro hodnocení hráčů: „úspěšnost kliček“ bez tohoto rozpadu míchá riskantní obcházení s bezpečným otevřením prostoru.

### `Dribble past` — Obejití obránce (z pohledu obránce)

*podtyp Defensive duel*

Pokus zabránit soupeři s míčem v tom, aby hráče obešel kličkou.

- **Atributy:** Successful: Yes / No — obránce vyhrává, pokud útočníka připraví o míč, vykopne míč ze hry nebo ho donutí jít zpět, a to bez faulu; jinak duel prohrává.
- **Pozor na:** Je to zrcadlo kličky z druhé strany. Nesměšuj s Defensive duel — dribble past je jeho podmnožina, konkrétně jen souboje proti kličkujícímu hráči.

### `Pressing duel` — Presinkový duel

*podtyp Non-ball · jen video, není v API*

Situace, kdy se hráč pohne, aby vyvinul tlak na soupeře, který drží míč, ale nedojde ke kontaktu s hráčem ani s míčem.

- **Detaily a metodika:** Nemůže jít o event, kde se hráč aktivně snaží získat míč — to je defenzivní duel. Nemůže jít ani o pokus zabránit kličce, což je také defenzivní duel. Pokud dojde ke kontaktu se soupeřem hned po tom, co dohrál přihrávku, označí se to jako presinkový duel.
- **Související metriky:** Pressing duels / 90
- **Pozor na:** Existuje jen ve videu, ne v API. Pokud pracuješ s event daty přes API, tato metrika ti nebude dostupná, i když ji vidíš v aplikaci.

### `Foul suffered` — Způsobený faul (obdržený)

*podtyp Offensive duel*

Přestupek spáchaný na hráči podle pravidla 12 (1, 3) pravidel IFAB.

- **Detaily a metodika:** Když hráč obdrží faul v duelu, duel se vždy považuje za vyhraný.
- **Pozor na:** Způsobený faul sice ukončí držbu, ale nepočítá se jako ztráta. To je důležité při ručním dopočítávání ztrát z držeb.


## 6. Obranné akce a přechody

*Zisky, ztráty, zachycení a odkopy. Přechody (transitions) jsou párový pojem: ztráta jednoho týmu je zisk druhého.*

### `Interception` — Zachycení míče

Akce, kdy hráč aktivně zachytí míč tím, že předvídá jeho pohyb, když soupeř střílí, přihrává nebo centruje.

- **Detaily a metodika:** Když hráč (typicky obránce) zblokuje střelu, označí se to jako zachycení.
- **Související metriky:** Interceptions / 90 minutes · Interceptions / per 30 minutes of opponent possession
- **Pozor na:** Zblokovaná střela se počítá jako zachycení, takže obránci, kteří hodně blokují, mají nadhodnocené počty zachycení. Zachycení je zároveň atributem přihrávky (tagId 1401) — jeden event tak může figurovat v obou statistikách.

### `Clearance` — Odkop

*eventId 7 · subeventId 71*

Akce (obvykle přihrávka), kdy hráč, i když má jinou možnost — přihrát nebo si míč podržet — místo toho míč odehrává: dlouhou přihrávkou vpřed bez přesného cíle, nebo na aut či na roh. Hraje na jistotu.

- **Detaily a metodika:** Ve většině případů je hráč odehrávající míč pod tlakem. Významná část odkopů jsou dlouhé dopředné přihrávky. Asi polovina odkopů je zároveň zachycení (hráč přerušuje přihrávku, aby míč odehrál).
- **Související metriky:** Clearances / 90
- **Pozor na:** Definice obsahuje záměr („i když má jinou možnost“), takže je částečně subjektivní. Vysoký počet odkopů většinou popisuje tým pod tlakem, ne kvalitu obránce.

### `Recovery` — Zisk míče

*podtyp Transition*

Jakákoli akce, která ukončí držbu soupeře (poslední akce této držby je ztráta) a začne držbu vlastního týmu.

- **Detaily a metodika:** Zisk se zaznamenává tam, kde se hráč přebírající držení dotkne míče, ne tam, kde došlo ke ztrátě. Držby začínající po zámezí nebo po faulu jsou z klasifikace zisků vyloučené. Zisky obvykle vznikají duelem (44 %) nebo zachycením (16 %), ale mohou nastat i pasivním postavením.
- **Atributy:** Zone: High / Mid / Low / Opponent Half — podle třetin hřiště (low = vlastní třetina, high = útočná třetina); opponent half zahrnuje všechny zisky v polovině soupeře. Positioning recovery: zisky dosažené bez aktivního obranného zapojení (bez defenzivního duelu, skluzu nebo zachycení).
- **Související metriky:** Recoveries / 90 · Opponent half recoveries / 90
- **Pozor na:** Zisky po zámezí a po faulu se nepočítají, takže počet zisků není počet držeb. Positioning recovery je důležitý filtr: „hodně zisků“ může znamenat jen to, že hráč stál na správném místě, když k němu míč doskákal.

### `Counterpressing recovery` — Counterpressing zisk

*podtyp Recovery*

Jakýkoli zisk, který ukončí držbu soupeře kratší než 5 sekund.

- **Pozor na:** Definice je čistě časová — neříká nic o tom, jestli tým skutečně presoval. Krátká držba soupeře ukončená náhodným odrazem se počítá stejně jako vydřený zisk po okamžitém napadení.

### `Loss` — Ztráta míče

*podtyp Transition*

Jakákoli akce, která ukončí držbu vlastního týmu.

- **Detaily a metodika:** Ztráta se zaznamenává v bodě, kde hráč skutečně přišel o míč. U jiných akcí než přihrávek je to jeho poslední akce, ale například u neúspěšné dlouhé přihrávky se ztráta zaznamená v koncovém bodě přihrávky, ne v počátečním. Eventy, kdy míč opustí hřiště od hráče, jsou podle definice ztráty. Každá neúspěšná přihrávka je ztráta. Ztráta je vždy neúspěšná akce.
- **Atributy:** Zone: High / Mid / Low / Own Half — podle třetin (low = vlastní třetina, high = finální třetina); own half zahrnuje všechny ztráty ve vlastní polovině. Leading to opponent shot: když po ztrátě následuje střela soupeře do 20 sekund.
- **Související metriky:** Losses / 90 · Own half losses / 90
- **Pozor na:** Umístění ztráty u dlouhé přihrávky je v místě dopadu, ne odkopu — to systematicky posouvá ztráty dlouhých míčů do útočné třetiny a může vytvořit dojem, že hráč ztrácí míče vysoko. Způsobený faul držbu ukončí, ale za ztrátu se nepočítá.

### `Covering teammate` — Zajištění spoluhráče

*podtyp Non-ball · jen video, není v API*

Obranný běh bez míče, kterým hráč zajišťuje zónu opuštěnou spoluhráčem.

- **Detaily a metodika:** Charakteristickým pohybem je zpětný nebo diagonální běh z běžné pozice hráče, aby zakryl prázdnou zónu. Převážně se děje ve vlastní třetině, s průměrnou vzdáleností 20 metrů od vlastní branky.
- **Pozor na:** Jen ve videu, v API není. Pro datovou analýzu je tedy nedostupné, i když se v aplikaci zobrazuje.

### `Defensive positioning` — Obranné postavení

*podtyp Non-ball · jen video, není v API*

Obranný běh hráče, kterým se vrací na svou pozici v obraně a/nebo předchází hrozícímu útočnému nebezpečí soupeře.

- **Detaily a metodika:** Chyba v postavení v obranné fázi se označí jako defensive positioning se speciálním atributem nastaveným na bad.
- **Pozor na:** Jen ve videu, v API není. Atribut „bad“ je jedna z mála přímých chybových značek v celém glosáři — hodí se pro videoanalýzu, ne pro statistiku.


## 7. Brankář

*Eventy specifické pro brankáře — zákroky, střely na branku, obdržené góly, výběhy a rozehrávky od branky.*

### `Shot against (Save attempt)` — Střela na branku (pokus o zákrok)

*eventId 9 · subeventId 91*

Střela na branku, které brankář čelí.

- **Detaily a metodika:** Brankářský event, který může skončit buď zákrokem (Save), nebo gólem (Goal conceded). Označí se, i když se brankář míče vůbec nedotkne a míč jde do sítě nebo ho vyrazí obránce.
- **Atributy:** Goal (tagId 101): Yes / No — jestli střela na branku skončila obdrženým gólem. Pokud ne, je event zákrok.
- **Související metriky:** Shots against / 90
- **Pozor na:** Zahrnuje i střely, u kterých brankář nemohl nic udělat, i míče vyražené obráncem. „Zákroky na 90“ tedy nejsou čistá míra brankářské práce — pro to je potřeba xG a post-shot xG.

### `Save` — Zákrok

*podtyp Shot against*

Úspěšný pokus brankáře zabránit tomu, aby střela skončila gólem.

- **Detaily a metodika:** Zákrok se označí u všech střel na branku, i ze střední a dlouhé vzdálenosti. Obtížné zákroky jsou v podstatě reflexivní zákroky.
- **Atributy:** xG: číslo — pre-shot xG hodnota pravděpodobnosti, že by daná střela (ne nutně na branku) skončila gólem. xCG / xG2: číslo — post-shot xG2 hodnota pravděpodobnosti, že by daná střela (zaručeně na branku) skončila gólem.
- **Pozor na:** Protože se zákrok počítá u každé střely na branku, hrubý počet zákroků měří především to, kolik toho na brankáře šlo. Pro hodnocení brankáře porovnávej obdržené góly s xCG / xG2, ne počet zákroků.

### `Reflexes save` — Reflexivní zákrok

*eventId 9 · subeventId 90 · podtyp Save*

Zákrok po střele z blízké vzdálenosti, kde brankář musí reagovat okamžitě a využívá reflexy.

- **Detaily a metodika:** Když se brankář pokusí o reflexivní zákrok, zaznamená se to jako pokus o zákrok (eventId 9, subeventId 90, tagId 201) bez ohledu na výsledek — i když míč následně skončí v branc, původní akce zůstává zaznamenaná s těmito identifikátory.
- **Pozor na:** Pozor na formulaci: „reflexivní zákrok“ v API je pokus, ne nutně úspěšný zákrok. Počítání eventů s tímto subeventId bez kontroly výsledku nadhodnotí brankářovy zákroky.

### `Goal conceded` — Obdržený gól

*podtyp Shot against*

Gól vstřelený soupeřem podle pravidla 10.1 pravidel IFAB.

- **Související metriky:** Goals conceded · Goals conceded / 90
- **Pozor na:** V kontextu hráče se vztahuje pouze na brankáře. Obdržené góly týmu a obdržené góly brankáře se mohou rozcházet, pokud v zápase nastoupili dva brankáři.

### `Goalkeeper Leaving Line` — Výběh brankáře

*eventId 4 · subeventId 40*

Pokus brankáře aktivně zahrát vysoký centr nebo dlouhou vzdušnou přihrávku ve vzduchu, ať už míč chytit nebo vyrazit.

- **Detaily a metodika:** Pokud je brankář napaden hráčem soupeře, event se klasifikuje také jako vzdušný duel.
- **Související metriky:** Exits, per 90 mins
- **Pozor na:** Zahrnuje jen aktivní zásahy do vzdušných míčů — ne výběhy proti hráči do pozemního míče. „Exits / 90“ tedy neměří celkovou odvahu brankáře opustit branku.

### `Goal Kick` — Rozehrání od branky

*eventId 3 · subeventId 34*

Rozehrání od branky podle pravidla 16 pravidel IFAB.

- **Detaily a metodika:** Pokud sudí nechá rozehrání od branky opakovat po faulu nebo jiné situaci, uvažuje se jen poslední instance. Počáteční pozice se neoznačuje — předpokládá se, že se to vždy děje ve vlastním pokutovém území. Rozehrání od branky může být krátká přihrávka i delší vzdušná přihrávka, ale podle definice nikdy nemůže být přihrávka rukou. Byť to obvykle provádí brankář, technicky to může udělat kterýkoli hráč.
- **Atributy:** Successful: Yes (1801) / No (1802) — úspěšné, pokud je další dotek míče od spoluhráče.
- **Pozor na:** Rozehrání od branky se nepočítá do statistiky přihrávek. Přesnost přihrávek brankáře tedy nezahrnuje jeho rozehrávky od branky, což je u brankářů zásadní rozdíl.


## 8. Fauly, karty a ofsajd

*Faul je vždy neúspěšná akce. Wyscout rozlišuje devět podtypů faulu podle důvodu, za který byl odpískán.*

### `Foul` — Faul

*eventId 2 · subeventId 20*

Přestupek spáchaný hráčem podle pravidla 12 (1, 3) pravidel IFAB.

- **Detaily a metodika:** Obvykle vede k přiznání volného kopu; spáchaný v pokutovém území vede k penaltě. Fauly v duelech vytvoří odpovídající „foul suffered“ pro soupeře; fauly mimo duely (například ruka) nikoli. Podtypy: Hand ball, Late card foul, Out of play foul, Penalty foul, Protest foul, Simulation foul, Time lost foul, Violent foul.
- **Atributy:** Successful: vždy neúspěšný. Card: může být žlutá (tagId 1702) nebo červená (tagIds 1701 / 1703).
- **Související metriky:** Fouls / 90
- **Pozor na:** Faul je vždy neúspěšná akce, což zkresluje agregované metriky typu „úspěšné akce“. Fauly se navíc počítají do obranných akcí v PPDA — taktický faul tedy PPDA zlepšuje.

### `Hand ball` — Ruka

*eventId 2 · subeventId 21 · podtyp Foul*

Faul odpískaný hráči v poli za dotek míče rukou v nepřirozené pozici.

- **Detaily a metodika:** Dotek rukou, který sudí vidí jako přirozenou pozici a nenásleduje faul, se za ruku nepočítá. Nedovolený dotek rukou brankářem ve vlastním pokutovém území (například po pozemní přihrávce od spoluhráče), potrestaný nepřímým volným kopem, se také označí jako ruka.
- **Atributy:** Successful: No. Card: No / žlutá (1702) / červená (1701 / 1703).

### `Late card foul` — Faul s dodatečnou kartou

*eventId 2 · subeventId 22 · podtyp Foul*

Nastane, když sudí nezapíská a nechá hru pokračovat, a až když se hra zastaví, dá kartu hráči, který faul spáchal.

- **Atributy:** Successful: No. Card: No / žlutá (1702) / červená (1701 / 1703).
- **Pozor na:** Časová značka eventu odpovídá faulu, ne momentu udělení karty — při analýze časových řad karet to může vytvořit nesoulad s televizním záznamem.

### `Out of Play Foul` — Faul mimo otevřenou hru

*eventId 2 · subeventId 23 · podtyp Foul*

Faul odpískaný mimo otevřenou hru.

- **Detaily a metodika:** Často nastává během standardních situací, kdy se dva hráči násilně přetlačují o pozici v pokutovém území a oba dostanou od sudího žlutou kartu.
- **Atributy:** Successful: No. Card: No / žlutá (1702) / červená (1701 / 1703).

### `Penalty Foul` — Faul na penaltu

*podtyp Foul*

Faul odpískaný v pokutovém území, po kterém následuje penalta.

- **Atributy:** Successful: No. Card: No / žlutá (1702) / červená (1701 / 1703).
- **Pozor na:** Způsobený faul na penaltu se nepočítá jako asistence, ani když penaltu proměnil tentýž hráč nebo spoluhráč.

### `Protest Foul` — Faul za protesty

*eventId 2 · subeventId 24 · podtyp Foul*

Faul odpískaný za hádku se sudím. Obvykle po něm následuje karta.

- **Atributy:** Successful: No. Card: No / žlutá (1702) / červená (1701 / 1703).

### `Simulation Foul` — Faul za simulování

*eventId 27 · podtyp Foul*

Faul odpískaný za pád, simulování faulu. Obvykle po něm následuje karta.

- **Detaily a metodika:** Ve většině případů se simulování děje v pokutovém území.
- **Atributy:** Successful: No. Card (attributeId 21): no (0) / žlutá (1) / červená (2).
- **Pozor na:** Používá odlišné schéma identifikátorů karet (attributeId 21 s hodnotami 0/1/2) než ostatní fauly (tagIds 1701–1703). Při parsování API na to pozor.

### `Time Lost Foul` — Faul za zdržování

*eventId 2 · subeventId 26 · podtyp Foul*

Faul odpískaný za příliš dlouhé zdržování při rozehrání. Obvykle ho doprovází karta.

- **Atributy:** Successful: No. Card: No / žlutá (1702) / červená (1701 / 1703).

### `Violent Foul` — Násilný faul

*eventId 2 · subeventId 27 · podtyp Foul*

Násilná akce, úmyslný kop nebo úder soupeře bez míče, nebo velmi špatný zákrok, kdy hráč riskuje zranění soupeře.

- **Atributy:** Successful: No — fauly jsou vždy neúspěšné.

### `Yellow card` — Žlutá karta

*podtyp Non-ball*

Disciplinární opatření sudího vyjádřené ukázáním žluté karty podle pravidla 12.3 pravidel IFAB.

- **Detaily a metodika:** Může být ukázána jen u eventu, který je faul. Zahrnuje žluté karty obdržené z jakýchkoli důvodů — nejen za fauly, ale i za nesportovní chování. Zahrnuje i karty obdržené na střídačce a karty, proti kterým bylo po zápase úspěšně odvoláno.
- **Související metriky:** Yellow cards, total · Yellow cards / 90 minutes
- **Pozor na:** V případě druhé žluté karty se žlutá označí a bude dostupná ve F24 API, ale ne ve statistikách. Součet žlutých karet ze statistik proto může být nižší než skutečnost.

### `Red card` — Červená karta

*podtyp Non-ball*

Disciplinární opatření sudího vyjádřené ukázáním červené karty podle pravidla 12.3 pravidel IFAB.

- **Detaily a metodika:** Může být ukázána jen u eventu, který je faul. Zahrnuje červené karty z jakýchkoli důvodů včetně nesportovního chování, karty obdržené na střídačce a karty, proti kterým bylo po zápase úspěšně odvoláno. Druhá žlutá karta se považuje za červenou.
- **Související metriky:** Red cards, total · Red cards / 90 minutes
- **Pozor na:** Zahrnutí zrušených karet znamená, že statistika nemusí odpovídat oficiálnímu disciplinárnímu záznamu. Přepočet červených karet na 90 minut je zavádějící — jde o téměř jednorázový jev.

### `Offside` — Ofsajd

*eventId 6 · subeventId 60*

Ofsajd podle pravidla 11 pravidel IFAB.

- **Detaily a metodika:** Označují se jen ofsajdy, které sudí odpíská a po kterých se hra rozehrává nepřímým volným kopem pro soupeře. Všechny akce mezi přihrávkou na hráče, který byl v ofsajdu, a rozhodnutím sudího se ignorují. Pokud VAR zruší sekvenci eventů kvůli ofsajdu, všechny akce v sekvenci po ofsajdu se ignorují.
- **Pozor na:** Neodpískané ofsajdové postavení se v datech vůbec neobjeví. Zároveň platí, že přihrávka hráči v ofsajdu nemůže mít hodnotu xA, i kdyby potom padl gól.


## 9. Standardní situace

*Situace, kterými se míč vrací do hry po přerušení. Většina z nich se nepočítá jako přihrávka.*

### `Set pieces` — Standardní situace

Eventy, kdy se míč vrací do otevřené hry po přerušení (po faulu nebo po zámezí).

- **Detaily a metodika:** Podtypy: rohový kop, volný kop, penalta, aut.
- **Pozor na:** Držba začínající standardkou není open play possession, takže se nepočítá do metrik otevřené hry. To má velký vliv na týmy, které staví hru na standardkách.

### `Corner kick` — Rohový kop

*eventId 3 · subeventId 30 · podtyp Set pieces*

Rohový kop rozehraný podle pravidla 17 pravidel IFAB.

- **Detaily a metodika:** Vždy nastává po zámezí. Pokud sudí rozhodne o opakování rohu po faulu nebo jiné situaci před rozehráním, označí se jen poslední instance. Roh se nepovažuje za přihrávku. Roh, po kterém následuje bezprostředně zákrok brankáře nebo přímý gól, se považuje za střelu.
- **Atributy:** Height: high (tagId 801) / low (802) — krátce rozehraný roh má vždy nízkou výšku. Scheme: Yes / No — nastaví se, pokud je roh zahraný způsobem, který vyžadoval synchronizaci pohybů více hráčů a vypadá předtrénovaně.
- **Pozor na:** Roh se nepočítá do přihrávek, takže „přesnost přihrávek“ exekutora rohů jeho rohy nezahrnuje. Atribut Scheme je jeden z mála přímých ukazatelů nacvičených situací v datech.

### `Free kick` — Volný kop

*eventId 3 · subeventId 31 · podtyp Set pieces*

Provedení volného kopu podle pravidla 13 pravidel IFAB.

- **Detaily a metodika:** Penalty ani rohové kopy do této definice nepatří.
- **Atributy:** Scheme (Yes / No) — v API zatím nedostupné. Nastaví se, pokud je volný kop zahraný způsobem vyžadujícím synchronizaci pohybů více hráčů a vypadá předtrénovaně.
- **Pozor na:** Atribut Scheme u volných kopů je zatím jen ve videu, ne v API — na rozdíl od rohů, kde dostupný je.

### `Free kick cross` — Centr ze standardky

*eventId 3 · subeventId 32 · podtyp Free kick*

Centr, který následuje po volném kopu podle pravidla 13 pravidel IFAB.

- **Detaily a metodika:** Obvykle míří do pokutového území. Centry z volných kopů se převážně zahrávají vysoko.
- **Atributy:** Height: high (801) nad úrovní pasu / low (802) pod úrovní pasu.
- **Pozor na:** Nepočítá se do statistiky centrů ani přihrávek. Hráč, který centruje výhradně ze standardek, bude mít v Crosses / 90 nulu.

### `Free kick shot` — Střela z volného kopu

*eventId 3 · subeventId 33 · podtyp Free kick*

Střela buď přímo z přímého kopu, nebo po jedné akci z nepřímého kopu, podle pravidla 13 pravidel IFAB.

- **Atributy:** Directness (tagId 1101 / 1102): direct se nastaví, když hráč střílí přímo z volného kopu, a na false, když se před střelou míče dotkne nebo ho přihraje spoluhráč. Foot (401 / 402). Goal (101). Zone (1201–1223) — střely do tyče jako plt, kde p nahrazuje o odpovídajícího úhlu; střely do tyče se skórováním se označí rohem, kam dopadly.
- **Pozor na:** Zahrnuje i střelu po jedné akci z nepřímého kopu, takže „střely z volných kopů“ nejsou jen přímé kopy. Pro přímé kopy filtruj podle Directness.

### `Penalty Kick` — Penalta

*eventId 3 · subeventId 35 · podtyp Set pieces*

Střela z penalty podle pravidla 14 pravidel IFAB.

- **Detaily a metodika:** Nezahrnuje penalty po zápase (rozstřel). Zahrnuje střely mimo, úmyslně zahozené i přihrávku místo střely.
- **Atributy:** Foot (401–402). Goal (101). Zone (1201–1223) — 23 zón branky; střely do tyče značené plt.
- **Pozor na:** xG penalty je fixně 0,76 — nezávisle na exekutorovi a brankáři. Při součtech xG to znamená, že tým s hodně penaltami má xG nadhodnocené vůči skutečné kvalitě šancí z otevřené hry.

### `Throw in` — Aut

*eventId 3 · subeventId 36 · podtyp Set pieces*

Aut zahraný podle pravidla 17 pravidel IFAB.

- **Detaily a metodika:** Nastává po zámezí, když míč přejde postranní čáru. Pokud sudí nechá aut opakovat kvůli faulu nebo jiné okolnosti, označí se jen poslední instance. Aut se neklasifikuje jako přihrávka.
- **Atributy:** Scheme: Yes / No — jestli je aut zahraný způsobem vyžadujícím synchronizaci pohybů více hráčů a vypadá předtrénovaně.
- **Pozor na:** Aut se nepočítá do přihrávek ani do přihrávek do finální třetiny a do vápna. Dlouhý aut do vápna se tedy v přihrávkových metrikách vůbec neobjeví.

### `Ball out` — Míč ze hry

*eventId 5 · subeventId 50*

Míč celým objemem přejde hranice hřiště podle pravidla 9 pravidel IFAB.

- **Detaily a metodika:** Když míč opustí hřiště přes postranní čáru, musí být nutně přiznán buď rozehrání od branky, nebo rohový kop podle toho, kdo se míče dotkl naposled. Když míč opustí hřiště přes brankovou čáru, musí být nutně přiznán aut.
- **Pozor na:** Pozor: zdrojová dokumentace má u této pasáže zaměněné pojmy touchline a byline — logicky platí, že přes postranní čáru následuje aut a přes brankovou čáru roh nebo rozehrání od branky. Text výše cituje původní znění; při implementaci se řiď pravidly hry.

### `Game interruption (Whistle)` — Přerušení hry

*eventId 5 · subeventId 51 · podtyp Non-ball*

Sudí zastavuje hru z důvodu nesouvisejícího s hrou (zranění vyžadující ošetření, kouř, fanoušci na hřišti).

- **Detaily a metodika:** Herní čas dál běží; zastavení se přidá jako nastavený čas. Když sudí zastaví hru během aktivní hry, pokračuje se rozehráním sporného míče; pokud byl míč už mimo hru, pokračuje se normálně.
- **Pozor na:** Tento event je jeden z mála způsobů, jak v datech najít delší přerušení. Do čistého času držení míče se nepočítá ani jednomu týmu.


## 10. Pohyb, běhy a doteky

*Akce s míčem i bez míče: akcelerace, progresivní běhy, náběhy do prostoru, doteky. Část z nich existuje jen ve videu, ne v API.*

### `Acceleration` — Akcelerace

*eventId 7 · subeventId 70*

Běh s míčem s výrazným zrychlením.

- **Detaily a metodika:** Akcelerace se označují jen u smysluplných běhů, dlouhých aspoň 10 metrů. Hráč se musí dotknout míče — jinak by smysluplný běh do otevřeného prostoru byl off the ball move. Asi polovina akcelerací jsou zároveň progresivní běhy.
- **Související metriky:** Accelerations / 90
- **Pozor na:** Nezaměňovat s fyzickou metrikou akcelerace (m/s²) z Advanced Search — tohle je event z videoanalýzy, nikoli měření zrychlení. Podmínka doteku míče znamená, že akcelerace bez míče se sem nepočítají.

### `Progressive run` — Progresivní běh

Nepřerušená kontrola míče jedním hráčem se snahou dostat tým výrazně blíž k branc soupeře.

- **Detaily a metodika:** Prahy: aspoň 30 metrů blíž, když jsou počáteční i koncový bod ve vlastní polovině; aspoň 15 metrů, když body překračují půlicí čáru; aspoň 10 metrů, když jsou oba body v polovině soupeře.
- **Související metriky:** Progressive runs / 90
- **Pozor na:** Stejné prahy jako u progresivní přihrávky, takže obě metriky jsou srovnatelné. Pozor ale na chybu v oficiálním katalogu metrik: definice u Progressive runs / 90 tam omylem uvádí „number of progressive passes“ — jde o překlep, metrika počítá běhy.

### `Off the ball movement` — Náběh bez míče

*podtyp Non-ball · jen video, není v API*

Výrazný pohyb bez míče do prázdného prostoru.

- **Detaily a metodika:** Hráč by měl aktivně hledat volný prostor v útoku a svým pohybem ukazovat, že je připraven přijmout míč. Často, ale ne výhradně, se to děje při brejcích. Hráč nemusí míč nakonec dostat, ale je to možné.
- **Pozor na:** Jen ve videu, v API není. Toto je nejbližší ekvivalent SkillCorner off-ball runs, ale je nesrovnatelně méně strukturovaný — bez typů náběhů, bez threat hodnoty a bez informace, zda byl hráč přihrávkovou možností.

### `Touch` — Dotek

*eventId 7 · subeventId 72*

Dotek míče, když hráč neprovádí přihrávku ani jinou jasně identifikovatelnou akci.

- **Detaily a metodika:** Doteky mohou být záměrné i nezáměrné, včetně tečí a vlastních gólů. Zaznamenávají se, když hráč kontroluje míč na významnou vzdálenost, aniž by provedl jinou definovanou akci. Označují se také, když hráč překročí hranici pokutového území nebo půlicí čáru a když přihrávka změní směr (dozadu nebo dopředu).
- **Atributy:** Missed: No / Missed (tagId 1302) / Dummy (tagId 1301) — neúspěšné pokusy o dotek dostanou označení missed. Dummy se použije, když se hráč doteku úmyslně vyhne, ať aby míč nechal spoluhráči, nebo aby oklamal obránce.
- **Pozor na:** Je to zbytková kategorie („nic jiného to není“), takže její obsah je heterogenní. Nepoužívej počet doteků jako míru zapojení do hry.

### `Missed ball` — Minutý míč

*podtyp Touch*

Typ doteku, kdy se hráč snaží míč zpracovat, ale nedosáhne ho.

- **Detaily a metodika:** Minuté skluzy se také označují jako minuté míče.
- **Související metriky:** Missed balls / 90 minutes
- **Pozor na:** Minutý míč nepřeruší držbu — akce soupeře, které netvoří smysluplné držení, včetně minutých míčů, držbu neukončí. Do ztrát se tedy nepočítá.

### `Touch in box` — Dotek ve vápně

Akce (přihrávka nebo dotek), která se děje v pokutovém území soupeře. Duely jsou z definice vyloučené.

- **Detaily a metodika:** Dva doteky ve vápně v jednom útoku se počítají jako dvě samostatné akce.
- **Související metriky:** Touches in box, per 90
- **Pozor na:** Vyloučení duelů je zásadní: žádné pozemní ani vzdušné duely a žádné fauly se za dotek ve vápně nepočítají. Útočník, který ve vápně hlavně bojuje o míče, bude mít nízké číslo.

### `Link-up Play` — Napojení hry

Akce útočícího hráče, který přijímá míč od obránce nebo záložníka zády k branc soupeře.

- **Detaily a metodika:** Obvykle končí ofenzivním duelem nebo zpětnou přihrávkou.
- **Pozor na:** Je to atribut přihrávky (Link-up play u Pass a Smart pass), ne samostatný počitatelný event s vlastní metrikou per 90. Vyhodnocuje se z pohledu přijímajícího hráče, ale příznak nese přihrávka.

### `Non-ball` — Event bez míče

Eventy, které nevyžadují dotek míče.

- **Detaily a metodika:** Podtypy: zajištění spoluhráče, obranné postavení, přerušení hry, náběh bez míče, presinkový duel, červená karta, žlutá karta.
- **Pozor na:** Většina non-ball eventů (kromě karet a přerušení) existuje jen ve videu, ne v API. Kdo pracuje výhradně s API, o celou tuto vrstvu přichází.


## 11. Modely a odvozené metriky

*Metriky, které nejsou spočítané z jednoho eventu, ale z modelu nebo z agregace: xG, xA, PPDA, Wyscout Index, ball progression, challenge intensity.*

### `Expected goals (xG)` — Očekávané góly

*xG*

Prediktivní model strojového učení, který hodnotí pravděpodobnost skórování u každé střely v zápase.

- **Detaily a metodika:** Vstupy modelu: pozice střely; pozice asistence; noha nebo hlava; typ asistence; jestli střele bezprostředně předcházela klička hráče v poli nebo brankáře; jestli akce vznikla ze standardky; jestli šlo o brejk nebo přechodovou fázi; hodnocení nebezpečnosti střely od taggera; a další technické parametry. Pravděpodobnosti jsou mezi 0 a 1 — střela s xG 0,1 by měla skončit gólem v 10 % případů, střela s 0,8 v 80 %. xG penalty je fixně 0,76.
- **Atributy:** Post-shot xG (PSxG / xCG / xG2): pre-shot xG se trénuje na všech střelách včetně zblokovaných a mimo, a hodnotí se v momentě střely. Post-shot xG se trénuje jen na střelách na branku (zblokované a mimo mají automaticky 0) a zahrnuje souřadnice místa v branc. Post-shot xG je u dané střely obvykle vyšší než pre-shot a může odrážet zakončovatelskou kvalitu. Je zvlášť cenný pro hodnocení vlivu brankáře na obdržené góly.
- **Pozor na:** Pro střely v téže držbě zatím neexistuje žádné dodatečné omezení, takže sekvence střel v rychlém sledu — třeba dorážka po zákroku — může teoreticky dát součet xG větší než 1. Při součtech xG za držbu s tím počítej.

### `xA` — Očekávané asistence

*xA*

Hodnota expected assist (xA) přihrávky je hodnota expected goals (xG) střely, ke které tato přihrávka vedla.

- **Detaily a metodika:** Aby přihrávka měla hodnotu xA, musí být klasifikovaná jako shot assist. Platí pro běžné přihrávky, centry, rozehrání rohů, auty a přihrávky ze standardek, po kterých následuje střela.
- **Pozor na:** Vyloučeno je: způsobené fauly vedoucí k penaltě nebo přímému kopu (góly z nich se nepočítají jako asistované), přihrávky hráče v ofsajdové pozici (nemohou mít xA, i kdyby potom padl gól), góly zrušené VARem a jakékoli akce po faulu nebo ofsajdu identifikovaném VARem. xA tedy není „xG všech mých finálních přihrávek“ — je to xG střel, které z nich vznikly.

### `PPDA` — Přihrávky na obrannou akci

*PPDA*

Metrika kvantifikující intenzitu vysokého presinku, kterou zavedl Colin Trainor v roce 2014. Počítá se jen z eventů v posledních 60 % hřiště.

- **Detaily a metodika:** PPDA = počet přihrávek soupeře v této zóně dělený součtem obranných akcí presujícího týmu ve stejné zóně. Do obranných akcí se počítají: fauly, zachycení míče, vyhrané defenzivní duely a skluzy. Příklad Liverpool–Manchester United, 20. 10. 2019: United v zóně dokončil 207 přihrávek, Liverpool měl 10 faulů + 16 zachycení + 11 vyhraných duelů + 3 skluzy = 40 akcí, tedy PPDA = 207 / 40 = 5,2.
- **Pozor na:** Nižší hodnota znamená intenzivnější presink — obráceně než u většiny metrik, což se v grafech snadno splete. Průměr v top pěti evropských ligách 2018/19 byl 11,01; nejlepší tým Eibar 6,72. Metrika nic neříká o tom, jak vysoko na hřišti presink začíná, jen jak je hustý v dané zóně.

### `Challenge intensity` — Intenzita zápasů o míč

Týmová metrika kvantifikující, kolik obranných akcí (defenzivní duely, duely o volný míč, zachycení, skluzy) tým dělá na minutu držení míče soupeře.

- **Detaily a metodika:** Odráží, jak často se tým aktivně snaží získat míč, když ho drží soupeř — proto koreluje s PPDA. Čím vyšší číslo, tím intenzivnější tým v zápasech o míč. V top pěti evropských ligách 2018/19 byl průměr 6,04, nejlepší Eibar se 7,7; Parma, Nürnberg a Angers nejméně (5).
- **Pozor na:** Na rozdíl od PPDA je tady vyšší hodnota lepší ve smyslu aktivity. Obě metriky měří podobnou věc obrácenou logikou — nepoužívej je v jednom grafu bez upozornění.

### `Ball progression` — Posun míče vpřed

*v metrech*

Metrika kvantifikující, o kolik metrů hráč posouvá míč vpřed.

- **Detaily a metodika:** U každé úspěšné přihrávky vpřed Wyscout spočítá, o kolik se přihrávka přiblížila k branc soupeře. Například přihrávka ze středu hřiště, která úspěšně dorazila na hranici vápna, posunula míč vpřed o 36 metrů. Stejná logika platí pro běhy, tedy úspěšné vedení míče na vzdálenost tímtéž hráčem: rozdíl mezi vzdáleností počátku běhu od branky soupeře a vzdáleností konce běhu se uloží jako progrese běhu.
- **Pozor na:** Počítají se jen úspěšné přihrávky a běhy vpřed, takže metrika je vždy nula nebo víc. Neúspěšná riskantní přihrávka se neodečte — metrika tedy neměří čistý přínos, ale jen kladnou složku.

### `Wyscout Index` — Wyscout Index

Index dostupný v aplikaci Rankings, který v rámci soutěže řadí hráče pro každou pozici podle jejich statistik.

- **Detaily a metodika:** Každé statistice je přiřazena váha, kladná nebo záporná. Algoritmus z toho spočítá rozdělení v rámci sezóny a přiřadí hodnoty lineárně podle minima a maxima v lize. Index je součet statistických parametrů vynásobených vahami. Aktualizuje se po každém odehraném zápase. Parametry se liší podle pozice — například brankář: obdržené góly, gólové chyby, zákroky, čelené střely, chycené penalty, výběhy, přesnost přihrávek; střední obránce: obdržené góly týmu, vyhrané defenzivní duely, vyhrané duely o volný míč, zachycení, odkopy, vyhrané vzdušné duely, skluzy, ztracené míče, zblokované střely, karty, přesnost přihrávek; útočník: góly, vytvořené šance, průnikové přihrávky, asistence, střely, vyhrané kličky, střely na branku, vyhrané duely, centry, link-up plays.
- **Pozor na:** Protože se hodnoty přiřazují lineárně podle minima a maxima v dané lize a sezóně, index není srovnatelný mezi ligami ani mezi sezónami. Váhy Wyscout nezveřejňuje, takže index nelze rekonstruovat ani auditovat.

### `Opportunity` — Gólová šance

Jasná příležitost ke skórování.

- **Detaily a metodika:** Označuje se převážně u střely — znamená tedy nebezpečnou střelu. V event feed API označuje tagId 201 gólovou šanci, která neskončila gólem.
- **Pozor na:** Je to hodnocení taggera, ne výstup modelu. Zároveň vstupuje jako příznak do xG modelu, takže mezi „opportunity“ a xG je závislost — nepoužívej je jako dvě nezávislá potvrzení téhož.


## 12. Katalog — fyzické metriky

*Kompletní seznam fyzických metrik z Advanced Search. Dostupné jen pro vybrané soutěže a pro hráče s aspoň 60 minutami aktivní hry napříč všemi zápasy.*

### `Count HI per 90` — Počet vysokointenzivních akcí na 90 min

*počet/90*

Počet vysokointenzivních akcí: součet Count HSR (běhy ve vysoké rychlosti) a Count Sprint, v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Count HSR per 90` — Počet běhů ve vysoké rychlosti na 90 min

*počet/90*

Počet běhů ve vysoké rychlosti detekovaných mezi 20 a 25 km/h, v přepočtu na 90 minut. Akce musí trvat aspoň 1 sekundu.

- **Detaily a metodika:** Produkt: Advanced Search

### `Count Sprint per 90` — Počet sprintů na 90 min

*počet/90*

Počet sprintů překračujících 25 km/h, v přepočtu na 90 minut. Akce musí trvat aspoň 1 sekundu.

- **Detaily a metodika:** Produkt: Advanced Search

### `Count High Acceleration per 90` — Počet vysokých akcelerací na 90 min

*počet/90*

Počet akcelerací s vrcholovou hodnotou vyšší než 3 m/s², v přepočtu na 90 minut. Akce musí trvat aspoň 1 sekundu.

- **Detaily a metodika:** Produkt: Advanced Search

### `Count Medium Acceleration per 90` — Počet středních akcelerací na 90 min

*počet/90*

Počet akcelerací s vrcholovou hodnotou mezi 1,5 a 3 m/s², v přepočtu na 90 minut. Akce musí trvat aspoň 1 sekundu.

- **Detaily a metodika:** Produkt: Advanced Search

### `Count High Deceleration per 90` — Počet vysokých decelerací na 90 min

*počet/90*

Počet decelerací s vrcholovou hodnotou nižší než −3 m/s², v přepočtu na 90 minut. Akce musí trvat aspoň 1 sekundu.

- **Detaily a metodika:** Produkt: Advanced Search

### `Count Medium Deceleration per 90` — Počet středních decelerací na 90 min

*počet/90*

Počet decelerací s vrcholovou hodnotou mezi −1,5 a −3 m/s², v přepočtu na 90 minut. Akce musí trvat aspoň 1 sekundu.

- **Detaily a metodika:** Produkt: Advanced Search

### `HI Distance per 90` — Vysokointenzivní vzdálenost na 90 min

*m/90*

Vzdálenost naběhaná nad 20 km/h, v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `HSR Distance per 90` — Vzdálenost ve vysoké rychlosti na 90 min

*m/90*

Vzdálenost naběhaná mezi 20 a 25 km/h, v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Running Distance per 90` — Běžecká vzdálenost na 90 min

*m/90*

Vzdálenost naběhaná mezi 15 a 20 km/h, v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Sprinting Distance per 90` — Sprintová vzdálenost na 90 min

*m/90*

Vzdálenost naběhaná nad 25 km/h, v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Total Distance per 90` — Celková vzdálenost na 90 min

*m/90*

Celková naběhaná vzdálenost, v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Meter/min` — Metry za minutu

*m/min*

Celková vzdálenost naběhaná napříč všemi akcemi, dělená počtem minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Max Speed (km/h)` — Maximální rychlost

*km/h*

Nejvyšší zaznamenaná rychlost.

- **Detaily a metodika:** Produkt: Advanced Search


## 13. Katalog — hráčské metriky

*Kompletní seznam hráčských metrik, převážně z Advanced Search. Toto jsou názvy sloupců, se kterými se pracuje v exportech.*

### `Accelerations / 90` — Akcelerace na 90 min

*počet/90*

Počet akcelerací v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Aerial duels / 90 minutes` — Vzdušné duely na 90 min

*počet/90*

Počet vzdušných duelů v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Aerial duels won (%)` — Úspěšnost vzdušných duelů

*%*

Procento vyhraných vzdušných duelů.

- **Detaily a metodika:** Produkt: Advanced Search

### `Accurate long passes (%)` — Přesnost dlouhých přihrávek

*%*

Procento úspěšných dlouhých přihrávek.

- **Detaily a metodika:** Produkt: Advanced Search

### `Accurate progressive passes (%)` — Přesnost progresivních přihrávek

*%*

Procento úspěšných progresivních přihrávek.

- **Detaily a metodika:** Produkt: Advanced Search

### `Accurate smart passes (%)` — Přesnost kreativních průnikovek

*%*

Procento úspěšných smart passes.

- **Detaily a metodika:** Produkt: Advanced Search

### `Accurate through passes (%)` — Přesnost průnikových přihrávek

*%*

Procento úspěšných průnikových přihrávek.

- **Detaily a metodika:** Produkt: Advanced Search

### `Assists / 90` — Asistence na 90 min

*počet/90*

Počet asistencí v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Clearances / 90` — Odkopy na 90 min

*počet/90*

Počet odkopů v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Cross accuracy` — Přesnost centrů

*%*

Procento úspěšných centrů.

- **Detaily a metodika:** Produkt: Advanced Search

### `Cross accuracy from left flank (%)` — Přesnost centrů z levého křídla

*%*

Procento úspěšných centrů z levého křídla (nejlevějších 23 metrů).

- **Detaily a metodika:** Produkt: Advanced Search

### `Cross accuracy from right flank (%)` — Přesnost centrů z pravého křídla

*%*

Procento úspěšných centrů z pravého křídla (nejpravějších 23 metrů).

- **Detaily a metodika:** Produkt: Advanced Search

### `Cross accuracy to six-yard box (%)` — Přesnost centrů do malého vápna

*%*

Procento úspěšných centrů, po kterých následuje dotek uvnitř malého vápna.

- **Detaily a metodika:** Produkt: Advanced Search

### `Crosses / 90` — Centry na 90 min

*počet/90*

Počet pokusů o centr v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Crosses from left flank, per 90` — Centry z levého křídla na 90 min

*počet/90*

Počet pokusů o centr z levého křídla (nejlevějších 23 metrů) v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Crosses from right flank, per 90` — Centry z pravého křídla na 90 min

*počet/90*

Počet pokusů o centr z pravého křídla (nejpravějších 23 metrů) v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Crosses to six-yard box, per 90 mins` — Centry do malého vápna na 90 min

*počet/90*

Počet pokusů o centr s dalším dotekem uvnitř malého vápna, v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Deep completed crosses / 90` — Hluboké dokončené centry na 90 min

*počet/90*

Počet hlubokých dokončených centrů na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Deep completions passes / 90` — Hluboké dokončené přihrávky na 90 min

*počet/90*

Počet hlubokých dokončených přihrávek na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Defensive duels / 90 minutes` — Defenzivní duely na 90 min

*počet/90*

Počet defenzivních duelů v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Defensive duels won (%)` — Úspěšnost defenzivních duelů

*%*

Procento vyhraných defenzivních duelů.

- **Detaily a metodika:** Produkt: Advanced Search

### `Dribbles / 90` — Kličky na 90 min

*počet/90*

Počet pokusů o kličku v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Dribbles %` — Úspěšnost kliček

*%*

Procento úspěšných kliček.

- **Detaily a metodika:** Produkt: Advanced Search

### `Exits, per 90 mins` — Výběhy na 90 min

*počet/90*

Počet výběhů brankáře v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Fouls / 90` — Fauly na 90 min

*počet/90*

Počet faulů v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Goal conversion (%)` — Úspěšnost zakončení

*%*

Procento střel, které skončily gólem.

- **Detaily a metodika:** Produkt: Advanced Search

### `Goals` — Góly

*počet*

Celkový počet vstřelených gólů.

- **Detaily a metodika:** Produkt: Advanced Search

### `Goals / 90` — Góly na 90 min

*počet/90*

Počet gólů v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Head goals, avg per 90 mins` — Hlavičkové góly na 90 min

*počet/90*

Celkový počet gólů hlavou v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Head goals, total` — Hlavičkové góly celkem

*počet*

Celkový počet gólů hlavou.

- **Detaily a metodika:** Produkt: Advanced Search

### `Interceptions / 90 minutes` — Zachycení na 90 min

*počet/90*

Počet zachycení míče v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Interceptions / per 30 minutes of opponent possession` — Zachycení na 30 min držení soupeře

*počet/30 min*

Počet zachycení míče upravený na 30 minut držení míče soupeřem.

- **Detaily a metodika:** Produkt: Advanced Search

### `Key passes / 90` — Klíčové přihrávky na 90 min

*počet/90*

Počet klíčových přihrávek v přepočtu na 90 minut. Pozor: v reportech a v Advanced Search tato metrika zahrnuje i vstřelené asistence.

- **Detaily a metodika:** Produkt: Advanced Search

### `Long passes / 90 minutes` — Dlouhé přihrávky na 90 min

*počet/90*

Počet dlouhých přihrávek v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Loose ball duels / 90 minutes` — Duely o volný míč na 90 min

*počet/90*

Počet duelů o volný míč v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Loss index` — Index ztrát

*index*

Počet ztrát míče hráče dělený úspěšnými akcemi v útoku (střely na branku, přesné centry a úspěšné kličky).

- **Detaily a metodika:** Produkt: Player Lists

### `Losses / 90` — Ztráty na 90 min

*počet/90*

Počet ztrát míče na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Missed balls / 90 minutes` — Minuté míče na 90 min

*počet/90*

Počet minutých míčů v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Non-penalty goals, per 90 mins` — Góly bez penalt na 90 min

*počet/90*

Celkový počet gólů kromě penalt, v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Non-penalty goals, total` — Góly bez penalt celkem

*počet*

Celkový počet gólů kromě penalt.

- **Detaily a metodika:** Produkt: Advanced Search

### `Offensive Duels / 90` — Ofenzivní duely na 90 min

*počet/90*

Počet ofenzivních duelů v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Offensive Duels %` — Úspěšnost ofenzivních duelů

*%*

Procento úspěšných ofenzivních duelů.

- **Detaily a metodika:** Produkt: Advanced Search

### `Opponent half recoveries / 90` — Zisky v polovině soupeře na 90 min

*počet/90*

Počet zisků míče v polovině soupeře v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Own half losses / 90` — Ztráty ve vlastní polovině na 90 min

*počet/90*

Počet ztrát ve vlastní polovině v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Pass accuracy` — Přesnost přihrávek

*%*

Procento úspěšných přihrávek.

- **Detaily a metodika:** Produkt: Advanced Search

### `Passes / 90` — Přihrávky na 90 min

*počet/90*

Počet přihrávek v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Passes to final third / 90` — Přihrávky do finální třetiny na 90 min

*počet/90*

Počet přihrávek do finální třetiny v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Passes to final third %` — Přesnost přihrávek do finální třetiny

*%*

Procento úspěšných přihrávek do finální třetiny.

- **Detaily a metodika:** Produkt: Advanced Search

### `Passes to penalty area / 90` — Přihrávky do vápna na 90 min

*počet/90*

Počet přihrávek do pokutového území v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Passes to penalty area %` — Přesnost přihrávek do vápna

*%*

Procento úspěšných přihrávek do pokutového území.

- **Detaily a metodika:** Produkt: Advanced Search

### `Pressing duels, per 90` — Presinkové duely na 90 min

*počet/90*

Počet presinkových duelů normalizovaný na 90 minut na hřišti.

- **Detaily a metodika:** Produkt: Advanced Search

### `Progressive passes / 90` — Progresivní přihrávky na 90 min

*počet/90*

Počet progresivních přihrávek v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Progressive passes allowed` — Umožněné progresivní přihrávky

*počet*

Počet progresivních přihrávek soupeře v zóně hráče (například defenzivní levé křídlo u levého obránce).

- **Detaily a metodika:** Produkt: Rankings

### `Progressive runs / 90` — Progresivní běhy na 90 min

*počet/90*

Počet progresivních běhů v přepočtu na 90 minut. (V originálním katalogu je u této metriky překlep — uvádí „progressive passes“.)

- **Detaily a metodika:** Produkt: Advanced Search

### `Recoveries / 90` — Zisky na 90 min

*počet/90*

Počet zisků míče v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Red cards / 90 minutes` — Červené karty na 90 min

*počet/90*

Počet červených karet v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Red cards, total` — Červené karty celkem

*počet*

Celkový počet červených karet v časovém rámci.

- **Detaily a metodika:** Produkt: Advanced Search

### `Second assists / 90` — Druhé asistence na 90 min

*počet/90*

Počet druhých asistencí v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Short/medium passes / 90` — Krátké a střední přihrávky na 90 min

*počet/90*

Počet krátkých a středně dlouhých přihrávek v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Short/medium passes %` — Přesnost krátkých a středních přihrávek

*%*

Přesnost krátkých a středně dlouhých přihrávek.

- **Detaily a metodika:** Produkt: Advanced Search

### `Shot assists / 90` — Přihrávky před střelou na 90 min

*počet/90*

Počet shot assists v přepočtu na 90 minut. (V originálním katalogu je u této metriky překlep — uvádí „number of dribbles“.)

- **Detaily a metodika:** Produkt: Advanced Search

### `Shots / 90` — Střely na 90 min

*počet/90*

Počet střel v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Shots against / 90` — Střely na branku na 90 min

*počet/90*

Počet střel na branku brankáře normalizovaný na 90 minut na hřišti.

- **Detaily a metodika:** Produkt: Advanced Search

### `Shots on target %` — Podíl střel na branku

*%*

Procento střel, které míří na branku.

- **Detaily a metodika:** Produkt: Advanced Search

### `Shots, total` — Střely celkem

*počet*

Počet všech střel v časovém rámci.

- **Detaily a metodika:** Produkt: Advanced Search

### `Sliding tackles / per 30 minutes of opponent possession` — Skluzy na 30 min držení soupeře

*počet/30 min*

Počet skluzů upravený na 30 minut držení míče soupeřem.

- **Detaily a metodika:** Produkt: Advanced Search

### `Smart passes / 90` — Kreativní průnikovky na 90 min

*počet/90*

Počet smart passes v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Successful attacking actions / 90` — Úspěšné útočné akce na 90 min

*počet/90*

Součet střel na branku, přesných centrů a úspěšných kliček v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Successful defensive actions / 90` — Úspěšné obranné akce na 90 min

*počet/90*

Součet vyhraných defenzivních duelů, zachycení a skluzů v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Third assists / 90` — Třetí asistence na 90 min

*počet/90*

Počet třetích asistencí v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Through passes / 90` — Průnikové přihrávky na 90 min

*počet/90*

Počet průnikových přihrávek v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Touches in box, per 90` — Doteky ve vápně na 90 min

*počet/90*

Počet doteků v pokutovém území normalizovaný na 90 minut na hřišti.

- **Detaily a metodika:** Produkt: Advanced Search

### `xA / 90` — xA na 90 min

*xA/90*

Součet hodnot xA všech shot assists v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `xG / 90` — xG na 90 min

*xG/90*

Součet hodnot xG všech střel v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `xG + xA / 90` — xG + xA na 90 min

*/90*

Součet hodnot xG všech střel a hodnot xA všech shot assists v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `xG, Total` — xG celkem

*xG*

Součet hodnot xG všech střel v časovém rámci.

- **Detaily a metodika:** Produkt: Advanced Search

### `Yellow cards / 90 minutes` — Žluté karty na 90 min

*počet/90*

Počet žlutých karet v přepočtu na 90 minut.

- **Detaily a metodika:** Produkt: Advanced Search

### `Yellow cards, total` — Žluté karty celkem

*počet*

Celkový počet žlutých karet v časovém rámci.

- **Detaily a metodika:** Produkt: Advanced Search


## 14. Katalog — zápasové a týmové metriky

*Kompletní seznam metrik na úrovni zápasu, týmu a hráče z Match reportu, Player Stats a Team Stats.*

### `Actions` — Akce

*počet*

Celkový počet akcí.

- **Detaily a metodika:** Produkt: Match report, Player Stats

### `Actions / successful` — Úspěšné akce

*počet*

Celkový počet úspěšných akcí. K dispozici i jako procento.

- **Detaily a metodika:** Produkt: Match report, Player Stats

### `Aerial duels` — Vzdušné duely

*počet*

Celkový počet vzdušných duelů.

- **Detaily a metodika:** Produkt: Match report, Player Stats, Team Stats

### `Aerial duels won` — Vyhrané vzdušné duely

*počet*

Celkový počet vyhraných vzdušných duelů. K dispozici i jako procento.

- **Detaily a metodika:** Produkt: Match report, Player Stats, Team Stats

### `Assists` — Asistence

*počet*

Celkový počet asistencí.

- **Detaily a metodika:** Produkt: Match report, Player Stats

### `Attacks` — Útoky

*počet*

Celkový počet držeb, které mají aspoň jednu úspěšnou akci ve finální třetině.

- **Detaily a metodika:** Produkt: Match report

### `Attacks per minute` — Útoky za minutu

*počet/min*

Počet útoků z otevřené hry na minutu hry.

- **Detaily a metodika:** Produkt: Match report

### `Attacks with shots` — Útoky se střelou

*počet*

Počet útoků obsahujících střelu. K dispozici i jako procento.

- **Detaily a metodika:** Produkt: Match report

### `Average formation line` — Průměrná linie rozestavení

*m*

Průměrná pozice na ose od vlastní branky k branc soupeře u všech eventů týmu s míčem.

- **Detaily a metodika:** Produkt: Match report

### `Average pass length` — Průměrná délka přihrávky

*m*

Průměrná délka přihrávek.

- **Detaily a metodika:** Produkt: Match report, Team Stats

### `Average passes per possession` — Průměr přihrávek na držbu

*počet*

Průměrný počet přihrávek v držbě z otevřené hry.

- **Detaily a metodika:** Produkt: Team Stats

### `Average possession duration` — Průměrná délka držby

*s*

Průměrná délka držby z otevřené hry.

- **Detaily a metodika:** Produkt: Match report

### `Average shot distance` — Průměrná vzdálenost střely

*m*

Průměrná vzdálenost na ose od vlastní branky k branc soupeře u všech střel týmu.

- **Detaily a metodika:** Produkt: Match report, Team Stats

### `Back passes` — Zpětné přihrávky

*počet*

Celkový počet přihrávek v 90° výseči otočené o 45° směrem dozadu.

- **Detaily a metodika:** Produkt: Match report, Player Stats, Team Stats

### `Back passes / accurate` — Přesné zpětné přihrávky

*počet*

Celkový počet přesných zpětných přihrávek. K dispozici i jako procento.

- **Detaily a metodika:** Produkt: Match report, Player Stats, Team Stats

### `Back passes to GK` — Zpětné přihrávky na brankáře

*počet*

Celkový počet zpětných přihrávek, kde je příjemcem vlastní brankář.

- **Detaily a metodika:** Produkt: Match report

### `Ball distributions` — Rozehrávky

*počet*

Celkový počet rozehrání od branky.

- **Detaily a metodika:** Produkt: Player Stats

### `Ball possession (%)` — Držení míče

*%*

Procento držení míče. Metodika viz pojem Držení míče.

- **Detaily a metodika:** Produkt: Match report, Team Stats

### `Challenge intensity` — Intenzita zápasů o míč

*počet/min*

Počet obranných akcí (defenzivní duely, duely o volný míč, zachycení, skluzy) na minutu držení míče soupeře.

- **Detaily a metodika:** Produkt: Match report

### `Clearances` — Odkopy

*počet*

Celkový počet odkopů.

- **Detaily a metodika:** Produkt: Match report, Player Stats, Team Stats

### `Conceded penalty goals` — Obdržené góly z penalt

*počet*

Celkový počet gólů obdržených z penalty. Platí pro brankáře.

- **Detaily a metodika:** Produkt: Match report

### `Corners` — Rohy

*počet*

Celkový počet zahraných rohových kopů.

- **Detaily a metodika:** Produkt: Match report, Team Stats

### `Corners with shots` — Rohy se střelou

*počet*

Celkový počet rohů, které vedly ke střele týmu zahrávajícího roh do 14 sekund. K dispozici i jako procento.

- **Detaily a metodika:** Produkt: Match report, Team Stats

### `Counterattacks` — Brejky

*počet*

Celkový počet brejků.

- **Detaily a metodika:** Produkt: Match report, Team Stats

### `Counterattacks with shots` — Brejky se střelou

*počet*

Celkový počet brejků, ve kterých držba obsahovala střelu. K dispozici i jako procento.

- **Detaily a metodika:** Produkt: Team Stats

### `Crosses` — Centry

*počet*

Celkový počet centrů.

- **Detaily a metodika:** Produkt: Match report, Player Stats, Team Stats

### `Crosses / accurate` — Přesné centry

*počet*

Celkový počet přesných centrů. K dispozici i jako procento.

- **Detaily a metodika:** Produkt: Match report, Player Stats, Team Stats

### `Crosses / blocked` — Zblokované centry

*počet*

Celkový počet centrů, které byly zblokovány.

- **Detaily a metodika:** Produkt: Match report

### `Crosses / high` — Vysoké centry

*počet*

Celkový počet centrů nad úrovní pasu.

- **Detaily a metodika:** Produkt: Match report

### `Crosses / low` — Nízké centry

*počet*

Celkový počet centrů pod úrovní pasu.

- **Detaily a metodika:** Produkt: Match report

### `Dead time` — Mrtvý čas

*s*

Čas, kdy míč nedržel ani jeden z týmů.

- **Detaily a metodika:** Produkt: Match report

### `Deep completions` — Hluboké dokončené přihrávky

*počet*

Celkový počet hlubokých dokončených přihrávek.

- **Detaily a metodika:** Produkt: Match report, Team Stats

### `Deep completed crosses` — Hluboké dokončené centry

*počet*

Celkový počet hlubokých dokončených centrů.

- **Detaily a metodika:** Produkt: Team Stats

### `Defensive duels` — Defenzivní duely

*počet*

Celkový počet defenzivních duelů.

- **Detaily a metodika:** Produkt: Match report, Player Stats, Team Stats

### `Defensive duels won` — Vyhrané defenzivní duely

*počet*

Celkový počet vyhraných defenzivních duelů. K dispozici i jako procento.

- **Detaily a metodika:** Produkt: Match report, Player Stats, Team Stats

### `Direct free kicks taken` — Zahrané přímé kopy

*počet*

Celkový počet střel zahraných z volných kopů.

- **Detaily a metodika:** Produkt: Match report

### `Dribbles` — Kličky

*počet*

Celkový počet kliček.

- **Detaily a metodika:** Produkt: Match report, Player Stats

### `Dribbles / successful` — Úspěšné kličky

*počet*

Celkový počet úspěšných kliček. K dispozici i jako procento.

- **Detaily a metodika:** Produkt: Match report, Player Stats

### `Duels` — Duely

*počet*

Celkový počet duelů (ofenzivních, defenzivních, o volný míč, vzdušných).

- **Detaily a metodika:** Produkt: Match report, Player Stats

### `Duels win rate` — Úspěšnost duelů

*%*

Procento vyhraných duelů za interval.

- **Detaily a metodika:** Produkt: Match report

### `Duels won` — Vyhrané duely

*počet*

Celkový počet vyhraných duelů. K dispozici i jako procento.

- **Detaily a metodika:** Produkt: Match report, Player Stats

### `Expected Assists (xA)` — Očekávané asistence

*xA*

Součet hodnot xA všech shot assists.

- **Detaily a metodika:** Produkt: Match report, Player Stats

### `Expected Goals (xG)` — Očekávané góly

*xG*

Součet hodnot xG všech střel.

- **Detaily a metodika:** Produkt: Match report, Player Stats, Team Stats

### `Expected Conceded Goals (xCG, xG2)` — Očekávané obdržené góly

*xCG*

Součet hodnot xCG všech střel na branku.

- **Detaily a metodika:** Produkt: Match report, Player Stats

### `Forward passes` — Dopředné přihrávky

*počet*

Celkový počet přihrávek v 90° výseči otočené o 45° směrem dopředu.

- **Detaily a metodika:** Produkt: Match report, Player Stats, Team Stats

### `Forward passes / accurate` — Přesné dopředné přihrávky

*počet*

Celkový počet přesných dopředných přihrávek. K dispozici i jako procento.

- **Detaily a metodika:** Produkt: Match report, Player Stats, Team Stats

### `Fouls` — Fauly

*počet*

Celkový počet faulů ve hře.

- **Detaily a metodika:** Produkt: Match report, Player Stats, Team Stats

### `Fouls suffered` — Obdržené fauly

*počet*

Celkový počet faulů, které hráč obdržel.

- **Detaily a metodika:** Produkt: Match report, Player Stats

### `Free kicks` — Volné kopy

*počet*

Celkový počet volných kopů.

- **Detaily a metodika:** Produkt: Match report, Team Stats

### `Free kicks with shots` — Volné kopy se střelou

*počet*

Celkový počet volných kopů, které vedly ke střele týmu zahrávajícího kop do 14 sekund.

- **Detaily a metodika:** Produkt: Match report, Team Stats

### `Goalkeeper exits` — Výběhy brankáře

*počet*

Celkový počet výběhů brankáře.

- **Detaily a metodika:** Produkt: Match report, Player Stats

### `Goals` — Góly

*počet*

Celkový počet vstřelených gólů. V týmovém kontextu zahrnuje i vlastní góly.

- **Detaily a metodika:** Produkt: Match report, Player Stats, Team Stats

### `Goals conceded` — Obdržené góly

*počet*

Celkový počet obdržených gólů. V kontextu hráče se vztahuje jen na brankáře.

- **Detaily a metodika:** Produkt: Match report, Player Stats, Team Stats

### `Interceptions` — Zachycení

*počet*

Celkový počet zachycení míče.

- **Detaily a metodika:** Produkt: Match report, Player Stats, Team Stats

### `Key passes` — Klíčové přihrávky

*počet*

Celkový počet klíčových přihrávek.

- **Detaily a metodika:** Produkt: Match report

### `Lateral passes` — Příčné přihrávky

*počet*

Celkový počet přihrávek ve dvou 90° výsečích otočených o 45° do strany, delších než 12 metrů.

- **Detaily a metodika:** Produkt: Match report, Team Stats

### `Lateral passes / accurate` — Přesné příčné přihrávky

*počet*

Celkový počet přesných příčných přihrávek. K dispozici i jako procento.

- **Detaily a metodika:** Produkt: Match report, Team Stats

### `Long pass share (%)` — Podíl dlouhých přihrávek

*%*

Procento z přihrávek týmu, které jsou dlouhé přihrávky.

- **Detaily a metodika:** Produkt: Match report, Team Stats

### `Long passes` — Dlouhé přihrávky

*počet*

Celkový počet dlouhých přihrávek.

- **Detaily a metodika:** Produkt: Match report, Player Stats, Team Stats

### `Long passes / accurate` — Přesné dlouhé přihrávky

*počet*

Celkový počet přesných dlouhých přihrávek. K dispozici i jako procento.

- **Detaily a metodika:** Produkt: Match report, Player Stats, Team Stats

### `Loose ball duels` — Duely o volný míč

*počet*

Celkový počet duelů o volný míč.

- **Detaily a metodika:** Produkt: Match report, Player Stats

### `Loose ball duels won` — Vyhrané duely o volný míč

*počet*

Celkový počet vyhraných duelů o volný míč. K dispozici i jako procento.

- **Detaily a metodika:** Produkt: Match report, Player Stats

### `Losses` — Ztráty

*počet*

Celkový počet ztrát držení míče.

- **Detaily a metodika:** Produkt: Match report, Player Stats, Team Stats

### `Losses / High` — Ztráty ve finální třetině

*počet*

Celkový počet ztrát držení míče ve finální třetině.

- **Detaily a metodika:** Produkt: Match report, Team Stats

### `Losses / Medium` — Ztráty ve střední třetině

*počet*

Celkový počet ztrát držení míče ve střední třetině.

- **Detaily a metodika:** Produkt: Match report, Team Stats

### `Losses / Low` — Ztráty ve vlastní třetině

*počet*

Celkový počet ztrát držení míče ve vlastní třetině.

- **Detaily a metodika:** Produkt: Match report, Team Stats

### `Losses / Own half` — Ztráty ve vlastní polovině

*počet*

Celkový počet ztrát držení míče ve vlastní polovině.

- **Detaily a metodika:** Produkt: Match report, Player Stats

### `Match tempo` — Tempo zápasu

*počet/min*

Počet přihrávek týmu na minutu čistého držení míče.

- **Detaily a metodika:** Produkt: Match report

### `Number of possessions` — Počet držeb

*počet*

Celkový počet držeb.

- **Detaily a metodika:** Produkt: Match report

### `Offensive duels` — Ofenzivní duely

*počet*

Celkový počet ofenzivních duelů.

- **Detaily a metodika:** Produkt: Match report, Player Stats, Team Stats

### `Offensive duels won` — Vyhrané ofenzivní duely

*počet*

Celkový počet vyhraných ofenzivních duelů. K dispozici i jako procento.

- **Detaily a metodika:** Produkt: Match report, Player Stats, Team Stats

### `Offsides` — Ofsajdy

*počet*

Celkový počet ofsajdů.

- **Detaily a metodika:** Produkt: Match report, Player Stats, Team Stats

### `Open play possessions / Short` — Krátké držby z otevřené hry

*počet*

Celkový počet držeb z otevřené hry o délce 0–10 sekund.

- **Detaily a metodika:** Produkt: Match report

### `Open play possessions / Medium` — Středně dlouhé držby z otevřené hry

*počet*

Celkový počet držeb z otevřené hry o délce 10–20 sekund.

- **Detaily a metodika:** Produkt: Match report

### `Open play possessions / Long` — Dlouhé držby z otevřené hry

*počet*

Celkový počet držeb z otevřené hry o délce 20–45 sekund.

- **Detaily a metodika:** Produkt: Match report

### `Open play possessions / Very long` — Velmi dlouhé držby z otevřené hry

*počet*

Celkový počet držeb z otevřené hry o délce nad 45 sekund.

- **Detaily a metodika:** Produkt: Match report

### `Open play possessions / Total` — Držby z otevřené hry celkem

*počet*

Celkový počet držeb z otevřené hry.

- **Detaily a metodika:** Produkt: Match report

### `Pass accuracy (%)` — Přesnost přihrávek

*%*

Procento přesných přihrávek.

- **Detaily a metodika:** Produkt: Match report

### `Passes` — Přihrávky

*počet*

Celkový počet přihrávek.

- **Detaily a metodika:** Produkt: Match report, Player Stats, Team Stats

### `Passes / accurate` — Přesné přihrávky

*počet*

Celkový počet přesných přihrávek. K dispozici i jako procento.

- **Detaily a metodika:** Produkt: Match report, Player Stats, Team Stats

### `Passes beyond own third` — Přihrávky za vlastní třetinu

*počet*

Celkový počet přihrávek (včetně rozehrání od branky), které skončily mimo vlastní třetinu.

- **Detaily a metodika:** Produkt: Match report

### `Passes beyond own third / accurate` — Přesné přihrávky za vlastní třetinu

*počet*

Celkový počet přesných přihrávek (včetně rozehrání od branky), které skončily mimo vlastní třetinu. K dispozici i jako procento.

- **Detaily a metodika:** Produkt: Match report

### `Passes inside own third` — Přihrávky ve vlastní třetině

*počet*

Celkový počet přihrávek (včetně rozehrání od branky) provedených uvnitř vlastní třetiny.

- **Detaily a metodika:** Produkt: Match report

### `Passes inside own third / accurate` — Přesné přihrávky ve vlastní třetině

*počet*

Celkový počet přesných přihrávek (včetně rozehrání od branky) uvnitř vlastní třetiny. K dispozici i jako procento.

- **Detaily a metodika:** Produkt: Match report

### `Passes per minute` — Přihrávky za minutu

*počet/min*

Počet přihrávek na minutu držení míče.

- **Detaily a metodika:** Produkt: Team Stats

### `Passes to final third` — Přihrávky do finální třetiny

*počet*

Celkový počet přihrávek zvenčí finální třetiny do finální třetiny.

- **Detaily a metodika:** Produkt: Match report, Team Stats

### `Passes to final third / accurate` — Přesné přihrávky do finální třetiny

*počet*

Celkový počet přesných přihrávek zvenčí finální třetiny do finální třetiny. K dispozici i jako procento.

- **Detaily a metodika:** Produkt: Match report, Team Stats

### `Passes to penalty area` — Přihrávky do vápna

*počet*

Celkový počet přihrávek zvenčí pokutového území soupeře do pokutového území soupeře.

- **Detaily a metodika:** Produkt: Match report, Player Stats

### `Passes to penalty area / accurate` — Přesné přihrávky do vápna

*počet*

Celkový počet přesných přihrávek zvenčí pokutového území soupeře do pokutového území soupeře. K dispozici i jako procento.

- **Detaily a metodika:** Produkt: Match report, Player Stats

### `Penalties` — Penalty

*počet*

Celkový počet penalt.

- **Detaily a metodika:** Produkt: Team Stats

### `Penalties converted` — Proměněné penalty

*počet*

Celkový počet proměněných penalt.

- **Detaily a metodika:** Produkt: Team Stats

### `Penalties saved` — Chycené penalty

*počet*

Celkový počet chycených penalt. Platí pro brankáře.

- **Detaily a metodika:** Produkt: Match report

### `Penalty area entries` — Vstupy do vápna

*počet*

Celkový počet vstupů do pokutového území (přihrávkou, centrem nebo vedením míče).

- **Detaily a metodika:** Produkt: Team Stats

### `Positional attacks` — Poziční útoky

*počet*

Celkový počet pozičních útoků.

- **Detaily a metodika:** Produkt: Match report, Team Stats

### `Positional attacks with shots` — Poziční útoky se střelou

*počet*

Celkový počet pozičních útoků, ve kterých držba obsahovala střelu.

- **Detaily a metodika:** Produkt: Match report, Team Stats

### `Possessions reaching opponent box` — Držby do vápna soupeře

*počet*

Celkový počet držeb, které mají aspoň jednu úspěšnou akci v pokutovém území soupeře.

- **Detaily a metodika:** Produkt: Match report

### `Possessions reaching opponent half` — Držby do poloviny soupeře

*počet*

Celkový počet držeb, které mají aspoň jednu úspěšnou akci v polovině soupeře.

- **Detaily a metodika:** Produkt: Match report

### `Pressing intensity (PPDA)` — Intenzita presinku

*index*

Metrika kvantifikující intenzitu vysokého presinku v posledních 60 % hřiště. Nižší hodnota znamená intenzivnější presink.

- **Detaily a metodika:** Produkt: Match report, Team Stats

### `Progressive passes` — Progresivní přihrávky

*počet*

Celkový počet progresivních přihrávek.

- **Detaily a metodika:** Produkt: Match report, Team Stats

### `Progressive passes / accurate` — Přesné progresivní přihrávky

*počet*

Celkový počet přesných progresivních přihrávek. K dispozici i jako procento.

- **Detaily a metodika:** Produkt: Match report, Team Stats

### `Progressive runs` — Progresivní běhy

*počet*

Celkový počet progresivních běhů.

- **Detaily a metodika:** Produkt: Player Stats

### `Pure possession time` — Čistý čas držení

*s*

Čistý čas strávený v držení míče.

- **Detaily a metodika:** Produkt: Match report

### `Received passes` — Přijaté přihrávky

*počet*

Celkový počet přijatých přesných přihrávek.

- **Detaily a metodika:** Produkt: Player Stats

### `Recoveries` — Zisky

*počet*

Celkový počet zisků míče.

- **Detaily a metodika:** Produkt: Match report, Player Stats, Team Stats

### `Recoveries / High` — Zisky ve finální třetině

*počet*

Celkový počet zisků držení míče ve finální třetině.

- **Detaily a metodika:** Produkt: Match report, Team Stats

### `Recoveries / Medium` — Zisky ve střední třetině

*počet*

Celkový počet zisků držení míče ve střední třetině.

- **Detaily a metodika:** Produkt: Match report, Team Stats

### `Recoveries / Low` — Zisky ve vlastní třetině

*počet*

Celkový počet zisků držení míče ve vlastní třetině.

- **Detaily a metodika:** Produkt: Match report, Team Stats

### `Recoveries / Opponent half` — Zisky v polovině soupeře

*počet*

Celkový počet zisků držení míče v polovině soupeře.

- **Detaily a metodika:** Produkt: Match report, Player Stats

### `Recoveries per minute` — Zisky za minutu

*počet/min*

Celkový počet zisků držení míče na minutu hry.

- **Detaily a metodika:** Produkt: Match report

### `Red cards` — Červené karty

*počet*

Celkový počet červených karet.

- **Detaily a metodika:** Produkt: Match report, Player Stats, Team Stats

### `Reflex saves` — Reflexivní zákroky

*počet*

Celkový počet reflexivních zákroků. Platí pouze pro brankáře.

- **Detaily a metodika:** Produkt: Match report, Player Stats

### `Saves` — Zákroky

*počet*

Celkový počet zákroků. Platí pouze pro brankáře.

- **Detaily a metodika:** Produkt: Match report, Player Stats

### `Second assists` — Druhé asistence

*počet*

Celkový počet druhých asistencí.

- **Detaily a metodika:** Produkt: Match report, Player Stats

### `Set pieces` — Standardní situace

*počet*

Celkový počet útoků začínajících standardní situací.

- **Detaily a metodika:** Produkt: Team Stats

### `Set pieces with shots` — Standardky se střelou

*počet*

Celkový počet útoků začínajících standardkou, ve kterých držba obsahovala střelu. K dispozici i jako procento.

- **Detaily a metodika:** Produkt: Team Stats

### `Short + medium passes` — Krátké a střední přihrávky

*počet*

Celkový počet přihrávek, které nebyly dlouhé.

- **Detaily a metodika:** Produkt: Match report

### `Short + medium passes / accurate` — Přesné krátké a střední přihrávky

*počet*

Celkový počet přesných přihrávek, které nebyly dlouhé. K dispozici i jako procento.

- **Detaily a metodika:** Produkt: Match report

### `Shot assists` — Přihrávky před střelou

*počet*

Celkový počet shot assists.

- **Detaily a metodika:** Produkt: Match report, Player Stats

### `Shots` — Střely

*počet*

Celkový počet střel.

- **Detaily a metodika:** Produkt: Match report, Player Stats, Team Stats

### `Shots against` — Střely na branku

*počet*

Celkový počet střel na branku (včetně zblokovaných a mimo).

- **Detaily a metodika:** Produkt: Team Stats

### `Shots blocked` — Zblokované střely

*počet*

Celkový počet střel zblokovaných soupeřem.

- **Detaily a metodika:** Produkt: Match report

### `Shots from the box` — Střely z vápna

*počet*

Celkový počet střel z pokutového území soupeře.

- **Detaily a metodika:** Produkt: Match report

### `Shots from the box on target` — Střely z vápna na branku

*počet*

Celkový počet střel z pokutového území soupeře, které mířily na branku. K dispozici i jako procento.

- **Detaily a metodika:** Produkt: Match report

### `Shots on post` — Střely do tyče

*počet*

Celkový počet střel, které trefily tyč a poté šly mimo.

- **Detaily a metodika:** Produkt: Match report

### `Shots on target` — Střely na branku

*počet*

Celkový počet střel, které mířily na branku. K dispozici i jako procento.

- **Detaily a metodika:** Produkt: Match report, Player Stats, Team Stats

### `Shots outside the box` — Střely mimo vápno

*počet*

Celkový počet střel z prostoru mimo pokutové území soupeře.

- **Detaily a metodika:** Produkt: Match report, Team Stats

### `Shots outside the box on target` — Střely mimo vápno na branku

*počet*

Celkový počet střel z prostoru mimo pokutové území soupeře, které mířily na branku. K dispozici i jako procento.

- **Detaily a metodika:** Produkt: Match report, Team Stats

### `Shots wide` — Střely mimo

*počet*

Celkový počet střel, které nemířily na branku (zblokované).

- **Detaily a metodika:** Produkt: Match report

### `Sliding tackles` — Skluzy

*počet*

Celkový počet skluzů.

- **Detaily a metodika:** Produkt: Match report, Player Stats, Team Stats

### `Sliding tackles / won` — Vyhrané skluzy

*počet*

Celkový počet vyhraných skluzů. Metodika viz Defenzivní duel. K dispozici i jako procento.

- **Detaily a metodika:** Produkt: Match report, Player Stats, Team Stats

### `Smart passes` — Kreativní průnikovky

*počet*

Celkový počet pokusů o smart pass.

- **Detaily a metodika:** Produkt: Match report, Team Stats

### `Smart passes / accurate` — Přesné kreativní průnikovky

*počet*

Celkový počet přesných smart passes. K dispozici i jako procento.

- **Detaily a metodika:** Produkt: Match report, Team Stats

### `Third assists` — Třetí asistence

*počet*

Celkový počet třetích asistencí.

- **Detaily a metodika:** Produkt: Match report

### `Through passes` — Průnikové přihrávky

*počet*

Celkový počet pokusů o průnikovou přihrávku.

- **Detaily a metodika:** Produkt: Match report, Player Stats

### `Through passes / accurate` — Přesné průnikové přihrávky

*počet*

Celkový počet přesných průnikových přihrávek. K dispozici i jako procento.

- **Detaily a metodika:** Produkt: Match report, Player Stats

### `Throw-ins` — Auty

*počet*

Celkový počet zahraných autů.

- **Detaily a metodika:** Produkt: Match report

### `Touches in box` — Doteky ve vápně

*počet*

Celkový počet akcí s míčem v pokutovém území soupeře.

- **Detaily a metodika:** Produkt: Match report, Team Stats

### `Yellow cards` — Žluté karty

*počet*

Celkový počet žlutých karet.

- **Detaily a metodika:** Produkt: Match report, Player Stats, Team Stats

---

## Poznámky ke zdroji

**Jen ve videu, ne v API:** Covering teammate, Defensive positioning, Off the ball movement, Pressing duel. Kdo pracuje výhradně s API, o celou tuto vrstvu přichází.

**Chyby v oficiálním katalogu:** `Progressive runs / 90` je popsáno jako „number of progressive passes“ a `Shot assists / 90` jako „number of dribbles“ — v obou případech jde o překlep. U pojmu Ball out jsou v původním textu zaměněné touchline a byline.

**Nejostřejší past:** u PPDA znamená **nižší** hodnota **intenzivnější** presink — obráceně než u většiny metrik. Challenge intensity měří podobnou věc obrácenou logikou (vyšší = aktivnější). Nedávej je do jednoho grafu bez upozornění.

## Souvislosti

- [[Wyscout]] – wiki stránka o Wyscoutu jako zdroji: historie, co z něj v Sigmě bereme, ukázky z Barça kurzu. Tahle poznámka je její detailní datový protějšek.
- [[SkillCorner – slovník metrik]] – stejný typ slovníku pro druhý hlavní zdroj, 127 hesel. Pozor: metriky stejného jména (HSR, sprint, akcelerace, per 90) mají v obou systémech jiný původ i jiné prahy, takže nejsou přímo srovnatelné.
- [[SkillCorner]] – wiki stránka o SkillCorneru jako zdroji: tracking místo event dat.
- [[📊 Fotbalová zápasová data]] – tři pohledy na data (průměr na zápas, 30 min TIP, 100 situací). Pozor: tyhle pohledy jsou SkillCornerí; Wyscout nabízí per 90 a possession-adjusted, což není totéž.
- [[Normalizace herních dat]] – přepočty per 90 a per 30 TIP/OTIP. Pozor: Wyscoutí `Minutes played` zahrnuje nastavení, takže jeho per 90 není přímo srovnatelné se SkillCornerem.
- [[Expected goals (xG)]] – koncept xG obecně. Wyscoutí implementace přidává post-shot xG (xCG/xG2) a fixní 0,76 u penalt.
- [[Datový skauting – metriky a úskalí]] – proč metriky samy nestačí. Tenhle slovník je k tomu praktická příručka, co která metrika doopravdy měří.
- [[Skauting – proces a reporting]] – kde se metriky používají v procesu a jak se z nich staví postové thresholdy.
- [[Eyeball – platforma, data a metriky]] – třetí datová platforma, stejný typ soupisu metrik. Dobré k porovnání pokrytí.
- [[Karta hráče 🎯]] – cílové místo, kde se metriky zobrazují hráčům a trenérům.
- [[🔍 Skauting]] – skautingová témata v Sigmě.
- [[🥅 Brankářská data]] – brankářské metriky. Wyscout k nim přidává `Shot against`, `Save`, `Reflexes save`, `Exits` a post-shot xG.
- [[📡 GPS Data]] – fyzická data z GPS. Wyscoutí fyzické metriky (kategorie 12) jsou jejich hrubší náhrada tam, kde GPS nemáme, tedy u soupeřů a ve skautingu.
- [[Analýza soupeře – metodika]] a [[Hodnocení utkání a pozápasový report]] – hlavní výstupy, do kterých tyhle metriky vstupují.

## Otevřené body

- [x] Doplnit do Znalostí i slovník SkillCorneru jako protějšek téhle poznámky — hotovo 2026-10-19, viz [[SkillCorner – slovník metrik]].
- [ ] Ověřit, které z katalogových metrik máme reálně dostupné v našem tarifu — část je jen v Advanced Search, část jen v Rankings nebo Player Lists.
- [ ] Rozhodnout, jestli do [[Karta hráče 🎯]] vstupují Wyscoutí metriky v surové podobě, nebo až po possession-adjusted přepočtu.
