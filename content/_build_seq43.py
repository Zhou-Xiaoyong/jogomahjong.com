# -*- coding: utf-8 -*-
"""Build PT + EN article seq=43 — como fazer um par no mahjong / how to make a pair in mahjong."""
import os, re, json, sys

ROOT = os.getcwd()
TODAY = "2026-11-20"

PT_DIR = "como-jogar-mahjong/como-fazer-par-mahjong"
EN_DIR = "en/how-to-play-mahjong/how-to-make-pair-mahjong"
CANON_PT = "https://jogomahjong.com/como-jogar-mahjong/como-fazer-par-mahjong/"
CANON_EN = "https://en.jogomahjong.com/how-to-play-mahjong/how-to-make-pair-mahjong/"

# ---------------------------------------------------------------- PT
PT_TITLE = "Como fazer um par no Mahjong: o olho que fecha as 14 peças"
PT_DESC = ("O par é o único conjunto de dois do Mahjong e o único que não se compra no descarte. "
           "Como formar o olho, quando chamar o terceiro custa a mão e qual par sai primeiro.")
PT_H1 = "Como fazer um par no Mahjong: o olho que fecha as 14 peças"
PT_LEAD = ("Quatorze peças na mão, doze comprometidas com quatro grupos de três e duas soltas. "
           "O par é o único conjunto de dois que existe no jogo, e é ele que decide se a mão fecha.")

