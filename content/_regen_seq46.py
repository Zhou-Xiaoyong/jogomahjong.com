# -*- coding: utf-8 -*-
"""Full sitemap regeneration for seq=46.

Scans every indexable page on disk, builds loc from each page's own canonical,
keeps existing lastmod, stamps TODAY on pages added/modified in this run.
"""
import os, re
import xml.etree.ElementTree as ET

ROOT = os.getcwd()
TODAY = "2026-11-24"
NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
XH = "http://www.w3.org/1999/xhtml"

SKIP_DIRS = {"en", "content", "assets", "functions", ".workbuddy", ".git", "mah-app"}

MODIFIED = {
    "https://jogomahjong.com/cultura-mahjong/mahjong-zodiaco-chines/",
    "https://en.jogomahjong.com/culture-mahjong/mahjong-chinese-zodiac/",
    "https://jogomahjong.com/cultura-mahjong/",
    "https://en.jogomahjong.com/culture-mahjong/",
}


def load_lastmod(path):
    d = {}
    if not os.path.isfile(path):
        return d
    for url in ET.parse(path).getroot().findall(f"{{{NS}}}url"):
        loc = url.find(f"{{{NS}}}loc")
        lm = url.find(f"{{{NS}}}lastmod")
        if loc is not None and loc.text:
            d[loc.text.strip()] = (lm.text.strip() if (lm is not None and lm.text) else TODAY)
    return d


def scan(base):
    out = []
    for dp, dn, fn in os.walk(base):
        rel = os.path.relpath(dp, base).replace("\\", "/")
        parts = [] if rel == "." else rel.split("/")
        if parts and (parts[0] in SKIP_DIRS or any(p.startswith(".") for p in parts)):
            dn[:] = []
            continue
        for f in fn:
            if f.endswith(".html"):
                out.append(os.path.relpath(os.path.join(dp, f), base).replace("\\", "/"))
    return out


def is_noindex(h):
    m = re.search(r'<meta name="robots" content="([^"]*)"', h, re.I)
    return bool(m and "noindex" in m.group(1).lower())


def build(pages, base, is_en, lm_map):
    root = ET.Element(f"{{{NS}}}urlset")
    rows = []
    for relp in pages:
        full = os.path.join(base, relp)
        html = open(full, encoding="utf-8").read()
        if is_noindex(html) or "404" in relp:
            print("SKIP noindex/404:", relp)
            continue
        can = re.search(r'<link rel="canonical" href="([^"]+)"', html)
        pt = re.search(r'hreflang="pt-BR" href="([^"]+)"', html)
        en = re.search(r'hreflang="en" href="([^"]+)"', html)
        if not can:
            print("WARN sem canonical:", relp)
            continue
        loc = can.group(1).strip()
        alt_pt = (pt.group(1).strip() if pt else loc)
        alt_en = (en.group(1).strip() if en else loc)
        if is_en and alt_en != loc:
            print("WARN en alternate != loc:", relp, alt_en, loc)
        lm = TODAY if loc in MODIFIED else lm_map.get(loc, TODAY)
        u = ET.SubElement(root, f"{{{NS}}}url")
        ET.SubElement(u, f"{{{NS}}}loc").text = loc
        for hl, href in (("pt-BR", alt_pt), ("en", alt_en), ("x-default", alt_pt)):
            a = ET.SubElement(u, f"{{{XH}}}link")
            a.set("rel", "alternate")
            a.set("hreflang", hl)
            a.set("href", href)
        ET.SubElement(u, f"{{{NS}}}lastmod").text = lm
        ET.SubElement(u, f"{{{NS}}}changefreq").text = "weekly"
        ET.SubElement(u, f"{{{NS}}}priority").text = "0.9"
        rows.append(loc)
    pairs = sorted(zip(rows, list(root)), key=lambda x: x[0])
    root[:] = [u for _, u in pairs]
    return root, [r for r, _ in pairs]


def main():
    ET.register_namespace("s", NS)
    ET.register_namespace("xhtml", XH)
    pt_lm = load_lastmod(os.path.join(ROOT, "sitemap.xml"))
    en_lm = load_lastmod(os.path.join(ROOT, "en", "sitemap.xml"))

    pt_pages = scan(ROOT)
    en_pages = scan(os.path.join(ROOT, "en"))

    pt_root, pt_locs = build(pt_pages, ROOT, False, pt_lm)
    en_root, en_locs = build(en_pages, os.path.join(ROOT, "en"), True, en_lm)

    ET.ElementTree(pt_root).write(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8", xml_declaration=True)
    ET.ElementTree(en_root).write(os.path.join(ROOT, "en", "sitemap.xml"), encoding="utf-8", xml_declaration=True)
    print("PT files scanned:", len(pt_pages), "-> locs", len(pt_locs))
    print("EN files scanned:", len(en_pages), "-> locs", len(en_locs))
    print("NEW PT present:", "https://jogomahjong.com/cultura-mahjong/mahjong-zodiaco-chines/" in pt_locs)
    print("NEW EN present:", "https://en.jogomahjong.com/culture-mahjong/mahjong-chinese-zodiac/" in en_locs)
    for f in ("sitemap.xml", os.path.join("en", "sitemap.xml")):
        raw = open(os.path.join(ROOT, f), encoding="utf-8").read()
        print(f, "html hits:", raw.count(".html"))


if __name__ == "__main__":
    main()
