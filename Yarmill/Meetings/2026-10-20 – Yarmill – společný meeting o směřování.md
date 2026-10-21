---
typ: meeting
datum: 2026-10-20
nazev: Yarmill – společný meeting o směřování
misto: společné setkání celého týmu Yarmillu (neformální, večer)
ucastnici: [celý tým Yarmillu – mimo jiné Danů, Tomáš (?), Tonda (?), Anička/Aniška, Adam, Honza, Aleš, Oskárek]
oblast: Yarmill
temata: [produktové směřování, roadmapa, AI, Yollanda, čísla firmy, fotbal, Sigma, centralizace svazů, diskrétnost, proaktivní upozornění, marketing, Instagram, B2C, integrace, data sportovců a soukromí]
tags: [meeting, yarmill, produkt, strategie]
otevrene_body: 9
ukoly: 9
prepis: "[[LLM Wiki/raw/Přepisy/2026-10-20 – Yarmill – společný meeting o směřování (přepis)|2026-10-20 – Yarmill – společný meeting o směřování (přepis)]]"
---

# Yarmill – společný meeting o směřování

> [!summary] Shrnutí
> Společné setkání celého Yarmillu, které mělo otevřít „poločasové review“ produktového směřování: jaké mají být mantinely, co v Yarmillu ve střednědobém horizontu dělat a co ne, a jak se postavit k tomu, co se teď děje s AI. Detailní debatu o roadmapě si pak vezme produktový tým (hlavně Aniška), tady šlo o volný brainstorm. Zazněla čísla firmy (ARR zhruba 8,4 mil. Kč z licencí, útrata za AI stoupla z ~3 tis. na ~37–38 tis. Kč měsíčně, Sigma je po ~10 měsících 6. největší klient all-time). Danů popsal, jak funguje Sigma (Yarmill jako jediná datová páteř, ~300 aktivních uživatelů, ale jeho model „člověka v klubu“ nejde škálovat). Hlavní produktové linie: trenéři chtějí, aby systém **hlídal za ně** (proaktivní upozornění, personalizovaná úvodní stránka), Yollanda má umět **výstupy** (PDF, PowerPoint, Excel) a Yarmill se má stát **hubem**, do kterého si „kutilové“ s AI posílají data (MCP, vstup i výstup). Ostrá debata byla o marketingu a Instagramu (sdílitelná fialová mapa aktivity, nedotažená spolupráce s externisty) a o B2C pro hobby sportovce (spíš ne, mezikrok přes kluby a hotové sportovní instance). Druhá nahrávka zachytila večerní debatu o tom, jak nebýt nástrojem dohledu nad sportovci (alkohol, spánek, odpojené hodinky).

## Kontext a cíl
- Úvodní slovo (pravděpodobně Tomáš [?]): s Aniškou chystají **poločasové review produktového směřování** – mantinely, co chceme a nechceme dělat. Krok zpátky už se to rýsovalo, pak to odložili jako samostatný projekt, aby „nebyli zaháčkovaní a neskákali na všechno“.
- Spouštěč: „teď se toho děje hrozně moc s AI“ – je čas zreflektovat, jestli roadmapu lehce upravit, nebo na ni mít aspoň názor.
- Detail se bude řešit v produktovém týmu, tady jen společné „plácání“: co kdo vidí, co používá jinde, na co si dát pozor.
- Do debaty zahrnout zkušenosti: **Zbrojovka skončila**, fotbal (Viktoria Plzeň – hrozně moc úsilí, podpora od Danů, Vaška, Kryštofa a dalších), **svazy a centralizace** (svaz plavání = ~6 000 lidí, stovky klubů, není reálné, aby svaz řekl „všichni budete používat Yarmill“).

## Účastníci
- Celý tým Yarmillu. Z přepisu jsou jasně slyšet: **Danů** (Sigma), **Tomáš (?)** – vedení, otevírá debatu a čte čísla, **Aniška/Anička** – produkt, **Tonda (?)** – vedení, pro něj je marketing „citlivá věc“, **Adam**, **Honza** (data z hodinek, backend), **Aleš** (zobrazení, frontend), **Oskárek** (Instagram), zmíněni externisté **Kýbl** a **Anet** (marketing).
- Kdo přesně co říkal, z přepisu často nejde poznat. Atribuce s (?) prosím zkontroluj.

## Průběh po tématech

### Fun facts: čísla firmy
- **Útrata za AI** (API + účty: ChatGPT, Claude, Gemini, API Yollandy):
  - leden 2026: ~3 000 Kč měsíčně (rok předtím skoro žádné účty, možná jeden ChatGPT),
  - červen 2026: ~16 000 Kč,
  - září 2026: ~37–38 000 Kč měsíčně (včetně Gemini).
  - Nezdražilo se to výrazně. Narostly hlavně vlastní účty (Claude) a API Yollandy, kterou klienti používají „jako dost“. „To je dobře, neříkám, že je to něco špatného.“
- **Klienti:** 32 platících svazů (?), 110 (?) – číslo uživatelů/instancí z přepisu nejde jednoznačně přečíst. Bez parasportu je to **19 různých sportů**. Nejvíc uživatelů mají plavci.
- **9 zemí:** Česko, Slovensko, Rakousko, Švýcarsko, Itálie (zatím demo instance), Polsko, Lotyšsko, Británie, Kanada (biatlon).
- **Top klienti podle revenue all-time:**
  1. Svaz lyžařů ČR – ~8 mil. Kč (víc, „než je za Teslu“),
  2. plavání – ~6,6 mil. Kč,
  3. Dukla,
  4. biatlon (od začátku speciální režim),
  5. (?) – zmíněn „Horosvaz“,
  6. **Sigma** – za ~10 měsíců (od léta). „To je dobrý.“
  - Docela dobrý je i **jachting**.
