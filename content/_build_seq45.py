# -*- coding: utf-8 -*-
"""Build PT + EN article seq=45 — mahjong e o feng shui / mahjong and feng shui."""
import os, re, json

ROOT = os.getcwd()
TODAY = "2026-11-23"

PT_DIR = "cultura-mahjong/mahjong-feng-shui"
EN_DIR = "en/culture-mahjong/mahjong-feng-shui"
CANON_PT = "https://jogomahjong.com/cultura-mahjong/mahjong-feng-shui/"
CANON_EN = "https://en.jogomahjong.com/culture-mahjong/mahjong-feng-shui/"

# ---------------------------------------------------------------- PT
PT_TITLE = "Mahjong e feng shui: onde sentar e o que a bússola mede de verdade"
PT_DESC = ("As dezesseis peças de vento, as quatro direções com estação, cor e elemento, a cadeira de "
           "costas para a porta e o motivo pelo qual a regra do jogo já resolve o assento sozinha.")
PT_H1 = PT_TITLE
PT_LEAD = ("Tem sempre um jogador que chega antes e recusa a cadeira de costas para a porta. A escolha tem "
           "nome, escola e bússola, e o dado da primeira rodada pode desfazer tudo em quatro mãos.")

PT_BODY = """
<h2>A cadeira que ninguém quer</h2>
<p>Numa sala de mahjong, a pior cadeira é a que fica de costas para a porta. Você não vê quem entra, não vê a saída e passa a noite virando a cabeça a cada passo no corredor.</p>
<p>Quem pratica feng shui tem nome para isso. A posição favorável é a diagonal oposta à entrada, com parede maciça atrás, e a cadeira de costas para o vão é justamente a que fica sem apoio. A regra nasceu para cama, mesa de jantar e escrivaninha. A mesa de mahjong entrou na lista depois, quando o jogo virou hábito de salão no fim do século XIX, e entrou por analogia.</p>

<h2>As quatro direções já estão no baralho</h2>
<p>Dezesseis das 144 peças são vento. Quatro direções, quatro cópias de cada: leste, sul, oeste e norte. Nenhuma outra peça do conjunto nomeia um ponto cardeal, e é essa parte do baralho que dá ao feng shui algo concreto para comentar.</p>
<p>A tradição chinesa liga cada direção a uma estação, um elemento, uma cor e um animal guardião. Leste é primavera, madeira, verde e o dragão azul. Sul é verão, fogo, vermelho e a ave vermelha. Oeste é outono, metal, branco e o tigre branco. Norte é inverno, água, preto e a tartaruga negra. O centro, que na mesa é o espaço onde caem os descartes, é terra e amarelo.</p>
<p>A tabela tem mais de dois mil anos e serve para orientar casa, túmulo e cidade. O atrito aparece quando ela é levada para um jogo em que a direção de cada jogador muda por regra.</p>

<h2>Sentar de costas para o norte e olhar o sul</h2>
<p>A orientação mais citada da arquitetura chinesa é sentar ao norte e olhar ao sul. Os salões principais da Cidade Proibida abrem para o sul, e nas casas antigas o assento de honra é o do fundo do cômodo, de frente para a porta.</p>
<p>Transportada para a mesa, a ideia virou conselho de salão: procure a cadeira virada para o sul. Só que o mahjong não distribui assento por mérito. O banqueiro é leste, e os ventos sul, oeste e norte caem sobre os outros três conforme a vez corre. O que sobra de escolha ao jogador é onde pendurar o casaco.</p>

<h2>A mesa quadrada e o nome que ela carrega</h2>
<p>Mesa de mahjong de casa é quadrada, um jogador por lado, e no interior da China costuma ser a mesma em que a família janta. O nome tradicional é mesa dos oito imortais, porque cabem oito pessoas, duas por lado.</p>
<p>A forma tem leitura cosmológica: quatro lados, quatro estações, quatro direções, um centro. Na mesa, o centro é para onde vão os descartes, e é ele que fica visível para os quatro ao mesmo tempo.</p>

<h2>O que a bússola mede</h2>
<p>Quem leva feng shui a sério usa a bússola geomântica, com vinte e quatro direções no aro externo. A leitura não é feita na mesa. É feita na porta de entrada do imóvel, com a fachada medida ali, e vale para a casa inteira.</p>
<p>Existe uma razão de doutrina para a mesa ficar de fora. A escola que organiza residências parte de três elementos fixos: a porta, o cômodo principal e o fogão. Móvel que se arrasta não entra nessa conta, porque a leitura não muda quando ele muda de lugar.</p>
<p>Daí uma conclusão prática. Empurrar a mesa dois metros não altera direção nenhuma da casa. O que altera a noite é o que está atrás do jogador, e isso é conforto, não cálculo.</p>

<h2>Uma rodada inteira em cada direção</h2>
<p>A regra do jogo resolve a geografia sem ajuda. O banqueiro abre a partida como leste. Se não fecha a mão, a vez de banqueiro anda uma cadeira para a direita e o vento vai junto, então a mesa gira sem que ninguém se levante. Ao fim de quatro rodadas, todo mundo já ocupou as quatro direções e foi banqueiro quatro vezes.</p>
<p>Quem sentou na cadeira ruim fica nela uma rodada, no máximo, e a mesa troca de posição sem ninguém levantar.</p>
<p>No riichi a direção é sorteada antes da primeira peça: cada jogador tira uma peça de vento e senta onde ela manda. Os dados decidem só onde a muralha abre.</p>
<p>Em Sichuan o assunto nem chega. O conjunto tem 108 peças, sem vento e sem dragão, e nenhuma peça do baralho aponta para um lado. Numa mesa de Chengdu, feng shui de assento é conversa de intervalo.</p>

<h2>O que muda a noite de verdade</h2>
<p>Três arranjos de sala têm consequência real.</p>
<ul>
<li>Parede atrás do jogador. Cadeira encostada em parede evita o vaivém da casa e o esbarrão na mesa.</li>
<li>Nada de viga baixa em cima da mesa. Viga força a cabeça para baixo e corta a luz justamente sobre as peças.</li>
<li>Porta fora das costas de todos. Se não der, ao menos mantenha a porta fechada: corrente de ar derruba peça leve.</li>
</ul>
<p>A terceira é a única com efeito de jogo. Peça que cai da mesa é peça exposta, e peça exposta é informação de graça para os outros três.</p>

<h2>Quando a tradição ajuda e quando atrapalha</h2>
<p>Para jogar em casa, use o feng shui como projeto de sala. Mesa no canto, parede atrás, luz de cima, ninguém de costas para o corredor. A partida rende mais e ninguém discute bússola no meio da mão.</p>
<p>A exceção é clube e torneio. Lá existe sorteio de lugar, folha de regra impressa e árbitro. Levar a bússola para a mesa de torneio não muda a muralha, não muda o dado e não muda a mão. Muda o tempo que você perde reclamando da cadeira.</p>
<p>Se a conversa da noite for essa, ela tem parentes próximos: o descarte que assusta aparece em <a href="/cultura-mahjong/mahjong-supersticao/">mahjong e superstição</a>, o peso do acaso em <a href="/cultura-mahjong/mahjong-e-a-sorte/">mahjong e a sorte</a>, e a face de cada peça no <a href="/cultura-mahjong/significado-das-pecas-de-mahjong/">significado das peças</a>.</p>
<p>Para quem quer só sentar e jogar, o <a href="/jogar-mahjong/">Solitário</a> resolve o assento de outro jeito: uma cadeira, nenhuma porta atrás e as 112 peças à vista desde a primeira jogada. O resto das dúvidas de mesa está no <a href="/cultura-mahjong/">índice de Cultura</a>.</p>
"""

