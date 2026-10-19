# Log LLM Wiki

Chronologický, append-only záznam. Formát hlavičky: `## [RRRR-MM-DD] typ | název`. Posledních 5: `grep "^## \[" log.md | tail -5`.

## [2026-10-15] schéma | Založení wiki

- Vytvořena struktura `LLM Wiki/` (raw/, wiki/zdroje|entity|koncepty|projekty|syntezy), schéma [[CLAUDE]], [[index]], tento log.
- Rozhodnutí: osobní „druhý mozek“, česky; stávající poznámky ve vaultu = neměnné surové zdroje (čtou se na místě, nekopírují se); `Apple Notes/Sigma Olomouc ⚽/` jsou duplikáty → neingestovat.

## [2026-10-15] ingest | Počáteční ingest celého vaultu

- 9 zdrojových stránek (≈ 95 poznámek), 13 entit, 17 konceptů, 6 projektů, 4 syntézy.
- Zjištěné rozpory: normy VALD (Nordic, ISO PRONE, asymetrie, AB/AD, flexe/extenze), škála hodnocení → [[Rozpory a nesrovnalosti]].
- Bezpečnost: v poznámce *Analýza soupeře kompletní prompt* (a kopii v Apple Notes) je heslo k SkillCorner v otevřeném textu – nepřeneseno, doporučeno odstranit a změnit.
- PDF a obrázky zatím neingestovány (jen odkazy v indexu).

## [2026-10-15] ingest | Barça Match Analysis (kurz, 16 PDF)

- Zdroj: 16 PDF kurzu match analysis od Barça Innovation Hub, uloženo do `raw/Barca Match Analysis/`. Skeny bez textu → OCR + vizuální kontrola tabulek; nejistá místa „(?)“.
- Nové: [[Zdroj – Barça Match Analysis]]; entity [[Barça Innovation Hub]], [[Mediacoach]]; 17 konceptů (plány analýzy, IFP, obranná linie, herní cyklus, analýza soupeře, operativní strategie, mikrocyklus MD, standardky, pre-match, live a poločas, video feedback, sezónní hodnocení, analýza tréninku, taktická komunikace, oddělení analýzy, typy dat, tagging); syntéza [[Barça kurz – návrhy pro Sigmu]].
- Aktualizováno: Hodnocení utkání a pozápasový report, Aplikace – Analýza soupeře, Aplikace – Match tracker, Analýza trenérské komunikace, Postové profily, Sigma Way, Skauting, Principy vizualizace, Normalizace herních dat, Wyscout, StatsBomb, SK Sigma Olomouc, Mapa datových zdrojů, Otevřené otázky, Přehled wiki, index.
- Rozpory: žádné věcné. Terminologická nesrovnalost – španělské číslování postů (P2 = krajní obránce) vs. značení v Postových profilech → zapsáno do Otevřených otázek, ne do Rozporů.
- Ingest proběhl bez úvodní diskuse o důrazech (Danů zadal „zapracuj“) – důrazy lze doladit zpětně.

## [2026-10-15] ingest | Soccermatics (D. Sumpter, 2016)

- Zdroj: kniha *Soccermatics – Mathematical Adventures in the Beautiful Game* (Pro-Edition, 293 s.), uložena do `raw/Soccermatics (Sumpter 2016).pdf`. PDF s textovou vrstvou; čtení po částech (I–IV), vzorce z obrázků chybí → dopočty označeny.
- Nové: [[Zdroj – Soccermatics]]; entity [[Opta]], [[Brentford a FC Midtjylland]]; 7 konceptů ([[Expected goals (xG)]], [[Possession value a Markovovy řetězce]], [[Pasové sítě a prostorové mapy]], [[Pressing a kolektivní pohyb]], [[Half-spaces a taktická geometrie]], [[Predikce a pravděpodobnostní modely]], [[Datový skauting – metriky a úskalí]]); syntéza [[Soccermatics – návrhy pro Sigmu]].
- Aktualizováno: StatsBomb, SkillCorner, Wyscout, Sigma Way, Normalizace herních dat, Principy vizualizace, Skauting, Oddělení analýzy, Typy dat, Hodnocení utkání, GPS metriky, Aplikace – Analýza soupeře, Mapa datových zdrojů, Otevřené otázky, Přehled wiki, index.
- Rozpory: žádné věcné. Zpřesnění, ne rozpor: represink „do 6 s“ (Sigma Way) vs. data Prozone 2,5 s / 5,5 s. Napětí: „herní dominance“ vs. zjištění, že držení míče samo góly nepředpovídá (poznamenáno na Sigma Way).
- Kniha je z let 2016–17 → zastaralá tvrzení (firmy, role lidí, stav tracking analýzy) označena calloutem „Aktualita“ jako poznámka LLM k ověření.
- Ingest bez úvodní diskuse o důrazech (Danů zadal „zpracuj“); důraz dán na přenositelnost do klubové analytiky, analogie mimo fotbal (biologie, davy) vynechány.