- **Dukla:** od letoška nová **rámcová smlouva na 4 roky** (vysoutěžená rámcovka, čerpají podle počtu licencí). Obnovuje se s každým ASO. Historicky někteří klienti chtěli, ať si Yarmill sežene druhou/třetí nabídku do soutěže – to tým odmítá („Nechápu, že by si to někdo risknul“).
- **Cenotvorba:**
  - plavání a lyžování mají kvůli počtu licencí **flat fee** (účtování bylo složité a stejně se dělaly velké ústupky),
  - ostatní se postupně převádí z **2 500 Kč bez DPH** (a 1 000 Kč za U15) na jednotný model **3 000 Kč za uživatele a rok**. Kdo dostane nové vyúčtování, je o tom informován.
- **ARR:** zhruba **8,4 mil. Kč** – čistě licenční recurring revenue. Nejsou v tom implementační fáze (fotbal) ani platform fee.
- **Platform fee:** dnes 50 tisíc až několik milionů. 50 tis. za úplně easy instanci, víc ve chvíli, kdy fotbal má Catapult, VALD, InBody a tráví se spousta času na specifickém setupu. Fotbaly začínají jako projekt (implementační fáze) a pak přecházejí na licence (akademie, A-tým…).
- Dotaz, jestli se drží poměr „největší zákazník vs. nejvíc spáleného času“: nevíme. Příklad **Kanada (biatlon)** – vzala docela dost času (menší věci furt dokola), ale je to semínko: z Alberty se to rozšířilo na celý kanadský biatlonový svaz a teď o tom říkají běžcům na lyžích a dalším. Zahraniční klient je na začátku jako „Taylor“ (?) – víc času.

### Novinek je tolik, že je nestíháme komunikovat
- Produktově se toho dělá hrozně moc nového, „až tolik, že to ani nestíháme říkat těm lidem“.
- Řeší se to osobně: po Dukle chodí **každý týden zkouška s jedním ASO** (minulý týden atletika, tento vodní slalom, předtím střelci). Vždycky to skončí 2–3hodinovou ukázkou a debatou, a to se nejde do detailů. „Vždycky se totálně diví, co už všechno tam je.“
- Dosud se drželi kurzu: **fotbal** a **„zemní“ sporty**, kde jsou dlouho a dobří (lyžování, biatlon).
- **Biatlon** nově za poslední dva roky v Lotyšsku, Polsku, Kanadě, Británii, řeší se Španělsko, letos nově Slováci.
- **Fotbal:** „celé to odmakal Danů“ – dostali se tam, kde ovládá XPS, a teď podepsali Viktorii Plzeň. Náročné a těžké dealy.
- **Cyklistika:** VIF Cycling team – sportovní ředitel **Vojta Řepa** (sám závodil). Spousta lidí je nadšená z toho, co tam vzniká, hlavně z nového designu, Yollandy a **termínovky** („začíná se mi plnit termínovka“ – to tým těší, „a přitom taková blbost“). Podobná reakce od atletů (zmíněn Holuša) i z Kanady.

### Příběh: trenér Janča Jilavský (?)
- Starý trenér z Jablonce, přes 80 let, pořád točí techniku pro biatlonovou a lyžařskou reprezentaci, platí za metodika, od něj se přebíraly tréninkové deníky („brutální Excel“). Každý rok volá.
- Teď chtěl podklady na prezentaci a pak napsal: „Díky za videa. Děláte fantastický projekt. Jako starý matador smekám. Držím palce.“ Ocenění i od „takového kmeta“.

### Danů: jak funguje Sigma
- **Yarmill je na Sigmě skutečně datová páteř a jediné místo pro data.** Kromě ukládání souborů se data nikam jinam nedávají a nikdo si netvoří nic svého. Je to i tím, že to Danů „úplně nedovolí“.
- **Role se otočila:** původně se plánovala pozice „supportu“, ve skutečnosti je Danů v hierarchii mezi šéfy sekcí pod nejvyšším managementem (předseda představenstva, sportovní ředitel). Minulý týden byl na třídenním semináři v Beskydech s top managementem. Oficiálně to nikde není, ale když se řeší data, vystupuje za klub on.
  - V Plzni se fáze probírají s klubem. Na Sigmě Danů řekne, co se bude dělat, a jen to představí vedení, které podepisuje faktury.
  - Danůmu to vyhovuje a myslí si, že to pomáhá zabudovat Yarmill jako běžnou součást.
- **Kdo Yarmill používá:** trenéři od U9 po A-tým. U14 a U15 hodně pracují v XPS (návaznost na svaz). Celý dorost od U16 po A-tým pravidelně plánuje a „jedou úplně ve všem“.
- **Směřování:** jednou přes Yarmill identifikovat talenty, predikovat, kteří hráči mají největší potenciál, a sledovat jejich cestu.
- **Odpor:** za celou dobu se nesetkal s tím, že by někdo řekl „sere mě to“ (na rozdíl od Pardubic a jinde). Je tam jeden „rejpal“, ale i ten to dělá. Klíčové je, že to jde **z nejvyšších míst** – „tohle je naše cesta“.
- **Limity lidí:** Danův velký cíl je, aby se primárně pracovalo s **Yollandou** a lidé se ptali v souvislostech (plány, testy, hodnocení hráčů). Tady naráží na velké limity.
- **Management se učí:** pondělní hodnoticí porady, souhrny ze zápasů. I předseda představenstva leze do Yarmillu a má přehled o datech.
- **Beskydy a FIFA projekt:** Sigma je v projektu FIFA (herní tvář Sigmy, individuální rozvojové plány hráčů). Danů na semináři reagoval „pojďme se podívat do Yarmillu“ a ukazoval věci v Yollandě – líbilo se to. Ale řešil se třeba kariérní plán hráče a vedení si ho malovalo v PowerPointu. Danů musí být u toho a říct: „To nebude v PowerPointu, to bude u nás v Yarmillu pro všechny. Pak si s tím dělejte, co chcete.“ Takových situací bylo za tři dny „X“.
- **Údržba:** jednou měsíčně sedí s jednotlivými realizačními týmy (2–4 lidi). Stojí to spoustu sil, ale nese to ovoce. Sere ho, že musí lidi kontrolovat – to má dělat šéf a trenéři.
- **Čísla:** odhadem **~300 aktivních uživatelů**, hráči od U14 po A-tým, přípravky zatím ne.
- **Byznys:** „vydělá to další peníze“, v dalších fázích se bude pokračovat a navyšovat.
- **Danův týden:** 2 dny přímo na Sigmě (jednu noc tam spí), 1 den dělá věci pro Sigmu z domu, 2 dny ostatní projekty. V neděli plánuje týden, ale Sigma ohlašuje porady na poslední chvíli a on u nich chce být (aspoň online), „nesmí si to nechat utéct“.
- **Smlouva:** Danů je 100% zaměstnanec Yarmillu. Sigma má smluvně slíbené 3 dny jeho času, ale **platí 2** – třetí den je práce, kterou by Yarmill dodával stejně (konfigurace). „Vždycky se nám vyplatilo být s nimi fér.“
- **Neškálovatelnost:** nemůžeme mít s každým fotbalovým klubem dalšího Danů. Potřebujeme se z toho naučit, udělat **„yarmillovský balíček pro fotbal“** a na straně klubu mít **championa**, který si to vezme za své, sám chce mít vše v Yarmillu a bude to vysvětlovat. Jinak by to znamenalo další a další lidi do klubů, což zatím nechceme.

