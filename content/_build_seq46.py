# -*- coding: utf-8 -*-
"""Build PT + EN article seq=46 — mahjong e o zodíaco chinês / mahjong and the chinese zodiac."""
import os, re, json

ROOT = os.getcwd()
TODAY = "2026-11-24"

PT_DIR = "cultura-mahjong/mahjong-zodiaco-chines"
EN_DIR = "en/culture-mahjong/mahjong-chinese-zodiac"
CANON_PT = "https://jogomahjong.com/cultura-mahjong/mahjong-zodiaco-chines/"
CANON_EN = "https://en.jogomahjong.com/culture-mahjong/mahjong-chinese-zodiac/"

# ---------------------------------------------------------------- PT
PT_TITLE = "Mahjong e o zodíaco chinês: onde os doze animais aparecem (e onde não)"
PT_DESC = ("O cavalo de fogo de 2026, as doze horas do dia, os doze dragões que não são bichos e o motivo "
           "pelo qual nenhuma das 144 peças muda de acordo com o ano em que você nasceu.")
PT_H1 = PT_TITLE
PT_LEAD = ("Quem nasceu em 1978 chega ao quinto ano do cavalo em 2026 e costuma avisar isso antes de lavar "
           "as peças. O zodíaco rende assunto na mesa, mas não mexe em uma única face do baralho.")

