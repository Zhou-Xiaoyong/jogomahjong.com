# -*- coding: utf-8 -*-
"""Validator for seq=45 run: sitemaps, canonicals, language, style parity, links."""
import os, re, json, csv, sys
import xml.etree.ElementTree as ET

ROOT = os.getcwd()
NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
XH = "http://www.w3.org/1999/xhtml"
TODAY = "2026-11-23"

PT = "cultura-mahjong/mahjong-feng-shui/index.html"
EN = "en/culture-mahjong/mahjong-feng-shui/index.html"
CANON_PT = "https://jogomahjong.com/cultura-mahjong/mahjong-feng-shui/"
CANON_EN = "https://en.jogomahjong.com/culture-mahjong/mahjong-feng-shui/"

fails, passes = [], 0


def ck(cond, label):
    global passes
    if cond:
        passes += 1
    else:
        fails.append(label)


def article(html):
    m = re.search(r'<article class="article">(.*?)</article>', html, re.S)
    return m.group(1) if m else ""


def body(html):
    return article(html).split('<div class="related-internal">')[0]


def wordcount(html):
    t = re.sub(r"<[^>]+>", " ", html)
    return len([w for w in re.split(r"\s+", t) if w.strip()])


pt = open(PT, encoding="utf-8").read()
en = open(EN, encoding="utf-8").read()

for label, h in (("PT", pt), ("EN", en)):
    ck("{{" not in h, f"{label}: placeholder restante")
    ck("[TBD]" not in h, f"{label}: TBD residual")
    ck("http://localhost" not in h, f"{label}: localhost")

for label, h in (("PT", pt), ("EN", en)):
    stripped = h.replace('<span class="logo-mark">中</span>', "")
    ck(not re.search(r"[\u3000-\u9fff\uff00-\uffef]", stripped), f"{label}: caractere CJK residual")

for label, h, can in (("PT", pt, CANON_PT), ("EN", en, CANON_EN)):
    ck(re.search(r'<link rel="canonical" href="([^"]+)"', h).group(1) == can, f"{label}: canonical != clean url")
    ck(re.search(r'<meta property="og:url" content="([^"]+)"', h).group(1) == can, f"{label}: og:url != canonical")
    ck(".html" not in can, f"{label}: canonical tem .html")
    ck(re.search(r'hreflang="pt-BR" href="([^"]+)"', h).group(1) == CANON_PT, f"{label}: alternate pt")
    ck(re.search(r'hreflang="en" href="([^"]+)"', h).group(1) == CANON_EN, f"{label}: alternate en")
    ck(re.search(r'hreflang="x-default" href="([^"]+)"', h).group(1) == CANON_PT, f"{label}: x-default")

for label, h in (("PT", pt), ("EN", en)):
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)
    try:
        d = json.loads(m.group(1))
        ck(d["@type"] == "Article", f"{label}: JSON-LD @type")
        ck(d["mainEntityOfPage"] == (CANON_PT if label == "PT" else CANON_EN), f"{label}: JSON-LD mainEntity")
    except Exception as e:
        fails.append(f"{label}: JSON-LD nao parseia {e}")

wpt, wen = wordcount(body(pt)), wordcount(body(en))
ck(700 <= wpt <= 1100, f"PT: {wpt} palavras fora de 700-1100")
ck(700 <= wen <= 1100, f"EN: {wen} palavras fora de 700-1100")
print("palavras PT/EN (eyebrow+H1+lead+body):", wpt, wen,
      "| com bloco relacionado:", wordcount(article(pt)), wordcount(article(en)))

BAN_EN = ["in today's fast-paced", "when it comes to", "it's important to note", "let's dive in",
          "in conclusion", "delve", "unlock", "elevate", "seamless", "game-changer", "robust",
          "testament to", "furthermore", "moreover", "needless to say", "look no further",
          "the realm of", "navigating the landscape"]
BAN_PT = ["no mundo atual", "nos dias de hoje", "vale ressaltar", "é importante destacar",
          "em suma", "por fim, conclui", "mergulhar", "desbloque", "sem costura",
          "revolucion", "robust"]
low_en = body(en).lower()
low_pt = body(pt).lower()
for b in BAN_EN:
    ck(b not in low_en, f"EN: termo banido '{b}'")
for b in BAN_PT:
    ck(b not in low_pt, f"PT: termo banido '{b}'")
ck(len(re.findall(r"(?<![a-zà-ú])além disso", low_pt)) <= 1, "PT: 'além disso' repetido")

ck(body(pt).count("—") <= 2, f"PT: {body(pt).count('—')} travessoes")
ck(body(en).count("—") <= 2, f"EN: {body(en).count('—')} travessoes")


def links(h):
    return re.findall(r'href="([^"]+)"', body(h))


for label, h, en_side in (("PT", pt, False), ("EN", en, True)):
    ls = [l for l in links(h) if l.startswith("/")]
    uniq = sorted(set(ls))
    ck(len(uniq) >= 3, f"{label}: menos de 3 links internos ({len(uniq)})")
    for l in uniq:
        target = os.path.join(ROOT, "en" if en_side else "", l.strip("/"))
        ck(os.path.isfile(os.path.join(target, "index.html")), f"{label}: link quebrado {l}")
    print(label, "links:", uniq)