### Biatlon jako srovnání
- Biatlon platí kontinuálně, je mezi největšími a navíc platí **analytické služby měsíčně** za dedikovaný čas. Tomáš (?) tam nikdy nebyl tak intenzivně jako Danů na Sigmě, takže to trvalo mnohem déle – dlouhé roky se dělo spoustu věcí mimo Yarmill.
- Teď je čeká **překlopení kontrolních testů SCM**, které jsou pořád v Excelu (podobně u lyžařů).
- Dnes už ale většina lidí sama tlačí, aby nové věci byly v Yarmillu. Příklad: **Michal** (trenér v SCM Jilemnice): „Než dostanu z laborky laktátovky, utečou tři měsíce. Pak už je to pro mě obsolete. Chci to v Yarmillu a co nejdřív.“
- Závěr: jsme B2B, ale nemůžeme mít v každém svazu/klubu „jednoho z nás“. Ve **velkých svazech** se champion na úrovni svazu nedostane přes SCM do klubů → zůstává problém centralizace.

### Diskrétnost: Danů vidí do Plzně i Sigmy
- Otázka od kolegy: není bizarní, že Danů komunikuje s Plzní, když je vidět, že sedí na Sigmě? Jsou to přímí konkurenti o 2.–3. místo.
- Danů: jediný smluvní vztah má s Yarmillem, má podepsané **NDA** a „je to pro mě svaté“.
- Řeší se to i jinde: biatlon (jiné národy vidí lidi Yarmillu v oblečení české repre na Světových pohárech, Lotyš se bál, aby to neukázali Čechům), judo (slovenské i české).
- I proto šli za horších podmínek do zahraničí (Polsko) – zbavit se nálepky „nástroj pro český sport“.
- Vyžaduje to **osobní kázeň** – přešlap nebo prozrazení by stálo reputaci. Svazy se hodně ptají na bezpečnost dat (přitom jim vše teče přes Garmin a Google Drive a nečetli podmínky), ale Yarmill klidně pomluví.
- **Zbrojovka** opakovaně tvrdila, že za její peníze něco používá Sigma. Odpověď od začátku otevřeně: ano, přišli k mnoha věcem, které nezaplatili oni, do Yarmillu už byly investovány desítky milionů a oni do toho nepřispěli. Princip: **„absolutně čisté svědomí v tom, co a jak děláme“**.
- Konec Zbrojovky: po tom, co řekli, že to lidi nepoužívají, jim Yarmill na třikrát prodlužoval instanci o 2 měsíce, protože v ní fungovali. „Nezneužili jsme toho.“

### Postoj k fotbalu
- Kolega (?): vadí mu, že pro nás jsou fotbalisti automaticky „čuráci“. Fotbal nás v určité chvíli podržel, nalil do nás peníze, a o malém svazu s 10 uživateli mluvíme hezky.
- Reakce: fotbal jsme si vybrali jako jeden z pilířů. Navenek se říká: „Nejsem fanoušek fotbalu, ale dneska jsou v Yarmillu a jsou super“ – je to fenomén, který nemá žádný jiný sport. V mnohém je funkčnější než svazy (jsou tam lidi zodpovědní, na Dukle je člověk „nevyhoditelný“).
- Ale realita: změní lidi a neřeknou to, klub vlastněný nejbohatším Čechem (Plzeň) má **80 dní po splatnosti obě faktury za první fázi**.
- Fotbal táhne vývoj: **VALD, Catapult, profil hráče** – použije se všude a ostatní sporty se inspirují.
- Návštěva Slavie (?): slušní lidé, ženský fotbal, milé.

### Danů: co by produktově pomohlo nejvíc
- **Plně funkční karta hráče.** Dvě cesty: plzeňská (karta hráče je primární, protože do dat tolik nevstupují) a sigmácká (nejdřív plnit data a z nich dojít ke kartě v plné funkčnosti jako „první vrchol“).
- Kdyby mohl, věnoval by se **scoutingu** – chtělo by to týdny až měsíce intenzivní práce, řeší se to na jiné úrovni než report nebo výpočet.
- **Patrik Kmínek** (šéf úseku kondice a zdraví) zná Yarmill déle než Danů (jezdil s Pepou Andrlem). Kondičáci jsou páteř a od začátku jeli na 100 %, Danů se o ně mohl opřít.
- **Konkrétní bolesti:**
  - hodnocení zápasu: překlikávání z hráče na hráče, opakované vyplňování data, kategorie atd. – ozývá se opakovaně,
  - dotazy hlavně kolem Yollandy (např. VALD),
  - **fyzio screening:** chtěli hromadný export výsledků, aby rozdělili hráče do skupin. Místo exportu řekli Yollandě, ať je rozdělí podle nálezů – „perfektní“ (zadní řetězec atd.),
  - kondičáci mají nápady na propojení plánování s metodikou a rutinou.
