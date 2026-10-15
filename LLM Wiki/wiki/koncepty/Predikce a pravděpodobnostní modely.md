---
typ: koncept
tags: [predikce, statistika, pravdepodobnost, rozhodovani, metodika]
zdroje: ["[[Zdroj – Soccermatics]]"]
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

## Souvislosti

[[Expected goals (xG)]] · [[Datový skauting – metriky a úskalí]] · [[Sezónní hodnocení týmu a soutěže]] · [[Brentford a FC Midtjylland]]
