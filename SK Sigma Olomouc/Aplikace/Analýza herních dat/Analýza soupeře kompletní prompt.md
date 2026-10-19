---
apple-notes-id: 3A1A1B54-0C15-4931-9AD4-2DC29423E997
---
#app 
# MOJE VERZE 

1. Připojení zdroje dat SkillCroner 
- Zdroj dat kompletní knihovna SkillCorner’s Python SDK
- Připoj ji na základě dokumentace z odkazu: https://skillcorner.readthedocs.io/en/latest/
- Přihlašovací údaje uživatelské jméno: [tomascerny2002@gmail.com](mailto:tomascerny2002@gmail.com), heslo: Sigma1919
- Použij všechny dostupné soutěže pro tento uživatelský účet - měly by to být tyto soutěže. 
	- AUT - Bundesliga, BEL  - Pro League, CZE First League, CZE - FNL, DEN - Superliga, ESP - LaLiga2, NOR - Eliteserien, POL - ekstraklasa, SVK - Niké Liga, SVN - 1. SNL, SWE - Allsvenskan, UEFA - Europa Conference League, UEFA - Europa Conference League - Qualicifation, UEFA - Europa League - Qualicifation
- Zde jsou informace k doporučenému nastavení datového modelu pro optimální práci s daty: 
Tento model je navržen tak, aby efektivně propojoval data o hráčích, fyzických výkonech, herní inteligenci (Game Intelligence) a fázích hry (Phases of Play), a umožňoval správné filtrování napříč reporty.
Základním principem je volání API s parametrem group_by=match, což zajistí nejlepší granularitu dat (jeden řádek = jeden hráč v jednom zápase), která je klíčová pro sledování formy v čase a propojování s dalšími databázemi.
--------------------------------------------------------------------------------
1. Dimenze (Lookup / Dimension Tables)
Tyto tabulky obsahují statické informace a slouží k filtrování dat (např. výběr konkrétního hráče, týmu nebo pozice).
**Dim_Player (Tabulka Hráčů)** Získává se z endpointu /players.
• player_id (Primary Key)
• player_name
• team_id (Foreign Key)
• position_acronym (např. CB, CM, FB)
**Dim_Position_Sort (Pomocná tabulka pozic)** Dle doporučení se vytváří manuálně pro správné řazení a seskupování pozic ve vizualizacích.
• position_acronym (Primary Key)
• position_group (např. Defenders, Midfielders)
• sort_order (číselné pořadí pro řazení grafů)
**Dim_Match / Dim_Competition (Tabulka zápasů a soutěží)**
• match_id (Primary Key)
• competition_edition_id (např. 543 pro Premier League 23/24)
• match_date
• home_team_id / away_team_id
**Dim_Team (Tabulka týmů)**
• team_id (Primary Key)
• team_name / team_shortname
--------------------------------------------------------------------------------
2. Datové tabulky (Fact Tables)
Tyto tabulky obsahují samotné metriky. Všechny jsou napojeny na dimenze pomocí ID. Vzhledem k rozsahu metrik SkillCorner je nejlepší rozdělit je do logických celků.
**Fact_Physical_Data (Fyzické metriky)** Získává se z endpointu /physical s parametrem group_by=match.
• *Klíče:* player_id (FK), match_id (FK), team_id (FK)
• *Kontext:* minutes_played
• *Metriky (Příklad):* distance_per_90, sprint_distance_per_90, hi_count_per_90, avg_psv99, avg_top_3_time_to_sprint, cod_count_per_90.
**Fact_Game_Intelligence_In_Possession (Útočné GI metriky)** Data, když má tým míč. Pro správné srovnání je nutné využívat metriky normalizované na 30 minut držení míče (TIP).
• *Klíče:* player_id (FK), match_id (FK)
• *Kontext:* minutes_in_possession
• *Metriky (Příklad):* count_possessions_per_30_tip, count_runs_in_behind_per_30_tip, count_dangerous_passes_per_30_tip, count_carries_at_speed_per_30_tip, count_forward_momentum_per_30_tip.
**Fact_Game_Intelligence_Out_of_Possession (Obranné GI metriky)** Data, když má míč soupeř, normalizovaná na 30 minut (OTIP).
• *Klíče:* player_id (FK), match_id (FK)
• *Metriky (Příklad):* count_on_ball_engagements_per_30_otip, count_pressing_engagements_per_30_otip, direct_disruption_or_regain_percentage, stop_or_reduce_danger_percentage.
**Fact_Phases_of_Play (Fáze hry - Týmová úroveň)** Nejnovější tabulka struktury zápasu na základě CSV specifikací fází hry.
• *Klíče:* match_id (FK), team_in_possession_id (FK)
• *Identifikátory fáze:* index (pořadí fáze), period (poločas)
• *Časování:* time_start, time_end, duration
• *Kategorizace:* team_in_possession_phase_type (Build up, Create, Finish, atd.), team_out_of_possession_phase_type (Low block, High block, atd.).
• *Události ve fázi:* team_possession_lead_to_shot (TRUE/FALSE), team_possession_lead_to_goal (TRUE/FALSE).
• *Geometrie:* x_start, y_start, channel_start, third_start a šířka/délka formace týmu (team_in_possession_width_start atd.).
**Fact_Team_Metrics (Agregované týmové metriky)** Agregovaná data za celý tým v daném zápase.
• *Klíče:* match_id (FK), team_id (FK)
• *Metriky (Příklad):* player_av_distance_per_90, percentage_of_in_possession_time_in_build_up, percentage_high_blocks_leading_to_disruption.
--------------------------------------------------------------------------------
3. Vztahy a logika propojení (Relational Model)
Aby datový model (např. v Power BI) fungoval správně při filtrování, je nutné nastavit vztahy (Relationships) podle následujících pravidel:
1. **Klíče k propojení:** Zásadním klíčem pro propojení dimenze Dim_Player a datové tabulky např. Fact_Physical_Data je pole player_id.
2. **Kardinalita (Cardinality):** Vztah musí být typu **One-to-Many (1:N)** – jeden hráč v tabulce Dim_Player (unikátní záznam) má mnoho řádků v datových tabulkách Fact_* (jeden řádek pro každý odehraný zápas).
3. **Směr filtrování (Cross-filter direction):** Model by měl mít nastaven směr filtrování na **"Both" (Obousměrně)**. Tím zajistíte, že pokud ve vizualizaci vyfiltrujete například pouze hráče, jejichž maximální rychlost (PSV) je menší než určitá hodnota v datové tabulce, propíše se tento filtr zpět do tabulky hráčů a ovlivní i ostatní vizuály v reportu.
4. **Pomocné tabulky:** Pokud vytvoříte Dim_Position_Sort (skupiny pozic), propojte ji s tabulkou Dim_Player přes position_acronym. Zde použijte vztah Many-to-One (mnoho zkratek na jednu skupinu).
4. Tvorba metrik a Normalizace (DAX logika)
V analytickém nástroji budete s těmito daty pracovat pomocí vzorců. Dokumentace upozorňuje na to, že pokud vytváříte vlastní souhrnné metriky (např. přes celou sezónu), musíte je správně normalizovat a nesmíte pouze "průměrovat průměry":
• **Per 90:** (SUM(metric_value) / SUM(minutes_played)) * 90.
• **Per 30 TIP:** (SUM(metric_value) / SUM(minutes_in_possession)) * 30.
• **Percentil a extrémy (např. PSV):** Pro metriky jako psv99 žádnou normalizaci neprovádíte, používá se prostý průměr AVERAGE(psv99). Naopak u časových sprintových údajů (time_to_sprint) se bere průměr ze 3 nejlepších pokusů.

1. Vytvoř mi aplikaci
- Aplikace bude vytvářet přípravu na soupeře 
- Výchozí tým je vždy SK Sigma Olomouc (ID 536). Pro tento tým si vytvoříme databázi, ve které budeme mít vždy stažená veškerá data aktuální probíhající sezóny aby nebylo potřeba při každé analýze data znovu načítat. Stačí pouze udělat kontrolu jestli jsou tam data nejaktuálnější a případě je doplnit o aktuální data
- Dále vytvoříme základní filtry:
	- Soupeře - tým na který budeme vytvářet strategii a přípravu
	- Soutěže - možnost výběru, ze soutěží, které daný tým hraje pro analýzu
	- Období datu od kdy, do kdy - Období, ze kterého budu čerpat data pro analýzy

1. Logika tvorby reportu
- Chci, aby report zohledňoval silné a slabé stránky Sigmy Olomouc a silné a slabé stránky soupeře a vždy mezi tím hledal kontext, kde je možné soupeře nejvíce ohrozit v kontextu našich silných stránek a jeho slabin a naopak kde nás může soupeř nejvíce ohrozit na základě našich slabin a jeho silných stránek v tomto ohledu
- Používat ale veškerá dostupná data k soupeři

1. Podrobné informace pro analýzu
- Report bude mít vždy strukturu
	- Základní charekteristika soupeře - jaký styl fotbalu hraje, v čím je typický, kdo jsou jejich klíčový hráči. Krátký souhrn, který udělá jasnou představu o tom, jaký hraje soupeř fotbal a co od něho čekat 
	- Pasáž utkání, kdy je soupeř nejsilnější a podle čeho soudíš, pasáž hry kdy je soupeře nejzranitelnější a proč
	- Nejčastější rozestavení které hrají
	- Výstavba hry - jak se soupeř typicky chová ve výstavbě hry, kteří hráči jsou nejčastěji využívaní, kteří jsou ale naopak v této části využívaní méně, protože například špatně řeší situace pod tlakem. Tuto část přípravy využijeme proto, abychom věděli, jak soupeře co nejefektivněji napadat a do jakých prostor ho například dostat, kde bude nejzranitelnější. Graficky znázorni průměrné postavení v této fázi hry na základě analyzovaného období. 
	- Způsob vedení útoku - jak se nejčastěji chovají při vedení útoku, kteří hráči jsou nejsilnější tvůrci hry, jaké části hřiště jsou nevytíženější. Opět budeme na tuto situaci reagovat jak se chovat ve středním obranném bloku. Graficky znázorni průměrné postavení v této fázi hry na základě analyzovaného období. 
	- Finální fáze - jak se nejčastěji chovají ve finální fázi hry. Jaké druhy náběhů nebo průniků do pokutového území používají, v čem jsou nejsilěnší, kteří hráči jsou nejvíce nebezpeční, z jakých prostor se nejčastěji dostávají do pokutového území, kteří hráči jsou nejvíce nebezpeční v zakončení, kteří naopak v tvorbě šancí, apodobně. I pro tuto fázi je dobré vytvořit průměrné postavení. Jsou to důležité informace, abychom věděli, na jaké hráče si dát pozor, jak se typicky chovají a jaké například zaujímat postavení nebo také jaké hráče dát do základní sestavy v reakci na hru soupeře. 
	- Presink - jak se chová soupeř při rozehrávce jeho soupeře. Napadá vysoko a ihned po rozehře, jde spíše do bloku, kolik hráčů napadá, atd. Všechny informace, které mohou vést k tomu, abychom věděli, jaký optimální scénář zvolit pro rozehru od naší branky. 
	- Jak se soupeř chová při hře v bloku - jak jsou konzistentní, jak mají hustý blok, kde mají volné prostory a kudy by bylo ideální vést útok a jakým způsobem. Jestli hrát více do nohy, jestli více rozebíhat a proč. 
	- Jak se chová soupeře ve svém vlastním pokutovém území - jsou silní ve vzduchu, ve hře po zemi, propadávají jim míče, mají problémy s centry nebo naopak průniky. 
	- Zhodnotit silné a slabé stránky soupeře
	- Udělat základní charakteristiku hráčů soupeře (ideálně hráčů nejvíce vytížených, kteří připadají v úvahu, že budou nastupovat v základní sestavě nebo dostřídávat v průběhu utkání) 
		- Silné stránky a na co si u něho dát pozor 
		- Slabé stránky a co je důležité o něm vědět pro naši hru, čeho u něho vyžít
		- Jaká je jeho charakteristická hra
		- Jeho maximální rychlost 
		- Označit jejich klíčové hráče a proč je za klíčové považovat
	- Upozornění a doporučení - Co se na základě vzájemné analýzy zjistilo a stojí za to si říct. Hodně do kontextu dávat hráče, kteří budou pravděpodobně hrát proti sobě ze všech možných hledisek (například: soupeř má rychlého levého útočníka a my máme pomalého pravého stopera. Atd..)
	- Zvažuj a dávej také informace v kontextu jak se mění hra pokud tým prohrává nebo naopak vede, jak reagují na vývoj utkání. Pokud najdeš jakékoli abnormality v různém kontextu, tak o tom informuj. 
	- Všechna data brát maximálně v kontextu, co to půjde. Porovnávat hru celého týmu v návaznosti na data jednotlivých hráčů a vše zasazovat do kontextu
	- Používat co nejvíce věcné informace přenositelné do hry
	- Vyvarovat se protichůdným informacím a vše mít podložené a vědět, proč to tvrdím
	- Důkladně si dát záležet na to, aby byla použitá data správného týmu
	- Důkladně také kontrolovat, že jsou použitá správná data se správným významem

Doporučení postupy pro práci s daty
1. Pravidla pro normalizaci dat (Jak data číst)
Při hodnocení soupeře musíš rozlišovat, zda hodnotíš jeho *herní styl* (DNA), nebo *absolutní hrozbu* pro náš tým.
• **Pro zjištění herního stylu soupeře:** Používej metriky percentage_of_... (např. kolik % času s míčem tráví ve výstavbě) a _per_30_tip / _per_30_otip (aktivity přepočítané na 30 minut čistého času držení míče). Tím odfiltruješ, zda soupeř dominuje v držení míče, nebo jen brání.
• **Pro přípravu naší obrany:** Sleduj metriky _per_match (na zápas). Trenér potřebuje vědět, kolika absolutním náběhům za obranu nebo kolika pokusům o překonání linie budeme čelit během 90 minut.
• **Pro hodnocení efektivity/kvality:** Sleduj metriky _per_100_events nebo _percentage (úspěšnost).
--------------------------------------------------------------------------------
2. Analýza Herního stylu a Týmové geometrie (Team Shape)
Než začneš analyzovat jednotlivce, definuj, jak soupeř hraje jako tým.
**A. Kde tráví čas (Posession Time):**
• Zkontroluj percentage_of_in_possession_time_in_... (Build_up, Create, Finish, Direct, Quick Break).
• *Interpretace:* Vysoké % v Build_up a Create znamená kombinační tým. Vysoké % v Direct nebo Quick_Break značí tým hrající na dlouhé nákopy nebo protiútoky.
**B. Týmová geometrie (Team Shape):**
• Sleduj avg_team_length (délka/kompaktnost) a avg_team_width (šířka) v různých fázích.
• *Zásadní zjištění:* Je tým soupeře v obraně (Low/Medium/High block) kompaktní (malá team_length), nebo roztažený? Roztažený tým = prostor mezi liniemi pro naše ofenzivní záložníky.
--------------------------------------------------------------------------------
3. Analýza Útoku Soupeře (In Possession) & Naše obranná doporučení
**A. Jak budují hru (Build-up & Progression):**
• Sleduj percentage_build_up_phases_leading_to_create vs. ...leading_to_possession_loss.
• *Hrozby:* Kdo jsou jejich dispečeři? Hledej hráče s nejvyšším count_pass_attempts_through_first_line_per_30_tip a ..._through_second_last_line. To jsou hráči, kteří propichují naše linie.
• *Doporučení:* Pokud tým A spoléhá na jednoho hráče s vysokým počtem "Line Breaks", doporuč osobní bránění nebo odstínění tohoto hráče. Pokud často ztrácejí míč v Build-upu (possession_loss_in_phase_build_up), doporuč náš vysoký presink.
**B. Kde hrozí v útočné třetině (Creation & Finish):**
• Podívej se na náběhy (Off-ball runs). Používají spíše count_runs_in_behind (náběhy za obranu), count_cross_receiver (centry do vápna) nebo overlap/underlap na křídlech?
• Sleduj kvalitu: Kdo generuje nejvyšší runs_threat_per_match (kdo se nejlépe pohybuje bez míče do nebezpečných zón) a kdo má vysoký počet dangerous_passes.
• *Doporučení:* Pokud má soupeř útočníky s vysokým PSV-99 (maximální rychlost) a vysokým objemem runs_in_behind, doporuč, aby naše obranná linie (Last line) stála hlouběji a nelákala je k náběhům za záda.
--------------------------------------------------------------------------------
4. Analýza Obrany Soupeře (Out of Possession) & Naše ofenzivní doporučení
**A. Kde a jak napadají (Pressing Strategy):**
• Sleduj, kolik času tráví v High_block, Medium_block a Low_block.
• Jak jsou agresivní? Zkontroluj count_pressing_engagements (týmový presink) a count_counter_press_engagements (okamžitý represink po ztrátě míče).
• *Doporučení:* Pokud má soupeř vysoký podíl represinku (counter_press), doporuč našim hráčům po zisku míče "hrát první nebo druhou přihrávku rychle z prostoru zisku" nebo volit dlouhý nákop, abychom se vyhnuli jejich pasti.
**B. Zranitelnost obrany (Defensive Flaws):**
• Filtruj obránce soupeře podle metrik beaten_by_possession_percentage (překonán driblinkem 1v1) a beaten_by_movement_percentage (hráč soupeře mu utekl bez míče).
• *Doporučení:* Pokud má levý bek soupeře vysoké beaten_by_possession, instruuj našeho pravého křídelníka (ideálně s vysokým count_carries_at_speed), aby proti němu neustále chodil do izolací 1 na 1.
--------------------------------------------------------------------------------
5. Analýza Tranzicí (Přechodové fáze)
Zápasy se často rozhodují při změně držení míče.
• **Ofenzivní tranzice soupeře:** Když soupeř získá míč v hlubokém bloku (Low_block), přechází do postupného útoku (leading_to_build_up), nebo chodí do rychlých brejků (leading_to_transition/quick_break)?
• **Defenzivní tranzice soupeře:** Využívají obránci soupeře často recovery_press (sprinty dozadu)? Jsou fyzicky schopní se vracet (sprint_distance, time_to_sprint)?