## [2026-10-15] ingest | Football Hackers (Ch. Biermann, 2019)

- Zdroj: kniha *Football Hackers – The Science and Art of a Data Revolution* (Blink 2019, 212 s.), uložena do `raw/Football Hackers (Biermann 2019).pdf`. PDF s textovou vrstvou; grafy a tabulky jen částečně v textu → převzata jen čísla z textu.
- Nové: [[Zdroj – Football Hackers]]; entity [[Impect]], [[21st Club]]; 7 konceptů ([[Kognitivní zkreslení v hodnocení]], [[Výkon vs. výsledek a role náhody]], [[Packing]], [[Goalimpact a plus-minus]], [[Kognitivní trénink]], [[Osobnostní profily hráčů]], [[Strategie menšího klubu]]); syntéza [[Football Hackers – návrhy pro Sigmu]].
- Aktualizováno: Expected goals (xG), Possession value, Pressing, Half-spaces, Datový skauting, Standardní situace, Oddělení analýzy, Hodnocení utkání, Predikce, Brentford a FC Midtjylland, Opta, StatsBomb, Wyscout, Barça Innovation Hub, Mapa datových zdrojů, Vstupní diagnostika, Hodnocení hráčů, Skauting, Otevřené otázky, Přehled wiki, index.
- Rozpory: žádné věcné. Zpřesnění: dlouhodobé překonávání xG (Favre) vs. „neudržitelná konverze“ na stránce xG – vysvětleno slepým místem modelu (shot clarity / pressure), zapsáno jako callout, ne do Rozporů. Nuance u Midtjyllandu: největší prodeje přišly od skautů, ne z dat (doplněno na entitu).
- Kniha je z let 2017–19 → vývoj firem a metrik označen calloutem „Aktualita“ (poznámka LLM k ověření). Anekdoty a osobní detaily (zdraví, soukromí hráčů) vynechány.
- Ingest bez úvodní diskuse o důrazech (Danů zadal „zapracuj“); důraz na rozhodování, skauting a přenos do Sigmy.

## [2026-10-15] ingest | The Numbers Game (Ch. Anderson & D. Sally, 2013)

- Zdroj: kniha *The Numbers Game – Why Everything You Know About Football Is Wrong* (Penguin 2013, 333 s.), uložena do `raw/The Numbers Game (Anderson, Sally 2013).pdf`. PDF s textovou vrstvou, přečteno celé; grafy jen jako titulky → převzata čísla z textu a tabulek.
- Nové: [[Zdroj – The Numbers Game]]; 5 konceptů ([[Teorie slabého článku (O-ring)]], [[Hodnota gólu – útok vs. obrana]], [[Držení míče a ztráty]], [[Střídání a vyloučení]], [[Vliv trenéra a jeho výměna]]); syntéza [[The Numbers Game – návrhy pro Sigmu]]. Nové entity nezaloženy (firmy z knihy už většinou neexistují samostatně) – doplněna [[Opta]].
- Aktualizováno: Výkon vs. výsledek a role náhody, Predikce, Standardní situace, Kognitivní zkreslení, Strategie menšího klubu, Oddělení analýzy, Datový skauting, Pasové sítě, Expected goals, Hodnocení hráčů, Hodnocení utkání, IDP, Analýza tréninku, Analýza trenérské komunikace, Live analýza a poločas, Analýza soupeře, Sigma Way, Brentford a FC Midtjylland, Opta, Rozpory, Otevřené otázky, Přehled wiki, index.
- Rozpory (→ [[Rozpory a nesrovnalosti]]): zkušenost trenéra (Heidel ve Football Hackers vs. data Bridgewater et al.); hodnota rohů/standardek (doporučení se liší, čísla ne). Zpřesnění, ne rozpor: držení míče souvisí s výsledky (NG), ale po zohlednění xG nepředpovídá góly (Soccermatics) – rozhodují ztráty.
- Kniha je z let 2010–2012 → zastaralá místa (Castrol rankings, hot hand, pravidlo 3 střídání, předpověď ~1 000 gólů v PL) označena calloutem „Aktualita“ (poznámka LLM k ověření). Nesrovnalosti uvnitř knihy (Reepova čísla, 89 vs. 92 % mzdy) poznamenány na zdrojové stránce.
- Ingest bez úvodní diskuse o důrazech (Danů zadal „udělej z knihy znalosti“); důraz na nová témata, která předchozí knihy nepokrývají (slabý článek, obrana, ztráty, střídání, trenéři), a přenos do Sigmy. Anekdoty (Megrelishvili, Villas-Boas) jen jako příklady.

