---
typ: koncept
tags: [datove-oddeleni, organizace, role, strategie, barca]
zdroje: ["[[Zdroj – Barça Match Analysis]]", "[[Zdroj – Soccermatics]]", "[[Zdroj – Football Hackers]]", "[[Zdroj – The Numbers Game]]"]
aktualizovano: 2026-10-15
---
# Oddělení analýzy – struktura a role

Proč a jak zřídit v klubu samostatné oddělení analýzy (P4 M1 + P2 M1, P3 R4 [[Zdroj – Barça Match Analysis]]; opora Vales Vázquez 2012, Couto Lago 2017–18). Relevantní pro budování datového oddělení v [[SK Sigma Olomouc]].

## Proč samostatné oddělení

Ve většině klubů analýzu dělají skauti a asistent, který stříhá video. **Při výměně trenérského štábu klub ztrácí know-how.** Samostatné oddělení zajišťuje kontinuitu, specializaci a databázi. Riziko: tření se štábem → analytik musí prokazovat „velkou schopnost adaptace“.

Definice: „technická jednotka multidisciplinárního týmu, jejímž úkolem je generovat kvalifikovanou informaci formou technických reportů, která pozitivně ovlivňuje rozhodování trenéra“ (Vales Vázquez 2012). **Analytik = trenér, který se nebojí technologie** – musí znát fotbal a fotbalisty.

## Postavení a odpovědnosti

Podřízeno **sportovnímu vedení** (štábní útvar), ne konkrétnímu trenérovi. Tři prioritní odpovědnosti:
1. **Získávání talentů** se skautingem.
2. **Identifikace opakujících se vzorců hry** – se štábem.
3. **Studium vývoje tréninku v akademii** – odchylky hráčů a týmů od cílových hodnot kurikula.

Dodává informace i medicíně, kondici a psychologii („interaktivní matice“, „globální nástroj kontroly kvality“).

## Role

| Role | Náplň |
|---|---|
| **Chief (trainer-)analyst** | vede oddělení, spojka se sportovním vedením, štábem, medicínou; rozděluje soupeře; předkládá dossiery jako jednotný názor |
| **Game analysts** | vlastní tým · soupeř · **standardky** · **brankáři** · **trénink** |
| **Data analysts / data technicians** | sběr a analýza dat |
| **Audiovizuální technici / IT** | nahrávání, software, technika |

V malém klubu kumulují role 1–2 lidé. Kurz předpovídá i **osobní analytiky hráčů**.

## Workflow (Vales Vázquez 2012)

1. definice pracovní strategie a kritérií → 2. příjem a produkce dat a videa po každém zápase → 3. **ukládání do strukturovaných databází** s rychlým přístupem → 4. analýza a technické reporty → 5. **doporučení** (úpravy herního a tréninkového plánu).
Smyčka: co analyzovat → jak → report a aplikace → zpětná vazba. Dva horizonty: **týden** (soupeř, vlastní výkon) a **sezóna** (plán obměny kádru).

**DFB data compression:** Generate (data, skauti) → Analyze (analytici) → Present (trenéři + analytici) → Execute (tým).

## Skauting podle úrovní

Lokální (dohody s kluby, přímé pozorování) → regionální (síť skautů pod delegátem) → národní (přímé i nepřímé přes platformy) → mezinárodní (nejdřív **nepřímo přes video platformy**, pak ověření na místě). Vlastní oddělení je lepší než agentura – zná kontext klubu.

## Reporting

- Dossier → databáze oddělení → hlavní trenér, který **filtruje, co jde k hráčům**.
- Hráči dostávají týmové a individuální reporty: „specific, brief and easy to understand“.
- „Mít hodně informací neznamená být dobře informován“ – se štábem **předem dohodnout, jaká data se sbírají**.

## Lekce z případovky „Antonio“ (P4 M2)

Jasný mandát a role; **data o práci kolegy (kondičáka, trenéra) neprezentovat vedení bez jeho souhlasu**; budovat důvěru se štábem; zajistit hardware a rozpočet předem; obecná ERP nejsou pro sportovní data; vést „**manual of metrics**“ (glosář opakovaných dotazů trenérů).

## Lekce ze Soccermatics (2016)

