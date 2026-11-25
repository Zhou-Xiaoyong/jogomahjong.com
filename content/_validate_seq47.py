# -*- coding: utf-8 -*-
"""Validation for seq=47 — como fazer uma trinca no mahjong / how to make a pung in mahjong."""
import os, re, json, glob
import xml.etree.ElementTree as ET

ROOT = os.getcwd()
NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
PT_URL = "https://jogomahjong.com/como-jogar-mahjong/como-fazer-trinca-mahjong/"
EN_URL = "https://en.jogomahjong.com/how-to-play-mahjong/how-to-make-pung-mahjong/"
PT_FILE = os.path.join(ROOT, "como-jogar-mahjong", "como-fazer-trinca-mahjong", "index.html")
EN_FILE = os.path.join(ROOT, "en", "how-to-play-mahjong", "how-to-make-pung-mahjong", "index.html")

fails, checks = [], 0


def ck(cond, msg):
    global checks
    checks += 1
    if not cond:
        fails.append(msg)


def article(html):
    m = re.search(r'<article class="article">(.*?)</article>', html, re.S)
    return m.group(1) if m else ""


def body_only(html):
    a = article(html)
    a = a.split('<div class="related-internal">')[0]
    return a


def words(t):
    t = re.sub(r"<[^>]+>", " ", t)
    return len([w for w in re.split(r"\s+", t) if w.strip()])


# ---------------------------------------------------------------- 1. sitemaps
for f, base in (("sitemap.xml", "https://jogomahjong.com/"),
                (os.path.join("en", "sitemap.xml"), "https://en.jogomahjong.com/")):
    path = os.path.join(ROOT, f)
    raw = open(path, encoding="utf-8").read()
    root = ET.parse(path).getroot()
    urls = root.findall(f"{{{NS}}}url")
    locs = [u.find(f"{{{NS}}}loc").text.strip() for u in urls]
    ck(raw.count(".html") == 0, "%s contains .html" % f)
    ck(len(locs) == len(set(locs)), "%s duplicate loc" % f)
    ck(all(l.startswith(base) for l in locs), "%s loc fora do dominio" % f)
    bad = 0
    for u in urls:
        links = [c for c in u if c.tag.endswith("}link")]
        hl = sorted(c.get("hreflang") for c in links)
        if hl != ["en", "pt-BR", "x-default"]:
            bad += 1
    ck(bad == 0, "%s alternates incompletos em %d urls" % (f, bad))
    noidx = []
    for u in urls:
        loc = u.find(f"{{{NS}}}loc").text.strip()
        is_en = base.endswith("en.jogomahjong.com/")
        p = os.path.join(ROOT, "en" if is_en else "", loc.replace(base, "").strip("/"))
        cand = os.path.join(p, "index.html")
        if not os.path.isfile(cand):
            continue
        h = open(cand, encoding="utf-8").read()
        m = re.search(r'<meta name="robots" content="([^"]*)"', h, re.I)
        if m and "noindex" in m.group(1).lower():
            noidx.append(loc)
    ck(not noidx, "%s contem noindex: %s" % (f, noidx))
    globals()["locs_" + ("en" if base.endswith("en.jogomahjong.com/") else "pt")] = locs
    print(f, "locs:", len(locs), "| lastmod distintos:",
          len({u.find(f"{{{NS}}}lastmod").text for u in urls}))


def disk_canonicals(base):
    out = set()
    for dp, dn, fn in os.walk(base):
        rel = os.path.relpath(dp, base).replace("\\", "/")
        parts = [] if rel == "." else rel.split("/")
        if parts and (parts[0] in {"en", "content", "assets", "functions", ".workbuddy", ".git"}
                      or any(p.startswith(".") for p in parts)):
            dn[:] = []
            continue
        for f in fn:
            if not f.endswith(".html"):
                continue
            h = open(os.path.join(dp, f), encoding="utf-8").read()
            m = re.search(r'<meta name="robots" content="([^"]*)"', h, re.I)
            if m and "noindex" in m.group(1).lower():
                continue
            if "404" in f:
                continue
            c = re.search(r'<link rel="canonical" href="([^"]+)"', h)
            if c:
                out.add(c.group(1).strip())
    return out


