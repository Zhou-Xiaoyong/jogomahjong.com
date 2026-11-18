# -*- coding: utf-8 -*-
"""Build seq=41: mahjong tradicional vs moderno (PT) / traditional vs modern mahjong (EN)."""
import os, re, sys

ROOT = os.getcwd()
SLUG_PT = "mahjong-tradicional-vs-moderno"
SLUG_EN = "traditional-vs-modern-mahjong"
ART_PT = os.path.join(ROOT, "cultura-mahjong", SLUG_PT)
ART_EN = os.path.join(ROOT, "en", "culture-mahjong", SLUG_EN)
CANON_PT = f"https://jogomahjong.com/cultura-mahjong/{SLUG_PT}/"
CANON_EN = f"https://en.jogomahjong.com/culture-mahjong/{SLUG_EN}/"

# ---------------- PORTUGUES ----------------
PT_TITLE = "Mahjong tradicional e mahjong moderno: a mesma mesa, quatro caixas diferentes"
PT_DESC = ("Quatro conjuntos, quatro contagens: 144, 136, 152 e 108 peças. O que o mahjong moderno "
           "mudou de fato e o que nenhuma versão mexeu.")
PT_EYEBROW = "Cultura · Variações"
PT_LEAD = ("Um conjunto de Xangai dos anos 1920 traz 144 peças. Um japonês traz 136, um americano 152 "
           "e um de Chengdu 108. O jogo é o mesmo nas quatro caixas, e é aí que a diferença começa.")

