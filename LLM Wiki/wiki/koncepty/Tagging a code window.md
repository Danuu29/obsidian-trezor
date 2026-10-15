---
typ: koncept
tags: [tagging, video, software, event-data, barca]
zdroje: ["[[Zdroj – Barça Match Analysis]]"]
aktualizovano: 2026-10-15
---
# Tagging a code window

Ruční klasifikace událostí z videa podle předem daných kritérií a nahrávání videa, které jí předchází (P4 M3–M4, P3 R2 [[Zdroj – Barça Match Analysis]]; ukázky ze Sportscode). Vlastní tagging doplňuje externí event data ([[Wyscout]]) o to, co odpovídá **našemu hernímu modelu**.

## Pojmy

- **Event** = action (co) + timestamp (kdy) + status (kontext: hráč, situace) – Wetzler 2017.
- **Code** = pojmenovaná sekvence s trváním (např. organized attack). *Manuální* (stisk na začátku a konci) vs. *automatický* (jeden stisk s **lead / lag time**).
- **Tag (label)** = deskriptor upřesňující code (direct, shot on goal…); jeden code může mít víc tagů.
- **Notes** = volný text k tomu, co kódy nepokryjí.
- **Timeline** = řádky kódů v čase; **event matrix** = kódy × tagy s počty a prolinkem na klipy, export do Excelu; kombinace tagů hledá vzorce.
- **Code window / push button panel / botonera** = panel tlačítek – základ celé analýzy.

Analytik není „klasifikátor videa“ – klíčová je znalost hry a schopnost interpretovat; rychlost přichází praxí. **Před analýzou vyčerpávajícím způsobem kategorizovat všechny prvky hry** (implicitně operační definice).

> [!note] Doplnění (návrh)
> Kurz explicitně neřeší **inter-rater reliability**. Pro Sigmu – kde by tagovalo víc lidí napříč kategoriemi – ke každému kódu napsat operační definici a občas ověřit shodu mezi tagujícími.

## Struktura code window

Standardní klasifikace podle [[Herní cyklus]] (každý si ji upraví podle svého modelu): **Offense** (start of play, organized / fast / direct attack, counterattack, změny orientace, centry) · **Defense** (pressing, návrat do bloku, defensive transition, presink po ztrátě, výška bloku) · **Set pieces** (samostatný panel: strana, inswing/outswing, tyč, dorážka, druhý míč).

Pokročilý panel („Botonera M-Tamarit“): hlavička s metadaty (soutěž, datum, kolo), START short/long, organized attack (combination/direct, between lines), counter-offense, události recovery / loss / offside / shot a **zónová mřížka 3 × 4** (levá/střed/pravá × 4 pásma).

Další vzory: FFA (*Counter / Pressure / Retain*, Entry do vápna, tlačítka **Review** a **Error**), Španělsko MS 2018 (Attack start–continuity–finishing; Defense low/mid/high block) → [[Live analýza a poločas]].

## Software

| Software | Výrobce | OS |
|---|---|---|
| Hudl Sportscode | Hudl | Mac |
| Nacsport | Nacsport | Windows |
| LongoMatch | Fluendo | Mac, Windows, Linux |
| Eric | Eric Sports | Windows |
| Vision | Catapult | Mac |
| Video Observer | Video Observer | Mac, Windows |
| Coach Capture | ChyronHego | Mac, Windows |
| Angles | Fulcrum | Mac |

Telestrace: Coach Paint, KlipDraw, RT Software (Edit-3D); obecně Adobe (Photoshop → Illustrator → After Effects → Premiere / Final Cut).

## Tagování tréninku

Proměnné: období, číslo mikrocyklu, číslo jednotky, datum, příští soupeř, den (*návrh:* MD+x/−y → [[Mikrocyklus a značení MD]]), **typ úkolu**, rozvíjené koncepty. Účel: tréninková databáze a ověření, **zda to, co trénujeme, přenášíme do zápasu**.

## Nahrávání videa

- **Interní** záznam (plná kontrola) vs. **externí** (TV, platformy, výměna s jinými kluby – budovat vztahy).
- Pro taktiku vždy **panoramatický / tactical feed** z **dostatečné výšky ze středu tribuny** – nízká kamera zkresluje vzdálenosti mezi liniemi. Preferovat optický zoom.
- Akční kamera pro trénink brankářů; drony a multikamery podle rozpočtu.
- *Syntéza:* kvalita panoramatického záběru je i předpokladem trackingu z videa ([[SkillCorner]], [[Eyeball]]).

## Souvislosti

[[Aplikace – Match tracker]] · [[Typy sportovních dat a datová architektura]] · [[Oddělení analýzy – struktura a role]] · [[Plány analýzy (micro, meso, macro)]]