PT_BODY = """
<h2>A frase que abre a noite</h2>
<p>Todo grupo tem alguém que senta e anuncia: este é o meu ano, hoje eu ganho. Em 2026 a frase pertence a quem nasceu em 1966, 1978, 1990, 2002 ou 2014, porque 17 de fevereiro abriu o ano do cavalo e ele segue até 5 de fevereiro de 2027.</p>
<p>A pergunta embaixo é outra e quase ninguém responde: o zodíaco toca nas peças? A resposta curta é não. A longa ocupa os parágrafos seguintes, porque baralho e calendário usam números parecidos para coisas sem relação nenhuma.</p>

<h2>Doze animais, doze ramos, doze horas</h2>
<p>O zodíaco chinês não é um horóscopo de doze signos como o ocidental. É um ciclo de doze ramos terrestres, cada um com um animal colado, e ele roda em anos, em meses e nas horas do dia.</p>
<p>A camada das horas é a que quase ninguém usa e a que explica mais. Cada ramo cobre duas horas: o rato vai das 23h à 1h, o cavalo das 11h à 13h. A palavra chinesa para meio-dia foi montada em cima do ramo do cavalo. O relógio da parede não tem nada a ver com a mesa, mas o nome da hora tem.</p>
<p>Nos anos, 2026 é o 33º termo de um ciclo de sessenta, que combina dez troncos com doze ramos. O mesmo par volta em 2086. Vale saber porque "ano do cavalo" não é uma coisa só: existem cinco cavalos dentro do ciclo, um por elemento, e o de 2026 é o de fogo.</p>

<h2>O doze do baralho é outra conta</h2>
<p>A conta de uma caixa cheia fecha em 144: 108 de naipe, 16 de vento, 12 dragões, 8 flores. O único grupo que chega a doze é o dos dragões, e ele não tem doze coisas diferentes. São três desenhos, quatro cópias de cada.</p>
<p>Os três desenhos são o centro vermelho, a prosperidade verde e o quadro branco. Nenhum deles é bicho, e nenhum deles é o dragão do zodíaco. O nome em inglês saiu do mercado de exportação do século XIX, que precisava de rótulo vendável. As três peças têm texto próprio em <a href="/cultura-mahjong/simbolismo-dos-dragoes-mahjong/">simbolismo dos dragões</a>.</p>
<p>Também é possível dividir 108 por 12 e achar nove, que é exatamente quantos números cada naipe carrega. A conta é aritmética, não simbolismo: três naipes de nove, quatro cópias cada, porque quatro é o que permite trinca, sequência e par na mesma mesa. Um baralho desenhado pelo zodíaco teria doze números por naipe, e a mão de catorze peças não fecharia mais.</p>

<h2>Os quatro guardiões não são signos</h2>
<p>Quem já leu sobre os ventos conhece o dragão azul, a ave vermelha, o tigre branco e a tartaruga negra. São guardiões de direção, vindos das vinte e oito casas lunares, e não animais do zodíaco. Dois nomes coincidem, dragão e tigre, e a coincidência morre ali.</p>
<p>Nenhum dos quatro aparece na face de uma peça. O que a mesa tem são dezesseis peças de vento que nomeiam leste, sul, oeste e norte sem bicho em cima.</p>

<h2>O relógio da mesa conta de quatro em quatro</h2>
<p>O zodíaco gira em doze. O mahjong gira em quatro. Quatro ventos, quatro assentos, quatro rodadas para fechar uma volta da mesa. Cada jogador banca uma vez por volta, e uma partida inteira pede quatro voltas, dezesseis mãos no mínimo.</p>
<p>O padrão japonês é mais curto: leste e sul, oito mãos. Quem joga só o leste termina em quatro. É o inverso de um calendário em que uma volta leva doze anos. Na mesa, uma volta leva uma noite.</p>

<h2>O ano do próprio animal</h2>
<p>A cada doze anos o seu animal volta, e a tradição chinesa trata o retorno como ano de cuidado, não de festa. A defesa mais comum é vermelho no corpo, cinto ou camiseta, dado por alguém mais velho da família.</p>
<p>Quem nasceu em 1990 vê o animal voltar pela terceira vez em 2026. O efeito na mão é zero. As 144 peças são as mesmas, o banqueiro continua leste e a muralha continua fechada antes da primeira compra. O que muda é o assunto da mesa e o volume de mensagens no grupo da família.</p>

<h2>Onde o animal do ano aparece de fato</h2>
<p>Em loja, não em mesa de jogo. Conjuntos de presente e caixas de Ano Novo trazem o animal na tampa, e alguns vêm com peças extras decorativas. Essas peças não pertencem a nenhum dos quatro grandes livros de regra, e a mesa que quiser usá-las precisa combinar a contagem em voz alta antes da primeira mão.</p>

<h2>Três decisões que o zodíaco não toma</h2>
<ul>
<li>Não escolhe assento. Lugar e vento saem da regra ou do sorteio, e o vento de cada jogador anda quando a vez passa.</li>
<li>Não escolhe descarte. O que você solta depende do que já está aberto na mesa, não do ano em que você nasceu.</li>
<li>Não decide vitória. A mão de catorze peças fecha com quatro conjuntos e um par em qualquer ano do ciclo.</li>
</ul>
<p>O que sobra para o zodíaco é a melhor parte da noite: conversa. Quem chega com a história do cavalo de fogo está puxando assunto, não pedindo aula de regra.</p>

<h2>Como usar isso sem estragar o jogo</h2>
<p>Em casa, trate o zodíaco como calendário. Se o ano é do cavalo, comente, ria e jogue. A partida rende mais e ninguém precisa defender o próprio signo no meio de uma mão.</p>
<p>Clube e torneio ficam de fora. Ali o regulamento manda, o assento sai no sorteio e tem árbitro de pé. Ninguém pergunta o seu signo ao preencher a ficha de inscrição, e insistir no assunto só atrasa a mesa.</p>
<p>Se o assunto da noite for calendário, ele tem vizinhos: o <a href="/cultura-mahjong/mahjong-ano-novo-chines/">mahjong no Ano Novo chinês</a> trata da mesa de festa, e o <a href="/cultura-mahjong/mahjong-feng-shui/">feng shui</a> trata do lugar onde ela fica. Para quem quer só sentar e jogar, o <a href="/jogar-mahjong/">Solitário</a> dispensa zodíaco, muralha e sorteio: a tela abre com as 112 peças já de face para cima. O resto está no <a href="/cultura-mahjong/">índice de Cultura</a>.</p>
"""

PT_RELATED = [
    ("https://jogomahjong.com/cultura-mahjong/mahjong-feng-shui/",
     "Mahjong e feng shui: onde sentar e o que a bússola mede de verdade"),
    ("https://jogomahjong.com/cultura-mahjong/mahjong-ano-novo-chines/",
     "Mahjong no Ano Novo chinês: a mesa que virou tradição de família"),
    ("https://jogomahjong.com/jogar-mahjong/", "Jogar Mahjong Solitário grátis"),
    ("https://jogomahjong.com/cultura-mahjong/", "Todos os artigos de Cultura"),
]