PT_BODY = """
<h2>Quatro caixas, quatro contagens</h2>
<p>As 144 peças do conjunto clássico saem de uma soma simples: 108 de naipe (três naipes de 36), 16 ventos, 12 dragões e 8 peças de flor e estação. Foi esse número que atravessou o porto de Xangai nos anos 1920, dentro de caixas de madeira com palitos de ponto.</p>
<p>O Japão tirou as oito flores e ficou com 136. A subtração abriu espaço para a parede morta, catorze peças separadas em sete montes que servem de reserva para cada kong e de onde sai o indicador de dora antes do primeiro descarte.</p>
<p>Os Estados Unidos fizeram o contrário e somaram oito coringas às 144, chegando a 152. O coringa não é peça livre: ele só vale dentro de uma mão que está impressa no cartão do ano.</p>
<p>Sichuan cortou mais fundo. Cento e oito peças, três naipes, nenhum vento e nenhum dragão. A mão fecha em metade do tempo, e a mesa compensa com uma regra em que ninguém levanta quando alguém ganha.</p>

<h2>O piso: a invenção mais moderna da mesa</h2>
<p>Aqui está o ponto que mais atrapalha quem aprendeu a jogar em casa. Na mesa de família, qualquer mão fechada vale. Na mesa moderna, a mão precisa de nome.</p>
<p>No riichi, isso se chama yaku: pelo menos um padrão nomeado, sempre. Quatro dora na mão não pagam nada se não houver padrão, porque dora multiplica uma mão que já pontua e não cria valor do zero. Nas regras de competição chinesa publicadas em 1998, são 81 padrões e um mínimo de 8 pontos para declarar. Nos Estados Unidos, a combinação tem que estar no cartão da liga nacional, que muda todo ano: uma mão bonita que não está impressa ali não pode ser anunciada.</p>
<p>O piso não é esnobismo de torneio. Ele muda a decisão. Sem piso, você descarta o que não serve e espera. Com piso, você descarta uma mão quase pronta porque ela não tem nome.</p>

<h2>Duas marcas que denunciam a versão</h2>
<p>Se você sentar numa mesa americana, olhe o canto das peças de naipe. Os conjuntos de lá imprimem o número em algarismo arábico ao lado do caractere, para quem não lê chinês não precisar decorar a ordem dos círculos. Conjuntos chineses e japoneses não têm essa ajuda.</p>
<p>A segunda marca é o começo da mão. A mesa americana abre com o Charleston, uma troca obrigatória de três peças para a esquerda, três para o lado oposto e três para a direita antes de qualquer compra. Nenhuma mesa chinesa ou japonesa faz isso, e aprender o Charleston é o primeiro choque de quem troca de regra.</p>
<p>A terceira é física. A mesa americana costuma usar estantes com empurrador na frente de cada jogador, e as peças ficam em pé, viradas para quem joga. Na mesa asiática a peça fica deitada no feltro e a parede é construída com as mãos.</p>

<h2>Os palitos viraram tabela</h2>
<p>O conjunto tradicional vinha com palitos de 10, 100 e 500 pontos. A conta era feita na mesa, em voz alta, e cada jogador conferia a do vizinho. Errar era comum, e ninguém perdia a mão por isso.</p>
<p>Depois vieram as tabelas impressas e a conta deixou de ser discussão. Hoje o aplicativo fecha o cálculo antes de você terminar de olhar as peças. O que se perdeu foi a parte social do cálculo, aquela em que quatro pessoas discordam de vinte pontos e chegam a um acordo.</p>

<h2>A mesa que fala e a mesa que cala</h2>
<p>Mesa de casa é barulhenta. Anuncia-se a peça descartada pelo nome, comenta-se a sorte, alguém reclama do vento. Nada disso é regra. É hábito, e muda de bairro para bairro.</p>
<p>Mesa de competição é silenciosa, e tem preço. No riichi, anunciar mahjong sem a mão fechada é chombo: a penalidade usual é de 8.000 pontos pagos à mesa, além da mão perdida.</p>
<p>É a mudança menos visível e a mais profunda. A regra passou a existir para ser aplicada por um terceiro, não negociada entre quatro pessoas que se conhecem.</p>

<h2>O mahjong que nunca foi de mesa</h2>
<p>Em 1981, Brodie Lockard escreveu num sistema de ensino chamado PLATO um jogo com as mesmas 144 peças e nenhuma das regras. Sem adversário, sem compra, sem descarte: só pares iguais retirados de uma pilha, desde que a peça esteja livre dos dois lados.</p>
<p>É o formato que a maioria dos brasileiros conhece como mahjong, e ele não tem vento, dragão nem sequência. Aqui no site o <a href="/jogar-mahjong/">Solitário</a> usa 112 peças em 56 pares, com o desenho de sempre. Nada disso é o jogo de quatro, mas as faces são idênticas, e é por isso que tanta gente chega à mesa achando que já sabe jogar.</p>

<h2>O que não mudou</h2>
<p>Quatro cadeiras. Treze peças na mão, catorze na vez de quem compra. Uma parede que se constrói e se consome pelas duas pontas. Compra, descarte, espera.</p>
<p>Um jogador por vez, no sentido anti-horário, e a sequência só se pede ao vizinho da esquerda. Essa geometria é de antes de 1900 e nenhuma versão moderna mexeu nela, porque é ela que faz o jogo funcionar. Quem está à sua esquerda pode te alimentar. Quem está à direita, não.</p>

<h2>Como escolher a sua mesa</h2>
<p>Se você está começando e tem quatro pessoas, fique na versão de 144 peças sem piso: o <a href="/mahjong-classico/">Clássico</a> com flores e estações, aposta simbólica e conta em voz alta. A mão fecha rápido, o erro é barato e você aprende a ler descarte sem pagar por isso.</p>
<p>A exceção é quem quer competir. Aí o caminho é o inverso: escolha uma regra e fique nela por seis meses. Riichi, competição chinesa e Sichuan premiam coisas diferentes, e trocar de regra toda semana deixa você bom em nenhuma. O <a href="/cultura-mahjong/mahjong-no-japao-riichi/">riichi japonês</a> é o mais fácil de estudar sozinho, porque tem aplicativo que corrige a mão na hora. A versão <a href="/cultura-mahjong/mahjong-nos-eua/">americana</a> é a mais difícil de aprender sem alguém do lado, porque o cartão do ano muda as combinações válidas.</p>
<p>O que sobrou de comum entre as duas pontas está no <a href="/cultura-mahjong/">índice de Cultura</a>: a mesma parede, as mesmas 34 faces e a mesma espera por uma peça que talvez não venha.</p>
"""

PT_RELATED = """              <li><a href="/cultura-mahjong/mahjong-no-japao-riichi/">Mahjong no Japão: como funciona o riichi</a></li>
              <li><a href="/cultura-mahjong/mahjong-nos-eua/">Mahjong nos Estados Unidos: o jogo que mudou de cartão</a></li>
              <li><a href="/mahjong-classico/">Jogar Mahjong Clássico com 144 peças</a></li>
              <li><a href="/jogar-mahjong/">Jogar Mahjong Solitário grátis</a></li>
              <li><a href="/cultura-mahjong/">Todos os artigos de Cultura</a></li>"""

PT_SIDEBOX = """            <li><a href="/jogar-mahjong/">Mahjong Solitário</a></li>"""

# ---------------- ENGLISH ----------------
EN_TITLE = "Traditional and Modern Mahjong: Four Boxes, One Game"
EN_DESC = ("Four sets, four counts: 144, 136, 152 and 108 tiles. What modern mahjong actually changed, "
           "and the part of the table no version has touched.")
