---
typ: entita
tags: [klub, vzor, recruitment, analytika]
zdroje: ["[[Zdroj – Soccermatics]]", "[[Zdroj – Football Hackers]]", "[[Zdroj – The Numbers Game]]"]
aktualizovano: 2026-10-15
---
# Brentford a FC Midtjylland

Dva kluby vlastněné **Matthewem Benhamem** (majitel sázkových firem Smartodds a Matchbook) – vzorový příklad klubu řízeného daty. Midtjylland koupil 2014 ([[Zdroj – Soccermatics]], Kap. 4, 13; podrobně [[Zdroj – Football Hackers]], Kap. 3, 4, 7, 8).

## Model Midtjylland (k 2015)

- Sportovní ředitel Claus Steinlein: „Dřív jsme měli jednoho skauta… teď máme tým v Londýně, který chroustá čísla.“
- Databáze vytvoří shortlist dřív, než hráče kdokoli vidí živě – **statistika je začátek skautingu, ne náhrada**.
- **Kopací trenér** (analýza rotace míče) a detailní analýza **standardek** → výrazně víc gólů ze standardek.
- O **poločase** dostává trenér rozpad šancí obou týmů.
- Výsledek: první dánský titul (léto 2015).
- Brentford: v knize jen zmínka; Marek Kwiatkowski pracoval jako analytik i pro Brentford.

> [!note] Aktualita (poznámka LLM – ověřit)
> Brentford postoupil 2021 do Premier League a drží se v ní; model je široce kopírován.

## Relevance pro Sigmu

Vzor pro klub menší velikosti: datový shortlist + skauting, standardky jako „levná“ výhoda, poločasové shrnutí šancí → [[Soccermatics – návrhy pro Sigmu]], [[Standardní situace – analýza]], [[Live analýza a poločas]].

## Detail z Football Hackers

- **Benham:** fyzik, derivátový obchodník; sázení chápe jako využívání neefektivního trhu. Brentford podporoval od 2006, většinu koupil 2012. Změny v Brentfordu ale narážely na konzervativní prostředí → experiment přesunul do Dánska, kde Midtjylland potřeboval peníze. Smartodds dodával modely a hodnocení, zaměstnanci dostávají Kahnemanovu knihu. Benham odmítá nálepku „Moneyball“ – fotbal nemá tajný vzorec, výhod je mnoho a některé jsou na tréninkovém hřišti.
- **Lidé v Midtjyllandu:** CEO/předseda **Rasmus Ankersen** (bývalý hráč klubu, autor *The Gold Mine Effect*, spoluzakladatel [[21st Club]]), sportovní ředitel Claus Steinlein, trenéři Glen Riddersholm → Jess Thorup; rozpočet na mzdy ~7 mil. € (polovina rivalů z Kodaně).
- **Recruitment:** na každou pozici 20 kandidátů z databáze Smartodds → video → teprve pak klasický skauting, agenti, rozhovory. Sparv (z 2. BL) jako první hráč doporučený modelem. Největší prodeje (Sörloth 0,4 → 9 mil. €, Sanneh 0,2 → 8 mil. €) ale přišly **od skautů**, data jednoho zpochybnila.
- **Model v zápase:** o poločase SMS s hodnocením šancí; po výhře může model tým snížit v ratingu. KPI pro hodnocení hráčů. „Reverse-engineered xG“ – zjistit, odkud se nejlépe skóruje, a dostávat tam míč. Vedení 1:0 se brání útočně (další útočník v závěru), protože pasivita zvyšuje šanci soupeře.
- **Standardky:** specialista Mads Buttgereit, téměř 1 gól ze standardky na zápas; tituly 2015 a 2018 by bez nich nebyly → [[Standardní situace – analýza]].
- **Lidé a kultura:** osobnostní profily pro celý klub, sportovní psycholog, neurovědec z Oxfordu → [[Osobnostní profily hráčů]]. Akademie (první v Dánsku, 2000) a škola v Nigérii (od 2004).
- **Obrana trenéra přes xG** (Ankersen 2016, „tabulka spravedlnosti“) → [[Výkon vs. výsledek a role náhody]].
- **Marginal gains** podle Sparva: jídlo, regenerace, kvalitní hřiště → [[Strategie menšího klubu]].
- **Brentford:** zrušená akademie (2017) → B-tým a hráči odmítnutí akademiemi PL; specialista na standardky Nicolas Jover (10–15 min denně); velmi detailní dotazy agentům na hráče; chybný datový výběr trenéra (Dijkhuizen z Excelsioru); čtyři sezóny v top 10 Championship s jedním z nejnižších rozpočtů.

## Poznámka z The Numbers Game

Charles Reep, první fotbalový „účetní“ dat a otec teorie dlouhých míčů, pracoval jako analytik mimo jiné pro **Brentford** (a Wolves) – desítky let před Benhamovým projektem → [[Držení míče a ztráty]] ([[Zdroj – The Numbers Game]], Kap. 12).

## Souvislosti

[[Datový skauting – metriky a úskalí]] · [[Predikce a pravděpodobnostní modely]] · [[Oddělení analýzy – struktura a role]] · [[Strategie menšího klubu]] · [[21st Club]] · [[Výkon vs. výsledek a role náhody]]
