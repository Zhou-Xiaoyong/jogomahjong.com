# -*- coding: utf-8 -*-
"""Build seq=42: mitos e lendas sobre o mahjong (PT) / myths and legends about mahjong (EN)."""
import os, re, sys

ROOT = os.getcwd()
SLUG_PT = "mitos-lendas-mahjong"
SLUG_EN = "mahjong-myths-legends"
ART_PT = os.path.join(ROOT, "cultura-mahjong", SLUG_PT)
ART_EN = os.path.join(ROOT, "en", "culture-mahjong", SLUG_EN)
CANON_PT = f"https://jogomahjong.com/cultura-mahjong/{SLUG_PT}/"
CANON_EN = f"https://en.jogomahjong.com/culture-mahjong/{SLUG_EN}/"

# ---------------- PORTUGUES ----------------
PT_TITLE = "Mitos e lendas sobre o mahjong: sete histórias que a mesa repete"
PT_DESC = ("Os 108 heróis, o pardal do um de bambu, as oito flores e a peça quente: o que as lendas "
           "dizem e o que o conjunto de 144 peças mostra de verdade.")
PT_EYEBROW = "Cultura · Folclore"
PT_LEAD = ("Alguém descarta um três de bambus e comenta que o naipe nasceu dos 108 heróis da "
           "<em>Margem d'Água</em>. Três jogadores assentem, a mão continua, e o baralho fica sem defesa.")

PT_BODY = """
<h2>Os 108 heróis que nunca couberam no baralho</h2>
<p>A história mais repetida dentro da China não é a de Confúcio, que já respondemos em <a href="/cultura-mahjong/quem-inventou-o-mahjong/">quem inventou o mahjong</a>. É outra: as 108 peças de naipe seriam os 108 foras da lei do romance <em>Margem d'Água</em>.</p>
<p>O número fecha bonito e a conta não passa. Um conjunto de 144 peças tem 108 peças de naipe, mas apenas 27 desenhos diferentes, quatro cópias de cada. Um baralho feito de heróis precisaria de 108 faces distintas. O que existe é o contrário: três naipes de nove números, cada um repetido quatro vezes, porque quatro é o que permite trinca, kong e par na mesma mesa.</p>
<p>A origem dos naipes é outra e está escrita nos nomes. O caractere conta miríades, a unidade antiga de cordas de moeda. O bambu é a corda de mil moedas com o furo no meio. O círculo é a moeda. Os três naipes herdaram as denominações do dinheiro de papel que se jogava antes de existir peça, e o número 108 veio da estrutura do jogo, não de um livro.</p>

<h2>O pardal do um de bambu</h2>
<p>O nome chinês do jogo é <em>maque</em>, pardal. A explicação que corre na mesa diz que as peças soam como pardais numa árvore quando são lavadas, e que daí vem o apelido.</p>
<p>A parte do som é bonita e não explica nada, porque o nome já estava nos baralhos antes de virar jogo de peças. O que sustenta o pardal é a face: o um de bambu não mostra bambu nenhum, mostra uma ave pousada num galho. Em muitos conjuntos ela é um pardal, e é a única peça do naipe com bicho.</p>
<p>Vale guardar a distinção porque ela aparece em discussão de clube. O nome vem da ave da peça. O barulho da mesa é consequência, não causa.</p>

<h2>As oito flores não são os oito imortais</h2>
<p>Muitos conjuntos antigos trazem os oito imortais do taoísmo gravados no verso das peças de bônus. Daí saiu a frase: "as oito flores são os oito imortais".</p>
<p>A face conta outra coisa. Quatro plantas, ameixa, orquídea, bambu e crisântemo, e quatro estações escritas por extenso. Os imortais ficam no verso, onde nenhuma regra olha.</p>
<p>O que a lenda esconde é a parte que custa ponto. A flor só paga quando é a sua: na contagem de Hong Kong, 1 fan pela flor do seu assento e 1 fan pela estação do seu assento. Na oficial chinesa, a peça não vale nada por si e serve só para comprar de reposição no rabo da muralha. No conjunto japonês as oito nem existem, porque são 136 peças. O passo a passo está no <a href="/cultura-mahjong/flores-estacoes-mahjong/">guia das flores e estações</a>.</p>

<h2>A peça quente e a memória que conta mal</h2>
<p>Toda mesa tem uma. "Não descarta o cinco de círculos, ele está voltando." A sensação é real. A mecânica não existe.</p>
<p>A muralha é fechada antes da primeira compra e não muda de ordem porque alguém pediu. Num conjunto de 144, 53 peças saem na distribuição, catorze para o banqueiro e treze para cada um dos outros, e 91 ficam na parede. Com 136, sobram 83, das quais catorze viram muralha morta e nunca são compradas: 69 compras vivas.</p>
<p>A memória faz o resto. Você arquiva as duas noites em que a peça voltou e pagou, e não arquiva as vinte em que ela ficou enterrada. Uma única regra dura cobre peça que volta: o furiten. Peça que está no seu próprio monte de descartes não pode fechar a sua mão. O resto é contar o que está visível.</p>
<p>Na tela a conta fica honesta. O <a href="/jogar-mahjong/">Solitário</a> não tem muralha nem sorteio: as 112 peças estão à vista desde o começo, e o que separa você do fim do jogo é a ordem em que você abre espaço.</p>

<h2>Marfim, osso e a junta que denuncia</h2>
<p>Conjunto antigo com cara de marfim quase nunca é marfim. A construção padrão do fim do século XIX é uma lâmina de osso de boi de uns dois milímetros encaixada por cauda de andorinha num verso de bambu. Um conjunto assim pesa perto de 4 kg e bate um som seco que o plástico não repete.</p>
<p>Marfim de verdade existiu em conjuntos de exportação caros, e desde 1989 o comércio internacional é proibido pela Cites. O teste mais rápido é o verso: osso e bambu são duas peças unidas, com emenda visível. Plástico sai da forma inteiro.</p>

<h2>"Foi proibido na China" é meia verdade</h2>
<p>Depois de 1949, o mahjong foi atacado como hábito de aposta e herança feudal. Conjuntos foram escondidos, alguns destruídos, a produção parou. Não houve decreto único com data e artigo. Houve campanha, e campanha não se cita como lei.</p>
<p>A volta veio nos anos 1980, com a produção retomada e as casas de chá reabrindo. Chengdu hoje tem salões com centenas de mesas, jogando a versão de 108 peças, sem sequência e com naipe obrigatório de descarte. O jogo que voltou não era o que tinha saído.</p>

<h2>O assento da sorte</h2>
<p>Trocar de cadeira, soprar o dado, recusar o Norte. A regra já resolve a sorte de assento sozinha: o banqueiro começa como Leste e, quando não fecha a mão, o Leste passa para o jogador da direita e os ventos rodam com ele. Em quatro rodadas, cada um é Leste uma vez. O dado não escolhe quem ganha, escolhe onde a muralha abre.</p>

<h2>O que fazer com a lenda</h2>
<p>Não corrija ninguém no meio da mão. A história é parte da noite, e quem chega com os 108 heróis está conversando, não pedindo aula.</p>
<p>Três das lendas mudam decisão, e essas merecem uma frase antes da primeira compra: se a flor paga, se existe peça quente e se o assento influencia. Combine a escola de regras em voz alta e a discussão morre ali.</p>
<p>A exceção é clube e torneio. Lá existe folha de regra impressa, e "todo mundo joga assim" não vale nada. Se você quer as crenças que mexem no descarte, o texto sobre <a href="/cultura-mahjong/mahjong-supersticao/">mahjong e superstição</a> trata delas, e o índice de <a href="/cultura-mahjong/">Cultura</a> guarda o resto.</p>
"""

