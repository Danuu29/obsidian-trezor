---
typ: zdroj
tags: [zdroj, kniha, analytika, xG, tracking, predikce, skauting]
cesta: "LLM Wiki/raw/Soccermatics (Sumpter 2016).pdf"
ingest: 2026-10-15
aktualizovano: 2026-10-15
---
# Zdroj – Soccermatics

Kniha **David Sumpter: *Soccermatics – Mathematical Adventures in the Beautiful Game*** (Bloomsbury Sigma, 2016; *Pro-Edition* s doplněnou částí IV „The Analysts“, události do 2016/17). Sumpter je profesor aplikované matematiky (Uppsala), specialista na kolektivní chování zvířat. Kniha populárně ukazuje, jak matematické modely (pravděpodobnost, sítě, geometrie, teorie her, kolektivní pohyb) vysvětlují fotbal – a jak se analytika reálně používá v klubech.

> [!info] Poznámky ke zdroji
> - PDF má textovou vrstvu (293 s.); vzorce a tabulky z obrázků v textu chybí – kde je LLM dopočítalo, je to označeno *dopočet*.
> - Kniha je z let 2016–17. Data, firmy a role lidí jsou historické; místa, kde se obor posunul, jsou na stránkách označena calloutem **Aktualita** (*poznámka LLM – ověřit*).
> - Citace: **Kap. 7** = kapitola knihy; čísla stran PDF se neuvádějí (tisková sazba).
> - Polovina knihy jsou analogie mimo fotbal (ryby, mravenci, slizovky, rakovina) – do wiki přeneseno jen to, co se týká fotbalu a analytiky.

## Struktura knihy

| Část | Kapitoly | Téma → stránka wiki |
|---|---|---|
| I – On the Pitch | 1 Poissonovo rozdělení gólů · 2 Barcelona: trojúhelníky, Voronoi · 3 flow fields, bránění 1v1, Pirlo vs. Schweinsteiger · 4 extrémní výkony, hodnoticí indexy, statistický skauting · 5 fyzika střely (Zlatan), míče | [[Predikce a pravděpodobnostní modely]] · [[Half-spaces a taktická geometrie]] · [[Pasové sítě a prostorové mapy]] · [[Datový skauting – metriky a úskalí]] |
| II – In the Dugout | 6 3 body za výhru → útočit, nebo bránit · 7 taktická mapa (pasové sítě, centralizace, hulls) · 8 spolupráce v týmu, Lobanovskyj · 9 tracking data, synchronizace, pressing (Prozone) | [[Predikce a pravděpodobnostní modely]] · [[Pasové sítě a prostorové mapy]] · [[Pressing a kolektivní pohyb]] |
| III – From the Crowd | 10 sociální nákaza (chorály, potlesk, přestupové fámy) · 11 moudrost davu, experti vs. benchmark · 12–13 vlastní sázkový experiment (5 strategií, xG model, Kelly) | [[Predikce a pravděpodobnostní modely]] · [[Expected goals (xG)]] |
| IV – The Analysts | 14 hledání talentu (Leicester vs. Villa, radary, xG, Markov, defenzivní metriky) · 15 budoucnost (half-spaces, xG a úhel, #HackMCFC, workflow analytiků) | [[Datový skauting – metriky a úskalí]] · [[Possession value a Markovovy řetězce]] · [[Expected goals (xG)]] · [[Half-spaces a taktická geometrie]] · [[Oddělení analýzy – struktura a role]] |

## Hlavní myšlenky

1. **Náhoda + struktura + „magie“.** Góly přicházejí náhodně (Poisson), proto je jednotlivý zápas těžko předvídatelný, ale sezóna předvídatelná je. Zajímavé je to, co náhodou vysvětlit nejde – struktura týmu (Kap. 1, 5, 15).
2. **Struktura je geometrie.** Dobré pokrytí prostoru = dobré pasové možnosti (Delaunay triangulace ↔ Voronoi zóny). Hráči nepočítají geometrii, řídí se jednoduchými pravidly pohybu naučenými v tréninku (Kap. 2, 9).
3. **Analytik má dodat „taktickou mapu“, ne metodu.** Jednoduchý vizuál vysvětlitelný o poločase; trenér se ptá „so what?“ (Kap. 7, 15) → [[Principy vizualizace a reportingu]].
4. **Měřit přidanou hodnotu, ne objem.** Mnoho skluzů může znamenat špatné postavení, vysoká přesnost přihrávek bezpečnou volbu; lepší je xG, změna pravděpodobnosti gólu (Markov), „patch“ metriky obránců (Kap. 4, 14).
5. **Benchmark a vzorek.** Experti většinou neporazí loňskou tabulku; trh (kurzy) je silný odhad; 50 pokusů neodliší štěstí od dovednosti (Kap. 11–13).
6. **Data fungují jen s důvěrou.** Leicester i Villa použily stejný statistický skauting – rozhodla důvěra mezi štábem a analytiky (Kap. 14) → [[Oddělení analýzy – struktura a role]].
7. **Validace.** Analytici sami přiznávají, že své metody nemají prokázané („art more than science“) – „nikdy slepě nevěřit tomu, co děláš“ (Kap. 14).

## Klíčová čísla (výběr)

- Průměr gólů PL 2012/13: 2,79 / zápas, rozložení ≈ Poisson (Kap. 1).
- Pravidlo 3 bodů: **útočit, pokud soupeř nemá víc než 2× vyšší šanci na výhru** (Kap. 6).
- Pasová frekvence 5/min vs. 3/min ≈ +20 % gólů za sezónu; decentralizace ≈ +8 % (Grund 2012; Kap. 7).
- Counter-press (Prozone, PL): 1. hráč do **~2,3 s**, 2. do **~5,5 s**; Bielsův Marseille presoval 43 % akcí soupeře vs. ~25 % v PL (Kap. 9).
- Jednoduché xG: malé vápno 32,2 %, zbytek vápna 12,4 %, mimo vápno 3,4 % (Kap. 12).
- Kanté 2014/15 nejvíc úspěšných skluzů v Evropě → Leicester ~5,6 mil. £ → Chelsea 32 mil. £ (Kap. 14).

## Co z toho plyne pro wiki / Sigmu

Kniha doplňuje [[Zdroj – Barça Match Analysis]] (metodika video analýzy) o **kvantitativní stranu**: modely, metriky, validaci a predikci. Konkrétní návrhy → [[Soccermatics – návrhy pro Sigmu]].

## Lidé a organizace zmínění v knize

Analytici: Omar Chaudhuri (21st Club), Ted Knutson ([[StatsBomb]]), Sam Green ([[Opta]] → Aston Villa), Sarah Rudd (StatDNA/Arsenal), Thom Lawrence (Deep XG), Marek Kwiatkowski, Paul Power (Prozone), Ian Graham (Liverpool), René Marić (Salzburg), Rory Campbell (West Ham), Lucy Rushton (Atlanta United), Dan Altman (North Yard Analytics), Simon Gleave (Infostrada). Kluby: [[Brentford a FC Midtjylland]], Leicester, Aston Villa, Arsenal (StatDNA), Manchester City (#HackMCFC), Fulham. Výzkum: Grund (2012), Vestberg et al. (2012), Lucey et al. (2015), Bialkowski et al. (2014), Folgado et al., McHale & Scarf (2012).

## Souvislosti

[[Přehled wiki]] · [[Zdroj – Barça Match Analysis]] · [[Soccermatics – návrhy pro Sigmu]] · [[Normalizace herních dat]] · [[Hodnocení utkání a pozápasový report]]
