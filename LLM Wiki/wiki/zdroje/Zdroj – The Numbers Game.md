---
typ: zdroj
tags: [zdroj, kniha, analytika, nahoda, drzeni-mice, slaby-clanek, treneri, strategie]
cesta: "LLM Wiki/raw/The Numbers Game (Anderson, Sally 2013).pdf"
ingest: 2026-10-15
aktualizovano: 2026-10-15
---
# Zdroj – The Numbers Game

Kniha **Chris Anderson & David Sally: *The Numbers Game – Why Everything You Know About Football Is Wrong*** (Penguin/Viking, 2013). Anderson je politický ekonom a bývalý brankář (později šéf Coventry City – viz [[Zdroj – Football Hackers]], Kap. 3), Sally behaviorální ekonom a bývalý baseballový nadhazovač. Kniha **testuje fotbalová klišé na datech** (Opta, StatDNA, Prozone, Deloitte, akademické studie) a nabízí „reformaci“: méně dogmat, víc otázek „proč?“.

> [!info] Poznámky ke zdroji
> - PDF s textovou vrstvou (333 s.); grafy (51 obrázků) jsou jen jako titulky – převzata čísla z textu a tabulek.
> - Stav poznání **2010–2012** (PL, Bundesliga, La Liga, Serie A). Je to **nejstarší ze tří analytických knih** ve wiki (Soccermatics 2016, Football Hackers 2019). Místa, kde se obor posunul, jsou označena calloutem **Aktualita** (*poznámka LLM – ověřit*).
> - Většina analýz autorů je **korelační** (regrese na sezónních datech) – ukazují vztahy, ne nutně příčiny.
> - Citace: **Úvod** a **Kap. 1–12**. Stránky se neuvádějí.

## Struktura knihy

| Kap. | Název (orig.) | Obsah → stránka wiki |
|---|---|---|
| Úvod | Football for Sceptics | analytika vs. statistika, Reep („Football Accountant“), analytici Evertonu, rohy ~0,022 gólu, „nejzranitelnější po vstřelení gólu“ je mýtus → [[Standardní situace – analýza]], [[Držení míče a ztráty]] |
| 1 | Riding Your Luck | Poisson (2,66 gólu), kurzy a favorité, Heuer, Skinner & Freeman, Spiegelhalter 48/26/26, Lames 44 % „šťastných“ gólů → **fotbal je 50/50 štěstí a dovednost** → [[Výkon vs. výsledek a role náhody]], [[Predikce a pravděpodobnostní modely]] |
| 2 | The Goal: Football’s Rare Beauty | góly ubývají a od 70. let stagnují, rozdíly mezi týmy se zmenšují, top ligy jsou v číslech stejné → [[Predikce a pravděpodobnostní modely]] |
| 3 | They Should Have Bought Darren Bent | 3 body za výhru (víc karet, ne víc gólů), „směnný kurz“ gólů na body, **marginální body** útočníků → [[Hodnota gólu – útok vs. obrana]] |
| 4 | Light and Dark | Menotti: útok vs. obrana, regrese gólů na výhry a prohry, **čisté konto > 1 gól (0 > 1)**, hot hand, „They Saw a Game“, princip Maldini → [[Hodnota gólu – útok vs. obrana]], [[Kognitivní zkreslení v hodnocení]] |
| 5 | Piggy in the Middle | hráč má míč 53 s za zápas, „držení je množné“ (~190 ztrát týmu), obtížnost přihrávky, **ztráty důležitější než držení** → [[Držení míče a ztráty]] |
| 6 | The Deflation of the Long Ball | Stoke (míč méně ve hře, auty), Reep vs. Hughes & Franks, četnost vs. pravděpodobnost gólu → [[Držení míče a ztráty]] |
| 7 | Guerrilla Football | Wigan (Martínez): pravděpodobnost sestupu podle mezd, protiútoky, přímé kopy, střely z dálky; „fourth down“ (Romer, Belichick); data jsou pravda, ne návod → [[Strategie menšího klubu]] |
| 8 | Why a Football Team Is Like the Space Shuttle | **O-ring teorie** (Kremer), shlukování kvality, nejslabší hráč ovlivní výsledky víc než nejlepší (Castrol data) → [[Teorie slabého článku (O-ring)]] |
| 9 | How Do You Solve a Problem Like Megrelishvili? | 5 možností, co s nejslabším článkem: schovat, podpořit, **vystřídat** (<58<73<79), zlepšit (Köhlerův efekt, učení od lepších), prodat; **cena červené karty** → [[Střídání a vyloučení]], [[Teorie slabého článku (O-ring)]] |
| 10 | Stuffed Teddy Bears | mzdy vysvětlují 81 % pořadí za dekádu, ale 59 % v jedné sezóně; trenér ≈ 15 % jako CEO; studie úmrtí CEO → [[Vliv trenéra a jeho výměna]] |
| 11 | The Young Prince | Villas-Boas v Chelsea: zkušenost trenéra, talent není vrozený, přenositelnost výkonu (Groysberg), čistá data o trenérovi, **odvolání = regrese k průměru**, chvála vs. trest (Kahneman), Wooden → [[Vliv trenéra a jeho výměna]] |
| 12 | Life During the Reformation | 10 předpovědí na dekádu: inovace z chudých klubů, víc dat (GPS, tracking), geometrie a trojúhelníky, levnější útočníci vs. obránci, „150–4–4–2“, sportovní ředitel, odpor proti analytice → [[Oddělení analýzy – struktura a role]] |

