# -*- coding: utf-8 -*-
"""Build PT + EN article seq=47 — como fazer uma trinca no mahjong / how to make a pung in mahjong."""
import os, re, json

ROOT = os.getcwd()
TODAY = "2026-11-25"

PT_DIR = "como-jogar-mahjong/como-fazer-trinca-mahjong"
EN_DIR = "en/how-to-play-mahjong/how-to-make-pung-mahjong"
CANON_PT = "https://jogomahjong.com/como-jogar-mahjong/como-fazer-trinca-mahjong/"
CANON_EN = "https://en.jogomahjong.com/how-to-play-mahjong/how-to-make-pung-mahjong/"

# ---------------------------------------------------------------- PT
PT_TITLE = "Como fazer uma trinca no Mahjong: três peças iguais e a chamada de qualquer assento"
PT_DESC = ("Trinca no Mahjong são três peças do mesmo desenho, e só existem quatro cópias de cada uma. "
           "A chamada de qualquer assento, a conta dos fu, o dragão que paga a mão aberta e a armadilha da quarta cópia.")
PT_H1 = PT_TITLE
PT_LEAD = ("Três peças de desenho igual, sem ordem e sem ponta. A trinca é o único conjunto do Mahjong que "
           "qualquer um dos três adversários pode te entregar no descarte, e a que mais muda a mão quando você abre por ela.")

