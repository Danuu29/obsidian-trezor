---
typ: koncept
tags: [tracking, pressing, kolektivni-pohyb, taktika]
zdroje: ["[[Zdroj – Soccermatics]]", "[[Zdroj – Football Hackers]]"]
aktualizovano: 2026-10-15
---
# Pressing a kolektivní pohyb

Co tracking data říkají o pohybu týmu jako celku – pressing, synchronizace, vůdcovství, dostupné přihrávky. Sumpter přenáší metody ze studia hejn a rojů; hodnota je v přenosu **matematiky**, ne metafory ([[Zdroj – Soccermatics]], Kap. 3, 9).

## Pressing (Prozone, Paul Power – celá sezóna PL, 260 mil. datových bodů)

- **Counter-press** (po ztrátě na soupeřově polovině): první hráč u míče do **~2,3 s** (koučovací bod ~2,5 s), druhý do **~5,5 s**. Zpřesňuje Guardiolovo pravidlo 6 s. „260 milionů datových bodů, dva koučovací body.“
- **Deep press** (obrana poslední třetiny): klíč je **zpomalit postup míče**; na míč jde **jen jeden** hráč, ostatní blokují kanály. Víc hráčů na míči otevírá pasovou síť soupeře. „Deep defending is about stability, counter-defending about dynamism.“
- Intenzita: Bielsův Marseille 2014/15 presoval **43 %** akcí soupeře s míčem vs. ~25 % u týmů PL. Lyon vs. Marseille: presink zúžil Lyonu dopředné možnosti; když v 64′ polevil, 10 přihrávek a gól.
- **Pressing jako minimalizace prostoru:** Barcelona 2011 prostor maximalizovala, Bayern 2013 ho soupeři minimalizoval (7:0 v semifinále CL) (Kap. 3).
- Bránění 1v1 (Badstuber): napadnout hned, zůstat blízko, nepadat do skluzu, „ukázat“ útočníkovi cestu od branky. Model obrany zón (Pan et al. 2012): obránce mezi útočníkem a cílem jde nejdřív přímo na útočníka, druhý zmenšuje prostor – bez komunikace stačí reagovat na pozici útočníka.

> [!info] Vztah k Sigma Way
> [[Sigma Way]] má represink „do 6 s, jinak zpět“. Data Prozone nabízejí jemnější cíle (1. hráč ~2,5 s, 2. ~5,5 s) – *návrh* je převzít jako měřitelné KPI. Čísla jsou z PL 2014/15; intenzita presinku od té doby vzrostla → ověřit na aktuálních datech.

## Tracking metriky kolektivu

- **Dostupné přihrávky** (Prozone): každých 0,1 s je přihrávka „životaschopná“, pokud ji příjemce zpracuje do 1 m a žádný obránce nezachytí do 1 m → síť dostupných přihrávek.
- **Alignment (polarizace):** součet směrových vektorů hráčů; bránící tým bývá zarovnanější, útočící zarovnání rozbíjí, aby vytvořil prostor.
- **Synchronizace (Folgado et al.):** nejvíc synchronizovaní obránci a střední záložníci, nejméně útočníci. Při **3 dnech mezi zápasy** nižší týmová synchronizace než při 6+ dnech, ačkoli vzdálenost a rychlost se neměnily → únava se může projevit spíš kognitivně/takticky než fyzicky.
- **Vůdcovství přes lag:** posunout časové řady a najít zpoždění s maximálním zarovnáním → kdo se otáčí první. Příklad: kapitán (záložník) vedl pohyb obránců bez toho, že by dominoval v držení míče.
- **Identifikace formace** z průměrných pozic (Bialkowski et al. 2014) – varianty 4-4-2 mezi týmy.
- **Predikce šance ze stavu hry** (Lucey et al. 2015): vychýlení obránců z pozic, rychlosti, počet obránců mezi míčem a brankou → nejlepší šance z protiútoků.
- Vicsek model: stačí sledovat sousedy v okruhu ~10 m a koordinace celého týmu vznikne sama. Hráči nepočítají geometrii – řídí se jednoduchými pravidly naučenými v tréninku (Michels: cvičit rozpoznání situace, ne izolované drily).

> [!note] Aktualita (poznámka LLM – ověřit)
> Sumpter v roce 2016 píše, že analýza pohybu je „v plenkách“ a kluby data nesdílejí. Dnes jsou tracking data běžná (broadcast tracking [[SkillCorner]], otevřená data Metrica / StatsBomb 360) a existují modely pitch control, EPV, hodnota náběhů bez míče.

## Trénink (Kap. 3)

GPS (5 Hz) na mládeži: 2v1 v řadě je špatné cvičení (obránce vždy vyhraje); se 4. hráčem vznikají **dynamické trojúhelníky** a obránce může jen napadat míč. Zobrazení „kondenzační stopy“ pohybu.

## PPDA a další metriky presinku (Football Hackers)

- **PPDA – passes per defensive action** (Colin Trainor; definice obranných akcí podle Opty: skluzy, neúspěšné skluzy, interceptions, fauly) – počet přihrávek soupeře na jednu obrannou akci v prvních ~60 m od soupeřovy branky. **Nižší = intenzivnější presink.**
- Dortmund pod Kloppem: 8,76 (2012/13) → 8,72 → **9,59** v krizovém podzimu 2014; soupeř si mohl dovolit v průměru o přihrávku víc. Rozpad podle hráčů: Lewandowski nechyběl jen gólově, ale i v presinku; náhrada Immobile měl zhruba poloviční počet obranných akcí.
- **Krawietzova výhrada:** PPDA ovlivňuje plán na konkrétní zápas – někdy tým záměrně nechá soupeře 2–3 přihrávky a napadá až v místě, kde je soupeř nepohodlný. Metriku číst v kontextu herního plánu.
- Opta sekvence: přihrávky soupeře na sekvenci bez míče – City 2,4 (nejaktivnější) vs. Swansea 3,9 (PL 2017/18).
- Nagelsmann: raději donutit soupeře ke špatné přihrávce než vyhrávat 1v1 souboje; zisk tak, aby tým měl rychlostní výhodu proti roztaženému soupeři ([[Kognitivní trénink]]).
- [[Packing]]: zisky s mnoha vyřazenými soupeři jsou typické pro gegenpressing.

Zdroj: [[Zdroj – Football Hackers]] (Kap. 5, 7).

## Souvislosti

[[GPS metriky a zatížení]] (kongesce zápasů) · [[Herní cyklus]] · [[Obranná linie – principy]] · [[Pasové sítě a prostorové mapy]] · [[Operativní strategie a trénink]] · [[SkillCorner]] · [[Packing]]