## [2026-10-15] ingest | Pořiďte si druhý mozek (T. Forte, 2022/2023)

- Zdroj: kniha *Pořiďte si druhý mozek* (orig. *Building a Second Brain*, Atria 2022; česky Jan Melvil 2023), uložena do `raw/Pořiďte si druhý mozek (Forte 2023).pdf`. E-kniha s textovou vrstvou, přečtena celá; obrázky jen jako popisky. Vodoznak s údaji kupujícího nepřenesen.
- **První zdroj mimo fotbal** – oblast osobní efektivita a práce se znalostmi; zároveň popisuje princip samotné wiki.
- Nové: [[Zdroj – Pořiďte si druhý mozek]]; 7 konceptů ([[Metoda CODE]], [[Zaznamenávání a oblíbené problémy]], [[PARA – organizace podle akčnosti]], [[Postupná sumarizace]], [[Dílčí balíčky a znovuvyužití práce]], [[Divergence a konvergence]], [[Revize a návyky druhého mozku]]); projekt [[Druhý mozek – LLM Wiki]] (wiki sama jako projekt); syntéza [[Druhý mozek – návrhy pro wiki a práci]]. Entity nezaloženy (Forte Labs není pro wiki relevantní organizace).
- Aktualizováno: Kognitivní zkreslení v hodnocení (recency a confirmation bias při sběru), Principy vizualizace a reportingu (report ve vrstvách), Aplikace – Strategická aplikace, Analytické balíčky Yarmill, Otevřené otázky, Přehled wiki, index.
- Rozpory: žádné věcné. **Napětí kniha × schéma wiki** (zhušťovat až při použití vs. kompilovat při ingestu; ukládat ≤ 10 % vs. číst celý zdroj; třídit podle akčnosti vs. podle typu) – popsáno v syntéze a v Otevřených otázkách jako návrh ke změně schématu, schéma [[CLAUDE]] **neměněno** (čeká na Danů).
- Aktualita: kniha nepočítá s LLM nástroji; navazující *The PARA Method* (2023) zatím neingestováno – callout na zdrojové stránce.
- Ingest bez úvodní diskuse o důrazech (Danů zadal „zapracuj do znalostí“); důraz na přenos do wiki a do práce datového oddělení, příběhy z knihy jen jako příklady.

## [2026-10-15] ingest | Persuading with Data (M. Kazakoff, 2022)

