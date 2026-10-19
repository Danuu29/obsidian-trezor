---
typ: treninkovy-denik
aktualizovano: 2026-10-19
tags: [cyklistika]
---
# Tréninkový deník

> [!info] Kopie tréninkového deníku z Claude Docs – needitovat, při synchronizaci se přepíše. Zdroj: [Cyklistika – tréninkový deník (Danů)](https://claude.ai/code/artifact/3c977ff5-90bc-4fae-b04a-4a5908ddf6fb)

## Zóny a pravidla

Intenzitu řídíme výhradně podle tepových zón a wattů z testu 21. 9. 2026. Do wattmetru (cca konec října) jen podle tepu a RPE, pak na trenažéru podle wattů.

| Zóna | TF (tep/min) | Výkon (W) | Charakter |
|---|---|---|---|
| Z1 | pod 130 | pod 155 | regenerace |
| Z2 | 130–155 | 160–205 (dlouhé jízdy hlavně 155–195) | aerobní vytrvalost |
| Z3 | 156–172 | 206–230 | tempo |
| Z4 | 173–180 | 231–250 | prahová intenzita |
| Z5 | nad 180 | nad 250 | VO₂max a vysoká intenzita |

Orientační prahy: aerobní práh cca 205 W / 155 tep/min, anaerobní práh cca 240 W / 178 tep/min.

### Jak spolupracujeme

1. Každou neděli: Danů pošle pracovní a rodinný plán na týden, Claude postaví týdenní plán podle dlouhodobého plánu a zapíše ho do archivu.
2. Po každém tréninku: Danů pošle co udělal (typ, délka, TF průměr/max, případně watty, vzdálenost, převýšení), RPE 1–10 a jak se cítil. Claude to zapíše do deníku.
3. Zatížení = RPE × minuty (session RPE). Z toho sledujeme týdenní zatížení a poměr akutní/chronické zátěže.
4. Připravenost hodnotíme podle zatížení, RPE, spánku, klidového tepu ráno a pocitu v nohách (1–5).
5. Po příchodu wattmetru uděláme na trenažéru vlastní test a zóny ve W případně upravíme podle reálných dat.

### Kvalitní jednotky podle zprávy

| Typ | Obsah | Intenzita |
|---|---|---|
| Aerobní vytrvalost | 90–180 min, 2–4× týdně | Z2 |
| Tempo | 2× 20 nebo 3× 15 min, 5 min lehce; 1× za 7–10 dní | Z3, 210–225 W |
| Práh | 2× 12–15 nebo 3× 8–10 min, 5–8 min lehce | Z4, 230–245 W |
| VO₂max | 4–6× 3–4 min, stejně dlouhé vyjetí | 260–290 W, TF na konci 180–190 |

Maximálně 2 kvalitní jednotky týdně (práh a VO₂max střídat). Každý 3.–4. týden objem −25–30 %.

## Výsledky testů a závodů

Výchozí test: CPET 21. 9. 2026 (Klinika sportovní medicíny, Mgr. Marek Maráček) – laktátové schody + rampa do maxima na cyklistickém ergometru. Hmotnost 69 kg, výška 178 cm.

### Maxima

| Parametr | Hodnota |
|---|---|
| VO₂max | 58,6 ml/kg/min (cca 4,04 l/min) |
| Max. výkon v rampě | 450 W (6,52 W/kg) – krátkodobá špička, ne FTP |
| Max. TF | 190 tep/min |
| RER max | 1,29 |
| Max. laktát | 8,2 mmol/l (po 5 min 7,8) |
| Max. ventilace | 139,6 l/min |
| Klidová TF | 76 tep/min |

### Laktátové schody

| Výkon | TF | Laktát | RER |
|---|---|---|---|
| 140 W | 108 | 0,9 mmol/l | 0,89 |
| 180 W | 135 | 1,2 mmol/l | 0,91 |
| 210 W | 157 | 2,1 mmol/l | 0,95 |
| 240 W | 178 | 4,0 mmol/l | 0,99 |

Poznámky z dat: tep během stupňů výrazně driftoval (na 210 W ze 138 na 165), proto na delších úsecích kontrolovat i RPE. Na dlouhých jízdách počítat s vysokou spotřebou sacharidů (60–90 g/h).

### Plán dalších testů

| Kdy | Test | Účel |
|---|---|---|
| 1. týden s wattmetrem | Trenažér: 20 min rozjetí, 5 min naplno, 10 min lehce, 20 min naplno | Ověřit W zóny na vlastním trenažéru (20 min × 0,95 ≈ FTP) |
| Každé 4–6 týdnů | Kontrolní 20 min test na trenažéru | Sledovat posun prahu |
| Za 10–12 týdnů | Opakovaný CPET na klinice (stejné podmínky) | Porovnání s 21. 9. 2026 |

### Závody 2026

Obě akce ukazují velkou výdrž na vysokém tepu; limitem byla opakované nástupy nad prahem ve skupině. Watty ze Stravy jsou odhad bez wattmetru (u Road stage navíc nezohledňuje háček), proto je nehodnotíme.

| Datum | Závod | Vzdálenost / převýšení | Čas / rychlost | TF prům./max | Poznámka |
|---|---|---|---|---|---|
| 12. 9. | Road stage 133, Hradec Králové | 134,56 km / 722 m | 3:32:49 / 38,2 km/h | 170 / 189 | Nejdelší jízda. 55 km v pelotonu (odpadnutí), 30 km sám, pak se skupinkou. Cca 49 % času nad 173 tep/min, 44 % 156–172. Kadence prům. 92 |
| 6. 6. | Můj první závod, Deštné v Orlických horách | 78,08 km / 1 301 m | 2:39:40 / 29,3 km/h | 163 / 183 | Od cca 15. km trvale 160–180 tep/min |

Co z toho plyne pro přípravu:

- Průměr 163 tep/min po 2:40 h a zhruba 1:45 h nad 173 tep/min na Road stage = výborná výdrž v Z3–Z4.
- Odpadnutí z pelotonu po 55 km: chybí rezerva nad prahem a schopnost opakovaně zvládat nástupy. Cíl: vyšší anaerobní práh (víc wattů na stejné tepy) a intervaly typu over-under a 30/15.
- Energie: cca 3 700 kcal na Road stage – jídlo 60–90 g sacharidů/h od začátku je součást výkonu, trénovat i na dlouhých jízdách.
- Road stage: průměr 170 tep/min po 3:33 h (max 189), jen cca 8 tepů pod anaerobním prahem z testu. Po takové akci počítat se 2–3 dny lehké zátěže.

## Dlouhodobý plán

Cíl: být na jaře 2027 připravený na závod (konkrétní zatím není; počítáme s prvním startem od konce dubna). Do jara posunout anaerobní práh nad 240 W a aerobní práh nad 205 W, udržet VO₂max a zlepšit zvládání nástupů ve skupině. Rámec týdne: 3× kolo (2× 60–90 min, 1× 3–4 h), 1× posilovna, 1–2× domácí posilování (expandér, jednoručka 10 kg).

| Fáze | Termín | Řízení | Hlavní náplň |
|---|---|---|---|
| 1 – Základ venku | 28. 9. – 25. 10. | TF + RPE | Z2 objem, tempo, první práh; týden 4 odlehčení |
| 2 – Základ na trenažéru | 26. 10. – 22. 11. | W (po testu) | Test v 1. týdnu; tempo → práh 2× 12–15 min; dlouhá Z2 |
| 3 – Rozvoj | 23. 11. – 13. 12. | W | Práh 2× 15 až 3× 10 min, VO₂max 4–6× 3–4 min, střídat |
| Test | 14. – 20. 12. | – | Kontrolní CPET, lehčí týden |
| Svátky | 21. 12. – 3. 1. | TF/W | Udržovací objem, volnější režim |

Pokračování do jara:

| Fáze | Termín | Řízení | Hlavní náplň |
|---|---|---|---|
| 4 – Rozvoj II | 4. 1. – 14. 2. | W | Práh 2× 20 min, sweet spot, over-under |
| 5 – Specifická příprava | 15. 2. – 4. 4. | W + venku TF | VO₂max, 30/15, over-under, delší jízdy venku, skupinové jízdy |
| Test | kolem 22.–28. 3. | – | Kontrolní test na trenažéru (20 min) |
| 6 – Ladění a závody | od 5. 4. | W + TF | Méně objemu, udržet intenzitu, první závod |

### Týdenní kostra

| Jednotka | Náplň |
|---|---|
| Kolo A (60–90 min) | Kvalitní: tempo, práh nebo VO₂max podle fáze |
| Kolo B (60–90 min) | Z2, případně kadence nebo kratší tempo |
| Kolo C (3–4 h) | Dlouhá Z2, občas tempo blok uprostřed |
| Posilovna | Celé tělo s důrazem na nohy a zadní řetězec (dřep, rumunský mrtvý tah, bulharský dřep, hip thrust) + přítahy, tlaky, Pallof |
| Doma | 20–25 min: jednonožné cviky pomalým tempem, core, expandér |

Posilovna nikdy den před kvalitní jízdou nebo dlouhou jízdou.

Až bude jasný jarní závod, doladíme fáze 5 a 6 na jeho termín.

### Fáze 1 – Základ venku: rozpis po týdnech (28. 9. – 25. 10.)

Cíl fáze: zvednout objem v Z2 a naučit tělo tempo, na konci první práh. Dlouhá jízda roste o 15 min týdně, jídlo na dlouhé jízdě o 5 g/h (trénink trávení). Řízení TF + RPE; na konci fáze přichází wattmetr a fáze 2 začíná testem na trenažéru.

| Týden | Kolo A – kvalita | Kolo B – Z2 | Kolo C – dlouhá | Síla | Cíl zatížení |
|---|---|---|---|---|---|
| 1: 28. 9. – 4. 10. | Tempo 2× 15 min Z3 (TF 158–168) | 75–90 min Z2 + 4× 3 min kadence 100–110 | 3:00 Z2, 60 g sacharidů/h | Jen doma (pobyt) | cca 1 800 |
| 2: 5.–11. 10. | Tempo 2× 20 min Z3 (TF 158–170) | 90 min Z2 + kadence | 3:15 Z2, 65 g/h | Posilovna A + 1× doma | cca 2 100 |
| 3: 12.–18. 10. | První práh 3× 8 min Z4 (TF 173–180, RPE 7–8), 5 min lehce | 90 min Z2 | 3:30 Z2, ve 2. hodině 1× 20 min Z3; 70 g/h | Posilovna B + 1× doma | cca 2 300 |
| 4: 19.–25. 10. (odlehčení) | Tempo 2× 10 min Z3 | 60 min Z2 | 2:15–2:30 Z2 | Posilovna A lehčí (2 série) | cca 1 500 |

Pravidla fáze: obsah jednotek je daný rozpisem, týdenní plán jen rozmístí jednotky do dnů podle kalendáře. Pořadí priorit, když není čas: C → A → B → síla. Vynechaná jednotka se nedohání zdvojením, další týden jede podle rozpisu. Kvalita A nikdy den po posilovně s nohama ani den před C. Pata: týden 1–2 izometrie lýtek, od týdne 3 excentrické výpony, pokud bolest na schodech max 2/10; jinak zůstat u izometrií. Na konci týdne 4 vyhodnotit fázi (zatížení, drift na dlouhých jízdách, RPE tempa) a doladit fázi 2.

## Posilovna

Posilovna má dvě role: sílu nohou a trupu pro kolo a vyrovnání jednostranné zátěže ze sedu na kole (zkrácené kyčle, kulatá záda, slabší horní polovina a boky). Každý trénink proto obsahuje obojí.

### Periodizace

| Období | Cíl | Hlavní cviky | Série × opakování | Úsilí |
|---|---|---|---|---|
| 28. 9. – 8. 11. | Adaptace, technika, stabilita | vše | 3 × 8–12 | RPE 6–7, 3–4 opakování v rezervě |
| 9. 11. – 14. 2. | Maximální síla | dřep / mrtvý tah | 4 × 4–6 | RPE 8, 2 opakování v rezervě |
| 15. 2. – 4. 4. | Síla + výbušnost | hlavní cvik + výskoky | 3 × 3–5 + 3 × 5 výskoků | RPE 8, menší objem |
| od 5. 4. | Udržovací | hlavní cvik | 2 × 3–5 | RPE 7–8 |

Nikdy do selhání. Posilovna ne den před kvalitní nebo dlouhou jízdou; ideálně den po intervalech.

### Trénink v posilovně (60–70 min, střídat A a B po týdnu)

| Blok | Varianta A | Varianta B | Proč |
|---|---|---|---|
| Rozcvička 10 min | Veslo nebo kolo 5 min, pak 90/90 kyčle, world's greatest stretch, rotace hrudní páteře, glute bridge | stejně | Mobilita kyčlí a hrudníku |
| Hlavní cvik | Dřep s velkou činkou | Mrtvý tah s trap barem | Síla nohou a zadního řetězce |
| Jednonožný cvik | Bulharský dřep | Výstupy na bednu s jednoručkami | Vyrovnání stran, stabilita kolene |
| Zadní řetězec | Rumunský mrtvý tah | Hip thrust | Hýždě a hamstringy |
| Tah | Přítahy v předklonu nebo shyby | Stahování kladky nebo přítah na kladce vsedě | Protiváha shrbené pozici |
| Tlak | Tlak jednoručkami nad hlavu | Kliky nebo tlak na šikmé lavici | Horní polovina těla, ramena |
| Trup | Pallof press + dead bug | Boční plank / Copenhagen plank + farmer's walk | Stabilita trupu a boků |
| Doplněk | Nordic curl (hamstringy) | Výpony na lýtka + face pull | Prevence zranění |

Objem v první fázi: hlavní cvik 3 × 8, ostatní 3 × 10–12 (na stranu), trup 3 × 30–40 s nebo 10–12 opakování.

### Doma (20–25 min, 1–2× týdně)

Vybavení doma (od 14. 10. 2026): jednoručka 10 kg, kettlebell 6 kg, expandér a nová sada odporových gum s karabinami (různé síly, např. 30 lb ≈ 12 kg; kombinovat), kotvou do dveří, úchyty a manžetami na kotníky. Gumy používat běžně ve všech domácích jednotkách i jako náhradu posilovny (přítahy, stahování, tlaky, face pull, Pallof, woodchop, cviky s manžetou na kotník). Kotvu zavírat do dveří na straně, kam se otvírají od cvičícího.

| Cvik | Dávka | Video |
|---|---|---|
| Goblet dřep s 10 kg, 3 s dolů | 3 × 12 | [goblet dřep v tempu](https://www.youtube.com/watch?v=4G6P4RzNyOg) |
| Rumunský mrtvý tah na jedné noze s jednoručkou | 3 × 10 na nohu | [RDL na jedné noze](https://www.youtube.com/watch?v=k83AIfjDbnI) |
| Glute bridge na jedné noze | 3 × 12 na stranu | [glute bridge na jedné noze](https://www.youtube.com/watch?v=Zb3ILLdI6fk) |
| Přítahy s expandérem + face pull | 3 × 12 + 3 × 15 | [přítahy s expandérem](https://www.youtube.com/watch?v=LSkyinhmA8k) · [face pull s expandérem](https://www.youtube.com/watch?v=PYj77in44ms) |
| Kliky | 3 × 10–15 | [technika kliku](https://www.youtube.com/watch?v=mECzqUIDWfU) |
| Dead bug, boční plank | 3 × 10 na stranu, 3 × 30 s | [dead bug](https://www.youtube.com/watch?v=-gRN_JyVTLY) · [boční plank](https://www.youtube.com/watch?v=oEs8ZvVDOzI) |
| Mobilita: flexory kyčle, hrudní páteř, lýtka | 5 min | [flexory kyčle](https://www.youtube.com/watch?v=Bfb-9dIWEr4) · [hrudní páteř (open book)](https://www.youtube.com/watch?v=5TdmVlQe64c) · [lýtka](https://www.youtube.com/watch?v=JSzCfi0wbcA) |

Všestrannost navíc (volitelně, místo domácí jednotky): 30–45 min chůze do kopce, plavání nebo aktivní hra venku – cokoli mimo kolo, co zapojí tělo jinak.

## Zatížení a připravenost

Týdenní souhrn z deníku; od 4. týdne dat sledujeme poměr akutní (7 dní) a chronické (průměr 4 týdnů) zátěže.

| Týden | Kolo (jízdy / h) | Posilovna / doma | Zatížení | Poměr A/C | Připravenost | Poznámka |
|---|---|---|---|---|---|---|
| 19.–25. 10. | plán 0–1 trenažér / max 0,4 h | plán 0 / 2 (vršek vsedě) | plán cca 250–350 | – | – | Fáze 1, týden 4 – místo odlehčení pauza na kole do MR 22. 10.; zbytek týdne podle výsledku |
| 12.–18. 10. | 3 trenažér / cca 1,1 h + Út (bez dat) | 0 / 2 (vršek vsedě) | cca 600–700 (plán 2 300) | cca 0,4 | snížená (zranění) | Upraveno kvůli zranění pravé nohy; kolo od 17. 10. pozastaveno do MR |
| 5.–11. 10. | plán 2–3 / cca 5–6,5 h | plán 1 / 0–1 (+ lezení) | plán cca 2 100 | – | – | Fáze 1, týden 2; Po lezení místo kola, Pá nic, B podle času |
| 28. 9. – 4. 10. | plán 3 / cca 5,5 h | plán 0 / 1–2 | plán cca 1 800 | – | – | Fáze 1, týden 1; Po–St rodinný pobyt |
| 21.–27. 9. | 3 / 5,9 h (+ test) | 1 / 0 | 1 932 | – | – | Testovací týden; víkend jen Z2 |

### Pravidla připravenosti

| Signál | Co udělat |
|---|---|
| Poměr A/C 0,8–1,3 | Plán beze změny |
| Poměr A/C nad 1,3 | Snížit intenzitu nebo objem v dalším týdnu |
| Klidový tep ráno o 5+ výš než obvykle | Kvalitní jednotku vyměnit za Z2 nebo volno |
| Nohy 1–2 z 5 nebo špatný spánek 2 noci po sobě | Den volna nebo Z1 |
| RPE o 2 body vyšší, než odpovídá tréninku | Zkrátit a přidat den lehčí zátěže |

Pro přesnější hodnocení je užitečné posílat i ranní klidový tep a spánek (hodiny, kvalita 1–5).

### Sledované zdravotní problémy

| Od | Problém | Co ho spouští | Postup |
|---|---|---|---|
| cca začátek září (k 1. 10. 4. týden) | Levá pata / Achilova šlacha | Vysoká intenzita pohybu (schody, běh); kolo a chůze nevadí | Řízení zátěže: nic neběhat ani neskákat. Posilování postupně: izometrie lýtek (výdrž ve výponu 5× 30–45 s, bolest max 3/10) → excentrické výpony. Úlevu od bolesti (mast apod.) nebrat jako důvod zvednout zátěž. Každý týden zapsat stav (bolest 0–10 při schodech, ráno po probuzení). Stav: 28. 9. – 0/10, na kole vůbec necítí (večer izometrie). 29. 9. – po procházce do kopce a z kopce (166 m) pata bolela, nohy unavené celý den. 1. 10. – po jízdě B (106 min) pata cítit víc než dřív, na stejné (levé) noze pobolívá i koleno a trochu celá noha; nelimituje. Trvá 4. týden bez zlepšení → objednat se ke sportovnímu fyzioterapeutovi (vyšetřit patu i koleno, případně nastavení kola). |

## Tréninkový deník

Každá aktivita jeden řádek, nejnovější nahoře. Zatížení = RPE × minuty. Délka posilovny 22. 9. je odhad.

Jednotlivé tréninky jsou v poznámkách týdnů (sekce Týdny níže).

## Poučení

| Datum | Poznatek |
|---|---|
| 24. 9. | Test, posilovna a intenzivní jízda tři dny po sobě jsou moc nahuštěné; kvalitní jednotky rozložit. |
| 24. 9. | Kratší jízdy nemají být pokaždé „švih“ – jedna kvalitní, druhá v Z2. |
| 24. 9. | Den po maximálním testu je horní polovina těla + core správná volba; v běžných týdnech má posilovna obsahovat i nohy a zadní řetězec. |
| 26. 9. | Dlouhá Z2 držet v plánované délce. Když ke konci tep driftuje a nohy těžknou, zvolnit a nepřetlačovat – RPE dlouhé jízdy má zůstat do 5. Drift sledovat i ve vztahu k jídlu a pití. |
| 19. 10. | Při zranění kosti nebo podezření na nerv rozhoduje reakce nohy večer a druhý den, ne pocit během jízdy na trenažéru. Krátká jízda navíc přidá málo, zhoršení může stát týdny. |

## Týdny
Každou neděli přibude nový týden nahoru; po jeho skončení doplníme, co se splnilo a co z toho plyne.

- [[2026-10-19 – Tréninkový týden (fáze 1, týden 4)]] – fáze 1 – Základ venku, týden 4 – odlehčení, upraveno kvůli zranění; zatížení plán cca 250–350 / skutečnost –
- [[2026-10-12 – Tréninkový týden (fáze 1, týden 3)]] – fáze 1, týden 3 – upraveno kvůli zranění; zatížení plán 2 300 / skutečnost cca 600–700
- [[2026-10-05 – Tréninkový týden (fáze 1, týden 2)]] – fáze 1 – Základ venku, týden 2; zatížení plán cca 2 100 / skutečnost –
- [[2026-09-28 – Tréninkový týden (fáze 1, týden 1)]] – fáze 1 – Základ venku, týden 1; zatížení plán cca 1 800 / skutečnost –
- [[2026-09-21 – Tréninkový týden (testovací týden)]] – testovací týden; zatížení plán – / skutečnost 1 932
