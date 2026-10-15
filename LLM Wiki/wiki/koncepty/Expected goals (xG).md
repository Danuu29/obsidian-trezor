---
typ: koncept
tags: [herni-data, metrika, xG, strely]
zdroje: ["[[Zdroj – Soccermatics]]", "[[Zdroj – Football Hackers]]", "[[Zdroj – The Numbers Game]]"]
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

## Rozšíření a historie (Football Hackers)

Podle [[Zdroj – Football Hackers]] (Kap. 2, 5):
- **Původ:** koncept popsal Sam Green (OptaPro) 2012; profesionální sázkaři (Benham, Smartodds) ale kategorizovali šance pomocí „watcherů“ u obrazovek už dřív a přesněji. Kontext střely (protiútok, standardka, hlavička, počet obránců mezi střelcem a brankou) mění pravděpodobnost výrazně. Penalta v PL ~77 %.
- **Kvalita zakončení je u elitních hráčů malá veličina:** Ronaldo proměnil o ~2 p. b. víc než průměr (1–2 góly za sezónu navíc), ale díky **pozicím střel a jejich počtu** dal o 8–10 gólů víc než průměrný útočník (Chaudhuri). Lewandowski měl stabilní xG/střelu rok co rok – útočníci mají individuální tendence.
- **Odvozené metriky:**
  - **After Shot xG** (Trainor) – hodnotí i trajektorii: zablokovaná a mimo branku = 0, střela do těžkého místa = vysoká hodnota → hodnocení zakončení i brankářů.
  - **xG Against vs. obdržené góly** = **Keeping Goals Prevented** (Opta) – výkon brankáře očištěný od kvality obrany.
  - **xA – Expected Assists** (Devin Pleuler, 2012) – pravděpodobnost, že přihrávka bude asistencí, nezávisle na zakončení (Groß v Ingolstadtu: xA téměř 2× vyšší než skutečné asistence → Brighton).
  - **xGChain** – xG střely připíše všem hráčům nepřerušené posese (i brankáři a stoperovi); **pre-xGC** bez střelce a asistenta → odhalí „motor“ týmu (Lahm, Kimmich, Xabi Alonso).
  - **xGplots** (Ijtsma) – časová osa šancí v zápase → [[Výkon vs. výsledek a role náhody]].
- **Trenéři** podle Ijtsmy hodnotí šance svého týmu přesně, šance soupeře výrazně hůř.
- **Mainstream:** BBC Match of the Day (2017), The Times tabulka xPoints (2018/19), Sky.

> [!info] Zpřesnění: dlouhodobé překonávání xG (Favre)
> Stránka výše říká, že nadprůměrná konverze bývá neudržitelná. Favreho Gladbach však tři sezóny po sobě dával ~1,2 gólu na 1 xG (šance ~1 %, že jde o náhodu) a podobně Nice i Dortmund. Vysvětlení: tehdejší modely nezohledňovaly **počet obránců mezi střelcem a brankou (shot clarity)** a **tlak na střelce (shot pressure)** – Favreho týmy střílely s ≤ 2 hráči v cestě a soupeře nutily do střel pod tlakem. Nejde o rozpor, ale o **slepé místo modelu**: překonávání xG je udržitelné, pokud tým systematicky vytváří kvalitu, kterou model nevidí. Novější modely (StatsBomb, Opta) tyto faktory zahrnují ([[Zdroj – Football Hackers]], Kap. 5).

## Konverze střel (The Numbers Game)

Podle [[Zdroj – The Numbers Game]] (Úvod, Kap. 1, 6, 7) – doba před rozšířením xG:
- **Gól z 1 z ~9 střel** je stabilní poměr už od Reepových dat (1953–67); Heuer odhaduje 1 z 8. I střely po rozích končí gólem asi v 1 z 9 případů.
- Tým s víc střelami vyhraje jen 47 % zápasů → rozhoduje kvalita šancí, ne počet (argument pro xG).
- **Délka akce:** střely po krátkých akcích jsou efektivnější (1 z 9 vs. 1 z 15), ale dlouhé akce přinesou víc střel; úspěšné týmy mají stejnou konverzi jako neúspěšné a o třetinu víc střel (Hughes & Franks) → [[Držení míče a ztráty]].
- Penalta ~77 %, střela ze hry ~12 % (PL od 2009).
- Wigan (Martínez) střílel záměrně z dálky (průměr ~24 m) – nízká kvalita šancí jako vědomá volba stylu → [[Strategie menšího klubu]].

## Souvislosti

[[Possession value a Markovovy řetězce]] · [[Predikce a pravděpodobnostní modely]] · [[Hodnocení utkání a pozápasový report]] · [[Wyscout]] · [[StatsBomb]] · [[Opta]] · [[Výkon vs. výsledek a role náhody]] · [[Packing]]
