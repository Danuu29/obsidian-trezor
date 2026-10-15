---
typ: synteza
tags: [data, zdroje, prehled]
aktualizovano: 2026-10-15
---
# Mapa datových zdrojů

Které datové zdroje Sigma (resp. Yarmill) používá nebo zvažuje a k čemu. *Syntéza ze všech zdrojů wiki.*

| Oblast | Zdroj | Stav | Kde se používá |
|---|---|---|---|
| Zatížení | GPS (Catapult) | používá se | [[GPS metriky a zatížení]] |
| Síla, skoky | [[VALD]] (+ Meloq) | používá se, Meloq chybí v reportu | [[Silové testy a normy]] |
| Složení těla | [[InBody]] | používá se | [[Silové testy a normy]] |
| Vytrvalost | schodový laktátový test (tabular) | používá se | [[Silové testy a normy]] |
| Reakce | reakční test (tabular) | používá se | [[Silové testy a normy]] |
| Připravenost | [[Whoop]], wellness dotazníky | používá se (TOP program) | [[Denní připravenost a wellness]] |
| Zdraví | zdravotní modul Yarmill, fyzio, lékař | částečně | [[Vstupní diagnostika hráče]] |
| Herní data (tracking) | [[SkillCorner]] | používá se (A-tým, skauting) | [[Aplikace – Analýza soupeře]] |
| Herní data (event) | [[Wyscout]] | používá se | [[Hodnocení utkání a pozápasový report]] |
| Herní data (event) | [[StatsBomb]] | zvažuje se | [[Analytické balíčky Yarmill]] |
| Herní data (event) | [[Opta]] (Stats Perform) | nepoužívá se – referenční provider literatury | [[Expected goals (xG)]] |
| Pravděpodobnost výsledku | kurzy sázkových kanceláří (normalizované) | nápad | [[Predikce a pravděpodobnostní modely]] |
| Herní data mládež | [[Eyeball]], iBall | zjišťuje se | [[Karta hráče – koncept]] |
| Hodnocení | trenéři + sebehodnocení (Yarmill) | přípravky hotovo, akademie se tvoří | [[Hodnocení hráčů – metodika]] |
| Vlastní záznam | [[Aplikace – Match tracker]] | používá se | – |
| Biologický věk | měření Slavia/Baník | plán | [[Biologický věk]] |
| Ostatní | GymAware, krevní rozbory, 3D sken pohybu | nápad / řeší se | [[Future Blue]] |

## Typologie dat

Podle Barça kurzu 5 typů: eventing, tracking, biological, financial, video – se standardy F24, EPTS, OSICS… → [[Typy sportovních dat a datová architektura]]. Cíl architektury: žádná data sila, sjednocená ID napříč zdroji.

## Odvozené metriky (Soccermatics)

Z event a tracking dat lze počítat xG, possession value (xThreat ve SkillCorneru), pasové sítě a centralizaci, defenzivní hulls, metriky presinku a týmové synchronizace → [[Expected goals (xG)]], [[Possession value a Markovovy řetězce]], [[Pasové sítě a prostorové mapy]], [[Pressing a kolektivní pohyb]].

## Mezery

Brankáři · herní data pro mládež · biologický věk · mentální dotazníky · **vlastní video tagging** podle herního modelu (zatím jen Match tracker) → [[Tagging a code window]].
