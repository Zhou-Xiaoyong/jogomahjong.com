# -*- coding: utf-8 -*-
"""Validador seq=43 — como fazer um par no mahjong (PT+EN)."""
import os, re, sys, json, glob
import xml.etree.ElementTree as ET

ROOT = os.getcwd()
NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
XH = "http://www.w3.org/1999/xhtml"
TODAY = "2026-11-20"
FAILS = []


def ck(cond, msg):
    print(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        FAILS.append(msg)


pt_path = "como-jogar-mahjong/como-fazer-par-mahjong/index.html"
en_path = "en/how-to-play-mahjong/how-to-make-pair-mahjong/index.html"
CANON_PT = "https://jogomahjong.com/como-jogar-mahjong/como-fazer-par-mahjong/"
CANON_EN = "https://en.jogomahjong.com/how-to-play-mahjong/how-to-make-pair-mahjong/"

pt = open(os.path.join(ROOT, pt_path), encoding="utf-8").read()
en = open(os.path.join(ROOT, en_path), encoding="utf-8").read()

# 1. placeholders
for name, h in (("PT", pt), ("EN", en)):
    ck("{{" not in h and "}}" not in h, f"{name} sem placeholders")
    ck("[TBD]" not in h and "lorem" not in h, f"{name} sem texto de rascunho")

# 2. canonical / og:url == clean url
for name, h, c in (("PT", pt, CANON_PT), ("EN", en, CANON_EN)):
    can = re.search(r'<link rel="canonical" href="([^"]+)"', h).group(1)
    og = re.search(r'<meta property="og:url" content="([^"]+)"', h).group(1)
    ck(can == c, f"{name} canonical = {c}")
    ck(og == c, f"{name} og:url = canonical")
    ck(".html" not in can, f"{name} canonical sem .html")
    ck(f'hreflang="pt-BR" href="{CANON_PT}"' in h, f"{name} alternate pt-BR")
    ck(f'hreflang="en" href="{CANON_EN}"' in h, f"{name} alternate en")
    ck(f'hreflang="x-default" href="{CANON_PT}"' in h, f"{name} alternate x-default")

# 3. JSON-LD
for name, h in (("PT", pt), ("EN", en)):
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)
    try:
        d = json.loads(m.group(1))
        ck(d["@type"] == "Article" and d["headline"], f"{name} JSON-LD valido")
        ck(d["inLanguage"] == ("pt-BR" if name == "PT" else "en-US"), f"{name} inLanguage {d['inLanguage']}")
    except Exception as e:
        ck(False, f"{name} JSON-LD parse: {e}")

# 4. noindex ausente
for name, h in (("PT", pt), ("EN", en)):
    ck("noindex" not in h, f"{name} indexavel (sem noindex)")

# 5. CJK fora do logo
for name, h in (("PT", pt), ("EN", en)):
    body = h.replace('<span class="logo-mark">中</span>', "")
    ck(not re.search(r"[\u3000-\u9fff\uff00-\uffef]", body), f"{name} sem caracteres CJK")

# 6. palavra count dentro do article
for name, h in (("PT", pt), ("EN", en)):
    a = re.search(r'<article class="article">(.*?)<div class="related-internal">', h, re.S).group(1)
    n = len([w for w in re.split(r"\s+", re.sub(r"<[^>]+>", " ", a)) if w.strip()])
    ck(700 <= n <= 1100, f"{name} palavras no article = {n}")

# 7. travessoes <=2 e sem termos banidos
BAN_PT = ["No mundo atual", "Nos dias de hoje", "Vale ressaltar", "É importante destacar",
          "Em suma", "Por fim, conclui", "mergulhe", "desbloqueie", "eleve", "robusto"]
BAN_EN = ["In today's", "When it comes to", "It's important to note", "Let's dive",
          "In conclusion", "delve", "unlock", "seamless", "game-changer", "robust",
          "realm", "testament to", "elevate"]