EN_EYEBROW = "Culture · Variations"
EN_LEAD = ("A Shanghai set from the 1920s holds 144 tiles. A Japanese set holds 136, an American set 152, "
           "a Chengdu set 108. The loop on the table is the same in all four, and that is where the "
           "comparison gets interesting.")

EN_BODY = """
<h2>Four boxes, four counts</h2>
<p>The 144 comes out of a plain sum: 108 suited tiles (three suits of 36), 16 winds, 12 dragons and 8 flowers and seasons. That is the number that left Shanghai in the 1920s, packed in wooden cases with point sticks.</p>
<p>Japan dropped the eight flowers and kept 136. The subtraction paid for the dead wall, fourteen tiles stacked in seven pairs that refill every kong and hold the dora indicator before the first discard.</p>
<p>The United States went the other way and added eight jokers to the 144, landing on 152. A joker is not a free tile. It only counts inside a hand printed on that year's card.</p>
<p>Chengdu cut deeper: 108 tiles, three suits, no winds and no dragons. Hands close in half the time, and the table makes up for it with a rule where nobody stands up when somebody wins.</p>

<h2>The floor: modern mahjong's real invention</h2>
<p>This is the part that trips up anyone who learned at a kitchen table. In a family game, any closed hand counts. In modern rules, the hand needs a name.</p>
<p>Riichi calls it a yaku: at least one named pattern, every hand. Four dora sitting in your hand pay nothing without one, because dora multiplies a hand that already scores and never builds value from zero. The Chinese competition rules published in 1998 list 81 patterns and demand 8 points before you may declare. In the US, the combination has to appear on the national league's card, which is reissued each year, so a tidy hand that is not printed there cannot be called at all.</p>
<p>The floor is not tournament snobbery. It changes the decision. Without a floor you throw away what does not fit and wait. With one, you throw away a nearly finished hand because it has no name.</p>

<h2>Two tells that give the version away</h2>
<p>Sit at an American table and look at the corner of a suited tile. US sets print the Arabic numeral next to the character, so a player who does not read Chinese never has to memorize the circle order. Chinese and Japanese sets offer no such help.</p>
<p>The second tell is the opening. American mahjong starts with the Charleston, a compulsory pass of three tiles left, three across and three right before anyone draws. No Chinese or Japanese table does this, and the Charleston is the first shock for anyone switching rule sets.</p>
<p>The third is furniture. American play usually puts a rack with a pusher in front of each player and stands the tiles on edge, facing the owner. At an Asian table the tiles lie flat on felt and the wall goes up by hand.</p>

<h2>Sticks became a chart</h2>
<p>An old set came with sticks worth 10, 100 and 500 points. The arithmetic happened out loud at the table, and each player checked the neighbour's count. Mistakes were routine. Nobody lost a hand over one.</p>
<p>Printed scoring charts came next, and the counting stopped being an argument. Now the app settles it before you finish looking at your tiles. What went missing was the social half of the math, the four people who disagree about twenty points and then agree on a number.</p>

<h2>The table that talks, the table that doesn't</h2>
<p>A home table is loud. Discards get announced by name, luck gets discussed, somebody complains about the wind. None of that is a rule. It is habit, and it changes from one neighbourhood to the next.</p>
<p>A competition table is quiet, and it charges for noise. In riichi, calling mahjong on an incomplete hand is chombo: the usual penalty is 8,000 points paid to the table on top of the lost hand.</p>
<p>That is the least visible change and the deepest one. The rule now exists to be enforced by a third party rather than negotiated among four people who know each other.</p>

<h2>The mahjong that was never a table game</h2>
<p>In 1981 Brodie Lockard wrote a game on the PLATO teaching system that used the same 144 tiles and none of the rules. No opponent, no draw, no discard: just matching pairs pulled off a stack as long as the tile is free on both sides.</p>
<p>That is the format most players outside Asia meet first, and it has no winds, no dragons and no runs. Our <a href="/jogar-mahjong/">Solitaire</a> runs 112 tiles in 56 pairs with the familiar faces. None of it is the four-player game, but the artwork is identical, which is why so many people sit down at a real table convinced they already know how to play.</p>

<h2>What never moved</h2>
<p>Four seats. Thirteen tiles in hand, fourteen on the draw. A wall that gets built and eaten from both ends. Draw, discard, wait.</p>
<p>One player at a time, counter-clockwise, and a run can only be claimed from the player on your left. That geometry predates 1900 and no modern version has touched it, because it is what makes the game work. Your left-hand neighbour can feed you. Your right-hand neighbour cannot.</p>

<h2>Picking your table</h2>
<p>If you are new and have four people, stay on the 144-tile game with no floor: the <a href="/mahjong-classico/">Classic</a> set with flowers and seasons, token stakes and the count spoken out loud. Hands close quickly, mistakes are cheap and you learn to read discards without paying tuition.</p>
<p>The exception is anyone who wants to compete. Then reverse it: pick one rule set and stay there for six months. Riichi, Chinese competition and Sichuan reward different skills, and switching every week leaves you good at none. <a href="/culture-mahjong/mahjong-japan-riichi/">Japanese riichi</a> is the easiest to study alone because an app will correct your hand on the spot. The <a href="/culture-mahjong/mahjong-united-states/">American game</a> is the hardest to learn without a patient neighbour, since the yearly card rewrites which hands exist.</p>
<p>What survives at both ends sits in the <a href="/culture-mahjong/">Culture index</a>: the same wall, the same 34 faces and the same wait for a tile that may not come.</p>
"""