## Hlavní myšlenky

1. **Fotbal je napůl náhoda.** Favorit vyhrává jen o málo víc než polovinu zápasů, ~44 % gólů má viditelnou složku štěstí, tým s víc střelami vyhraje jen 47 % zápasů. Sezóna je ale předvídatelná (Poisson) (Kap. 1) → [[Výkon vs. výsledek a role náhody]].
2. **Góly jsou vzácné a nemají stejnou cenu.** Nejcennější je druhý gól; pátý skoro nic nepřidá. Hodnotit útočníky podle bodů, které jejich góly přinesly, ne podle počtu gólů (Kap. 2–3) → [[Hodnota gólu – útok vs. obrana]].
3. **Obrana je stejně cenná jako útok, při vyhýbání se porážkám cennější.** Čisté konto má větší bodovou hodnotu než vstřelený gól (**0 > 1**). Obranu podceňujeme, protože nevidíme, co se nestalo (princip Maldini) (Kap. 4).
4. **Fotbal je hra řízení ztrát, ne držení.** Klíčové je **nevracet míč soupeři**; přesnost přihrávek určuje hlavně situace, kterou tým hráči vytvoří (Kap. 5–6) → [[Držení míče a ztráty]].
5. **Neexistuje vítězný vzorec.** Stoke i Wigan přežívaly díky stylu na míru svým zdrojům; tradiční cesty se často drží jen proto, že selhat konvenčně je bezpečnější (Kap. 6–7) → [[Strategie menšího klubu]].
6. **Fotbal je hra slabého článku.** Kvalita se v klubech shlukuje a zlepšení nejslabšího hráče přinese víc bodů než zlepšení hvězdy (Kap. 8–9) → [[Teorie slabého článku (O-ring)]].
7. **Trenér záleží, ale v mezích.** Peníze vysvětlí většinu dlouhodobého pořadí, trenér ~15 % – což ve fotbale malých marginů rozhoduje. Odvolání trenéra samo nepomáhá: tým by se vrátil k průměru i bez něj (Kap. 10–11) → [[Vliv trenéra a jeho výměna]].
8. **Analytika je způsob myšlení, ne statistiky.** Data dávají pravdu, ne návod; výhodu přinese organizace celého klubu (Kap. 7, 12) → [[Oddělení analýzy – struktura a role]].

## Klíčová čísla (výběr)

