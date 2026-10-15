---
typ: koncept
tags: [herni-data, metrika, xG, strely]
zdroje: ["[[Zdroj – Soccermatics]]"]
aktualizovano: 2026-10-15
---
# Expected goals (xG)

Pravděpodobnost, že střela skončí gólem, odhadnutá statistickým modelem z minulých střel z podobných situací. Týmové xG zápasu = součet xG všech šancí. Měří **kvalitu šancí (proces)**, ne výsledek ([[Zdroj – Soccermatics]], Kap. 12, 14, 15).

## Jak se počítá

- **Nejjednodušší model (Sumpter, 3 zóny):** malé vápno 32,2 % · zbytek vápna 12,4 % · mimo vápno 3,4 % (≈ 30 střel z dálky na gól). Zdroj polohy střel: FourFourTwo StatsZone.
- **Klubové modely:** x,y střely, typ přípravy (centr, through ball), část těla (hlava, volej, kontrolovaná střela). Každý klub má vlastní variantu, metodika je stejná (Kap. 14).
- **Úhel mezi tyčemi** je podle Sumptera „nejdůležitější jednotlivý faktor“: 38° ≈ 15 %, 17° ≈ 7 %; kontury se po stranách „zplošťují“. Výhoda pro komunikaci s trenérem: „čím víc branky vidíš…“ (Kap. 15).

## K čemu je dobré

- **Hodnocení výkonu nezávisle na náhodě** – týmy s vyšším xG v minulosti spíš vyhrávají budoucí zápasy (Kap. 14).
- **Udržitelnost konverze:** Sam Green (Opta, 2013) – United za Fergusona konvertovali nadprůměrně (střely ze středu), ale neudržitelně; za Moyese konverze spadla. Coutinho 2015/16: 4 góly z 69 střel z dálky vs. typických ~3 % → „spíš štěstí“ (Kap. 14, 15).
- **Krátká okna jsou šum:** Arsenal 11/2014 +5,3 xG rozdíl, přesto 3:4 na góly (Michael Caley; Kap. 13). Srov. [[Hodnocení utkání a pozápasový report]] („xG nemusí odpovídat výsledku“).

## Úskalí

- **Není to taktický recept.** xG je průměr minulých taktických bitev; neřekne, co funguje proti sobotnímu soupeři. Arsenal 2015/16 vedl ligu v xG, skončil 10 bodů za Leicesterem (Kap. 15).
- **Adaptace soupeře a „gaming“ metriky:** pokud tým maximalizuje xG (málo střel z dálky), soupeř zahustí vápno; pokud jsou hráči hodnoceni podle typu šancí, přizpůsobí se (Özil: 16 asistencí v 1. polovině sezóny, 3 ve 2.). *Goodhartův zákon – pojmenování LLM.*
- **Komunikace:** Tim Sherwood (Villa) po vyhazovu: „expected goals… What a load of nonsense“ – xG bez důvěry štábu nefunguje (Kap. 14) → [[Datový skauting – metriky a úskalí]].
- Jednoduchý 3zónový model v sázkovém experimentu nevydělával – užitečný popisně, ne jako zdroj výhody na trhu (Kap. 13).

> [!note] Aktualita (poznámka LLM – ověřit)
> Od 2016 jsou xG modely výrazně bohatší: pozice brankáře a obránců z freeze-frame / tracking dat, post-shot xG, xA, xT. Wyscout i StatsBomb dodávají xG standardně.

## Souvislosti

[[Possession value a Markovovy řetězce]] · [[Predikce a pravděpodobnostní modely]] · [[Hodnocení utkání a pozápasový report]] · [[Wyscout]] · [[StatsBomb]] · [[Opta]]