PT_BODY = """
<h2>A conta que só tem um dois</h2>
<p>Quatorze peças, doze delas já comprometidas com quatro grupos de três. As duas que sobram formam o único conjunto de dois que o jogo permite, e é a ele que os jogadores brasileiros dão o nome de olho.</p>
<p>A conta não muda de mesa para mesa. Riichi japonês, Mahjong de Hong Kong, liga americana: 4 × 3 + 2 = 14 em todas. Quem tem 13 peças está sempre a uma do fim, e essa peça pode ser de qualquer desenho, desde que feche a dupla.</p>
<p>Em japonês o par é o <i>jantou</i>, cabeça de pardal. Trincas e sequências são o corpo; sem a cabeça, doze peças arrumadas não valem nada.</p>
<p>Daí vem a primeira armadilha, e ela é estrutural. O par é indivisível. Se uma das duas peças sai para entrar numa sequência, o olho deixou de existir e você precisa de outro antes de declarar. No Solitário isso fica óbvio, porque lá o <a href="/jogar-mahjong/">par é a regra inteira</a>: duas peças iguais saem da mesa, e não há mão para completar.</p>

<h2>O par não vem do descarte</h2>
<p>Dá para chamar o descarte de outro jogador para fechar trinca, sequência ou kong. Não existe chamada para fechar par, e essa é a diferença que separa o par dos outros conjuntos da mão.</p>
<p>Na prática: você segura um 7 de bambus solto. Alguém descarta um 7. Serve para quem tem 8 e 9, serve para quem já tem dois 7 e quer trinca, e não serve para você. Sua peça entra de duas formas: comprando da parede ou ganhando a mão com ela.</p>
<p>Por isso a espera por um par é a mais silenciosa do jogo: não depende de ninguém e não aproveita nada do que os outros fazem. O <a href="/como-jogar-mahjong/">índice de como jogar</a> separa cada etapa da mão, e o par aparece em quase todas.</p>

<h2>Chamar o terceiro é perder o olho</h2>
<p>Dois 5 de círculos separados como olho provável. Um terceiro 5 aparece no descarte do jogador à sua direita. Chamar o pong parece ganho limpo: um conjunto fechado e uma peça a menos no lixo público.</p>
<p>Só que as duas peças que formavam o olho agora formam uma trinca. O par acabou. Se a mão estava a duas peças do fim, com a dupla pronta e um conjunto pela metade, a chamada transforma isso em um conjunto a mais e um par inteiro por fazer.</p>
<p>Chame quando a trinca resolver um conjunto que não fecharia de outro jeito, ou quando o par já não servisse de cabeça porque existe outra dupla melhor na mão. Fora desses dois casos, deixe o 5 passar. As <a href="/como-jogar-mahjong/regras-do-mahjong-passo-a-passo/">regras do Mahjong passo a passo</a> listam as três chamadas permitidas, e nenhuma delas é o par.</p>

<h2>Esperar no par aceita três peças</h2>
<p>O caso espelho é mais frequente: quatro conjuntos prontos e uma peça solta esperando a companheira. No Japão essa espera é o <i>tanki</i>. Você segura uma cópia, sobram três no jogo.</p>
<p>Compare com a espera de dois lados, do tipo 3-4 de bambus, que aceita 2 e 5: até oito cópias. Três contra oito é a diferença entre fechar a mão e ficar olhando a parede encolher.</p>
<p>Existe um consolo de 2 <i>fu</i> no riichi, porque a espera no par vale um pouco mais na contagem. Na prática ele quase nunca muda o total, porque a conta arredonda de dez em dez. O valor real do <i>tanki</i> é outro: você pode trocar a peça solta por outra no meio da mão, coisa que uma espera de dois lados não permite. Quem começa sente essa diferença antes de saber o nome dela, e o <a href="/como-jogar-mahjong/como-jogar-mahjong-iniciantes/">guia para iniciantes</a> mostra onde ela aparece.</p>

<h2>Nem todo par vale o mesmo</h2>
<p>Par de dragão e par de vento não pesam igual na hora de contar. No riichi, um par de dragões vale 2 fu, um par do vento da rodada ou do seu assento vale 2 fu, e um par de vento que não é nem uma coisa nem outra vale zero. Três pares de aparência parecida, três valores diferentes.</p>
<p>Em Hong Kong a unidade é o fan e as mesas divergem. Algumas contam 1 fan só pelo par de dragões, outras só pontuam a trinca. Vale perguntar antes da primeira mão, porque a resposta muda o descarte da quarta rodada.</p>
<p>Nos Estados Unidos, o cartão anual da liga traz uma regra seca: curinga não fecha par. O par que a mão pede tem de ser de peças naturais, e é por isso que cartões simples travam tanta gente na primeira tentativa.</p>

<h2>Sete pares, sete duplas diferentes</h2>
<p>A única mão em que o par deixa de ser cabeça e passa a ser a estrutura toda é a de sete pares: 2 han, 25 fu fixos e nenhuma peça chamada na mesa.</p>
<p>As sete duplas precisam ser diferentes entre si. Quatro peças iguais não valem como dois pares, e essa é a confusão mais comum de quem aprende a mão pelo nome. O quadrado é um par com duas sobras: uma delas vai para o descarte antes de a mão andar, e quem conta o quadrado duas vezes se acha mais perto do fim do que está.</p>

<h2>Qual par sai primeiro</h2>
<p>Dois pares no meio da mão, nenhum conjunto fechado, um descarte obrigatório. A escolha não é entre o par bonito e o par feio. É entre o par que ocupa peças úteis e o par que não ocupa nada.</p>
<p>Um par de 4 de caracteres prende duas peças que também serviriam em 3-4-5 e em 4-5-6. Um par de vento não prende nada, porque nenhuma sequência usa vento. Com a mão aberta, sai o par de naipe e fica o de homenagem, que já tem jeito de olho.</p>
<p>A exceção é a peça que a mesa está jogando fora. Um par de 4 de círculos com dois 4 já no lixo público é a trinca mais barata disponível, porque o terceiro vem de qualquer assento. Nesse caso o par de naipe fica e o de vento sai.</p>
<p>Se a dúvida aparece na primeira partida, jogue uma mão no <a href="/mahjong-classico/">Mahjong Clássico</a> antes de sentar com quatro pessoas: são as mesmas 144 peças e as três chamadas de verdade, sem dinheiro e sem pressa.</p>
"""

