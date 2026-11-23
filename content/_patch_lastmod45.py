# -*- coding: utf-8 -*-
"""Aplica lastmod=2026-11-23 nas URLs tocadas nesta rodada (2 artigos + 2 hubs)."""
import os
import xml.etree.ElementTree as ET

ROOT = os.getcwd()
NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
XH = "http://www.w3.org/1999/xhtml"
TODAY = "2026-11-23"

TARGETS = {
    os.path.join(ROOT, "sitemap.xml"): {
        "https://jogomahjong.com/cultura-mahjong/mahjong-feng-shui/",
        "https://jogomahjong.com/cultura-mahjong/",
    },
    os.path.join(ROOT, "en", "sitemap.xml"): {
        "https://en.jogomahjong.com/culture-mahjong/mahjong-feng-shui/",
        "https://en.jogomahjong.com/culture-mahjong/",
    },
}

for path, targets in TARGETS.items():
    tree = ET.parse(path)
    root = tree.getroot()
    hits = 0
    for u in root.findall(f"{{{NS}}}url"):
        loc = u.find(f"{{{NS}}}loc").text.strip()
        if loc in targets:
            lm = u.find(f"{{{NS}}}lastmod")
            lm.text = TODAY
            hits += 1
            print("lastmod", loc)
    ET.register_namespace("s", NS)
    ET.register_namespace("xhtml", XH)
    tree.write(path, encoding="utf-8", xml_declaration=True)
    raw = open(path, encoding="utf-8").read()
    raw = raw.replace("ns0:", "s:")
    open(path, "w", encoding="utf-8", newline="\n").write(raw)
    print(f"{os.path.basename(path)}: {hits}/{len(targets)} marcados")
