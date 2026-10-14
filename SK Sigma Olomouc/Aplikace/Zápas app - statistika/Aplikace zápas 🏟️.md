---
apple-notes-id: 5B32ED9E-AF90-4751-A985-D802486D3FF8
---
#app
Potřebuji vytvořit aplikaci, do které budu moc zaznamenávat statistiky z utkání přímo v průběhu utkání pouze pomocí klikání na tlačítka. Bude to jakýsi klikací panem, díky kterému se mi zaznamená počet předem stanovených metrik v průběhu utkání. Z toho celého se mi pak bude sestavovat report.

Aplikace bude složena ze třech částí

1. Záznam dat
- Úvodní stránka bude obsahovat 1. Tlačítko pro vytvoření nového utkání 2. Archiv, ve kterém budou zaznamenána veškerá data z minulých záznamu a utkání (musím mít databázi, do které se mohu vždy na své záznamy podívat)
- V prvním kroku pokud kliknu na “Nové utkání” je potřeba: 1. Vložit Datum utkání, 2. Vložit název domácího a hostujícího týmu včetně jejich loga (možnost nahrát logo ve formátu obrazku a z těchto obrázků se mi bude dělat databáze, ze které si vždy mohu vybrat logo v příštích záznamech), 3. Vybrat o jaký typ utkání se jedná (rozbalovací seznam) - liga, evropské poháry, domácí pohár, přípravné utkání 4. Zvolit si panel, který pro záznam použiju (mohu si vkládat různé panely - vždy musím určit jaká tlačítka bude obsahovat - jaké metriky budu zaznamenávat a na jaké pozici tlačítko chci)
- Následné se dostaneme do zaznamenávacího prostředí: 1. Potřebuji aby obsahovalo časomíru, kterou když spustím tak poběží čas utkání - současně ale musí být možné časomíru pozastavit, protože v poločase nechci, aby běžela ale v druhém poločase chci aby navázala (musí tak být možnost rozlišit 1. a 2. poločas) - a musí být tlačítko “zahájit druhý poločas) a tam začne čas opět běžet od 45. minuty   2. Zaznamenávání počtu vybraných metrik v průběhu zápasu - nutné je aby každé tlačítko pro danou metriku bylo jak pro domácí tak hostující tým - při kliknutí na tlačítko se zaznamená +1 pro danou metriku pro daný tým a to včetně záznamu času z časomíry v kolikáté minutě utkání k tomu došlo (musí být editovatelne pro případ že kliknu na špatne tlačítko). Také musí být možné ke konkrétnímu času a záznamu vložit poznámku
- Musí to vypadat úplně jednoduše jednoduchý panel na kterém budou tlačítka kterými já budu jen přidávat počet pro danou metriku - jasně rozlišitelné pro který tým zaznamenávám (používat se může jak na počítači, tabletu tak na mobilu)

1. Live report zaznamenaných dat
- Za všech zaznamenaných dat udělat jednoduchý live report, který bude dostupný přes odkaz z konkrétního utkání (tento odkaz by se měl automaticky vytvořit ihned poté, se vytvoří nové utkání v zadávání dat a bude možné tyto statistiky sledovat živě)
- Chci, aby pro každé tlačítko byla jedna položka v reportu
- Chci aby report ukazoval, kolik čeho má který tým, ideálně rozděleno na 1/2 v reportu na levé straně je domácí tým a na pravé straně hostující tým
- Vše rozděleno na 1.  a 2. poločas aby bylo zřetelné, ve kterém poločase čeho bylo

1. Celkový report
- Vytvořit celkový report, který bude opět rozdělený na hostující a domácí tým
- Záznamy budou rozdělený do 5 minutových úseků
- Ke každému záznamu se zobrazí o jakou situaci šlo a případný komentář, který k tomu byl napsán (a může být i zpětně doplněn)
- Pod všemi situacemi je číslený souhrn
- Rozděleno je vše na 1. a 2. poločas

https://nvidia-evaluated-nam-recommendations.trycloudflare.com/live/WgwM76Jx5F4

## Poznámkhy:

- Kdo měl větší držení míče - jak to vymyslet (automatismus)
- Více přiblížit finální report tomu jejich
- Nastavení barev u jednotlivých metrik

Aplikace **match-tracker**

- upravit, aby se dals nastavit prava - skupiny (vztahuje se panel i reporty)
- Upravit aby sel export vybraných dat v konkrétním formátu

## Prompt pro AI

- Udělej úpravu, díky které budu moc jednotlivé uživatele zařadit do konkrétních skupin. Uživatelé pak uvidí pouze data, která vytvoří v dané skupině nebo pro danou skupinu, ale nebudou moc vidět nic jiného a data ostatních skupin.
- Doplň mi možnost, aby se data, která se vytvoří dala vyexportovat do CSV nebo EXCELU
