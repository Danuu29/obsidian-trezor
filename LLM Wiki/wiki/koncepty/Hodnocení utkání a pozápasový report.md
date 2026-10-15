---
typ: koncept
tags: [utkani, reporting, herni-data]
zdroje: ["[[Zdroj – Analytická témata Sigma]]", "[[Zdroj – Zadání aplikací]]", "[[Zdroj – Barça Match Analysis]]", "[[Zdroj – Soccermatics]]", "[[Zdroj – Football Hackers]]"]
aktualizovano: 2026-10-15
---
# Hodnocení utkání a pozápasový report

Propojení hodnocení utkání od trenérů s GPS a herními daty. Zdroje: [[SK Sigma Olomouc/Analytická témata/🏟️ Hodnocení utkání|🏟️ Hodnocení utkání]], [[SK Sigma Olomouc/Aplikace/Analýza herních dat/Post match report|Post match report]].

## Hodnocení utkání (Yarmill)

Pilot na jednom týmu: kategorie, soupeř, datum, výsledek, sestava a střídání, hodnocení hráčů (známka + slovně), hodnocení utkání, cíle do utkání a jejich plnění, nejlepší hráči, data Wyscout/Eyeball, GPS. Pohledy: vs. poslední utkání, vs. nejlepší utkání. (Linear: YWE-6617.)

## Pozápasová analýza (aplikace)

Kde nás soupeř ohrožoval a kdo propadal; v čem jsme byli lepší; dlouhodobé slabiny; **porovnání s plánem hry** (vložit strategické kroky do zápasu) → [[Aplikace – Analýza soupeře]].

## Metodika post-matche (Barça kurz)

Podle [[Zdroj – Barça Match Analysis]] (P3 R3): post-match vlastního týmu je **výchozí bod obsahu dalšího mikrocyklu** – analytici ho často přeskakují a hned skočí na soupeře. Měří se vzdálenost mezi **očekávaným a dosaženým**.

- **Perspektivy:** akce (technika) → rozhodnutí (taktika) → **match plan** (co dobře / co špatně / co z plánu jsme neudělali a proč: špatný přenos, nenastaly okolnosti, chybělo nasazení) → efektivita.
- **4 otázky zásluhy:** kolik našeho úspěchu je naše zásluha / slabost soupeře; kolik úspěchu soupeře jde na nás / je jeho zásluha.
- Data číst oběma směry (dojem → data, data → závěr); vývoj od počtů přes procenta k advanced metrics (xG, PPDA). **xG nemusí odpovídat výsledku.**
- Kontext metrik: stav skóre (*quite for* +2 / *balanced* / *quite against* −2) a role hráče (základ vs. náhradník) → [[Live analýza a poločas]].
- Každé hodnocení musí jít **ruku v ruce s řešením**; skupinový vs. individuální obsah; individuálně i krátkodobé cíle s rubrikou a GPS v kontextu výkonu.
- Předávání hráčům (poměr klipů, načasování, skupiny po liniích) → [[Video feedback a komunikace s hráči]].

## Myšlenky

- Jak hráč hodnotí utkání při výhře vs. prohře; rozdíl pohledu trenéra a hráče.
- Data z hodnocení dál: report známek, minuty dle kategorie a pozice.
- Prohrané zápasy: hledat nuance oproti vítězným (fyzicky, mikrocyklus).

## Náhoda a výsledek (Soccermatics)

Góly přicházejí náhodně (Poisson) – jednotlivý zápas je silně ovlivněn štěstím. Hodnotit výkon přes **xG a kvalitu šancí**, ne jen výsledek; krátké série (2–3 zápasy, i 50 pokusů) neodliší štěstí od kvality; sledovat udržitelnost konverze ([[Zdroj – Soccermatics]]) → [[Expected goals (xG)]], [[Predikce a pravděpodobnostní modely]].

## Výkon vs. výsledek (Football Hackers)

- **Brazílie–Německo 1:7 (MS 2014):** Brazílie měla lepší držení, víc centrů, rohů, nebezpečných útoků i střel – „klíčové“ ukazatele nebyly klíčové. Bundesliga 2016/17: lepší tým v držení vyhrál jen 54 % rozhodnutých zápasů, v soubojích 56 %, v naběhané vzdálenosti 60 %, ve střelách 61 %, v **šancích 75 %**.
- **Löw 2010:** výroční hodnocení bez výsledků – jen procesní ukazatele (fauly, zisky, **doba držení míče jednotlivcem 2,8 s → 1,1 s**).
- **Vlny útoků:** hodnotit obranu i podle toho, kolik útoků k ní pustí zbytek týmu ([[Packing]]).
- Midtjylland: model hodnotí výkon i po výhře; trenér je kritizován za slabý výkon i při výhře a chráněn při smolné porážce → [[Výkon vs. výsledek a role náhody]].
- Krawietz kontroloval styl přes **počet přihrávek** (~600 v dominantním zápase; víc = spíš sterilní držení) a poměr centrů z obou stran.
- Moyes chtěl „600 přihrávek místo 400“ – Ferdinand: radši 5 gólů z 10 přihrávek. Metrika, která se stane cílem, mění chování (srov. Goodhart v [[Expected goals (xG)]]).

## Souvislosti

[[GPS metriky a zatížení]] · [[Hodnocení hráčů – metodika]] · [[Wyscout]] · [[Sezónní hodnocení týmu a soutěže]] · [[Barça kurz – návrhy pro Sigmu]] · [[Soccermatics – návrhy pro Sigmu]] · [[Výkon vs. výsledek a role náhody]] · [[Kognitivní zkreslení v hodnocení]] · [[Football Hackers – návrhy pro Sigmu]]
