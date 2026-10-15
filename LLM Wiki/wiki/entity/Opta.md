---
typ: entita
tags: [datovy-zdroj, herni-data, event-data, provider]
zdroje: ["[[Zdroj – Soccermatics]]", "[[Zdroj – Football Hackers]]", "[[Zdroj – The Numbers Game]]"]
aktualizovano: 2026-10-15
---
# Opta

Britský poskytovatel **event dat** (kdo komu přihrál, kde, kdy; střely, skluzy, bloky). Jeho formát F24 je standard eventingu ([[Typy sportovních dat a datová architektura]]). V [[Zdroj – Soccermatics]] hlavní zdroj dat většiny analýz (přes aplikaci FourFourTwo StatsZone); OptaPro Forum = konference analytiků.

## Zmínky v knize

- Leicester City 2015/16 – analytici A-týmu používali Opta data pro pozápasové briefingy manažera.
- Sam Green (Opta) jako jeden z prvních budoval [[Expected goals (xG)]] pro kluby PL, později Head of Research v Aston Ville.
- **Prozone** (tracking a pressing analýzy, databáze Football Manageru pro kluby; Paul Power) – samostatná firma, viz [[Pressing a kolektivní pohyb]].

> [!note] Aktualita (poznámka LLM – ověřit)
> Prozone se 2015 spojil se STATS a ten 2019 s Optou (Perform Group) → dnes **Stats Perform**. StatsZone už v původní podobě neexistuje.

## Vztah k Sigmě

Sigma Optu nepoužívá; event data má z [[Wyscout]], zvažuje [[StatsBomb]] → [[Mapa datových zdrojů]].

## Zmínky ve Football Hackers

- **OptaPro** – oddělení pro kluby: Sam Green tu 2012 popsal xG; dále Keeping Goals Prevented (brankáři), „Chances created“, **sekvence** a **Direct Speed** (2017), xG s *Shot Clarity* a *Shot Pressure*; Scout7 (skautská platforma) převzat 2018; spolupráce s TruMedia (data + video) → [[Expected goals (xG)]], [[Possession value a Markovovy řetězce]].
- **Prozone** (1995, Derby County, Ram Mylvaganam) – první tracking (tepelné kamery); první platící klient Manchester United 1999; Bolton (Allardyce) postavil styl na datech. Prozone → STATS.
- Brazílie–Mexiko (MS 2018): tři provideři, tři různé naběhané vzdálenosti → kvalita a definice dat.

Zdroj: [[Zdroj – Football Hackers]] (Kap. 2, 5, 6).

## Zmínky v The Numbers Game

- Opta založili v 90. letech manažerští konzultanti jako **index výkonu hráčů** (1996 v Sky Sports a Observeru, financoval Carling, odborník Don Howe). Brzy zjistili, že data mají větší hodnotu než publicita – nejdřív pro média, pak pro kluby.
- Zpočátku trvalo zakódování zápasu ~4 hodiny (tužka a video). Finále LM 2010: **2 842 událostí** (~1 za 2 s), tři analytici – jeden na každý tým, třetí kontroloval.
- Konkurence 2012: **Prozone** (Leeds) a **Amisco** (Francie; sloučeny 2011) – kamery nad hřištěm a tagování videa; **StatDNA** (USA, Rosenfeld, Rudd); Impire (Německo), Infostrada (Nizozemsko), Match Analysis (USA).
- Data Opta jsou hlavním zdrojem většiny analýz knihy (držení, ztráty, góly a body, formace).

Zdroj: [[Zdroj – The Numbers Game]] (Úvod, Kap. 2–5).

## Souvislosti

[[Wyscout]] · [[StatsBomb]] · [[SkillCorner]] · [[Datový skauting – metriky a úskalí]]
