---
apple-notes-id: 32F43FEE-35EC-447A-8CEB-C696A16C863F
---
#app 
- rezervační systém na hřiště pro klub
- Notifikace 
- AI pomoc s plánováním 
- Konflikty
- Můžeš rezervovat část hřiště 
- Totální přehled všeho 
- V administraci musíš mít možnost prodat zařízení a prostor 
- Analytika vytíženosti hřišť a prostor 

Potřebuji vytvořit aplikaci, ve které bude fotbalový klub plánovat a dávat možnost rezervovat fotbalová hřiště, posilovny, testovací místnosti atd. Důležité je, aby ve všem fungoval “hlídací pes” který bude řešit konflikty na daných místech a nedovolí, aby se jedno konkrétní místo křížilo v jeden datum a čas s několika aktivitami. Do aplikace budou přicházet různí zaměstnanci, trenéři a manažeři, kteří si budou rezervovat vše místo na určitý datum a čas, aby vše bylo jasné pod kontrolou a nedocházelo ke konfliktům, že se na jednom místě sejde více týmů, nebo líbí a nebudou se vejít. Melo by se jednat o centrální místo pro správu prostor a sportovišť. 

Základní požadavky:

**Designe**
- Chtěl bych aby designe aplikace byl podobný jako má prostředí Apple - čisté, jasné přehledné a se zaoblenými rohy
- Chtěl bych, aby aplikace měla svoji „nástěnku“ nebo „úvodní stranu“, na které uvidím 
	- Jaké mám rezervace
	- Jsou tam informace o které jsou jinak na horší liště v seznamu aktivit, které se udály
**Datové uložiště + analýza dat**
- vše musí být postaveno na datovém řešení - udělej dostatečnou datovou zakladu, aby bylo možné analyzovat: vytíženost jednotlivých ploch, míst, zařízení, aby bylo vidět kdo dělá kde nejčastější rezervace, atd.. musím mít možnost vše zpětně analyzovat. Podle toho musí být také postavený datový prostor k systému. Do dat musí být vidět
- Skvělé by bylo kdyby byla také analytická část, kde bych si mohl vybrat podobně jako třeba v power BI na jaká data a jak se chci podívat. 
**Administrace** 
- Musí být možnost přidávat areály a v každém areálu pak musí být možnost přidávat prostory pro rezervaci - dále mohu jak areálům tak jednotlivým sportovištím přidávat barvu
- Musí být možnost upravovat možnosti daného prostorou (například fotbalové hřiště musí být možnost rezervovat celé nebo jen jeho část) - takže rozdělení na části, atd..
- Musí mít možnost přidávat jednotlivé kategorie a týmy
- Dále chci přidávat uživatele a jim přiřazovat role - nejvyšší role bude administrátor, pak bude trenér, správce (role administrátor má veškerá práva a ostatním rolím může jejich práva upravovat, omezovat, přidávat) 
	- Každý uživatel musí mít ve svém profilu email, telefonní číslo, a přiřazené kategorie (kategorie není povinná ale možnost to je)
**Uživatele a přístupy**
- rozdělit přístupy administrátor uvidí vaše a může dělat úplně vše a administrovat vše 
- Pro registraci nového uživatele je potřeba dat email 
**Rezervační systém - podstata aplikace** 
- Ke každému areálu může být přiřazen jeho správce - bude mít přehled o tom, co přesně se v jeho areálu děje a kdy
- Představují si, že bude fungovat podobně jako klasický Google kalendář 
- Možnosti zobrazení budou 
	- Jeden den - pokud je jeden den tak automaticky vidím celý areál a všechny sportoviště (ve sloupcích jsou jednotlivá sportoviště, řádky jsou čas - mám možnost si listovat mezi dny. Pokud si kliknu na rezervaci v pravém sloupci automaticky vidím veškeré podrobnosti k rezervaci) 
	- Jeden týden - Sloupce jsou dny v týdnu, řádky pak čas, v jednotlivých dnech a časech vidím různě barevné rezervace sportovišť
	- Měsíc - sloupce jsou dny v týdny, řádky jsou jednotlivé týdny - ve zmenšené formě vidím dané rezervace se základními informacemi
	- Pokud kliknu na událost u měsíce a týdne mi vyskočí okno u události, ve zobrazení jednoho dne se mi zobrazí lišta na pravé straně podobně jako v Google kalendáři. Rád bych, aby tato číst fungovala na velmi podobném principu jako Google kalednář