dp_ = disk_canonicals(ROOT)
de_ = disk_canonicals(os.path.join(ROOT, "en"))
ck(dp_ == set(locs_pt), "PT sitemap != canonicals do disco (%d vs %d)" % (len(locs_pt), len(dp_)))
ck(de_ == set(locs_en), "EN sitemap != canonicals do disco (%d vs %d)" % (len(locs_en), len(de_)))
print("disk canonicals PT/EN:", len(dp_), len(de_))
ck(PT_URL in locs_pt, "PT URL nova ausente do sitemap")
ck(EN_URL in locs_en, "EN URL nova ausente do sitemap")


def lastmod_of(path, url):
    for u in ET.parse(path).getroot().findall(f"{{{NS}}}url"):
        if u.find(f"{{{NS}}}loc").text.strip() == url:
            return u.find(f"{{{NS}}}lastmod").text.strip()
    return None


ck(lastmod_of(os.path.join(ROOT, "sitemap.xml"), PT_URL) == "2026-11-25", "lastmod PT errado")
ck(lastmod_of(os.path.join(ROOT, "en", "sitemap.xml"), EN_URL) == "2026-11-25", "lastmod EN errado")

# ---------------------------------------------------------------- 2. pages
for path, can, lang in ((PT_FILE, PT_URL, "pt-BR"), (EN_FILE, EN_URL, "en")):
    h = open(path, encoding="utf-8").read()
    ck("{{" not in h, "%s placeholder" % path)
    ck(can in h, "%s canonical ausente" % path)
    c = re.search(r'<link rel="canonical" href="([^"]+)"', h).group(1)
    ck(c == can, "%s canonical != esperado (%s)" % (path, c))
    og = re.search(r'<meta property="og:url" content="([^"]+)"', h).group(1)
    ck(og == can, "%s og:url != canonical" % path)
    ck(h.count('<link rel="alternate" hreflang=') == 3, "%s hreflang count" % path)
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)
    try:
        data = json.loads(m.group(1))
        ck(data["mainEntityOfPage"] == can, "%s JSON mainEntityOfPage" % path)
        ck(data["inLanguage"] == ("pt-BR" if lang == "pt-BR" else "en-US"), "%s JSON inLanguage" % path)
        ck(data["headline"].startswith("Como fazer uma trinca" if lang == "pt-BR" else "How to Make a Pung"),
           "%s JSON headline" % path)
    except Exception as e:
        ck(False, "%s JSON-LD invalido: %s" % (path, e))
    stripped = h.replace('<span class="logo-mark">中</span>', '')
    ck(not re.search(r"[\u4e00-\u9fff]", stripped), "%s contem CJK" % path)
    ck("[TBD]" not in h and "lorem" not in h.lower(), "%s placeholder textual" % path)
    ck(not re.search(r'rel="canonical" href="[^"]*\.html"', h), "%s canonical com .html" % path)

    art = article(h)
    n = words(body_only(h))
    ck(700 <= n <= 1100, "%s palavras %d fora de 700-1100" % (path, n))
    print(path.split(os.sep)[-3], "words(article):", n, "| body:", words(body_only(h)))
    ck(art.count("—") <= 2, "%s travessoes %d" % (path, art.count("—")))
    ck(len(re.findall(r"<h2>", art)) >= 6, "%s poucos h2" % path)
    links = re.findall(r'href="(/[^"#]*)"', body_only(h))
    uniq = sorted(set(links))
    ck(4 <= len(uniq) <= 7, "%s links internos %d" % (path, len(uniq)))
    for l in uniq:
        p = l.lstrip("/")
        base_dir = ROOT if lang == "pt-BR" else os.path.join(ROOT, "en")
        tgt = os.path.join(base_dir, p, "index.html")
        ck(os.path.isfile(tgt), "%s link quebrado: %s" % (path, l))
    print("   links:", uniq)
    # mandatory link_to targets present in body
    hub = "/como-jogar-mahjong/" if lang == "pt-BR" else "/how-to-play-mahjong/"
    ck(hub in uniq, "%s sem link para hub" % path)
    ck("/jogar-mahjong/" in uniq, "%s sem link para /jogar-mahjong/" % path)

# banned terms
banned_pt = ["vale ressaltar", "é importante destacar", "em suma", "por fim, conclui",
             "nos dias de hoje", "no mundo atual", "mergulhe", "desvende", "eleve",
             "reino", "testemunho de", "robusto", "perfeito para", "além disso, além"]