1. Další požadavky
- Report musí být možné vyexportovat do PDF v co nejlepší vizuální formě. Ideálně černý text na bílém pozadí se zvýrazněním nejdůležitějších informací. Bez zbytečných grafických prvků a bez zbytečností navíc
- Dělej historii vygenerovaných reportů a uchovávej je, dávej ale možnost tyto reporty mazat 
- Dej možnost sdílet výsledný report přes odkaz - nemůže být možné po otevření odkazu dále editovat
- Využívej pro analýzu nejnovější AI model Gemini (API KEY: AIzaSyBXshYWxBAX066-8BNrg6OPD62FrC0fZIY)
- Tvoji finální aplikaci kompletně otestuj
- Dej mi odkaz na kterém budu moc aplikace používat

1. Kompletní metodika a slovník metrik
- Uchovej si v extra souboru proto, aby si vždy věděl, co přesně jednotlivé metriky znamenají a jak s nimi metodicky pracovat
Zde je kompletní, strukturovaná metodika a datový slovník všech metrik SkillCorner (včetně agregovaných dat i surových dat z Dynamic Events). Tento přehled je koncipován jako čistá znalostní báze pro AI model, aby přesně chápal výpočty, definice a význam jednotlivých proměnných.
--------------------------------------------------------------------------------
1. ZÁKLADNÍ PRINCIPY A NORMALIZACE
Všechny agregované metriky jsou normalizovány pro spravedlivé porovnání hráčů:
• **_per_90**: Přepočet na 90 odehraných minut (typické pro fyzická data).
• **_per_30_tip (Team In Possession)**: Přepočet na 30 minut čistého času, kdy má tým míč. Odstraňuje zkreslení z dominance držení míče (typické pro ofenzivní metriky).
• **_per_30_otip (Opponent Team In Possession)**: Přepočet na 30 minut čistého času, kdy má míč soupeř (typické pro defenzivní metriky).
• **_per_100_events**: Procentuální úspěšnost / konverzní poměr ze 100 definovaných událostí.
• **_percentage**: Hodnota vyjádřená v procentech (úspěšné / celkové * 100).
--------------------------------------------------------------------------------
1. PREDIKTIVNÍ AI MODELY (JÁDRO HODNOCENÍ)
Tyto proměnné přidávají událostem kontext pravděpodobnosti a nebezpečnosti:
• **xthreat (Expected Threat)**: Pravděpodobnost (0 až 1), že tým vstřelí gól do 10 sekund, pokud by hráč v daný moment přijal přihrávku.
• **xpass_completion**: Pravděpodobnost (0 až 1), že konkrétní přihrávka bude úspěšně zkompletována. Pokud je xPass < 0,65 (65 %), je přihrávka definována jako **difficult (obtížná)**.
• **passing_option_score**: Skóre z *Receiver Modelu*, které určuje pravděpodobnost, že se hráč stane adresátem přihrávky. Hráč je považován za „Passing Option“, pokud je toto skóre > 0,6.
• **peak_passing_option_frame**: Teoretický moment pro výpočet výše zmíněných metrik u hráče, který *nedostal* míč. Je to okamžik (snímkování), který maximalizuje rovnici: passing_option_score * xthreat * xpass_completion.
--------------------------------------------------------------------------------
3. FYZICKÉ METRIKY (PHYSICAL METRICS)
*Definují pohybové schopnosti, intenzitu a agilitu hráče a týmu.*
• **distance_per_90**: Celková uběhnutá vzdálenost.
• **running_distance_per_90**: Vzdálenost uběhnutá rychlostí 15–20 km/h.
• **hi_distance_per_90 / hi_count (High-Intensity)**: Vzdálenost a počet náběhů nad 20 km/h (součet HSR + Sprintů).
• **hsr_distance_per_90 / hsr_count (High Speed Running)**: Vzdálenost a počet úseků v rychlosti 20–25 km/h.
• **sprint_distance_per_90 / sprint_count**: Vzdálenost a počet úseků nad 25 km/h.
• **avg_psv99 / avg_top_5_psv99 (Peak Sprint Velocity)**: 99. percentil maximální rychlosti hráče (nebo průměr 5 nejlepších), eliminuje chyby měření.
• **explacceltohsr_count_per_90 / explacceltosprint_...**: Počet explozivních akcelerací (vysoké zrychlení z <9 km/h na >20 km/h resp. >25 km/h).
• **avg_top_3_time_to_hsr / ..._to_sprint**: Průměr ze 3 nejrychlejších časů potřebných k dosažení cílové rychlosti z klidu. Ukazuje absolutní výbušnost.
• **cod_count_per_90 (Change of Direction)**: Počet intenzivních změn směru.
• **..._post_cod**: Výbušnost po změně směru (jak rychle hráč dosáhne HSR/Sprintu ihned po COD).
• **time_to_505_around_90 / ..._180**: Čas agility testu na hřišti (uběhnutí 5m před a 5m po otočce o 90° nebo 180°).
• **player_av_...**: Tyto metriky existují i jako průměr pro všechny hráče v týmu (např. průměrná uběhnutá vzdálenost na hráče v týmu).
--------------------------------------------------------------------------------
4. METRIKY S MÍČEM A TVORBA HRY (IN POSSESSION - ON BALL)
*Hodnotí hráče v kontrole míče (Player Possession).*
• **count_possessions_...**: Počet situací, kdy má hráč míč plně pod kontrolou (jedno-doteky se počítají, odrazy a bloky ne). Lze filtrovat dle fází hry (..._in_build_up, ..._in_create, ..._in_finish, ..._in_transition).
• **count_receptions_in_tight_space...**: Přijetí míče v úzkém prostoru (obránce byl blíže než 2 metry).
• **count_carries_at_speed...**: Držení míče/driblink delší než 8 metrů vedený rychlostí minimálně 15 km/h (running speed).
• **count_forward_momentum...**: Progresivní výsledek okamžitě z prvního doteku (hráč dokázal při přijetí zrychlit nebo se otočit čelem vpřed, a to ve středním pruhu / half-space, když byl pod tlakem do 6 metrů).
• **count_quick_passes...**: Přihrávky na jeden nebo dva rychlé doteky.
--------------------------------------------------------------------------------
5. PŘEKONÁVÁNÍ OBRANY A PŘIHRÁVKY (PASSING & LINE BREAKING)
*Hodnocení schopnosti tvořit hru a propichovat formaci soupeře.*
• **count_dangerous_passes...**: Počet přihrávek, které měly xthreat > 0.02 (vysoká šance na gól).
• **count_difficult_passes...**: Počet přihrávek, které měly xpass_completion < 0.65 (obtížné na provedení).
• **Taktika překonávání linií (Line Breaks)**:
    ◦ **Línie**: _first_line (překonání útočníků), _second_last_line (překonání zálohy), _last_line (překonání obrany).
    ◦ **Způsob**: _through_ (míč prošel skrz střed formace), _around_ (míč formaci obešel po straně).
• **count_option_through_... vs count_pass_attempts_through_...**: První metrika udává, kolikrát se hráč nabízel pro přihrávku přes linii. Druhá metrika udává, kolikrát hráč přes tuto linii skutečně zkusil přihrát.
• **count_pass_attempts_cross_receiver_runs...**: Přihrávky adresované hráči, který nabíhal do vápna na centr.
• **count_pass_attempts_runs_in_behind...**: Průnikové přihrávky za obrannou linii.
--------------------------------------------------------------------------------
6. POHYB BEZ MÍČE A NÁBĚHY (OFF-BALL RUNS)
*Náběh je pohyb bez míče trvající >0.7s, v rychlosti >15 km/h, hráč je k dispozici pro přihrávku.*
• **Typologie náběhů (count_..._runs)**:
    ◦ _cross_receiver_: Běh do vápna na centr.
    ◦ _in_behind_: Náběh za záda poslední obranné linie.
    ◦ _ahead_of_the_ball_: Běh ze zadní pozice dopředu, před úroveň míče.
    ◦ _overlap_: Náběh křídelním prostorem zvenku kolem hráče s míčem.
    ◦ _underlap_: Náběh vnitřkem hřiště (meziprostorem) kolem hráče s míčem.
    ◦ _support_: Podpůrný náběh směrem k držiteli míče z pozice za ním (dorovnání).
    ◦ _coming_short_: Náběh proti míči (od obrany k držiteli míče) pro přijetí krátké přihrávky.
    ◦ _pulling_wide_: Výběr do volného prostoru na křídle (roztažení hry).
    ◦ _pulling_half_space_: Náběh ze středu do meziprostoru.
    ◦ _dropping_off_: Stažení (odskočení) hráče hlouběji na vlastní polovinu pro otevření úhlu.
• **Sekvence Náběhu (Efektivita)**:
    ◦ count_runs...: Udělal náběh.
    ◦ ..._targeted...: Spoluhráč se mu pokusil přihrát.
    ◦ ..._received...: Skutečně míč přijal.
    ◦ ..._leading_to_shot / goal: Přijetí míče vedlo ke střele/gólu do 10 sekund.
• **Nebezpečnost (Focus on Dangerousness)**:
    ◦ Dangerous Run: Náběh, který měl xthreat > 0.02 (alespoň 2% šance na gól).
    ◦ Threat of runs...: Součet veškerého xThreat (očekávaných gólů), které hráč svými náběhy vytvořil. Hodnotí čistou kvalitu pohybu do volného prostoru i bez obdržení míče.
--------------------------------------------------------------------------------
7. CHOVÁNÍ POD TLAKEM A OBRANA (PRESSURE & ON-BALL ENGAGEMENTS)
*Tlak je situace, kdy se alespoň jeden soupeř nachází v blízkosti a snaží se získat nebo narušit držení míče.*
• **Pro útočníka na míči (Overcoming Pressure)**:
    ◦ count_pressures_received: Počet situací, kdy byl pod tlakem.
    ◦ count_ball_retentions: Udržení míče pod tlakem (driblink nebo úspěšná přihrávka).
    ◦ count_forced_losses: Vynucená ztráta míče pod tlakem.
    ◦ ball_retention_ratio: Procento úspěšného udržení míče.
• **Pro obránce bez míče (On-Ball Engagements / OBE)**:
    ◦ count_pressure_engagements: Samostatná individuální akce vyvinutí tlaku.
    ◦ count_pressing_engagements: Akce jako součást organizovaného řetězce více hráčů.
    ◦ count_counter_press...: Tlak aplikovaný ihned po ztrátě míče (do 3 vteřin).
    ◦ count_recovery_press...: Obranný návrat – tlak aplikovaný při sprintu směrem k vlastní bráně.
• **Obranné výsledky a úspěšnost (OBE Outcomes)**:
    ◦ direct_disruption_or_regain_percentage: Samotný obránce získal míč nebo přerušil akci.
    ◦ indirect_disruption_or_regain...: Tlak obránce pomohl k tomu, že míč získal spoluhráč.
    ◦ stop_or_reduce_danger_percentage: Obránce snížil pravděpodobnost skórování soupeře.
    ◦ force_backward_percentage: Obránce donutil soupeře nahrát zpět dozadu.
    ◦ got_goal_side / got_close: Obránce zavřel prostor nebo se úspěšně dostal mezi hráče s míčem a vlastní bránu.
    ◦ beaten_by_possession...: Útočník obránce obehrál na míči (např. kličkou).
    ◦ beaten_by_movement...: Soupeř naběhl obránci z mrtvého úhlu a přijal přihrávku.
    ◦ affected_line_break_percentage: Obránce svým zásahem zničil nebo snížil šanci soupeře k propíchnutí obranné linie.
--------------------------------------------------------------------------------
8. FÁZE HRY A TÝMOVÁ GEOMETRIE (PHASES OF PLAY & SHAPE)
*Události, pokud není míč mimo hru, probíhají v jedné z 8 definovaných fází (pro útočící i bránící tým).*
• **Fáze útoku / Obrany**:
    ◦ Build up / High Block: Výstavba z vlastní třetiny.
    ◦ Create / Medium Block: Tvorba ve střední třetině.
    ◦ Finish / Low Block: Dobývání zakončovací třetiny / ustálená obrana před vápnem.
    ◦ Transition: Rychlý protiútok zahájený ziskem na vlastní polovině.
    ◦ Quick Break: Rychlý protiútok zahájený ziskem na soupeřově polovině.
    ◦ Direct: Dlouhý nákop (nad 32 m dopředu) z vlastní poloviny s cílem udržet hru na hrotu.
    ◦ Set Play: Standardní situace směřující do pokutového území (max na 20 sec).
    ◦ Chaotic: Chaos, souboje, odkopy pod tlakem, odražené míče. Žádný tým neprovedl alespoň 3 přihrávky nebo nedržel míč více než 5 vteřin.
• **Přechody Fází (Phase Progression)**:
    ◦ Rozlišuje se, jak daná fáze končí (_leading_to_shot, _leading_to_goal, _leading_to_possession_loss, nebo _leading_to_\[dalsi_faze\]).
• **Geometrie Týmu (Team Shape)**:
    ◦ avg_team_width_...: Rozestoupení celého týmu do šířky (v konkrétní fázi).
    ◦ avg_team_length_...: Kompaktnost/délka týmu (vzdálenost mezi nejvyšším útočníkem a nejhlubším obráncem). Lze měřit na začátku a na konci fáze (_start a _end).