- Zdroj: kniha *Persuading with Data – A Guide to Designing, Delivering, and Defending Your Data* (MIT Press 2022, 318 s.), uložena do `raw/Persuading with Data (Kazakoff 2022).pdf`. PDF s textovou vrstvou, přečteno celé; grafy a ukázkové slidy jen jako popisky.
- Zjištění: Danůva poznámka `Apple Notes/Yarmill/Vizualizace dat` se s Kap. 1–3 shoduje téměř bod po bodu → zřejmě výpisky z této knihy (?); kniha je původní zdroj části [[Principy vizualizace a reportingu]].
- Nové: [[Zdroj – Persuading with Data]]; 9 konceptů ([[Vysvětlování dat – tři výzvy]], [[Vnímání grafů – preattentivní atributy a Gestalt]], [[Výběr grafu podle vztahu v datech]], [[Data-ink ratio a vizuální hierarchie]], [[Headline a testy slidu]], [[Minto pyramida]], [[WIIFT a přesvědčování publika]], [[TOP-T – prezentace grafu]], [[Audience Confusion Matrix]]); syntéza [[Persuading with Data – návrhy pro Sigmu]]. Entity nezaloženy (MIT Sloan / autor nejsou pro wiki relevantní organizace).
- Aktualizováno: Principy vizualizace a reportingu, Kognitivní zkreslení v hodnocení, Thresholdy a benchmarky, Hodnocení utkání a pozápasový report, Oddělení analýzy, Výkon vs. výsledek, Analytické balíčky Yarmill, Yollanda, Sezónní hodnocení, Video feedback, Předzápasová příprava, Normalizace herních dat, Rozpory, Otevřené otázky, Přehled wiki (nový proud 8 „Komunikace dat“), index.
- Rozpory: žádné věcné. Drobná nesrovnalost – kapacita pracovní paměti „2–3 prvky / 7 ± 2“ (Danůva poznámka) vs. „3–4 chunky“ (kniha) → [[Rozpory a nesrovnalosti]]. Vnitřní napětí knihy („začni pointou“ vs. TOP-T „pointa až po orientu“) vysvětleno na stránce TOP-T (celek vs. jednotlivý důkazní slide).
- Kniha je z byznysu, ne ze sportu → všechny fotbalové příklady označeny jako *návrh LLM*. Aktualita: cílí na statické slidy, interaktivní dashboardy a AI reporty jen okrajově (callout na zdrojové stránce).
- Ingest bez úvodní diskuse o důrazech (Danů zadal „zpracuj do znalostí“); důraz na přenos do reportingu datového oddělení, porad štábu a Yarmillu. Byznysové případovky (Craigstone) jen jako příklady.

## [2026-10-16] schéma | Vlastní poznámky jako živé zdroje, vyloučené složky, detekce nového

- Rozlišeny dva druhy zdrojů: `raw/` (cizí materiál, neměnný) a vlastní poznámky ve vaultu (živé – při změně se zdrojová stránka aktualizuje).
- Vyloučeno z wiki: `Úkoly/`, `Apple Notes/Sigma Olomouc ⚽/`, `Markdown – tahák.md`, poznámky s `wiki: ne`. [[Zdroj – Úkoly]] označen jako archivní snímek k 2026-10-15.
- Nový skript `nastroje/nove.py` pro „ingestuj vše nové“; ingest vlastních poznámek nově zapisuje do logu řádek `- git: <hash>`.
- Údržba: Danů přesunul `Diskuze a meetingy` do `Meetings/` – odkazy přepsal Obsidian, opravena `cesta:` u [[Zdroj – Porady akademie (podzim 2026)]] a index. Smazány prázdné/nerelevantní poznámky *Beskydy – meeting managementu* a *_Přehled úprav* (wiki na ně neodkazovala).
- Základ pro detekci změn (stav vaultu, který wiki pokrývá):
- git: 8732be2

## [2026-10-19] ingest | Zátěžový test CPET 2026-09-21

- Zdroj: Danova poznámka `Osobní rozvoj/Kondice/Zátěžové testy/Zátěžový test CPET 2026-09-21.md` (živá, hlavní zdroj) + 2 PDF z Kliniky sportovní medicíny uložené do `raw/Zátěžové testy/` (slovní vyhodnocení 3 s.; data dech po dechu a 9 grafů 7 s., interpretace označena „NÁVRH“). Klíčová čísla poznámky ověřena proti PDF.
- **První zdroj o Danově vlastním tréninku** – nová oblast kondice / vytrvalostní trénink.
- Nové: [[Zdroj – Zátěžový test CPET 2026-09-21]]; koncepty [[CPET a laktátové schody]], [[Tréninkové zóny a prahy]]; entita [[Klinika sportovní medicíny]]; projekt [[Osobní cyklistický trénink]].
- Aktualizováno: Thresholdy a benchmarky, GPS metriky a zatížení, Silové testy a normy, Vstupní diagnostika hráče, VIF Cycling team (doplněna sekce Souvislosti), Rozpory, Otevřené otázky, Přehled wiki (nahrazena věta „osobní trénink zatím nemá zdroje“), index.
- Rozpory (→ [[Rozpory a nesrovnalosti]]): anaerobní práh ~240 W (klinika) vs. FTP/MLSS 225–235 W (doplňující rozbor); max. 450 W z rampy vs. MAP ~300–320 W. Rozhodnuto Danům: platí zóny kliniky.
- Soukromí: z PDF nepřeneseno datum narození ani další osobní údaje; jde o Danovy vlastní údaje (pravidlo o zdraví se týká hráčů/závodnic).
- Ingest bez úvodní diskuse o důrazech (Danů poznámku už napsal a zadal „ulož jako zdroj“); důraz na zóny, rozhodnutí a milníky.
- git: 406624f