PT_RELATED = """              <li><a href="/cultura-mahjong/quem-inventou-o-mahjong/">Quem inventou o mahjong: a lenda de Confúcio e o que sobrou dela</a></li>
              <li><a href="/cultura-mahjong/mahjong-supersticao/">Mahjong e superstição: o que a mesa evita</a></li>
              <li><a href="/cultura-mahjong/flores-estacoes-mahjong/">Flores e estações: as oito peças que nunca entram na mão</a></li>
              <li><a href="/jogar-mahjong/">Jogar Mahjong Solitário grátis</a></li>
              <li><a href="/cultura-mahjong/">Todos os artigos de Cultura</a></li>"""

PT_SIDEBOX = """            <li><a href="/jogar-mahjong/">Mahjong Solitário</a></li>"""

# ---------------- ENGLISH ----------------
EN_TITLE = "Mahjong Myths and Legends: Seven Stories the Table Still Repeats"
EN_DESC = ("The 108 outlaws, the sparrow on the one of bamboo, the eight flowers and the hot tile: "
           "what the stories claim and what a 144-tile set actually shows.")
EN_EYEBROW = "Culture · Folklore"
EN_LEAD = ("Someone throws a 3 of bamboo and mentions that the suit comes from the 108 outlaws of "
           "<em>Water Margin</em>. Three players nod, the hand moves on, and the tile set gets no defence.")