--------------------------------------------------------------------------------
9. ATRIBUTY SUROVÝCH DYNAMICKÝCH UDÁLOSTÍ (DYNAMIC EVENTS CSV - RAW DATA)
*Jednotlivé události (Pass, Run, Possession) v CSV nesou následující klíčové vlastnosti.*
• **Geometrie a Pozice**:
    ◦ Souřadnice: x_start, y_start, x_end, y_end v metrech. Střed hřiště = (0,0). Osa X je dlouhá strana, útok vždy směřuje zleva doprava.
    ◦ channel_...: Rozdělení hřiště do 5 vertikálních pruhů: wide_left, half_space_left, center, half_space_right, wide_right.
    ◦ third_...: Horizontální třetiny: defensive_third, middle_third, attacking_third.
• **Měření Času a Rychlosti**:
    ◦ duration: Trvání události ve vteřinách.
    ◦ speed_avg: Průměrná rychlost hráče v momentu události. Vyžaduje minimálně 5 snímků (frames). Rozdělena do pásem: jogging (<15 km/h), running (15-20), hsr (20-25), sprinting (>25).
• **Směr a postavení**:
    ◦ Forward / Backward / Sideway: Úhel pohybu ve vztahu k bráně.
    ◦ Ahead / Same line / Behind: Relativní lokace k míči/hráči (minimálně +/- 3 metry rozdíl osy X definuje, zda je hráč před míčem, nebo za ním).
• **Disrupce (Disruption)**:
    ◦ Special Case: Disruption: Pokud obránce míč jenom tečuje/vypíchne (bez získání držení) a získá jej zpět útok. Fáze hry se tímto momentem nemění, událost se značí jako *Disruption*.
Tato struktura zahrnuje naprosto všechny datové vrstvy od matematického mapování hřiště, přes strojové hodnocení rozhodnutí (xThreat) až po komplexní taktické metriky (fáze hry, line-breaking).

# AI UPRAVENÁ VERZE

**Účel a cíle:**
- Působit jako datový analytik specializovaný na fotbal a vývojář, který vytvoří robustní webovou aplikaci pro analýzu soupeře.
- Propojovat různé datové body (např. xG, držení míče, xThreat, úspěšnost přihrávek, fyzická data) do souvislého a logického příběhu o hře.
- Poskytovat výstupy v kontextu různých herních situací, taktických variant a možných scénářů.
**Základní zadání:** Vytvoř mi aplikaci, ve které si budu moci vygenerovat report o soupeři a jak proti němu hrát. Výchozí tým je vždy SK Sigma Olomouc (ID 536). Aplikace bude primárně sloužit pro trenérský štáb a analytiky k taktické přípravě.

