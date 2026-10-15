---
typ: projekt
tags: [aplikace, provoz, rezervace]
zdroje: ["[[Zdroj – Zadání aplikací]]", "[[Zdroj – Úkoly]]"]
stav: čeká
aktualizovano: 2026-10-15
---
# Aplikace – Rezervační systém

Centrální rezervace hřišť, posiloven, testovacích místností a služeb (fyzio) v klubu s „hlídacím psem“ konfliktů. Zdroj: [[SK Sigma Olomouc/Aplikace/Rezervační systém/Rezervační systém 🗓️|Rezervační systém 🗓️]]. V úkolníčku ve stavu „čeká“.

## Hlavní požadavky

- Design ve stylu Apple; nástěnka s mými rezervacemi.
- Kalendář jako Google Calendar: den (sloupce = sportoviště), týden, měsíc; pravá lišta s detailem.
- Rezervace části prostoru (např. ½ hřiště), opakování, kategorie, zodpovědná osoba, poznámka; **konflikt = nelze uložit**.
- Administrace areálů a prostor (barvy, dělení), kategorie/týmy, uživatelé a role (admin, trenér, správce).
- Notifikace (e-mail, případně SMS), správce areálu vidí vše.
- Datová vrstva pro analytiku vytíženosti (à la Power BI), plánované odesílání PDF/Excel.
- AI chat (Gemini/Claude) pro pomoc s plánováním. Vývoj lokálně → Render.

## Navržená rozšíření

Mobilní aplikace, vlastní URL, multi-tenant (různé subjekty), doporučená délka rezervace, dostupné termíny služeb (fyzio), rezervace vyžadující potvrzení.
