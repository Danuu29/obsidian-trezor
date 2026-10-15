---
typ: koncept
tags: [predikce, statistika, pravdepodobnost, rozhodovani, metodika]
zdroje: ["[[Zdroj – Soccermatics]]", "[[Zdroj – Football Hackers]]", "[[Zdroj – The Numbers Game]]"]
aktualizovano: 2026-10-15
---
# Predikce a pravděpodobnostní modely

Jak modelovat výsledky zápasů a sezóny, jak vyhodnocovat předpovědi (expertů, modelů, skautů) a jak z pravděpodobností dělat rozhodnutí. Hlavní poselství: **náhoda je velká, vzorky malé a benchmark povinný** ([[Zdroj – Soccermatics]], Kap. 1, 4, 6, 11–13).

## Modely

- **Poissonovo rozdělení gólů:** gól může padnout kdykoli se stejnou pravděpodobností (PL 2012/13: 2,79 gólu / 90 min ≈ 0,031 za minutu). Rozložení počtu gólů sedí na Poisson (PL i NHL). Skóre jednotlivého zápasu je náhodné, sezóna předvídatelná.
- **Simulace sezóny:** útočná a obranná síla každého týmu (doma/venku) → simulace všech zápasů 10 000× → pravděpodobnost titulu (Liverpool 11,5 %, United 26,2 %…). Výsledek je rozložení, ne jedna tabulka.
- **Poissonova regrese s výkonovými ukazateli** (Kap. 12): góly ~ exp(a + b·passing rate + c·xG). xG i pasová frekvence předpovídaly góly lépe než minulé výsledky. Samotné **držení míče góly mezi vyrovnanými týmy nepředpovídá** (vedoucí tým často míč přenechá).
- **Elo / Euro Club Index:** přesun bodů mezi týmy podle výsledku a síly soupeře. Reaguje pomalu, nepřeceňuje formu.
- **Extrémní hodnoty:** Gumbelovo rozdělení pro „jak vzácný je výkon“ (Messi 50 gólů ≈ 1× za 73 let). Pravidlo odhadu: P(rekord letos) ≈ 1/(počet sezón bez rekordu + 1). Předpoklad „žádný trend“ často neplatí (Kap. 4).

## Vyhodnocování předpovědí

- **Naivní benchmark:** loňská tabulka (průměrná chyba ~2,2 místa) nebo průměrná změna pozice (~2,9). Z 17 expertů 2014/15 loňskou tabulku porazil jen 1, z 14 expertů 2013/14 13 horších než benchmark (Simon Gleave).
- **Kurzy sázkových kanceláří** jsou silný, kalibrovaný odhad („lidmi postavený index“). Implikovaná pravděpodobnost = 1/kurz; součet > 100 % je marže (typicky 5–6 %) → normalizovat.
- **Kalibrace:** porovnat implikované a skutečné četnosti (např. favorité s kurzem 1,33–1,43 vyhráli 89 % místo 70–75 %; logistická regrese).
- **Štěstí vs. dovednost:** při 50 sázkách vyhraje hráč se skutečnou výhodou 1 % nad náhodným jen v **62,6 %** simulací → krátké série nerozliší. Platí i pro hodnocení skautů, trenérů a rozhodnutí (*přenos LLM*).
- **Moudrost davu:** nezávislé odhady → medián bývá přesnější než jednotlivci (medián robustnější než průměr). Dav selhává při kopírování (informační kaskády) a u úloh vyžadujících počty.

## Rozhodování z pravděpodobností

- **Očekávaná hodnota:** sázet / rozhodnout se jen když p > 1/kurz – maximalizovat EV, ne „trefit vítěze“. **Kellyho kritérium** pro velikost sázky podle výhody.
- **Útok vs. obrana při 3 bodech za výhru** (Kap. 6): bránit se vyplatí jen pokud **l > 2w** (soupeř má víc než 2× vyšší šanci vyhrát). Za 2 bodů by slabší tým bránil vždy. Evoluční simulace manažerských pravidel tuto strategii („Twice“) vybere sama.
- **Ensemble:** převést každý model na W/D/L, zprůměrovat, váhovat podle historické úspěšnosti.

> [!warning] Slabiny Sumpterova experimentu
> Sázková strategie „odds bias“ (+140 % na 90 zápasech, „96,4 %“) byla zvolena se znalostí dat → riziko vícenásobného srovnávání a look-ahead biasu. Trhy jsou dnes efektivnější (*poznámka LLM*).

## Využití v klubu (návrh)

