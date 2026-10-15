---
typ: koncept
tags: [nahoda, xG, hodnoceni, rozhodovani, treneri]
zdroje: ["[[Zdroj – Football Hackers]]", "[[Zdroj – Soccermatics]]"]
aktualizovano: 2026-10-15
---
# Výkon vs. výsledek a role náhody

Ve fotbale se výkon a výsledek rozcházejí víc než v jiných míčových sportech, protože padá málo gólů (~2,7 na zápas). Tabulka proto **není spravedlivý obraz výkonu** – a rozhodnutí podle výsledků (odvolání trenéra, prodej hráče) mohou být rozhodnutí podle náhody ([[Zdroj – Football Hackers]], Kap. 2, 3, 8; navazuje na [[Predikce a pravděpodobnostní modely]] ze [[Zdroj – Soccermatics]]).

## Nástroje

- **xG** – kvalita šancí → [[Expected goals (xG)]].
- **xPoints (Expected Points)** – kolik bodů by tým získal, kdyby góly odpovídaly šancím; „tabulka spravedlnosti“ (Midtjylland).
- **xGplots** (Sander Ijtsma, 11tegen11) – kumulativní xG obou týmů na časové ose 90 minut; ukazuje *příběh* zápasu včetně načasování šancí. Příklad: Belgie porazila Brazílii (MS 2018), ačkoli podle šancí měla v základní hrací době ~4 % na výhru.
- **Signál vs. šum** (Benham): výsledek minulého zápasu je „většinou šum“; vzájemné zápasy a „nepříjemný soupeř“ také. Signál = kvalita šancí, absence klíčových hráčů, dokonce i délka cesty na venkovní zápas.
- **Indikátory štěstí v tabulce:** vysoko umístěný tým s malým kladným skóre; „efektivní“ rozdělení gólů (hodně výher o gól, pár vysokých proher); slabé **net shots on target** (Newcastle 2011/12 – 5. místo, ale 6. nejhorší v tomto ukazateli).

## Případy z knihy

- **Dortmund 2014/15 (Colin Trainor):** o Vánocích 17. místo a 15 bodů; podle xG měli být čtvrtí s ~30 body. Trainor předpověděl návrat – na jaře bez velkých změn kádru získali 31 bodů (**regrese k průměru**). Část propadu byla i skutečná: horší pozice střel, slabší presink (PPDA) a brankáři pod očekáváním → [[Pressing a kolektivní pohyb]].
- **Klopp → Liverpool:** Ian Graham (výzkum Liverpoolu) vyhodnotil, že Dortmund neměl systémový problém, jen smůlu – podklad pro jedno z nejdůležitějších rozhodnutí klubu, angažování trenéra.
- **Newcastle 2011/12 vs. 2012/13:** podle xG skoro stejné výkony, ale +19 bodů nad očekáváním, pak −3; z 5. místa na 16., trenér nejdřív s osmiletou smlouvou, pak terčem kritiky.
- Leicester 2015/16 +12 bodů nad očekáváním, Arsenal −6; Chelsea 2016/17 +17, City −7; WBA 2016/17 −12 (sestup místo 13. místa).
- **Midtjylland (Ankersen, 2016):** po třech porážkách a tlaku fanoušků i sponzora obhájil trenéra Thorupa veřejně přes xG („tabulka spravedlnosti“: 15 bodů pod očekáváním). Příští sezónu titul. Ankersen sám připouští, že správné rozhodnutí může být i špatné, pokud veřejný tlak poškodí klub.
- **D.C. United (MLS, 2017):** totéž zdůvodnění přes xG, ale tým se nezlepšil a skončil předposlední – xG není záruka.
- **Midtjylland zápasově:** trenér dostal po šťastné výhře 1:0 zprávu, že model tým *snížil* v ratingu; naopak ho nikdo nekritizoval za smolnou porážku. Riddersholm to bral jako osvobození od náhody.

## Proč to kluby nedělají

- **Mluvit o štěstí je tabu** – hráči a trenéři se bojí, že by to vedlo k výmluvám; ani o šťastných výhrách se nemluví („udělali jsme si štěstí“). Krawietz (Klopp): fotbal je „šachy s kostkou“.
- Odvolání trenéra často funguje jako rituální oběť; studie ukazují, že výměna trenéra má malý trvalý efekt, a málokdo před ní systematicky ověřuje, zda měl trenér smůlu.
- Pověrčivost hráčů a trenérů (rituály, talismany) je podle autora projev toho, jak velkou roli náhoda hraje.

## Pravidla pro praxi (syntéza)

1. Hodnotit výkon přes kvalitu šancí na **dostatečném vzorku** (půl sezóny je minimum pro závěr o trenérovi).
2. Před rozhodnutím o trenérovi / hráči se zeptat: **je to signál, nebo šum?**
3. Oddělit smůlu od skutečných změn (Dortmund: obojí současně).
4. Komunikovat to i navenek (Ankersen) – ale počítat s tlakem okolí.

## Souvislosti

[[Kognitivní zkreslení v hodnocení]] (outcome bias) · [[Hodnocení utkání a pozápasový report]] · [[Sezónní hodnocení týmu a soutěže]] · [[Brentford a FC Midtjylland]] · [[21st Club]]