- **Výstupy:** dnes Danů často nechá výstup převést do PDF přes Claude. Nápad: aby Yollanda uměla **„a teď mi z toho udělej prezentaci“** (téma spíš pro Adama). Dnes Yollanda neumí vyplivnout Excel ani PDF.
- **Uložené pohledy:** lidé si s Yollandou definují vlastní pohledy na data. Trenér parahokejistů si udělal vlastní ranní check (klidová tepovka, kdo nemá vyplněný Yarmill za předchozí den). Chtějí to buď ven (PDF, PowerPoint, Excel), nebo uložit a dívat se opakovaně bez nového ptaní.

### Opakované produktové požadavky z terénu
- **Kartotéka:** realizační tým a role (doktor, masér).
- **Termínovka:** kdo z realizáku jede na soustředění, aby to sportovci věděli.
- **Notifikace** sportovcům při změně plánu.
- **Fyzio komentáře:** řadit opačně (nejnovější nahoře), **skrýt** některé komentáře (subjektivní pocit sportovce může vidět, objektivní hodnocení fyzia jen fyzio – sportovce to znervózňuje).
- **Sportovci mají určovat, kdo co vidí.** Obava, kdo vidí na data, blokuje sdílení. Příklad: **Kuba Koula** (slopestyle instance) nemá propojené hodinky, protože neví, kdo na ně vidí („viděl by, že jsem spal se svou holkou a proto jsem čilý ve dvě ráno“).
- **Kanada:** závodnice se samy ptají na prostor pro **informace o menstruačním cyklu** – ale zase: kdo to uvidí? Mechanismus zatím není.
- S každým modulem (medical, wellness dotazník…) přibývají další nápady. Termínovka „dělá hrozně moc muziky“.

### AI: hrozba, nebo příležitost?
- Hlavní motivátor debaty: **nestaneme se za tři měsíce obsolete**, když přijde Claude a trenéři si začnou dělat věci sami? Čím dál víc trenérů, i neprogramátorů, má pocit, že zvládnou cokoliv.
- Příklady: trenéři si dělají boardy v Claude nebo ChatGPT nad daty (hodí tam Excel z testování nebo PDF z InBody a dostanou interpretaci). Jen v biatlonu jsou **tři lidé, kteří dělají appku na záznam střelby**, žádný není programátor (zmíněn Boušek, kluk z Letohradu, trenér z Nového Města).
- Starší fenomén „**kutilů**“: bývalý závodník s IT vzděláním, který svazu zadarmo něco udělá. Pár svazů se tím už spálilo – vždycky to definitivně selhalo, když člověk odešel nebo neměl čas. Teď jsou kutilové posílení AI a je jich víc, na vstupu i na výstupu.
- **Advanced users** (chtějí měnit filtry v analýzách, vlastní pohledy): je jich málo, ale jsou hlasití a často sedí na schůzkách, které rozhodují o tom, jestli tam Yarmill bude.
- Slovensko: lidé zvyklí na vlastní nástroj dávají jiným přihlašovací údaje do Yarmillu, ať jim to tam vyplní.
- **Shoda: není to hrozba.** Kutilové neudělají řešení, které integruje 20 zařízení, chybí bezpečnost, funguje to na jeden use case a pak se to rozpadne. Ale je to **příležitost**:
  - pustit advanced uživatele k datům přes **MCP**, ať si analýzy dělají sami,
  - na vstupu přijímat data z jejich appek – nedělat modul na každou věc každého sportu (freestyle lyžování chce appku na čtení triků z videa, plavání vlastní analýzy). Boušek má na starosti 4 lidi v A-týmu, trenér v SCM 15 – každý potřebuje jinou appku. „Ať si ji udělají a pošlou data k nám.“ Fabian Štoček (laboratoř SKP) ať si vymýšlí, co chce, a důležité věci pošle k nám.
  - Yarmill jako **hub**, kde se data sbíhají.
- **Ztratili jsme výhodu flexibility:** dřív jsme byli rychlejší než rigidní velká řešení. Dnes má trenér za 3 minuty dashboard s interpretací a za 10 minut klikací prototyp. Tak flexibilní nejsme. Je potřeba si říct, kde bude naše místo, a nebýt „zapšklí“ („vy nás nikdy nenahradíte“).
- **Adam z Londýna** (Glyfik / Airspeed ?) řeší totéž: lidé s AI chtějí MCP a myslí si, že si všechno udělají sami. Ale ve firmě 50 % lidí AI nepoužívá. Stejně je to s trenéry na Sigmě.
- Většina trenérů **nemá nápady**, co se ptát. Když jim insight naservíruješ („podívejte, jak trénuje, jak spí“), zkonzumují ho. To je pořád naše výhoda.
- **Chytrá AI uvnitř modulů:** silné moduly (termínovku si v Claude nikdo neudělá) udělat chytřejší. Inspirace **Linear**: nahraješ video a samo se rozdělí do popsaných sekcí, změna 6 bodů v popisu projektu přijde jako notifikace shrnutá do jedné věty. Plánování s AI v Yarmillu bude lepší než v Claude, protože je v ekosystému (sportovci to hned vidí a pracují s tím), zatímco z Claude to skončí v PDF.