## 1. Připojení dat a Bezpečnost
Zdroj dat: Kompletní knihovna SkillCorner’s Python SDK (dokumentace: <a href="https://skillcorner.readthedocs.io/en/latest/" rel="noopener" class="external-link" target="_blank"><u>https://skillcorner.readthedocs.io/en/latest/</u></a>).
**BEZPEČNOST A PŘIHLAŠOVÁNÍ:** Aplikace musí být maximálně bezpečná. Přihlašovací údaje k API SkillCorner a API klíč pro Gemini **NESMÍ** být v kódu "hardcoded". Vytvoř aplikaci tak, aby tyto údaje četla z lokálního souboru .env. Vytvoř v projektu šablonu .env.example s touto strukturou:
Fragment kódu


```
SKILLCORNER_USER=tomascerny2002@gmail.com
SKILLCORNER_PASS=tvoje_heslo
GEMINI_API_KEY=tvuj_api_klic
```
Použij všechny dostupné soutěže pro tento uživatelský účet: AUT - Bundesliga, BEL - Pro League, CZE First League, CZE - FNL, DEN - Superliga, ESP - LaLiga2, NOR - Eliteserien, POL - Ekstraklasa, SVK - Niké Liga, SVN - 1. SNL, SWE - Allsvenskan, UEFA - Europa Conference League, UEFA - Europa Conference League - Qualification, UEFA - Europa League - Qualification.

## 2. Architektura a Databázové řešení
Abychom nečekali dlouho na API odpověď a nezatěžovali limity API, navrhni **lokální databázovou vrstvu** (např. SQLite nebo Parquet soubory ovládané přes Pandas/DuckDB).
- Při spuštění/inicializaci systém stáhne data pro probíhající sezónu a uloží je lokálně pro tým SK Sigma Olomouc a jeho soupeře.
- Následně aplikace provádí jen **inkrementální updaty** (stahuje jen chybějící/nové zápasy z posledního období).

## 3. Datový model
Základním principem je volání API s parametrem group_by=match, což zajistí nejlepší granularitu dat (jeden řádek = jeden hráč v jednom zápase), která je klíčová pro sledování formy v čase a propojování s dalšími databázemi.
**A. Dimenze (Lookup Tables)** Slouží k filtrování dat (výběr hráče, týmu, pozice).
- Dim_Player: Získáno z /players. Obsahuje player_id, player_name, team_id, position_acronym.
- Dim_Position_Sort: Manuálně vytvořená pro řazení pozic (position_acronym, position_group, sort_order).
- Dim_Match / Dim_Competition: match_id, competition_edition_id, match_date, home_team_id, away_team_id.
- Dim_Team: team_id, team_name, team_shortname.
- **Dim_Game_State:** Dimenze pro filtrování stavu utkání (winning, drawing, losing), abychom mohli zkoumat reakce týmu na vývoj skóre.
**B. Datové tabulky (Fact Tables)**
- Fact_Physical_Data: Získáno z /physical (group_by=match). Kontext: minutes_played. Metriky: distance_per_90, sprint_distance_per_90, hi_count_per_90, avg_psv99, avg_top_3_time_to_sprint, cod_count_per_90.
- Fact_Game_Intelligence_In_Possession: Útočné metriky (normalizované na 30 min TIP). Příklad: count_possessions_per_30_tip, count_runs_in_behind_per_30_tip, count_dangerous_passes_per_30_tip, count_carries_at_speed_per_30_tip, count_forward_momentum_per_30_tip.
- Fact_Game_Intelligence_Out_of_Possession: Obranné metriky (normalizované na 30 min OTIP). Příklad: count_on_ball_engagements_per_30_otip, count_pressing_engagements_per_30_otip, direct_disruption_or_regain_percentage, stop_or_reduce_danger_percentage.
- Fact_Phases_of_Play: Struktura zápasu z CSV fází hry (Identifikátory fáze, kategorizace Build up / Block, události leading to shot/goal, time_start, duration, geometrie x_start, y_start, channel_start).
- Fact_Team_Metrics: Agregovaná týmová data v daném zápase (např. percentage_of_in_possession_time_in_build_up).
- **Fact_Positional_Data:** Surová data (Dynamic Events) obsahující průměrné X, Y souřadnice hráčů při držení míče, přihrávkách a nábězích. Tato data budou využita pro tvorbu map.
**C. Normalizace a Výpočty (Logika)**
- **Per 90:** (SUM(metric_value) / SUM(minutes_played)) * 90
- **Per 30 TIP/OTIP:** (SUM(metric_value) / SUM(minutes_in_possession)) * 30
- Pro hodnocení **stylu (DNA)** týmu používejte parametry _per_30_tip/otip a percentage_of...
- Pro hodnocení **absolutní hrozby** pro naši obranu používejte metriky _per_match.
- U rychlostí (PSV) nedělat normalizaci, použít prostý průměr AVERAGE(psv99). U časových sprintových údajů (time_to_sprint) se bere průměr ze 3 nejlepších pokusů.

## 4. Způsob práce s Gemini AI (LLM Optimalizace)
Aplikace **NESMÍ** posílat do Gemini celou syrovou databázi najednou, překročil by se limit tokenů a hrozí halucinace. Postup generování reportu bude následující:
1. **Python (Backend)** vyfiltruje data soupeře a Sigmy Olomouc, provede normalizace a spočítá klíčové odchylky, percentily a zjištění.
2. Backend vygeneruje strukturovaný JSON souhrn agregovaných dat a taktických zjištění pro daný zápas.
3. Tento **zkomprimovaný datový souhrn** spolu se specifickým systémovým promptem odešle přes API do modelu Gemini.
4. Gemini z tohoto souhrnu vygeneruje čtivý, fotbalově odborný a taktický textový report zasazený do kontextu, který se následně zobrazí v uživatelském rozhraní.

## 5. Struktura a Obsah Reportu
Aplikace musí mít základní filtry: Výběr soupeře, Soutěž, Období. Report musí zohledňovat naše silné/slabé stránky (Sigma) vs. silné/slabé stránky soupeře a hledat mezi nimi kontext.
**DŮLEŽITÁ INSTRUKCE PRO AI (GEMINI):** Níže uvedené popisy u jednotlivých sekcí slouží jako **hlavní vodítko a definice cíle**. AI model se však při analýze **nesmí omezit pouze na tyto explicitně vyjmenované metriky**. Pro každou sekci musí AI model proaktivně zvážit **veškerý dostupný datový kontext** (všechny relevantní taktické, fyzické i poziční metriky z dané fáze hry) a sám vyhodnotit, co je v daném kontextu nejvíce signifikantní a nebezpečné.
**Hlavní sekce reportu:**
1. **Základní charakteristika:** Komplexní shrnutí toho, jaký styl fotbalu hrají, v čem jsou typičtí a kdo jsou jejich klíčoví hráči. Zhodnoť jejich dominanci, tempo hry, typické rozestavení a celkovou geometrii týmu (kompaktnost, šířka atd.).
2. **Pasáže utkání a Game State:** Kdy je soupeř nejsilnější a kdy nejzranitelnější (podloženo daty). Zvažuj a detailně popiš, jak se mění jejich hra, taktika a datové výstupy v závislosti na vývoji skóre (když vedou, prohrávají nebo je remíza).
3. **Výstavba hry (Build-up):** Jak se soupeř typicky chová ve výstavbě hry. Kteří hráči jsou nejčastěji využívaní (dispečeři, překonávání linií), a kteří naopak dělají pod tlakem chyby. AI zde zváží všechny dostupné metriky k výstavbě, presinku soupeře i ztrátám míče. **Vizuál:** Graficky znázorni průměrné postavení v této fázi hry na základě analyzovaného období (striktně využij Python knihovnu mplsoccer).
4. **Způsob vedení útoku & Finální fáze:** Jak přecházejí do útoku a jak se chovají ve finální třetině. Jaké druhy náběhů nebo průniků používají, kudy nejčastěji vedou útoky a kdo je největší hrozbou (tvorba šancí, xThreat, finální přihrávky, náběhy za obranu). AI vyhodnotí komplexní ofenzivní data. **Vizuál:** Graficky znázorni průměrné postavení v této fázi a heatmapy vytížení hřiště (pomocí mplsoccer).
5. **Presink a hra v bloku:** Jak se chová soupeř při naší rozehrávce. Kde mají těžiště obrany (High/Medium/Low block time), kolik hráčů napadá a jak jsou agresivní po ztrátě míče. Detailně rozeber hru v jejich obranném bloku – jak jsou konzistentní, kudy vést útok, kdo propadá v duelech (např. překonání driblinkem/náběhem) a zda hrát spíše do nohy nebo za obranu.
6. **Chování ve vlastním pokutovém území:** Jsou silní ve vzduchu, po zemi, mají problémy s centry, nebo naopak s průniky? (Vyvozeno ze všech dostupných defenzivních metrik).
7. **Detailní profil hráčů soupeře:** Charakteristika vytížených a klíčových hráčů. U každého zhodnoť: Silné stránky (co u něj hrozí), Slabé stránky (čeho využít), jeho charakteristickou hru a fyzická specifika (např. extrémní maximální rychlost PSV-99 nebo agilita).
8. **Upozornění a doporučení (Taktická syntéza):** Co se na základě vzájemné analýzy zjistilo a stojí za to si říct. **Kritický bod:** AI zde musí dávat informace tvrdě do kontextu našich hráčů proti jejich. (Příklad: *„Soupeř má extrémně rychlého levého útočníka s obrovským objemem náběhů za obranu, zatímco náš pravý stoper má nízkou maximální rychlost. Doporučení: pravá strana naší obrany musí hrát v hlubším bloku a nelákat soupeře k náběhům.“*) Využívej pro hru maximálně přenositelné, věcné informace a vyvaruj se protichůdným tvrzením.

## 6. UI, Export a Další požadavky
- Report musí být možné vyexportovat do PDF v co nejlepší vizuální formě. Ideálně černý text na bílém pozadí se zvýrazněním nejdůležitějších informací. Bez zbytečných grafických prvků a bez zbytečností navíc.
- Dělej historii vygenerovaných reportů a uchovávej je, dávej ale možnost tyto reporty mazat.
- Dej možnost sdílet výsledný report přes odkaz - nemůže být možné po otevření odkazu dále editovat (Read-only).
- Tvoji finální aplikaci kompletně otestuj.
- Dej mi odkaz/instrukce, na kterém budu moct aplikaci používat.
## 7. Kompletní metodika a slovník metrik SkillCorner
*(Tento slovník si uchovej v extra logice, abys vždy věděl, co přesně jednotlivé metriky znamenají a jak s nimi metodicky pracovat pro účely výpočtů i pro účely generování reportu přes Gemini).*
**1. ZÁKLADNÍ PRINCIPY A NORMALIZACE** Všechny agregované metriky jsou normalizovány pro spravedlivé porovnání hráčů: • _per_90: Přepočet na 90 odehraných minut (typické pro fyzická data). • _per_30_tip (Team In Possession): Přepočet na 30 minut čistého času, kdy má tým míč. Odstraňuje zkreslení z dominance držení míče (typické pro ofenzivní metriky). • _per_30_otip (Opponent Team In Possession): Přepočet na 30 minut čistého času, kdy má míč soupeř (typické pro defenzivní metriky). • _per_100_events: Procentuální úspěšnost / konverzní poměr ze 100 definovaných událostí. • _percentage: Hodnota vyjádřená v procentech (úspěšné / celkové * 100).
**2. PREDIKTIVNÍ AI MODELY (JÁDRO HODNOCENÍ)** Tyto proměnné přidávají událostem kontext pravděpodobnosti a nebezpečnosti: • xthreat (Expected Threat): Pravděpodobnost (0 až 1), že tým vstřelí gól do 10 sekund, pokud by hráč v daný moment přijal přihrávku. • xpass_completion: Pravděpodobnost (0 až 1), že konkrétní přihrávka bude úspěšně zkompletována. Pokud je xPass < 0,65 (65 %), je přihrávka definována jako difficult (obtížná). • passing_option_score: Skóre z Receiver Modelu, které určuje pravděpodobnost, že se hráč stane adresátem přihrávky. Hráč je považován za „Passing Option“, pokud je toto skóre > 0,6. • peak_passing_option_frame: Teoretický moment pro výpočet výše zmíněných metrik u hráče, který nedostal míč. Je to okamžik (snímkování), který maximalizuje rovnici: passing_option_score * xthreat * xpass_completion.
**3. FYZICKÉ METRIKY (PHYSICAL METRICS)** Definují pohybové schopnosti, intenzitu a agilitu hráče a týmu. • distance_per_90: Celková uběhnutá vzdálenost. • running_distance_per_90: Vzdálenost uběhnutá rychlostí 15–20 km/h. • hi_distance_per_90 / hi_count (High-Intensity): Vzdálenost a počet náběhů nad 20 km/h (součet HSR + Sprintů). • hsr_distance_per_90 / hsr_count (High Speed Running): Vzdálenost a počet úseků v rychlosti 20–25 km/h. • sprint_distance_per_90 / sprint_count: Vzdálenost a počet úseků nad 25 km/h. • avg_psv99 / avg_top_5_psv99 (Peak Sprint Velocity): 99. percentil maximální rychlosti hráče (nebo průměr 5 nejlepších), eliminuje chyby měření. • explacceltohsr_count_per_90 / explacceltosprint_...: Počet explozivních akcelerací (vysoké zrychlení z <9 km/h na >20 km/h resp. >25 km/h). • avg_top_3_time_to_hsr / ..._to_sprint: Průměr ze 3 nejrychlejších časů potřebných k dosažení cílové rychlosti z klidu. Ukazuje absolutní výbušnost. • cod_count_per_90 (Change of Direction): Počet intenzivních změn směru. • ..._post_cod: Výbušnost po změně směru (jak rychle hráč dosáhne HSR/Sprintu ihned po COD). • time_to_505_around_90 / ...*180: Čas agility testu na hřišti (uběhnutí 5m před a 5m po otočce o 90° nebo 180°). • player_av*...: Tyto metriky existují i jako průměr pro všechny hráče v týmu (např. průměrná uběhnutá vzdálenost na hráče v týmu).
**4. METRIKY S MÍČEM A TVORBA HRY (IN POSSESSION - ON BALL)** Hodnotí hráče v kontrole míče (Player Possession). • count_possessions_...: Počet situací, kdy má hráč míč plně pod kontrolou (jedno-doteky se počítají, odrazy a bloky ne). Lze filtrovat dle fází hry (..._in_build_up, ..._in_create, ..._in_finish, ..._in_transition). • count_receptions_in_tight_space...: Přijetí míče v úzkém prostoru (obránce byl blíže než 2 metry). • count_carries_at_speed...: Držení míče/driblink delší než 8 metrů vedený rychlostí minimálně 15 km/h (running speed). • count_forward_momentum...: Progresivní výsledek okamžitě z prvního doteku (hráč dokázal při přijetí zrychlit nebo se otočit čelem vpřed, a to ve středním pruhu / half-space, když byl pod tlakem do 6 metrů). • count_quick_passes...: Přihrávky na jeden nebo dva rychlé doteky.
**5. PŘEKONÁVÁNÍ OBRANY A PŘIHRÁVKY (PASSING & LINE BREAKING)** Hodnocení schopnosti tvořit hru a propichovat formaci soupeře. • count_dangerous_passes...: Počet přihrávek, které měly xthreat > 0.02 (vysoká šance na gól). • count_difficult_passes...: Počet přihrávek, které měly xpass_completion < 0.65 (obtížné na provedení). • Taktika překonávání linií (Line Breaks): ◦ Línie: _first_line (překonání útočníků), *second_last_line (překonání zálohy), last_line (překonání obrany). ◦ Způsob: through (míč prošel skrz střed formace), around (míč formaci obešel po straně). • count_option_through... vs count_pass_attempts_through*...: První metrika udává, kolikrát se hráč nabízel pro přihrávku přes linii. Druhá metrika udává, kolikrát hráč přes tuto linii skutečně zkusil přihrát. • count_pass_attempts_cross_receiver_runs...: Přihrávky adresované hráči, který nabíhal do vápna na centr. • count_pass_attempts_runs_in_behind...: Průnikové přihrávky za obrannou linii.
**6. POHYB BEZ MÍČE A NÁBĚHY (OFF-BALL RUNS)** Náběh je pohyb bez míče trvající >0.7s, v rychlosti >15 km/h, hráč je k dispozici pro přihrávku. • Typologie náběhů (count_..._runs): ◦ *cross_receiver*: Běh do vápna na centr. ◦ *in_behind*: Náběh za záda poslední obranné linie. ◦ *ahead_of_the_ball*: Běh ze zadní pozice dopředu, před úroveň míče. ◦ *overlap*: Náběh křídelním prostorem zvenku kolem hráče s míčem. ◦ *underlap*: Náběh vnitřkem hřiště (meziprostorem) kolem hráče s míčem. ◦ *support*: Podpůrný náběh směrem k držiteli míče z pozice za ním (dorovnání). ◦ *coming_short*: Náběh proti míči (od obrany k držiteli míče) pro přijetí krátké přihrávky. ◦ *pulling_wide*: Výběr do volného prostoru na křídle (roztažení hry). ◦ *pulling_half_space*: Náběh ze středu do meziprostoru. ◦ *dropping_off*: Stažení (odskočení) hráče hlouběji na vlastní polovinu pro otevření úhlu. • Sekvence Náběhu (Efektivita): ◦ count_runs...: Udělal náběh. ◦ ..._targeted...: Spoluhráč se mu pokusil přihrát. ◦ ..._received...: Skutečně míč přijal. ◦ ..._leading_to_shot / goal: Přijetí míče vedlo ke střele/gólu do 10 sekund. • Nebezpečnost (Focus on Dangerousness): ◦ Dangerous Run: Náběh, který měl xthreat > 0.02 (alespoň 2% šance na gól). ◦ Threat of runs...: Součet veškerého xThreat (očekávaných gólů), které hráč svými náběhy vytvořil. Hodnotí čistou kvalitu pohybu do volného prostoru i bez obdržení míče.
**7. CHOVÁNÍ POD TLAKEM A OBRANA (PRESSURE & ON-BALL ENGAGEMENTS)** Tlak je situace, kdy se alespoň jeden soupeř nachází v blízkosti a snaží se získat nebo narušit držení míče. • Pro útočníka na míči (Overcoming Pressure): ◦ count_pressures_received: Počet situací, kdy byl pod tlakem. ◦ count_ball_retentions: Udržení míče pod tlakem (driblink nebo úspěšná přihrávka). ◦ count_forced_losses: Vynucená ztráta míče pod tlakem. ◦ ball_retention_ratio: Procento úspěšného udržení míče. • Pro obránce bez míče (On-Ball Engagements / OBE): ◦ count_pressure_engagements: Samostatná individuální akce vyvinutí tlaku. ◦ count_pressing_engagements: Akce jako součást organizovaného řetězce více hráčů. ◦ count_counter_press...: Tlak aplikovaný ihned po ztrátě míče (do 3 vteřin). ◦ count_recovery_press...: Obranný návrat – tlak aplikovaný při sprintu směrem k vlastní bráně. • Obranné výsledky a úspěšnost (OBE Outcomes): ◦ direct_disruption_or_regain_percentage: Samotný obránce získal míč nebo přerušil akci. ◦ indirect_disruption_or_regain...: Tlak obránce pomohl k tomu, že míč získal spoluhráč. ◦ stop_or_reduce_danger_percentage: Obránce snížil pravděpodobnost skórování soupeře. ◦ force_backward_percentage: Obránce donutil soupeře nahrát zpět dozadu. ◦ got_goal_side / got_close: Obránce zavřel prostor nebo se úspěšně dostal mezi hráče s míčem a vlastní bránu. ◦ beaten_by_possession...: Útočník obránce obehrál na míči (např. kličkou). ◦ beaten_by_movement...: Soupeř naběhl obránci z mrtvého úhlu a přijal přihrávku. ◦ affected_line_break_percentage: Obránce svým zásahem zničil nebo snížil šanci soupeře k propíchnutí obranné linie.
**8. FÁZE HRY A TÝMOVÁ GEOMETRIE (PHASES OF PLAY & SHAPE)** Události, pokud není míč mimo hru, probíhají v jedné z 8 definovaných fází (pro útočící i bránící tým). • Fáze útoku / Obrany: ◦ Build up / High Block: Výstavba z vlastní třetiny. ◦ Create / Medium Block: Tvorba ve střední třetině. ◦ Finish / Low Block: Dobývání zakončovací třetiny / ustálená obrana před vápnem. ◦ Transition: Rychlý protiútok zahájený ziskem na vlastní polovině. ◦ Quick Break: Rychlý protiútok zahájený ziskem na soupeřově polovině. ◦ Direct: Dlouhý nákop (nad 32 m dopředu) z vlastní poloviny s cílem udržet hru na hrotu. ◦ Set Play: Standardní situace směřující do pokutového území (max na 20 sec). ◦ Chaotic: Chaos, souboje, odkopy pod tlakem, odražené míče. Žádný tým neprovedl alespoň 3 přihrávky nebo nedržel míč více než 5 vteřin. • Přechody Fází (Phase Progression): ◦ Rozlišuje se, jak daná fáze končí (_leading_to_shot, *leading_to_goal, leading_to_possession_loss, nebo leading_to\[dalsi_faze\]). • Geometrie Týmu (Team Shape): ◦ avg_team_width...: Rozestoupení celého týmu do šířky (v konkrétní fázi). ◦ avg_team_length*...: Kompaktnost/délka týmu (vzdálenost mezi nejvyšším útočníkem a nejhlubším obráncem). Lze měřit na začátku a na konci fáze (_start a _end).
**9. ATRIBUTY SUROVÝCH DYNAMICKÝCH UDÁLOSTÍ (DYNAMIC EVENTS CSV - RAW DATA)** Jednotlivé události (Pass, Run, Possession) v CSV nesou následující klíčové vlastnosti. • Geometrie a Pozice: ◦ Souřadnice: x_start, y_start, x_end, y_end v metrech. Střed hřiště = (0,0). Osa X je dlouhá strana, útok vždy směřuje zleva doprava. ◦ channel_...: Rozdělení hřiště do 5 vertikálních pruhů: wide_left, half_space_left, center, half_space_right, wide_right. ◦ third_...: Horizontální třetiny: defensive_third, middle_third, attacking_third. • Měření Času a Rychlosti: ◦ duration: Trvání události ve vteřinách. ◦ speed_avg: Průměrná rychlost hráče v momentu události. Vyžaduje minimálně 5 snímků (frames). Rozdělena do pásem: jogging (<15 km/h), running (15-20), hsr (20-25), sprinting (>25). • Směr a postavení: ◦ Forward / Backward / Sideway: Úhel pohybu ve vztahu k bráně. ◦ Ahead / Same line / Behind: Relativní lokace k míči/hráči (minimálně +/- 3 metry rozdíl osy X definuje, zda je hráč před míčem, nebo za ním). • Disrupce (Disruption): ◦ Special Case: Disruption: Pokud obránce míč jenom tečuje/vypíchne (bez získání držení) a získá jej zpět útok. Fáze hry se tímto momentem nemění, událost se značí jako Disruption.

# Aktualizace 2.3. 2026

Chci změnit koncept a zdroj data. Pro svoji analýzu potřebuji vytvořit databázy, do které nejdříve předpřipravím data vybraných týmů. 
1) Nejdříve si vyberu jakou sezónu chci řešit Nyní je to od 1.7. 2025 do 30.6.2026 sezóna 2025/2026 - a vždy bude defaultně nastavená aktuální sezóna s možností změnit 
2) Defaultně bude vybraná  SK Sigma Olomouc jakou tým, pro který se analýza připravuje ve všech soutěžích, ve kterých Sigma Olomouc hraje.  
2) Pak chci mít možnost v rozbalovacím seznamu vybrat soupeře - v nabídce musí být pouze týmy, ke kterým je prostřednictvím API klíče přístup k aktuálním datům. Další nabídka musí být soutěže, které soupeře hraje a mít možnost vícenásobného výběru. Jako poslední bude omezení na časové období, ze kterého budeou data čerpána. 
3) Pak by měla být možnost dát generovat data a v tu chvíli se mi v databázi vytvoří data, ze kterých až následně bude AI tvořit analýzu. Data pro SK Sigma Olomouc by měla zůstat v databázi stále zpracována a pouze se aktualizovat. Vždy musí u SK Sigma Olomouc svítit z jakého dne jsou data akutální. Poté, co budou aktuální data vygenerována a zpracována jak pro SK Sigma Olomouc, tak pro vybraného soupeře, tak musí svítit ikona, že jsou data aktuální a připravená k analýze. 
4) Zásadní změna ale je to, že data musíme používat hlavně z Dynamic event dat 
a) tato data je potřeba nejdříve agregovat. Vše budeme agregovat podle utkání ne na 90 minut, ale přesně podle MatchID, aby data odpovídala každému utkání, ale je důležité, abychom měli správně postavenou strukturu a propojení dat navzájem. Chci mít zvlášť data pro jednotlivé hráče, a následně data tým jako celek. Důležitá jsou pak samostatná polohová data pro jednotlivé hráče, abychom mohli vykreslit jejich průměrné postavení v jednotlivých fázích hry. U polohových dat je zásadní zohlednit také o jaký se jedná poločas a jaký je směr hry, aby byla poloha vždy správně zaznamenána. 
b) Data musí být rozdělená do logických struktur - tuto strukturu je potřeba excelentně načíst z dokumentace API SkillCorner, aby databáze byla postavená opravdu precizně a analýza pak čerpala z precizně připravených dat. Zásadní je, aby byla jasně zřetelná data o jakého hráče se jedná z jakého je týmu, byla do detailu zpracovaná data off_ball_runns, on_ball_engagements, passing_options, phase_of_play, player_possessions, on_ball_pressures, passes, out_of_possession, physical data a to se všemi svými detaily a typy akcí
1. V leví části obrazovky bude nabídka ve které budou řazené týmy, pro které jsou v databázi vytvořená data s aktuálním datumem, ke kterému jsou data aktuální. Na prvním místě bude vždy SK Sigma Olomouc a následně pod ní budou řazené další týmy, pro které se data generovala a zpracovávala. Musím mít možnost se do zdrojových dat podívat jako do tabulky. Musím mít možnost data kdykoli smazat nebo aktualizovat k aktuálnímu datu. 
2. V levé. Nabídce chci mít možnost nahrát ještě data pro tým po jednotlivých utkáních a pro jednotlivé hráče ve formátu xlsx, která pomůžou k dokreslení kontextu a budou doplňovat data získaná přes API. Nicméně v databázi budou mít svojí vlastní tabulku. 
3. Ještě potřebuji jednu možnost, pokud nemám přístup v API k nějakému týmu, tak potřebuji mít možnost tým přidat a nahrát jeho dynamic event data v CSV. 

Až poté, co budou data správně připravená, agregovaná, očištěná, doplněná o další kontextová data, tak až poté bude AI provádět analýzu na základě pravidel, která jsem si doposud nastavili. 


# Doplnění zdrojů
Dej mi několi možností 1) Data SK Sigma Olomouc dej na úvodní stránce na nejvyšší možné místo a přidej mi tlačítko aktualizovat data, díky kterému získám přístup k nejnovějším datům. 2) Dále mi dej možnost ještě nahrát další CSV, ve kterém budou doplňující SkillCorner hráčská data, která je nutné vzít do kontextu. bude se jednat o absolutní hodnoty za každé utkání. V těchto dokumentech je možné data párovat přes Match ID. Zanech také možnost nahrát soubor hráčských i týmových dat xlsx. 



# Manuální data - 06.03.2025
**Účel a cíle:**
- Působit jako datový analytik specializovaný na fotbal a vývojář, který vytvoří robustní webovou aplikaci pro analýzu soupeře.
- Tvůj úkol je z dostupných dat udělat kvalitní analýzu, ze které bude dostatek informací pro vytvoření herního plánu, jak překonat soupeře a na jaká nebezpečí si dát pozor. 

**Základní zadání:** 
Vytvoř mi aplikaci, ve které si budu moci vygenerovat report o soupeři a jak proti němu hrát. Výchozí tým je vždy SK Sigma Olomouc (ID 536). Aplikace bude primárně sloužit pro trenérský štáb a analytiky k taktické přípravě. Důležité je, aby si jako výchozí tým bral Sigmu Olomouc. Porovnej data Sigmy Olomouc a soupeře a snaž se najít to, kde se protnou - jak soupeře ohrozit a naopak kde by nás soupeř mohl ohrozit právě na základě porovnání dat. 

**Datové zdroje:** 
Jako zdroj dat bude sloužit 9 souborů k jednomu týmu, které ti vždy poskytnu skrze odkaz na složku na Google disku. Jeden odkaz bude vždy na Sigmu Olomouc a druhý bude na konkrétního soupeře. Odkaz musí být editovatelny.. Níže ti posílám popis toho, jak jednotlivé soubory vypadají v jakém jsou souboru a krátké informace co v nich najdeš a jak je propojíš s ostatními. Vždy je nejdříve název souboru, poté následuje podržíte a název týmu, kterému data patří. 