# ---------------------------------------------------------------- EN
EN_TITLE = "Mahjong and the Chinese Zodiac: Where the Twelve Animals Show Up, and Where They Don't"
EN_DESC = ("The 2026 fire horse, the twelve two-hour branches of the day, the twelve dragon tiles that are "
           "not animals, and why none of the 144 tiles changes with the year you were born.")
EN_H1 = EN_TITLE
EN_LEAD = ("Anyone born in 1978 reaches a fifth horse year in 2026 and usually mentions it before the tiles "
           "get washed. The zodiac fuels the table talk, but it does not touch a single face in the box.")

EN_BODY = """
<h2>The line that opens the evening</h2>
<p>Every group has one. Someone sits down and announces that this is their year, so they are winning tonight. In 2026 that belongs to anyone born in 1966, 1978, 1990, 2002 or 2014, because February 17 opened the Year of the Horse and it runs through February 5, 2027.</p>
<p>The question underneath is different, and it rarely gets answered: does the zodiac touch the tiles? Short answer, no. The long answer takes a few sections, because the box and the calendar lean on similar numbers for unrelated reasons.</p>

<h2>Twelve animals, twelve branches, twelve hours</h2>
<p>The Chinese zodiac is not a twelve-sign horoscope in the Western sense. It is a cycle of twelve earthly branches with an animal attached to each, and it turns on years, on months and on the hours of the day.</p>
<p>The hourly layer is the one nobody uses and the one that explains the most. Each branch covers two hours: the rat from 11 p.m. to 1 a.m., the horse from 11 a.m. to 1 p.m. The Chinese word for noon was built on the horse branch. Your wall clock has nothing to do with the table, but the name of the hour does.</p>
<p>On years, 2026 is the 33rd term of a sixty-year cycle pairing ten stems with twelve branches. The same pair comes back in 2086. Worth knowing, because "Year of the Horse" is not one thing: five horses sit inside the cycle, one per element, and 2026 is the fire horse.</p>

<h2>The twelve in the box is a different twelve</h2>
<p>The tally for a full box lands on 144: 108 suited, 16 winds, 12 dragons, 8 flowers. The only group that reaches twelve is the dragons, and it does not hold twelve different things. Three designs, four copies of each.</p>
<p>Those three are the red center, the green prosperity and the white board. Not one of them is an animal, and none is the zodiac dragon. The English name came out of the nineteenth-century export trade, which needed a label that sold. The three tiles get their own article in <a href="/culture-mahjong/dragon-symbolism-mahjong/">dragon symbolism</a>.</p>
<p>You can also divide 108 by 12 and land on nine, which happens to be how many numbers each suit carries. That is arithmetic, not symbolism: three suits of nine, four copies each, since four is what makes a pung, a chow and a pair possible at one table. A deck drawn from the zodiac would run twelve numbers per suit, and a fourteen-tile hand would never close again.</p>

<h2>The four guardians are not signs</h2>
<p>Anyone who has read about the winds knows the azure dragon, the vermilion bird, the white tiger and the black tortoise. They are direction guardians out of the twenty-eight lunar mansions, not zodiac animals. Two names overlap, dragon and tiger, and the overlap ends there.</p>
<p>None of the four is printed on a tile. What the table has is sixteen wind tiles naming east, south, west and north, with no creature on any of them.</p>

<h2>The table's clock counts in fours</h2>
<p>The zodiac turns in twelves. Mahjong turns in fours. Four winds, four seats, four deals to complete one turn of the table. Everybody deals once per turn, and a full game asks for four turns, sixteen hands at minimum.</p>
<p>The Japanese standard is shorter: east and south, eight hands. Play east only and you are done in four. That is the reverse of a calendar where one turn takes twelve years. At the table, a turn takes an evening.</p>

<h2>Your own animal year</h2>
<p>Every twelve years your animal comes back, and Chinese tradition treats the return as a year for caution rather than celebration. The usual defense is red worn on the body, a belt or a shirt, given by an older relative.</p>
<p>Someone born in 1990 meets the animal for the third time in 2026. The effect on the hand is zero. Same 144 tiles, dealer still east, wall still closed before the first draw. What changes is the table talk and the traffic in the family group chat.</p>

<h2>Where the year's animal actually shows up</h2>
<p>In shops, not on a playing table. Gift sets and New Year boxes print the animal on the lid, and a few ship with extra decorative tiles. Those tiles belong to none of the four major rule books, and a table that wants to use them has to agree on the count out loud before the first hand.</p>

<h2>Three calls the zodiac does not make</h2>
<ul>
<li>It does not pick the seat. Position and wind come from the rules or the draw, and each player's wind moves when the deal passes.</li>
<li>It does not pick the discard. What you let go depends on what is already face up, not on the year you were born.</li>
<li>It does not decide the win. A fourteen-tile hand closes with four melds and a pair in any year of the cycle.</li>
</ul>
<p>What is left for the zodiac is the best part of the night: talk. Someone arriving with the fire horse story is starting a conversation, not asking for a rules lecture.</p>

<h2>How to use it without wrecking the game</h2>
<p>At home, treat the zodiac as a calendar. If it is the horse's year, say so, laugh, and play. The hands run better and nobody has to defend a sign mid-turn.</p>
<p>Clubs and tournaments sit outside all this. The rule book runs the room, seats come out of a draw, and a referee is standing there. Nobody asks your animal on the entry form, and pressing the point only holds up the table.</p>
<p>If the talk at your table runs to calendars, it has neighbors: <a href="/culture-mahjong/mahjong-chinese-new-year/">mahjong at Chinese New Year</a> covers the holiday table, and <a href="/culture-mahjong/mahjong-feng-shui/">feng shui</a> covers the room it sits in. Anyone who just wants to play can skip the zodiac, the wall and the draw in <a href="/jogar-mahjong/">Solitaire</a>, which opens with its 112 tiles already turned up. The rest lives in the <a href="/culture-mahjong/">Culture index</a>.</p>
"""