### Komplexní pohled a proaktivní systém
- Opakovaně slyšeno (2× za 14 dní): máme analýzu zatížení, regenerace, wellness, závodních výsledků – **ale kde je komplexní pohled?** Trenér se každý den rozhoduje, co se sportovcem dělat, jestli sedí plán, nebo něco změnit, aby se nezranil.
- Trenéři chtějí, **aby to hlídalo za ně**, protože nevědí, na co se ptát. Trenér vícebojařů (Hamutý ?): „Potřebuju, aby to Yollanda hlídala za mě.“ Podobně Dušan Živek (?).
- **Případ zraněného hráče A-týmu Sigmy:** fyzio a performance kouč Patrik měli podezření, že byl málo zatěžovaný (vymlouval se z tréninků), a přesto chodil do zápasů. Prasklý křížák (?) – mohlo to souviset? Popsali to Yollandě, ta začala hloubat a zjistilo se, že **nenosil Whoop**. Signály tam byly. Dnes by se na Sigmě u hráče, který nosí Whoop, daly najít paterny (VALD několikrát týdně – asymetrie, síla v nohách; oslabená část těla mohla v souboji hrát roli). Yollanda zatím **nevidí GPS**. Vina je i na kondičácích, že Whoop neměl, i když ho má a platí se.
- **Případ talenta, který chodí spát ve 2 ráno:** najednou chodil v 10–11. Změnil se, nebo nosí Whoop někdo jiný? Yollanda podle HRV a klidové tepovky řekla, že nevykazuje známky, že by Whoop nosil někdo jiný.
- **Riziko přístupů:** předseda představenstva vidí všechno, je analytický a může se zeptat, kdy hráč šel spát. Hrozí, že v emocích řekne „vidím, že chodíš kalit, vidím, že jsi tlustý“. Patrik se s tím v A-týmu bojí: jakmile to hráči zjistí, přestanou nosit. Příklad: předseda řešil kluka z B-týmu s 15–16 % tuku. „Je to hodně o lidech a kultuře.“
- **Whoop ukázal nemoc 2 dny dopředu** (jiná porada, hráč se střevními potížemi) – trenér by tu informaci chtěl mít. To slyšíme od mnoha lidí.
- **Návrh feature:** upozornění jako Oura („trošku se ti tady změnilo“) – u nás složitější, ale super. Mohla by to být **úvodní stránka / landing page** s nejdůležitějším souhrnem abnormalit, **personalizovatelná**. Pravidla: část od nás (naše znalost a zkušenost), část si nadefinují trenéři („každé ráno chci čeknout tohle“). Inspirace: Linear inbox. „Taková asistentka, která hlídá za tebe.“
- Systém musí být **proaktivní**, lidé jsou reaktivní. Jarmil a Yollanda mají dělat věci na pozadí, ne jen chatovátko, kde se máš ptát. Řada lidí neumí otázky klást, nejsou analyticky nastavení – když dostanou první insight, chytnou se.

### Marketing, Instagram a sdílitelná mapa
- Návrh (?): chceme být **vidět mezi sportovci**, aby i kutilové s vlastní appkou na střelbu měli tendenci cpát data do Yarmillu a aby nás sportovci vnímali jako místo, kde se jejich sport děje.
- **Sdílitelná mapa aktivity** jako Strava: zkopíruješ mapu do Instagram story, jen fialová a s logem Yarmillu. Bude to „něco jiného, co nikdo jiný nemá“ (zmíněn „Polymer“ ? – kdo ho má, vypadá cool). Sportovci si začnou psát „ty máš taky Yarmill?“ (plavec s biatlonistou). Dá platformě tvář. Potřeba připravit formáty pro sdílení (víc variant, jako Strava share).
  - Stav: mapa je **ready**, Honza musí pustit víc dat z hodinek a Aleš je zobrazí. Honza: „Mapa nestojí na mě, já mám data… ale odkládám to.“
- **Promo video / výstup z klubu** (Sigma, Plzeň by k tomu byly ochotné): ukázat, jak to v klubu žije. Lidi říkají, že web je super, ale na sítích nás nenajdou. Organické sdílení. Pocit, že „máme strach to ukázat“.
- **Napětí kolem Instagramu:**
  - Tonda (?) to vnímá jako extrémně citlivé, protože to bude vidět nejvíc.
  - Proběhly první pokusy s Oskárkem a Aniškou, poslední příspěvky po dvou feedbackových kolech už byly podle zastánce (?) super.
  - Externisté **Kýbl a Anet** se na to „vysrali“, Kýbl se neozval, Anet se třikrát omluvila. Vedení pak přes noc sepsalo strategii samo.
  - Frustrace zastánce (?): „Řekne se, že na to není čas, a pak se dělají lahve a trička.“ Příklad: oslovená závodnice (dva Světové poháry, státnice) poslala fotky a za měsíc a půl se ptala, co bude – nic. Demotivující.
  - Odpověď vedení (?): na strategii Instagramu potřebuje **dvoudenní focus mód** s Claude (deep research nejlepších příkladů – Oatly, Ryanair), zatímco trička a bidony stojí půl hodiny, protože je řeší Anička s Oskárkem. „Není to omluva.“ Původně do toho nechtěl vůbec vstupovat, udělal se tým zodpovědných lidí.
  - Protiargument: ty jsi nám neřekl, co od toho čekáš. Zastánce netušil, že by to mohlo stát na něm.
  - **Návrh:** „Přimhuř oči a dej nám dva měsíce“ (s Aniškou a Oskárkem), pak to vyhodnotíme. Pravidelný obsah: v pondělí analýza zápasu Sigmy, odjetý Světový pohár.
  - Hlas k rovnováze: nebagatelizovat to, i za zdánlivě jednoduchým marketingem je strategie. Chyběl někdo se širším pohledem. Ale externistka se ptala „pro koho to je“ a my jsme to nebyli schopní říct.
  - Přirovnání s podcastem: rozhovor stojí na moderátorovi, komunikace na jiném (Šimba). „Lidi chtějí, aby to bylo jednou takhle, jednou takhle.“

### B2C a hobby sportovci
- Návrh: otevřít Yarmill částečně veřejnosti přes subscription, jako Strava. Tým **Petra Fialy** (trénuje Honzu Střechu ?, který dělá hlavní marketing) – všichni jedou na **TrainingPeaks**. Když budeme ready na zpracování wattů, „budou to srdcaři“, prodají to na Instagramu a YouTube. „Musíme na to být ready.“
- Protiargumenty: B2C je **úplně jiná disciplína**. Instance jsou přizpůsobené svazu, někdo tě musí pozvat, chybí self-onboarding a návody, mobilní appky jsou „dneska trapné“, sportovec si **sám nemůže plánovat**. To je rok práce, ne měsíc. 50–100 lidí tě nevytrhne. Příklad: firma se sedly – milion měsíčně do marketingu, 15 000 sedel venku. Hobbíci neradi platí: **Strava** má velký problém převádět lidi na placené licence, přestože má desítky až stovky milionů USD investic (Crunchbase).
- Hobbík, co by chtěl Yarmill, si to dnes udělá v Claude nebo mu stačí Garmin.
- **Mezikrok, který dává větší smysl:** pod svazem jsou kluby. Hotová instance pro sport (běžecká, cyklistická) pro klub, fitness coache nebo osobního trenéra – „tak jak je“, drobná změna za půl dne OK. Takhle můžeme mít desítky subjektů se základním setupem.