banned_en = ["in today's", "when it comes to", "it's important to note", "let's dive",
             "in conclusion", "delve", "unlock", "elevate", "seamless", "game-changer",
             "robust", "realm", "testament to", "furthermore", "moreover", "landscape"]
for path, banned in ((PT_FILE, banned_pt), (EN_FILE, banned_en)):
    t = body_only(open(path, encoding="utf-8").read()).lower()
    hits = [b for b in banned if b in t]
    ck(not hits, "%s termos banidos: %s" % (path, hits))

# ---------------------------------------------------------------- 3. hubs + csv
pt_hub = open(os.path.join(ROOT, "como-jogar-mahjong", "index.html"), encoding="utf-8").read()
en_hub = open(os.path.join(ROOT, "en", "how-to-play-mahjong", "index.html"), encoding="utf-8").read()
ck(PT_URL in pt_hub, "hub PT sem a nova URL")
ck(EN_URL in en_hub, "hub EN sem a nova URL")


def hub_count(h):
    m = re.search(r'<ul[^>]*id="article-index"[^>]*>(.*?)</ul>', h, re.S)
    return len(re.findall(r"<li>", m.group(1)))


ck(hub_count(pt_hub) == 23, "hub PT itens %d" % hub_count(pt_hub))
ck(hub_count(en_hub) == 23, "hub EN itens %d" % hub_count(en_hub))
# no PT title leaking into EN hub and vice versa
ck("trinca no Mahjong" in pt_hub, "hub PT titulo ausente")
ck("Pung in Mahjong" in en_hub, "hub EN titulo errado")
ck("trinca" not in en_hub, "hub EN contem texto PT")

csv = open(os.path.join(ROOT, "content", "keywords.csv"), encoding="utf-8").read()
row = [l for l in csv.splitlines() if l.startswith("47,")][0]
ck(",Gerado,2026-11-25," in row, "CSV status/data errados: %s" % row)
ck(csv.count(",Pendente,") == 61, "CSV pendentes: %d" % csv.count(",Pendente,"))

# ---------------------------------------------------------------- 4. structural parity
def skel(h):
    a = body_only(h)
    a = re.sub(r">[^<>]*<", "><", a)
    return re.findall(r"</?([a-z0-9]+)[^>]*>", a)


sp, se = skel(open(PT_FILE, encoding="utf-8").read()), skel(open(EN_FILE, encoding="utf-8").read())
ck(sp == se, "paridade estrutural PT/EN: %d vs %d" % (len(sp), len(se)))
print("tags PT/EN:", len(sp), len(se))

# ---------------------------------------------------------------- 5. shingles vs neighbours
def shingles(t, k=10):
    w = re.findall(r"[a-zà-ÿ0-9']+", t.lower())
    return {" ".join(w[i:i + k]) for i in range(len(w) - k + 1)}


new_pt = shingles(re.sub(r"<[^>]+>", " ", body_only(open(PT_FILE, encoding="utf-8").read())))
new_en = shingles(re.sub(r"<[^>]+>", " ", body_only(open(EN_FILE, encoding="utf-8").read())))
for paths, new, is_en in ((glob.glob(os.path.join(ROOT, "como-jogar-mahjong", "*", "index.html")), new_pt, False),
                          (glob.glob(os.path.join(ROOT, "en", "how-to-play-mahjong", "*", "index.html")), new_en, True)):
    reported = []
    for p in paths:
        if "como-fazer-trinca" in p or "how-to-make-pung" in p:
            continue
        h = open(p, encoding="utf-8").read()
        t = shingles(re.sub(r"<[^>]+>", " ", body_only(h)))
        inter = len(new & t)
        if inter:
            reported.append((inter, os.path.basename(os.path.dirname(p))))
    reported.sort(reverse=True)
    ck(not any(n >= 3 for n, _ in reported), "%s shingle >=3: %s" % ("EN" if is_en else "PT", reported[:4]))
    print(("EN" if is_en else "PT"), "shingle overlaps:", reported[:5] if reported else "none")

print("\nCHECKS:", checks, "FAILS:", len(fails))
for f in fails:
    print(" FAIL:", f)
print("RESULT:", "PASS" if not fails else "FAIL")