- **Player Possessions (Držení míče hráčem) Formát: Google tabulka:** Tato sekce se zaměřuje na individuální akce hráče ve chvíli, kdy má míč pod kontrolou. Obsahuje statistiky o přijetí míče (včetně přijetí pod intenzivním tlakem nebo v úzkém prostoru), vyvezení míče na delší vzdálenost (tzv. carries), schopnosti vymanit se z tlaku (escaped pressure) a o tom, zda dokázal překonat obránce a vytvořit posun hry vpřed (forward momentum).
- **Physical (Fyzické metriky) Formát: Google tabulka:** Obsahuje čistě atletická data o pohybu hráče. Najdete zde uběhnuté vzdálenosti, počty náběhů ve vysoké intenzitě (HSR) a ve sprintu, ale také pokročilé údaje jako je maximální dosažená rychlost, explozivní akcelerace a schopnost rychle měnit směr.
- **Passing Options (Možnosti přihrávky) Formát: Google tabulka:** Vyhodnocuje momenty, kdy hráč zrovna nemá míč, ale **nabízí se jako volba pro přihrávajícího spoluhráče**. Sleduje, kolikrát hráč takovou možnost vytvořil, zda nabízel možnost překonat obrannou linii, zda operoval uvnitř či vně obranného bloku soupeře, kolikrát mu byla přihrávka skutečně určena (targeted) a kolikrát míč dostal (received).
- **Passes (Přihrávky) Formát: Google tabulka:** Mapuje distribuci míče a kreativitu **přihrávajícího hráče**. Hodnotí, kolik přihrávek hráč zkusil a zkompletoval, jaká byla jejich očekávaná úspěšnost (xPass), a zda šlo o přihrávky propichující obranné linie soupeře (Line-Breaking). Patří sem i hodnocení obtížných (difficult) a nebezpečných (dangerous) přihrávek a přihrávek směřujících přesně na hráče v náběhu.
- **On Ball Engagements (Obranné akce vůči hráči s míčem) Formát: Google tabulka:** Tato tabulka detailně popisuje defenzivní chování hráče, když má míč soupeř. Klasifikuje různé druhy tlaku na míč (individuální tlak, organizovaný presink, okamžitý represink, návratový presink). Dále hodnotí výsledky tohoto tlaku – například zda obránce míč získal (regain), donutil soupeře hrát dozadu (force backward), narušil akci (disruption), nebo zda naopak propadl a soupeř ho překonal driblinkem či pohybem.
- **Off Ball Runs (Náběhy bez míče) Formát: Google tabulka:** Sleduje aktivní a rychlý pohyb hráčů útočícího týmu, kteří právě nemají míč. Náběhy detailně člení do specifických typologických kategorií, jako jsou náběhy za obranu (in behind), na centr (cross receiver), seběhnutí nakrátko (coming short) nebo obíhání (overlap a underlap). Kromě absolutních počtů hodnotí, zda byly náběhy nebezpečné (Dangerous runs) a kolik očekávané hrozby (Avg Threat / xThreat) konkrétní pohyb vygeneroval.
- **Player stats (Hráčská data) Formát: Google tabulka**: Všeobecná herní data za jednotlivá utkání. 
- **Team Stats (Týmová data) Formát: Google tabulka**: Všeobecná souhrnná dat týmu v jednotlivých utkání
- **In Possession Summary (Data týmu v držení míče)**: PDF report specifikující chování týmy v čase, kdy drží míč po jednotlivých utkáních. Zásadní jsou grafická znázornění s postavením ve výstavbě hry, tvorbě hry a ve finální fázi, ze kterých chci udělat jedno průměrné postavení ze všech analyzovaných utkání. Stejně tak chci vidět jejich průměrnou šířku a hloubku v útočné hře. 
- **Out of Possession (Data týmu ve hře bez míče):** PDF report specifikující chování týmy v čase, kdy nedrží míč. Z grafického zobrazení určí z průměrných hodnot analyzovaných utkání, kde je soupeř nejúspěšnější v získávání míčů a kde má naopak slabiny a kudy je na základě tohoto poznatku nejvýhodnější vést útok. 

Párování dat: 
- Match ID - v každém souboru najdeš ID pro konrkétní utkání
- Player ID - v každém hráčském souboru najdeš ID konkrétního sportovce
- Team ID - v každém souboru najdeš také ID týmu, který analyzujeme
- Všechna data propojuj právě těmito ID. U týmových dat je pouze Match ID a Team ID, ale u hráčských statistik najdeš navíc ještě Player ID, aby si pároval správného hráče
- V PDF reportu je důležité, aby si respektoval název týmy a pročítal data

Níže zasílám přesný popis jednotlivých metrik z datasetů. Vytvoř si smostatny soubor, ze kterého budeš vždy při analýze čerpat znalosti.

Off Ball Runs
- **Competition Edition ID** (competition_edition_id): Unikátní identifikátor konkrétního ročníku soutěže (např. Premier League 2023/2024).
- **Competition ID** (competition_id): Obecný identifikátor soutěže (např. Premier League napříč všemi ročníky).
- **Competition** (competition_name): Textový název soutěže.
- **Season ID** (season_id): Identifikátor konkrétní sezóny.
- **Season** (season_name): Textový název sezóny (např. "2023/2024").
- **Match ID** (match_id): Unikátní identifikátor konkrétního zápasu.
- **Match** (match_name): Názvy týmů v zápase (např. "Arsenal vs Chelsea").
- **Date** (match_date): Datum odehrání zápasu.
- **Player ID** (player_id): Unikátní identifikátor hráče.
- **Player** (player_name): Celé jméno hráče.
- **Short Name** (player_short_name): Zkrácené jméno hráče pro vizualizace.
- **Birthdate** (player_birthdate): Datum narození hráče.
- **Team ID** (team_id): Unikátní identifikátor týmu, za který hráč nastoupil.
- **Team** (team_name): Celý název týmu.
- **Position** (position): Konkrétní zkratka pozice hráče v daném zápase (např. CB, CM, CF).
- **Position Group** (position_group): Obecnější kategorie pozice (např. Defenders, Midfielders, Forwards).
## 2. HERNÍ ČAS A KVALITA DAT (Základ pro normalizaci)
- **Minutes** (minutes): Celkový počet odehraných minut hráče v utkání.
- **Minutes (Tip)** (minutes_tip): Čistý čas (v minutách), po který měl **tým hráče míč v držení** (Team In Possession). Zásadní pro přepočet ofenzivních metrik.
- **Minutes (Otip)** (minutes_otip): Čistý čas (v minutách), po který měl **míč v držení soupeř** (Opponent Team In Possession). Zásadní pro přepočet defenzivních metrik.
- **GI Check Passed** (gi_check_passed): Logická hodnota (TRUE/FALSE) udávající, zda kvalita trackingu v tomto zápase byla dostatečně vysoká pro generování pokročilých metrik "Game Intelligence". Pokud je FALSE, data by se neměla pro hlubší analýzu používat.
## 3. METRIKY NÁBĚHŮ BEZ MÍČE (Off-Ball Runs)
*Náběh je definován jako úmyslný pohyb hráče bez míče rychlostí nad 15 km/h po dobu delší než 0,7 sekundy, kdy se hráč nabízí pro přihrávku.*
- **Runs Total** (offballrun_count_total): Celkový absolutní počet všech zaznamenaných náběhů hráče.
- **Runs** (offballrun_count): Počet platných náběhů vyhodnocených systémem jako útočná nabídka.
- **Runs Leading To Shot** (offballrun_count_shotwithin10s): Náběhy, u kterých tým dokázal do 10 sekund od jejich realizace (a případného obdržení míče) vyprodukovat střelu.
- **Runs Leading To Goal** (offballrun_count_goalwithin10s): Náběhy, u kterých tým dokázal do 10 sekund vstřelit gól.
- **Runs Targeted** (offballrun_count_targeted): Náběhy, u kterých se hráč stal adresátem přihrávky (spoluhráč s míčem se na něj pokusil přihrát, bez ohledu na to, zda přihrávka prošla).
- **Runs Received** (offballrun_count_received): Náběhy zakončené tím, že hráč úspěšně přijal míč a dostal jej pod svou kontrolu.
- **Runs Avg Distance** (offballrun_avgdistance): Průměrná vzdálenost (v metrech), kterou hráč urazí během jednoho náběhu.
- **Runs (Above HSR)** (offballrun_count_abovehsr): Náběhy provedené ve vysoké intenzitě (High Speed Running). Tedy takové, kdy hráč při náběhu překročil rychlost **20 km/h**.
- **Runs (Penalty Area)** (offballrun_count_penaltyarea): Náběhy bez míče, které směřovaly přímo do pokutového území (vápna) soupeře.
- **Runs (Dangerous)** (offballrun_count_dangerous): Počet "Nebezpečných náběhů". AI model hodnotí náběh jako nebezpečný, pokud se jím hráč dostal do pozice, kde je pravděpodobnost vstřelení gólu (Expected Threat / xThreat) **vyšší než 2 % (0.02)**. Odfiltrovává alibistické běhání.
- **Runs Targeted (Dangerous)** (offballrun_count_dangerous_targeted): Počet *nebezpečných náběhů* (xThreat > 0.02), kterých si spoluhráč všiml a zkusil na ně míč přihrát.
- **Runs Received (Dangerous)** (offballrun_count_dangerous_received): Počet nejcennějších náběhů v ofenzivě: Hráč udělal nebezpečný náběh, spoluhráč mu přihrál a hráč míč **úspěšně dostal pod kontrolu**. Tvoří přímou hrozbu pro branku soupeře.

On Ball Engagements
- **Competition Edition ID** (competition_edition_id): Unikátní identifikátor konkrétního ročníku soutěže.
- **Competition ID** (competition_id): Obecný identifikátor soutěže (např. Premier League).
- **Competition** (competition_name): Textový název soutěže.
- **Season ID** (season_id): Identifikátor konkrétní sezóny.
- **Season** (season_name): Textový název sezóny.
- **Match ID** (match_id): Unikátní identifikátor zápasu.
- **Match** (match_name): Názvy týmů v zápase.
- **Date** (match_date): Datum zápasu.
- **Player ID** (player_id): Unikátní identifikátor hráče.
- **Player** (player_name): Celé jméno hráče.
- **Short Name** (player_short_name): Zkrácené jméno hráče pro grafiky.
- **Birthdate** (player_birthdate): Datum narození hráče.
- **Team ID** (team_id): Unikátní identifikátor týmu.
- **Team** (team_name): Název týmu.
- **Position** (position): Konkrétní zkratka pozice hráče (např. CB).
- **Position Group** (position_group): Skupina pozic (např. Defenders).
- **Minutes** (minutes): Celkový počet odehraných minut hráče.
- **Minutes (Tip)** (minutes_tip): Čistý čas, po který měl tým hráče míč v držení (Team In Possession).
- **Minutes (Otip)** (minutes_otip): Čistý čas, po který měl míč v držení soupeř (Opponent Team In Possession). Klíčové pro přepočet obranných metrik.
- **GI Check Passed** (gi_check_passed): Indikátor (TRUE/FALSE) kvality trackingu pro generování pokročilých metrik.
## 2. ZÁKLADNÍ OBRANNÉ AKCE (On-Ball Engagements)
*On-Ball Engagement (OBE) je situace, kdy obránce aktivně vyvíjí tlak na hráče s míčem nebo s ním vstupuje do souboje.*
- **Engagements Total** / **Engagements** (onballengagement_count): Celkový počet obranných akcí a zapojení vůči hráči s míčem.
- **Engagements (Above HSR)** (onballengagement_count_abovehsr): Počet obranných akcí na míči, které hráč provedl ve vysoké rychlosti (nad 20 km/h).
- **Engagements (Pressing Chain)** (onballengagement_count_pressingchain): Počet obranných akcí, které byly součástí organizovaného týmového presinku (řetězce tlaků).
- **Engagements (Consecutive)** (onballengagement_count_consecutive): Počet navazujících (opakovaných) obranných tlaků bezprostředně po sobě.
- **Engagements (Forward Trajectory)** (onballengagement_count_forwardtrajectory): Počet obranných akcí, při kterých se obránce aktivně posouval směrem vpřed proti soupeři.
## 3. VÝSLEDKY TLAKU A ZISK MÍČE (Defensive Outcomes)
*Hodnotí, nakolik byla obranná akce úspěšná a k čemu přesně vedla.*
- **Engagements Regain** (onballengagement_count_directregain): Počet akcí, které vedly k **přímému zisku míče** samotným obráncem.
- **Engagements Regain Pct** (onballengagement_pct_directregain): Procentuální úspěšnost přímého zisku míče z celkového počtu obranných akcí.
- **Engagements Indirect Regain** (onballengagement_count_indirectregain): Počet akcí vedoucích k **nepřímému zisku**. Tlak obránce donutil soupeře k chybě, ale míč fyzicky získal jiný spoluhráč.
- **Engagements Indirect Regain Pct** (onballengagement_pct_indirectregain): Procentuální poměr nepřímých zisků míče.
- **Engagements Disruption** (onballengagement_count_directdisruption): Počet akcí, při kterých obránce přímo **narušil** nebo přerušil akci soupeře (např. odkop do autu, zblokování), aniž by tým získal míč pod kontrolu.
- **Engagements Disruption Pct** (onballengagement_pct_directdisruption): Procento obranných akcí končících přímým narušením.
- **Engagements Indirect Disruption** (onballengagement_count_indirectdisruption): Počet akcí, kdy tlak hráče nepřímo způsobil narušení akce jiným hráčem.
- **Engagements Indirect Disruption Pct** (onballengagement_pct_indirectdisruption): Procento obranných akcí končících nepřímým narušením.
- **Engagements Forced Backward** (onballengagement_count_forcedbackward): Počet akcí, při kterých obránce donutil soupeře přihrát nebo se pohnout zpět směrem od vlastní branky.
- **Engagements Forced Backward Pct** (onballengagement_pct_forcedbackward): Procento akcí, které úspěšně vytlačily soupeře dozadu.
## 4. ZABRÁNĚNÍ NEBEZPEČÍ A ZACHYCENÍ PŘIHRÁVKY
- **Engagements Line Break Affected** (onballengagement_count_linebreakaffected): Počet obranných akcí, kterými hráč přímo ztížil, ovlivnil nebo překazil soupeřovu snahu o překonání obranné linie.
- **Engagements Line Break Affected Pct** (onballengagement_pct_linebreakaffected): Procento akcí ovlivňujících průnikové přihrávky.
- **Engagements (Dangerous Situation)** (onballengagement_count_dangeroussituation): Počet obranných akcí, které hráč musel řešit v objektivně nebezpečné situaci pro vlastní branku.
- **Engagements Danger Mitigated (Dangerous Situation)** (onballengagement_count_dangeroussituation_dangermitigated): Počet nebezpečných situací, ve kterých hráč svým obranným zákrokem úspěšně snížil nebo zcela zastavil gólovou hrozbu.
- **Engagements Danger Mitigated Pct** (onballengagement_pct_dangermitigated): Celkové procento všech obranných akcí, při kterých hráč snížil hrozbu (xThreat) soupeře.
## 5. PROPADNUTÍ A CHYBY V OBRANĚ (Defensive Flaws)
*Tyto metriky měří prohrané obranné duely a slabiny obránce.*
- **Engagements (Beaten By Possession)** (onballengagement_count_beatenbypossession): Počet akcí, při kterých byl obránce úspěšně překonán soupeřem s míčem u nohy (např. obehrán úspěšným driblinkem 1v1).
- **Engagements (Beaten By Possession) Pct** (onballengagement_pct_beatenbypossession): Procento případů, kdy byl obránce překonán hráčem na míči.
- **Engagements (Beaten By Movement)** (onballengagement_count_beatenbymovement): Počet akcí, při kterých byl obránce překonán soupeřem bez míče (např. zaspal náběh a soupeř za jeho zády úspěšně přijal přihrávku).
- **Engagements (Beaten By Movement) Pct** (onballengagement_pct_beatenbymovement): Procento obranných situací, ve kterých obránce propadl po náběhu soupeře.

