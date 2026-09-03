# -*- coding: utf-8 -*-
"""Regenera sitemap.xml (PT) e en/sitemap.xml (EN) escaneando o disco.
Preserva lastmod das paginas nao alteradas; usa hoje para paginas novas.
Valida: XML valido, sem <loc> duplicado, sem '.html', contagem bate com disco, sem noindex.
"""
import os, re, datetime, sys
import xml.etree.ElementTree as ET

ROOT = os.getcwd()
TODAY = datetime.date.today().isoformat()
NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
XH = "http://www.w3.org/1999/xhtml"

SKIP_DIRS = {"en", "content", "assets", "functions", ".workbuddy"}


def load_lastmod(path):
    d = {}
    if not os.path.isfile(path):
        return d
    try:
        for url in ET.parse(path).getroot().findall(f"{{{NS}}}url"):
            loc = url.find(f"{{{NS}}}loc")
            lm = url.find(f"{{{NS}}}lastmod")
            if loc is not None and loc.text:
                d[loc.text.strip()] = (lm.text.strip() if (lm is not None and lm.text) else TODAY)
    except Exception as e:
        print("WARN parsing", path, e)
    return d


def scan_pt():
    pages = []
    for dp, dn, fn in os.walk(ROOT):
        rel = os.path.relpath(dp, ROOT).replace("\\", "/")
        parts = rel.split("/") if rel != "." else []
        if parts and parts[0] in SKIP_DIRS:
            dn[:] = []; continue
        if any(p.startswith(".") for p in parts):
            dn[:] = []; continue
        for f in fn:
            if f.endswith(".html"):
                pages.append(os.path.relpath(os.path.join(dp, f), ROOT).replace("\\", "/"))
    return pages


def scan_en():
    pages = []
    enroot = os.path.join(ROOT, "en")
    if not os.path.isdir(enroot):
        return pages
    for dp, dn, fn in os.walk(enroot):
        rel = os.path.relpath(dp, enroot).replace("\\", "/")
        parts = rel.split("/") if rel != "." else []
        if any(p.startswith(".") for p in parts):
            dn[:] = []; continue
        for f in fn:
            if f.endswith(".html"):
                pages.append(os.path.relpath(os.path.join(dp, f), enroot).replace("\\", "/"))
    return pages


def parse_head(html):
    canonical = re.search(r'<link rel="canonical" href="([^"]+)"', html)
    en_alt = re.search(r'hreflang="en" href="([^"]+)"', html)
    pt_alt = re.search(r'hreflang="pt-BR" href="([^"]+)"', html)
    return (canonical.group(1).strip() if canonical else None,
            en_alt.group(1).strip() if en_alt else None,
            pt_alt.group(1).strip() if pt_alt else None)


def is_noindex(html):
    m = re.search(r'<meta name="robots" content="([^"]*)"', html, re.I)
    return bool(m and "noindex" in m.group(1).lower())


def make_url(loc, alt_pt, alt_en, xdefault, lastmod):
    u = ET.Element(f"{{{NS}}}url")
    ET.SubElement(u, f"{{{NS}}}loc").text = loc
    for hl, href in (("pt-BR", alt_pt), ("en", alt_en), ("x-default", xdefault)):
        a = ET.SubElement(u, f"{{{XH}}}link")
        a.set("rel", "alternate"); a.set("hreflang", hl); a.set("href", href)
    ET.SubElement(u, f"{{{NS}}}lastmod").text = lastmod
    ET.SubElement(u, f"{{{NS}}}changefreq").text = "weekly"
    ET.SubElement(u, f"{{{NS}}}priority").text = "0.9"
    return u


def build_sitemap(pages, is_en, lastmod_map):
    root = ET.Element(f"{{{NS}}}urlset")
    entries = []
    for relp in pages:
        full = os.path.join(ROOT, relp if not is_en else os.path.join("en", relp))
        html = open(full, encoding="utf-8").read()
        if is_noindex(html) or "404" in relp:
            print("SKIP noindex/404:", relp); continue
        canonical, en_alt, pt_alt = parse_head(html)
        if not canonical:
            print("WARN sem canonical:", relp); continue
        if is_en:
            loc = canonical
            alt_pt = pt_alt or canonical
            alt_en = canonical
            xdefault = canonical
        else:
            loc = canonical
            alt_pt = canonical
            alt_en = en_alt or canonical
            xdefault = canonical
        lm = lastmod_map.get(loc, TODAY)
        entries.append((loc, make_url(loc, alt_pt, alt_en, xdefault, lm)))
    # ordena por loc para estabilidade
    entries.sort(key=lambda x: x[0])
    for _, u in entries:
        root.append(u)
    return root, len(entries)


def write_sitemap(path, root):
    ET.register_namespace("s", NS)
    ET.register_namespace("xhtml", XH)
    ET.ElementTree(root).write(path, encoding="utf-8", xml_declaration=True)
    print("WROTE", path)


def validate(pt_count, en_count):
    ok = True
    for label, path, expect in (("PT", os.path.join(ROOT, "sitemap.xml"), pt_count),
                                ("EN", os.path.join(ROOT, "en", "sitemap.xml"), en_count)):
        raw = open(path, encoding="utf-8").read()
        tree = ET.parse(path)  # XML valido?
        locs = [u.find(f"{{{NS}}}loc").text for u in tree.getroot().findall(f"{{{NS}}}url")]
        if len(locs) != len(set(locs)):
            print("FAIL", label, "loc duplicado"); ok = False
        if ".html" in raw:
            print("FAIL", label, "ainda ha .html em <loc>"); ok = False
        if len(locs) != expect:
            print("FAIL", label, f"contagem {len(locs)} != disco {expect}"); ok = False
        print(f"OK {label} sitemap: {len(locs)} urls, sem .html, sem duplicados")
    return ok


def main():
    pt_lm = load_lastmod(os.path.join(ROOT, "sitemap.xml"))
    en_lm = load_lastmod(os.path.join(ROOT, "en", "sitemap.xml"))
    pt_pages = scan_pt()
    en_pages = scan_en()
    pt_root, pt_n = build_sitemap(pt_pages, False, pt_lm)
    en_root, en_n = build_sitemap(en_pages, True, en_lm)
    write_sitemap(os.path.join(ROOT, "sitemap.xml"), pt_root)
    write_sitemap(os.path.join(ROOT, "en", "sitemap.xml"), en_root)
    if not validate(pt_n, en_n):
        print("VALIDACAO FALHOU"); sys.exit(1)
    print("REGEN OK")


if __name__ == "__main__":
    main()
