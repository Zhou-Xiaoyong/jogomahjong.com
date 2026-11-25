# -*- coding: utf-8 -*-
"""Live check after push for seq=47."""
import ssl, time, urllib.request

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

TARGETS = [
    ("PT art", "https://jogomahjong.com/como-jogar-mahjong/como-fazer-trinca-mahjong/", "três peças iguais e a chamada"),
    ("EN art", "https://en.jogomahjong.com/how-to-play-mahjong/how-to-make-pung-mahjong/", "Three of a Kind From Any Seat"),
    ("PT hub", "https://jogomahjong.com/como-jogar-mahjong/", "como-fazer-trinca-mahjong"),
    ("EN hub", "https://en.jogomahjong.com/how-to-play-mahjong/", "how-to-make-pung-mahjong"),
    ("PT sitemap", "https://jogomahjong.com/sitemap.xml", "como-fazer-trinca-mahjong"),
    ("EN sitemap", "https://en.jogomahjong.com/sitemap.xml", "how-to-make-pung-mahjong"),
]


def fetch(url, tries=4, timeout=40):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
            with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
                return r.status, r.read().decode("utf-8", "replace")
        except Exception as e:
            last = e
            time.sleep(2)
    return None, "ERR %s" % last


for name, url, needle in TARGETS:
    st, body = fetch(url)
    ok = needle in body
    extra = ""
    if url.endswith("sitemap.xml"):
        extra = " locs=%d html=%d" % (body.count("<loc>") + body.count("<s:loc>"), body.count(".html"))
    print("%-11s %s bytes=%-6d needle=%s%s" % (name, st, len(body), "OK" if ok else "MISSING", extra))