### Strava, integrace a „všechno na jednom místě“
- Kolegyně (?) nerada píše: udělá 4 print screeny ze Stravy, dá je Claude, ten to zapíše do Google Sheetu a podle toho plánuje. Nenapadlo ji, že by to mohl zapsat do Yarmillu → nápad: připojit Claude do Yarmillu (MCP), ať to zapíše sám.
- **Integrovat Stravu** – „super krok kupředu“ (Apple Watch nezaznamenávají, vše jede přes Stravu).
- Koupená **váha**, která není implementovaná.
- Kdo Yarmill používá déle, oceňuje **vše na jednom místě** (InBody v PDF, laktátové testy v Excelu, složky po sportovcích na Drivu, aktivity v Garminu/Polaru). Stejný příběh má Vojta z VIF. Oura/Whoop nemají týmové pohledy – to je naše výhoda.
- Ale bez integrace je to problém: tabulky musíme vytvářet my a jsou celoinstanční. Trenér s vlastní skupinou a vlastními testy si to v Yarmillu nevyřeší → hodí to do Claude.
- **Výsledky závodů:** kde je napojení (IBU, FIS), je to geniální. Jinde ruční vypisování jen svých závodníků. Tenis žádná data nedá, mezinárodní střelecká federace žádná nemá, jachting (?) podobně, freestyle taky ne – ale PDF výsledků existují. **Příležitost: nahraj PDF a AI ho přečte.** Rakouští snowboardisté si parsování nastavili a je skvělé, lyžaři ho nepoužili vůbec (řeší se s novým trenérem Vojtou).

### Informování o novinkách (newsletter)
- Instagram má být hlavně pro sportovce. Pro trenéry **newsletter** jednou za 14 dní / měsíc, nebo když se nasbírá dost novinek.
- Produktově se chystá: **announcementy** v aplikaci, **changelog** v nové dokumentaci a totéž e-mailem, vše provázané.
- Skepse: announcement většina lidí zavře. Funguje to u Linearu (jedna velká věc) a Stravy (obrázky), ale „čtou to jen ti, které to zajímá“.

### XPS a plánování ve fotbale
- Největší kámen úrazu: ve fotbale mluví o plánování, ale v XPS neplánují – **kreslí trénink**. „To v Yarmillu není.“ XPS je dobré na týmové sporty směrem ke sportovci (sdílení videa, dotazníky).
- Pro ně plánování = napsat si trénink na zítra a nakreslit obrázky. Nechápou, že plánuješ, abys zpětně viděl výsledek.
- **Plán vs. skutečnost** nepoužívají ani v Yarmillu. Ale nad plánem se už umí zeptat. Na Sigmě skutečnost slouží hlavně k tomu, aby hráč zapsal, co dělal na tréninku a regeneraci.

### Večer: data sportovců, alkohol a důvěra (nahrávka „Alešova“)
- Příklad: ráno přijde alert a trenér pošle sportovce domů → zabránil zranění. „Jsme na hrozně tenké hraně“ – chceme být appka, která je u sportovce v jeho výkonu, ne nástroj, který ho potápí.
- Sportovci si **nepropojují hodinky** (Whoop/Oura), aby trenér nevěděl, že pili. Vysvětlení sportovcům: buď to tam nedáš, trenér to neuvidí, půjdeš těžký trénink a dopadne to špatně (zranění, nemoc). Nebo to přiznáš a trenér má říct: „Jdi domů, dneska to nemá cenu.“ Trenér to ale musí brát s nadhledem.
- Odhad: takhle férově nastavené vztahy jsou v **10–15 %** případů. Riziko, že se staneme nástrojem, který lidi vyhazuje ze systému. Opačný extrém: „když přijde na trénink, rovnou mu objedná záchranku“.
- Starý fotbal (příklad Borise Řabky ?, „Slovák píču chlastáš, píču hraješ“) vs. dnešní intenzita – dnešní hráč si to dovolit nemůže. Hokej je na tom „ještě furt trošku“ jinak.
- „Už teď jsme nástroj, který ho potápí v tom, že to musí vyplňovat.“ Bojíme se, že nás sportovci začnou ještě víc nenávidět a hodinky si budou odpojovat.
- Protiargument: kolik stojí hráč A-týmu a jeho zranění – u A-týmu je to jasné. Ale první uživatelé jsou **sportovci SCM**. U nich řekne „dneska netrénuj“ jeden trenér z dvaceti, ostatní mu řeknou, že končí.
- Příklad: o 17letém hráči jsme věděli, že má třikrát týdně „dancing“ (?) do dvou do rána.
- Vtip o „vyšším manažerovi“ s jedinou smlouvou s Yarmillem, služebním autem atd.
- Příklad z vlastních dat: po víkendu na horském školení **HRV 25** → „anomaly detection“.
- Dodatek z hlavní nahrávky: v Letohradu jsme to zkoušeli obejít, sportovci se bojí, ale tlak trenérů je tam větší, takže budou nosit. Kdo to chce obcházet, obejde to a se SCM skončí se sportem. Kdo ne (příklad **Matyáš Bauer** – nejvíc tréninků v Yarmillu: 6 371 záznamů, ~17 mil. tréninkových jednotek (?), ~50 000 km), ten se o Yarmill opře. Apple zavedl periodický safety check „kdo vidí tvoje health data“ – inspirace.

