#!/usr/bin/env python3
"""Co je nového k ingestu od posledního ingestu.
Spuštění z kořene vaultu: python3 "LLM Wiki/nastroje/nove.py"

1) Vlastní poznámky mimo LLM Wiki: nové / změněné od git hashe posledního ingestu
   (řádek `- git: <hash>` v log.md), včetně necommitnutých změn.
   Čisté přesuny (beze změny obsahu) se ignorují, smazání se jen vypíší.
2) Soubory v LLM Wiki/raw/, které zatím nezmiňuje žádná zdrojová stránka ani log.
Vyloučené složky/soubory jsou v EXCLUDE; poznámka s `wiki: ne` ve frontmatteru se přeskočí.
"""
import os, re, subprocess, unicodedata

N = lambda s: unicodedata.normalize("NFC", s)
here = os.path.dirname(os.path.abspath(__file__))
wiki_root = os.path.dirname(here)
vault = os.path.dirname(wiki_root)

EXCLUDE = ["LLM Wiki/", ".obsidian/", ".trash/", "Úkoly/", "Markdown – tahák.md"]

def git(*a):
    return subprocess.run(["git", "-c", "core.quotepath=off", "-C", vault, *a],
                          capture_output=True, text=True).stdout

def excluded(p):
    p = N(p)
    if any(p.startswith(N(e)) or p == N(e).rstrip("/") for e in EXCLUDE): return True
    fp = os.path.join(vault, p)
    if p.endswith(".md") and os.path.exists(fp):
        head = open(fp, encoding="utf-8", errors="ignore").read(800)
        if re.search(r"^wiki:\s*(ne|no|false)\s*$", head, re.M | re.I): return True
    return False

log = open(os.path.join(wiki_root, "log.md"), encoding="utf-8").read()
hashes = re.findall(r"^- git: ([0-9a-f]{6,40})", log, re.M)
base = hashes[-1] if hashes else None

changed, deleted = {}, []
if base:
    for line in git("diff", "--name-status", "-M", base, "HEAD").splitlines():
        parts = line.split("\t"); st = parts[0]
        if st.startswith("R"):
            if st == "R100": continue
            path = parts[2]
        else:
            path = parts[1]
        if st == "D": deleted.append(path); continue
        changed[path] = st[0]
for line in git("status", "--porcelain", "-uall").splitlines():
    st, path = line[:2].strip(), line[3:].strip().strip('"')
    if " -> " in path: path = path.split(" -> ")[1]
    if st == "D": deleted.append(path)
    else: changed[path] = "A" if st == "??" else "M"

notes = sorted(p for p in changed if not excluded(p) and (p.endswith(".md") or p.endswith(".pdf")))
deleted = sorted(p for p in set(deleted) if not excluded(p))

mentioned = N(log)
zd = os.path.join(wiki_root, "wiki", "zdroje")
for f in os.listdir(zd):
    mentioned += N(open(os.path.join(zd, f), encoding="utf-8").read())
raw_new = []
raw = os.path.join(wiki_root, "raw")
for entry in sorted(os.listdir(raw)):
    if entry in ("assets",) or entry.startswith("."): continue
    name = N(os.path.splitext(entry)[0])
    if name not in mentioned and N(entry) not in mentioned:
        raw_new.append(entry)

print(f"Základ: git {base or '— (žádný hash v logu)'}  →  HEAD {git('rev-parse','--short','HEAD').strip()}")
print(f"\n## Nové/změněné vlastní poznámky: {len(notes)}")
for p in notes: print(f"  - [{changed[p]}] {p}")
print(f"\n## Smazané (zkontrolovat odkazy ve wiki): {len(deleted)}")
for p in deleted: print(f"  - {p}")
print(f"\n## Nezpracované v raw/: {len(raw_new)}")
for p in raw_new: print(f"  - {p}")