for name, h, bans in (("PT", pt, BAN_PT), ("EN", en, BAN_EN)):
    a = re.search(r'<article class="article">(.*?)<div class="related-internal">', h, re.S).group(1)
    ck(a.count("—") <= 2, f"{name} travessoes = {a.count('—')}")
    hit = [b for b in bans if re.search(r"(?<![A-Za-zÀ-ú])" + re.escape(b) + r"(?![A-Za-zÀ-ú])", a, re.I)]
    ck(not hit, f"{name} termos banidos: {hit}")

# 8. links internos do corpo resolvem
for name, h, prefix in (("PT", pt, ""), ("EN", en, "en/")):
    a = re.search(r'<article class="article">(.*?)<div class="related-internal">', h, re.S).group(1)
    hrefs = sorted(set(re.findall(r'href="(/[^"]*)"', a)))
    ck(3 <= len(hrefs) <= 5, f"{name} links no corpo = {len(hrefs)}: {hrefs}")
    for hr in hrefs:
        p = os.path.join(ROOT, prefix + hr.strip("/"), "index.html") if hr.endswith("/") else os.path.join(ROOT, prefix + hr.lstrip("/"))
        ck(os.path.isfile(p), f"{name} link resolve: {hr}")
    # link_to obrigatorios
    ck("/jogar-mahjong/" in hrefs, f"{name} link_to /jogar-mahjong/")
    ck(("/como-jogar-mahjong/" if name == "PT" else "/how-to-play-mahjong/") in hrefs,
       f"{name} link_to hub")

# 9. related links resolvem
for name, h, prefix in (("PT", pt, ""), ("EN", en, "en/")):
    rel = re.search(r'<div class="related-internal">(.*?)</div>', h, re.S).group(1)
    urls = re.findall(r'href="([^"]+)"', rel)
    ck(len(urls) == 5, f"{name} related = {len(urls)}")
    for u in urls:
        host = "https://en.jogomahjong.com/" if name == "EN" else "https://jogomahjong.com/"
        assert u.startswith(host), u
        p = os.path.join(ROOT, prefix + u[len(host):].strip("/"), "index.html")
        ck(os.path.isfile(p), f"{name} related resolve: {u}")

# 10. hubs listam o artigo
hub_pt = open(os.path.join(ROOT, "como-jogar-mahjong", "index.html"), encoding="utf-8").read()
hub_en = open(os.path.join(ROOT, "en", "how-to-play-mahjong", "index.html"), encoding="utf-8").read()
ck(CANON_PT in hub_pt, "hub PT lista o artigo novo")
ck("Como fazer um par no Mahjong" in hub_pt, "hub PT com titulo PT")
ck(CANON_EN in hub_en, "hub EN lista o artigo novo")
ck("How to Make a Pair in Mahjong" in hub_en, "hub EN com titulo EN")
ck(hub_pt.count("<li>") > 20, f"hub PT itens = {hub_pt.count('<li>')}")

# 11. sitemaps
disk_pt, disk_en = set(), set()
for f in glob.glob(os.path.join(ROOT, "**", "index.html"), recursive=True) + glob.glob(os.path.join(ROOT, "*.html")):
    rel = os.path.relpath(f, ROOT).replace("\\", "/")
    if rel.startswith(("content/", "assets/", ".")) or rel == "index.html" and False:
        continue
    html = open(f, encoding="utf-8").read()
    if re.search(r'<meta name="robots" content="[^"]*noindex', html, re.I):
        continue
    if "404" in rel:
        continue
    can = re.search(r'<link rel="canonical" href="([^"]+)"', html)
    if not can:
        continue
    (disk_en if rel.startswith("en/") else disk_pt).add(can.group(1))

