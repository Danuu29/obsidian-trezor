---
typ: koncept
tags: [data, architektura, standardy, analytics, barca]
zdroje: ["[[Zdroj – Barça Match Analysis]]"]
aktualizovano: 2026-10-15
---
# Typy sportovních dat a datová architektura

Úvod do metrických dat ve sportu (P4 M2 [[Zdroj – Barça Match Analysis]]; Alamar 2013, Davenport 2014, O'Donoghue 2014, Jayal et al. 2018). **Analytics** = analýza explicitně navázaná na rozhodování, ne jen popis.

## 5 typů sportovních dat a standardy

| Typ | Obsah | Standard | U nás (návrh mapování) |
|---|---|---|---|
| **Eventing** | akce s míčem: action + timestamp + status | F24 (Opta) | [[Wyscout]], vlastní tagging, [[Aplikace – Match tracker]] |
| **Tracking** | souřadnice X,Y hráčů a míče (1–50 Hz) | EPTS (FIFA) | [[SkillCorner]], GPS |
| **Biological** („vitals“) | fyziologie, složení těla, zranění | OSICS (zranění) | [[VALD]], [[InBody]], [[Whoop]], zdravotní modul |
| **Financial** | platy, přestupy | Financial Fair Play | mimo scope |
| **Video** | video jako data indexovaná metadaty | PAL, DCI 4k, H.264 | Wyscout, [[Eyeball]], vlastní kamera |

Video jako data je v Evropě málo využité – propojit klipy s filtry databáze je potenciální výhoda. Davenport: klíčový faktor úspěchu je **rychlý přístup k videu**.

## Architektura

**Data lake** (vše surové na jednom místě, server nebo cloud; cíl: **žádná data sila**) → **data warehouse** (ETL, data marts, **governance** – definice a klasifikace dat) → **Business Intelligence** (filtrování a vizualizace bez programování; Power BI, Tableau, QlikView).
Praktické nástroje z případovky: Python (tracking), R a SQL (eventing), Excel přestane stačit → SQL databáze.

## Výběr proměnných

- Proměnné obvykle určuje data provider – široce, ale **bez struktury vlastního herního modelu**. Výchozí bod má být model fází hry ([[Herní cyklus]]). „Vědět, jak pozorovat, je vědět, co vybrat“ (Whitehead).
- Kvantitativně (dopad na výsledek) vs. kvalitativně (klíčové vazby v řetězci akcí).
- **Matice relevance × frekvence** – dashboard má akcentovat relevantní, i když řídké situace:

| | málo časté | časté |
|---|---|---|
| **relevantní** | střely na branku | přihrávky v poslední třetině |
| **irelevantní** | rozhodčí míč | přihrávky stoperů bez tlaku |

- **Customizace** přes **kombinované indexy ze standardních metrik**, ne stavět metriky od nuly.
- Pyramida využití: výběr kategorií → design registru (live vs. postgame) → analýza → souhrn → závěry (spíš deskriptivní) → využití štábem.

## Jak přemýšlet o datech

- **Smart Data > Big Data** (3–4 V jsou nadužívaný marketing).
- Trenéři jsou **heuristicko-induktivní** (od představ k datům), analytici **algoritmicko-deduktivní** (od dat k závěrům) → počítat s tím v komunikaci → [[Principy vizualizace a reportingu]].
- U predikčních / hodnoticích nástrojů komunikovat **chybu** a sledovat **false positives** (hodnoceni dobře, nezlepšili se) a **false negatives** (vyřazení, kteří se prosadili); hlídat velikost vzorku.
- Mládežnická soutěž je jiný typ soutěže než vrcholová – data se v ní mají používat jinak (Hohmann et al. 2005).

## Souvislosti

[[Mapa datových zdrojů]] · [[Normalizace herních dat]] · [[Oddělení analýzy – struktura a role]] · [[Yarmill]] · [[Thresholdy a benchmarky]]