for label, h, hub in (("PT", pt, "/cultura-mahjong/"), ("EN", en, "/culture-mahjong/")):
    hl = [l for l in links(h) if l.startswith("/")]
    ck(hub in hl, f"{label}: hub ausente")
    ck("/jogar-mahjong/" in hl, f"{label}: solitario ausente")
    sib = [l for l in hl if l not in ("/jogar-mahjong/", hub, "/mahjong-classico/")]
    ck(len(sib) >= 2, f"{label}: menos de 2 artigos irmaos ({sib})")


def check_sitemap(path, expect_new, disk_canons):
    raw = open(path, encoding="utf-8").read()
    tree = ET.parse(path)
    urls = tree.getroot().findall(f"{{{NS}}}url")
    locs = [u.find(f"{{{NS}}}loc").text for u in urls]
    ck(len(locs) == len(set(locs)), f"{path}: loc duplicado")
    ck(".html" not in raw, f"{path}: .html presente")
    ck(expect_new in locs, f"{path}: URL nova ausente")
    ck(set(locs) == disk_canons, f"{path}: conjunto != canonicals do disco ({len(locs)} vs {len(disk_canons)})")
    bad_alt = sum(1 for u in urls if len(u.findall(f"{{{XH}}}link")) != 3)
    ck(bad_alt == 0, f"{path}: {bad_alt} urls sem 3 alternates")
    lm_today = sum(1 for u in urls if (u.find(f"{{{NS}}}lastmod").text or "") == TODAY)
    lms = set(u.find(f"{{{NS}}}lastmod").text for u in urls)
    print(path, "locs", len(locs), "lastmod hoje", lm_today, "valores distintos", len(lms))
    return locs


def disk_canonicals(base, skip_en):
    skip = {"content", "assets", "functions", ".workbuddy", ".git", "mah-app"}
    if skip_en:
        skip = skip | {"en"}
    out = set()
    for dp, dn, fn in os.walk(base):
        rel = os.path.relpath(dp, base).replace("\\", "/")
        parts = [] if rel == "." else rel.split("/")
        if parts and (parts[0] in skip or any(p.startswith(".") for p in parts)):
            dn[:] = []
            continue
        for f in fn:
            if f.endswith(".html"):
                h = open(os.path.join(dp, f), encoding="utf-8").read()
                m = re.search(r'<link rel="canonical" href="([^"]+)"', h)
                if m and not re.search(r'<meta name="robots" content="[^"]*noindex', h, re.I) and "404" not in f:
                    out.add(m.group(1))
    return out


pt_disk = disk_canonicals(ROOT, skip_en=True)
en_disk = disk_canonicals(os.path.join(ROOT, "en"), skip_en=True)
pt_locs = check_sitemap(os.path.join(ROOT, "sitemap.xml"), CANON_PT, pt_disk)
en_locs = check_sitemap(os.path.join(ROOT, "en", "sitemap.xml"), CANON_EN, en_disk)

pt_hub = open("cultura-mahjong/index.html", encoding="utf-8").read()
en_hub = open("en/culture-mahjong/index.html", encoding="utf-8").read()
ck("mahjong-feng-shui" in pt_hub, "PT hub nao lista o artigo")
ck("mahjong-feng-shui" in en_hub, "EN hub nao lista o artigo")
ck("Mahjong e feng shui" in pt_hub, "PT hub sem titulo")
ck("Mahjong and Feng Shui" in en_hub, "EN hub sem titulo")
print("hub PT itens:", pt_hub.count("<li><a href="), "hub EN itens:", en_hub.count("<li><a href="))

rows = list(csv.DictReader(open("content/keywords.csv", encoding="utf-8")))
row = [r for r in rows if r["seq"] == "45"][0]
ck(row["status"] == "Gerado", "CSV status != Gerado")
ck(row["published_date"] == TODAY, f"CSV data {row['published_date']}")
print("CSV seq45:", row["status"], row["published_date"], "|", row["keyword_pt"], "/", row["keyword_en"])


def skel(h):
    return re.findall(r"<(/?[a-z0-9]+)", article(h))


spt, sen = skel(pt), skel(en)
if spt != sen:
    import difflib
    print("SKELETON DIFF:", list(difflib.unified_diff(spt, sen, lineterm=""))[:20])
ck(spt == sen, f"paridade de tags PT/EN ({len(spt)} vs {len(sen)})")
print("tags PT/EN:", len(spt), len(sen))


def shingles(h, n=10):
    t = re.sub(r"<[^>]+>", " ", body(h)).lower()
    ws = re.findall(r"[\wà-ú']+", t)
    return {" ".join(ws[i:i + n]) for i in range(len(ws) - n + 1)}


def others(section_pt, my_path):
    out = []
    for dp, dn, fn in os.walk(section_pt):
        if "index.html" in fn:
            p = os.path.join(dp, "index.html").replace("\\", "/")
            if p != my_path:
                out.append(p)
    return out


for label, base, mine in (("PT", "cultura-mahjong", PT), ("EN", "en/culture-mahjong", EN)):
    h = pt if label == "PT" else en
    s = shingles(h)
    worst = []
    for p in others(base, mine):
        inter = s & shingles(open(p, encoding="utf-8").read())
        if inter:
            worst.append((len(inter), p, list(inter)[:1]))
    worst.sort(reverse=True)
    print(f"shingle {label}: {len(worst)} artigos com overlap; top:", worst[:2])
    ck(all(w[0] <= 2 for w in worst), f"{label}: shingle overlap alto {worst[:2]}")

print("\nCHECKS OK:", passes, "FAIL:", len(fails))
for f in fails:
    print(" -", f)
sys.exit(1 if fails else 0)
