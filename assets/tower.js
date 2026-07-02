/*
 * Mahjong Torre — layout em torre vertical com 5 camadas.
 * Variante do solitário: apenas peças com topo livre e pelo menos
 * um lado livre podem ser selecionadas.
 * Dependência: /assets/tiles-data.js (window.MAHJONG_TILES)
 */
(function () {
  const board = document.querySelector("#tower-board");
  if (!board) return;

  const movesEl = document.querySelector("#moves");
  const pairsEl = document.querySelector("#pairs");
  const timeEl = document.querySelector("#time");
  const messageEl = document.querySelector("#game-message");
  const newGameBtn = document.querySelector("#new-game");
  const hintBtn = document.querySelector("#hint");
  const shuffleBtn = document.querySelector("#shuffle");

  const tileW = 108;
  const tileH = 147;
  const gapX = 8;
  const gapY = 6;
  const layerShift = 12;
  const rowFactor = 0.5;

  const T = window.MAHJONG_TILES;
  const tileTypes = T.core;

  // Layout em torre: 5 camadas, cada camada menor que a de baixo
  // z=0: base larga (9 col x 6 linhas)
  // z=1: 7 col x 5 linhas
  // z=2: 5 col x 4 linhas
  // z=3: 3 col x 3 linhas
  // z=4: 1 col x 2 linhas (topo)
  const layerConfigs = [
    { cols: 9, rows: 6, offsetCol: 0, offsetRow: 0 },
    { cols: 7, rows: 5, offsetCol: 1, offsetRow: 0.5 },
    { cols: 5, rows: 4, offsetCol: 2, offsetRow: 1 },
    { cols: 3, rows: 3, offsetCol: 3, offsetRow: 1.5 },
    { cols: 1, rows: 2, offsetCol: 4, offsetRow: 2 }
  ];

  let tiles = [];
  let selected = null;
  let moves = 0;
  let removedPairs = 0;
  let startedAt = null;
  let timer = null;
  let totalPairs = 0;

  function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
  }

  function buildLayout() {
    const layout = [];
    layerConfigs.forEach((cfg, z) => {
      for (let r = 0; r < cfg.rows; r++) {
        for (let c = 0; c < cfg.cols; c++) {
          layout.push({
            r: r + cfg.offsetRow,
            c: c + cfg.offsetCol,
            z: z
          });
        }
      }
    });
    return layout;
  }

  function buildDeck(count) {
    const pairsNeeded = Math.floor(count / 2);
    const deck = [];
    for (let i = 0; i < pairsNeeded; i++) {
      const type = tileTypes[i % tileTypes.length];
      deck.push(type, type);
    }
    return shuffle(deck);
  }

  function startGame() {
    tiles = [];
    selected = null;
    moves = 0;
    removedPairs = 0;
    startedAt = Date.now();
    if (timer) clearInterval(timer);
    timer = setInterval(updateTimer, 1000);

    const layout = buildLayout();
    const deck = buildDeck(layout.length);
    totalPairs = Math.floor(layout.length / 2);

    layout.forEach((pos, i) => {
      tiles.push({
        id: i,
        type: deck[i],
        r: pos.r,
        c: pos.c,
        z: pos.z,
        removed: false,
        el: null
      });
    });

    renderBoard();
    updateStats();
    setMessage("Boa sorte! Combine duas peças iguais livres.");
  }

  function renderBoard() {
    board.innerHTML = "";
    tiles.forEach(tile => {
      if (tile.removed) return;
      const el = document.createElement("div");
      el.className = "tile";
      el.dataset.suit = tile.type.suit;
      el.dataset.id = tile.id;
      el.style.position = "absolute";
      el.style.width = tileW + "px";
      el.style.height = tileH + "px";
      const x = tile.c * (tileW + gapX) - tile.z * layerShift;
      const y = tile.r * (tileH * rowFactor + gapY) - tile.z * layerShift;
      el.style.left = x + "px";
      el.style.top = y + "px";
      el.style.zIndex = tile.z * 100 + tile.r * 10 + tile.c;
      el.innerHTML = `
        <div class="tile-face">
          <div class="tile-symbol">${tile.type.symbol}</div>
          <div class="tile-name">${tile.type.name}</div>
        </div>
      `;
      el.addEventListener("click", () => onTileClick(tile));
      tile.el = el;
      board.appendChild(el);
    });
    updateFreeTiles();
  }

  function isTileFree(tile) {
    if (tile.removed) return false;
    // Verificar se há alguma peça acima (cobrindo o topo)
    const hasAbove = tiles.some(t => {
      if (t.removed || t.z <= tile.z) return false;
      // Verificar sobreposição horizontal e vertical
      const overlapX = Math.abs(t.c - tile.c) < 0.9;
      const overlapY = Math.abs(t.r - tile.r) < 0.9;
      return overlapX && overlapY;
    });
    if (hasAbove) return false;

    // Verificar se tem pelo menos um lado livre (esquerdo ou direito)
    const hasLeft = tiles.some(t => {
      if (t.removed || t.z !== tile.z) return false;
      return Math.abs(t.r - tile.r) < 0.5 && Math.abs(t.c - tile.c - 1) < 0.3;
    });
    const hasRight = tiles.some(t => {
      if (t.removed || t.z !== tile.z) return false;
      return Math.abs(t.r - tile.r) < 0.5 && Math.abs(t.c - tile.c + 1) < 0.3;
    });

    return !hasLeft || !hasRight;
  }

  function updateFreeTiles() {
    tiles.forEach(tile => {
      if (tile.removed || !tile.el) return;
      if (isTileFree(tile)) {
        tile.el.classList.add("free");
        tile.el.style.pointerEvents = "auto";
      } else {
        tile.el.classList.remove("free");
        tile.el.style.pointerEvents = "none";
      }
    });
  }

  function onTileClick(tile) {
    if (!isTileFree(tile)) return;
    window.MAHJONG_SOUND?.select();

    if (!selected) {
      selected = tile;
      tile.el.classList.add("selected");
      return;
    }

    if (selected.id === tile.id) {
      selected.el.classList.remove("selected");
      selected = null;
      return;
    }

    moves++;

    if (selected.type.id === tile.type.id) {
      window.MAHJONG_SOUND?.match();
      selected.el.classList.add("removing");
      tile.el.classList.add("removing");
      const a = selected;
      const b = tile;
      setTimeout(() => {
        a.removed = true;
        b.removed = true;
        removedPairs++;
        selected = null;
        renderBoard();
        updateStats();
        if (removedPairs >= totalPairs) {
          window.MAHJONG_SOUND?.win();
          setMessage("Parabéns! Você desmontou a torre toda!");
          clearInterval(timer);
        } else {
          const pair = findHintPair();
          if (!pair) {
            setMessage("Sem jogadas disponíveis. Use embaralhar ou dica.");
          } else {
            setMessage("Par removido! Continue desmontando.");
          }
        }
      }, 280);
    } else {
      window.MAHJONG_SOUND?.error();
      tile.el.classList.add("shake");
      selected.el.classList.add("shake");
      setTimeout(() => {
        tile.el?.classList.remove("shake");
        selected?.el?.classList.remove("shake");
      }, 320);
      selected.el.classList.remove("selected");
      selected = null;
    }
  }

  function findHintPair() {
    const free = tiles.filter(t => !t.removed && isTileFree(t));
    for (let i = 0; i < free.length; i++) {
      for (let j = i + 1; j < free.length; j++) {
        if (free[i].type.id === free[j].type.id) {
          return [free[i], free[j]];
        }
      }
    }
    return null;
  }

  function updateStats() {
    if (movesEl) movesEl.textContent = moves;
    if (pairsEl) pairsEl.textContent = `${removedPairs}/${totalPairs}`;
  }

  function updateTimer() {
    if (!startedAt || !timeEl) return;
    const s = Math.floor((Date.now() - startedAt) / 1000);
    const mm = String(Math.floor(s / 60)).padStart(2, "0");
    const ss = String(s % 60).padStart(2, "0");
    timeEl.textContent = `${mm}:${ss}`;
  }

  function setMessage(msg) {
    if (messageEl) messageEl.textContent = msg;
  }

  function doHint() {
    const pair = findHintPair();
    if (!pair) {
      setMessage("Nenhuma dica disponível. Tente embaralhar!");
      window.MAHJONG_SOUND?.error();
      return;
    }
    window.MAHJONG_SOUND?.hint();
    pair.forEach(t => {
      if (t.el) t.el.classList.add("hint-glow");
    });
    setTimeout(() => {
      pair.forEach(t => {
        if (t.el) t.el.classList.remove("hint-glow");
      });
    }, 1800);
    setMessage("Lá vai uma dica — duas peças livres piscando!");
  }

  function doShuffle() {
    window.MAHJONG_SOUND?.shuffle();
    const remaining = tiles.filter(t => !t.removed);
    const types = remaining.map(t => t.type);
    shuffle(types);
    remaining.forEach((t, i) => {
      t.type = types[i];
    });
    selected = null;
    renderBoard();
    updateStats();
    setMessage("Peças embaralhadas! Novas oportunidades apareceram.");
  }

  newGameBtn?.addEventListener("click", startGame);
  hintBtn?.addEventListener("click", doHint);
  shuffleBtn?.addEventListener("click", doShuffle);

  startGame();
})();
