---
typ: koncept
tags: [stridani, cervena-karta, koucink, zapas, unava, rozhodovani]
zdroje: ["[[Zdroj – The Numbers Game]]"]
aktualizovano: 2026-10-15
---
# Střídání a vyloučení

Co data říkají o načasování střídání a o ceně červené karty. Obojí je způsob, jak zacházet s nejslabším článkem na hřišti ([[Teorie slabého článku (O-ring)]]). Ze [[Zdroj – The Numbers Game]] (Kap. 9).

## Cena červené karty

- Vyloučení je vzácné: v Itálii a Španělsku ~1× za 5–6 zápasů týmu, v Anglii a Německu ~1× za 12–13.
- Vyloučení hráči mají za sezónu horší statistiky (přesnost střel, méně klíčových přihrávek, víc než dvojnásobek faulů) – často jde o slabý článek.
- Jedna červená sníží očekávané body ze ~1,5 na ~1 (Bundesliga 2005–10: 1,42 → 0,75).
- Regrese (top 4 ligy, 5 sezón, po zohlednění domácího prostředí, střel, gólů a faulů): pravděpodobnost prohry **24 % → 38 %**, výhry **36 % → 22 %**; po druhé červené je prohra nejpravděpodobnější výsledek.
- **Červená karta ≈ −0,42 bodu**, hrát venku místo doma ≈ −0,43 bodu. Vyloučení je jako darovat soupeři domácí prostředí.
- Výjimka: „taktická“ červená může být racionální (Suárez – ruka na brankové čáře proti Ghaně 2010: jistý gól → penalta).

## Načasování střídání

**Jak se střídá (Myers; PL, La Liga, Serie A):** málo střídání v 1. poločase; první střídání o přestávce nebo v 56.–65. min, druhé 66.–80., třetí v posledních 10 min. 40 % střídání je záložník za záložníka, obránci se střídají nejméně.

**Pravidlo <58<73<79** (Bret Myers, data mining, ověřeno na Bundeslize, MS a MLS): pokud tým **prohrává**, první střídání do 58. min, druhé do 73., třetí do 79. Pokud neprohrává, na načasování nezáleží.

| Soutěž | Snížení / vyrovnání při dodržení pravidla | Bez pravidla |
|---|---|---|
| PL | 40 % | 22 % |
| Serie A (něco ze zápasu) | 52 % | 18 % |

- Pravidlo dodržovalo 44 % týmů na MS, ale méně než čtvrtina prohrávajících týmů PL; nejkonzervativnější byli trenéři PL a Bundesligy (Klopp, Benítez).
- Příklady: Tenerife (Oltra) pravidlo nedodrželo nikdy – dvakrát otočilo, sestup. Portsmouth (Grant) 2009/10 ho mohl použít ve 21 zápasech, použil 4× (2× snížil), v 17 ostatních se skóre 14× nezlepšilo.

## Proč trenéři střídají pozdě

- **Ukotvení (anchoring):** trenér „věří“ původnímu výběru a čeká, až je pokles výkonu nepopiratelný – to už bývá pozdě. Hráči navíc přesvědčují, že ještě mají sílu.
- **Únava není vidět:** Carling (Lille) nenašel u střídaných hráčů rozdíl ve fyzických datech mezi poločasy – hráči **šetří síly** (pacing) a pracují pod maximem. Únava se ukáže až ve chvíli, kdy je potřeba jít z 90 % na 95 % (skluz, výskok).
- **Střídající záložníci** naběhají víc celkem i ve vysoké intenzitě a rychleji se zotavují než záložníci, kteří zůstali na hřišti.
→ Střídat dřív, než to „oči a mozek“ trenéra řeknou; pomáhá předem daná pravidla.

> [!note] Aktualita (poznámka LLM – ověřit)
> Pravidlo vzniklo pro **3 střídání**. Od 2020 se smí střídat pětkrát (ve třech oknech), takže konkrétní minuty neplatí; obecný závěr (při prohře střídat dřív) je vhodné ověřit na novějších datech.

## Pro praxi (návrh LLM)

- Vyhodnotit střídání Sigmy (A-tým, U19) za poslední sezóny: minuta, stav, změna skóre a xG po střídání → podklad pro trenéry → [[Live analýza a poločas]].
- Do live analýzy přidat upozornění „prohráváme, čas na střídání“ a fyzická data střídajících vs. hráčů na hřišti ([[GPS metriky a zatížení]]).
- Disciplína jako KPI: vyloučení a zbytečné žluté stojí body srovnatelně s hraním venku.

## Souvislosti

[[Teorie slabého článku (O-ring)]] · [[Live analýza a poločas]] · [[Kognitivní zkreslení v hodnocení]] · [[Vliv trenéra a jeho výměna]]