- Tlačítkem „nová rezervace“ nebo tahem nebo kliknutím si vytvořím rezervaci na konkrétní čas a místo
- Musím vyplnit:
	- Datum a čas - možnost nastavit pravidelné opakování (jak často se opakuje, kdy opakování končí)
	- Co tam bude za aktivitu
	- K aktivitě musím přiřadit kategorii
	- Kdo je zodpovědná osoba za akci
	- Mám možnost vložit poznámku
	- Při vytvoření přichází notifikace (emailem) správci areálu, pokud má notifikace zapnuté (notifikace si může zapnout kdokoli a může si zvolit jaký druh notifikací bude z jakého reálu dostávat)
	- Na horním panelu bude také lišta ve které bude jednak možnost spravovat vlastní profil, ale také tam bude prostor prostor, kde budou jednotlivý uživatelé dostávat informace - pokud se ve stejný čas přidal někdo na stejné hřiště (může se stát, že si někdo rezervuje jen 1/2 hřiště a druhou si rezervuje někdo jiný, tak dostane informaci - popřípadě notifikaci emailem, pokud má nastaveno), správce areálu dostane informaci o všem, co se v jeho areálu děje
- Musí být na první pohled zřejmé, ze je daný prosotor zaplněný nebo volný 
- Pokud by došlo ke konfliktu v nějakém prostoru musí být ihned oznámeno a nesmí být možnost rezervaci udělat 
**Automatizace** 
- Chci, aby bylo možné nastavit pravidelné odesílání PDF nebo excelu na konkrétní emaily v konkrétní den nebo čas a nastavit také opakování odesílání 
- Chci, aby bylo možné do aplikace připojit přes API AI - Gemini nebo Claud 
- Chci, aby v aplikace bylo na úvodní straně chatovací okno, kde mohu napsat svůj požadavek a AI mi poradí jak uspořádat nebo mi prohlédne možnosti rezervace

- Nyní budu aplikaci testovat na localu ve svém počítači, ale po jejím základní odladění ji chci vložit na Render pro online použití 
- Pokud by tě napadla jakákoli další vychytávka, která by mohla aplikace obohatit nebo vylepšit, klidně mi je sepiš, odsouhlasíme si je a přidáme to

**Navrhované úpravy:**
- Můžeme udělat mobilní aplikace? Jak to funguje? 
- Pokud chci dostat na web ke konkrétní URL adres?
- Pokud bych chtěl, aby se mi ta mohli logvat různé subjekty a každý měl jiné nastavení - jak to udělat? 

- Posílání notifikací přes email - popřípadě nějaké SMS nebo něco takového?
- Pokud kliknu do kalendáře, chci primární zobrazení na Den a do aktuálního času
- U služeb dát možnost nastavit doporučenou délku rezervace a pokud někdo udělá delší rezervaci, tak dát upozornění
- U služeb dát možnost nastavit dostupné termíny - tzn. Fyzioterapeut uvolní termíny jen v nějaký den třeba na 3 hodiny (naopak od zařízení - kde spíše budeme termíny blokovat)
- Mít možnost u konkrétních prostor nebo služeb zadat, že musí být rezervace potvrzená - na základě toho u každého prostoru musí být zodpovědná osoba s možností vybrat stejná jako je pro daný areál, pokud ale není zodpovědná osoba nastavená není možné potvrzení rezervací zapnout