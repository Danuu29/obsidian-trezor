---
typ: koncept
tags: [skauting, recruitment, metriky, herni-data]
zdroje: ["[[Zdroj – Soccermatics]]", "[[Zdroj – Football Hackers]]", "[[Zdroj – The Numbers Game]]"]
aktualizovano: 2026-10-15
---
# Datový skauting – metriky a úskalí

Jak kluby používají statistiky při hledání hráčů, jaké metriky dávají smysl a kde data selhávají. Doplňuje procesní stránku [[Skauting – proces a reporting]] ([[Zdroj – Soccermatics]], Kap. 4, 14).

## Postup

- **„Spreadsheet scouting / Row A“:** tabulka metrik, seřadit podle sloupce zájmu, začít nahoře. Kanté (Caen 2014/15) vedl Evropu v úspěšných skluzech → Leicester (Steve Walsh, ~5,6 mil. £) → titul → Chelsea 32 mil. £. Walsh pak v Evertonu vzal „Row B“ Gueyeho.
- **Statistika = začátek, ne náhrada:** shortlist z databáze → živé sledování ve více zápasech → rozhovor, trénink, osobnost (FC Midtjylland; všichni profesionální skauti).
- **Nejdřív styl hry, pak hledání:** klub definuje herní styl → profily → algoritmy, které hledají kandidáty pasující do stylu → diskuse se skauty „fotbalovým jazykem“ (Rory Campbell). Kritika: v mnoha klubech je recruitment „obráceně“ – začíná agentem.
- **Modely spolupráce:** Fulham „ticks both boxes“ (skauting i čísla musí být kladné); Atlanta United – žádné dělení: buď datové hledání → skaut, nebo skautův tip → **video sestřih všech akcí hráče v dané situaci** (Lucy Rushton).
- **Nejslabší článek:** posílit nejslabší pozici a hledat **fit se strukturou týmu** spíš než marginální zisky (Anderson & Sally). Leighton Baines – nadprůměrný v soupeřově polovině, slabší ve vlastní → kupující potřebuje silného levého stopera.
- Statistický skauting dává největší výhodu **menším klubům** (velké mají armády skautů).

## Metriky a kontext

- **Radary (Ted Knutson, StatsBomb):** typy akcí, které hráč dělá úspěšně. „Reprezentují jen statistický výstup“ – mění se s ligou, týmem, postem a věkem.
- **Úprava na držení míče:** Kantého interceptions po přepočtu na čas, kdy Leicester neměl míč, klesly → vynikal i díky stylu týmu → [[Normalizace herních dat]] (per 30 OTIP).
- **Objemové metriky klamou:** hodně skluzů = možná špatné postavení; vysoká přesnost přihrávek = možná bezpečná volba. Fotbal „nikdy nebude Moneyball“ – baseball je hra individuálních statistik, fotbal týmových vzorců.
- **Defenzivní „patch“ (Thom Lawrence):** vymezit území obránce a měřit, **jak daleko soupeř v jeho území posune míč**. Nejlepší 2015/16 Busquets; v březnu 2016 na vrcholu Umtiti → v červnu Barcelona (anekdota, jeden případ). Slabina: týmy, které záměrně pouštějí soupeře po křídlech (Leicester), mají „špatné“ krajní obránce.
- **Kompozitní indexy** (EA Sports PPI; McHale & Scarf): původní čistě statistická verze vynesla nahoru brankáře a obránce, po úpravě „aby to dávalo smysl“ ofenzivní hráče. **Každý index navrhují lidé** – rozhodnutí o vahách je potřeba explicitně popsat.
- Hodnota přínosu místo objemu → [[Possession value a Markovovy řetězce]], [[Expected goals (xG)]].
- **Executive functions:** hráči skórují v testu design fluency ~o 50 % lépe než populace, nejvyšší liga lépe než 3. liga, skóre korelovalo s góly + asistencemi další sezónu (Vestberg et al. 2012). *Možný doplněk vstupní diagnostiky – návrh.*

## Úskalí a varování

- **Leicester vs. Aston Villa (2015/16):** oba začínali statistickým hledáním ve Francii. Leicester vyhrál ligu, Villa (13 posil) sestoupila s rekordně nízkým počtem bodů. Rozdíl podle Sumptera: **vzájemná důvěra štábu a analytiků**.
- **Validace chybí:** „art more than science“ (Kwiatkowski); „nemám důkaz, že má metoda funguje“ (Lawrence); „další krok je prokázat, že čísla fungují“ (Newman). Twitter a blogy nedávají peer review.
- Přestupní cena není míra kvality; ceny top hráčů rostou exponenciálně (Chaudhuri, 21st Club).

> [!note] Aktualita (poznámka LLM – ověřit)
> Radary a „spreadsheet scouting“ nahradily percentilové dashboardy, role-based modely a ML vyhledávání podobných hráčů. Postupy lidí a klubů v knize jsou stav 2016–17.

## Praxe 2017–2019 (Football Hackers)

