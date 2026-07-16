/*
 * Shared Mahjong tile data.
 * Uses traditional Chinese symbols (Unicode U+1F000 - U+1F021)
 * with English annotations.
 *
 * Suit in English:
 *   - wind     (风) : East, South, West, North
 *   - dragon   (箭) : Red, Green, White
 *   - character(万) : 1 to 9 Wan
 *   - bamboo   (索) : 1 to 9 Sou
 *   - circle   (筒) : 1 to 9 Pin
 *   - flower   (花) : Plum, Orchid, Bamboo, Chrysanthemum
 *   - season   (季) : Spring, Summer, Autumn, Winter
 */
window.MAHJONG_TILES = (function () {
  const winds = [
    { id: "wind_east",  symbol: "🀀", cn: "東", name: "East",   suit: "wind", suitLabel: "Wind" },
    { id: "wind_south", symbol: "🀁", cn: "南", name: "South",  suit: "wind", suitLabel: "Wind" },
    { id: "wind_west",  symbol: "🀂", cn: "西", name: "West",   suit: "wind", suitLabel: "Wind" },
    { id: "wind_north", symbol: "🀃", cn: "北", name: "North",  suit: "wind", suitLabel: "Wind" }
  ];

  const dragons = [
    { id: "dragon_red",   symbol: "🀄", cn: "中", name: "Red Dragon",   suit: "dragon", suitLabel: "Dragon" },
    { id: "dragon_green", symbol: "🀅", cn: "發", name: "Green Dragon", suit: "dragon", suitLabel: "Dragon" },
    { id: "dragon_white", symbol: "🀆", cn: "白", name: "White Dragon", suit: "dragon", suitLabel: "Dragon" }
  ];

  const characters = [
    { id: "char1", symbol: "🀇", cn: "一萬", name: "1 Character",  suit: "character", suitLabel: "Wan (万)" },
    { id: "char2", symbol: "🀈", cn: "二萬", name: "2 Characters", suit: "character", suitLabel: "Wan (万)" },
    { id: "char3", symbol: "🀉", cn: "三萬", name: "3 Characters", suit: "character", suitLabel: "Wan (万)" },
    { id: "char4", symbol: "🀊", cn: "四萬", name: "4 Characters", suit: "character", suitLabel: "Wan (万)" },
    { id: "char5", symbol: "🀋", cn: "五萬", name: "5 Characters", suit: "character", suitLabel: "Wan (万)" },
    { id: "char6", symbol: "🀌", cn: "六萬", name: "6 Characters", suit: "character", suitLabel: "Wan (万)" },
    { id: "char7", symbol: "🀍", cn: "七萬", name: "7 Characters", suit: "character", suitLabel: "Wan (万)" },
    { id: "char8", symbol: "🀎", cn: "八萬", name: "8 Characters", suit: "character", suitLabel: "Wan (万)" },
    { id: "char9", symbol: "🀏", cn: "九萬", name: "9 Characters", suit: "character", suitLabel: "Wan (万)" }
  ];

  const bamboos = [
    { id: "bamboo1", symbol: "🀐", cn: "一索", name: "1 Bamboo",  suit: "bamboo", suitLabel: "Sou (索)" },
    { id: "bamboo2", symbol: "🀑", cn: "二索", name: "2 Bamboo", suit: "bamboo", suitLabel: "Sou (索)" },
    { id: "bamboo3", symbol: "🀒", cn: "三索", name: "3 Bamboo", suit: "bamboo", suitLabel: "Sou (索)" },
    { id: "bamboo4", symbol: "🀓", cn: "四索", name: "4 Bamboo", suit: "bamboo", suitLabel: "Sou (索)" },
    { id: "bamboo5", symbol: "🀔", cn: "五索", name: "5 Bamboo", suit: "bamboo", suitLabel: "Sou (索)" },
    { id: "bamboo6", symbol: "🀕", cn: "六索", name: "6 Bamboo", suit: "bamboo", suitLabel: "Sou (索)" },
    { id: "bamboo7", symbol: "🀖", cn: "七索", name: "7 Bamboo", suit: "bamboo", suitLabel: "Sou (索)" },
    { id: "bamboo8", symbol: "🀗", cn: "八索", name: "8 Bamboo", suit: "bamboo", suitLabel: "Sou (索)" },
    { id: "bamboo9", symbol: "🀘", cn: "九索", name: "9 Bamboo", suit: "bamboo", suitLabel: "Sou (索)" }
  ];

  const circles = [
    { id: "circle1", symbol: "🀙", cn: "一筒", name: "1 Circle",  suit: "circle", suitLabel: "Pin (筒)" },
    { id: "circle2", symbol: "🀚", cn: "二筒", name: "2 Circles", suit: "circle", suitLabel: "Pin (筒)" },
    { id: "circle3", symbol: "🀛", cn: "三筒", name: "3 Circles", suit: "circle", suitLabel: "Pin (筒)" },
    { id: "circle4", symbol: "🀜", cn: "四筒", name: "4 Circles", suit: "circle", suitLabel: "Pin (筒)" },
    { id: "circle5", symbol: "🀝", cn: "五筒", name: "5 Circles", suit: "circle", suitLabel: "Pin (筒)" },
    { id: "circle6", symbol: "🀞", cn: "六筒", name: "6 Circles", suit: "circle", suitLabel: "Pin (筒)" },
    { id: "circle7", symbol: "🀟", cn: "七筒", name: "7 Circles", suit: "circle", suitLabel: "Pin (筒)" },
    { id: "circle8", symbol: "🀠", cn: "八筒", name: "8 Circles", suit: "circle", suitLabel: "Pin (筒)" },
    { id: "circle9", symbol: "🀡", cn: "九筒", name: "9 Circles", suit: "circle", suitLabel: "Pin (筒)" }
  ];

  const flowers = [
    { id: "flower1", symbol: "🀢", cn: "梅", name: "Plum",         suit: "flower", suitLabel: "Flower" },
    { id: "flower2", symbol: "🀣", cn: "蘭", name: "Orchid",       suit: "flower", suitLabel: "Flower" },
    { id: "flower3", symbol: "🀤", cn: "竹", name: "Bamboo-flower", suit: "flower", suitLabel: "Flower" },
    { id: "flower4", symbol: "🀥", cn: "菊", name: "Chrysanthemum", suit: "flower", suitLabel: "Flower" }
  ];

  const seasons = [
    { id: "season1", symbol: "🀦", cn: "春", name: "Spring", suit: "season", suitLabel: "Season" },
    { id: "season2", symbol: "🀧", cn: "夏", name: "Summer", suit: "season", suitLabel: "Season" },
    { id: "season3", symbol: "🀨", cn: "秋", name: "Autumn", suit: "season", suitLabel: "Season" },
    { id: "season4", symbol: "🀩", cn: "冬", name: "Winter", suit: "season", suitLabel: "Season" }
  ];

  const backTile = { id: "back", symbol: "🀫", cn: "麻", name: "Back", suit: "back", suitLabel: "" };

  const all = [].concat(winds, dragons, characters, bamboos, circles, flowers, seasons);

  const core = [].concat(winds, dragons, characters, bamboos, circles);

  const groups = [
    { suit: "wind",      label: "Winds (风)",       hint: "Cardinal directions",     tiles: winds },
    { suit: "dragon",    label: "Dragons (箭)",     hint: "Honor tiles",             tiles: dragons },
    { suit: "character", label: "Characters (万)",  hint: "Numbers 1-9 in wan",      tiles: characters },
    { suit: "bamboo",    label: "Bamboo (索)",      hint: "Numbers 1-9 in sou",      tiles: bamboos },
    { suit: "circle",    label: "Circles (筒)",     hint: "Numbers 1-9 in pin",      tiles: circles },
    { suit: "flower",    label: "Flowers (花)",     hint: "Special set",             tiles: flowers },
    { suit: "season",    label: "Seasons (季)",     hint: "Special set",             tiles: seasons }
  ];

  return {
    winds, dragons, characters, bamboos, circles, flowers, seasons,
    all, groups, backTile, core
  };
})();