## [2026-10-19] schéma | Smazaná složka Apple Notes/

- Danů smazal celou složku `Apple Notes/` (Yarmill poznámky, duplikáty Sigmy, PDF) – dělala nepořádek.
- Odkazy na smazané poznámky nahrazeny textem: Zdroj – Yarmill poznámky, Zdroj – Persuading with Data, Rozpory, Principy vizualizace a reportingu, GPS metriky a zatížení, Vnímání grafů, Analytické balíčky Yarmill. [[Zdroj – Yarmill poznámky]] označen jako archivní snímek k 2026-10-15; znalosti z něj ve wiki zůstávají.
- Index: opraven řádek zdroje a poznámka o neingestovaných PDF (smazána – pro ingest vložit do `raw/`). Zdroj – Zadání aplikací: kopie s heslem SkillCorner smazána, v historii gitu zůstává.
- Schéma: z [[CLAUDE]] odstraněno `Apple Notes/` (příklad živých poznámek i vyloučení duplikátů), přidán příklad `Osobní rozvoj/`; z `nove.py` odstraněna položka `EXCLUDE`.
- git: 65caf21

## [2026-10-19] ingest | Vše nové (1 zdroj: Tréninkový deník – cyklistika)

- Plánovaná pondělní údržba (bez úvodní domluvy s Danů – běží automaticky).
- `nove.py` hlásil: změněný `Osobní rozvoj/Kondice/Tréninkový deník.md` (týdenní synchronizace z Claude Docs – doplněné odkazy na videa cviků) a „nový“ `Zátěžový test CPET 2026-09-21.md` – ten je už zpracovaný, jde jen o rozdíl Unicode normalizace názvu (NFD na disku vs. NFC v gitu), ne o změnu obsahu.
- Zjištěno, že `Tréninkový deník.md` + 5 poznámek `Tréninkové plány/` přibyly v commitu 65caf21, který se dostal do logu jen u záznamu `schéma`, takže je `nove.py` neviděl jako nové a nikdy nebyly ingestovány → zpracovány teď.
- Nové: [[Zdroj – Tréninkový deník (cyklistika)]] (dlouhodobý plán 6 fází do jara 2027, posilovna, závody 2026, session RPE a poměr A/C, průběh týdnů 21. 9. – 25. 10., poučení).
- Aktualizováno: [[Osobní cyklistický trénink]] (plán, aktuální stav – fáze 1 přerušena zraněním, otevřené body), [[Tréninkové zóny a prahy]], [[GPS metriky a zatížení]] (paralela session RPE / A/C k ACWR), [[Zdroj – Zátěžový test CPET 2026-09-21]] (odkaz), [[Otevřené otázky]], [[Přehled wiki]], index.
- Rozpory: žádné nové (zóny v deníku = zóny kliniky).
- Lint: 0 ve všech kategoriích.
- git: 65caf21

## [2026-10-19] lint | Údržba vaultu (obsidian-notes)

- Wiki lint: 0 ve všech kategoriích.
- Vault mimo wiki: název `Zátěžový test CPET 2026-09-21.md` převeden z NFD na NFC Unicode (opravuje rozbitý odkaz ze [[Zdroj – Zátěžový test CPET 2026-09-21]] a falešné „[A]“ v `nove.py`).
- Nová mapa vaultu `MOC.md` (`wiki: ne`) – odkazuje všechny vlastní poznámky mimo wiki; sirotků ve vaultu 9 → 0.
- Zbývá na Danů: 10 odkazů na přílohy (PDF/PNG) smazané s `Apple Notes/` – v Analytická témata (Future Blue, Nápady a požadavky, Skauting, Yollanda insights) a Analýza audio trenéra; obnovitelné z gitu.

## [2026-10-19] schéma | nove.py porovnává názvy souborů v NFC

- Na pokyn Danů: `nove.py` normalizuje cesty z gitu na NFC a necommitnutý „nový“ soubor, který je v gitu pod stejným NFC názvem, nehlásí. Smazaný soubor hlásí, jen když opravdu na disku chybí. Důvod: macOS může mít názvy s diakritikou na disku v NFD a git je pak vidí jako nové (případ CPET poznámky). Ověřeno testem s dočasně přejmenovaným souborem.
- Přílohy smazané s `Apple Notes/` Danů nepotřebuje (vše potřebné je přesunuté v Obsidianu).