Podle [[Zdroj – Football Hackers]] (Kap. 6):
- **Datový předvýběr je standard:** Dortmund dostával ~2 500 nabídek hráčů za sezónu; přes [[Wyscout]] (předtagované video, ~40 000 hráčů) a data umí top kluby do 24 h sestavit e-dossier (data + video min. ze 3 zápasů) a ušetří zbytečné cesty. Agent už nemůže „prodat“ průměrného hráče sestřihem s hudbou.
- **Matchmetrics / Scoutpanel (Sven Mislintat, Dortmund):** hřiště rozdělené na **100 polí s vahou podle důležitosti** (zisk míče v malém vápně > ve středovém kruhu) → index hráče. Filtrování: minuty (≥ 200) → věk → post (nadkategorie „defensive left winger“) → kvalitativní filtry (celkový index, 1v1, zakončení, centry) → hrstka jmen. Ligový koeficient **0,7–1** podle výsledků v evropských pohárech; maximum 10, top hráč nižší ligy ~7 – přenositelnost do vyšší ligy je subjektivní úsudek skauta. Mislintat často vypínal filtr zemí, aby nepřišel o talenty.
- **Sobiechův paradox:** první verze modelu zařadila do „týmu sezóny“ průměrného stopera Fürthu – jeho tým bránil hluboko a pouštěl nejvíc centrů v lize, takže měl hodně odvrácených míčů. **Akce hráče je nutné vztáhnout k akcím týmu** (podíl na obranných akcích týmu; u útočníků naopak víc příležitostí v dominantních týmech) → [[Normalizace herních dat]].
- **Stability:** konzistence výkonu (Lahm = maximum). Mladý hráč s vysokou variabilitou mezi průměrem a špičkou je příležitost (Dembélé); 24letý s velkými výkyvy už spíš riziko (Philipp Max, [[Packing]]).
- **Similar Players** – hledání podle podobnosti profilu (Kanté → Torreira).
- **Prezentace rozhoduje o přijetí:** stejná data v Excelu nikoho nezajímala, s atraktivním rozhraním na iPadu je chtěl každý.
- **StatDNA (Arsenal):** ruční kódování detailů (lepší noha, pozice brankáře, obránci mezi střelcem a brankou), kategorie **Defensive Errors** (pomalost, špatné postavení, špatné natočení těla) → nalezení nenápadně solidních obránců (Mertesacker). Zpětná analýza ukázala, že data by varovala před drahými omyly (Chamakh – „hot streak“ ze střel z nízkého xG; Park Chu-young). Mislintat: model podhodnocuje fyzicky soubojové obránce.
- **Kde data nestačí:** skenování prostoru (Weigl se před převzetím třikrát rozhlédl), odvaha, nervy, leadership (Guendouzi), hráč ve „špatném“ týmu, motivace a strachy. Výběr hráče, kterého data zpochybnila, může dopadnout skvěle (Midtjylland: Sörloth, Sanneh – doporučili skauti).
- **Tým skautů:** mix pohledů – starý přísný skaut i mladý trenér; na finálního kandidáta poslat všechny, každý se svými kritérii. „Nikdy jen Moneyball, ale ani bez matematiky – jinak zbudou jen subjektivní názory“ (Mislintat, parafráze).
- **Transfer exchange rate:** porovnání lig přes Club Elo (leden 2019: La Liga 1 736, PL 1 709, BL 1 680 … 2. BL 1 460, Švýcarsko 1 458, Eredivisie 1 424); vybírat ligy odpovídající vlastní úrovni. Midtjylland koupil Sparva z 2. BL, kterou model hodnotil jako dánskou špičku. Kontext: víc Srbů než Maďarů v top ligách při podobné úrovni lig – možná kvůli agentům, ne kvalitě.
- **Avoid costly mistakes:** vyhnout se drahému omylu je skoro důležitější než najít podhodnoceného hráče (Renato Sanches – efektní, ale defenzivně slabý pro post šestky).
- Plus-minus přístup → [[Goalimpact a plus-minus]]; super-skauti (Walsh, Campos, Monchi, Mislintat) jsou dnes přestupovaným „zbožím“.

## Doplnění z The Numbers Game (2013)

Podle [[Zdroj – The Numbers Game]] (Kap. 3, 4, 5, 8, 11):
- **Nejslabší článek:** zlepšení nejslabšího hráče sestavy přinese víc bodů než zlepšení nejlepšího → [[Teorie slabého článku (O-ring)]].
- **Útočníci podle bodů, ne gólů:** góly za stavu, kdy rozhodují (první, druhý), mají větší cenu než góly do rozhodnutého zápasu (Darren Bent vs. Torres) → [[Hodnota gólu – útok vs. obrana]].
- **Obránci podle toho, čemu zabránili:** málo skluzů může být znak kvality (Maldini, Stam).
- **Přesnost přihrávek** očistit o obtížnost – po očištění jsou hráči skoro stejní; rozhoduje, jak se dostanou do prostoru (Rosenfeld) → [[Držení míče a ztráty]].
- **Přenositelnost výkonu:** po přestupu výkon klesá, protože závisí na spoluhráčích a systému (Groysberg: 89 % vs. 69 % špičkových analytiků si udrželo hodnocení); počítat s adaptací a plánovat integraci → [[Vliv trenéra a jeho výměna]].
- **Technický skaut** (Steven Houston, Hamburg; dříve NBA) – raný příklad skauta pracujícího s daty.

## Souvislosti

[[Skauting – proces a reporting]] · [[Vstupní diagnostika hráče]] · [[Postové profily]] · [[Thresholdy a benchmarky]] · [[Brentford a FC Midtjylland]] · [[StatsBomb]] · [[Opta]] · [[Packing]] · [[Goalimpact a plus-minus]] · [[Kognitivní zkreslení v hodnocení]] · [[Impect]]
