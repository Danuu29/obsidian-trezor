---
typ: synteza
tags: [prehled, moc]
aktualizovano: 2026-10-19
---
# Přehled wiki

Vrcholná syntéza: co wiki aktuálně ví a jak to do sebe zapadá. Katalog všech stránek je v [[index]].

## Velký obraz (k 2026-10-15)

Těžiště znalostí je **datová analytika a rozvoj hráčů v [[SK Sigma Olomouc]]**, realizovaná na platformě [[Yarmill]]. Práce běží ve třech propojených proudech:

1. **Rozvoj hráčů (akademie)** – herní identita [[Sigma Way]] → [[Postové profily]] → [[Hodnocení hráčů – metodika]] → [[Karta hráče – koncept]] → [[Individuální rozvojový plán (IDP)]] → [[Kariérní plán]], s programem [[Future Blue]] a [[Biologický věk]] jako klíčovým parametrem. Teoretickou páteří je [[Zdroj – FIFA Talent ID Guide]].
2. **Výkon a zdraví (kondice)** – [[GPS metriky a zatížení]], [[Silové testy a normy]], [[Denní připravenost a wellness]], [[Vstupní diagnostika hráče]]. Spojuje je princip [[Thresholdy a benchmarky]]: ukazovat vztah k normě, ne čísla.
3. **Herní data a aplikace** – [[SkillCorner]], [[Wyscout]], [[Eyeball]]; vlastní aplikace ([[Aplikace – Analýza soupeře]], [[Aplikace – Match tracker]], [[Aplikace – Analýza audio trenéra]]…) a [[Skauting – proces a reporting]].

4. **Herní a video analýza (metodika)** – od 15. 10. 2026 má wiki teoretickou páteř z [[Zdroj – Barça Match Analysis]]: [[Plány analýzy (micro, meso, macro)]], [[Herní cyklus]], [[Analýza soupeře – metodika]] → [[Operativní strategie a trénink]] → [[Mikrocyklus a značení MD]], cyklus zápasu ([[Předzápasová příprava a komunikace]], [[Live analýza a poločas]], [[Hodnocení utkání a pozápasový report]], [[Sezónní hodnocení týmu a soutěže]]) a stavba oddělení ([[Oddělení analýzy – struktura a role]], [[Typy sportovních dat a datová architektura]], [[Tagging a code window]]). Napojení na aplikace Sigmy → [[Barça kurz – návrhy pro Sigmu]].

5. **Kvantitativní analytika (modely a metriky)** – od 15. 10. 2026 z [[Zdroj – Soccermatics]]: [[Expected goals (xG)]], [[Possession value a Markovovy řetězce]], [[Pasové sítě a prostorové mapy]], [[Pressing a kolektivní pohyb]], [[Half-spaces a taktická geometrie]], [[Predikce a pravděpodobnostní modely]], [[Datový skauting – metriky a úskalí]]. Doplňuje Barça kurz (metodika) o čísla, validaci a lekce z klubů (Leicester vs. Villa, [[Brentford a FC Midtjylland]]) → [[Soccermatics – návrhy pro Sigmu]].

6. **Rozhodování a organizace (lidé, skauting, strategie)** – od 15. 10. 2026 z [[Zdroj – Football Hackers]]: [[Kognitivní zkreslení v hodnocení]], [[Výkon vs. výsledek a role náhody]], [[Packing]], [[Goalimpact a plus-minus]], [[Kognitivní trénink]], [[Osobnostní profily hráčů]], [[Strategie menšího klubu]]; entity [[Impect]], [[21st Club]]. Spojuje modely ze Soccermatics s praxí klubů: jak data prosadit, jak nehodnotit podle výsledku a jak menší klub hledá výhodu → [[Football Hackers – návrhy pro Sigmu]].

7. **Kádr, styl a trenéři (testování klišé)** – od 15. 10. 2026 z [[Zdroj – The Numbers Game]] (2013, nejstarší ze tří knih): [[Teorie slabého článku (O-ring)]], [[Hodnota gólu – útok vs. obrana]], [[Držení míče a ztráty]], [[Střídání a vyloučení]], [[Vliv trenéra a jeho výměna]]. Doplňuje modely a rozhodování o to, **jak skládat kádr** (nejslabší článek), **co měřit** (ztráty, body z gólů, obrana) a **jak zacházet s trenéry** (regrese k průměru, integrace) → [[The Numbers Game – návrhy pro Sigmu]].

