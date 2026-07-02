# Jogo Mahjong

Site estático em português do Brasil para `jogomahjong.com`.

## Estrutura

- `index.html` — página inicial otimizada para `jogo de mahjong grátis online`
- `jogar-mahjong/` — página principal do jogo
- `como-jogar-mahjong/` — guia SEO para termos como `como jogar mahjong` e `mahjong solitário`
- `politica-de-privacidade/` — página necessária para monetização e confiança
- `assets/styles.css` — estilo visual do site
- `assets/game.js` — jogo HTML5 original, sem imagens de terceiros
- `robots.txt` e `sitemap.xml` — arquivos de SEO
- `ads.txt` — placeholder para Google AdSense

## Deploy no Cloudflare Pages

1. Suba esta pasta para um repositório Git.
2. No Cloudflare Pages, escolha o repositório.
3. Build command: deixe vazio.
4. Build output directory: `/` ou a raiz desta pasta.
5. Configure o domínio `jogomahjong.com`.

## Depois do deploy

1. Verifique o domínio no Google Search Console.
2. Envie `https://jogomahjong.com/sitemap.xml`.
3. Configure o Google AdSense somente depois que o site estiver indexado e com conteúdo suficiente.
4. Substitua o placeholder em `ads.txt` pelo ID real do AdSense.
