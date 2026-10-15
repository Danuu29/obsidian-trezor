---
typ: koncept
tags: [herni-data, metrika, possession-value, modelovani]
zdroje: ["[[Zdroj – Soccermatics]]", "[[Zdroj – Football Hackers]]"]
aktualizovano: 2026-10-15
---
# Possession value a Markovovy řetězce

Rodina modelů, které hodnotí **každou akci s míčem podle toho, o kolik změní pravděpodobnost gólu**. Řeší slabinu objemových statistik (počet přihrávek) – odměňuje posun ke gólu, trestá akce, které šanci snižují ([[Zdroj – Soccermatics]], Kap. 14).

## Markovův model (Sarah Rudd, 2011)

- **Stavy** = kde má útočící tým míč (+ defenzivní kontext); dva absorpční stavy: **Gól** a **Ztráta**. Tabulka pravděpodobností přechodů mezi stavy.
- **Markovská vlastnost:** další stav závisí jen na současném, ne na historii – ve fotbale ne vždy platí, ale je to „rozumný start“.
- **Hodnota stavu** = pravděpodobnost, že posese skončí gólem. Ilustrace: vápno 25 %, střed 15 %, křídlo 12 % (záměrně nadsazené).
- **Kredit hráče = změna hodnoty:** přihrávka křídlo → střed +3; průnikovka střed → vápno +10; gól 100 − 25 = +75; střed → křídlo −3. Křídelník s 10 přihrávkami do středu a 5 do vápna = 95 bodů.
- Rudd: 22 stavů (11 poloh × 2 úrovně tlaku). S polohovými daty stovky až tisíce stavů (např. 11 poloh × 11 počtů obránců mezi míčem a brankou × 2 typy útoku = 242).
- Příklad: Rooney vs. Iceland (Euro 2016) 61 přesných přihrávek, většinou bezpečné změny strany s minimálním přínosem; Matuidi 77 přihrávek dopředu na Payeta a Griezmanna.

## Alternativy zmíněné v knize

- **Packing** – počet soupeřů „vyřazených“ přihrávkou nebo driblinkem.
- Stavy podle překonání obranných linií soupeře (srov. presinkové linie v [[Herní cyklus]]).
- **Possession chains** (Marek Kwiatkowski) – nejdřív klasifikovat typ posese (protiútok, kombinace středem, hra po křídle), pak hodnotit provedení v rámci typu.
- „Frontier“ podle Sumptera: najít malou sadu základních herních stavů a pravděpodobnosti gólu / inkasování z nich.

> [!note] Aktualita (poznámka LLM – ověřit)
> Z „frontieru“ roku 2016 se stal standard: Expected Threat (xT), VAEP, OBV (StatsBomb), possession value modely datových providerů. [[SkillCorner]] přidává tracking kontext (passing options, off-ball runs).

## Využití (návrh)

Hodnocení přínosu hráče v [[Datový skauting – metriky a úskalí]] a v [[Karta hráče – koncept]] místo prostých počtů; přirozeně navazuje na [[Herní cyklus]] (stavy = fáze a kontexty herního modelu).

## Další modely (Football Hackers)

Podle [[Zdroj – Football Hackers]] (Kap. 5, 6, 8) se různé týmy nezávisle dopracovaly ke stejné myšlence – **hodnota akce = změna pravděpodobnosti gólu**:
- **[[Packing]] / Impect model** – kolik soupeřů akce vyřadí, přepočteno na změnu pravděpodobnosti gólu vstřeleného i obdrženého.
- **Dangerousity** (Daniel Link, TU München; studie financovaná DFL, PLOS ONE 2016) – pravděpodobnost gólu v každém okamžiku, kdy má hráč míč, ze 4 složek z tracking dat: **Zone** (poloha v mřížce 2 × 2 m v posledních 34 m), **Control** (relativní rychlost míče a hráče – jak těžké je míč ovládnout), **Pressure** (schopnost obrany zabránit akci), **Density** (počet obránců mezi hráčem a brankou). Validace: křivky „horečky“ zápasu porovnány s hodnocením trenérů a hráčů ve 64 zápasech. **Action Value** = Dangerousity po akci − před akcí → přínos hráče; použití jako filtr videa (ukaž mi momenty, kdy jsem nebezpečí nezvýšil) a pro hledání hráčů, kteří **rozbijí rovnováhu** zápasu. Link: o tom, co pustit hráčům, rozhoduje trenér.
- **Pass Value / Value Creation** (StatDNA, Arsenal) – stejný princip pro skauting a nastavení mezd.
- **EPV – Expected Possession Value** (FC Barcelona, Fernández, Bornn, Cervone; nejlepší paper Sloan 2019, deep learning) – navazuje na Linka; v roce 2019 zatím ne v reálném čase.
- **Sekvence** (OptaPro, 2017) – úseky hry jednoho týmu ukončené obrannou akcí, přerušením nebo střelou (~200 za zápas). Přihrávky na sekvenci PL 2017/18: City 5,5 vs. Stoke/WBA 2,5. **Direct Speed** = čistý posun míče k brance / čas sekvence (ukázka Liverpool: 3,85 m/s). STATS „Playing Styles“ kombinuje KPI do profilu stylu.
- **Ghosting** (Caltech, Hoang M. Le) – model naučený na datech ukazuje, kde by se v dané situaci postavil „průměrný“ obránce; v basketbalu (Toronto Raptors) funkční od 2014, ve fotbale „sci-fi“.

Výhled autora: **prediktivní analytika** (co udělat, abychom vyhráli příští / probíhající zápas; potenciál hráče) bude důležitější než popisná; data automatizují vyhledávání situací ve videu.

## Souvislosti

[[Expected goals (xG)]] · [[Pasové sítě a prostorové mapy]] · [[Normalizace herních dat]] · [[Packing]]