EN_BODY = """
<h2>The 108 outlaws who never fit in the set</h2>
<p>The story told most often inside China is not the Confucius one, which we settled in <a href="/culture-mahjong/who-invented-mahjong/">who invented mahjong</a>. It is this: the 108 suited tiles stand for the 108 outlaws of <em>Water Margin</em>.</p>
<p>The number lands neatly and the arithmetic fails. A 144-tile set holds 108 suited tiles, but only 27 different faces, four copies of each. A deck built from heroes would need 108 distinct faces. What exists is the opposite: three suits of nine numbers, each repeated four times, because four is what allows a pung, a kong and a pair on the same table.</p>
<p>The suits came from somewhere else, and the names still say it. The character suit counts myriads, the old unit for strings of coin. The bamboo suit is a string of a thousand coins with the hole in the middle. The circle is the coin. All three inherited their denominations from paper money games played long before tiles existed, and the 108 came out of the structure of the game rather than out of a novel.</p>

<h2>The sparrow on the one of bamboo</h2>
<p>The Chinese name of the game is <em>maque</em>, sparrow. The version heard at tables says the tiles sound like sparrows in a tree when they are washed, and that the nickname grew from there.</p>
<p>The sound is charming and explains nothing, since the name was on the decks before the tile game existed. What holds the sparrow up is a face: the one of bamboo shows no bamboo at all. It shows a bird perched on a branch, and on many sets that bird is a sparrow. It is the only tile in the suit with an animal on it.</p>
<p>Worth keeping the distinction, because it comes up in club arguments. The name comes from the bird on the tile. The noise at the table is a result, not a cause.</p>

<h2>The eight flowers are not the eight immortals</h2>
<p>Plenty of older sets engrave the eight Taoist immortals on the back of the bonus tiles. From that decoration comes a line you will hear: "the eight flowers are the eight immortals".</p>
<p>The faces disagree. Four plants, plum, orchid, bamboo and chrysanthemum, and four seasons spelled out. The immortals sit on the reverse, where no rule ever looks.</p>
<p>What the story hides is the part that costs points. A flower pays only when it belongs to you: Hong Kong scoring gives 1 fan for the flower matching your seat and another for the matching season. Chinese official scoring gives the tile no value on its own; it only buys a replacement draw from the tail of the wall. Japanese sets leave the eight out entirely, since riichi runs 136 tiles. The detail sits in our <a href="/culture-mahjong/flowers-seasons-mahjong/">guide to flowers and seasons</a>.</p>

<h2>The hot tile and a memory that keeps bad books</h2>
<p>Every table has one. "Don't throw the five of circles, it keeps coming back." The feeling is real. The mechanics are not.</p>
<p>The wall is sealed before the first draw and does not reorder itself because somebody asked. In a 144-tile set, 53 tiles leave in the deal, fourteen to the dealer and thirteen to each of the other three, and 91 stay in the wall. With 136, the wall holds 83, fourteen of which become the dead wall and are never drawn, leaving 69 live draws.</p>
<p>Memory does the rest. You file the two nights a discarded tile came back and paid, and never file the twenty when it stayed buried. One hard rule covers a tile coming back: furiten. A tile in your own discard pile cannot complete your hand. Everything else is counting what is visible.</p>
<p>On a screen the books get honest. Our <a href="/jogar-mahjong/">Solitaire</a> has no wall and no draw: all 112 tiles are face up from the start, and the only thing between you and a cleared board is the order in which you open space.</p>

<h2>Ivory, bone and the joint that gives it away</h2>
<p>An old set that looks like ivory almost never is. The standard late-19th-century build is a slice of ox bone about two millimetres thick, dovetailed onto a bamboo back. Such a set weighs close to 4 kg and clicks in a way plastic does not.</p>
<p>Real ivory did exist in expensive export sets, and since 1989 the international trade has been banned under CITES. The fastest test is the back: bone and bamboo are two pieces joined, seam visible. Plastic comes out of a mould in one piece.</p>

<h2>"It was banned in China" is half true</h2>
<p>After 1949 mahjong was attacked as a gambling habit and a feudal leftover. Sets went into hiding, some were destroyed, production stopped. There was no single decree with a date and a clause. There was a campaign, and a campaign is not a statute.</p>
<p>The return came in the 1980s, with production restarting and tea houses reopening. Chengdu now runs halls with hundreds of tables, playing the 108-tile game with no chows and a compulsory void suit. The game that came back was not the one that left.</p>

<h2>The lucky seat</h2>
<p>Swap chairs, blow on the dice, refuse the north seat. The rule already handles seat luck on its own: the dealer starts as East, and when the dealer fails to win, East passes to the player on the right and the winds travel with it. Across four rounds everybody deals once. The dice do not pick a winner. They pick where the wall opens.</p>

<h2>What to do with the story</h2>
<p>Don't correct anyone mid-hand. The story is part of the evening, and the player who opens with the 108 outlaws is making conversation, not asking for a lecture.</p>
<p>Three of the stories change a decision, and those deserve a sentence before the first draw: whether flowers pay, whether a tile can run hot, whether the seat matters. Agree the rule set out loud and the argument ends there.</p>
<p>The exception is a club or a tournament. A printed rule sheet exists there, and "everyone plays it this way" is worth nothing. If you want the beliefs that actually move a discard, the piece on <a href="/culture-mahjong/mahjong-superstition/">mahjong and superstition</a> covers them, and the <a href="/culture-mahjong/">Culture index</a> holds the rest.</p>
"""

EN_RELATED = """              <li><a href="/culture-mahjong/who-invented-mahjong/">Who invented mahjong: the Confucius story and what is left of it</a></li>
              <li><a href="/culture-mahjong/mahjong-superstition/">Mahjong and superstition: what the table avoids</a></li>
              <li><a href="/culture-mahjong/flowers-seasons-mahjong/">Flowers and seasons: the eight tiles that never enter a hand</a></li>
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
        print(name, "em-dash:", h.count("\u2014"))
    print("WROTE", ART_PT)
    print("WROTE", ART_EN)


if __name__ == "__main__":
    main()
