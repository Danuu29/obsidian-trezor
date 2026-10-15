---
typ: koncept
tags: [skauting, metrika, plus-minus, talent, predikce]
zdroje: ["[[Zdroj – Football Hackers]]"]
aktualizovano: 2026-10-15
---
# Goalimpact a plus-minus

Hodnocení hráče podle toho, **jak si tým vede, když je hráč na hřišti** – bez ohledu na to, co hráč konkrétně dělá. Převzato z basketbalového **plus-minus**; ve fotbale ho rozvinul Jörg Seidel (manažer energetické firmy z Hamburku, bez fotbalového zázemí) jako **Goalimpact** ([[Zdroj – Football Hackers]], Kap. 6).

## Princip

- Vstup: jen **sestavy, střídání a časy gólů**. Žádné běhy, přihrávky ani střely.
- Výstup: čistý přínos hráče k rozdílu skóre, podobně jako Elo v šachu nebo handicap v golfu. „Umím říct, že je hráč dobrý, ale ne proč“ (Seidel, parafráze).
- Úpravy: síla ligy a týmu, **věk** (vrchol kolem 26 let), u mládeže **relative age effect**.
- Potřebuje data alespoň **dvou sezón**; databáze ~320 000 hráčů z 200+ soutěží včetně nižších lig, které velcí provideři nepokrývají.

## Proč to dává smysl

- Zachytí hráče, jejichž přínos klasické statistiky nevidí – „lepidlo“ týmu, správné postavení, organizace (basketbal: Chuck Hayes).
- Lidské vnímání podle Seidela přeceňuje **akce** (driblinky, góly), **minutáž** („nehraje, tak je slabý“) a **útočnou hru**.
- Případy z knihy: včasné označení Sadia Mané (Salzburg → Southampton) i Alphonse Daviese (Vancouver, ~0,45 mil. € → Bayern 10 mil. €); naopak Bakayoko (Chelsea, 40 mil. €) podle modelu nikdy neměl úroveň PL. Průměr sestav Brazílie 128 vs. Německo 154,8 před semifinále MS 2014.
- Hodnotí i trenéry: kdo soustavně překonává predikci modelu (Guardiola, Streich), dostává z týmu víc než součet hráčů.
- **Projekce kariéry** z mládežnických zápasů (Ronaldo, Özil a Ibrahimović předčili prognózu, Bojan Krkić ne).

## Úskalí

- **Malý vzorek = past:** Dallas Mavericks podepsali Evana Eschmeyera kvůli skvělému plus-minus a zaplatili zbytečně mnoho – vzorek byl příliš malý.
- Ve fotbale je málo gólů a střídání, 22 hráčů → šum je větší než v basketbalu.
- Štěstí týmu se přelévá do ratingu hráče (Bale v Tottenhamu).
- Žebříček superhvězd vypadá „divně“ (Götze 1., Messi 4., Ronaldo 38. v zimě 2016) – podle Seidela stačí, že jsou v top 50 ze statisíců.
- **Nikdy nekupovat podle jednoho čísla** – výkon vždy posoudit v kontextu týmu a očima.

## Obchodní model (zajímavost)

Malé kluby platí symbolickou licenci + **podíl z budoucího prodeje** hráče doporučeného modelem; větší kluby paušál. Typické dotazy: objektivní posouzení hráče nabídnutého agentem; vyhledávání („nejlepší stopeři do 2 mil. € s končící smlouvou“).

## Využití (návrh)

Pro Sigmu jako **levný doplňkový filtr** pro nižší a exotické ligy a pro **odhad potenciálu mládeže** – vždy v kombinaci s [[Skauting – proces a reporting]]. Princip plus-minus lze počítat i interně z vlastních zápasů (sestavy + góly) pro akademii; vzorky ale budou malé → [[Football Hackers – návrhy pro Sigmu]].

## Souvislosti

[[Datový skauting – metriky a úskalí]] · [[Predikce a pravděpodobnostní modely]] (Elo) · [[Biologický věk]] (relative age effect) · [[Výkon vs. výsledek a role náhody]]
