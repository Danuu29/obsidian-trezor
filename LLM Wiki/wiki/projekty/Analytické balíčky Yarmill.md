---
typ: projekt
tags: [yarmill, produkt, nabidka]
zdroje: ["[[Zdroj – Yarmill poznámky]]", "[[Zdroj – Pořiďte si druhý mozek]]", "[[Zdroj – Persuading with Data]]"]
aktualizovano: 2026-10-19
---
# Analytické balíčky Yarmill

Produktová nabídka analytických řešení [[Yarmill]] (pro XPS). Zdroj: *Možnosti analytických řešení* (smazaná poznámka z Apple Notes).

| Balíček | Data | Přínos |
|---|---|---|
| **Bronze – Připravenost** | dotazníky (denní připravenost, náročnost tréninku), tréninková data od trenérů | připravenost hráčů, upozornění na přetrénování → [[Denní připravenost a wellness]] |
| **Silver – Rozvoj výkonnosti** | + GPS, testování, další zdroj stavu (např. Oura) | kondiční normy dle pozice, reporting cílů, predikce vývoje z testů → [[Thresholdy a benchmarky]] |
| **Gold – Okamžitý úspěch** | + Wyscout / StatsBomb / SkillCorner | herní normy dle pozic, predikce k seniorům, pozápasové analýzy, přípravy na soupeře → [[Aplikace – Analýza soupeře]] |
| **Skauting (modul)** | externí herní data + přestupy, setrvání v klubu, minuty, úspěšnost týmu s/bez hráče | vyhledávání hráčů podle požadavků a herních principů → [[Skauting – proces a reporting]] |

Doplněk: predikční model vývoje hráčů z pravidelného hodnocení trenérů a testů (k A-týmu nebo prodeji).

*Syntéza:* Sigma je v praxi referenční implementace balíčku Gold + Skauting.

*Návrh (Druhý mozek):* šablony reportů, grafy, prompty a definice metrik vznikající v Sigmě ukládat jako knihovnu **dílčích balíčků** – nový balíček pro další klub se pak skládá z hotových kusů → [[Dílčí balíčky a znovuvyužití práce]].

*Návrh (Persuading with Data):* ve všech balíčcích jednotná **šablona grafů** (headline nad sekcí, referenční čára thresholdu, popisky místo legendy, barvoslepě bezpečný semafor) a pro každý report vyplněný **WIIFT** cílového publika (trenér / vedení / hráč) → [[Persuading with Data – návrhy pro Sigmu]], [[Headline a testy slidu]].
