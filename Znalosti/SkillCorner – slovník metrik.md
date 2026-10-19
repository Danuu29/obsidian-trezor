---
datum: 2026-10-19
aktualizovano: 2026-10-19
typ: referenční slovník
zdroj: skillcorner.crunch.help (zpracováno s Claude)
projekt: SK Sigma Olomouc – analytika
tags: [skillcorner, herni-data, metriky, slovnik, tracking, fyzicka-data, skauting]
aliases: [SkillCorner glosář, SkillCorner metriky, SkillCorner Knowledge Base]
---
# SkillCorner – slovník metrik

> Kompletní český výklad [SkillCorner Knowledge Base](https://skillcorner.crunch.help/en/glossaries) — **127 hesel** ve 13 kategoriích: fyzická data, náběhy bez míče, přihrávky na běžce, hra pod tlakem, modely a normalizace. U každé metriky definice, metodika výpočtu, možnosti normalizace a nástrahy při srovnávání hráčů. Stav ke 17. 8. 2026.

## Kontext a cíl

[[SkillCorner]] je poskytovatel tracking dat z videa — běžecká data podobná GPS plus metriky hry bez míče („Game Intelligence“). Jeho dokumentace je anglicky a roztříštěná: samotný glosář odkazuje na definice, které leží jinde (typy náběhů, prahy intenzity tlaku, threat model, predikce zátěže). Cílem bylo dostat to na jedno místo v češtině a doplnit, co v dokumentaci explicitně nestojí — kde jsou pasti a které metriky spolu nejsou srovnatelné.

Protějšek k [[Wyscout – slovník metrik]] (320 hesel). Dohromady pokrývají oba hlavní zdroje herních dat, se kterými pracujeme — SkillCorner tracking, [[Wyscout]] event data. Navazuje na pohledy na data v [[📊 Fotbalová zápasová data]] a na přepočty v [[Normalizace herních dat]].

Anglický název je ten, který najdeš ve Web Appu, v API i v CSV exportech — používej ho jako klíč. České názvy jsou pracovní překlady. Sekce **Pozor na** je u většiny hesel to nejcennější. Neoficiální dokument.

## Nejdůležitější nástrahy

Výtah toho, na co se v praxi naráží nejčastěji:

1. **PSV-99 a Peak Velocity nejsou zaměnitelné.** PSV-99 záměrně odřezává 1 % nejvyšších měření (proto je stabilní v čase a mezi ligami), Peak Velocity míří na skutečné maximum. V jedné analýze drž jednu z nich.
2. **Výkony pod 30 minut se nedoporučují vůbec.** Model predikce zátěže je nastavený na výkony nad 70 minut; u střídajících hráčů se PSV-99 navíc nadhodnocuje, protože rozložení rychlostí je posunuté nahoru bez běžného nízkointenzivního zotavení.
3. **Mužské a ženské prahy se liší** u všech zónových metrik (HSR, sprint, akcelerace). Hodnoty mezi pohlavími proto nejsou přímo srovnatelné.
4. **Metriky `Time to…` a 5-0-5 jdou obráceně — nižší je lepší.** V percentilových žebříčcích se to snadno splete. Navíc se dodají jen při aspoň 3 výkonech, takže chybějící hodnota neznamená pomalého hráče, ale malý vzorek.
5. **Threat je hodnota nabídky, ne realizace.** Počítá se i u náběhů, na které nikdo nepřihrál, a popisuje šanci týmu na gól do 10 s — není to xG ani xA. Viz [[Expected goals (xG)]].
6. **Náběhy bez míče se nedetekují u standardních situací a rozehrávek**, protože vznikají jen během držby hráče. Hráčům aktivním při standardkách to čísla systematicky sráží.
7. **Typ náběhu určují poslední 4 sekundy.** Pohyb, který začal jako support run a skončil za obranou, se počítá celý jako in behind.
8. **Volba normalizace mění pořadí hráčů.** Pro náběhy a přihrávky je per 30 min TIP správnější než per 90, protože odstraňuje vliv toho, jak dlouho tým drží míč. Detailně [[Normalizace herních dat]].
9. **Sada Overcoming Pressure je označená jako deprecated** — nahrazují ji On-Ball Engagements v Game Intelligence V2. Zůstává ale ve starších reportech a exportech, proto je ve slovníku zpracovaná celá (17 hesel, kategorie 10).
10. **Chybějící zápas neznamená, že hráč nehrál.** Může znamenat jen neúspěšnou kontrolu kvality (QC). Do průměrů vstupují pouze výkony, které QC prošly — proto SkillCorner doporučuje pro týmové agregace přepočet per 900 minut.

## Obsah

1. **Základ a kvalita dat** — 8 hesel
2. **Fyzika — vzdálenosti** — 6 hesel
3. **Fyzika — počty akcí** — 7 hesel
4. **Fyzika — maximální rychlost** — 4 hesel
5. **Fyzika — explozivita** — 10 hesel
6. **Fyzika — změny směru** — 7 hesel
7. **Typy náběhů bez míče** — 11 hesel
8. **Náběhy bez míče — metriky** — 16 hesel
9. **Přihrávky na běžce** — 16 hesel
10. **Hra pod tlakem** — 17 hesel
11. **Modely a koncepty** — 9 hesel
12. **Eventy a geometrie** — 10 hesel
13. **Normalizace a průměrování** — 6 hesel

## Prahy a hranice

Numerické hranice, na kterých definice stojí — nejčastější zdroj chyb při srovnávání.

| Pojem | Muži | Ženy |
|---|---|---|
| Running | muži 15–20 km/h | ženy 13–19 km/h |
| High Speed Running (HSR) | muži 20–25 km/h | ženy 19–23 km/h |
| Sprinting | muži nad 25 km/h | ženy nad 23 km/h |
| High Intensity (HI) | muži od 20 km/h výš | ženy od 19 km/h výš |
| Medium Acceleration | muži 1,5–3 m/s² | ženy 1,4–2,7 m/s² |
| High Acceleration | muži nad 3 m/s² | ženy nad 2,7 m/s² |
| Medium Deceleration | muži −1,5 až −3 m/s² | ženy −1,4 až −2,7 m/s² |
| High Deceleration | muži pod −3 m/s² | ženy pod −2,7 m/s² |
| Explozivní akcelerace — start | pod 9 km/h | — |
| Off-ball run — min. rychlost | 4,2 m/s = 15 km/h, aspoň 0,7 s | — |
| PSV-99 — vstupní filtr | pohyb nad 4,0 m/s | — |
| Dangerous run / dangerous pass | threat nad 2 % | — |
| Difficult pass | xPass pod 65 % | — |
| Passing option | skóre nad 0,6, aspoň 0,3 s | — |
| Akce acc/dec — min. trvání | 0,7 s | — |
| Time to 505 — úhel 180° | 150°–210° | — |
| Time to 505 — úhel 90° | 70°–120° | — |
| Doporučená min. délka výkonu | 30 min (pod 30 min nedoporučeno) | — |

## 1. Základ a kvalita dat

*Pojmy, bez kterých se ostatní metriky nedají správně přečíst: co je výkon (performance), jak funguje kontrola kvality, co znamená TIP/OTIP, jak se řeší neviditelnost hráče v televizním záběru a jaké pozice SkillCorner používá.*

### `Performance` — Výkon (start v zápase)

Jedno vystoupení jednoho hráče v jednom zápase. Dva zápasy jednoho hráče = dva výkony; jeden zápas dvou hráčů = také dva výkony; dva zápasy dvou hráčů = čtyři výkony.

- **Metodika:** Základní jednotka vzorku. Všechny agregace (průměry, TOP 3, TOP 5) se počítají přes výkony, ne přes zápasy.
- **Pozor na:** Když se v datech objeví „počet výkonů ve vzorku“, je to hlavní indikátor důvěryhodnosti. U TOP 3 / TOP 5 metrik se hodnota vůbec nedodá, pokud hráč nemá dost výkonů s danou metrikou.

### `Quality Check` — Kontrola kvality

*QC*

Automatická kontrola, zda je kvalita dat u konkrétního výkonu dost vysoká na to, aby se jí dalo věřit. Když projde, data se dodají; když neprojde, nedodá se nic.

- **Metodika:** Celý proces SkillCorner je plně automatický, bez lidské korekce. Kontrola kvality je proto jediná pojistka — a je záměrně striktní: co může být chybné, se nedodá.
- **Pozor na:** Do průměrů vstupují jen výkony, které QC prošly. Chybějící zápas tedy neznamená, že hráč nehrál — může znamenat jen neúspěšný QC. Při agregaci na úroveň týmu proto SkillCorner doporučuje relativní přístup per 900 minut (P900).

### `TIP` — Tým v držení míče

Team In Possession — období, kdy je tým daného hráče na míči. Fyzické metriky lze rozdělit podle držení: `Distance TIP` je vzdálenost naběhaná v době, kdy byl hráč na hřišti a jeho tým měl míč.

- **Metodika:** Minuty TIP se v API vrací jako `minutes_tip` na úrovni hráče, období i týmu.
- **Pozor na:** TIP/OTIP split výrazně mění výklad objemových metrik. Krajní obránce dominantního týmu naběhá většinu metrů v TIP, hráč bránícího se týmu v OTIP — surové celkové číslo tento rozdíl zamaskuje.

### `OTIP` — Soupeř v držení míče

Opponent Team In Possession — období, kdy má míč soupeř. `Distance OTIP` je vzdálenost naběhaná při bránění.

- **Metodika:** V API `minutes_otip`. Pro tým platí, že jeho OTIP se rovná TIP soupeře.
- **Pozor na:** Vysoké OTIP objemy u záložníka nemusí být známkou pracovitosti, ale toho, že jeho tým málo drží míč. Vždy porovnávej v kontextu stylu týmu.

### `Adjusted minutes TIP` — Upravené minuty TIP

Období, kdy (i) byl tým hráče na míči *a zároveň* (ii) SkillCorner byl schopen monitorovat náběhy, přihrávky a presink.

- **Metodika:** Používá se jako jmenovatel pro metriky náběhů, přihrávek a presinku — tedy pro vše z Game Intelligence, ne pro fyzická data.
- **Pozor na:** Kvůli televizní režii (detailní záběry, kamera na tribunu) nelze zachytit každý náběh a každou přihrávku. Proto se pro tyto metriky nepoužívají skutečné minuty TIP, ale jen ty monitorovatelné. Nemíchej s `minutes_tip` u fyzických dat.

### `minutes_played / minutes_played_regular_time` — Odehrané minuty

`minutes_played` = minuty odehrané v celém zápase včetně prodloužení. `minutes_played_regular_time` = jen během prvních dvou půlí.

- **Metodika:** Dostupné přes endpoint `/match` nebo `get_match()` v Python klientovi, celkově i po jednotlivých obdobích. Uvádí se i `start_frame` a `end_frame` pobytu na hřišti.
- **Pozor na:** Uvedena jsou jen období, ve kterých hráč skutečně hrál. Mezi koncem jednoho a začátkem dalšího období bývají framy, kdy se nehraje — proto se celkové minuty nerovnají rozdílu framů.

### `Data Quality Standards` — Standardy kvality dat

Soubor podmínek, které musí zápas splnit, aby se data vůbec dodala. Nesplněný zápas se ve Web Appu ani v API neobjeví.

- **Metodika:** Dva hlavní důvody vyřazení: **vysoká chybovost homografie** (kalibrace kamery — špatně viditelné linie hřiště, kamera nízko nebo blízko postranní čáry, přehnaný zoom, komprese videa) a **nízký podíl identifikovaných hráčů** (nečitelná čísla na zádech). Vstupem je HD video od Wyscoutu.
- **Pozor na:** Pokrytí není v ligách rovnoměrné. Pruhované a dvoubarevné dresy (typicky UK a Jižní Amerika) i malé stadiony (Skotsko, Portugalsko) systematicky snižují dostupnost dat. Když hráči chybí zápasy, kontroluj velikost vzorku, ne jen průměr.

### `Positions` — Pozice hráčů

20 pozic: GK, LB, LWB, LCB, CB, RCB, RWB, RB, LDM, DM, RDM, LM, CM, RM, AM, LW, RW, LF, CF, RF.

- **Metodika:** Skupiny pozic pro benchmarking: **Central Defender** (LCB, CB, RCB), **Full Back** (LB, LWB, RWB, RB), **Midfield** (LDM, DM, RDM, LM, CM, RM, AM), **Wide Attacker** (LF, LW, RW, RF), **Center Forward** (CF).
- **Pozor na:** Logika pozic se změnila 15. 4. 2024 (přidány LB, RB, LDM, RDM a skupiny Wide Attacker / Center Forward). Data z doby před touto změnou používají starší rozdělení — při dlouhých časových řadách to ověř. Skupina Midfield je velmi široká: DM a AM se srovnávají proti stejnému benchmarku.

## 2. Fyzika — vzdálenosti

*Kolik hráč naběhá celkem a v jednotlivých rychlostních zónách. Objemové metriky: říkají, kolik práce hráč odvedl, ne jak byla kvalitní.*

Objemové metriky. Samy o sobě říkají, kolik práce hráč odvedl, ne jak byla kvalitní — význam získávají až po rozpadu do rychlostních zón a do TIP/OTIP. Srovnej s [[📡 GPS Data]].

### `Total Distance` — Celková naběhaná vzdálenost

*m*

Celková vzdálenost, kterou hráč nachodil a naběhal na hřišti.

- **Metodika:** Odvozeno z XY tracking dat, doplněno extrapolačním modelem pro části hry, kdy hráč nebyl v záběru hlavní kamery.
- **Normalizace:** celkem · per 90 · M/min · per půle · TIP/OTIP
- **Pozor na:** Nejméně rozlišující fyzická metrika — rozdíly mezi hráči jsou malé a silně závislé na pozici a herním stylu. Sama o sobě neříká o výkonu téměř nic; význam získává až po rozpadu do rychlostních zón a do TIP/OTIP.

### `M/min` — Metry za minutu

*m/min*

Celková vzdálenost dělená počtem odehraných minut. Pro TIP (resp. OTIP) se dělí počtem minut TIP (resp. OTIP).

- **Metodika:** Základní intenzitní ukazatel — vyrovnává rozdíly v odehraném čase.
- **Normalizace:** celkem · TIP · OTIP · per půle
- **Pozor na:** Pozor na jmenovatel: `M/min TIP` se dělí minutami TIP, ne celkovými minutami. Když to čtenář neví, srovnává nesrovnatelné.

### `Running Distance` — Vzdálenost v běžecké zóně

*m*

Vzdálenost naběhaná v pásmu „běh“ — muži 15–20 km/h, ženy 13–19 km/h.

- **Metodika:** Prahy se liší podle pohlaví, aby zóny odpovídaly reálnému rozložení rychlostí.
- **Normalizace:** celkem · per 90 · per půle · TIP/OTIP
- **Pozor na:** Nikdy nesrovnávej mužské a ženské hodnoty přímo — stojí na jiných prazích.

### `High Speed Running Distance` — Vzdálenost ve vysoké rychlosti

*HSR · m*

Vzdálenost naběhaná v pásmu HSR — muži 20–25 km/h, ženy 19–23 km/h.

- **Metodika:** Jedna z nejpoužívanějších metrik pro hodnocení vysokointenzivní zátěže.
- **Normalizace:** celkem · per 90 · per půle · TIP/OTIP
- **Pozor na:** HSR je zóna, ne „vše nad 20 km/h“ — sprint (nad 25 km/h) se do ní nepočítá. Pro součet obou zón použij High Intensity Distance.

### `Sprinting Distance` — Sprintová vzdálenost

*m*

Vzdálenost naběhaná nad sprintovým prahem — muži nad 25 km/h, ženy nad 23 km/h.

- **Metodika:** Otevřená zóna bez horního limitu.
- **Normalizace:** celkem · per 90 · per půle · TIP/OTIP
- **Pozor na:** Silně ovlivněná herním kontextem: tým, který hodně brání v nízkém bloku, nabízí méně příležitostí ke sprintu. Nízká hodnota nemusí znamenat nízkou schopnost sprintovat — na to se dívej na PSV-99 a Time to Sprint.

### `High Intensity Distance` — Vysokointenzivní vzdálenost

*HI · m*

Vzdálenost naběhaná v pásmu HSR a výše — tedy HSR + sprint dohromady.

- **Metodika:** Součet Running… ne: součet HSR Distance a Sprinting Distance.
- **Normalizace:** celkem · per 90 · per půle · TIP/OTIP
- **Pozor na:** Praktický souhrnný ukazatel zátěže, ale skrývá profil: 800 m HI může být 700 HSR + 100 sprint (vytrvalý typ) nebo 500 + 300 (explozivní typ). Vždy se podívej i na rozklad.

## 3. Fyzika — počty akcí

*Kolikrát hráč provedl diskrétní vysokointenzivní akci — sprint, HSR úsek, zrychlení, zpomalení. Doplňují vzdálenosti informací o frekvenci a opakovatelnosti.*

### `Count HSR` — Počet HSR úseků

*počet*

Počet diskrétních akcí, kde klouzavý průměr rychlosti v jednosekundovém okně padne do pásma HSR.

- **Metodika:** Klouzavý průměr přes 1 s zabraňuje tomu, aby se jediný chybný frame počítal jako akce.
- **Normalizace:** celkem · per 90 · per půle · TIP/OTIP
- **Pozor na:** Počty a vzdálenosti si odpovídají jen zhruba — hráč s vysokým počtem a nízkou vzdáleností dělá krátké opakované úseky (typicky krajní záložník), obráceně dlouhé nájezdy.

### `Count Sprint` — Počet sprintů

*počet*

Počet diskrétních akcí, kde klouzavý průměr rychlosti v jednosekundovém okně přesáhne sprintový práh.

- **Metodika:** Stejná logika jako u Count HSR, jen nad sprintovým prahem.
- **Normalizace:** celkem · per 90 · per půle · TIP/OTIP
- **Pozor na:** U střídajících hráčů bývá nadhodnocená v přepočtu per 90 — krátký vstup s vysokou intenzitou se špatně extrapoluje na celý zápas.

### `Count HI` — Počet vysokointenzivních akcí

*počet*

Součet Count HSR a Count Sprint.

- **Metodika:** Prostý součet obou počtů.
- **Normalizace:** celkem · per 90 · per půle · TIP/OTIP
- **Pozor na:** Protože je to součet, nelze z něj poznat poměr mezi HSR a sprinty. Pro profilování hráče je informativnější dvojice čísel než jejich součet.

### `Count Medium Acceleration` — Počet středních akcelerací

*počet*

Počet akcí ve pásmu středního zrychlení — muži 1,5–3 m/s², ženy 1,4–2,7 m/s². Akce musí trvat aspoň 0,7 s.

- **Metodika:** Podmínka 0,7 s filtruje krátké šumové výchylky v tracking datech.
- **Normalizace:** celkem · per 90 · per půle · TIP/OTIP
- **Pozor na:** Akcelerační a decelerační počty jsou nejvíc citlivé na kvalitu trackingu — u zápasů s horší homografií je ber s rezervou.

### `Count High Acceleration` — Počet vysokých akcelerací

*počet*

Počet akcí nad prahem vysokého zrychlení — muži nad 3 m/s², ženy nad 2,7 m/s². Akce musí trvat aspoň 0,7 s.

- **Metodika:** Tvoří základ pro navazující explozivní metriky (Explosive Acceleration to HSR / to Sprint).
- **Normalizace:** celkem · per 90 · per půle · TIP/OTIP
- **Pozor na:** Vysoké číslo samo neříká, jak byla akcelerace „výbušná“ — k tomu slouží až Count Explosive Acceleration, které navíc podmiňuje start pod 9 km/h.

### `Count Medium Deceleration` — Počet středních decelerací

*počet*

Počet akcí v pásmu středního zpomalení — muži −1,5 až −3 m/s², ženy −1,4 až −2,7 m/s². Akce musí trvat aspoň 0,7 s.

- **Metodika:** Znaménková konvence: deceleraci vyjadřují negativní hodnoty.
- **Normalizace:** celkem · per 90 · per půle · TIP/OTIP
- **Pozor na:** Decelerace je z hlediska mechanické zátěže a rizika zranění často důležitější než akcelerace, ale v reportech se přehlíží.

### `Count High Deceleration` — Počet vysokých decelerací

*počet*

Počet akcí pod prahem vysokého zpomalení — muži pod −3 m/s², ženy pod −2,7 m/s². Akce musí trvat aspoň 0,7 s.

- **Metodika:** Pozor na formulaci „pod prahem“: jde o hodnoty zápornější než −3 m/s².
- **Normalizace:** celkem · per 90 · per půle · TIP/OTIP
- **Pozor na:** Typicky vysoké u presujících útočníků a u obránců, kteří opakovaně dostupují a zastavují. Souvisí s COD metrikami — čti je společně.

## 4. Fyzika — maximální rychlost

*Odhad maximální rychlosti hráče. SkillCorner nabízí dva odlišné přístupy (PSV-99 a Peak Velocity), které nelze míchat.*

Dva odlišné přístupy k maximální rychlosti, které nelze míchat. Viz nástraha č. 1 výše.

### `PSV-99` — Maximální sprintová rychlost (99. percentil)

*km/h*

Peak Sprint Velocity, 99. percentil. Silný zástupný ukazatel maximální rychlosti, navržený tak, aby byl srovnatelný v čase a mezi ligami.

- **Metodika:** Model izoluje veškerý pohyb hráče nad 4,0 m/s, rozdělí všechna okamžitá měření rychlosti do 100 stejně velkých košů (percentilů) a horní hodnota 99. koše je PSV-99. Přesnost na úrovni jednoho zápasu: MAE 0,73 km/h, MAPE 2,56 %. Na PSV-99 se **neaplikuje extrapolace** — je zkonstruovaná tak, aby fungovala jen z viditelných framů.
- **Normalizace:** nelze dělit per půle · nelze dělit TIP/OTIP · agreguje se přes výkony (TOP 5)
- **Pozor na:** Tři věci: (1) Není to skutečná maximální rychlost — vylučuje 1 % nejvyšších měření právě proto, aby odfiltrovala chyby trackingu. (2) U velmi krátkých vstupů (5–10 min) se hodnota nadhodnocuje, protože rozložení rychlostí je posunuté k horní části bez běžného nízkointenzivního zotavení. (3) Výkony pod 30 minut se pro analýzu nedoporučují vůbec.

### `TOP 5 PSV-99` — Nejlepších 5 PSV-99

*km/h*

Průměr pěti nejlepších PSV-99 výkonů hráče.

- **Metodika:** Vybírá nejlepší výkony, aby se přiblížil skutečnému rychlostnímu potenciálu, ne průměrné hře.
- **Normalizace:** agregát přes výkony
- **Pozor na:** Vyžaduje dostatečný počet výkonů. U hráče s malým vzorkem je hodnota volatilní a snadno tažená jedním nadhodnoceným zápasem.

### `Peak Velocity` — Skutečná maximální rychlost

*km/h*

Skutečná, v zápase naměřená okamžitá maximální rychlost hráče. Využívá vylepšené filtrační metody a míří na věrný odhad absolutního maxima.

- **Metodika:** Novější metrika než PSV-99. Zatímco PSV-99 záměrně odřezává extrémy, Peak Velocity se je snaží zachytit správně díky lepší filtraci.
- **Normalizace:** nelze dělit per půle · nelze dělit TIP/OTIP
- **Pozor na:** **Nemíchej s PSV-99.** Jsou to dvě různé definice a jejich hodnoty nejsou zaměnitelné ani vzájemně přepočitatelné. Pro historickou kontinuitu a srovnání se starými reporty používej PSV-99, pro odhad absolutního maxima Peak Velocity — ale drž jednu z nich v celé analýze.

### `Top 3 Peak Velocity` — Nejlepší 3 skutečná maxima

*km/h*

Průměr tří nejlepších výkonů Peak Velocity hráče.

- **Metodika:** Stejná logika jako TOP 5 PSV-99, jen nad metrikou Peak Velocity a s menším počtem výkonů.
- **Normalizace:** agregát přes výkony
- **Pozor na:** Menší vzorek (3 vs. 5) znamená větší citlivost na odlehlou hodnotu.

## 5. Fyzika — explozivita

*Jak rychle se hráč dostane z klusu do vysoké rychlosti. Kombinace počtů explozivních akcelerací a časových metrik Time to…*

### `Count Explosive Acceleration to HSR` — Počet explozivních akcelerací do HSR

*počet*

Počet vysokých akcelerací, které začínají pod 9 km/h a dosáhnou rychlosti HSR.

- **Metodika:** Kombinuje dvě podmínky: akcelerace musí být vysoká (nad 3 m/s² u mužů, trvat aspoň 0,7 s) a musí startovat z klusu pod 9 km/h a skončit v HSR pásmu.
- **Normalizace:** celkem · per 90 · per půle · TIP/OTIP
- **Pozor na:** Podmínka startu pod 9 km/h je klíčová — akcelerace z už rozběhnutého stavu se nepočítá. Proto je to metrika „výbušnosti z klidu“, ne obecné akcelerační schopnosti.

### `Count Explosive Acceleration to Sprint` — Počet explozivních akcelerací do sprintu

*počet*

Počet vysokých akcelerací, které začínají pod 9 km/h a dosáhnou sprintové rychlosti.

- **Metodika:** Stejná logika jako u varianty do HSR, jen s vyšším cílovým prahem.
- **Normalizace:** celkem · per 90 · per půle · TIP/OTIP
- **Pozor na:** Náročnější podmínka než u HSR varianty, takže čísla jsou výrazně nižší. Nesrovnávej obě metriky mezi sebou jako by byly ve stejném řádu.

### `Time to HSR` — Čas do HSR

*s*

Nejkratší čas, který hráč během daného výkonu strávil mezi 9 km/h a dolní hranicí HSR při explozivní akceleraci do HSR.

- **Metodika:** Bere se minimum přes celý výkon — tedy hráčův nejlepší jednotlivý pokus v zápase, ne průměr.
- **Normalizace:** nelze dělit per půle · nelze dělit TIP/OTIP · agreguje se přes výkony (TOP 3)
- **Pozor na:** Nižší je lepší — obráceně než u většiny fyzických metrik, což se v grafech a percentilových žebříčcích snadno splete. Metrika existuje jen tehdy, když hráč ve výkonu vůbec nějakou explozivní akceleraci do HSR provedl.

### `Time to HSR Post-COD` — Čas do HSR po změně směru

*s*

Nejkratší čas mezi 9 km/h a dolní hranicí HSR při explozivní akceleraci do HSR, která následuje po změně směru.

- **Metodika:** Stejná definice jako Time to HSR, ale zúžená na akcelerace navazující na změnu směru.
- **Normalizace:** agregát přes výkony (TOP 3)
- **Pozor na:** Herně nejrelevantnější varianta — ve fotbale se zrychluje spíš z obratu než z rovného rozjezdu. Zároveň nejvzácnější, takže vzorky bývají malé.

### `TOP 3 Time to HSR` — Nejlepší 3 časy do HSR

*s*

Při agregaci přes více výkonů průměr tří nejlepších hodnot Time to HSR.

- **Metodika:** Dodává se **jen** tehdy, když má hráč aspoň 3 výkony s naměřeným Time to HSR.
- **Normalizace:** agregát přes výkony
- **Pozor na:** Chybějící hodnota neznamená pomalého hráče — může znamenat jen málo příležitostí. Vždy kontroluj počet výkonů.

### `TOP 3 Time to HSR post-COD` — Nejlepší 3 časy do HSR po změně směru

*s*

Průměr tří nejlepších hodnot Time to HSR post-COD.

- **Metodika:** Dodává se jen při aspoň 3 výkonech s touto metrikou.
- **Normalizace:** agregát přes výkony
- **Pozor na:** Nejčastěji chybějící z celé rodiny Time to… metrik, právě kvůli přísné podmínce tří výkonů.

### `Time to Sprint` — Čas do sprintu

*s*

Nejkratší čas mezi 9 km/h a sprintovým prahem při explozivní akceleraci do sprintu během výkonu.

- **Metodika:** Minimum přes výkon, stejně jako u Time to HSR.
- **Normalizace:** agregát přes výkony (TOP 3)
- **Pozor na:** Nižší je lepší. Kombinace vysokého PSV-99 a špatného Time to Sprint popisuje hráče, který je rychlý, ale rozjíždí se dlouho — pro krajního obránce jiný profil než pro křídlo.

### `Time to Sprint Post-COD` — Čas do sprintu po změně směru

*s*

Nejkratší čas mezi 9 km/h a sprintovým prahem při explozivní akceleraci do sprintu, která následuje po změně směru.

- **Metodika:** Průsečík dvou vzácných událostí — proto nejmenší vzorky z celé sady.
- **Normalizace:** agregát přes výkony (TOP 3)
- **Pozor na:** Při malém vzorku je hodnota téměř nepoužitelná pro srovnání. Ber ji jako indicii, ne jako důkaz.

### `TOP 3 Time to Sprint` — Nejlepší 3 časy do sprintu

*s*

Průměr tří nejlepších hodnot Time to Sprint.

- **Metodika:** Dodává se jen při aspoň 3 výkonech s touto metrikou.
- **Normalizace:** agregát přes výkony
- **Pozor na:** Jde o „nejlepší co hráč umí“, ne o typický výkon. Nepoužívej jako ukazatel konzistence.

### `TOP 3 Time to Sprint post-COD` — Nejlepší 3 časy do sprintu po změně směru

*s*

Průměr tří nejlepších hodnot Time to Sprint post-COD.

- **Metodika:** Dodává se jen při aspoň 3 výkonech s touto metrikou.
- **Normalizace:** agregát přes výkony
- **Pozor na:** Nejrestriktivnější metrika sady — u mnoha hráčů prostě nebude existovat.

## 6. Fyzika — změny směru

*Change of Direction: schopnost zpomalit, obrátit a znovu zrychlit. Objem (počet) i kvalita (časy 5-0-5).*

### `Change of Direction Count` — Počet změn směru

*COD · počet*

Kolikrát hráč provede intenzivní změnu směru, bez ohledu na typ pohybu. Validuje fyzický objem, který hráč zvládne udržet, i celkovou pohyblivost.

- **Metodika:** Objemová COD metrika — počítá kvantitu, ne rychlost provedení.
- **Normalizace:** celkem · per 90 · per půle · TIP/OTIP
- **Pozor na:** Vysoký počet COD odpovídá spíš hernímu úkolu (křídlo, presující útočník) než atletické kvalitě. Kvalitu popisují až časy 5-0-5.

### `Time to 505 around 180` — Čas 5-0-5 při obratu o 180°

*s*

Čas, který běžící hráč potřebuje na posledních 5 metrů před ostrým obratem o 180° (v rozsahu 150°–210°) plus prvních 5 metrů po něm.

- **Metodika:** Adaptace laboratorního testu 5-0-5 na zápasová data. Měří se 10 metrů celkem: 5 m dobíhání, obrat, 5 m rozbíhání.
- **Normalizace:** agregát přes výkony (TOP 3)
- **Pozor na:** Nižší je lepší. Nesrovnávej s laboratorními 5-0-5 hodnotami — vstupní rychlost a povrch nejsou standardizované.

### `Time to 505 around 90` — Čas 5-0-5 při obratu o 90°

*s*

Čas, který běžící hráč potřebuje na posledních 5 metrů před ostrým obratem o 90° (v rozsahu 70°–120°) plus prvních 5 metrů po něm.

- **Metodika:** Stejná mechanika jako varianta 180°, jen s mírnějším úhlem — hodnoty jsou proto systematicky nižší.
- **Normalizace:** agregát přes výkony (TOP 3)
- **Pozor na:** Obě varianty 5-0-5 nejsou zaměnitelné ani vzájemně srovnatelné. Vždy uveď, o kterou jde.

### `TOP 3 Time to 505 around 180` — Nejlepší 3 časy 5-0-5 při 180°

*s*

Průměr tří nejlepších hodnot Time to 505 around 180.

- **Metodika:** Dodává se jen při aspoň 3 výkonech s touto metrikou.
- **Normalizace:** agregát přes výkony
- **Pozor na:** Ostrý obrat o 180° je v zápase relativně vzácný — podmínku tří výkonů nemusí splnit ani stabilní hráč základní sestavy.

### `TOP 3 Time to 505 around 90` — Nejlepší 3 časy 5-0-5 při 90°

*s*

Průměr tří nejlepších hodnot Time to 505 around 90.

- **Metodika:** Dodává se jen při aspoň 3 výkonech s touto metrikou.
- **Normalizace:** agregát přes výkony
- **Pozor na:** Dostupnější než varianta 180°, protože obraty o 90° jsou častější.

### `Split per period` — Rozdělení po půlích

Všechny fyzické metriky **kromě** Peak Velocity, PSV-99 a metrik Time to… lze rozdělit na první a druhou půli.

- **Metodika:** K dispozici je jen dělení na dvě půle, prodloužení se nerozděluje. Predikční model zátěže se aplikuje na každé období zvlášť, právě aby toto dělení bylo možné.
- **Pozor na:** Rozdíl mezi půlemi je jeden z nejrychlejších způsobů, jak najít pokles kondice — ale u střídajících hráčů je nesmyslný.

### `Split per possession type` — Rozdělení podle držení míče

Všechny fyzické metriky kromě Peak Velocity, PSV-99 a Time to… lze rozdělit na TIP a OTIP.

- **Metodika:** TIP = tým hráče na míči, OTIP = na míči soupeř.
- **Pozor na:** Nejužitečnější split, jaký SkillCorner nabízí — bez něj se fyzická data u týmů s odlišným stylem prakticky nedají srovnávat.

## 7. Typy náběhů bez míče

*Deset typů náběhů, do kterých klasifikační model zařazuje každý detekovaný náběh. Typ určují poslední 4 sekundy náběhu.*

### `Off-ball Run (detekce)` — Náběh bez míče

*OBR*

Aktivita se považuje za náběh bez míče, když: trvá aspoň 0,7 s, jde nad 4,2 m/s (= 15 km/h), hráč byl aspoň chvíli během náběhu v záběru kamery (nejméně 0,5 s) a navíc byl v průběhu náběhu — nebo do 8 framů po jeho aktivním konci — přihrávkovou možností, případně přihrávku skutečně dostal.

- **Metodika:** Okno se prodlužuje o 8 framů proto, že hráč může náběh udělat v předstihu a přihrávkovou možností se stát až po jeho zastavení. Podmínka „passing option“ vyřazuje náběhy, které by nikdy nebyly obslouženy.
- **Pozor na:** Náběhy se detekují jen během Player Possession — tedy když má někdo míč pod kontrolou. **Standardní situace a rozehrávky se nedetekují vůbec.** To systematicky snižuje čísla u hráčů, kteří se hodně pohybují právě při standardkách.

### `In behind` — Náběh za obranu

Hráč útočí prostor za poslední obrannou linií.

- **Metodika:** Klasifikováno LSTM modelem na základě posledních 4 sekund náběhu.
- **Pozor na:** Nejsledovanější typ náběhu a zároveň nejsilnější prediktor nebezpečnosti. Vysoký počet ale neznamená kvalitu — klíčové je, jak často byl hráč obsloužen (targeted/received).

### `Run ahead of the ball` — Náběh před míč

Hráč je před hráčem s míčem a běží směrem k brance soupeře, ale *neútočí* prostor za poslední obrannou linií (jinak by to byl náběh za obranu).

- **Metodika:** Definice je explicitně vymezená proti in behind — vzájemně se vylučují.
- **Pozor na:** Typický pro podporu v přechodové fázi. Nezaměňuj se support run, kde hráč přichází zezadu nebo z úrovně míče.

### `Support run` — Podpůrný náběh

Hráč podporuje ze zadu nebo z úrovně míče a snaží se zapojit do útočné či přechodové akce — typicky během rychlých přechodů.

- **Metodika:** Definováno hlavně herním záměrem, ne geometrií.
- **Pozor na:** Objemově častý typ. Vysoká čísla obvykle popisují pracovitost v přechodu, ne kreativitu.

### `Coming short` — Náběh na krátko

Hráč běží směrem k hráči s míčem, aby dostal krátkou přihrávku.

- **Metodika:** Protipól náběhu za obranu — pohyb k míči, ne od něj.
- **Pozor na:** Typicky vysoké u devítek, které se otevírají do nohy, a u záložníků nabízejících se k rozehrávce.

### `Dropping off` — Náběh do hloubky vlastní poloviny

Hráč se stahuje směrem k vlastní polovině, aby otevřel přihrávkový úhel nebo vytvořil přesilu v držení míče.

- **Metodika:** Klasifikováno podle směru a záměru pohybu.
- **Pozor na:** Nezaměňuj s coming short: dropping off je o vytvoření úhlu a přesily, coming short o přijetí krátké přihrávky.

### `Pulling wide` — Náběh do šířky

Náběh, který začíná v centru (nebo v poloprostoru), končí v krajním koridoru a na konci je hráč více u kraje než hráč s míčem.

- **Metodika:** Definováno geometricky — startovní a cílový koridor plus relativní pozice vůči hráči s míčem.
- **Pozor na:** Užitečné pro rozpoznání devítek, které rozšiřují hru, nebo záložníků obsazujících kraj po přesunu krajního obránce.

### `Pulling half space` — Náběh do poloprostoru

Náběh, který začíná v centrálním koridoru a končí v poloprostoru.

- **Metodika:** Čistě geometrická definice podle startovního a cílového koridoru.
- **Pozor na:** Poloprostory jsou v modelu hřiště dva (levý a pravý) — metrika je lze filtrovat podle kanálu, kde náběh *končí*.

### `Overlap` — Přeběh po vnější straně

Hráč běží v krajním koridoru nebo v poloprostoru, zezadu se dostává před hráče s míčem (nebo před příjemce míče) a příjemce je více u kraje než hráč s míčem.

- **Metodika:** Rozdíl proti underlapu je jen v relativní pozici: overlap = vně, underlap = uvnitř.
- **Pozor na:** Klasická metrika pro krajní obránce. Sama o sobě neříká, jestli byl přeběh užitečný — spoj ji s targeted/received a s threat.

### `Underlap` — Přeběh po vnitřní straně

Hráč běží v krajním koridoru nebo v poloprostoru, zezadu se dostává před hráče s míčem, a příjemce je vůči hráči s míčem více uvnitř.

- **Metodika:** Zrcadlová definice k overlapu.
- **Pozor na:** Nižší frekvence než overlap. Pro srovnání krajních obránců je poměr overlap : underlap zajímavější než absolutní čísla.

### `Cross receiver` — Náběh na centr

Náběh v pokutovém území s cílem přijmout míč z centru. Centr **nemusí** proběhnout — stačí, že šlo o situaci, kdy k němu mohlo dojít.

- **Metodika:** Definováno prostorem (pokutové území) a kontextem situace, ne tím, zda centr skutečně přišel.
- **Pozor na:** Tady se nejčastěji chybuje: metrika počítá i náběhy, po kterých žádný centr nepřišel. Je to metrika nabídky, ne realizace.

## 8. Náběhy bez míče — metriky

*Objem, typ a kvalita náběhů hráče, když je jeho tým na míči. Postavené na matici: náběh → byl adresátem → dostal míč → vznikla střela → padl gól.*

### `Count runs per match` — Počet náběhů na zápas

*počet*

Kolik náběhů (daného typu) hráč provedl. Příklad: `Count runs in behind per match`.

- **Metodika:** První krok matice náběhů: náběh → adresát → příjem → střela → gól.
- **Normalizace:** per match · per 100 runs · per 30 min TIP
- **Pozor na:** Objemová metrika. Bez navazujících kroků matice neříká nic o užitečnosti — hráč může běhat hodně a nikdy nedostat míč.

### `Count runs targeted per match` — Počet náběhů, na které šla přihrávka

*počet*

Počet náběhů, při kterých byl hráč adresátem přihrávky od hráče s míčem — bez ohledu na to, zda přihrávka došla.

- **Metodika:** Druhý krok matice.
- **Normalizace:** per match · per 100 runs · per 30 min TIP
- **Pozor na:** Poměr targeted / count je jedno z nejužitečnějších čísel v celé sadě: měří, nakolik spoluhráči hráče „vidí“. Nízký poměr může být o hráči, ale i o týmu.

### `Count runs received per match` — Počet náběhů zakončených příjmem míče

*počet*

Počet náběhů, při kterých hráč skutečně dostal míč.

- **Metodika:** Třetí krok matice.
- **Normalizace:** per match · per 100 runs · per 30 min TIP
- **Pozor na:** Rozdíl mezi targeted a received je z velké části o kvalitě přihrávky, nikoliv běžce — nepřičítej ho automaticky hráči.

### `Count runs leading to shot per match` — Počet náběhů vedoucích ke střele

*počet*

Počet náběhů, kdy hráč přijal míč a *kterýkoli* hráč jeho týmu vystřelil během 10 sekund po přihrávce.

- **Metodika:** Čtvrtý krok matice. Okno je 10 s a autorem střely nemusí být běžec.
- **Normalizace:** per match · per 100 runs · per 30 min TIP
- **Pozor na:** Není to individuální zásluha — jde o týmový následek. Nečti to jako „hráč si vytvořil střelu“.

### `Count runs leading to goal per match` — Počet náběhů vedoucích ke gólu

*počet*

Počet náběhů, kdy hráč přijal míč a kterýkoli hráč jeho týmu skóroval během 10 sekund po přihrávce.

- **Metodika:** Pátý a poslední krok matice.
- **Normalizace:** per match · per 100 runs · per 30 min TIP
- **Pozor na:** Extrémně malá čísla a vysoký šum. Pro hodnocení hráče používej threat metriky, ne tuto.

### `Count runs in sample` — Počet náběhů ve vzorku

*počet*

Počet náběhů, které vstoupily do výpočtu metrik. Zásadní právě u průměrů — čím větší vzorek, tím důvěryhodnější hodnota.

- **Metodika:** Příklad ze zdroje: hráč odehrál 3 zápasy s 5, 10 a 6 náběhy za obranu → `Count runs in behind per match = 7`, `Count runs in behind in sample = 21`.
- **Pozor na:** První číslo, na které se má člověk podívat, a poslední, které se v reportech objevuje. Bez něj nelze rozhodnout, jestli je rozdíl mezi dvěma hráči reálný.

### `Dangerous run` — Nebezpečný náběh

Náběh, u kterého je aspoň 2% šance, že do 10 sekund padne gól, pokud by běžec dostal míč.

- **Metodika:** Prahová hodnota 2 % nad výstupem Threat modelu. Stejná definice se používá i u nebezpečných přihrávek.
- **Pozor na:** 2 % je nízký, ale nikoli nulový práh — „nebezpečný“ tu neznamená vyloženou šanci. Filtr dělí náběhy na dvě skupiny, nedává jim spojitou váhu; k tomu slouží threat metriky.

### `Count dangerous runs per match` — Počet nebezpečných náběhů na zápas

*počet*

Kolikrát hráč provedl nebezpečný náběh — tedy náběh s threatem nad 2 %.

- **Metodika:** Stejná sada metrik jako u běžných náběhů, jen filtrovaná na nebezpečné.
- **Normalizace:** per match · per 100 runs · per 30 min TIP
- **Pozor na:** Vertikální čtení matice (náběhy vs. nebezpečné náběhy) říká, jak selektivně hráč vybírá prostor. Horizontální čtení (náběhy vs. obsloužené) říká, jak ho tým používá.

### `Count dangerous runs targeted per match` — Nebezpečné náběhy, na které šla přihrávka

*počet*

Kolikrát hráč provedl nebezpečný náběh a byl adresátem přihrávky od hráče s míčem.

- **Metodika:** Filtrovaná varianta targeted metriky.
- **Normalizace:** per match · per 100 runs · per 30 min TIP
- **Pozor na:** Nízká hodnota při vysokém počtu nebezpečných náběhů ukazuje na problém v rozhodování spoluhráčů — doplň pohledem na jejich passing metriky.

### `Count dangerous runs completed per match` — Nebezpečné náběhy zakončené příjmem

*počet*

Kolikrát hráč provedl nebezpečný náběh a skutečně dostal míč.

- **Metodika:** Poslední krok filtrované varianty matice.
- **Normalizace:** per match · per 100 runs · per 30 min TIP
- **Pozor na:** Absolutní čísla jsou malá — u jednoho zápasu prakticky nepoužitelná, potřebuje větší vzorek.

### `Threat of runs per match` — Threat náběhů na zápas

*threat (0–1, součet)*

Součet threat hodnot spojených s náběhy, které hráč provedl. Odpovídá počtu gólů, které by vstřelil průměrný hráč, kdyby dostal míč při stejných nábězích.

- **Metodika:** Threat náběhu se odečítá jako průměr threatu za **poslední sekundu** náběhu. Model simuluje, co by se stalo po přijetí míče, s průměrnými hráči.
- **Normalizace:** per match · per 100 runs · per 30 min TIP
- **Pozor na:** Je to hodnota *nabídky*, ne realizace: threat vzniká i u náběhů, na které nikdo nepřihrál. Interpretuj jako „kolik nebezpečí hráč svým pohybem vytvořil“, ne „kolik gólů dal“.

### `Threat of runs targeted per match` — Threat obsloužených náběhů

*threat (součet)*

Součet threat hodnot náběhů, u kterých byl hráč adresátem přihrávky.

- **Metodika:** Filtruje threat na náběhy, kterých si spoluhráč všiml.
- **Normalizace:** per match · per 100 runs · per 30 min TIP
- **Pozor na:** Rozdíl mezi celkovým a obslouženým threatem kvantifikuje „propadlou“ hodnotu — kolik nebezpečí tým nechal nevyužité.

### `Threat of runs received per match` — Threat náběhů s příjmem míče

*threat (součet)*

Součet threat hodnot náběhů, při kterých hráč skutečně dostal míč.

- **Metodika:** Nejblíže reálnému dopadu ze všech threat variant.
- **Normalizace:** per match · per 100 runs · per 30 min TIP
- **Pozor na:** Pozor: pořád jde o modelovaný threat s průměrným hráčem, ne o skutečné xG hráče po přijetí míče.

### `Off-ball runs matrix` — Matice náběhů bez míče

Souhrnné uspořádání hlavních metrik: řádky odpovídají krokům situace (náběh → obsloužen → přijal → střela → gól), sloupce úrovni filtru (všechny náběhy vs. nebezpečné náběhy vs. threat).

- **Metodika:** Čtení **horizontálně** = kolik náběhů hráč udělal vs. kolikrát byl obsloužen. Čtení **vertikálně** = kolik náběhů celkem vs. kolik nebezpečných.
- **Pozor na:** Matice je hlavní nástroj interpretace celé sady. Jednotlivé metriky vytržené z matice se dají snadno přečíst opačně, než odpovídá realitě.

### `Rozpady a normalizace (náběhy)` — Filtry sady náběhů

Všechny metriky náběhů lze rozpadnout podle **typu náběhu**, **koridoru** a **třetiny hřiště**. Průměrovat lze per match, per 100 runs nebo per 30 min TIP.

- **Metodika:** Třetina a koridor se určují podle místa, **kde náběh končí** — ne kde začal a ne kde je hráč s míčem.
- **Pozor na:** Kombinace filtrů rychle drtí velikost vzorku: „nebezpečné náběhy za obranu do levého poloprostoru v útočné třetině“ může být pár událostí za sezónu.

### `Souběžné a navazující náběhy` — Zacházení s navazujícími náběhy

Když hráč běží a hráč s míčem přihraje někomu jinému, připíše se běžci jen **jeden** náběh, přiřazený k jedné držbě. Když hráč běží, zastaví a rozbíhá se znovu, připíšou se **dva** náběhy.

- **Metodika:** Pokud náběh během svého trvání projde více typy, připíše se hráči jen jeden náběh a typ se určí podle posledních 4 sekund. Dva náběhy téhož hráče v jedné držbě s odstupem pod 0,5 s se slučují do jednoho.
- **Pozor na:** Pravidlo posledních 4 sekund znamená, že náběh, který začal jako support run a skončil za obranou, se počítá jako in behind. To ovlivňuje profily hráčů, kteří mění záměr v průběhu pohybu.

## 9. Přihrávky na běžce

*Zrcadlová sada k náběhům, ale z pohledu hráče s míčem: jaké měl možnosti přihrát na běžícího spoluhráče a jak s nimi naložil.*

### `Count opportunities to pass per match` — Počet příležitostí přihrát na běžce

*počet*

Kolikrát měl hráč s míčem příležitost přihrát spoluhráči, který provádí náběh (daného typu).

- **Metodika:** První krok přihrávkové matice: příležitost → pokus → dokončeno → střela → gól.
- **Normalizace:** per match · per 100 runs · per 30 min TIP
- **Pozor na:** Když běží dva spoluhráči současně, je to jen **jedna** příležitost — hráč musí volit. Počet náběhů spoluhráčů je pro tu situaci 2. Nemíchej obě čísla.

### `Count pass attempts per match` — Počet pokusů o přihrávku na běžce

*počet*

Počet přihrávek, které hráč zkusil na spoluhráče v náběhu. Běžec je adresátem bez ohledu na to, zda přihrávka došla.

- **Metodika:** Druhý krok matice.
- **Normalizace:** per match · per 100 runs · per 30 min TIP
- **Pozor na:** Poměr attempts / opportunities je nejpřímější měřítko ochoty hráče hrát vertikálně. Nízká hodnota ale může být i taktický pokyn.

### `Count completed passes per match` — Počet dokončených přihrávek na běžce

*počet*

Počet přihrávek na spoluhráče v náběhu, které došly (běžec dostal míč).

- **Metodika:** Třetí krok matice.
- **Normalizace:** per match · per 100 runs · per 30 min TIP
- **Pozor na:** Nezaměňuj s Count runs received — to je totéž číslo z pohledu běžce, ne přihrávajícího.

### `Count completed passes leading to a shot per match` — Dokončené přihrávky vedoucí ke střele

*počet*

Počet dokončených přihrávek na běžce, po kterých kterýkoli hráč téhož týmu vystřelil během 10 sekund.

- **Metodika:** Čtvrtý krok matice, okno 10 s.
- **Normalizace:** per match · per 100 runs · per 30 min TIP
- **Pozor na:** Volnější kritérium než asistence. Nepřevádět na „vytvořené šance“.

### `Count completed passes leading to a goal per match` — Dokončené přihrávky vedoucí ke gólu

*počet*

Počet dokončených přihrávek na běžce, po kterých kterýkoli hráč téhož týmu skóroval během 10 sekund.

- **Metodika:** Pátý krok matice.
- **Normalizace:** per match · per 100 runs · per 30 min TIP
- **Pozor na:** Velmi malá čísla, silný šum. Pro srovnávání hráčů použij threat varianty.

### `Count opportunities to pass in sample` — Počet příležitostí ve vzorku

*počet*

Počet příležitostí přihrát, které vstoupily do výpočtu. Čím větší vzorek, tím důvěryhodnější hodnoty.

- **Metodika:** Analogie Count runs in sample na straně přihrávajícího.
- **Pozor na:** Vždy uveď společně s poměrovými metrikami — bez velikosti vzorku je „completion ratio“ nesrovnatelné.

### `Pass completion ratio` — Úspěšnost přihrávek na běžce

*%*

Procento přihrávek na spoluhráče v náběhu, které byly dokončeny.

- **Metodika:** Podíl Count completed passes a Count pass attempts.
- **Normalizace:** lze filtrovat podle typu náběhu a lokality
- **Pozor na:** Interpretuj vždy spolu s objemem a s obtížností. Vysoká úspěšnost při nízkém počtu pokusů na náběhy za obranu znamená bezpečnou volbu, ne kvalitu přihrávky.

### `Count runs made by teammates per match` — Počet náběhů spoluhráčů

*počet*

Počet náběhů, které spoluhráči provedli, když měl daný hráč míč.

- **Metodika:** Zavedeno právě proto, aby se odlišilo od „příležitosti přihrát“: dva souběžní běžci = 2 náběhy spoluhráčů, ale 1 příležitost.
- **Normalizace:** per match · per 100 runs · per 30 min TIP
- **Pozor na:** Užitečné jako kontext kvality nabídky, kterou hráč dostával. Hráč s malým počtem náběhů spoluhráčů nemá koho hledat.

### `Count opportunities to pass to dangerous runs` — Příležitosti přihrát na nebezpečný náběh

*počet*

Kolikrát měl hráč příležitost přihrát spoluhráči, který provádí nebezpečný náběh (threat nad 2 %).

- **Metodika:** Filtrovaná varianta první úrovně matice.
- **Normalizace:** per match · per 100 runs · per 30 min TIP
- **Pozor na:** Tohle je nejlepší vstup do otázky „hraje hráč rizikově, nebo bezpečně?“ — v kombinaci s pokusy na nebezpečné náběhy.

### `Count pass attempts for dangerous runs` — Pokusy o přihrávku na nebezpečný náběh

*počet*

Počet přihrávek zkoušených na spoluhráče v nebezpečném náběhu, bez ohledu na dokončení.

- **Metodika:** Filtrovaná varianta druhé úrovně matice.
- **Normalizace:** per match · per 100 runs · per 30 min TIP
- **Pozor na:** Poměr k příležitostem odděluje hráče, kteří nebezpečné náběhy vidí a hrají na ně, od těch, kteří je ignorují.

### `Count completed pass for dangerous runs` — Dokončené přihrávky na nebezpečný náběh

*počet*

Počet přihrávek dokončených na spoluhráče v nebezpečném náběhu.

- **Metodika:** Filtrovaná varianta třetí úrovně matice.
- **Normalizace:** per match · per 100 runs · per 30 min TIP
- **Pozor na:** Malá čísla — vyžaduje sezónní vzorek.

### `Threat of opportunities to pass per match` — Threat příležitostí přihrát

*threat (součet)*

Součet threat hodnot náběhů, které spoluhráči nabízeli. Když jsou dva náběhy současně, počítá se jen threat **nejpravděpodobnějšího** příjemce.

- **Metodika:** Pokud hráč skutečně na jednoho z běžců přihrál, považuje se za nejpravděpodobnějšího příjemce právě on. Threaty souběžných náběhů se nesčítají — hráč nemůže přihrát dvěma naráz.
- **Normalizace:** per match · per 100 runs · per 30 min TIP
- **Pozor na:** Toto je „dostupné nebezpečí“, které hráč měl k dispozici. Bez porovnání s pokusy a dokončenými přihrávkami neříká nic o rozhodování.

### `Threat of runs to which a pass was attempted` — Threat náběhů, na které šel pokus

*threat (součet)*

Součet threat hodnot náběhů, na které hráč zkusil přihrát.

- **Metodika:** Druhá úroveň threat varianty.
- **Normalizace:** per match · per 100 runs · per 30 min TIP
- **Pozor na:** Rozdíl proti threatu příležitostí měří „nevyužité nebezpečí“ — kolik hodnoty hráč nechal na stole.

### `Threat of runs to which a pass was completed` — Threat náběhů s dokončenou přihrávkou

*threat (součet)*

Součet threat hodnot náběhů, na které hráč přihrávku dokončil.

- **Metodika:** Třetí úroveň threat varianty.
- **Normalizace:** per match · per 100 runs · per 30 min TIP
- **Pozor na:** Nejblíže reálnému přínosu, ale stále modelovaná hodnota s průměrným hráčem — nikoli xA.

### `Passing matrix` — Přihrávková matice

Souhrnné uspořádání přihrávkových metrik podle kroků situace (příležitost → pokus → dokončeno → střela → gól) a podle filtru (všechny náběhy / nebezpečné / threat).

- **Metodika:** Horizontálně: kolikrát měl hráč příležitost vs. kolikrát ji zkusil využít. Vertikálně: kolik pokusů na náběhy celkem vs. kolik na nebezpečné náběhy.
- **Pozor na:** Zrcadlo matice náběhů. Ideální je čtení obou matic současně — jedna popisuje běžce, druhá toho, kdo ho má obsloužit.

### `Rozpady (přihrávky)` — Filtry přihrávkové sady

Metriky lze rozpadnout podle typu náběhu a podle lokality — přičemž lokalita je určena místem, **kde náběh končí**, ne kde stojí hráč s míčem.

- **Metodika:** K dispozici 3 třetiny a 5 koridorů. Průměrovat lze per match, per 100 runs nebo per 30 min TIP. U souběžných náběhů se pro určení lokality použije náběh nejpravděpodobnějšího příjemce.
- **Pozor na:** To, že lokalita popisuje cíl a ne zdroj přihrávky, je nejčastější nedorozumění celé sady. „Příležitosti v útočné třetině“ neznamená, že hráč byl v útočné třetině.

## 10. Hra pod tlakem

*Jak si hráč poradí, když je pod tlakem soupeře — udržení míče, přesnost přihrávek, ochota riskovat. Nahrazováno sadou On-Ball Engagements.*

Celá kategorie je označená jako **deprecated** — SkillCorner ji nahrazuje sadou On-Ball Engagements v rámci Game Intelligence V2. Textové definice nové sady ve veřejné knowledge base zatím nejsou, proto je tu zpracovaná ta původní.

### `Pressure (situace pod tlakem)` — Tlak

***DEPRECATED***

Hráč je pod tlakem, když má míč a aspoň jeden soupeř v jeho blízkosti se snaží míč získat nebo omezit jeho možnosti. Z jakéhokoli směru a při jakékoli rychlosti.

- **Metodika:** Vyloučeny jsou střely, hlavičkové a vzdušné duely, duely o volný míč (kdy míč nikdo nedrží) a situace končící faulem. Detekce běží přes LSTM model nad 15 framy (1,5 s) před každou událostí z Wyscoutu; model byl trénován na 8 000 příkladech obranných zapojení z EPL, Bundesligy, Serie A, La Ligy a rakouské Bundesligy.
- **Pozor na:** Detekce se váže na události z Wyscoutu, takže kvalita synchronizace je limitem. Sada Overcoming Pressure je označena jako deprecated — nahrazuje ji On-Ball Engagements v Game Intelligence V2.

### `Pressure intensity` — Intenzita tlaku

***DEPRECATED***

Tlak se dělí na tři úrovně: nízkou, střední a vysokou. Všechny metriky tlaku lze podle intenzity rozpadnout.

- **Metodika:** Určuje se kombinací čtyř faktorů: modelu detekce tlaku, rychlosti útočníka i obránce, jejich vzájemné vzdálenosti a úhlu. **Přímý (dopředný) tlak** = obránce zezpředu nebo ze strany (240°–360° a 0°–120°), **zpětný tlak** = zezadu (120°–240°). Prahy: přímý tlak vysoká intenzita při D &lt; 2,5 m; zpětný tlak vysoká intenzita při D &lt; 2 m. Prahy byly manuálně kalibrovány videoanalýzou.
- **Pozor na:** Nejdřív se rozhoduje, jestli tlak vůbec je, a teprve pak jeho intenzita. Pokud detekovaný tlak nesplní ani kritéria nízké intenzity, přestane se za tlak považovat vůbec — počty tlaků tedy nejsou nadmnožinou tří úrovní jen formálně, ale skutečně jejich součtem.

### `Count pressures received per match` — Počet přijatých tlaků

*počet · **DEPRECATED***

Kolikrát byl hráč s míčem pod tlakem.

- **Metodika:** Jmenovatel pro poměrové metriky tlaku.
- **Normalizace:** per match · per 30 min TIP · per 100 pressures
- **Pozor na:** Vysoké číslo je hlavně funkce role a stylu soupeře, ne kvality hráče. Používej jako kontext, ne jako hodnocení.

### `Count forced losses under pressure per match` — Vynucené ztráty pod tlakem

*počet · **DEPRECATED***

Kolikrát hráč pod tlakem ztratil míč — nedokončená přihrávka, prohraný duel, špatný dotek vedoucí ke ztrátě, míč do zámezí.

- **Metodika:** Jeden ze dvou možných konců každé tlakové situace (druhý je udržení míče).
- **Normalizace:** per match · per 30 min TIP · per 100 pressures
- **Pozor na:** Absolutní počty jsou svázané s objemem tlaků. Pro srovnání hráčů použij poměr udržení míče.

### `Count ball retentions under pressure per match` — Udržení míče pod tlakem

*počet · **DEPRECATED***

Kolikrát tým hráče pod tlakem udržel míč — včetně případů, kdy hráč pod tlakem dokončil přihrávku spoluhráči nebo si míč udržel vedením.

- **Metodika:** Druhý možný konec tlakové situace.
- **Normalizace:** per match · per 30 min TIP · per 100 pressures
- **Pozor na:** Pozor na formulaci: udržení se hodnotí na úrovni **týmu**, ne hráče. Přihrávka spoluhráči se počítá jako udržení.

### `Ball retention ratio under pressure` — Podíl udržení míče pod tlakem

*% · **DEPRECATED***

Procento tlakových situací, ve kterých byl míč udržen. Podíl Count ball retentions a Count pressures received.

- **Metodika:** Nejpoužívanější poměrová metrika sady.
- **Normalizace:** lze rozpadnout podle intenzity tlaku a lokality
- **Pozor na:** Sama o sobě zavádí: hráč, který pod tlakem vždycky hraje zpět na stopera, bude mít výborný poměr. Vždy čti spolu s metrikami nebezpečnosti a obtížnosti přihrávek.

### `Count pass attempts under pressure per match` — Pokusy o přihrávku pod tlakem

*počet · **DEPRECATED***

Kolikrát se hráč pod tlakem pokusil přihrát spoluhráči.

- **Metodika:** Vstup do hodnocení přihrávkových schopností pod tlakem.
- **Normalizace:** per match · per 30 min TIP · per 100 pressures
- **Pozor na:** Nezaměňuj s tlaky celkem — hráč může pod tlakem míč i vést, obejít, ztratit či poslat do zámezí.

### `Count completed passes under pressure per match` — Dokončené přihrávky pod tlakem

*počet · **DEPRECATED***

Kolikrát hráč pod tlakem dokončil přihrávku spoluhráči.

- **Metodika:** Čitatel pro úspěšnost přihrávek pod tlakem.
- **Normalizace:** per match · per 30 min TIP · per 100 pressures
- **Pozor na:** Bez rozdělení podle intenzity tlaku má omezenou výpovědní hodnotu — nízký tlak a vysoký tlak jsou jiné úkoly.

### `Pass completion ratio under pressure` — Úspěšnost přihrávek pod tlakem

*% · **DEPRECATED***

Procento přihrávek pod tlakem, které hráč dokončil. Podíl dokončených a zkoušených přihrávek pod tlakem.

- **Metodika:** Poměrová metrika, ideální rozpadnout podle intenzity tlaku.
- **Normalizace:** lze rozpadnout podle intenzity a lokality
- **Pozor na:** Stejná past jako u poměru udržení míče: bezpečné volby zvyšují procento. Doplň o podíl nebezpečných a obtížných přihrávek.

### `Dangerous pass` — Nebezpečná přihrávka

***DEPRECATED***

Přihrávka na hráče, u které je při dokončení více než 2% šance na gól do 10 sekund.

- **Metodika:** Vyhodnocuje se pomocí SkillCorner xThreat modelu. Stejný 2% práh jako u nebezpečných náběhů.
- **Pozor na:** „Nebezpečná“ zde neznamená riskantní, ale hodnotnou. Riskantnost popisuje obtížná přihrávka (difficult pass) — to jsou dvě různé osy.

### `Difficult pass` — Obtížná přihrávka

***DEPRECATED***

Přihrávka s pravděpodobností dokončení pod 65 %.

- **Metodika:** Pravděpodobnost dokončení určuje SkillCorner xPass model (grafová neuronová síť).
- **Pozor na:** Obtížná ≠ nebezpečná. Přihrávka může být obtížná a bezcenná (dlouhý nákop do tlaku) i snadná a nebezpečná (krátká do vápna).

### `Count dangerous pass attempts under pressure per match` — Pokusy o nebezpečnou přihrávku pod tlakem

*počet · **DEPRECATED***

Kolikrát hráč pod tlakem zkusil přihrávku, u níž by při dokončení byla šance na gól do 10 s nad 2 %.

- **Metodika:** Filtrovaná varianta pokusů o přihrávku.
- **Normalizace:** per match · per 30 min TIP · per 100 pressures
- **Pozor na:** Toto je metrika ochoty riskovat pro hodnotu. Nízká čísla u hráče s vysokou úspěšností přihrávek pod tlakem popisují bezpečného distributora.

### `Count dangerous passes completed under pressure per match` — Dokončené nebezpečné přihrávky pod tlakem

*počet · **DEPRECATED***

Kolikrát hráč pod tlakem dokončil nebezpečnou přihrávku.

- **Metodika:** Čitatel pro úspěšnost nebezpečných přihrávek pod tlakem.
- **Normalizace:** per match · per 30 min TIP · per 100 pressures
- **Pozor na:** Malý objem — vyžaduje větší vzorek zápasů.

### `Dangerous pass completion ratio under pressure` — Úspěšnost nebezpečných přihrávek pod tlakem

*% · **DEPRECATED***

Procento nebezpečných přihrávek pod tlakem, které byly dokončeny.

- **Metodika:** Podíl dokončených a zkoušených nebezpečných přihrávek pod tlakem.
- **Pozor na:** Vysoká hodnota při velmi malém počtu pokusů není kvalita, ale šum. Bez čitatele a jmenovatele nečti.

### `Count difficult pass attempts under pressure per match` — Pokusy o obtížnou přihrávku pod tlakem

*počet · **DEPRECATED***

Kolikrát hráč pod tlakem zkusil přihrávku s pravděpodobností dokončení pod 65 %.

- **Metodika:** Filtrovaná varianta pokusů podle výstupu xPass modelu.
- **Normalizace:** per match · per 30 min TIP · per 100 pressures
- **Pozor na:** Druhá osa profilu hráče pod tlakem. Spolu s nebezpečnými přihrávkami tvoří čtyři typy profilů (bezpečný/riskující × hodnotný/nehodnotný).

### `Count difficult passes completed under pressure per match` — Dokončené obtížné přihrávky pod tlakem

*počet · **DEPRECATED***

Kolikrát hráč pod tlakem dokončil obtížnou přihrávku.

- **Metodika:** Čitatel pro úspěšnost obtížných přihrávek pod tlakem.
- **Normalizace:** per match · per 30 min TIP · per 100 pressures
- **Pozor na:** Nejzajímavější metrika sady pro hledání hráčů, kteří „umí ven z tlaku“ — ale nejmenší vzorky.

### `Difficult pass completion ratio under pressure` — Úspěšnost obtížných přihrávek pod tlakem

*% · **DEPRECATED***

Procento obtížných přihrávek pod tlakem, které byly dokončeny.

- **Metodika:** Podíl dokončených a zkoušených obtížných přihrávek pod tlakem.
- **Pozor na:** Protože se do jmenovatele počítají jen přihrávky s modelovanou úspěšností pod 65 %, hodnota nad 65 % znamená, že hráč překonává očekávání modelu.

## 11. Modely a koncepty

*Modely, ze kterých ostatní metriky vycházejí: Threat, xPass, Receiver, detekce tlaku, klasifikace náběhů, prolomení linií, predikce zátěže.*

### `Threat / xThreat` — Threat (hrozba)

*0–1*

Pravděpodobnost, že útočící tým skóruje během následujících 10 sekund, pokud by daný hráč dostal přihrávku od hráče s míčem.

- **Metodika:** Grafová neuronová síť. Vstupy: pozice a pohyb hráčů i míče (rychlost, úhel) a interakce mezi hráči (vzájemné vzdálenosti a úhly, příslušnost k týmu). Trénováno na milionech přihrávkových situací s cílem, zda do 10 s padl gól.
- **Pozor na:** Tři důležité věci: (1) threat lze spočítat, i když hráč míč nedostal — je to kontrafaktuál. (2) Není o tom, že hráč sám skóruje, ale že skóruje jeho **tým**. (3) Není to asistence ani xA. U náběhů se bere průměr threatu za poslední sekundu náběhu.

### `Passing option score` — Skóre přihrávkové možnosti

*PO score · 0–1*

Standardizované skóre pravděpodobnosti, že hráč bude adresátem přihrávky v daném framu. Nad 0,6 se hráč považuje za přihrávkovou možnost.

- **Metodika:** Receiver Model (grafová neuronová síť) zohledňuje pozici a pohyb hráče i míče a interakce mezi hráči. Trénováno na milionech přihrávkových situací s cílem, kdo byl adresátem přihrávky.
- **Pozor na:** Někteří hráči blízko míče se přihrávkovou možností nestanou, protože v průměru na ně hráč s míčem nehraje. Passing Option event se ale vytvoří vždy, když byl hráč přihrávkou adresován — bez ohledu na skóre.

### `xPass completion` — Pravděpodobnost dokončení přihrávky

*0–1*

Pravděpodobnost dokončení přihrávky na daného hráče v daném framu.

- **Metodika:** Grafová neuronová síť. Používá se pro atributy `xpass_completion`, `difficult_target` a `player_targeted_difficult`.
- **Pozor na:** Práh pro „obtížnou“ přihrávku je pod 65 %. Model hodnotí obtížnost přihrávky, ne její užitečnost — tu popisuje threat.

### `Passing Moment` — Okamžik přihrávky

Pro každou přihrávkovou možnost a náběh se určuje hodnota `passing_option_score`, `xthreat`, `xpass_completion` a příležitost k prolomení linie. Když hráč přihrávku dostal, počítají se v okamžiku přihrávky. Když nedostal, počítají se v teoretickém okamžiku přihrávky.

- **Metodika:** Okamžik přihrávky je frame, který — při `passing_option_score` nad 0,6 — maximalizuje součin `passing_option_score × xthreat × xpass_completion`. Maximalizuje se tedy potenciální hrozba, vážená pravděpodobností, že hráč míč skutečně dostane. Frame se dodává jako `peak_passing_option_frame`.
- **Pozor na:** Zásadní pro pochopení všech metrik u neobsloužených náběhů. Hodnoty nejsou „průměr přes náběh“, ale hodnoty v nejlepším možném momentě — mají tendenci být optimistické.

### `Run classification model` — Klasifikace typu náběhu

LSTM model, který každý detekovaný náběh zařadí do jednoho z 10 typů. Výsledek se dodává v atributu `event_subtype`.

- **Metodika:** Typ se určuje podle **posledních 4 sekund** náběhu.
- **Pozor na:** Náběh nemůže mít dva typy. Pohyb, který přejde z jednoho charakteru do druhého, dostane typ podle konce — to zkresluje profily hráčů s proměnlivým záměrem.

### `Pressure detection model` — Model detekce tlaku

Model, který u každé události na hřišti rozhoduje, zda některý obránce vyvíjí tlak na hráče s míčem.

- **Metodika:** LSTM. Prochází každého obránce a používá 15 framů (1,5 s) před událostí. Vstupy: X, Y, rychlost a úhel pohybu hráče s míčem i obránce, vzdálenost a úhel k brance, vzájemný úhel a vzdálenost, hloubka a výška týmu (bez brankáře). Trénováno na 8 000 příkladech z pěti lig.
- **Pozor na:** Tlak je definován široce: aktivní dostupování, už blízké krytí/sledování, i obránce držící pozici, na kterého útočník najíždí s míčem. Nečekej, že to odpovídá tomu, co bys sám nazval „presink“.

### `Line Breaking Passes` — Přihrávky prolamující linie

U každé přihrávkové možnosti (i neobsloužené) se dodává informace, zda a jaká obranná linie byla (mohla být) prolomena — a jak: skrz, nebo okolo.

- **Metodika:** Postup: (1) rozpozná se obranná struktura podle šablon (11 nebo 10 bránících hráčů; při dvou chybějících se struktura nedetekuje), (2) model rozhodne, zda je obrana organizovaná — atribut `organised_defense` vyřazuje brejky a chaotické fáze, (3) linie = blok 2 a více hráčů struktury; poslední linie je nejblíž vlastní brance, (4) prolomení se určuje podle pozice míče vůči linii ve framu přihrávky a v okamžiku příjmu, (5) ML model odfiltruje nerelevantní prolomení (příliš velký úhel obejití, obcházení mezi hráči 30 m od sebe, velmi krátké přihrávky). U neobsloužených možností se trajektorie odvozuje z rychlosti a směru hráče; validace na skutečných přihrávkách dosáhla přesnosti 95 %.
- **Pozor na:** Linie není vodorovná přímka, ale lomená čára kopírující rozestavení — prolomení tedy neznamená obejití nejhlubšího obránce. SkillCorner navíc **nepredikuje**, zda by přihrávka šla nad linii. Dodává jen příznak `high_pass` (míč dosáhl aspoň 1,8 m); u nedokončených přihrávek může být `high_pass` jen True nebo None, nikdy False.

### `Forward momentum` — Dopředná dynamika

Zachycuje hráče, kteří akcí kolem prvního doteku vytvoří progresivní výsledek — typicky se otočí dopředu a rychle vyrazí.

- **Metodika:** Podmínky: hráč dostal přihrávku zezadu nebo ze strany, v momentě prvního doteku je soupeř blíž než 6 metrů, a držba začíná v centrálním koridoru nebo v poloprostoru.
- **Pozor na:** Nezachycuje se u držeb začínajících v krajních koridorech — pro krajní hráče je tedy metrika strukturálně nedostupná.

### `Physical Load Prediction Model` — Model predikce fyzické zátěže

Extrapolační model, který z nesouvislých tracking dat (hráč je vidět jen část času) predikuje fyzické výstupy za celý zápas, rozdělené na TIP a OTIP.

- **Metodika:** Tracking běží na 10 Hz. Nejprve se z viditelných framů spočítají hodnoty se vyhlazením a kontrolními algoritmy, které odstraní nekoherentní rychlosti a zrychlení. Tyto hodnoty jsou systematicky nižší než realita, takže se dotrénuje regresní model. Vstupní příznaky: viditelnost, počet framů s hráčem, pozice hráče, odehraný čas, podíl hlavní vs. jiné kamery v době neviditelnosti, metriky ostatních hráčů v té době ad. Model se aplikuje na každé období zvlášť. Trénováno na oficiálních datech.
- **Pozor na:** Model je nastavený na výkony **nad 70 minut**. Validita: nad 90 min vysoká, nad 45 min dobrá, 30–45 min přijatelná, **pod 30 min se nedoporučuje**. Střídající hráči jsou pro model odlehlé hodnoty, protože v krátkém čase dosahují neobvykle vysoké zátěže. PSV-99 se neextrapoluje vůbec.

## 12. Eventy a geometrie

*Dynamické eventy (Player Possession, Passing Option, Off-Ball Run), souřadnicový systém, rychlostní pásma, směry a zóny hřiště.*

### `Player Possession` — Držba hráče

*PP*

Aktivita se považuje za držbu hráče, když má hráč míč pod kontrolou — tedy je schopen přihrát, vystřelit nebo míč vést. Trvá od prvního po poslední dotek.

- **Metodika:** Držba na jediný frame se nazývá one-touch. Zachycení míče bez následné kontroly (například blok) se za držbu nepočítá.
- **Pozor na:** Držba hráče je zastřešující event: každá přihrávková možnost a každý náběh patří přesně k jedné držbě. Event může začít před ní a skončit po ní, ale nikdy nesmí zasahovat do dvou držeb.

### `Passing Option (event)` — Přihrávková možnost

*PO*

Event vzniká, když je hráč vysoce pravděpodobným adresátem přihrávky (passing option score nad 0,6) a stav trvá aspoň 0,3 s.

- **Metodika:** Event se vytvoří i tehdy, když byl hráč přihrávkou adresován bez ohledu na skóre — pak trvá 0,3 s a končí framem přihrávky. U one-touch přihrávek se okno pro určení možností rozšiřuje o dva framy před a dva framy po prvním doteku.
- **Pozor na:** Detekuje se jen během držby hráče, takže **u standardek a rozehrávek se nedetekuje**. Když je hráč přihrávkovou možností přes několik navazujících držeb, vznikne několik samostatných eventů — jeden na každou držbu.

### `Relationship between events` — Vztahy mezi eventy

Každá přihrávková možnost i každý náběh patří k právě jedné držbě hráče. Každý náběh je navíc svázaný s právě jednou přihrávkovou možností — aby byl náběh zaznamenán, musel se hráč během něj aspoň v jednom momentě stát přihrávkovou možností.

- **Metodika:** Pokud hráč s míčem přihrával, event držby odkazuje na adresovanou přihrávkovou možnost. Event držby zároveň agreguje a odkazuje mnoho datových bodů o možnostech a náběžích, které během ní nastaly.
- **Pozor na:** Dvě přihrávkové možnosti (nebo dva náběhy) téhož hráče v jedné držbě s odstupem pod 0,5 s se slučují do jedné. U eventů kratších než 5 framů se pro výpočet rychlostí a úhlů použije posledních 5 framů před koncem eventu.

### `Pitch coordinates` — Souřadnice hřiště

Střed hřiště má souřadnice (0,0), jednotkou je metr. Osa x je delší strana, osa y kratší. Rozměry lze získat z `GET /api/match` — `pitch_length` je delší strana, `pitch_width` kratší.

- **Metodika:** Všechny atributy závislé na orientaci (kromě `attacking_side` a `attacking_side_id`) se dodávají tak, jako by tým v držení míče útočil zleva doprava. Souřadnice týmu, který v daném období útočí zprava doleva, se zrcadlí.
- **Pozor na:** Zrcadlení se dělá pro každé období zvlášť. Když si data zpracováváš sám, nedělej normalizaci směru útoku dvakrát.

### `Pitch zones (thirds & channels)` — Zóny hřiště

Hřiště se dělí na 3 třetiny (obranná, střední, útočná) a 5 koridorů (levý krajní, levý poloprostor, centrální, pravý poloprostor, pravý krajní).

- **Metodika:** Používá se pro rozpady metrik náběhů, přihrávek i tlaku.
- **Pozor na:** U náběhů a přihrávek se zóna určuje podle místa, kde náběh **končí**. U tlaku podle místa, kde tlaková situace nastane. Nejde tedy o stejnou logiku napříč sadami.

### `speed_avg / speed bands` — Průměrná rychlost a rychlostní pásma

*km/h*

Každý event má atribut průměrné rychlosti. Pásma: `None` (bez hodnoty), `jogging` (pod 15 km/h), `running` (15–20), `hsr` (20–25), `sprinting` (nad 25).

- **Metodika:** Pro výpočet je potřeba aspoň 5 framů s detekovaným hráčem, plus filtrace proti nepřesnostem. Pokrytí v ukázkovém zápase: držby hráče 91,6 %, přihrávkové možnosti 71,2 %, náběhy 97,9 %.
- **Pozor na:** Průměrná rychlost **není** `distance_covered` dělená dobou eventu — u one-touch by to nešlo, `distance_covered` zahrnuje i extrapolované úseky (rychlost jen detekované framy) a navíc se aplikují filtry. Prázdná hodnota je běžná zvlášť u přihrávkových možností, kdy je hráč mimo záběr.

### `Pass range` — Délková kategorie přihrávky

Vzdálenost přihrávky se kategorizuje jako **short** (pod 15 m), **medium** (15–30 m) a **long** (nad 30 m).

- **Metodika:** Stejná kategorizace se rozšiřuje i na vzdálenost mezi dvěma hráči.
- **Pozor na:** Hranice jsou fixní a nezávislé na kontextu — 16 m přes vápno a 16 m napříč vlastní polovinou jsou obojí „medium“.

### `Angles and Directions` — Úhly a směry

Úhly jsou ve stupních, převážně relativně ke směru útoku, na kružnici od −180° do 180° (proti směru hodinových ručiček). **Dopředu** −45° až +45°, **dozadu** pod −135° nebo nad 135°, **do strany vlevo** 45° až 135°, **do strany vpravo** −135° až −45°.

- **Metodika:** Definice směru je vždy relativní ke směru útoku, ne k absolutní orientaci hřiště.
- **Pozor na:** Kategorie jsou po 90°, takže „dopředu“ zahrnuje i výrazně diagonální pohyb. Pro jemnější analýzu použij surový úhel.

### `Ahead / Same line / Behind` — Před / na úrovni / za

U atributů typu `location_to_player_in_possession_start`: **Ahead** = hráč je aspoň 3 m před hráčem s míčem po ose x, **Same Line** = mezi 3 m za a 3 m před, **Behind** = aspoň 3 m za.

- **Metodika:** Měří se výhradně po ose x (podél delší strany hřiště).
- **Pozor na:** Pásmo „Same Line“ je 6 m široké — dva hráči označení jako na stejné úrovni mohou být od sebe skoro 6 metrů.

### `Dynamic Events (kvalita)` — Dynamické eventy — podmínky dodání

Dynamické eventy se generují z SkillCorner Tracking v3 a dodávají se jen u zápasů, které mají index kvality nad 4 pro hráče i pro míč a u kterých se podařilo spárovat dostatečný počet Wyscout eventů s trackingem.

- **Metodika:** Kvalita závisí na kvalitě videa (detailní záběry, opakované záběry, hráči mimo záběr), umístění kamery a podmínkách na stadionu a na schopnosti detekovat hráče, míč a čísla na dresech. U každého eventu se reportuje, zda se podařilo spárovat začátek držby, její konec, předchozí přihrávku a příjem další přihrávky. Párování se dělá podle vzdálenosti hráče od míče.
- **Pozor na:** Atributy jako `speed_avg`, souřadnice, `passing_option_score`, `xthreat` nebo `xpass_completion` mohou být prázdné — buď kvůli nedostatku informace (u velmi dlouhého detailního záběru se tracking po 10 s nedodává), nebo kvůli nízké důvěře v hodnotu.

## 13. Normalizace a průměrování

*Jak se hodnoty agregují přes více zápasů. Volba normalizace mění výsledné pořadí hráčů víc než většina lidí očekává.*

Tahle kategorie rozhoduje o tom, jestli srovnání hráčů dává smysl. Detailně [[Normalizace herních dat]].

### `Averaging per match` — Průměr na zápas

Průměr hodnot metriky přes zápasy, které vstupují do výpočtu. Do výpočtu vstupují **jen výkony, které prošly kontrolou kvality**.

- **Metodika:** Příklad ze zdroje: 3 zápasy s 10, 20 a 20 náběhy → `Count Runs per Match = (10+20+20)/3 = 16,7`.
- **Pozor na:** Při jediném zápase ve vzorku k žádnému průměrování nedochází — hodnota je prostě hodnota toho zápasu. Průměr na zápas ignoruje odehraný čas, takže znevýhodňuje hráče, kteří často střídají.

### `Averaging per 100 events` — Průměr na 100 událostí

Hodnota metriky na jednu událost, vynásobená stem. Událostí může být náběh, tlaková událost nebo příležitost přihrát.

- **Metodika:** Příklad: 3 zápasy s 10/20/20 náběhy a 4/3/10 nebezpečnými náběhy → `Count Dangerous Runs per 100 runs = 17/50 × 100 = 34`. Když filtruješ na část hřiště nebo typ náběhu, aplikují se stejné filtry i na těch 100 událostí.
- **Pozor na:** Když se metrika normalizuje přes tu samou událost, kterou počítá, výsledek je vždy 100 — `Count Runs per 100 runs = 100`. To je znak špatně zvolené normalizace, ne zjištění.

### `Averaging per minutes` — Průměr na minuty

Podle metriky lze průměrovat per 90 minut, per 30 minut v držení míče (TIP), nebo per 30 minut bez míče (OTIP).

- **Metodika:** Součet hodnot dělený součtem minut, vynásobený cílovým počtem minut. Příklad: 3 zápasy, 50 náběhů, 257 minut → `Count Runs per 90 = 50/257 × 90 = 17,5`. Při 73 minutách TIP → `per 30 min TIP = 50/73 × 30 = 20,5`.
- **Pozor na:** Volba jmenovatele mění pořadí hráčů. Per 30 min TIP je pro metriky náběhů a přihrávek správnější než per 90, protože odstraňuje vliv toho, jak dlouho tým drží míč.

### `P90 (Per 90)` — Přepočet na 90 minut

Normalizace fyzických výstupů na 90 minut, aby se vyrovnaly rozdíly v odehraném čase.

- **Metodika:** Pro více zápasů se metriky **nejprve sečtou** a pak se dělí **součtem minut** — nikoli tak, že by se počítala P90 hodnota pro každý zápas a ty se pak zprůměrovaly. SkillCorner považuje první postup za reprezentativnější.
- **Pozor na:** Ve Web Appu je P90 přepínač, který se dá zapnout před stažením dat. **V API P90 logika aktivní není** — uživatelé API si ji musí implementovat sami, a měli by použít stejné pořadí operací (sečti, pak vyděl).

### `Average Calculations (specifičnost výběru)` — Specifičnost výběru u průměrů

Průměry se musí zakotvit ve konkrétní soutěži, sezóně nebo klubu, jinak se počítají přes všechny odehrané soutěže.

- **Metodika:** Když vybereš hráče bez soutěže nebo klubu, průměr zahrne všechny soutěže — domácí ligu, evropské poháry i mezinárodní turnaje. Výběr konkrétní soutěže průměr automaticky omezí na ni.
- **Pozor na:** Nejčastější tichá chyba v reportech: srovnávání hráče s daty z Ligy mistrů proti hráči s daty jen z domácí ligy. Vždy aktivně vybírej sezónu, soutěž, tým a skupinu pozic.

### `P900 (team level)` — Přepočet na 900 minut (tým)

Pro reportování agregovaných týmových dat (bez brankářů) SkillCorner doporučuje relativní přístup per 900 minut.

- **Metodika:** 900 minut = 10 hráčů × 90 minut. Zohledňuje jak rozdílnou délku zápasů, tak fakt, že data některých hráčů nemusí být dostupná kvůli neúspěšné kontrole kvality.
- **Pozor na:** Bez P900 týmové součty systematicky podhodnocují týmy, kterým vypadli hráči z QC. Brankáře do výpočtu nezahrnuj.

## Poznámky ke zdroji

**Známá mezera:** textové definice metrik **On-Ball Engagements** nejsou ve veřejné knowledge base k dispozici — je tam jen video a přehledový dokument za přihlášením. Deprecated sada Overcoming Pressure, kterou nahrazují, je zpracovaná kompletně a je označená.

**Zdroje:** [Glossaries](https://skillcorner.crunch.help/en/glossaries), [Physical metrics](https://skillcorner.crunch.help/en/glossaries/physical-data-glossary), [Peak Sprint Velocity](https://skillcorner.crunch.help/en/glossaries/peak-sprint-velocity), [Running off-ball metrics](https://skillcorner.crunch.help/en/glossaries/running-off-ball-metrics-1), [Passing to Runners](https://skillcorner.crunch.help/en/glossaries/passing-metrics-1), [Overcoming Pressure](https://skillcorner.crunch.help/en/glossaries/overcoming-pressure), [Run types](https://skillcorner.crunch.help/en/getting-started/run-detection-and-classification), [Threat](https://skillcorner.crunch.help/en/models-general-concepts/threat), [Pressure detection](https://skillcorner.crunch.help/en/models-general-concepts/pressure-detection), [Physical Load Prediction](https://skillcorner.crunch.help/en/models-general-concepts/physical-load-prediction-model), [Averaging](https://skillcorner.crunch.help/en/working-with-the-data/averaging-per-match-per-events-or-per-min), [Pitch modelisation](https://skillcorner.crunch.help/en/working-with-the-data/pitch-modelisation), [Player positions](https://skillcorner.crunch.help/en/working-with-the-data/physical-data-glossary-1-1).

## Souvislosti

- [[SkillCorner]] – wiki stránka o SkillCorneru jako zdroji: co to je, datové sady, k čemu to v Sigmě používáme. Tahle poznámka je její detailní datový protějšek.
- [[Wyscout – slovník metrik]] – stejný typ slovníku pro druhý hlavní zdroj. Wyscout dává event data, SkillCorner tracking; metriky stejného jména v nich často znamenají něco jiného.
- [[Wyscout]] – wiki stránka o Wyscoutu.
- [[Normalizace herních dat]] – per 90 a per 30 TIP/OTIP. Tahle poznámka k tomu dodává, které metriky se kterou normalizací vůbec dají počítat a proč u náběhů TIP poráží per 90.
- [[📊 Fotbalová zápasová data]] – tři pohledy na data (průměr na zápas, 30 min TIP, 100 situací) pocházejí právě ze SkillCorneru; tady je k nim metodika.
- [[📡 GPS Data]] – fyzická data z GPS. SkillCorner je měří z videa a extrapoluje na celý zápas, takže metriky stejného jména (HSR, sprint, akcelerace) mají jiný původ i jiné prahy.
- [[Expected goals (xG)]] – pro srovnání s konceptem Threat, který měří něco jiného: šanci týmu na gól do 10 s, pokud by hráč dostal míč.
- [[Datový skauting – metriky a úskalí]] – proč metriky samy nestačí.
- [[Skauting – proces a reporting]] – postové thresholdy stojí hlavně na těchhle metrikách.
- [[Aplikace – Analýza soupeře]] – aplikace, která SkillCorner data konzumuje.
- [[Karta hráče 🎯]] – cílové místo, kde se metriky zobrazují hráčům a trenérům.
- [[🥅 Brankářská data]] – SkillCorner brankářské metriky nepokrývá, doplňuje je Wyscout.

## Otevřené body

- [ ] Doplnit On-Ball Engagements, až SkillCorner zveřejní textové definice (zatím jen video a dokument za přihlášením).
- [ ] Sjednotit, které normalizace používáme my — per 30 TIP vs. per 90 — a zapsat to do [[Normalizace herních dat]] jako závazné pravidlo.
- [ ] Ověřit, jestli u mládeže (U17/U19) platí mužské prahy, nebo je potřeba vlastní sada.

