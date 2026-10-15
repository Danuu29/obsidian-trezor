---
typ: entita
tags: [datovy-zdroj, herni-data, tracking]
zdroje: ["[[Zdroj – Znalosti]]", "[[Zdroj – Zadání aplikací]]", "[[Zdroj – Yarmill poznámky]]", "[[Zdroj – Soccermatics]]"]
aktualizovano: 2026-10-15
---
# SkillCorner

Poskytovatel tracking dat z videa (pomocí AI): běžecká/fyzická data podobná GPS + metriky hry bez míče („Game Intelligence“). Přístup přes Python SDK/API; Sigma má přístup k ~14 soutěžím (CZE 1. liga, FNL, AUT, BEL, DEN, POL, SVK, SWE… + UEFA předkola).

## Pohledy na data

- **Průměr na hráče za zápas** – příprava na soupeře
- **30 min TIP** (time in possession) – skauting; odstraní vliv dominance týmu na míči
- **100 situací** – typické chování hráče bez ohledu na tým
→ detailně [[Normalizace herních dat]]

## Datové sady

Physical · Passes · PassingOptions · OffBallRuns · OnBallEngagements · PlayerPossessions · Phases of Play · Dynamic Events (surové události se souřadnicemi). Klíčové metriky: PSV-99 (max. rychlost), HI/HSR/sprint, xThreat, xPass, dangerous/difficult passes, typologie náběhů (in behind, cross receiver, overlap…).

## Využití

[[Aplikace – Analýza soupeře]] · [[Skauting – proces a reporting]] (postové thresholdy) · [[Future Blue]] (profil hráče)

## Kontext ze Soccermatics

Metriky SkillCorneru odpovídají tomu, co Sumpter v roce 2016 popisuje jako budoucnost tracking analýzy: **PassingOptions** ≈ sítě dostupných přihrávek (Prozone), **xThreat** ≈ possession value modely, **OnBallEngagements** ≈ analýza presinku → [[Pressing a kolektivní pohyb]], [[Possession value a Markovovy řetězce]] ([[Zdroj – Soccermatics]]).

## Otevřené otázky

- Umí SkillCorner analyzovat U17/U19 tak, aby data neviděli soupeři? (zmíněno „pro dorost Adam“)
