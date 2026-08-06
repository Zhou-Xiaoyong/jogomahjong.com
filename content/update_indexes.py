# -*- coding: utf-8 -*-
"""Helper de wiring para o pipeline de conteúdo semanal do Jogo Mahjong.
Operações idempotentes:
  1. Insere o novo artigo no <ul id="article-index"> dos hubs PT e EN (hub -> artigo).
  2. Adiciona <url> com xhtml:link alternates nos sitemaps PT e EN.
  3. Injeta link do artigo nas páginas de jogo indicadas em link_from (pagina antiga -> artigo novo).
  4. Marca a linha do CSV como 'Gerado' com a data.
Uso:
  python content/update_indexes.py --section Culture --slug-pt historia-do-mahjong \
      --slug-en history-of-mahjong --title-pt "História do Mahjong" \
      --title-en "History of Mahjong" --date 2026-07-27
"""
import argparse, csv, os, re, sys

ROOT = os.getcwd()
CSV_PATH = os.path.join(ROOT, "content", "keywords.csv")
SITEMAP_PT = os.path.join(ROOT, "sitemap.xml")
SITEMAP_EN = os.path.join(ROOT, "en", "sitemap.xml")

CONFIG = {
    "Culture": {
        "hub_pt": "cultura-mahjong/index.html",
        "hub_en": "en/culture-mahjong/index.html",
        "art_pt_dir": "cultura-mahjong/{slug}",
        "art_en_dir": "culture-mahjong/{slug}",
        "hub_url_pt": "/cultura-mahjong/",
        "hub_url_en": "/culture-mahjong/",
    },
    "HowTo": {
        "hub_pt": "como-jogar-mahjong/index.html",
        "hub_en": "en/how-to-play-mahjong/index.html",
        "art_pt_dir": "como-jogar-mahjong/{slug}",
        "art_en_dir": "how-to-play-mahjong/{slug}",
        "hub_url_pt": "/como-jogar-mahjong/",
        "hub_url_en": "/how-to-play-mahjong/",
    },
}

def url_to_path(u):
    p = u.strip().lstrip("/")
    if p.endswith("/"):
        p += "index.html"
    return p

def inject_hub_index(hub_file, art_url, title):
    path = os.path.join(ROOT, hub_file)
    if not os.path.isfile(path):
        print("WARN hub ausente:", hub_file); return False
    s = open(path, encoding="utf-8").read()
    if art_url in s:
        print("SKIP hub index (ja existe):", hub_file); return False
    m = re.search(r'(<ul[^>]*id="article-index"[^>]*>)(.*?)(</ul>)', s, re.DOTALL)
    if not m:
        print("WARN sem <ul id=article-index> em:", hub_file); return False
    li = f'            <li><a href="{art_url}">{title}</a></li>\n'
    new = s[:m.end(2)] + li + s[m.start(3):]
    open(path, "w", encoding="utf-8").write(new)
    print("OK hub index:", hub_file)
    return True

def add_sitemap(sitemap_file, loc_primary, loc_pt, loc_en, date):
    """loc_primary e a URL que pertence ao dominio deste sitemap."""
    if not os.path.isfile(sitemap_file):
        print("WARN sitemap ausente:", sitemap_file); return False
    s = open(sitemap_file, encoding="utf-8").read()
    if loc_primary in s:
        print("SKIP sitemap (ja existe):", sitemap_file); return False
    block = (
        "  <url>\n"
        f"    <loc>{loc_primary}</loc>\n"
        f'    <xhtml:link rel="alternate" hreflang="pt-BR" href="{loc_pt}"/>\n'
        f'    <xhtml:link rel="alternate" hreflang="en" href="{loc_en}"/>\n'
        f'    <xhtml:link rel="alternate" hreflang="x-default" href="{loc_pt}"/>\n'
        f"    <lastmod>{date}</lastmod>\n"
        "  </url>\n"
    )
    s = s.replace("</urlset>", block + "</urlset>", 1)
    open(sitemap_file, "w", encoding="utf-8").write(s)
    print("OK sitemap:", sitemap_file)
    return True

def inject_link_from(game_url, art_url, title, prefix=""):
    if game_url.rstrip("/").endswith("cultura-mahjong") or game_url.rstrip("/").endswith("como-jogar-mahjong"):
        return False  # hub já tratado pelo índice
    path = os.path.join(ROOT, prefix, url_to_path(game_url)) if prefix else os.path.join(ROOT, url_to_path(game_url))
    if not os.path.isfile(path):
        print("WARN link_from ausente:", game_url); return False
    s = open(path, encoding="utf-8").read()
    if art_url in s:
        return False
    m = re.search(r'(<aside class="sidebox">.*?<ul>)(.*?)(</ul>)', s, re.DOTALL)
    if not m:
        print("WARN sem sidebox ul em:", game_url); return False
    li = f'              <li><a href="{art_url}">{title}</a></li>\n'
    new = s[:m.end(2)] + li + s[m.start(3):]
    open(path, "w", encoding="utf-8").write(new)
    print("OK link_from:", game_url)
    return True

def update_csv(slug_pt, date):
    rows = []
    changed = False
    with open(CSV_PATH, encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        fieldnames = r.fieldnames
        for row in r:
            if row["slug_pt"] == slug_pt and row["status"] == "Pendente":
                row["status"] = "Gerado"
                row["published_date"] = date
                changed = True
            rows.append(row)
    if changed:
        with open(CSV_PATH, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(rows)
        print("OK csv status Gerado:", slug_pt)
    else:
        print("SKIP csv (status ja atualizado ou slug nao encontrado):", slug_pt)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--section", required=True, choices=["Culture", "HowTo"])
    ap.add_argument("--slug-pt", required=True)
    ap.add_argument("--slug-en", required=True)
    ap.add_argument("--title-pt", required=True)
    ap.add_argument("--title-en", required=True)
    ap.add_argument("--date", required=True)
    a = ap.parse_args()

    cfg = CONFIG[a.section]
    art_pt_url = "https://jogomahjong.com/" + cfg["art_pt_dir"].format(slug=a.slug_pt) + "/"
    art_en_url = "https://en.jogomahjong.com/" + cfg["art_en_dir"].format(slug=a.slug_en) + "/"

    inject_hub_index(cfg["hub_pt"], art_pt_url, a.title_pt)
    inject_hub_index(cfg["hub_en"], art_en_url, a.title_en)
    add_sitemap(SITEMAP_PT, art_pt_url, art_pt_url, art_en_url, a.date)
    add_sitemap(SITEMAP_EN, art_en_url, art_pt_url, art_en_url, a.date)

    # link_from a partir do CSV
    with open(CSV_PATH, encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            if row["slug_pt"] == a.slug_pt:
                for g in row["link_from"].split("|"):
                    g = g.strip()
                    if g:
                        inject_link_from(g, art_pt_url, a.title_pt)
                        inject_link_from(g, art_en_url, a.title_en, prefix="en")
                break

    update_csv(a.slug_pt, a.date)
    print("DONE", art_pt_url)

if __name__ == "__main__":
    main()
