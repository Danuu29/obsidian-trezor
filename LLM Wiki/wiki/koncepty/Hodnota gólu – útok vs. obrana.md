---
typ: koncept
tags: [goly, body, utok, obrana, hodnoceni, utocnici, obranci]
zdroje: ["[[Zdroj – The Numbers Game]]"]
aktualizovano: 2026-10-15
---
# Hodnota gólu – útok vs. obrana

Kolik bodů má gól vstřelený a gól, který tým nedostal. Góly nemají stejnou cenu: záleží na tom, kolikátý gól v zápase je. **Gól, který tým nedostane, je v průměru cennější než gól vstřelený** – v knize zkratka **0 > 1** ([[Zdroj – The Numbers Game]], Kap. 2–4).

## Góly jsou vzácné

- Tým PL vstřelí v **63 %** zápasů nejvýš jeden gól a ve **30 %** žádný.
- PL 2008–2011: 91,6 % startů hráčů skončilo bez gólu, 56 % bez jediné střely; čtvrtina hráčů za tři sezóny nevystřelila ani jednou.
- Fotbal je ze všech kolektivních sportů nejméně gólový: tým skóruje průměrně jednou za **69 minut** (americký fotbal 9, ragby 12,5, hokej 22) a vystřelí ~12× za zápas (hokej 30, basketbal 123). Finále LM 2010: 2 góly z 2 842 událostí Opty.

## Směnný kurz gólů na body

Body na zápas podle počtu vstřelených gólů (top 4 ligy 2000–2011) mají tvar **S-křivky**:

| Vstřelené góly | Co to obvykle znamená |
|---|---|
| 0 | občas bod (7–8 % zápasů končí 0:0) |
| 1 | v průměru bod, výhra jen asi v 1 ze 4 případů |
| 2 | **víc výher než proher** – nejcennější gól (+0,99 bodu) |
| 3–4 | skoro jistá výhra |
| 5+ | výhra; pátý gól přidá ~0,1 bodu |

- Kurz je ve všech top ligách skoro stejný.
- Jeden gól na zápas (38 za sezónu) v PL historicky stačil na záchranu.
- Platí i obráceně: **druhý obdržený gól je nejdražší**.

## Marginální body útočníků

Sečíst každému hráči body, které jeho góly podle pořadí v zápase přinesly („marginal points contribution“), místo prostého počtu gólů (data Opta, PL 2009–2011):
- Drogba (král střelců 2009/10) byl v bodech až třetí, Berbatov 2010/11 čtvrtý – dávali góly, když už tolik nerozhodovaly.
- **Darren Bent** byl nejkonzistentnější: 2009/10 jeho góly tvořily **45,5 % bodů Sunderlandu**. Autoři: Chelsea měla v lednu 2011 koupit Benta za polovinu ceny místo Torrese za 50 mil. £.
- Saha (13 gólů) přinesl Evertonu skoro tolik bodů jako Defoe (18) Tottenhamu.

## Útok vs. obrana (PL 2001–2011)

- Tým s nejvíc vstřelenými góly vyhrál ligu v **51 %** sezón (top 4 ligy, 20 let), tým s nejlepší obranou ve **46 %**. Jen 16 z 80 mistrů byl nejlepší na obou koncích.
- Regrese (vliv útoku při stejné obraně a naopak):

| +10 gólů za sezónu | Výhry | Prohry |
|---|---|---|
| vstřelených | +2,30 | −1,76 |
| neobdržených | +2,16 | **−2,35** |

→ Pro výhry jsou útok a obrana zhruba stejně důležité; pro **vyhýbání se porážkám je neobdržený gól o 33 % cennější**.
- **Čisté konto ≈ 2,5 bodu** za zápas, jeden vstřelený gól ≈ 1 bod, jeden obdržený gól ≈ 1,5 bodu. Čisté konto má skoro stejnou bodovou hodnotu jako dva vstřelené góly.

## Proč obranu podceňujeme

- Útok spojujeme s radostí a vítězstvím, obranu s negací (Menotti: „levicový“ vs. „pravicový“ fotbal); útočníci vyhrávají Zlaté míče a dostávají víc peněz.
- **Princip Maldini – „psi, kteří neštěkají“:** nejlepší obránci skoro nemusí zakročit, protože stojí správně (Maldini podle Fordea jeden skluz za dva zápasy). Lidé hůř vnímají to, co se nestalo. **Ferguson prodal Stama** (2001) mimo jiné proto, že v datech dělal méně skluzů – později to označil za svou největší chybu.
- Xabi Alonso: skluz je poslední možnost, ne kvalita, kterou by se měl hráč učit.
- Defenzivní data jsou primitivnější než útočná – v každém sportu (Bill James).

> [!note] Souvislost se Soccermatics
> Sumpter došel modelem ke stejnému závěru z jiné strany: při 3 bodech za výhru se slabšímu týmu vyplatí bránit, jen když má soupeř víc než dvojnásobnou šanci vyhrát → [[Predikce a pravděpodobnostní modely]].

## Tři body za výhru

Zavedeny v Anglii 1981, FIFA 1995, aby se víc útočilo. Dilger & Geyer (Bundesliga, ligové vs. pohárové zápasy jako kontrolní skupina): **víc žlutých karet**, méně remíz, víc výher o gól, víc odkopů – ale ne víc gólů (Kap. 3).

## Pro praxi (návrh LLM)

- V kartě hráče a skautingu sledovat u útočníků **body z gólů**, nejen počet (pořadí gólu v zápase je v event datech).
- Hodnotit obránce podle toho, čemu zabránili (pozice, zachycení, xG soupeře s hráčem a bez něj), ne podle počtu skluzů → [[Datový skauting – metriky a úskalí]].
- V pozápasovém reportu pracovat s křivkou: kdy padl druhý gól, kolik bodů tým ztratil po prvním obdrženém.

## Souvislosti

[[Expected goals (xG)]] · [[Výkon vs. výsledek a role náhody]] · [[Kognitivní zkreslení v hodnocení]] · [[Hodnocení hráčů – metodika]] · [[Teorie slabého článku (O-ring)]] · [[Obranná linie – principy]]