PT_BODY = """
<h2>Três iguais, quatro cópias, um desenho</h2>
<p>Três peças do mesmo desenho e do mesmo naipe. Nenhuma delas tem função própria: não existe começo, fim nem peça do meio. Um 1-2-3 de bambus tem ordem; uma trinca de 5 de círculos não tem.</p>
<p>O baralho de 136 peças traz 34 desenhos, cada um em quatro cópias: 27 de naipe, quatro ventos e três dragões. Com as oito flores a caixa chega a 144, mas flor e estação não formam conjunto de três. São oito desenhos diferentes, uma cópia de cada, e a repetição que a trinca exige é impossível ali.</p>
<p>Daí saem dois números que quase ninguém compara: 34 trincas possíveis contra 21 sequências. Você não escolhe qual montar, espera o baralho repetir um desenho que já está na mão. E há só quatro montagens físicas de qualquer trinca, porque a conta é escolher três das quatro cópias.</p>
<p>No <a href="/mahjong-classico/">Mahjong Clássico</a> daqui a mesa usa as 144 peças, flores incluídas, e as flores nunca viram conjunto.</p>

<h2>A chamada que qualquer assento entrega</h2>
<p>A sequência só pode ser chamada do jogador à sua esquerda, porque a vez corre no sentido anti-horário e é o descarte dele que passa pela sua mão. A trinca pode vir de qualquer um dos três, inclusive de quem joga à sua direita e seria o próximo a comprar.</p>
<p>O nome viaja mal. <i>Pong</i> vem do cantonês, <i>pon</i> é o que se fala numa mesa japonesa, e a jogada é a mesma.</p>
<p>Depois de chamar, você descarta sem comprar da parede. O conjunto fica aberto à sua frente, com a peça chamada deitada na horizontal marcando quem a jogou fora, e essas três peças estão congeladas: não voltam para a mão.</p>
<p>A troca é seca. Você abre mão de uma compra desconhecida e recebe uma peça que já serve. Do outro lado entrega informação: a mesa sabe que o desenho está comprometido, e o quarto igual vira peça morta para todos. O conjunto que só vem do vizinho da esquerda está em <a href="/como-jogar-mahjong/como-fazer-sequencia-mahjong/">como fazer uma sequência</a>.</p>

<h2>Trinca aberta e trinca fechada não pagam igual</h2>
<p>No riichi a conta dos <i>fu</i> separa as duas com clareza.</p>
<ul>
<li><b>Fechada, peça simples (2 a 8):</b> 4 <i>fu</i>.</li>
<li><b>Aberta, peça simples:</b> 2 <i>fu</i>.</li>
<li><b>Fechada, 1, 9, vento ou dragão:</b> 8 <i>fu</i>.</li>
<li><b>Aberta, 1, 9, vento ou dragão:</b> 4 <i>fu</i>.</li>
</ul>
<p>O quadrado dobra cada linha: 8 aberto, 16 fechado, 32 quando a peça é de ponta ou homenagem. A soma arredonda para cima, de dez em dez, então uma mão que fecha em 22 e outra que fecha em 24 pagam o mesmo 30.</p>
<p>Três trincas fechadas valem 2 han sozinhas. Quatro valem yakuman, e essa mão não tem mais nada além dos quatro conjuntos e o par.</p>

<h2>O dragão é o motivo mais barato para abrir a mão</h2>
<p>Mão aberta no riichi precisa de um yaku. Sem yaku, nem a mão perfeita pode ser declarada, e é aí que a trinca de dragão resolve o problema.</p>
<p>Trinca de dragão branco, verde ou vermelho vale 1 han na hora, sem exigir mão fechada. Vento da rodada e vento do próprio assento valem o mesmo. Vento que não é nem uma coisa nem outra não vale nada.</p>
<p>Chamar trinca de dragão paga o preço da mão aberta. Chamar trinca de 3 de bambus não paga nada e ainda fecha a porta do riichi, do pinfu e do <i>iipeikou</i>.</p>
<p>Em Hong Kong a lógica é a mesma com fan no lugar de han: dragão 1 fan, vento da rodada 1 fan, trinca de naipe zero.</p>

<h2>A espera da trinca aceita duas cópias</h2>
<p>Segure dois 5 de círculos e sobram duas cópias no baralho, não quatro. É a espera mais curta do jogo: o par espera até três, a sequência de dois lados espera até oito.</p>
<p>O número engana, porém: a trinca aceita descarte de três jogadores, a sequência só de um. Duas cópias abertas para a mesa inteira não é a mesma coisa que oito cópias abertas para o vizinho da esquerda.</p>
<p>Há ainda o descarte. Quando as quatro cópias de um desenho já estão à vista, na mesa ou no lixo, aquele desenho não fecha trinca para ninguém, e o <a href="/como-jogar-mahjong/">índice de como jogar</a> mostra onde essa contagem entra na rodada.</p>

<h2>O quarto igual muda a conta</h2>
<p>Trinca aberta na mesa e a quarta cópia aparece na sua compra. Dá para subir o conjunto para quadrado, e a reposição vem do fundo da parede, não da frente.</p>
<p>O risco é imediato: no instante da declaração qualquer adversário pode roubar aquela peça e fechar a mão com ela. Chama-se <i>chankan</i>, e é a resposta mais cara contra quem acabou de subir um quadrado.</p>
<p>Por isso a quarta cópia fica na mão quando o oponente está perto do fim. O quadrado não rende han no riichi: rende <i>fu</i>, uma compra do fundo da parede e a chance de o adversário roubar a peça. Em Hong Kong a conta é outra, e o quadrado paga 1 fan. Trinca fechada que recebe a quarta cópia vira quadrado fechado, com 16 <i>fu</i> em peça simples e 32 em ponta ou homenagem.</p>

<h2>Quando a trinca vale a chamada</h2>
<p>Uma regra resolve a maior parte dos casos: chame quando o desenho for homenagem, ou quando a mão já estiver aberta por outro motivo. Deixe passar quando ela ainda puder fechar fechada e a trinca não paga yaku nenhum.</p>
<p>Conte as cópias antes de esticar a mão: segurando uma e com duas no lixo, aquela é a última chance da partida.</p>
<p>A exceção é a mão que precisa de velocidade, não de pontos. Mão já aberta, prazo curto, adversário perto do fim: toda trinca que aparecer entra, inclusive a de vento neutro, porque o objetivo virou fechar antes dos outros. Se a dúvida é sobre as peças em si, o <a href="/jogar-mahjong/">Solitário</a> deixa os 34 desenhos à vista numa mesa só. E o <a href="/como-jogar-mahjong/como-fazer-par-mahjong/">par</a> fecha a lista dos três conjuntos de uma mão de catorze peças.</p>
"""

PT_RELATED = [
    ("https://jogomahjong.com/como-jogar-mahjong/como-fazer-par-mahjong/",
     "Como fazer um par no Mahjong: o olho que fecha as 14 peças"),
    ("https://jogomahjong.com/como-jogar-mahjong/como-fazer-sequencia-mahjong/",
     "Como fazer uma sequência no Mahjong: o conjunto que só vem da esquerda"),
    ("https://jogomahjong.com/como-jogar-mahjong/regras-do-mahjong-passo-a-passo/",
     "Regras do Mahjong passo a passo: guia completo para iniciantes"),
    ("https://jogomahjong.com/como-jogar-mahjong/",
     "Guia completo: como jogar Mahjong do zero"),
    ("https://jogomahjong.com/jogar-mahjong/", "Jogar Mahjong Solitário online"),
]

# ---------------------------------------------------------------- EN
EN_TITLE = "How to Make a Pung in Mahjong: Three of a Kind From Any Seat"
EN_DESC = ("A pung is three identical tiles, and the set only holds four copies of each design. How to call one "
           "from any seat, what it does to your fu, why a dragon pung pays for an open hand, and the trap in the fourth copy.")
EN_H1 = EN_TITLE
EN_LEAD = ("Three tiles with the same face, no order and no ends. A pung is the one meld any of your three "
           "opponents can hand you on a discard, and the one that changes your hand most when you open with it.")

