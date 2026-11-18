# -*- coding: utf-8 -*-
"""Validator for seq=41 run."""
import os, re, json, glob
import xml.etree.ElementTree as ET

ROOT = os.getcwd()
TODAY = "2026-11-18"
NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
XH = "http://www.w3.org/1999/xhtml"
PT = os.path.join(ROOT, "cultura-mahjong", "mahjong-tradicional-vs-moderno", "index.html")
EN = os.path.join(ROOT, "en", "culture-mahjong", "traditional-vs-modern-mahjong", "index.html")
CANON_PT = "https://jogomahjong.com/cultura-mahjong/mahjong-tradicional-vs-moderno/"
CANON_EN = "https://en.jogomahjong.com/culture-mahjong/traditional-vs-modern-mahjong/"

fails, checks = [], 0


def ck(cond, msg):
    global checks
    checks += 1
    if not cond:
        fails.append(msg)
        print("FAIL", msg)


pt = open(PT, encoding="utf-8").read()
en = open(EN, encoding="utf-8").read()

# 1. placeholders / CJK / lang
for name, html in (("PT", pt), ("EN", en)):
    ck("{{" not in html, f"{name}: placeholder restante")
    stripped = re.sub(r'<span class="logo-mark">[^<]*</span>', "", html)
    hits = re.findall(r"[\u3400-\u9fff]", stripped)
    ck(not hits, f"{name}: caractere CJK fora do logotipo {hits}")
    ck("[TBD]" not in html, f"{name}: TBD")
ck('lang="pt-BR"' in pt, "PT: lang errado")
ck('lang="en"' in en, "EN: lang errado")

# 2. canonical / og:url / hreflang
ck(f'<link rel="canonical" href="{CANON_PT}">' in pt, "PT canonical")
ck(f'<meta property="og:url" content="{CANON_PT}">' in pt, "PT og:url")
ck(f'<link rel="canonical" href="{CANON_EN}">' in en, "EN canonical")
ck(f'<meta property="og:url" content="{CANON_EN}">' in en, "EN og:url")
ck(f'<link rel="alternate" hreflang="en" href="{CANON_EN}">' in pt, "PT hreflang en")
ck(f'<link rel="alternate" hreflang="pt-BR" href="{CANON_PT}">' in en, "EN hreflang pt")
ck(f'<link rel="alternate" hreflang="x-default" href="{CANON_PT}">' in pt, "PT x-default")

# 3. JSON-LD
for name, html in (("PT", pt), ("EN", en)):
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
    ck(bool(m), f"{name}: sem JSON-LD")
    if m:
        try:
            data = json.loads(m.group(1))
            ck(data["@type"] == "Article", f"{name}: @type errado")
            ck(data["mainEntityOfPage"] == (CANON_PT if name == "PT" else CANON_EN), f"{name}: mainEntityOfPage")
            ck(data["inLanguage"] == ("pt-BR" if name == "PT" else "en-US"), f"{name}: inLanguage")
        except Exception as e:
            ck(False, f"{name}: JSON-LD invalido {e}")

# 4. word count (article up to related block)
def wc(html):
    cut = html.split('<div class="related-internal">')[0]
    cut = cut.split('<article class="article">')[1]
    txt = re.sub(r"<[^>]+>", " ", cut)
    return len([w for w in txt.split() if w.strip()])

wpt, wen = wc(pt), wc(en)
print("words PT/EN:", wpt, wen)
ck(700 <= wpt <= 1100, f"PT palavras {wpt}")
ck(700 <= wen <= 1100, f"EN palavras {wen}")

# 5. links in body resolve
def body_links(html):
    body = html.split('<div class="related-internal">')[0].split('<article class="article">')[1]
    return re.findall(r'<a href="(/[^"]*)"', body)

def resolve(u):
    p = u.lstrip("/")
    if p == "":
        return os.path.isfile(os.path.join(ROOT, "index.html"))
    cand_dir = os.path.join(ROOT, "en", p) if not p.startswith("en/") else os.path.join(ROOT, p)
    # EN pages link within en/ tree
    return cand_dir

for name, html, base in (("PT", pt, ROOT), ("EN", en, os.path.join(ROOT, "en"))):
    links = body_links(html)
    ck(3 <= len(links) <= 6, f"{name}: {len(links)} links no corpo")
    for u in links:
        tgt = os.path.join(base, u.lstrip("/"), "index.html")
        ck(os.path.isfile(tgt), f"{name}: link quebrado {u}")
    print(name, "links:", links)

# 6. structure parity
def tags(html):
    body = html.split('<div class="related-internal">')[0].split('<article class="article">')[1]
    return re.findall(r"<(h2|h3|p|ul|li|em|strong)\b", body)

tpt, ten = tags(pt), tags(en)
print("tags PT/EN:", len(tpt), len(ten))
ck(tpt == ten, "paridade de tags PT/EN")

# 7. banned terms / dash
BAN_PT = ["No mundo atual", "Nos dias de hoje", "Vale ressaltar", "É importante destacar", "Em suma",
          "conclui-se", "mergulhe", "desbloqueie", "robusto", "perfeito"]
BAN_EN = ["In today's", "When it comes to", "It's important to note", "Let's dive", "In conclusion",
          "delve", "unlock", "elevate", "seamless", "game-changer", "robust", "realm", "testament to",
          "furthermore", "moreover", "All in all"]
for t in BAN_PT:
    ck(t.lower() not in pt.lower(), f"PT termo banido: {t}")