PT_RELATED = [
    ("https://jogomahjong.com/como-jogar-mahjong/regras-do-mahjong-passo-a-passo/",
     "Regras do Mahjong passo a passo: guia completo para iniciantes"),
    ("https://jogomahjong.com/como-jogar-mahjong/como-jogar-mahjong-iniciantes/",
     "Como jogar Mahjong para iniciantes: guia passo a passo"),
    ("https://jogomahjong.com/como-jogar-mahjong/quais-sao-pecas-do-mahjong/",
     "Quais são as peças do Mahjong: 144 no total e só 34 desenhos diferentes"),
    ("https://jogomahjong.com/jogar-mahjong/", "Jogar Mahjong Solitário online"),
    ("https://jogomahjong.com/mahjong-classico/", "Mahjong Clássico: partida de quatro jogadores"),
]

# ---------------------------------------------------------------- EN
EN_TITLE = "How to Make a Pair in Mahjong: The Eye That Closes a 14-Tile Hand"
EN_DESC = ("The pair is the only two-tile set in mahjong and the one thing you cannot call off a discard. "
           "How to build the eye, when the third tile costs you the hand, and which pair to cut first.")
EN_H1 = "How to Make a Pair in Mahjong: The Eye That Closes a 14-Tile Hand"
EN_LEAD = ("Fourteen tiles sit in your hand, twelve of them already spoken for by four groups of three. "
           "The leftover two form the only two-tile set the game allows, and that pair decides whether the hand closes.")