for label, path, disk, host in (("PT", os.path.join(ROOT, "sitemap.xml"), disk_pt, "https://jogomahjong.com/"),
                                ("EN", os.path.join(ROOT, "en", "sitemap.xml"), disk_en, "https://en.jogomahjong.com/")):
    raw = open(path, encoding="utf-8").read()
    tree = ET.parse(path)
    urls = tree.getroot().findall(f"{{{NS}}}url")
    locs = [u.find(f"{{{NS}}}loc").text for u in urls]
    ck(len(locs) == len(set(locs)), f"{label} sitemap sem loc duplicado ({len(locs)})")
    ck(not re.search(r"\.html<", raw), f"{label} sitemap sem .html em <loc>")
    ck(set(locs) == disk, f"{label} sitemap == canonicals do disco ({len(locs)} vs {len(disk)})")
    ck((CANON_PT if label == "PT" else CANON_EN) in locs, f"{label} sitemap contem URL nova")
    bad = []
    for u in urls:
        alts = {(a.get("hreflang"), a.get("href")) for a in u.findall(f"{{{XH}}}link")}
        if len(alts) != 3:
            bad.append(u.find(f"{{{NS}}}loc").text)
        for lang, href in alts:
            if not href.startswith("https://jogomahjong.com/") and not href.startswith("https://en.jogomahjong.com/"):
                bad.append(href)
        lm = u.find(f"{{{NS}}}lastmod")
        if lm is None or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", lm.text or ""):
            bad.append("lastmod " + (u.find(f"{{{NS}}}loc").text or ""))
    ck(not bad, f"{label} 3 alternates + lastmod por URL (problemas: {bad[:4]})")
    lms = {u.find(f"{{{NS}}}lastmod").text for u in urls}
    ck(len(lms) >= 10, f"{label} lastmod preservado em varias datas = {len(lms)} distintas")

# 12. CSV
import csv
rows = list(csv.DictReader(open(os.path.join(ROOT, "content", "keywords.csv"), encoding="utf-8")))
r = [x for x in rows if x["seq"] == "43"][0]
ck(r["status"] == "Gerado" and r["published_date"] == TODAY, f"CSV seq43 {r['status']} {r['published_date']}")

# 13. paridade estrutural PT/EN
def skel(h):
    a = re.search(r'<article class="article">(.*?)</div>', h, re.S).group(1)
    return re.findall(r"<(\w+)", a)
sp, se = skel(pt), skel(en)
ck(sp == se, f"paridade de tags PT/EN ({len(sp)} vs {len(se)})")
if sp != se:
    import difflib
    print("\n".join(list(difflib.unified_diff(sp, se, lineterm=""))[:40]))

# 14. shingle 10 palavras vs artigos anteriores da mesma secao
def shingles(txt):
    w = re.findall(r"[a-zà-ú0-9]+", txt.lower())
    return {" ".join(w[i:i + 10]) for i in range(len(w) - 9)}

def body(h):
    a = re.search(r'<article class="article">(.*?)<div class="related-internal">', h, re.S).group(1)
    return re.sub(r"<[^>]+>", " ", a)

for name, h, pat in (("PT", pt, "como-jogar-mahjong/*/index.html"),
                     ("EN", en, "en/how-to-play-mahjong/*/index.html")):
    mine = shingles(body(h))
    worst = (0, "")
    for f in glob.glob(os.path.join(ROOT, pat)):
        if os.path.abspath(f) == os.path.abspath(os.path.join(ROOT, pt_path if name == "PT" else en_path)):
            continue
        other = shingles(body(open(f, encoding="utf-8").read()))
        ov = len(mine & other)
        if ov > worst[0]:
            worst = (ov, os.path.basename(os.path.dirname(f)))
    ck(worst[0] <= 2, f"{name} shingle 10w max overlap = {worst[0]} ({worst[1]})")

print("\n===", "TODOS OS CHECKS OK" if not FAILS else f"{len(FAILS)} FALHAS", "===")
sys.exit(0 if not FAILS else 1)