EN_BODY = """
<h2>Three alike, four copies, one design</h2>
<p>Three tiles, same design, same suit. None of them has a job of its own: no first, no last, no middle. A 1-2-3 of bamboo has order. A pung of 5 of circles has none.</p>
<p>A 136-tile set carries 34 designs at four copies each: 27 suited, four winds, three dragons. Add the eight flowers and the box reads 144, but flowers and seasons never make a set of three. They are eight different designs with one copy apiece, and the repetition a pung needs cannot happen there.</p>
<p>Two counts rarely get compared: 34 possible pungs against 21 possible chows. You do not pick which one to build, you wait for the set to repeat a design already in your hand. There are exactly four physical ways to assemble any pung, since the choice is three tiles out of four copies.</p>
<p><a href="/mahjong-classico/">Classic Mahjong</a> here plays with all 144 tiles, flowers included, and their rule does not bend: they score when they turn up and never join a meld.</p>

<h2>The call any seat can feed</h2>
<p>A chow can only come from the player on your left, because turns run counterclockwise and theirs is the discard that reaches you. A pung can come from any of the three, including the player on your right, who would otherwise draw next.</p>
<p>The name travels badly. <i>Pong</i> comes from Cantonese, <i>pon</i> is what a Japanese table says, and the move is identical.</p>
<p>After the call you discard without drawing from the wall. The meld sits open in front of you, the claimed tile laid sideways to mark who threw it, and those three tiles are frozen: they do not return to the hand.</p>
<p>The trade is blunt. You give up an unknown draw and take a tile you already know fits. In return you hand over information: the table now knows that design is spoken for, and the fourth copy is dead for everyone. For the mirror case, where only one seat can feed you, see <a href="/how-to-play-mahjong/how-to-make-sequence-mahjong/">how to make a sequence</a>.</p>

<h2>An open pung and a closed pung do not pay alike</h2>
<p>Under riichi the <i>fu</i> table separates them cleanly.</p>
<ul>
<li><b>Closed, simple tile (2 through 8):</b> 4 <i>fu</i>.</li>
<li><b>Open, simple tile:</b> 2 <i>fu</i>.</li>
<li><b>Closed, 1, 9, wind or dragon:</b> 8 <i>fu</i>.</li>
<li><b>Open, 1, 9, wind or dragon:</b> 4 <i>fu</i>.</li>
</ul>
<p>Every kong doubles its line: 8 open, 16 closed, 32 once the tile is a terminal or an honor. The final total rounds up in tens, so a hand landing on 22 and one landing on 24 both pay 30.</p>
<p>Three closed pungs are worth 2 han on their own. Four are a yakuman, and that hand holds nothing but the four pungs and the pair.</p>

<h2>A dragon pung is the cheapest reason to open</h2>
<p>An open hand under riichi needs a yaku. Without one, even a perfect fourteen tiles cannot be declared, and that is where a dragon pung earns its keep.</p>
<p>A pung of white, green or red dragons is 1 han on the spot, closed hand not required. The round wind and your seat wind pay the same. A wind that is neither pays nothing.</p>
<p>Calling a dragon pung covers the cost of going open. Calling a 3 of bamboo pung covers nothing and also shuts the door on riichi, pinfu and <i>iipeikou</i>.</p>
<p>Hong Kong runs the same logic with fan instead of han: dragon 1 fan, round wind 1 fan, suited pung zero.</p>

<h2>A pung wait draws from two tiles</h2>
<p>Hold two 5 of circles and two copies remain in the set, not four. It is the shortest wait in mahjong: a pair wait reaches three, a two-sided chow wait reaches eight.</p>
<p>The number misleads, though. A pung accepts a discard from three players, a chow from one. Two copies open to the whole table is not the same as eight copies open to the player on your left.</p>
<p>Then there is the discard side. Once all four copies of a design are visible, on the table or in the pile, that design pungs for nobody. The <a href="/how-to-play-mahjong/">how-to-play index</a> shows where that count fits in a round.</p>

<h2>The fourth copy changes the arithmetic</h2>
<p>Open pung on the table, and the fourth copy arrives on your draw. The meld can be upgraded to a kong, with the replacement coming off the back of the wall.</p>
<p>The risk lands at once. The moment you declare, any opponent may take that tile and finish a hand on it. It is called <i>chankan</i>, and it is the most expensive answer to a player who just built a kong.</p>
<p>So the fourth copy stays in your hand when a rival is close to done. A kong scores no han under riichi. It pays in <i>fu</i> plus a draw off the back of the wall, and it hands a rival the chance to rob it. Hong Kong counts 1 fan instead. A closed pung that takes the fourth copy becomes a closed kong, worth 16 <i>fu</i> on a simple tile and 32 on a terminal or honor.</p>

<h2>When a pung is worth the call</h2>
<p>One rule covers most situations: call when the design is an honor, or when the hand is already open for another reason. Let it pass when the hand can still finish closed and the pung pays no yaku.</p>
<p>Count the copies before you reach out. Holding one with two already in the pile, that call is the last chance of the game and the wait is worth the price.</p>
<p>The exception is a hand that needs speed rather than points. Already open, clock running, opponent nearly done: every pung goes in, neutral wind included, because the goal has shifted from scoring well to finishing first. If the tiles themselves are still fuzzy, <a href="/jogar-mahjong/">Solitaire</a> lays all 34 designs face up on one board. And the <a href="/how-to-play-mahjong/how-to-make-pair-mahjong/">pair</a> completes the three melds that fill a fourteen-tile hand.</p>
"""