EN_BODY = """
<h2>The only two in a game of threes</h2>
<p>Fourteen tiles, twelve of them locked into four groups of three. The two at the end make the only two-tile set mahjong permits, and English-speaking players call it the eye.</p>
<p>Every table runs the same arithmetic. Japanese riichi, Hong Kong mahjong, the American league card: 4 × 3 + 2 = 14. Hold thirteen tiles and you are always one away, and that last tile can be any design at all as long as it completes the pair.</p>
<p>Japanese players call it <i>jantou</i>, sparrow's head. Melds are the body; twelve well-arranged tiles without a head score nothing.</p>
<p>Which sets up the first trap, and it is structural. A pair cannot be split. Send one of its two tiles into a chow and the eye is gone; you need a fresh one before you can declare. Solitaire makes that obvious, since there the <a href="/jogar-mahjong/">pair is the entire rule</a>: matching tiles leave the table and no hand gets completed at all.</p>

<h2>No call brings you a pair</h2>
<p>You can claim another player's discard to finish a pung, a chow, or a kong. There is no call that finishes a pair. That single gap separates the pair from every other set in the hand.</p>
<p>Put it on the table. You hold a lone 7 of bamboo and want its twin. Somebody discards a 7. That discard works for the player holding 8 and 9, works for the player holding two 7s who wants a pung, and does nothing for you. Your tile arrives two ways only: off the wall, or as the tile you win on.</p>
<p>That makes the pair wait the quietest in the game: it needs nobody and uses nothing the table hands you. The <a href="/how-to-play-mahjong/">how-to-play index</a> splits the hand into stages, and the pair turns up in nearly all of them.</p>

<h2>Calling the third tile costs you the eye</h2>
<p>Two 5 of circles sit apart as your likely eye. A third 5 hits the discard pile on your right. Calling pung looks like free progress: one closed meld and one less tile in the public pile.</p>
<p>Except those two tiles now form a pung. The pair is gone. If the hand was two tiles from finished, pair complete and one meld half built, the call converts that into an extra meld plus an entire pair still to find.</p>
<p>Call when the pung solves a meld you could not assemble any other way, or when another pair in the hand already does the head's job better. Otherwise let the 5 go by. The <a href="/how-to-play-mahjong/mahjong-rules-step-by-step/">step-by-step rules</a> list the three legal calls, and the pair is not among them.</p>

<h2>A pair wait takes three tiles</h2>
<p>The mirror case shows up more often: four melds done and one tile stranded, waiting for its partner. Japanese players call the wait <i>tanki</i>, and the count is easy. You hold one copy of a design, so three copies remain in play.</p>
<p>Set that against a two-sided wait, say 3-4 of bamboo taking 2 and 5: up to eight copies. Three against eight is the gap between finishing a hand and watching the wall shrink.</p>
<p>Riichi throws in 2 <i>fu</i> for the pair wait, and here is the honest part: it almost never moves the total, because fu rounds up in tens and the gain disappears inside the rounding. The real value of <i>tanki</i> is flexibility. You can swap the stranded tile for a different one mid-hand, which a two-sided wait never lets you do. Beginners feel that before they know its name, and the <a href="/how-to-play-mahjong/how-to-play-mahjong-beginners/">beginner walkthrough</a> shows where it first bites.</p>

<h2>Pairs do not all score alike</h2>
<p>A dragon pair and a wind pair are not the same animal on the scoresheet. Under riichi, a pair of dragons is 2 fu, a pair of the round wind or your seat wind is 2 fu, and a pair of a wind that is neither counts zero. Three pairs that look identical, three different values.</p>
<p>Hong Kong counts in fan, and houses split on this one. Some give 1 fan for the dragon pair alone, others only score the pung. Ask before the first hand; the answer changes what you cut in the fourth round.</p>
<p>The American league card is blunt about it: jokers may not be used in a pair. Whatever pair the hand calls for has to be natural tiles, which is why cards that look simple stop so many players on the first try.</p>

<h2>Seven pairs means seven different pairs</h2>
<p>One hand turns the pair from head into the whole structure: seven pairs, 2 han, a flat 25 fu, and no tile called off the table.</p>
<p>The seven have to be distinct. Four of a kind does not count as two pairs, and that is the mistake that follows the hand's name around. A quad is one pair with two tiles left over; one of them goes to the discard pile, and anyone counting a quad twice thinks they are closer to finished than they are.</p>

<h2>Which pair leaves first</h2>
<p>Two pairs mid-hand, no meld closed, one tile must go. The choice is not between the pretty pair and the ugly one. It is between the pair holding useful tiles and the pair holding nothing.</p>
<p>A pair of 4 of characters ties up two tiles that would also work in 3-4-5 and 4-5-6. A wind pair ties up nothing, because no chow uses a wind. While the hand is still open, the suited pair leaves and the honor pair stays as the likely eye.</p>
<p>The exception is a tile the table is throwing away. A pair of 4 of circles with two 4s already in the public pile is the cheapest pung on the board, since the third comes from any seat. Then the suited pair stays and the wind pair goes.</p>
<p>If this is still theory, play a hand of <a href="/mahjong-classico/">Classic Mahjong</a> before sitting down with four people. Same 144 tiles, same three real calls, no money and no clock.</p>
"""

EN_RELATED = [
    ("https://en.jogomahjong.com/how-to-play-mahjong/mahjong-rules-step-by-step/",
     "Mahjong Rules Step by Step: Complete Beginner's Guide"),
    ("https://en.jogomahjong.com/how-to-play-mahjong/how-to-play-mahjong-beginners/",
     "How to Play Mahjong for Beginners: A Step-by-Step Guide"),
    ("https://en.jogomahjong.com/how-to-play-mahjong/mahjong-tiles-guide/",
     "What Are the Mahjong Tiles: 144 in the Set and Only 34 Pictures"),
    ("https://en.jogomahjong.com/jogar-mahjong/", "Play Mahjong Solitaire online"),
    ("https://en.jogomahjong.com/mahjong-classico/", "Classic Mahjong: the four-player game"),
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

# JSON-LD sanity
for p in (p1, p2):
    h = open(p, encoding="utf-8").read()
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)
    json.loads(m.group(1))
    assert "{{" not in h
    assert "<loc>" not in h
print("JSON-LD OK em ambos")
