---
typ: synteza
tags: [navrhy, pkm, druhy-mozek, wiki, sigma, produktivita]
zdroje: ["[[Zdroj – Pořiďte si druhý mozek]]"]
aktualizovano: 2026-10-15
---
# Druhý mozek – návrhy pro wiki a práci

*Syntéza / návrhy LLM*: co z [[Zdroj – Pořiďte si druhý mozek]] přenést **(A) do této wiki**, **(B) do práce v datovém oddělení [[SK Sigma Olomouc]] a [[Yarmill]]** a **(C) do osobní praxe Danů**. Nic není rozhodnuté – seznam k probrání. Změny schématu [[CLAUDE]] jen po odsouhlasení.

## Kde se kniha a wiki rozcházejí

> [!warning] Napětí (ne rozpor ve faktech)
> 1. **Kdy zhušťovat:** Forte radí zhušťovat až při použití (*just-in-time*), wiki kompiluje při ingestu (*just-in-case*). Důvod: u knihy je zhuštění drahý lidský čas, u wiki ho dělá LLM. Riziko wiki: **nadměrné zvýrazňování** – dlouhé stránky, které nikdo nečte.
> 2. **Kolik ukládat:** kniha ≤ 10 % zdroje a jen co rezonuje; wiki čte zdroj celý. Filtr rezonance tak dělá Danů jen výběrem zdroje, ne uvnitř něj.
> 3. **Jak třídit:** kniha podle akčnosti (projekty první), wiki podle typu stránky (koncepty = „zdroje“ v PARA). Akční vrstva jsou jen `projekty/` a syntézy „návrhy“.

## A. Wiki

1. **Oblíbené problémy Danů** jako filtr pro Web Clipper i pro důrazy při ingestu. Seznam musí sepsat Danů; LLM může nabídnout kandidáty z [[Otevřené otázky]] (např. *Jak ukázat trenérům informace místo čísel?*, *Jak hodnotit hráče bez vlivu výsledku?*) → [[Zaznamenávání a oblíbené problémy]].
2. **Vrstva oblastí** (PARA): přehledové stránky typu „Datová analytika Sigma“, „Yarmill“, „Cyklistika a trénink“, „Osobní efektivita“ – vstupní body podle odpovědnosti, ne podle tématu. Alternativa: jen rozšířit [[Přehled wiki]] → [[PARA – organizace podle akčnosti]].
3. **„Aktuální stav“ na projektových stránkách** (Hemingwayův můstek): poslední krok, další krok, blokery. U pozastavených projektů povinně → [[Revize a návyky druhého mozku]].
4. **Archiv**: hotové nebo zrušené projekty a zastaralá tvrzení přesouvat do `wiki/archiv/` místo mazání.
5. **Vracet vlastní výstupy** (reporty, prompty, prezentace, zadání) jako zdroje – „dokončené projekty jsou kyslík systému“ → [[Dílčí balíčky a znovuvyužití práce]].
6. **Rytmus údržby:** týdně ingest `raw/` (inbox), měsíčně lint + revize [[Přehled wiki]] a [[Otevřené otázky]]. Ingest zůstává ruční (rozhodnutí Danů).
7. **Pojistka proti „nadměrnému zvýrazňování“:** každá stránka má mít nahoře 1–2 věty shrnutí (už ve schématu) a délku držet tak, aby šla přečíst za pár minut; detail patří do surového zdroje.
8. **Konvergence:** po každém ingestu nejen „návrhy“, ale i otázka *„Co z toho Danů reálně udělá tento měsíc?“* – zmenšení rozsahu na 1–3 kroky → [[Divergence a konvergence]].

## B. Práce v Sigmě / Yarmillu

1. **Checklist zahájení aplikace / reportu:** zeptat se wiki (dotaz), co už víme; definovat kritéria úspěchu a premortem; **checklist dokončení:** postmortem a uložení znovupoužitelných kusů → [[Revize a návyky druhého mozku]].
2. **MVP přes zmenšení rozsahu** u [[Aplikace – Analýza soupeře]] a [[Aplikace – Analýza audio trenéra]]: jedna funkce pro jednoho trenéra, zpětná vazba, pak další verze → [[Divergence a konvergence]].
3. **Knihovna dílčích balíčků** datového oddělení: šablony reportů, grafy, prompty, definice metrik, normy – základ pro [[Analytické balíčky Yarmill]] a nové kluby → [[Dílčí balíčky a znovuvyužití práce]].
4. **Reporty ve vrstvách** (postupná sumarizace): nahoře 3 zjištění + doporučení pro trenéra, pod tím detail → [[Principy vizualizace a reportingu]], [[Postupná sumarizace]].
5. **[[Aplikace – Strategická aplikace]] organizovat podle akčnosti:** podle role a situace („nový trenér U15 – první týden“, „před zápasem“), ne podle oddělení; tato wiki jako prototyp.
6. **Týdenní revize datového oddělení:** inbox požadavků od trenérů, stav aplikací, priority na týden.
7. **Zkreslení aktuálnosti** v analýze a hodnocení: sbírat podklady průběžně („pomalé zahřívání“), ne jen poslední zápas → [[Kognitivní zkreslení v hodnocení]].

## C. Osobní praxe (doplní Danů)

1. Sepsat **12 oblíbených problémů** a uložit je jako poznámku ve vaultu.
2. **Read-later + automatický export zvýraznění** do `raw/` (kniha to doporučuje jako první krok).
3. **Týdenní revize** v kalendáři (e-mail, kalendář, plocha, inbox poznámek, úkoly na týden).
4. Pravidlo **80 %**: dotahovat hlavně projekty, ke kterým je materiál už nasbíraný.

## Souvislosti

[[Druhý mozek – LLM Wiki]] · [[Metoda CODE]] · [[Otevřené otázky]] · [[Přehled wiki]]