EN_RELATED = [
    ("https://en.jogomahjong.com/culture-mahjong/mahjong-feng-shui/",
     "Mahjong and Feng Shui: Where to Sit and What a Compass Really Measures"),
    ("https://en.jogomahjong.com/culture-mahjong/mahjong-chinese-new-year/",
     "Mahjong at Chinese New Year: the table that became a family tradition"),
    ("https://en.jogomahjong.com/jogar-mahjong/", "Play Mahjong Solitaire free"),
    ("https://en.jogomahjong.com/culture-mahjong/", "All Culture articles"),
]


def words(t):
    t = re.sub(r"<[^>]+>", " ", t)
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
    "EYEBROW": "Cultura · Simbolismo", "H1": PT_H1, "LEAD": PT_LEAD,
    "BODY": PT_BODY.strip(),
    "RELATED_LINKS": "\n".join('              <li><a href="%s">%s</a></li>' % (u, t) for u, t in PT_RELATED),
    "SIDEBOX_PLAY": '            <li><a href="/jogar-mahjong/">Mahjong Solitário</a></li>',
    "SECTION_LABEL_PT": "Cultura", "HUB_URL_PT": "/cultura-mahjong/",
    "SECTION_LABEL_EN": "Cultura", "HUB_URL_EN": "/cultura-mahjong/",
}

en_map = {
    "TITLE": EN_TITLE, "DESCRIPTION": EN_DESC,
    "JSON_HEADLINE": EN_TITLE, "JSON_DESCRIPTION": EN_DESC,
    "CANONICAL_PT": CANON_PT, "CANONICAL_EN": CANON_EN,
    "EYEBROW": "Culture · Symbolism", "H1": EN_H1, "LEAD": EN_LEAD,
    "BODY": EN_BODY.strip(),
    "RELATED_LINKS": "\n".join('              <li><a href="%s">%s</a></li>' % (u, t) for u, t in EN_RELATED),
    "SIDEBOX_PLAY": '            <li><a href="/jogar-mahjong/">Mahjong Solitaire</a></li>',
    "SECTION_LABEL_EN": "Culture", "HUB_URL_EN": "/culture-mahjong/",
    "SECTION_LABEL_PT": "Cultura", "HUB_URL_PT": "/cultura-mahjong/",
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