## ✅ Rozhodnuto
- **Detailní review roadmapy si vezme produktový tým** (Aniška a vedení). Dnešní setkání byl jen otevřený brainstorm.
- **Shoda, že AI není hrozba, ale příležitost** – směr hub (vstup i výstup dat, MCP) a chytrá AI uvnitř modulů, ne modul na každou specialitu každého sportu.
- **Model „člověka v klubu“ (Danů na Sigmě) se nebude replikovat** – cílem je balíček pro fotbal a champion na straně klubu.
- Princip **diskrétnosti a čistého svědomí** platí dál (NDA, žádné informace mezi klienty).

## ❓ Nerozhodnuto / k dalšímu řešení
- **Jak má vypadat roadmapa a mantinely** – co dělat a co ne v příštím období.
- **Kde se ukotvit v AI světě:** MCP pro advanced uživatele? Jak přijímat data z kutilských appek?
- **Proaktivní upozornění / personalizovaná úvodní stránka:** jak to uchopit („vůbec si nedokážu představit, jak bychom to měli uchopit“).
- **Výstupy z Yollandy** (PDF, prezentace, Excel) a ukládání vlastních pohledů.
- **Řízení přístupů ke sportovcovým datům** (kdo co vidí, skryté komentáře, menstruační cyklus).
- **Marketing a Instagram:** dostane tým (Aniška, Oskárek, zastánce) dva měsíce volnou ruku? Kdo za to zodpovídá a co se od toho čeká?
- **Sdílitelná mapa aktivity** – kdy ji Honza a Aleš dotáhnou.
- **B2C vs. hotové instance pro kluby a trenéry** – spíš mezikrok přes kluby, ale bez závěru.
- **Jak řešit centralizaci velkých svazů** (champion se nedostane do klubů).

## ⚔️ Rozpory v názorech
### Marketing a Instagram
- **Zastánce (?):** nebát se ukázat, dát týmu dva měsíce, sdílitelná mapa a pravidelný obsah (analýza zápasu Sigmy). Vadí mu „není čas, ale na trička je“.
- **Vedení (Tonda ?):** je to nejvíc viditelná a citlivá věc, externisté selhali, sám potřebuje čas na strategii.
- **Třetí hlas:** marketing nebagatelizovat, chybí strategie a jasná cílovka.
- **Jak to skončilo:** bez závěru, návrh „dva měsíce“ zůstal na stole.

### B2C pro hobby sportovce
- **Pro:** tým Petra Fialy, TrainingPeaks komunita, srdcaři, kteří to prodají na sítích.
- **Proti:** jiná disciplína, rok práce, hobbíci neplatí (Strava), chybí self-onboarding a mobilní appka.
- **Jak to skončilo:** spíš mezikrok – hotové sportovní instance pro kluby a trenéry.

### Vztah k fotbalu
- **Kritik (?):** přestat o fotbalistech mluvit jako o „kreténech“, fotbal nás podržel a přinesl peníze.
- **Druhá strana:** fotbal chceme dělat a navenek o něm mluvíme hezky, ale realita (nezaplacené faktury Plzně, změny lidí bez oznámení) je frustrující.

### Dohled nad sportovci
- **Strach:** staneme se nástrojem dohledu, sportovci nás budou nenávidět a odpojovat hodinky. Férově nastavených vztahů je jen 10–15 %.
- **Druhý pohled:** kdo to chce obcházet, stejně skončí, a seriózní sportovci (Bauer) se o Yarmill opřou. U A-týmu ve fotbale jde o velké peníze.

## 📋 Úkoly
> V přepisu nezazněly konkrétní úkoly s termíny. Níže jsou další kroky, které z debaty vyplynuly – zkontroluj, co z toho platí.

### Moje (Danů)
- [ ] Sepsat pro produktový tým zkušenosti ze Sigmy jako podklad k review roadmapy (karta hráče, hodnocení zápasu, fyzio, výstupy, proaktivní upozornění)
- [ ] Sepsat konkrétní bolest hodnocení zápasů (překlikávání hráčů, opakované datum a kategorie) jako produktový požadavek
- [ ] Popsat případy ze Sigmy (zraněný hráč bez Whoopu, talent a spánek, nemoc vidět 2 dny dopředu) jako use case pro proaktivní upozornění
- [ ] Navrhnout, jak by vypadal „balíček Yarmill pro fotbal“ a role championa na straně klubu
- [ ] Připravit podklady/data pro pravidelný post „analýza zápasu Sigmy“, pokud se marketing rozjede
### Ostatní
- [ ] Review produktového směřování a mantinelů – **produktový tým (Aniška)**
- [ ] Rozhodnout o dvouměsíčním „volném režimu“ pro Instagram – **vedení (Tonda ?)**
- [ ] Dotáhnout data z hodinek pro sdílitelnou mapu aktivity – **Honza**, zobrazení – **Aleš**
- [ ] Zvážit výstupy Yollandy (PDF, prezentace) – **Adam (?)**

## 📅 Termíny, čísla, fakta
- AI útrata: leden 2026 ~3 000 Kč/měs., červen ~16 000 Kč, září ~37–38 000 Kč (vč. Gemini)
- ARR (jen licence): ~8,4 mil. Kč
- Platform fee: 50 tis. Kč až několik milionů
- Nový cenový model: 3 000 Kč za uživatele a rok (dřív 2 500 Kč bez DPH, U15 1 000 Kč); plavání a lyžování flat fee
- 19 sportů (bez parasportu), 9 zemí, nejvíc uživatelů plavci; 32 (?) platících svazů
- Top revenue all-time: lyžování ~8 mil., plavání ~6,6 mil., Dukla, biatlon, (?), Sigma 6. za ~10 měsíců
- Dukla: rámcová smlouva na 4 roky (od letoška)
- Biatlon nově: Lotyšsko, Polsko, Kanada, Británie, Slovensko; jednání Španělsko
- Sigma: ~300 aktivních uživatelů, hráči U14–A-tým, trenéři U9–A-tým, smluvně 3 dny Danů, placené 2
- Plzeň: 80 dní po splatnosti obě faktury za první fázi
- Svaz plavání: ~6 000 lidí, stovky klubů
- Matyáš Bauer: 6 371 záznamů, ~50 000 km (?)