Podle [[Zdroj – Soccermatics]] (Kap. 14–15):
- **Důvěra rozhoduje víc než model:** Leicester a Aston Villa začaly stejným statistickým hledáním; Leicester data zabudoval do celého provozu, ve Ville se recruitment a trenér (Sherwood) neshodli → sestup. Konflikty (Fulham) média zveličují – většina štábů je k datům zvídavá.
- **Dva adresáti:** největší dopad má analytika podle Omara Chaudhuriho (21st Club) ve **vedení** (dlouhodobé investice, „boardroom mythbuster“ – vyvracet mýty typu „na postup potřebujeme hráče se zkušeností z 2. ligy“); trenéři myslí na příští zápas a chtějí odpověď do pár minut.
- **Workflow analytiků:** video soupeře → zajímavý jev → najít způsob, jak ho změřit → ověřit, zda jde o vzorec, nebo jednorázovost.
- **Validace:** „Nikdy slepě nevěřit tomu, co děláš“; analytici přiznávají, že jejich metody nejsou prokázané → back-testy, benchmarky ([[Predikce a pravděpodobnostní modely]]).
- **Nábor:** veřejné portfolio / blog („Start writing! My blog was effectively my CV“), kombinace fotbalu a techniky; otevřená data a hackathony (#HackMCFC) jako pipeline.
- Lobanovskyj (Dynamo Kyjev): statistické cíle pro hráče a jejich plnění **vyvěšené na nástěnce** – raný příklad hráčských KPI.

## Lekce z Football Hackers (2019)

Podle [[Zdroj – Football Hackers]] (Kap. 3, 5, 6, 8):
- **Bez podpory shora to nefunguje:** mnoho klubů PL najalo analytiky jen proto, aby nevypadaly zastarale; jejich práce v rozhodování hraje malou roli a reporty často nikdo nečte (Anderson & Sally). Analytika musí být součástí manažerské strategie od vedení.
- **Trenéři vs. sportovní ředitelé:** trenéři tráví s týmem tolik času, že přidaná hodnota čísel o vlastním týmu je pro ně menší; sportovní ředitelé a recruitment po datech „hladoví“ – často chtějí **jedno číslo** na hráče.
- **Analytik myslí jako trenér, trenér pracuje jako analytik** (Niemeyer, Bayern). Guardiola strávil se štábem analytiků hodiny až noci nad videem.
- **Vizuální podoba výstupu rozhoduje** (Mislintat) → [[Principy vizualizace a reportingu]].
- **Historie video analýzy:** z handbalu Dortmundu (studenti stříhající videa) → firma Sports Analytics, kamery na celé hřiště, poločasové klipy v Bayernu (Henke 2008), Van Gaal nahrával všechny tréninky (od 2009) → Bayern má „vizuální knihovnu“ práce Van Gaala, Heynckese, Guardioly, Ancelottiho. Video změnilo fotbal víc než jakákoli jiná technologie.
- **„Big data hangover“ (MIT Sloan 2017):** po prvním nadšení kluby nenajímaly analytiky; základní KPI výsledek nepředpovídaly. DFB analytik Clemens po MS 2014: dostupná data jen popisují minulost, musí se generovat data, která nejsou samozřejmá.
- **Kondiční data se prosadila nejdřív** – pracují s nimi sportovní vědci zvyklí na čísla a trenéři vidí přímý užitek (fit hráči).
- **Kvalita dat:** různí provideři různé definice (co je vyhraný souboj) i hodnoty (Brazílie–Mexiko, MS 2018: naběhaná vzdálenost 93, 97 a 105 km podle zdroje) → [[Typy sportovních dat a datová architektura]].
- **Výzkumná oddělení:** Liverpool (Ian Graham, PhD fyzika, od 2012), City, Bayern – tajně; Barcelona naopak otevřeně přes [[Barça Innovation Hub]]. Ijtsma čeká, že nejlepší nápady zmizí za zavřenými dveřmi → propast mezi velkými a malými kluby roste.
- **Kompetence lidí:** kluby potřebují lidi kompetentní, důvěryhodné a věřící v misi (Anderson); outsider potřebuje „poručíka“ s kabinovou zkušeností (Coventry: Mark Venus). Almstadt (Arsenal) pracoval pro Wengera nenápadně; skauti ho nepřijali.
- **Koupě technologií pod vlivem social proof:** kluby kupují, co kupují ostatní, a nedokážou posoudit přínos → měřit dopad.

## Lekce z The Numbers Game (2013)

Podle [[Zdroj – The Numbers Game]] (Úvod, Kap. 7, 12) – pohled z doby, kdy analytici v klubech teprve začínali:
- **Everton (Brown, Graley):** před zápasem rozbor nejméně 5 zápasů soupeře (data Prozone + video) → souhrn pro trenéra, který ho dál zkrátí pro tým; individuální příprava hráčů na přímého protihráče; pozápasový rozbor s trenéry. Kancelář analytiků byla „jedna z mnoha na chodbě do jídelny“ – role bez jasného místa v hierarchii.
- **Köln SportLab (Notzon):** 3 analytici na plný úvazek a 30 na částečný z 15 zemí, data pro A-tým, rezervu i mládež. Všechny kluby 1. a 2. Bundesligy měly data od Impire, ale málokterý je používal.
- **Opta (Coulson):** přijetí video analýzy trvalo 10 let („nemůže trenérům ukázat nic, co nevědí“); další krok – data pro taktiku a recruitment – byl teprve v začátcích. **Rosenfeld (StatDNA):** data musí být dost složitá, aby odrážela hru, a dost jednoduchá, aby šla sbírat; „vysoká prémie za vhled“.
- **Analytika ≠ statistika:** je to způsob myšlení a práce s informacemi – kolik a jaké informace klub má, jak je čte a co s nimi udělá.
- **Hromady dat bez vhledu:** firmy chtějí prodávat a kluby chtějí působit moderně → hodně dat, málo poznání. Brunkhart (Match Analysis): „Chceme vyřešit fotbal, najímáme stážistu, můžete nám dát data?“ Odstrašující příklad: „Moneyball“ v Liverpoolu (Comolli).
- **Předpovědi na dekádu (Kap. 12):** průlomy mimo nejbohatší kluby; žádný jeden „Bill James“, spíš mnoho menších vhledů; mnohonásobně víc dat (GPS, tracking); analýza prostoru – sítě a **trojúhelníky** (hráč s míčem, příjemce, hráč mimo míč, který nejvíc narušuje obranu) místo počítání událostí; **„150–4–4–2“** – výhodu dá organizace všech ~150 lidí kolem týmu; sportovní ředitel jako partner trenéra; silný odpor tradice.

> [!note] Aktualita (poznámka LLM)
> Většina předpovědí se naplnila: tracking a pozice hráčů jsou dnes běžně dostupné (i z videa – [[SkillCorner]]) a sportovní ředitelé jsou standard.

## Souvislosti

[[Typy sportovních dat a datová architektura]] · [[Tagging a code window]] · [[Analýza soupeře – metodika]] · [[Skauting – proces a reporting]] · [[Yarmill]] · [[Analytické balíčky Yarmill]] · [[Kognitivní zkreslení v hodnocení]] · [[21st Club]]