for t in BAN_EN:
    ck(not re.search(r"(?<![a-z])" + re.escape(t.lower()) + r"(?![a-z])", en.lower()), f"EN termo banido: {t}")
ck(pt.count("—") <= 2, f"PT travessoes {pt.count('—')}")
ck(en.count("—") <= 2, f"EN travessoes {en.count('—')}")

# 8. sitemaps
for label, path, domain, canon in (("PT", "sitemap.xml", "https://jogomahjong.com/", CANON_PT),
                                   ("EN", "en/sitemap.xml", "https://en.jogomahjong.com/", CANON_EN)):
    full = os.path.join(ROOT, path)
    raw = open(full, encoding="utf-8").read()
    tree = ET.parse(full)
    urls = tree.getroot().findall(f"{{{NS}}}url")
    locs = [u.find(f"{{{NS}}}loc").text for u in urls]
    ck(len(locs) == len(set(locs)), f"{label} sitemap: loc duplicado")
    ck(".html" not in raw, f"{label} sitemap: .html presente")
    ck(canon in locs, f"{label} sitemap: novo URL ausente")
    ck(all(l.startswith(domain) for l in locs), f"{label} sitemap: loc fora do dominio")
    # alternates
    bad = 0
    for u in urls:
        alts = u.findall(f"{{{XH}}}link")
        if len(alts) != 3:
            bad += 1
    ck(bad == 0, f"{label} sitemap: {bad} URLs sem 3 alternates")
    # lastmod
    lms = {u.find(f"{{{NS}}}loc").text: u.find(f"{{{NS}}}lastmod").text for u in urls}
    ck(lms.get(canon) == TODAY, f"{label} sitemap: lastmod novo != hoje ({lms.get(canon)})")
    print(label, "sitemap urls:", len(locs), "lastmod distintos:", len(set(lms.values())))
    # no noindex pages in sitemap
    for l in locs:
        rel = l.replace(domain, "")
        fp = os.path.join(ROOT, "en" if label == "EN" else "", rel, "index.html") if rel else \
             os.path.join(ROOT, "en" if label == "EN" else "", "index.html")
        if os.path.isfile(fp):
            h = open(fp, encoding="utf-8").read()
            m = re.search(r'<meta name="robots" content="([^"]*)"', h, re.I)
            if m and "noindex" in m.group(1).lower():
                ck(False, f"{label} sitemap: noindex listado {l}")

# 9. sitemap set == canonicals on disk
def disk_canonicals(base, skip_en):
    out = set()
    for dp, dn, fn in os.walk(base):
        rel = os.path.relpath(dp, base).replace("\\", "/")
        parts = [] if rel == "." else rel.split("/")
        if parts and parts[0] in {"content", "assets", "functions", ".workbuddy"} and not skip_en:
            dn[:] = []
            continue
        if parts and parts[0] == "en" and not skip_en:
            dn[:] = []
            continue
        if any(p.startswith(".") for p in parts):
            dn[:] = []
            continue
        for f in fn:
            if f != "index.html" and not f.endswith(".html"):
                continue
            fp = os.path.join(dp, f)
            h = open(fp, encoding="utf-8").read()
            m = re.search(r'<link rel="canonical" href="([^"]+)"', h)
            mi = re.search(r'<meta name="robots" content="([^"]*)"', h, re.I)
            if mi and "noindex" in mi.group(1).lower():
                continue
            if "404" in fp:
                continue
            if m:
                out.add(m.group(1).strip())
    return out

pt_disk = disk_canonicals(ROOT, False)
en_disk = disk_canonicals(os.path.join(ROOT, "en"), True)
print("disco PT/EN:", len(pt_disk), len(en_disk))
pt_loc = set(u.find(f"{{{NS}}}loc").text for u in ET.parse(os.path.join(ROOT, "sitemap.xml")).getroot().findall(f"{{{NS}}}url"))
en_loc = set(u.find(f"{{{NS}}}loc").text for u in ET.parse(os.path.join(ROOT, "en", "sitemap.xml")).getroot().findall(f"{{{NS}}}url"))
ck(pt_disk == pt_loc, f"PT sitemap != canonicals ({len(pt_loc)} vs {len(pt_disk)}, diff {pt_loc ^ pt_disk})")
ck(en_disk == en_loc, f"EN sitemap != canonicals ({len(en_loc)} vs {len(en_disk)}, diff {en_loc ^ en_disk})")

# 10. hubs + csv
pt_hub = open(os.path.join(ROOT, "cultura-mahjong", "index.html"), encoding="utf-8").read()
en_hub = open(os.path.join(ROOT, "en", "culture-mahjong", "index.html"), encoding="utf-8").read()
ck("mahjong-tradicional-vs-moderno/" in pt_hub, "PT hub sem o artigo")
ck("traditional-vs-modern-mahjong/" in en_hub, "EN hub sem o artigo")
ck("Traditional and Modern Mahjong" in en_hub, "EN hub sem titulo EN")
ck("Mahjong tradicional e mahjong moderno" in pt_hub, "PT hub sem titulo PT")

import csv as _csv
rows = list(_csv.DictReader(open(os.path.join(ROOT, "content", "keywords.csv"), encoding="utf-8-sig")))
r41 = [x for x in rows if x["seq"] == "41"][0]
ck(r41["status"] == "Gerado", f"CSV status {r41['status']}")
ck(r41["published_date"] == TODAY, f"CSV data {r41['published_date']}")

print("checks:", checks, "FAILs:", len(fails))
print("RESULT:", "PASS" if not fails else "FAIL")