PT_RELATED = [
    ("https://jogomahjong.com/cultura-mahjong/mahjong-supersticao/",
     "Mahjong e superstição: o que a mesa evita e o que a regra resolve"),
    ("https://jogomahjong.com/cultura-mahjong/mahjong-e-a-sorte/",
     "Mahjong e a sorte na cultura chinesa: o que o acaso decide de verdade"),
    ("https://jogomahjong.com/jogar-mahjong/", "Jogar Mahjong Solitário grátis"),
    ("https://jogomahjong.com/cultura-mahjong/", "Todos os artigos de Cultura"),
]

# ---------------------------------------------------------------- EN
EN_TITLE = "Mahjong and Feng Shui: Where to Sit and What a Compass Really Measures"
EN_DESC = ("The sixteen wind tiles, the four directions with their seasons, colors and elements, the chair "
           "with its back to the door, and why the rules already settle the seating on their own.")
EN_H1 = EN_TITLE
EN_LEAD = ("Someone always arrives early and refuses the chair with its back to the door. The choice has a "
           "name, a school and a compass behind it, and the first roll of the dice can wipe it out in four hands.")

EN_BODY = """
<h2>The chair nobody wants</h2>
<p>In a mahjong room the worst seat is the one facing away from the door. You cannot see who walks in, you cannot see the exit, and you spend the evening turning your head at every sound in the hallway.</p>
<p>Feng shui has a name for this. The favorable spot is the diagonal opposite the entrance, with a solid wall behind you, and the chair backing onto the doorway is the one left without support. The rule was written for beds, dining tables and desks. Mahjong tables joined the list later, when the game became a teahouse habit in the late nineteenth century, and they joined by analogy.</p>

<h2>Four directions come with the tiles</h2>
<p>Sixteen of the 144 tiles are winds. Four directions, four copies each: east, south, west and north. No other tile in the set names a compass point, and that corner of the box is what gives feng shui something concrete to talk about.</p>
<p>Chinese tradition ties each direction to a season, an element, a color and a guardian animal. East is spring, wood, green and the azure dragon. South is summer, fire, red and the vermilion bird. West is autumn, metal, white and the white tiger. North is winter, water, black and the black tortoise. The center, which on the table is the bare space where discards land, is earth and yellow.</p>
<p>The table is over two thousand years old and was built to orient houses, graves and cities. Friction starts when it gets carried over to a game where each player's direction changes by rule.</p>

<h2>Sitting with your back to the north</h2>
<p>The most quoted orientation in Chinese architecture is to sit north and face south. The main halls of the Forbidden City open south, and in old houses the seat of honor is the one at the far end of the room, facing the door.</p>
<p>Moved to the table, the idea becomes club advice: take the chair facing south. Mahjong does not hand out seats by merit, though. The dealer is east, the other three take south, west and north in turn order, and the only thing a player picks is where to hang a coat.</p>

<h2>The square table and the name it carries</h2>
<p>A household mahjong table is square, one player to a side, and in most of China it is the same table the family eats at. The traditional name is the table of the eight immortals, because eight people fit, two per side.</p>
<p>The shape carries a cosmological reading: four sides, four seasons, four directions, one center. On the table the center is where discards go, and it is the one spot all four players can see at once.</p>

<h2>What the compass measures</h2>
<p>Anyone serious about feng shui uses the geomantic compass, with twenty-four directions on its outer ring. The reading is not taken at the table. It is taken at the front door of the building, with the facing measured there, and it applies to the whole home.</p>
<p>There is a doctrinal reason the table stays out of it. The school that organizes a dwelling starts from three fixed elements: the door, the main room and the stove. Furniture that gets dragged around does not enter that count, because the reading does not change when it moves.</p>
<p>Which leads somewhere practical. Shoving the table two meters to the left changes no direction in the house. What changes the evening is what sits behind each player, and that is comfort rather than calculation.</p>

<h2>One round in every seat</h2>
<p>The rules settle the geography without any help. The opening dealer sits east. Fail to win a hand as dealer and the deal moves one chair to your right, taking the east wind along, so the table rotates without anyone standing up. Four rounds in, every player has held all four seats and dealt four times.</p>
<p>Nobody stuck in the bad chair stays there all night. One round at most, and the table rotates without anyone standing up.</p>
<p>Riichi draws for it before the first tile: each player takes a wind tile and sits where it points. The dice only decide where the wall opens.</p>
<p>Sichuan never gets that far. The set has 108 tiles, no winds and no dragons, and not one tile in the box points anywhere. At a Chengdu table, seat feng shui is interval conversation.</p>

<h2>What actually changes the evening</h2>
<p>Three room arrangements have real consequences, and none of them needs a compass.</p>
<ul>
<li>A wall behind each player. A chair backed against plaster keeps the household traffic and the hip-check out of the game.</li>
<li>No low beam over the table. A beam pulls your head down and cuts the light exactly where the tiles are.</li>
<li>Doors off everyone's back. If that is impossible, at least keep the door shut, since a draft takes light tiles off the table.</li>
</ul>
<p>The third one has a playing consequence. A tile that hits the floor is a tile revealed, and a revealed tile is free information for the other three.</p>

<h2>When tradition helps and when it wastes the night</h2>
<p>For a home game, treat feng shui as room design. Table in the corner, wall behind, light from above, nobody facing a busy corridor. The hands run better and no one argues about a compass mid-hand.</p>
<p>Clubs and tournaments are the exception. Seats are drawn, a printed rule sheet exists, and a referee is standing there. Bringing the compass to a tournament table changes no wall, no dice and no hand. It changes the time you lose complaining about the chair.</p>
<p>If that is the conversation at your table, it has close relatives. The discard that spooks people gets its own piece in <a href="/culture-mahjong/mahjong-superstition/">mahjong and superstition</a>, the weight of chance gets one in <a href="/culture-mahjong/mahjong-and-luck/">mahjong and luck</a>, and every face is explained in <a href="/culture-mahjong/meaning-of-mahjong-tiles/">the meaning of the tiles</a>.</p>
<p>For anyone who just wants to sit down and play, <a href="/jogar-mahjong/">Solitaire</a> removes the seating question entirely: one chair, no door behind you, and all 112 tiles face up from the first move. The rest of the table questions live in the <a href="/culture-mahjong/">Culture index</a>.</p>
"""

EN_RELATED = [
    ("https://en.jogomahjong.com/culture-mahjong/mahjong-superstition/",
     "Mahjong and superstition: what the table avoids and what the rules settle"),
    ("https://en.jogomahjong.com/culture-mahjong/mahjong-and-luck/",
     "Mahjong and luck in Chinese culture: what chance really decides"),
    ("https://en.jogomahjong.com/jogar-mahjong/", "Play Mahjong Solitaire free"),
    ("https://en.jogomahjong.com/culture-mahjong/", "All Culture articles"),
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
    "EYEBROW": "Cultura · Simbolismo", "H1": PT_H1, "LEAD": PT_LEAD,
    "BODY": PT_BODY.strip(),
    "RELATED_LINKS": "\n".join('              <li><a href="%s">%s</a></li>' % (u, t) for u, t in PT_RELATED),
    "SIDEBOX_PLAY": '            <li><a href="/jogar-mahjong/">Mahjong Solitário</a></li>',
    "SECTION_LABEL_PT": "Cultura", "HUB_URL_PT": "/cultura-mahjong/",
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