EN_RELATED = [
    ("https://en.jogomahjong.com/how-to-play-mahjong/how-to-make-pair-mahjong/",
     "How to Make a Pair in Mahjong: The Eye That Closes a 14-Tile Hand"),
    ("https://en.jogomahjong.com/how-to-play-mahjong/how-to-make-sequence-mahjong/",
     "How to Make a Sequence in Mahjong: The Set That Only Comes From the Left"),
    ("https://en.jogomahjong.com/how-to-play-mahjong/mahjong-rules-step-by-step/",
     "Mahjong Rules Step by Step: Complete Beginner's Guide"),
    ("https://en.jogomahjong.com/how-to-play-mahjong/",
     "How to Play Mahjong: the full guide"),
    ("https://en.jogomahjong.com/jogar-mahjong/", "Play Mahjong Solitaire online"),
]


def words(html):
    t = re.sub(r"<[^>]+>", " ", html)
    return len([w for w in re.split(r"\s+", t) if w.strip()])


def build(tpl, mapping, outpath):
    s = open(tpl, encoding="utf-8").read()
    for k, v in mapping.items():
        s = s.replace("{{%s}}" % k, v)
    left = re.findall(r"\{\{[A-Z_]+\}\}", s)
    assert not left, "placeholders restantes: %s" % left
    os.makedirs(os.path.dirname(outpath), exist_ok=True)
    open(outpath, "w", encoding="utf-8", newline="\n").write(s)
    return s


pt_map = {
    "TITLE": PT_TITLE, "DESCRIPTION": PT_DESC,
    "JSON_HEADLINE": PT_TITLE, "JSON_DESCRIPTION": PT_DESC,
    "CANONICAL_PT": CANON_PT, "CANONICAL_EN": CANON_EN,
    "EYEBROW": "Como jogar · Regras", "H1": PT_H1, "LEAD": PT_LEAD,
    "BODY": PT_BODY.strip(),
    "RELATED_LINKS": "\n".join('              <li><a href="%s">%s</a></li>' % (u, t) for u, t in PT_RELATED),
    "SIDEBOX_PLAY": '            <li><a href="/mahjong-classico/">Jogar Mahjong Clássico</a></li>',
    "SECTION_LABEL_PT": "Como jogar", "HUB_URL_PT": "/como-jogar-mahjong/",
}

en_map = {
    "TITLE": EN_TITLE, "DESCRIPTION": EN_DESC,
    "JSON_HEADLINE": EN_TITLE, "JSON_DESCRIPTION": EN_DESC,
    "CANONICAL_PT": CANON_PT, "CANONICAL_EN": CANON_EN,
    "EYEBROW": "How to Play · Rules", "H1": EN_H1, "LEAD": EN_LEAD,
    "BODY": EN_BODY.strip(),
    "RELATED_LINKS": "\n".join('              <li><a href="%s">%s</a></li>' % (u, t) for u, t in EN_RELATED),
    "SIDEBOX_PLAY": '            <li><a href="/mahjong-classico/">Play Classic Mahjong</a></li>',
    "SECTION_LABEL_EN": "How to Play", "HUB_URL_EN": "/how-to-play-mahjong/",
}

p1 = os.path.join(ROOT, PT_DIR, "index.html")
p2 = os.path.join(ROOT, EN_DIR, "index.html")
build(os.path.join(ROOT, "content", "article-template.html"), pt_map, p1)
build(os.path.join(ROOT, "content", "article-template-en.html"), en_map, p2)

print("PT body words:", words(PT_BODY))
print("EN body words:", words(EN_BODY))
print("WROTE", p1)
print("WROTE", p2)

for p in (p1, p2):
    h = open(p, encoding="utf-8").read()
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)
    json.loads(m.group(1))
    assert "{{" not in h
print("JSON-LD OK em ambos")
