---
tags:
  - tahák
  - obsidian
---

# Markdown – tahák

> [!tip] Na začátek stačí
> **Nadpisy, odrážky, úkoly a `[[odkazy]]`** – to pokryje 90 % běžné práce.

## Formátování textu

| Napíšete          | Výsledek        | Zkratka |
| ----------------- | --------------- | ------- |
| `**tučně**`       | **tučně**       | Cmd + B |
| `*kurzíva*`       | *kurzíva*       | Cmd + I |
| `~~přeškrtnuto~~` | ~~přeškrtnuto~~ |         |
| `==zvýraznění==`  | ==zvýraznění==  |         |
| `` `kód` ``       | `kód`           |         |

## Nadpisy

```
# Nadpis 1
## Nadpis 2
### Nadpis 3
```

Mezera za `#` je nutná. Nadpisy tvoří osnovu poznámky (panel *Osnova*).

## Seznamy a úkoly

```
- odrážka
  - vnořená odrážka (odsazení tabulátorem)
1. číslovaný seznam
- [ ] úkol
- [x] hotový úkol
```

Ukázka:

- odrážka
  - vnořená odrážka
1. číslovaný seznam
- [ ] úkol
- [x] hotový úkol

**Cmd + L** přepíná odrážku → úkol → hotovo.

## Odkazy a vkládání

| Napíšete | Co to dělá |
|---|---|
| `[[Název poznámky]]` | odkaz na jinou poznámku (po napsání `[[` se nabídnou poznámky) |
| `[[Poznámka\|jiný text]]` | odkaz zobrazený pod jiným textem |
| `[[Poznámka#Nadpis]]` | odkaz na konkrétní nadpis |
| `![[Poznámka]]` | vloží obsah jiné poznámky |
| `![[obrázek.png]]` | vloží obrázek |
| `[text](https://...)` | odkaz na web (Cmd + K) |
| `#tag` | štítek pro hledání a třídění |

## Citace, čára, callouty

```
> citace

---

> [!note] Nadpis
> Barevný rámeček – dále např. [!tip], [!warning], [!todo]
```

Ukázka:

> citace

> [!note] Poznámka
> Takhle vypadá callout.

> [!warning] Pozor
> A takhle varování.

## Blok kódu

````
```sql
SELECT * FROM hraci;
```
````

Ukázka:

```sql
SELECT * FROM hraci;
```

## Tabulka

```
| Hráč | Minuty |
|------|--------|
| A    | 90     |
```

Ukázka:

| Hráč | Minuty |
|------|--------|
| A    | 90     |

## Klávesové zkratky Obsidianu

| Zkratka | Co dělá |
|---|---|
| Cmd + N | nová poznámka |
| Cmd + O | rychle otevřít poznámku |
| Cmd + P | paleta příkazů |
| Cmd + Shift + F | hledat v celém trezoru |
| Cmd + E | přepnout editaci a čtení |
| Cmd + klik na odkaz | otevřít odkaz v nové kartě |
| Cmd + Z / Cmd + Shift + Z | zpět / znovu |
| Cmd + L | odrážka → úkol → hotovo |
| Cmd + K | vložit odkaz |
