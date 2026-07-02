/*
 * Dados compartilhados das peças de Mahjong.
 * Usa os símbolos tradicionais chineses (Unicode U+1F000 - U+1F021)
 * com anotações em português do Brasil.
 *
 * Naipe (suit) em português:
 *   - vento    (风) : Leste, Sul, Oeste, Norte
 *   - dragão   (箭) : Vermelho, Verde, Branco
 *   - caractere(万) : 1 a 9 Wan
 *   - bambu    (索) : 1 a 9 Sou
 *   - círculo  (筒) : 1 a 9 Pin
 *   - flor     (花) : Ameixa, Orquídea, Bambu, Crisântemo
 *   - estação  (季) : Primavera, Verão, Outono, Inverno
 */
window.MAHJONG_TILES = (function () {
  // Ventos (Winds)
  const winds = [
    { id: "wind_east",  symbol: "🀀", cn: "東", name: "Leste",  suit: "vento", suitLabel: "Vento" },
    { id: "wind_south", symbol: "🀁", cn: "南", name: "Sul",    suit: "vento", suitLabel: "Vento" },
    { id: "wind_west",  symbol: "🀂", cn: "西", name: "Oeste",  suit: "vento", suitLabel: "Vento" },
    { id: "wind_north", symbol: "🀃", cn: "北", name: "Norte",  suit: "vento", suitLabel: "Vento" }
  ];

  // Dragões (Dragons)
  const dragons = [
    { id: "dragon_red",   symbol: "🀄", cn: "中", name: "Dragão Vermelho", suit: "dragão", suitLabel: "Dragão" },
    { id: "dragon_green", symbol: "🀅", cn: "發", name: "Dragão Verde",    suit: "dragão", suitLabel: "Dragão" },
    { id: "dragon_white", symbol: "🀆", cn: "白", name: "Dragão Branco",   suit: "dragão", suitLabel: "Dragão" }
  ];

  // Caracteres / Wan (万) - 1 a 9
  const characters = [
    { id: "char1", symbol: "🀇", cn: "一萬", name: "1 Caractere",  suit: "caractere", suitLabel: "Wan (万)" },
    { id: "char2", symbol: "🀈", cn: "二萬", name: "2 Caracteres", suit: "caractere", suitLabel: "Wan (万)" },
    { id: "char3", symbol: "🀉", cn: "三萬", name: "3 Caracteres", suit: "caractere", suitLabel: "Wan (万)" },
    { id: "char4", symbol: "🀊", cn: "四萬", name: "4 Caracteres", suit: "caractere", suitLabel: "Wan (万)" },
    { id: "char5", symbol: "🀋", cn: "五萬", name: "5 Caracteres", suit: "caractere", suitLabel: "Wan (万)" },
    { id: "char6", symbol: "🀌", cn: "六萬", name: "6 Caracteres", suit: "caractere", suitLabel: "Wan (万)" },
    { id: "char7", symbol: "🀍", cn: "七萬", name: "7 Caracteres", suit: "caractere", suitLabel: "Wan (万)" },
    { id: "char8", symbol: "🀎", cn: "八萬", name: "8 Caracteres", suit: "caractere", suitLabel: "Wan (万)" },
    { id: "char9", symbol: "🀏", cn: "九萬", name: "9 Caracteres", suit: "caractere", suitLabel: "Wan (万)" }
  ];

  // Bambus / Sou (索) - 1 a 9
  const bamboos = [
    { id: "bamboo1", symbol: "🀐", cn: "一索", name: "1 Bambu",  suit: "bambu", suitLabel: "Sou (索)" },
    { id: "bamboo2", symbol: "🀑", cn: "二索", name: "2 Bambus", suit: "bambu", suitLabel: "Sou (索)" },
    { id: "bamboo3", symbol: "🀒", cn: "三索", name: "3 Bambus", suit: "bambu", suitLabel: "Sou (索)" },
    { id: "bamboo4", symbol: "🀓", cn: "四索", name: "4 Bambus", suit: "bambu", suitLabel: "Sou (索)" },
    { id: "bamboo5", symbol: "🀔", cn: "五索", name: "5 Bambus", suit: "bambu", suitLabel: "Sou (索)" },
    { id: "bamboo6", symbol: "🀕", cn: "六索", name: "6 Bambus", suit: "bambu", suitLabel: "Sou (索)" },
    { id: "bamboo7", symbol: "🀖", cn: "七索", name: "7 Bambus", suit: "bambu", suitLabel: "Sou (索)" },
    { id: "bamboo8", symbol: "🀗", cn: "八索", name: "8 Bambus", suit: "bambu", suitLabel: "Sou (索)" },
    { id: "bamboo9", symbol: "🀘", cn: "九索", name: "9 Bambus", suit: "bambu", suitLabel: "Sou (索)" }
  ];

  // Círculos / Pin (筒) - 1 a 9
  const circles = [
    { id: "circle1", symbol: "🀙", cn: "一筒", name: "1 Círculo",  suit: "círculo", suitLabel: "Pin (筒)" },
    { id: "circle2", symbol: "🀚", cn: "二筒", name: "2 Círculos", suit: "círculo", suitLabel: "Pin (筒)" },
    { id: "circle3", symbol: "🀛", cn: "三筒", name: "3 Círculos", suit: "círculo", suitLabel: "Pin (筒)" },
    { id: "circle4", symbol: "🀜", cn: "四筒", name: "4 Círculos", suit: "círculo", suitLabel: "Pin (筒)" },
    { id: "circle5", symbol: "🀝", cn: "五筒", name: "5 Círculos", suit: "círculo", suitLabel: "Pin (筒)" },
    { id: "circle6", symbol: "🀞", cn: "六筒", name: "6 Círculos", suit: "círculo", suitLabel: "Pin (筒)" },
    { id: "circle7", symbol: "🀟", cn: "七筒", name: "7 Círculos", suit: "círculo", suitLabel: "Pin (筒)" },
    { id: "circle8", symbol: "🀠", cn: "八筒", name: "8 Círculos", suit: "círculo", suitLabel: "Pin (筒)" },
    { id: "circle9", symbol: "🀡", cn: "九筒", name: "9 Círculos", suit: "círculo", suitLabel: "Pin (筒)" }
  ];

  // Flores (Flowers) - conjunto especial
  const flowers = [
    { id: "flower1", symbol: "🀢", cn: "梅", name: "Ameixa",     suit: "flor", suitLabel: "Flor" },
    { id: "flower2", symbol: "🀣", cn: "蘭", name: "Orquídea",   suit: "flor", suitLabel: "Flor" },
    { id: "flower3", symbol: "🀤", cn: "竹", name: "Bambu-flor", suit: "flor", suitLabel: "Flor" },
    { id: "flower4", symbol: "🀥", cn: "菊", name: "Crisântemo", suit: "flor", suitLabel: "Flor" }
  ];

  // Estações (Seasons) - conjunto especial
  const seasons = [
    { id: "season1", symbol: "🀦", cn: "春", name: "Primavera", suit: "estação", suitLabel: "Estação" },
    { id: "season2", symbol: "🀧", cn: "夏", name: "Verão",     suit: "estação", suitLabel: "Estação" },
    { id: "season3", symbol: "🀨", cn: "秋", name: "Outono",    suit: "estação", suitLabel: "Estação" },
    { id: "season4", symbol: "🀩", cn: "冬", name: "Inverno",   suit: "estação", suitLabel: "Estação" }
  ];

  // Carta "fundo" genérica para o verso das peças
  const backTile = { id: "back", symbol: "🀫", cn: "麻", name: "Fundo", suit: "fundo", suitLabel: "" };

  const all = [].concat(winds, dragons, characters, bamboos, circles, flowers, seasons);

  // Agrupa por naipe, útil para galerias e legendas
  const groups = [
    { suit: "vento",     label: "Ventos (风)",     hint: "Direções cardeais",      tiles: winds },
    { suit: "dragão",    label: "Dragões (箭)",    hint: "Honras especiais",       tiles: dragons },
    { suit: "caractere", label: "Caracteres (万)", hint: "Números 1 a 9 em wan",   tiles: characters },
    { suit: "bambu",     label: "Bambus (索)",     hint: "Números 1 a 9 em sou",   tiles: bamboos },
    { suit: "círculo",   label: "Círculos (筒)",   hint: "Números 1 a 9 em pin",   tiles: circles },
    { suit: "flor",      label: "Flores (花)",     hint: "Conjunto especial",      tiles: flowers },
    { suit: "estação",   label: "Estações (季)",   hint: "Conjunto especial",      tiles: seasons }
  ];

  return {
    winds, dragons, characters, bamboos, circles, flowers, seasons,
    all, groups, backTile,
    // Seleção enxuta para jogos que precisam de poucos tipos
    core: [].concat(winds, dragons, characters.slice(0, 9), bamboos.slice(0, 9), circles.slice(0, 9))
  };
})();