- Pre-match W/D/L z kurzů jako vstup do [[Aplikace – Analýza soupeře]] a doporučení „útočit / bránit“.
- Hodnocení výsledku vs. výkonu (xG) v [[Hodnocení utkání a pozápasový report]] – oddělit štěstí.
- Recruitment meetingy: **nezávislá písemná hodnocení před diskusí**, medián, sledovat úspěšnost doporučení v čase (srov. false positives / negatives v [[Typy sportovních dat a datová architektura]]).

## Profesionální sázkaři (Football Hackers)

- **Smartodds (Benham) a Starlizard (Bloom)** – sázkové firmy s matematiky a statistiky (často PhD); kurzy počítají modely, ne pocit. **Asijský handicap** eliminuje remízu a zjednodušuje pravděpodobnosti.
- Signál: kvalita šancí (ručně kategorizovaná „watchery“), vliv konkrétních hráčů (absence/návrat), délka cesty na venkovní zápas (kratší = o něco vyšší šance), „měkké“ informace (konflikty v kabině). Šum: výsledek posledního zápasu, vzájemné zápasy, „nepříjemný soupeř“, série penaltových rozstřelů (Anglie vs. Německo by podle Benhama vyšla podobně při hodu mincí).
- Podle Benhamova modelu vyhrál Bundesligu 2007 až 4. nejlepší tým (Stuttgart) a 2009 3. nejlepší (Wolfsburg).
- Zkreslení dopadá i na experty: Benham jako fanoušek po jednom špatném zápase „viděl“ svůj tým na sestupu, jako analytik by ho posunul o jedno místo.
- Tipy si zapisovat předem a zpětně kontrolovat (lekce pokory).

Zdroj: [[Zdroj – Football Hackers]] (Kap. 1–3) → [[Výkon vs. výsledek a role náhody]].

## Poisson, zákon velkých čísel a konvergence lig (The Numbers Game)

Podle [[Zdroj – The Numbers Game]] (Kap. 1–2):
- **2,66 gólu na zápas** (top 5 lig 1993–2011) a Poissonovo rozdělení stačí k odhadu sezóny PL: ~30 zápasů 0:0, ~70 s jedním gólem, ~95 se dvěma, ~80 se třemi, ~55 se čtyřmi, ~50 s pěti a víc. Skutečnost má o něco víc 0:0 a 1:1, než Poisson čeká (PL 8,3 % bezbrankových vs. 7,7 % podle modelu) – týmy hrají na remízu.
- Nejčastější výsledky PL 2001–2011: **1:1 (11,6 %)**, 1:0 (10,9 %), 2:1 (9,4 %), 2:0 (8,7 %), 0:0 (8,3 %), 0:1 (7,6 %).
- **Zákon velkých čísel:** kdo hraje dost dlouho, zažije všechno – i obrat z 0:3 (Liverpool poprvé za 112 let v Istanbulu 2005). Extrémy nejsou zázraky.
- **Vývoj gólů:** v anglické nejvyšší soutěži klesal průměr z ~4,5 (90. léta 19. stol.) na ~2,6 (1996), od 70. let je stabilní. Změny pravidel (ofsajd 1925, 3 body 1981, zákaz malé domů 1992) měly jen krátkodobý vliv. Pokles nevysvětluje ani rostoucí kvalita hráčů (Palacios-Huerta: stejný trend ve všech soutěžích, i když se rozdíly v kvalitě mezi nimi zvětšily). Vysvětlení: šíření taktiky a organizace.
- **Ligy jsou vyrovnanější, ne méně:** průměrný gólový rozdíl v zápase klesl za sto let z více než 1 na méně než 0,5.
- **Top 4 ligy jsou v číslech skoro stejné** (2010/11): 425–449 přihrávek, 13–14,5 střel, 4,4–4,8 na branku, ~5 rohů, 0,14 penalty na tým a zápas. Liší se fauly (PL 24 vs. La Liga 34) a žluté karty (3,2 vs. 5,1). Rozdíly mezi ligami jsou menší než meziroční výkyvy; v nižších ligách (Eredivisie, Ligue 1, MLS) jsou větší.

> [!note] Aktualita (poznámka LLM – ověřit)
> Předpověď „stabilně ~1 000 gólů za sezónu PL“ (Kap. 12) nevyšla: v posledních sezónách padá v PL výrazně víc gólů. Stabilita gólovosti tedy není trvalý zákon.

## Souvislosti

[[Expected goals (xG)]] · [[Datový skauting – metriky a úskalí]] · [[Sezónní hodnocení týmu a soutěže]] · [[Brentford a FC Midtjylland]] · [[Výkon vs. výsledek a role náhody]] · [[Goalimpact a plus-minus]]
