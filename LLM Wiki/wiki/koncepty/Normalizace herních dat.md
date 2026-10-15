---
typ: koncept
tags: [herni-data, metodika, skillcorner]
zdroje: ["[[Zdroj – Zadání aplikací]]", "[[Zdroj – Znalosti]]", "[[Zdroj – Yarmill poznámky]]"]
aktualizovano: 2026-10-15
---
# Normalizace herních dat

Jak převádět herní a fyzická data na srovnatelné hodnoty. Hlavně podle zadání [[Aplikace – Analýza soupeře]] a metodiky [[SkillCorner]].

## Přepočty

- **Per 90:** `SUM(metrika) / SUM(odehrané minuty) × 90` – typicky fyzická data.
- **Per 30 TIP / OTIP:** `SUM(metrika) / SUM(minuty v držení / bez držení týmu) × 30` – odstraní vliv dominance týmu na míči; vhodné pro **styl (DNA)** a skauting.
- **Per match** – pro hodnocení **absolutní hrozby** pro naši obranu.
- **Rychlosti (PSV-99)** nenormalizovat – prostý průměr; time to sprint = průměr 3 nejlepších pokusů.
- **100 situací** – typické chování hráče bez ohledu na tým.
- Granularita: `group_by=match` (řádek = hráč × zápas) – nutné pro formu v čase a propojování.

## Vážené průměry (Yarmill poznámky)

Vážit délkou zápasu, odehranými minutami, fází nástupu a kvalitou soupeře.

## Kontext je víc než procenta

Příklad z ladění aplikace: nižší % zisků ve středu hřiště není slabina, pokud se neporovná s celkovým počtem míčů v té zóně – soupeř může hrát po krajích. → Data vždy vyhodnocovat v kontextu.

## Souvislosti

[[GPS metriky a zatížení]] (přepočet na čistý čas hry) · [[Skauting – proces a reporting]]
