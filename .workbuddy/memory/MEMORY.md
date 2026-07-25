# JogoMahjong 项目记忆

## 项目概要
- 域名：jogomahjong.com（葡语 pt-BR）、en.jogomahjong.com（英语）
- 联系邮箱：hello@jogomahjong.com
- 目标：巴西葡语 + 英语麻将游戏网站，SEO + 广告变现
- 部署：Cloudflare Pages（直接托管根目录静态文件）
- GitHub：https://github.com/Zhou-Xiaoyong/jogomahjong.com（main 分支）
- 开源游戏引擎：ffalt/mah（MIT License，仅 mahjong-classico 用其 iframe）

## 重要架构事实（纠正旧 Astro 记忆）
- **仓库当前是构建后的静态站点（纯 HTML/CSS/JS），不是 Astro 源码。** 其他代理已把 dist 直接提交到 main。
- 根 `index.html` = PT 首页；`/en/` 目录 = EN 版本（由 en.jogomahjong.com 域名served）。
- 本地工作副本：E:\WorkBuddy\jm_work（对 main 的 sparse clone，排除 mahjong-classico/mah-app 484 文件第三方目录以避免克隆卡死）。
- 工作流约定：本地修改 → 验证 → **等用户明确确认后再 push**（用户多次强调不要擅自推送）。

## 游戏模式（共 11 个，vanilla JS 引擎在 /assets/）
- Solitário → game.js（/jogar-mahjong/）
- Clássico → ffalt/mah 第三方 iframe（mahjong-classico/mah-app/）
- Connect → connect.js（/mahjong-connect/）
- Cadeia → chain.js（/mahjong-cadeia/）
- Pirâmide → pyramid.js
- Cronometrado → timed.js
- Relaxante → relax.js
- Memória → memory.js
- Torre → tower.js
- Blitz → blitz.js
- Deslize → slide.js
- 英语变体：对应 *-en.js（game-en.js 等）；共享牌定义 tiles-data.js / tiles-data-en.js
- 牌面：Unicode 麻将牌 + I.Mahjong 字体（M+ License，开源）

## 设计系统（实测 styles.css :root，非旧记忆的 #C41E3A）
- --chinese-red: #b91c1c / --chinese-gold: #c9972a / --chinese-green: #2d5a27
- --bg: #f7f0e3（米白）/ --brand: #0f6b58 / --paper: #fffaf0 / --ink: #24170f
- 正文：Georgia, "Times New Roman", serif
- 标题/牌面装饰字体：I.Mahjong（@font-face 引用 /assets/I.Mahjong-TW.otf）

## 页面结构（15 PT + 15 EN，一一对应）
PT 根：`/`、`jogar-mahjong`、`mahjong-{connect,cadeia,piramide,cronometrado,relaxante,torre,blitz,deslize,classico}`、`memoria-mahjong`、`cultura-mahjong`、`como-jogar-mahjong`、`politica-de-privacidade`
EN 对应：`en/index.html` + `en/<同名>`（其中 culture-mahjong / how-to-play-mahjong / privacy-policy 路径与 PT 不同）

## SEO 现状
- schema.org：WebSite / ItemList（11 个 VideoGame）/ VideoGame / FAQPage
- hreflang：每页三向互链 pt-BR / en / x-default
- robots.txt 指向各自 sitemap；根 sitemap.xml 与 en/sitemap.xml 均已含 xhtml:link 跨语言互指

## 长尾内容更新管线（2026-07-25 建立）
- 目标：按长尾词库每周 1 篇更新 Culture（`cultura-mahjong/`）与 How to play（`como-jogar-mahjong/`）栏目。
- 词库：`content/keywords.csv`（108 词，Culture/HowTo 各 54，按 C,C,H,H 交错排布；列：seq,keyword_pt,keyword_en,category,section,slug_pt,slug_en,intent,priority,link_to,link_from,status,published_date,notes）。status 初为 Pendente，生成后改 Gerado。
- 文章模板：`content/article-template.html`（PT）、`content/article-template-en.html`（EN），用 {{PLACEHOLDER}} 填充（TITLE/DESCRIPTION/CANONICAL_PT/CANONICAL_EN/JSON_*/EYEBROW/H1/LEAD/BODY/RELATED_LINKS/SECTION_LABEL_*/HUB_URL_*）。
- 文章落地路径：PT `cultura-mahjong|<como-jogar-mahjong>/<slug_pt>/index.html`；EN `en/culture-mahjong|<how-to-play-mahjong>/<slug_en>/index.html`。
- 内链机制（双向）：(a) hub 页 `<ul id="article-index">` 由 helper 追加 li（老页→新文）；(b) 新文 BODY/RELATED_LINKS/SIDEBOX 链向 link_to 游戏页与兄弟文（新文→老页）；(c) link_from 游戏页首个 `.sidebox ul` 由 helper 注入 li（老页→新文）。
- 接线脚本：`content/update_indexes.py`（幂等）：写 hub 索引 + 两 sitemap（xhtml:link 跨语言）+ 改 CSV 状态。调用：`python content/update_indexes.py --section <Culture|HowTo> --slug-pt <slug> --slug-en <slug> --title-pt ".." --title-en ".." --date <YYYY-MM-DD>`。
- 自动化任务：`automation-1784994289655`（每周一 ACTIVE），读 CSV 取首个 Pendente → 写 PT+EN 文章 → 跑 update_indexes.py → **不 push**（遵循用户"检查后再同步"）。
- 关键坑：EN 文章 URL 无 `en/` 前缀（en 域根即对应 en/ 目录）；sitemap 的 en alternate 不能写成 `en.jogomahjong.com/en/...`（已修）。
- 已生成样例：seq=1 `cultura-mahjong/historia-do-mahjong/`（PT+EN），status=Gerado，作为模板参考。

## 网络/工具特殊配置
- GitHub clone 极慢且可能超时；用 sparse clone + `--filter=blob:none --depth 1` 并排除 mahjong-classico/mah-app
- 需 `git config --global http.sslVerify false` 或 `GIT_SSL_NO_VERIFY=1`
- WebFetch 对 iframe 游戏页只能取元数据；取原始 HTML 用 curl（带浏览器 UA）或 Python urllib（ssl.CERT_NONE）
- 托管 Python 用 Windows 路径（如 E:\WorkBuddy\jm_work），os.getcwd() 在 Git Bash cwd 下返回 Windows 形式
