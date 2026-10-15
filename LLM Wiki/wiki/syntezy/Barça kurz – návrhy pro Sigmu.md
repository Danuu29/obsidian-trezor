---
typ: synteza
tags: [navrhy, sigma, yarmill, analyza, barca]
zdroje: ["[[Zdroj – Barça Match Analysis]]"]
aktualizovano: 2026-10-15
---
# Barça kurz – návrhy pro Sigmu

*Syntéza / návrhy LLM*: co z [[Zdroj – Barça Match Analysis]] lze přenést do práce v [[SK Sigma Olomouc]] a [[Yarmill]]. Nic z toho zatím není rozhodnuté – seznam k probrání. Seřazeno podle projektů.

## [[Aplikace – Analýza soupeře]]

1. **Struktura reportu podle B.1–B.5**: general data → background (vč. *soupeře našeho soupeře*) → sestavy a střídání (minuta + skóre) → match plan soupeře po fázích (útok start/progression/finishing; obrana high/mid/low block; DAT; ADT; SP) → hráči. Hlídat „bez konceptuálních rozporů“ mezi sekcemi.
2. **Katalog otázek** (fáze × třetina × blok soupeře) převzít jako checklist do promptu.
3. **Filtry výběru zápasů**: posledních N, doma/venku, vzájemné zápasy, zápasy proti týmům podobným Sigmě, jak na soupeře vyzráli jiní.
4. **Skóre užitečnosti insightu** = True × Significant (frekvence „n z N zápasů“) × Trainable → méně jednorázových jevů, méně „overdose“.
5. Ke každé silné stránce soupeře strategie **Avoid / Condition / Assume** + návrh tréninkové úlohy (karta úlohy, rozměry SSG podle IPA).
6. **Insight report** jako „match plan card“: 3–4 řádky podmínka → řešení (odpovídá požadavku na krátký insight report).
7. Klasifikace **G.T.P.** (build-up / movement / defensive) z dat (PPDA, výška bloku, přímost) → predikce „formátu“ zápasu jako úvodní odstavec.
8. Individuální karty hráčů soupeře: checklist + 1–2 věty evidence + „kde konfrontovat“; personalizované výřezy pro naše hráče (protihráč).
9. Samostatný **SP modul** (šablony Kicker/Finishers… a Zone/Man/Wall…, one-page summary modře/červeně).

## [[Aplikace – Match tracker]]

1. Porovnat tlačítka s code windows Španělska a FFA; přidat **Review** a **Error**, případně lead/lag čas pro pozdější napojení na video.
2. **Statistické alarmy** – prahy z průměrů týmu/soupeře, zvýraznit při překročení.
3. **Poločasový balíček**: řazení podle herního cyklu, 3–5 klipů / situací, struktura dobře → špatně → pokyny jako řešení.
4. Live report max. ~9 metrik na obrazovku (vzor [[Mediacoach]]).
5. Sepsat **live protokol** (markery z game planu → check-in v prvních minutách → urgent/important → poločas) a řetězec analytik → asistent → trenér.

## [[Hodnocení utkání a pozápasový report]]

1. Sekce **„plán vs. realita“**: co dobře / špatně / co z plánu nenastalo a proč (přenos, okolnosti, nasazení) + 4 otázky zásluhy.
2. Filtry **kontextu skóre** (quite for / balanced / quite against) a role hráče (základ ≥ 60′ / náhradník < 30′).
3. Individuální post-match karta: souboje s řešeními, krátkodobý cíl s rubrikou, fyzická data vs. průměr posledních 2 měsíců.
4. Video pravidla: poměr 1 : 1 (2 : 1 při nízké sebedůvěře), menší schůzky po liniích, post-match 1–2 dny po zápase.

## Tréninkový proces a akademie

1. Značení **MD+x/−y** v Yarmillu pro plány i GPS → [[Mikrocyklus a značení MD]].
2. Šablony týdne pro rozložení videa (self-analysis, soupeř, SPA).
3. Feedback po tréninku (asimilace total / partial / null) jako krátký formulář.
4. **Tagování tréninku** s metadaty (MD, typ úkolu, koncepty) → ověřit transfer trénink → zápas.
5. Tactical communication slovník počeštit a sjednotit s [[Sigma Way]] → [[Taktická komunikace]]; měřit konzistenci v [[Aplikace – Analýza audio trenéra]].
6. **IFP klipová knihovna** po postech + functional role jako druhá osa hodnocení → [[Individuální fundamenty postů (IFP)]], [[Postové profily]], [[Karta hráče – koncept]].
7. Matice pozice × 4 subfáze (Cano Moreno) jako checklist pro hodnocení hráčů.

## Datové oddělení

1. Pozicovat oddělení pod **sportovní vedení** (kontinuita know-how při výměně trenérů); role chief analyst.
2. Architektura data lake → warehouse (sjednocená ID hráčů a zápasů napříč SkillCorner, Wyscout, GPS, Eyeball) → BI v Yarmillu; governance → [[Typy sportovních dat a datová architektura]].
3. KPI vybírat podle herního modelu a matice relevance × frekvence; customizovat kombinovanými indexy.
4. **Manual of metrics** – glosář definic a opakovaných dotazů trenérů (mohl by žít v této wiki).
5. Etika: data o práci kolegů neukazovat vedení bez jejich souhlasu; barvy přístupné barvoslepým.
6. U hodnoticích modelů akademie sledovat false positives / negatives.
7. Vlastní záznam mládeže: panoramatický záběr z výšky; výměna videa s jinými akademiemi.
8. Sezónní hodnocení: SP efektivita vs. liga, góly podle typu a 15min intervalů, dynamika skóre → [[Sezónní hodnocení týmu a soutěže]].

## Souvislosti

[[Přehled wiki]] · [[Otevřené otázky]] · [[Oddělení analýzy – struktura a role]]