- Průměr **2,66 gólu na zápas** v top 5 ligách 1993–2011; nejčastější výsledek 1:1 (11,6 % zápasů PL) (Kap. 1).
- Výsledky obecně: **48 % výher domácích, 26 % remíz, 26 % výher hostů** (Spiegelhalter) (Kap. 1).
- Ve 43 000 zápasech anglické ligy vyhrál outsider ve **45,2 %** (Ben-Naim a kol.) (Kap. 1).
- Roh: **20,5 %** vede ke střele, 1 z 9 střel je gól → **~0,022 gólu na roh** (StatDNA, 1 434 rohů) (Úvod).
- Druhý gól přidá v průměru **+0,99 bodu**, pátý **+0,1** (top 4 ligy 2000–2011) (Kap. 3).
- Čisté konto ≈ **2,5 bodu** na zápas vs. jeden vstřelený gól ≈ 1 bod (PL 2001–2011) (Kap. 4).
- Hráč má míč v průměru **53,4 s** za zápas a uběhne s ním 191 m (~1 % času, ~1,5 % vzdálenosti) (Carling, Ligue 1) (Kap. 5).
- Tým s méně ztrátami než soupeř prohrál **28 %** zápasů, s víc ztrátami **48 %** (PL 2008–11) (Kap. 5).
- Červená karta stojí **~0,42 očekávaného bodu** – zhruba jako přijít o domácí prostředí (0,43) (Kap. 9).
- Mzdy vysvětlují **81 %** rozdílů v průměrném pořadí za dekádu, ale jen **59 %** v jedné sezóně (PL 2001–2011) (Kap. 10).

> [!note] Nesrovnalost uvnitř knihy
> Reepova data: v Úvodu „asi polovina gólů“ z míčů získaných ve vápně soupeře, v Kap. 6 „30 % gólů“ z final-third regains (?). Podíl mezd na pořadí: 92 % (Kap. 7) vs. 89 % (Kap. 10) – obojí citace Kuper & Szymanski.

> [!note] Aktualita (poznámka LLM – ověřit)
> - Castrol Edge rankings (hodnocení hráčů v Kap. 8) už neexistují; StatDNA koupil Arsenal (2012), Prozone/Amisco jsou dnes součástí Stats Perform.
> - „Hot hand“ jako omyl (Kap. 4) zpochybnila pozdější práce Miller & Sanjurjo (2018), podle níž se v původní analýze skrývalo statistické zkreslení.
> - Pravidlo střídání <58<73<79 je z doby tří střídání; od 2020 se smí střídat pětkrát.
> - Předpověď „~1 000 gólů v PL i v roce 2023“ nevyšla – v posledních sezónách padá v PL výrazně víc gólů.

## Co z toho plyne pro wiki / Sigmu

Kniha je **první generací** fotbalové analytiky: místo nových metrik testuje staré pravdy. Doplňuje [[Zdroj – Soccermatics]] (modely) a [[Zdroj – Football Hackers]] (lidé a organizace) o **nová témata**: slabý článek, hodnota obrany, ztráty místo držení, načasování střídání, regrese k průměru po výměně trenéra a integrace posil. Návrhy → [[The Numbers Game – návrhy pro Sigmu]].

## Lidé a organizace zmínění v knize

Analytici a výzkumníci: Charles Reep, Mike Hughes a Ian Franks, Chris Carling (Lille), Jaeson Rosenfeld a Sarah Rudd (StatDNA), Ian Graham (Decision Technologies → Liverpool), Steve Brown a Paul Graley (Everton), Boris Notzon (Köln SportLab), Steven Houston (Hamburg), Mike Forde (Chelsea), Martin Lames (TU München), Andreas Heuer, David Spiegelhalter, Bret Myers, Sue Bridgewater, Bas ter Weel, Boris Groysberg, Egon Franck a Stephan Nüesch. Trenéři: Roberto Martínez, Tony Pulis, Arrigo Sacchi, Valerij Lobanovskyj, Alex Ferguson, André Villas-Boas. Firmy: [[Opta]], Prozone/Amisco, StatDNA, Impire, Infostrada, Match Analysis, Deloitte.

## Souvislosti

[[Přehled wiki]] · [[Zdroj – Soccermatics]] · [[Zdroj – Football Hackers]] · [[Zdroj – Barça Match Analysis]] · [[The Numbers Game – návrhy pro Sigmu]]