Passes
## 1. ZÁKLADNÍ METADATA A HERNÍ ČAS
*Slouží pro kontext a normalizaci dat.*
- **Competition Edition ID** až **Position Group**: Standardní identifikátory zápasu, ligy, týmu a hráče.
- **Minutes**: Celkový počet odehraných minut.
- **Minutes (Tip)** (minutes_tip): Minuty čistého času, kdy měl tým míč v držení. **Zásadní parametr pro normalizaci všech útočných (passing) metrik (per 30 TIP).**
- **Minutes (Otip)**: Minuty čistého času bez míče.
- **GI Check Passed**: Indikátor (TRUE/FALSE) dostatečné kvality trackingu pro výpočet Game Intelligence.
## 2. ZÁKLADNÍ PŘIHRÁVKY A KVALITA (Basic Passing)
- **Pass Opportunities Total / Pass Opportunities** (passopportunity_count): Počet situací, kdy měl hráč s míčem k dispozici reálnou možnost komukoliv přihrát (spoluhráč se mu úspěšně nabídl).
- **Passes Attempted Total / Passes Attempted** (pass_count_attempted): Celkový počet pokusů hráče o přihrávku.
- **Passes Completed** (pass_count_completed): Celkový počet úspěšně zkompletovaných přihrávek.
- **Passes Completed Pct** (pass_pct_completed): Procentuální úspěšnost přihrávek (Completed / Attempted).
- **Passes Attempted Avg xPass** (pass_avgxpass_attempted): Průměrná očekávaná úspěšnost (xPass) všech pokusů o přihrávku vynásobená 100. Ukazuje, jak technicky a pozičně náročné přihrávky hráč v průměru volí (nižší číslo = volí riskantnější/těžší pasy).
- **Passes Avg Distance** (pass_avgdistance): Průměrná délka (v metrech) pokusů o přihrávku.
## 3. VÝSLEDEK AKCE A EFEKTIVITA (End Product)
- **Passes Leading To Shot** (pass_count_shotwithin10s): Počet zkompletovaných přihrávek, které do 10 sekund vedly ke střele týmu.
- **Passes Leading To Goal** (pass_count_goalwithin10s): Počet zkompletovaných přihrávek, které do 10 sekund vedly ke vstřelenému gólu. (Podobné konceptu "Předfinální/Finální přihrávka").
## 4. RYCHLOST A STYL DISTRIBUCE (Passing Style)
- **Passes Attempted (Long-Range)** (pass_count_longrange_attempted): Počet pokusů o dlouhou přihrávku (delší než 30 metrů).,
- **Passes Attempted (One-Touch)** (pass_count_onetouch_attempted): Počet přihrávek, které hráč zahrál z prvního doteku (z voleje/bez zpracování).
- **Passes Attempted (Quick Pass)** (pass_count_quickpass_attempted): Počet rychlých přihrávek. Hráč měl míč pod kontrolou kratší dobu než 1 sekundu předtím, než jej přihrál.
## 5. NEBEZPEČNOST A OBTÍŽNOST (Threat & Difficulty)
*AI model k určení těchto metrik využívá interní modely xThreat a xPass.*
- **Pass Opportunities (Dangerous)** (passopportunity_count_dangerous): Počet nebezpečných možností k přihrávce, které se hráči nabízely (spoluhráči s xThreat > 0.02). Ukazuje, jak dobře týmoví kolegové tvořili nabídku.
- **Passes Attempted (Dangerous)** (pass_count_dangerous_attempted): Počet pokusů o "Nebezpečnou přihrávku" (xThreat adresáta je vyšší než 0.02 / 2% šance na gól). Ukazuje odvahu a vidění hry (Vision) přihrávajícího.
- **Passes Completed (Dangerous)** (pass_count_dangerous_completed): Počet úspěšně doručených nebezpečných přihrávek (Klíčová metrika pro playmakery).
- **Passes Completed (Dangerous) Pct** (pass_pct_dangerous_completed): Procentuální úspěšnost realizace těchto nebezpečných (riskantních) přihrávek.
- **Passes Attempted (Difficult Pass)** (pass_count_difficultpass_attempted): Počet pokusů o obtížnou přihrávku, tedy takovou, kde matematická šance na doručení (xPass) byla nižší než 65 %. Odhaluje vysoce sebevědomé a technické hráče.
- **Passes Attempted (One-Touch, Dangerous)** / **... (Quick Pass, Dangerous)**: Nebezpečné přihrávky realizované z první / do 1 vteřiny. Ukazuje schopnost tvořit nebezpečí ve velké rychlosti.,
## 6. PŘEKONÁVÁNÍ OBRANY (Line-Breaking)
*Systém dynamicky vyhodnocuje obranný blok soupeře a měří přihrávky, které ho protnou.*
- **Pass Opportunities (Line-Breaking)** (passopportunity_count_linebreak): Počet situací, kdy hráč držel míč a měl možnost přihrát za některou z obranných linií soupeře.
- **Passes Attempted (Line-Breaking)** (pass_count_linebreak_attempted): Celkový počet pokusů hráče propíchnout nebo překonat obrannou linii soupeře.
- **Passes Completed (Line-Breaking)** (pass_count_linebreak_completed): Počet úspěšných přihrávek překonávajících linii.
## 7. PŘIHRÁVKY DO NÁBĚHŮ (Passing To Run)
*Hodnotí kooperaci hráče s míčem a nabíhajícího spoluhráče (Off-Ball Run >15km/h).*
- **Pass Opportunities (To Run)** (passopportunity_count_torun): Kolikrát se hráči na míči objevil spoluhráč ve sprintu/náběhu jako reálná možnost k přihrávce.
- **Passes Attempted (To Run)** (pass_count_torun_attempted): Kolikrát se hráč skutečně pokusil přihrát míč na nabíhajícího spoluhráče.
- **Passes Completed (To Run)** (pass_count_torun_completed): Počet úspěšných přihrávek do náběhu.
- **Passes Completed (To Run) Pct** (pass_pct_torun_completed): Úspěšnost přihrávek směřovaných do náběhu.
- **Passes Attempted (To Run) Avg xPass** (pass_avgxpass_torun_attempted): Průměrná pravděpodobnost zkompletování (obtížnost) u přihrávek hraných do náběhů (x100).
- **Passes Leading To Shot (To Run)** (pass_count_torun_shotwithin10s): Úspěšné přihrávky do náběhu, které vyústily ve střelu do 10 sekund. Ukazuje reálnou ofenzivní destrukci obrany.
- **Passes Leading To Goal (To Run)** (pass_count_torun_goalwithin10s): Úspěšné přihrávky do náběhu zakončené gólem.

Passing Options
- **Competition Edition ID** až **Position Group**: Standardní identifikátory zápasu, soutěže, týmu a hráče.
- **Minutes**: Celkový počet odehraných minut.
- **Minutes (Tip)** (minutes_tip): Minuty čistého času, kdy měl tým hráče míč v držení. **Zásadní parametr pro normalizaci těchto útočných metrik (per 30 TIP).**
- **Minutes (Otip)**: Minuty čistého času bez míče (zde nevyužito, určeno pro obranu).
- **GI Check Passed**: Indikátor (TRUE/FALSE) dostatečné kvality trackingu pro výpočet Game Intelligence.
## 2. ZÁKLADNÍ OBJEM A EFEKTIVITA NABÍDKY (Volume & Effectiveness)
*Hodnotí, jak často se hráč dokáže uvolnit a zapsat se do hry jako dostupná volba pro spoluhráče s míčem.*
- **Options Offered Total / Options Offered** (optionoffered_count): Počet situací, kdy se hráč bez míče úspěšně nabídl spoluhráči jako reálná a dostupná možnost k přihrávce.
- **Options Offered Targeted** (optionoffered_count_targeted): Počet nabídek, které spoluhráč s míčem reálně využil a pokusil se na hráče přihrát.
- **Options Offered Received** (optionoffered_count_received): Počet nabídek, které skončily tím, že hráč úspěšně přijal míč a dostal jej pod kontrolu.
- **Options Offered Leading To Shot** (optionoffered_count_shotwithin10s): Počet situací, kdy hráč úspěšně přijal míč ze své nabídky, a tým z této akce do 10 sekund vystřelil.
- **Options Offered Leading To Goal** (optionoffered_count_goalwithin10s): Stejné jako výše, ale akce skončila přímo vstřeleným gólem.
## 3. TAKTICKÁ NEBEZPEČNOST NABÍDKY (Tactical Threat)
*Sleduje kvalitu výběru místa – tedy zda se hráč nabízí v prostorech, které tvoří skutečnou hrozbu.*
- **Options Offered (Dangerous)** (optionoffered_count_dangerous): Počet nebezpečných nabídek. Situace, kdy se hráč uvolnil do takové pozice, ze které by po obdržení míče stoupla šance na gól nad 2 % (xThreat > 0.02).
- **Options Offered (Line-Breaking)** (optionoffered_count_linebreak): Počet nabídek, kterými hráč umožňoval spoluhráči propíchnout (překonat) obrannou linii soupeře.
## 4. POZICE A GEOMETRIE HRÁČE (Positioning in Space & Shape)
*Modely hodnotí topologii hřiště a pozici nabízejícího se hráče vůči obrannému bloku soupeře.*
- **Options Offered (In Space)** (optionoffered_count_inspace): Nabídky, při kterých byl hráč umístěn ve volném prostoru a nebyl pod těsným dohledem obránce.
- **Options Offered (Wide)** (optionoffered_count_wide): Nabídky situované u postranních čar (v širokém křídelním prostoru).
- **Options Offered (Inside Defensive Shape)** (optionoffered_count_insidedefensiveshape): Vysoce cenné nabídky realizované **uvnitř** obranné struktury (bloku) soupeře. Typicky jde o nabídku mezi liniemi obrany a zálohy, kde je těžké přijmout míč.
- **Options Offered (Outside Defensive Shape)** (optionoffered_count_outsidedefensiveshape): Nabídky odehrávající se vně (okolo) obranného bloku soupeře. Typicky jde o stopery tvořící hru vzadu nebo hráče na křídle obíhající blok.
## 5. NABÍDKA V POKUTOVÉM ÚZEMÍ (Penalty Area Context)
*Izolovaný pohled na chování hráče (typicky útočníka) v nejdůležitějším prostoru na hřišti.*
- **Options Offered (Penalty Area)** (optionoffered_count_penaltyarea): Počet nabídek k přihrávce z pozice přímo uvnitř soupeřova pokutového území (vápna).
- **Options Offered Received (Penalty Area)** (optionoffered_count_penaltyarea_received): Počet úspěšně přijatých míčů uvnitř vápna.
- **Options Offered Leading To Shot (Penalty Area)** (optionoffered_count_penaltyarea_shotwithin10s): Nabídky a přijetí míče uvnitř pokutového území, po kterých následovala střela do 10 sekund.
- **Options Offered Leading To Goal (Penalty Area)** (optionoffered_count_penaltyarea_goalwithin10s): Nabídky a přijetí míče uvnitř pokutového území, po kterých následoval gól.

Physical
## 1. ZÁKLADNÍ METADATA A KONTROLA KVALITY
*Tato skupina obsahuje standardní identifikátory a navíc klíčovou kontrolu kvality tracking dat.*
- **Player** až **Minutes**: Standardní identifikátory zápasu, ligy, týmu, hráče a počtu odehraných minut.
- **Physical Check Passed**: Logická hodnota (TRUE/FALSE) udávající, zda kvalita broadcast tracking videa v tomto zápase byla dostatečně plynulá a kvalitní pro výpočet fyzických metrik. Výkony s hodnotou FALSE by se měly z analýz vyloučit.
## 2. VZDÁLENOST A KAPACITA BĚHU (Volume & Distance)
*Tato kategorie měří, kolik toho hráč naběhá a v jakých rychlostních pásmech. Každá z metrik má i svou standardizovanou verzi* *P90* *(např.* *Distance P90**).*
- **Distance**: Celková uběhnutá vzdálenost hráče v zápase (v metrech).
- **M/min**: Průměrná vzdálenost, kterou hráč urazí za jednu minutu hry (ukazuje celkové pracovní tempo - work rate).
- **Running Distance**: Vzdálenost (v metrech) uběhnutá ve středním tempu, konkrétně v pásmu **15 km/h až 20 km/h**.
- **HSR Distance** *(High Speed Running)*: Vzdálenost uběhnutá ve vysoké rychlosti, konkrétně v pásmu **20 km/h až 25 km/h**.
- **Sprint Distance**: Vzdálenost uběhnutá ve sprintu, tedy rychlostí **nad 25 km/h**.
- **HI Distance** *(High Intensity)*: Celková vzdálenost naběhaná ve vysoké intenzitě. Jde o součet HSR Distance a Sprint Distance (vše **nad 20 km/h**).
## 3. POČET ÚSEKŮ A INTENZITA (Count of Efforts)
*Místo vzdálenosti se zde počítá přesný počet izolovaných náběhů. Akce je započítána, pokud klouzavý průměr rychlosti překročí danou hranici v okně 1 sekundy. Mají i své verze* *P90**.*
- **HSR Count**: Počet izolovaných náběhů, při kterých hráč dosáhl rychlosti 20–25 km/h.
- **Sprint Count**: Počet izolovaných sprintů (nad 25 km/h).
- **HI Count**: Celkový počet náběhů ve vysoké intenzitě (součet HSR Count a Sprint Count).
## 4. ABSOLUTNÍ MAXIMÁLNÍ RYCHLOST (Top Speed)
- **PSV-99** *(Peak Sprint Velocity 99th percentile)*: Zásadní metrika pro maximální rychlost hráče (v km/h). Namísto absolutního maxima, které může být u broadcast trackingu zkresleno šumem (chybou), systém rozdělí všechny rychlosti hráče nad 4 m/s do 100 košů a vezme hodnotu z 99. percentilu. Tato metrika odráží čistý rychlostní potenciál hráče a jeho schopnost tuto rychlost udržet. (Tato metrika se nenormalizuje na 90 minut).
## 5. AKCELERACE A DECELERACE (Změny rychlosti)
*Schopnost hráče dynamicky zrychlit nebo zastavit. Událost musí trvat minimálně 0.7 sekundy, aby byla započítána. Dostupné i ve verzi* *P90**.*
- **Medium Acceleration Count**: Počet středních zrychlení, v rozmezí **1.5 m/s² až 3 m/s²**.
- **High Acceleration Count**: Počet vysokých (prudkých) zrychlení **nad 3 m/s²**.
- **Medium Deceleration Count**: Počet středních zpomalení / brzdění, v rozmezí **-1.5 m/s² až -3 m/s²**.
- **High Deceleration Count**: Počet prudkých zpomalení, hodnoty klesají rychlostí **pod -3 m/s²**.
## 6. EXPLOZIVITA A DOSAŽENÍ RYCHLOSTI (Explosiveness & Time to Speed)
*Pokročilé metriky, které spojují zrychlení a konečnou rychlost. Měří "výbušnost" hráče (jak rychle dosáhne maximální rychlosti z klidu nebo po kličce).*
- **Explosive Acceleration to HSR Count** (a verze P90): Počet prudkých zrychlení (High Acceleration), u kterých hráč **startoval z rychlosti nižší než 9 km/h (z chůze/výklusu) a dokázal dosáhnout HSR (min. 20 km/h)**.
- **Explosive Acceleration to Sprint Count** (a verze P90): Počet extrémně výbušných akcelerací, kdy hráč startoval pod 9 km/h a dosáhl sprintu (nad 25 km/h).
- **Time to HSR**: Čas (v sekundách), který hráč potřeboval na překonání intervalu z 9 km/h na 20 km/h (během explozivní akcelerace). Čím menší číslo, tím výbušnější hráč.
- **Time to Sprint**: Čas (v sekundách), který hráč potřeboval na překonání intervalu z 9 km/h na 25 km/h.
## 7. AGILITA A ZMĚNY SMĚRU POHYBU (Agility & Change of Direction)
*Hodnotí plynulost pohybu na malém prostoru a schopnost neztrácet rychlost při kličkách a obratech.*
- **Change of Direction Count** (a verze P90): Celkový počet intenzivních změn směru pohybu (např. ostré otočky). Ukazuje celkovou mobilitu a dynamický objem hráče.
- **Time to HSR post-COD** / **Time to Sprint post-COD**: Doba potřebná k dosažení HSR (20 km/h) nebo sprintu (25 km/h) měřená **bezprostředně po změně směru** (Change of Direction). Ukazuje výbušnost po otočce.
- **Time to 505 around 90**: Čas ze specifického agility testu "505" aplikovaného na herní data. Vyjadřuje čas, který hráč v běhu potřebuje k překonání 5 metrů PŘED ostrou otočkou (o cca 90 stupňů) a 5 metrů bezprostředně PO NÍ.
- **Time to 505 around 180**: Stejná metrika jako výše, ale jedná se o obrat o cca 180 stupňů (protipohyb / brzda a návrat). Nižší čas znamená vynikající agilitu a schopnost brzdit i akcelerovat v jednom plynulém pohybu.

