#!/usr/bin/env python3
"""Lint LLM Wiki: rozbité odkazy, kolize názvů, sirotci, chybějící frontmatter.
Spuštění z kořene vaultu: python3 "LLM Wiki/nastroje/lint.py"
"""
import os, re, sys, unicodedata
from collections import defaultdict

N = lambda s: unicodedata.normalize("NFC", s)
here = os.path.dirname(os.path.abspath(__file__))
wiki_root = os.path.dirname(here)
vault = os.path.dirname(wiki_root)

by_name = defaultdict(list)   # basename -> [relpath]
paths = set()
for dp, dn, fn in os.walk(vault):
    dn[:] = [d for d in dn if not d.startswith('.')]
    for f in fn:
        rel = N(os.path.relpath(os.path.join(dp, f), vault))
        paths.add(rel)
        if f.endswith('.md'):
            by_name[N(f[:-3])].append(rel)
        else:
            by_name[N(f)].append(rel)

wiki_pages = [p for p in paths if p.startswith('LLM Wiki/') and p.endswith('.md') and '/raw/' not in p and not p.endswith('CLAUDE.md')]
link_re = re.compile(r'\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\\?\|[^\]]*)?\]\]')
inbound = defaultdict(int)
broken, ambiguous, nofm = [], [], []
for p in wiki_pages:
    txt = N(open(os.path.join(vault, p), encoding='utf-8').read())
    if not txt.startswith('---') and not p.endswith('log.md'):
        nofm.append(p)
    for m in link_re.finditer(txt):
        t = m.group(1).strip().rstrip('\\')
        if '/' in t:
            ok = (t + '.md') in paths or t in paths
            if not ok: broken.append((p, t))
            else: inbound[t.split('/')[-1]] += 1
            continue
        hits = by_name.get(t, [])
        if not hits: broken.append((p, t))
        elif len(hits) > 1: ambiguous.append((p, t, hits))
        inbound[t] += 1

collisions = [(n, h) for n, h in by_name.items() if len(h) > 1 and any(x.startswith('LLM Wiki/') for x in h)]
orphans = [p for p in wiki_pages if p.startswith('LLM Wiki/wiki/') and inbound[os.path.basename(p)[:-3]] == 0]

def show(title, items):
    print(f"\n## {title}: {len(items)}")
    for i in items: print("  -", i)
show("Rozbité odkazy", broken)
show("Nejednoznačné odkazy", ambiguous)
show("Kolize názvů wiki s vaultem", collisions)
show("Sirotci (bez příchozích odkazů)", orphans)
show("Bez frontmatteru", nofm)
idx = N(open(os.path.join(wiki_root,'index.md'),encoding='utf-8').read())
missing = [p for p in wiki_pages if p.startswith('LLM Wiki/wiki/') and '[['+os.path.basename(p)[:-3]+']]' not in idx]
show("Chybí v indexu", missing)
print(f"\nStránek wiki: {len(wiki_pages)}")