## 💡 Nápady a myšlenky k návratu
- **Proaktivní personalizovaná úvodní stránka** s anomáliemi (pravidla od nás + vlastní pravidla trenérů), inspirace Oura a Linear inbox
- **Yollanda: „udělej mi z toho prezentaci“**, export PDF/Excel/PowerPoint, ukládání vlastních pohledů a checků
- **MCP do Yarmillu** – advanced uživatelé si analýzy dělají sami, Claude zapisuje data (např. ze screenshotů Stravy)
- **Yarmill jako hub** pro data z kutilských appek (střelba, triky z videa, laboratoř)
- **Nahrání PDF s výsledky závodů a parsování AI** tam, kde není napojení
- **Sdílitelná fialová mapa aktivity** s logem Yarmillu pro Instagram story
- **Promo video z klubu** (Sigma, Plzeň), jak to tam žije
- **Hotové sportovní instance** (běh, cyklistika) pro kluby a osobní trenéry
- **Integrace Stravy** a dotažení váhy
- **Řízení viditelnosti dat sportovcem** + periodický „safety check“ po vzoru Apple
- **Newsletter pro trenéry** navázaný na changelog a announcementy

## ⚠️ Rizika, obavy, závislosti
- Rychlost AI: trenéři si udělají vlastní nástroje a Yarmill přestane být flexibilnější alternativou.
- Hlasití advanced uživatelé sedí na rozhodovacích schůzkách.
- Model „Danů v klubu“ neškáluje, bez championa klub nepojede.
- Centralizace velkých svazů – nedostaneme se do klubů.
- Únik informací mezi konkurenčními klienty by zničil reputaci.
- Zneužití dat vedením (předseda vidí vše) → sportovci přestanou nosit hodinky a sdílet.
- Fotbal: náročný na čas, pozdní platby, změny lidí bez oznámení.
- Novinek je víc, než stíháme komunikovat.

## 🔗 Souvislosti
- [[LLM Wiki/wiki/entity/Yarmill|Yarmill]] (wiki)
- [[LLM Wiki/wiki/entity/Yollanda|Yollanda]] (wiki)
- [[LLM Wiki/wiki/entity/SK Sigma Olomouc|SK Sigma Olomouc]] (wiki)
- [[LLM Wiki/wiki/entity/VIF Cycling team|VIF Cycling team]] (wiki)
- [[LLM Wiki/wiki/entity/Whoop|Whoop]], [[LLM Wiki/wiki/entity/VALD|VALD]], [[LLM Wiki/wiki/entity/InBody|InBody]] (wiki)
- [[SK Sigma Olomouc/Analytická témata/Karta hráče 🎯|Karta hráče 🎯]]
- [[SK Sigma Olomouc/Analytická témata/🔮 Yollanda insights|🔮 Yollanda insights]]
- [[SK Sigma Olomouc/Meetings/Sigma - Beskydy 10-2026/Finální souhrn|Beskydy – Finální souhrn]] (seminář v Beskydech, kariérní plány v PowerPointu)
- Lidé: Patrik Kmínek (Sigma, kondice a zdraví), Pepa Andrle, Vojta Řepa (VIF), Kuba Koula, Michal (SCM Jilemnice), Boušek, Fabian Štoček, Matyáš Bauer, Petr Fiala
- Kluby a instituce: Viktoria Plzeň, Zbrojovka Brno, Dukla, svaz lyžařů, svaz plavání, biatlon (CZ, Kanada…), XPS, Strava, TrainingPeaks, Oura, Linear

## 💬 Klíčové citace
- „Abychom nebyli zaháčkovaní a neskákali úplně na všechno a věděli, co chceme dělat a co ne.“
- „Vždycky se totálně diví, co už všechno tam je.“
- „To nebude v PowerPointu, to bude u nás v Yarmillu, pro všechny.“ (Danů)
- „Nemůžeme mít s každým dalším fotbalovým klubem dalšího Danů.“
- „Musíme mít absolutně čisté svědomí v tom, co a jak děláme.“
- „Ať si tu appku udělají a pošlou data k nám.“
- „Já potřebuju, aby to Yollanda hlídala za mě.“ (trenér vícebojařů)
- „Chceme být spíš opora tomu sportovci než nástroj, který ho potápí.“

## 🎯 Moje poznámky a doporučené další kroky
- *Návrh:* proaktivní upozornění a personalizovaná úvodní stránka jsou nejsilnější společný jmenovatel debaty (trenéři, Sigma, biatlon, atletika). Sigma může být pilot – má Whoop, VALD a pravidelné testy.
- *Návrh:* téma přístupů k datům sportovců (viditelnost, skryté komentáře, safety check) řešit dřív než proaktivní alerty – bez důvěry sportovci přestanou nosit hodinky a alerty nebudou mít data.
- *Návrh:* sepsat, co na Sigmě dělá Danů jako „champion“, jako šablonu pro fotbalový balíček (Plzeň a další).

## Nejasná místa v přepisu
- Kdo co říkal: úvodní slovo a čísla (Tomáš ?), marketing (Tonda ?, zastánce Instagramu ?), postoj k fotbalu (kritik ?)
- Čísla: „32 platících svazů“ a „110“ (uživatelé? instance?), pátý největší klient („Horosvaz“ ?), Bauerových „17 milionů“
- Jména: Janča Jilavský, Hamutý (trenér vícebojařů), Dušan Živek, Adam z Londýna (Glyfik / Airspeed), Honza Střecha, Boris Řabka, „Arbis“, „Taylor“, „Polymer“
- „Dancing / tensing“ u 17letého hráče
- Část nahrávky je soukromý hovor (jídlo, pití, cesta do Chomutova) – vynecháno
- „Alešova“ nahrávka je útržek večerní debaty, začátek chybí

## Přepis
Kompletní přepis: [[LLM Wiki/raw/Přepisy/2026-10-20 – Yarmill – společný meeting o směřování (přepis)|2026-10-20 – Yarmill – společný meeting o směřování (přepis)]]