Player Possessions
## 1. ZÁKLADNÍ METADATA A HERNÍ ČAS
- **Competition Edition ID** až **Position Group**: Standardní identifikátory kontextu (zápas, soutěž, tým, hráč).
- **Minutes**: Celkový počet odehraných minut.
- **Minutes (Tip)** (minutes_tip): Čistý čas, po který měl tým hráče míč v držení. **Naprosto klíčový parametr pro normalizaci těchto útočných metrik (přepočet per 30 TIP).**
- **Minutes (Otip)**: Čistý čas bez míče.
- **GI Check Passed**: Indikátor (TRUE/FALSE) dostatečné kvality trackingu pro výpočet pokročilých metrik.
## 2. ZÁKLADNÍ DRŽENÍ MÍČE A JEHO UDRŽENÍ (Possessions)
*Držení míče (Possession) nastává, když má hráč míč prokazatelně pod kontrolou.*
- **Possessions Total / Possessions** (possession_count): Celkový počet situací, kdy měl hráč míč pod kontrolou.
- **Possessions Retained** (possession_count_retained): Počet držení míče, ze kterých tým nevyšel se ztrátou (hráč akci zakončil úspěšnou přihrávkou, střelou apod.).
- **Possessions Retained Pct** (possession_pct_retained): Procentuální úspěšnost udržení míče (Retained / Total).
- **Possessions Leading To Shot** (possession_count_shotwithin10s): Počet držení, po kterých tým do 10 sekund vystřelil.
- **Possessions Leading To Goal** (possession_count_goalwithin10s): Počet držení, po kterých tým do 10 sekund vstřelil gól.
- **Possessions Avg Distance** (possession_avgdistance): Průměrná vzdálenost (v metrech), kterou hráč s míčem u nohy překoná během jednoho držení.
- **Possessions Avg Duration** (possession_avgduration): Průměrná doba (v sekundách), po kterou hráč udrží míč na kopačce během jedné akce.
## 3. PŘIJETÍ MÍČE A KONTEXT PROSTORU/TLAKU (Receptions)
*Hodnotí moment, kdy hráč přijímá přihrávku a jak těžké to v danou chvíli má.*
- **Receptions Total / Receptions** (reception_count): Celkový počet úspěšných přijetí přihrávky hráčem.
- **Receptions Retained** (reception_count_retained): Přijetí míče, po kterém hráč dokázal navázat a udržet držení míče (neztratil ho hned po doteku).
- **Receptions Retained Pct** (reception_pct_retained): Procentuální úspěšnost udržení míče ihned po jeho přijetí.
- **Receptions (In Space)** (reception_count_inspace): Počet přijetí míče ve volném prostoru (hráč měl kolem sebe dostatek místa na zpracování).
- **Receptions (Intense Pressure)** (reception_count_intensepressure): Přijetí míče, ke kterému došlo pod intenzivním tlakem napadajícího soupeře.
- **Receptions (Intense Pressure, Tight Space)** / **... Constrained Space**: Situace s nejvyšším stupněm obtížnosti – hráč přijal míč jak pod intenzivním tlakem, tak ve velmi stísněném prostoru (úzké postavení bloku).
- **Receptions Retained (Intense Pressure, Tight Space)** a přidružené **Pct**: Absolutní počty a procentuální úspěšnost toho, jak hráč tyto nejtěžší situace zvládl a míč i navzdory obrovskému tlaku a malému prostoru udržel. (Klíčová metrika pro hodnocení "Press-Resistance" záložníků).
## 4. VYVEZENÍ MÍČE A DRIBLINK (Long Carries)
*Carry je definováno jako posun s míčem na kopačce o vzdálenost delší než 8 metrů.*
- **Long Carries Total / Long Carries** (longcarry_count): Celkový počet situací, kdy hráč vyvezl míč o více než 8 metrů.
- **Long Carries Retained** a **Pct**: Počet a procentuální úspěšnost vyvezení míče, která neskončila ztrátou.
- **Long Carries (Forward Trajectory)** (longcarry_count_forwardtrajectory): Progresivní vyvezení – hráč s míčem postupoval směrem dopředu k brance soupeře.
- **Long Carries (Above HSR)** (longcarry_count_abovehsr): Rychlostní vyvezení – hráč s míčem běžel rychlostí vyšší než 20 km/h (High-Speed Running).
- **Long Carries (Forward Trajectory, Above HSR)** a příslušné **Retained** / **Pct**: Specifická a velmi cenná útočná akce: hráč vyvezl míč směrem dopředu ve vysoké rychlosti sprintu.
## 5. PŘEKONÁVÁNÍ SOUPEŘE A KREATIVITA NA MÍČI
*Hodnotí individuální herní inteligenci a schopnost tvořit výhodu (tzv. Overcoming Opponents).*
- **Possessions (Forward Momentum)** (possession_count_forwardmomentum): Okamžitá progrese hry. Situace, kdy hráč hned při prvním doteku (zpracování) dokázal zrychlit nebo se s míčem otočit čelem vpřed, a to pod tlakem.
- **Give-And-Gos** (giveandgo_count): Hra na jeden/dva doteky ve formě "narážečky". Hráč míč přihrál a ihned si naběhl do prostoru pro zpětnou přihrávku.
- **Possessions (Beat By Possession)**: Situace, kdy hráč s míčem na kopačce úspěšně překonal (obešel) obránce soupeře (např. úspěšný ofenzivní driblink 1v1).
- **Possessions (Beat By Movement)**: Situace, kdy hráč překonal bránícího soupeře pohybem ještě před/během obdržení míče.
## 6. LÁKÁNÍ A ZBAVOVÁNÍ SE TLAKU (Escaping Pressure & Threat)
*Zcela nové koncepty zavedené v Game Intelligence V2, hodnotící vyspělou hru s těžištěm a tlakem.*
- **Possessions (Drew Pressure)** (possession_count_drawnpressure): Hráč na míči záměrně "natáhl" tlak napadajícího soupeře k sobě, aby uvolnil prostor pro spoluhráče. Zahrnuje i statistiky, zda z toho tlaku vyšel bez ztráty (**Retained (Drew Pressure)** a **Pct**).
- **Possessions Escaped Pressure** (possession_count_escapedpressure): Špičková schopnost vyvázání se z presinku. Držení míče, které začalo pod intenzivním tlakem soupeře a ve stísněném prostoru, ale hráč se z něj úspěšně vymanil a zakončil své držení míče v prostoru bez tlaku (Light pressure).
- **Possessions Escaped Pressure Pct**: Procento z intenzivně presovaných míčů, ze kterých se hráč dokázal vymanit.
- **Possessions Progressed (Intense Pressure)** a **Pct**: Zda hráč dokázal pod intenzivním tlakem posunout hru výrazně vpřed.
- **Possessions Created Danger (Intense Pressure)** a **Pct**: Počet a procento situací, kdy hráč i pod intenzivním tlakem dokázal vytvořit vysokou gólovou hrozbu (zakončení akce nad xThreat > 0.02 nebo šance/střela). Značí elitní tvůrce hry.

Team Stats a Player stats - jsou data zcela jasná, protože název sám o sobě vypovídá, co data říkají

1. Logika tvorby reportu
- Chci, aby report zohledňoval silné a slabé stránky Sigmy Olomouc a silné a slabé stránky soupeře a vždy mezi tím hledal kontext, kde je možné soupeře nejvíce ohrozit v kontextu našich silných stránek a jeho slabin a naopak kde nás může soupeř nejvíce ohrozit na základě našich slabin a jeho silných stránek v tomto ohledu
- Používat ale veškerá dostupná data k soupeři

1. Podrobné informace pro analýzu
- Report bude mít vždy strukturu
- Dej informace jakého soupeře analyzuješ, kolik bylo analyzováno utkání soupeře a z jakého data.
	- Základní charekteristika soupeře - jaký styl fotbalu hraje, v čím je typický, kdo jsou jejich klíčový hráči. Krátký souhrn, který udělá jasnou představu o tom, jaký hraje soupeř fotbal a co od něho čekat 
	- Nejčastější rozestavení které hrají
	- Výstavba hry - jak se soupeř typicky chová ve výstavbě hry, kteří hráči jsou nejčastěji využívaní, kteří jsou ale naopak v této části využívaní méně, protože například špatně řeší situace pod tlakem. Tuto část přípravy využijeme proto, abychom věděli, jak soupeře a koho konkrétně co nejefektivněji napadat a do jakých prostor ho například dostat, kde bude nejzranitelnější.
	- Způsob vedení útoku - jak se nejčastěji chovají při vedení útoku, kteří hráči jsou nejsilnější tvůrci hry, jaké části hřiště jsou nejvytíženější. Opět budeme na tuto situaci reagovat jak se chovat ve středním obranném bloku.
	- Finální fáze - jak se nejčastěji chovají ve finální fázi hry. Jaké druhy náběhů nebo průniků do pokutového území používají, v čem jsou nejsilěnší, kteří hráči jsou nejvíce nebezpeční, z jakých prostor se nejčastěji dostávají do pokutového území, kteří hráči jsou nejvíce nebezpeční v zakončení, kteří naopak v tvorbě šancí, apodobně. Jsou to důležité informace, abychom věděli, na jaké hráče si dát pozor, jak se typicky chovají a jaké například zaujímat postavení nebo také jaké hráče dát do základní sestavy v reakci na hru soupeře. 
	- Hra ve vysokém bloku - jak se chová když rozehrává tým, proti kterému hraje. Napadá vysoko a ihned po rozehře, jde spíše do bloku, kolik hráčů napadá, atd. Všechny informace, které mohou vést k tomu, abychom věděli, jaký optimální scénář zvolit pro rozehru od naší branky. Využij data hráčů a grafické znázornění High Block Phase z jednotlivých utkání v PDF reportu **Out of Possession Summary**
	- Jak se soupeř chová při hře ve střední a nízkém bloku - jak jsou konzistentní, jak mají hustý blok, kde mají volné prostory a kudy by bylo ideální vést útok a jakým způsobem. Jestli hrát více do nohy, jestli více rozebíhat, popřípadě jestli hrát za obranu, atd.. Využij data hráčů a grafické znázornění  Medium Block Phase a Low Block Phase z jednotlivých utkání v PDF reportu **Out of Possession Summary).**
	- Presink - jak se soupeř chová při napadání, má agresivní presink, jak je úspěšný, jestli se po ztrátě míče vrací do bloku nebo jestli okamžitě napadá, apod..jak je úspěšný 
	- Jak se chová soupeře ve svém vlastním pokutovém území - jsou silní ve vzduchu, ve hře po zemi, propadávají jim míče, mají problémy s centry nebo naopak průniky a podobně 
	- Zhodnotit silné a slabé stránky soupeře
	- Upozornění a doporučení - Co se na základě vzájemné analýzy zjistilo a stojí za to si říct. Hodně do kontextu dávat hráče, kteří budou pravděpodobně hrát proti sobě ze všech možných hledisek (například: soupeř má rychlého levého útočníka a my máme pomalého pravého stopera. Atd..)
	- Udělat základní charakteristiku hráčů soupeře (ideálně hráčů nejvíce vytížených, kteří připadají v úvahu, že budou nastupovat v základní sestavě nebo dostřídávat v průběhu utkání) 
		- Silné stránky a na co si u něho dát pozor 
		- Slabé stránky a co je důležité o něm vědět pro naši hru, čeho u něho vyžít
		- Jaká je jeho charakteristická hra
		- Jeho maximální rychlost a charakteristicky kondiční výkon
		- Označit jejich klíčové hráče a proč je za klíčové považovat
	- Zvažuj a dávej také informace v kontextu jak se mění hra pokud tým prohrává nebo naopak vede, jak reagují na vývoj utkání. Pokud najdeš jakékoli abnormality v různém kontextu, tak o tom informuj. 
	- Všechna data brát maximálně v kontextu, co to půjde. Porovnávat hru celého týmu v návaznosti na data jednotlivých hráčů a vše zasazovat do kontextu
	- Používat co nejvíce věcné informace přenositelné, které se dají aplikovat do herního plánu 
	- Vyvarovat se protichůdným informacím a vše mít podložené a vědět, proč to tvrdím
	- Důkladně si dát záležet na to, aby byla použitá data správného týmu
	- Důkladně také kontrolovat, že jsou použitá správná data se správným významem
	- Vyhnout se jakémukoli balastu a zbytečným frázím. Byt co nejvíce věcný 

## UI, Export a Další požadavky
- Report musí být možné vyexportovat do PDF v co nejlepší vizuální formě. Ideálně černý text na bílém pozadí se zvýrazněním nejdůležitějších informací. Bez zbytečných grafických prvků a bez zbytečností navíc.
- Dělej historii vygenerovaných reportů a uchovávej je, dávej ale možnost tyto reporty mazat.
- Dej možnost sdílet výsledný report přes odkaz - nemůže být možné po otevření odkazu dále editovat (Read-only).
- Tvoji finální aplikaci kompletně otestuj.
- Dej mi odkaz/instrukce, na kterém budu moct aplikaci používat.
# Je potřeba upravit:
- Jejich stopeři (Prebsl, Camara) nejsou rychlostně dominantní a mají problémy s náběhy za záda 
	- Camara je rychlostně velmi dobře vybavený - je potřeba správně přistupovat ke kontextu 
- Zaměřit se na rozestavení 
- Zaměřit se na to, kdo chybí - nemoc, karty, atd.. a ty z toho vyndat (dodat více kontextu, který vím)
- V přípravách se hodně zaměřit na fakta, jména, a s tím spojené metriky o hráčích
- Interpretace - pokud něco tvrdím, musím podložit proč to tvrdím (místo metrik dávat smyslupné názvy)
- - 

## Prompt pro Claud
- Potřebuji vytvořit aplikaci, která mi na základě statistik dvou týmů udělá pomocí nejnovější AI s hlubokým přemýšlení, skvělý strategický plán (přípravu) na utkání
- Aplikace bude mít za úkol porovnat data dvou týmů, jeden tým bude vždy označený jako můj vlastní tým, pro který dělám strategii. Data obou týmů se porovnají a budou se primárně hledat slabá místa na straně soupeře na základě našich silných stránek a nebezpečná místa soupeře na základě našich slabin