EN_RELATED = """              <li><a href="/culture-mahjong/mahjong-japan-riichi/">Mahjong in Japan: how riichi works</a></li>
              <li><a href="/culture-mahjong/mahjong-united-states/">Mahjong in the United States: the game that changes its card</a></li>
              <li><a href="/mahjong-classico/">Play Classic Mahjong with 144 tiles</a></li>
              <li><a href="/jogar-mahjong/">Play Mahjong Solitaire free</a></li>
              <li><a href="/culture-mahjong/">All Culture articles</a></li>"""

EN_SIDEBOX = """            <li><a href="/jogar-mahjong/">Mahjong Solitaire</a></li>"""


def fill(tpl, mapping):
    out = tpl
    for k, v in mapping.items():
        out = out.replace("{{" + k + "}}", v)
    left = re.findall(r"\{\{[A-Z_]+\}\}", out)
    if left:
        print("FAIL placeholders restantes:", left)
        sys.exit(1)
    return out


def body_words(html):
    txt = re.sub(r"<[^>]+>", " ", html)
    return len([w for w in txt.split() if w.strip()])


def main():
    tpl_pt = open(os.path.join(ROOT, "content", "article-template.html"), encoding="utf-8").read()
    tpl_en = open(os.path.join(ROOT, "content", "article-template-en.html"), encoding="utf-8").read()

    pt = fill(tpl_pt, {
        "TITLE": PT_TITLE, "DESCRIPTION": PT_DESC,
        "JSON_HEADLINE": PT_TITLE, "JSON_DESCRIPTION": PT_DESC,
        "CANONICAL_PT": CANON_PT, "CANONICAL_EN": CANON_EN,
        "EYEBROW": PT_EYEBROW, "H1": PT_TITLE, "LEAD": PT_LEAD,
        "BODY": PT_BODY.strip("\n"), "RELATED_LINKS": PT_RELATED,
        "SIDEBOX_PLAY": PT_SIDEBOX, "SECTION_LABEL_PT": "Cultura",
        "HUB_URL_PT": "/cultura-mahjong/",
    })
    en = fill(tpl_en, {
        "TITLE": EN_TITLE, "DESCRIPTION": EN_DESC,
        "JSON_HEADLINE": EN_TITLE, "JSON_DESCRIPTION": EN_DESC,
        "CANONICAL_PT": CANON_PT, "CANONICAL_EN": CANON_EN,
        "EYEBROW": EN_EYEBROW, "H1": EN_TITLE, "LEAD": EN_LEAD,
        "BODY": EN_BODY.strip("\n"), "RELATED_LINKS": EN_RELATED,
        "SIDEBOX_PLAY": EN_SIDEBOX, "SECTION_LABEL_EN": "Culture",
        "HUB_URL_EN": "/culture-mahjong/",
    })

    os.makedirs(ART_PT, exist_ok=True)
    os.makedirs(ART_EN, exist_ok=True)
    open(os.path.join(ART_PT, "index.html"), "w", encoding="utf-8").write(pt)
    open(os.path.join(ART_EN, "index.html"), "w", encoding="utf-8").write(en)

    print("PT body words:", body_words(PT_BODY))
    print("EN body words:", body_words(EN_BODY))
    for name, h in (("PT", PT_BODY), ("EN", EN_BODY)):
        print(name, "h2:", h.count("<h2>"), "p:", h.count("<p>"), "links:", h.count("<a href"))
        print(name, "em-dash:", h.count("—"))
    print("WROTE", ART_PT)
    print("WROTE", ART_EN)


if __name__ == "__main__":
    main()
