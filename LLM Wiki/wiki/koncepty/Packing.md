---
typ: koncept
tags: [herni-data, metrika, packing, possession-value, impect]
zdroje: ["[[Zdroj – Football Hackers]]", "[[Zdroj – Soccermatics]]"]
aktualizovano: 2026-10-15
---
# Packing

Metrika, která počítá, **kolik soupeřů (hlavně obránců) vyřadí ze hry úspěšná přihrávka nebo driblink** dopředu. Vymysleli ji hráči Bundesligy Stefan Reinartz a Jens Hegeler (Leverkusen), od 2015 ji prodává jejich firma [[Impect]] ([[Zdroj – Football Hackers]], Kap. 1, 5, 6). V [[Zdroj – Soccermatics]] zmíněna jako alternativa Markovových modelů → [[Possession value a Markovovy řetězce]].

## Vznik a definice

- Výchozí otázka: **která data skutečně souvisí s výhrou?** Trenéři argumentovali souboji, naběhanými kilometry, přesností přihrávek – žádná z nich výsledek spolehlivě nepředpovídá.
- Nejdřív zvažovali počítat překonané **linie**, ale fotbal není stolní fotbal → počítají **překonané hráče**. První pokus: ručně, s tužkou, 10 zápasů Dortmundu (Hummels, Subotić).
- Dlouhý míč, který sice přeletí mnoho hráčů, ale skončí v autu = neefektivní akce (0).
- Jméno: německé *packen* (přemoci, „sbalit“) + anglická forma.

## Rodina ukazatelů

| Ukazatel | Co měří | Příklad |
|---|---|---|
| **Bypassed opponents / defenders** (přihrávající) | kolik soupeřů / obránců přihrávka obešla | Kroos ~82 vyřazených soupeřů/zápas vs. Weigl ~42 (Euro 2016) – Tuchel chtěl po Weiglovi právě tohle zlepšit |
| **… receiving** (příjemce) | kolik soupeřů je za hráčem, když míč převezme | Özil ~66/zápas jako příjemce (Euro 2016) – „umí si říct o míč“ mezi liniemi; Müller ~72 (MS 2018) |
| **Zisk míče – vyřazení soupeři** | kolik soupeřů je po zisku za míčem | vysoké u týmů s gegenpressingem |
| **Zisk míče – „vrácení“ spoluhráčů** | kolik spoluhráčů bylo mimo hru před ziskem | záchranný zákrok posledního obránce |
| **Packed teammates po ztrátě** | kolik vlastních hráčů je mimo hru po ztrátě míče | Freiburg 97/zápas (nejlépe) vs. HSV 129 (nejhůř), Bundesliga 2016/17 |

**Hummels vs. Mavraj:** přesnost přihrávek 84,6 % vs. 89,5 % – ale Packing 72 vs. 23 vyřazených/zápas. Přesnost odměňuje bezpečnost, Packing efekt.

## Vztah k výsledku

- Euro 2016: 34 z 51 zápasů vyhrál tým s víc vyřazenými hráči, jen 3 prohrál – silnější vztah než držení nebo přihrávky.
- MS 2018: 7 z 8 týmů s nejvyšším čistým packingem postoupilo ze skupiny (malý vzorek).
- Bundesliga 2016/17: první dva týmy tabulky měly nejvíc vyřazených hráčů; některé týmy kompenzovaly málo vlastního packingu tím, že je soupeř těžko obcházel.
- **„Vlny“ útoků (Reinartz):** obranu nehodnotit jen podle obdržených gólů, ale podle poměru **vln, které obrana zastaví, k počtu vln, které vůbec dostane**. Leverkusen 2016/17 měl dobrou obranu, ale ztrácel míče s 4–5 hráči před míčem → obrana čelila příliš mnoha útokům.

## Od metriky k modelu (Impect, 2018)

Klubové vedení chtělo **jedno číslo** na hráče. Impect proto přepočítal packingové akce na **změnu pravděpodobnosti gólu** (vstřeleného i obdrženého) – ilustrace: přihrávka obránce za dva útočníky +0,5 %, převzetí před obrannou linií soupeře téměř +5 %. Součet za 90 min = přínos hráče; žebříčky pro 6 postů (stoper, pravá a levá strana obrany, defenzivní a ofenzivní záložník, útočník); „Offensive Impect“. Reinartz: „nepostavili jsme index, ale model“. Dále: hledání podle vlastních šablon, porovnání a **komplementarita profilů** (Kanté + Pogba), **variabilita výkonu** (Philipp Max – průměr dobrý, ale 10 výborných a 10 slabých zápasů → názory skautů se rozcházely) → [[Datový skauting – metriky a úskalí]].

> „Tradiční data zachycují dovednosti hráče, naše měří jeho výkon“ (Reinartz, parafráze).

## Úskalí

- **Sběr je drahý:** tracking data pokryjí ~75 %, zbytek ručně; bez trackingu ~7 h na zápas (studenti DSHS Köln, později pobočka v Manile).
- **Zjednodušení zabíjí smysl:** televizní použití (Mehmet Scholl, ARD, Euro 2016) bez vysvětlení udělalo z Packingu terč posměchu.
- **Trenéři ho využívají málo** – na vlastní tým mají dost času s videem; větší hodnota je pro sportovní ředitele a skauting.
- Kontext je nutný: vysoký packing v neúspěšném týmu (Německo na MS 2018) neznamená, že tým hrál dobře.

> [!note] Aktualita (poznámka LLM – ověřit)
> Impect dnes nabízí packingová data pro desítky soutěží a je jedním z běžných providerů vedle Wyscoutu a StatsBombu.

## Využití (návrh)

Packing / „bypassed opponents“ jako metrika progrese ve [[Karta hráče – koncept]] a [[Hodnocení utkání a pozápasový report]] místo přesnosti přihrávek; „packed teammates po ztrátě“ jako ukazatel rizikových ztrát → [[Football Hackers – návrhy pro Sigmu]].

## Souvislosti

[[Possession value a Markovovy řetězce]] · [[Impect]] · [[Normalizace herních dat]] · [[Expected goals (xG)]]