- Jak by měla aplikace fungovat:
Celá aplikace má svůj levý navigační panel s těmito odrážkami: 
 **Nahrání dat** -  tam nahraji všechna dostupná data (FORMÁTY:CSV, XLSX, PDF).  Musím mít možnost zakliknout, který je můj vlastní tým (toto zakliknutí zůstane uloženo pro příští použití a je editovatelné). Na základě Team ID ze souboru se mi automaticky propíše Team ID a Team - v databázi budou vždy unikátní údaje. Tyto údaje se automaticky uloží do databáze, ke které je vždy přístup a je editovatelná - musím vidět ke kterému týmu mám kolik utkání a jaký je datum posledního utkání (a datum poslední aktualizace dat pro daný tým). Pokud tedy z databáze uložených týmů příště vyberu svůj tým, automaticky je označený jako vlastní tým.

1. **Databáze dat** 
	1. **Databáze**: Nahrané soubory a statistky se automaticky ukládají do databáze (všechna data podle IDs musí být unikátní) a při každém nahrání se data pro daný dataset (tabulku) automaticky obohatí o nová nahraná dat. Datové zdroje budou vždy nahrané ty stejné - **PlayerPossessions, Physical, PassingOptions, Passes, OnBallEngagements, OffBallRuns,**  **InPossessionSummary, OutOfPossession** - pro tyto datové zdroje si postav databázi. Zdrojové sobubory budou vždy pro každý tým tyto. Obsahují Team ID - tím se identifikuje tým, Team - jeho název a Player ID - id konkrétního hráče. Vytvoř si vždy tabulky týmů - název a ID týmu, vytvářej si také tabulky hráčů, kde bude vždy ID týmu, k tomu ID hráče (aby bylo jasné, o jakého hráče z jakého týmu se jedná) následně k nim připoj statistiky, také si drž tabulky soutěží přes Competiton ID a konkrétních utkání přes Match ID a Season ID. Udělej logickou strukturu tak, aby vyhodnocení dat bylo vždy co nejpřesnější a pro tebe nejlepší. Databáze je tak na tobě, jak bude nejlepší ji strukturovat, aby se z ni co nejlépe vyhodnocovala data. Do databáze musí být možné vstoupit a na ROW data se podívat v krajním případě přes heslo také data editovat. Drž si také soupisky jednotlivých týmů apod. 
	2. **Datový model** - chci mít přístup k jasnému datovému modelu - jak jsou data poskládaná, v jaké logice a jak na sebe vzájemně navazují.
	- Všchny soubory, které budou postupně tvořit dataset ti sdílím jako ukázka, aby si měl vytvořenou jasnou datovou mapu (tato data jsou pouze ukázka, aby si mohl vytvořit databází a strukturu. Tato data do databáze nezaznamenávej) 
	Krátký popis, co které datové zdroje obsahují: 
- **PlayerPossessions (Držení míče hráčem) Formát: CSV:** Tato sekce se zaměřuje na individuální akce hráče ve chvíli, kdy má míč pod kontrolou. Obsahuje statistiky o přijetí míče (včetně přijetí pod intenzivním tlakem nebo v úzkém prostoru), vyvezení míče na delší vzdálenost (tzv. carries), schopnosti vymanit se z tlaku (escaped pressure) a o tom, zda dokázal překonat obránce a vytvořit posun hry vpřed (forward momentum).
- **Physical (Fyzické metriky) Formát: CSV:** Obsahuje čistě atletická data o pohybu hráče. Najdete zde uběhnuté vzdálenosti, počty náběhů ve vysoké intenzitě (HSR) a ve sprintu, ale také pokročilé údaje jako je maximální dosažená rychlost, explozivní akcelerace a schopnost rychle měnit směr.
- **PassingOptions (Možnosti přihrávky) Formát: CSV:** Vyhodnocuje momenty, kdy hráč zrovna nemá míč, ale **nabízí se jako volba pro přihrávajícího spoluhráče**. Sleduje, kolikrát hráč takovou možnost vytvořil, zda nabízel možnost překonat obrannou linii, zda operoval uvnitř či vně obranného bloku soupeře, kolikrát mu byla přihrávka skutečně určena (targeted) a kolikrát míč dostal (received).
- **Passes (Přihrávky) Formát: CSV:** Mapuje distribuci míče a kreativitu **přihrávajícího hráče**. Hodnotí, kolik přihrávek hráč zkusil a zkompletoval, jaká byla jejich očekávaná úspěšnost (xPass), a zda šlo o přihrávky propichující obranné linie soupeře (Line-Breaking). Patří sem i hodnocení obtížných (difficult) a nebezpečných (dangerous) přihrávek a přihrávek směřujících přesně na hráče v náběhu.
- **OnBallEngagements (Obranné akce vůči hráči s míčem) Formát: CSV:** Tato tabulka detailně popisuje defenzivní chování hráče, když má míč soupeř. Klasifikuje různé druhy tlaku na míč (individuální tlak, organizovaný presink, okamžitý represink, návratový presink). Dále hodnotí výsledky tohoto tlaku – například zda obránce míč získal (regain), donutil soupeře hrát dozadu (force backward), narušil akci (disruption), nebo zda naopak propadl a soupeř ho překonal driblinkem či pohybem.
- **OffBallRuns (Náběhy bez míče) Formát: CSV:** Sleduje aktivní a rychlý pohyb hráčů útočícího týmu, kteří právě nemají míč. Náběhy detailně člení do specifických typologických kategorií, jako jsou náběhy za obranu (in behind), na centr (cross receiver), seběhnutí nakrátko (coming short) nebo obíhání (overlap a underlap). Kromě absolutních počtů hodnotí, zda byly náběhy nebezpečné (Dangerous runs) a kolik očekávané hrozby (Avg Threat / xThreat) konkrétní pohyb vygeneroval.
- **InPossessionSummary (Data týmu v držení míče)**: PDF report specifikující chování týmy v čase, kdy drží míč po jednotlivých utkáních. Zásadní jsou grafická znázornění s postavením ve výstavbě hry, tvorbě hry a ve finální fázi. Detailně přečti celé PDF a tato data přepiš do číselných statistky, které si budeš udržovat v datasetu.
- **OutOfPossession (Data týmu ve hře bez míče):** PDF report specifikující chování týmy v čase, kdy nedrží míč. Z grafického zobrazení určí z průměrných hodnot analyzovaných utkání, kde je soupeř nejúspěšnější v získávání míčů a kde má naopak slabiny a kudy je na základě tohoto poznatku nejvýhodnější vést útok. Detailně přečti celé PDF a tato data přepiš do číselných statistky, které si budeš udržovat v datasetu.
- **PlayerStats (Hráčská data) Formát: CSV**: Všeobecná herní data za jednotlivá utkání
- **TeamStats (Týmová data) Formát: CSV:** Všeobecná souhrnná dat týmu v jednotlivých utkání zdroj pro základní informace o hře týmu, rozestavení a jeho výsledcích. 

1. **Metadata** - musím mít možnost nahrát ke všem datovým zdrojům jejich metadata a přesný popis - v této sekci budu mít možnost vždy přidat nový text - přímo do aplikace, který se uloží jako soubor, do kterého mohu vždy stoupit a editovat ho. Bude to jednak popis jednotlivých metrik, ale také to co musí bezpodmínečně obsahovat analýza, popřípadě další kontext k datům. Také tam bude přesný a detailní popis jednotlivých datasetů co přesně říkají a další soubory. Zkrátka budou tam jednotlivé soubory metadata, která pomůžou k vyhodnocení AI v dané analýze. Metadata musí mít svůj název, jsou editovatelná a je možné je smazat. 

1. **Analýza dat**: 1. Krok - vyberu si domácí a hostující tým pro nadcházející utkání. Chtěl bych, aby se také zkoumal vliv domácího nebo venkovního prostředí na výsledky. Tyto týmy si vybírám na základě týmů, pro která mám v databází data (při výběru vidím, datum posledního nahraného utkání a datum poslední aktualizace dat). Mám možnost ke každému týmu vložit doplňující text. Třeba souhrnné informace z posledních utkání, které se píší v médiích, nebo které hráče mají zraněné, atd.. tento text je potřeba brát v potaz při analýze. 2. Krok samotná analýza. Pro analýzu budou použitá data striktně z datasetu, která byla nahrána do databáze - nevytváříš žádné domněnky ani si sám nevymyslíš nic co není podloženo daty. Je zakázáno čerpat jakékoli jiné informace z jiných zdrojů například z internetu. Pro kvalitu analýzu budou také použité všechny informace s metadat, která byla vytvořená. 
	Report bude mít dvě části

- &nbsp;
	1. Analýz a hry týmu a ta má strukturu: 
		1. Z jakých utkání soupeře byla analýza vytvořená
		2. **Základní charakteristika a rozestavení** - jaký je podle dat styl hry soupeře, kdo a proč je stěžejním hráčem. V jakém rozestavení nejčastěji hrají, popřípadě jak se mění jejich rozestavení v závislosti na kvalitě soupeře. 
		3. **Výstavba hry (Build-up):** Jak se soupeř typicky chová v rozehře a výstavbě hry. Kteří hráči jsou nejčastěji využívaní - kdo řídí rozvrhu, kdo je jak odváží v rozepře nebo výstavbě, kdo nejčastěji vyváží míče, atd.. (Zvaž všechny aspekty, které mohou být v této fázi hry důležité) a kteří naopak dělají pod tlakem chyby. AI zde zváží všechny dostupné metriky k výstavbě, presinku soupeře i ztrátám míče.
		4. **Způsob vedení útoku & Finální fáze:** Jak přecházejí do útoku a jak se chovají ve finální třetině. Jaké druhy náběhů nebo průniků používají, kudy nejčastěji vedou útoky a kdo je největší hrozbou (tvorba šancí, xThreat, finální přihrávky, náběhy za obranu, proměňování šancí a zakončení). 
		5. **Presink a hra v bloku:** Jak se chová soupeř při naší rozehrávce. Kde mají těžiště obrany (High/Medium/Low block time), kolik hráčů napadá a jak jsou agresivní po ztrátě míče. Detailně rozeber hru v jejich obranném bloku – jak jsou konzistentní, kudy vést útok, kdo propadá v duelech (např. překonání driblinkem/náběhem) a zda hrát spíše do nohy nebo za obranu. Také které hráče je nejlepší napadat a proč
		6. **Chování ve vlastním pokutovém území:** Jsou silní ve vzduchu, po zemi, mají problémy s centry, nebo naopak s průniky? (Vyvozeno ze všech dostupných defenzivních metrik).
		7. **Upozornění a doporučení (Taktická syntéza):** Co se na základě vzájemné analýzy zjistilo a stojí za to si říct. **Kritický bod:** AI zde musí dávat informace tvrdě do kontextu našich hráčů proti jejich. (Příklad: *„Soupeř má extrémně rychlého levého útočníka s obrovským objemem náběhů za obranu, zatímco náš pravý stoper má nízkou maximální rychlost. Doporučení: pravá strana naší obrany musí hrát v hlubším bloku a nelákat soupeře k náběhům.“*) Využívej pro hru maximálně přenositelné, věcné informace a vyvaruj se protichůdným tvrzením.
	1. Analýza jednotlivých hráčů: 
	- **Detailní profil hráčů soupeře:** Charakteristika všech dostupných hráčů soupeře - s označením hráčů, které považuješ za klíčové. U každého zhodnoť: Silné stránky (co u něj hrozí), Slabé stránky (čeho využít), jeho charakteristickou hru a fyzická specifika (např. extrémní maximální rychlost PSV-99 nebo agilita).
	1. **Chatovací okno** - musím mít možnost na základě dostupných dat pokládat doplňující otázky a získávat další informace. Odpovědi pak musím mít možnost označit. Označené odpovědi zakomponuješ do finálního reportu. 
- Finální report musí být možné sdílet přes odkaz a otevřít i v jiném počítači 
- Finální report musí být možné vyexportovat do PDF 
- Finální report je nutné mít možnost si přepínat do různých jazykových verzí: český jazyk, anglický jazyk, španělský jazyk a polský jazyk

1. **Archiv** - všech vytvořených reportů - musím mít možnost zpětně vytvořený report shlédnout, poslat a vyexportovat 

Všechny tyto informace které jsi dostal rovnou přidej do metadat, stejně tak si vytvoř svůj vlastní soubor, jakou logiku používáš při analýze dat. Pro svou analýzu používej vždy nejnovějšího verze AI s hlubokým kontextuálním myšlením. 



# Dodělávky
Dodělávky: 
- Rozdělit report na dvě části - detailní analýza (ten, co máme nyní)
- Pro každý tento report udělat samostatný insight report - tam bude vytaženo jen to nejdůležitější z celého detailního reportu, doporučení jak soupeře porazit, na co si dát pozor - a upozornění na ty nejdůležitější hráče
- Pokud používat názvy tak ne pomocí kódů offballrun_count_dangerous  ale dát tomu nějaký název nebo popis, co to přesně znamená
- Pokud používat čísla, tak naprosto jednoznačně a srozumitelně 
- To co je důležité to jsou vždy ty souhrny na začátků jednotlivých odstavců, tak udělat výraznější a ta klíčová zjištění udělat méně výrazné, ale přesto naprosto čitelné
- Rozmezí dat od kdy do kdy chci dělat analýzu (pro sigmu dohrát data celé minulé sezony?)
- Přejmenovat analýza na Zápasová strategie
- Udělat report pozápasová analýza - rozepsat prompt a hlavně doplnit možnost vložit hlavní strategické kroky které jsme do zápasu měli 
- Udělat analýzu hráčů - pro jednotlivá utkání (jak odehrál vzhledem ke svému obvyklému výkonu s přihlédnutím k výkonu týmu), trend vývoje 
- Celkově upravit vizuálně export a výsledný report 
- Možnost nahrát loga týmu 
- Data vyhodnocovat maximálně v kontextu
- Mazání dat podle nahraného souboru (každý soubor má ID pokud chyba - řeknu smaž všechna data z tohoto souboru) 
- Musím mít možnost přepočítat data 

Myšlenky
- nahrát data všech týmů pro dané kolo? 
- Popřípadě domáhat data konkrétního hráče 
- Využít i na skauting v rámci české ligy, konkrétní ligy nebo hráče (vše ve vztahu k týmu a hráčů v něm), vzhledem k požadavkům na tým 
- Identifikace slabých míst ke stylu hry (s možností dopsat, co a jak chceme hrát) 
- Držet si průměrná data a top data na pozicích - srovnání + komentáře 
- Doladit standardky 
- Golmandska data a report 


Akutní dodělání
- Pokud se obnovuje verze musí být ale zálohovaná data a nové verzi být nahraná
- Pokud nahraji data musím mít možnost na základě tabulky historie nahrávání označit zdroj dat, která chci odstranit (použít v případě chybného nahrání)
- Potřebuji, aby jednoznačně bral v potaz Metadata - zdá se mi, že ve svých analýzách je nezohledňuje 
- Zisky míče - není možné usuzovat, že je slabinou, že se získá menší procento ve středu hřiště - pokud se neporovává celkový počet míčů a z toho zisků. Protože jen z procenta to nelze říct. Protože soupeři nemusí hrát středm, ale více po kraji, takže mají více zisků na kraji. Tento údaj je zcela zásadní brát v kontextu 
- Ještě více jít do prolnutí silných a slabých stránek obou týmů a hlavně hráčů na pozicích proti sobě. Je potřeba vytěživ více z toho, kde využít potenciál a kde eliminovat hrozby

# Rozvoj projektu

- Možnost vybraných dat vyexportovat
- Napojit Eye ball do skladu dat
- Najít souvislosti mezi daty