8. **Komunikace dat (od analýzy k rozhodnutí)** – od 15. 10. 2026 z [[Zdroj – Persuading with Data]] (Kazakoff, MIT Sloan 2022): [[Vysvětlování dat – tři výzvy]], [[Vnímání grafů – preattentivní atributy a Gestalt]], [[Výběr grafu podle vztahu v datech]], [[Data-ink ratio a vizuální hierarchie]], [[Headline a testy slidu]], [[Minto pyramida]], [[WIIFT a přesvědčování publika]], [[TOP-T – prezentace grafu]], [[Audience Confusion Matrix]]. Průřezová vrstva nad proudy 1–7: předchozí knihy říkají, **co** měřit a **jak** rozhodovat, tato **jak výsledek předat, aby podle něj někdo jednal**. Zřejmě je i původním zdrojem Danůvých zásad vizualizace → [[Persuading with Data – návrhy pro Sigmu]].

Napříč vším platí [[Principy vizualizace a reportingu]] („trenéři chtějí informace, ne čísla“) – Barça kurz to potvrzuje: filtrovat, každé zjištění s doporučením, společný jazyk ([[Taktická komunikace]]).

## Hlavní napětí a mezery

- **Chybí game model** → IDP a profily se dělají „pocitově“. Sigma Way je první krok.
- **Role B-týmu** nevyjasněna → blokuje kariérní plány i C-tým ([[Struktura týmů A–B–C]]).
- **Normy nejsou konzistentní** (VALD) → [[Rozpory a nesrovnalosti]].
- **Data pro mládež** (herní data U17/U19, brankáři, normy pro mládež a dívky) chybí → [[Mapa datových zdrojů]].
- Priorita č. 1 v úkolech: **karta hráče**.
- **Vlastní video tagging a analytické oddělení** – metodika je teď ve wiki, ale není jasné, kdo v Sigmě vlastní tagging, jaký software a pod koho oddělení spadá → [[Otevřené otázky]].

- **Validace analytiky** – Soccermatics upozorňuje, že metody bývají neprokázané a vzorky malé; Sigma zatím nemá proces, jak ověřovat doporučení (skauting, hodnocení) → [[Predikce a pravděpodobnostní modely]].

- **Outcome bias v rozhodování** – Football Hackers ukazuje, že hodnocení trenérů, hráčů i zápasů podle výsledku je hlavní zdroj chyb; Sigma zatím nemá „tabulku spravedlnosti“ ani procesní KPI pro vedení → [[Výkon vs. výsledek a role náhody]].

- **Regrese k průměru v rozhodování** – The Numbers Game ukazuje, že odvolání trenéra i „funkčnost“ křiku jsou z velké části regrese k průměru; Sigma zatím nemá proces, jak takové rozhodnutí ověřit (kontrolní srovnání, deník rozhodnutí) → [[Vliv trenéra a jeho výměna]].

- **Komunikace výsledků** – Sigma nemá jednotnou šablonu grafů ani zvyk psát pointu (headline) a srovnání (threshold) ke každému grafu; „nepříjemná“ data (zásah bez efektu) nemají připravený postup → [[Persuading with Data – návrhy pro Sigmu]].

## Mimo fotbal

[[VIF Cycling team]] – hodnocení závodnic.

**Osobní kondice a trénink na kole** – od 19. 10. 2026 z [[Zdroj – Zátěžový test CPET 2026-09-21]]: [[CPET a laktátové schody]], [[Tréninkové zóny a prahy]], [[Klinika sportovní medicíny]] a projekt [[Osobní cyklistický trénink]] (jaro 2027, kontrolní CPET v prosinci). Spojnice s fotbalem: individuální zóny jsou stejný princip jako [[Thresholdy a benchmarky]]. Hlavní zjištění: velký „motor“ (VO₂max 58,6), rezerva ve výkonu na prazích.

**Práce se znalostmi a osobní efektivita** – od 15. 10. 2026 z [[Zdroj – Pořiďte si druhý mozek]] (Forte): [[Metoda CODE]], [[Zaznamenávání a oblíbené problémy]], [[PARA – organizace podle akčnosti]], [[Postupná sumarizace]], [[Dílčí balíčky a znovuvyužití práce]], [[Divergence a konvergence]], [[Revize a návyky druhého mozku]]. Je to zároveň **metodický rámec této wiki** ([[Druhý mozek – LLM Wiki]]: Danů zaznamenává a vyjadřuje, LLM uspořádává a zhušťuje) a zdroj pracovních návyků pro datové oddělení (checklisty projektů, MVP aplikací, knihovna šablon) → [[Druhý mozek – návrhy pro wiki a práci]]. Hlavní napětí: kniha radí zhušťovat až při použití a ukládat málo, wiki kompiluje celé zdroje předem.

## Kam dál

[[Otevřené otázky]] · [[Rozpory a nesrovnalosti]] · [[Mapa datových zdrojů]]
