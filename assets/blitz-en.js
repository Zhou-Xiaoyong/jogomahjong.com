/*
 * Mahjong Blitz — 60-second race mode.
 * The board automatically refreshes to keep up the pace.
 * Dependency: /assets/tiles-data.js (window.MAHJONG_TILES)
 */
(function () {
  const board = document.querySelector("#blitz-board");
  if (!board) return;

  const scoreEl = document.querySelector("#score");
  const pairsEl = document.querySelector("#pairs");
  const timeEl = document.querySelector("#time");
  const bestEl = document.querySelector("#best");
  const messageEl = document.querySelector("#game-message");
  const newGameBtn = document.querySelector("#new-game");
  const hintBtn = document.querySelector("#hint");

  const tileW = 72;
  const tileH = 98;
  const gapX = 10;
  const gapY = 8;
  const layerShift = 10;
  const rowFactor = 0.5;

  const GAME_DURATION = 60;
  const POINTS_PER_PAIR = 10;

  const T = window.MAHJONG_TILES;
  const tileTypes = T.core;

  // Simple layout: 3 layers, 8x5 base
  const layerConfigs = [
    { cols: 8, rows: 5, offsetCol: 0, offsetRow: 0 },
    { cols: 6, rows: 4, offsetCol: 1, offsetRow: 0.5 },
    { cols: 4, rows: 3, offsetCol: 2, offsetRow: 1 }
  ];

  let tiles = [];
  let selected = null;
  let score = 0;
  let pairs = 0;
  let timeLeft = GAME_DURATION;
  let timer = null;
  let gameOver = false;
  let bestScore = 0;

  try {
    bestScore = parseInt(localStorage.getItem("mahjong_blitz_best") || "0", 10);
  } catch (e) { bestScore = 0; }
  if (bestEl) bestEl.textContent = bestScore;

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
          layout.push({ r: r + cfg.offsetRow, c: c + cfg.offsetCol, z });
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
    score = 0;
    pairs = 0;
    timeLeft = GAME_DURATION;
    gameOver = false;
    if (timer) clearInterval(timer);

    const layout = buildLayout();
    const deck = buildDeck(layout.length);

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

    timer = setInterval(() => {
      timeLeft--;
      if (timeEl) timeEl.textContent = timeLeft;
      if (timeLeft <= 10 && timeEl) {
        timeEl.style.color = "var(--chinese-red)";
        timeEl.style.animation = "cdPulse .6s ease-in-out infinite";
      }
      if (timeLeft <= 0) endGame();
    }, 1000);

    renderBoard();
    updateStats();
    setMessage("Go! 60 seconds — match as many pairs as possible!");
  }

  function renderBoard() {
    board.innerHTML = "";
    tiles.forEach(tile => {
      if (tile.removed) return;
      const el = document.createElement("div");
      el.className = "tile";
      el.dataset.suit = tile.type.suit;
      el.dataset.id = tile.type.id;
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
    const hasAbove = tiles.some(t => {
      if (t.removed || t.z <= tile.z) return false;
      const overlapX = Math.abs(t.c - tile.c) < 0.9;
      const overlapY = Math.abs(t.r - tile.r) < 0.9;
      return overlapX && overlapY;
    });
    if (hasAbove) return false;

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
    if (gameOver) return;
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

    if (selected.type.id === tile.type.id) {
      window.MAHJONG_SOUND?.match();
      selected.el.classList.add("removing");
      tile.el.classList.add("removing");
      const a = selected;
      const b = tile;
      setTimeout(() => {
        a.removed = true;
        b.removed = true;
        pairs++;
        score += POINTS_PER_PAIR;
        selected = null;
        renderBoard();
        updateStats();
        checkRefill();
      }, 200);
    } else {
      window.MAHJONG_SOUND?.error();
      tile.el.classList.add("shake");
      selected.el.classList.add("shake");
      setTimeout(() => {
        tile.el?.classList.remove("shake");
        selected?.el?.classList.remove("shake");
      }, 250);
      selected.el.classList.remove("selected");
      selected = null;
    }
  }

  function checkRefill() {
    const remaining = tiles.filter(t => !t.removed);
    const pair = findHintPair();
    // If there are few tiles or no available pair, refill
    if (remaining.length < 10 || !pair) {
      refillBoard();
    }
  }

  function refillBoard() {
    window.MAHJONG_SOUND?.shuffle();
    // Keep remaining tiles and add new ones
    const remaining = tiles.filter(t => !t.removed);
    const layout = buildLayout();
    // Fill empty spaces with new tiles
    const occupied = new Set(remaining.map(t => `${t.r},${t.c},${t.z}`));
    const freePositions = layout.filter(p => !occupied.has(`${p.r},${p.c},${p.z}`));

    const newPairs = Math.floor(freePositions.length / 2);
    const newDeck = [];
    for (let i = 0; i < newPairs; i++) {
      const type = tileTypes[Math.floor(Math.random() * tileTypes.length)];
      newDeck.push(type, type);
    }
    shuffle(newDeck);

    let nextId = Math.max(...tiles.map(t => t.id)) + 1;
    for (let i = 0; i < Math.min(newDeck.length, freePositions.length); i++) {
      const pos = freePositions[i];
      tiles.push({
        id: nextId++,
        type: newDeck[i],
        r: pos.r,
        c: pos.c,
        z: pos.z,
        removed: false,
        el: null
      });
    }

    renderBoard();
    updateStats();
    setMessage("+ New tiles! Keep going fast!");
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
    if (scoreEl) scoreEl.textContent = score;
    if (pairsEl) pairsEl.textContent = pairs;
  }

  function setMessage(msg) {
    if (messageEl) messageEl.textContent = msg;
  }

  function endGame() {
    gameOver = true;
    clearInterval(timer);
    if (score > bestScore) {
      bestScore = score;
      try { localStorage.setItem("mahjong_blitz_best", String(bestScore)); } catch (e) {}
      if (bestEl) bestEl.textContent = bestScore;
      setMessage(`Time's up! NEW RECORD: ${score} points (${pairs} pairs)! 🎉`);
    } else {
      setMessage(`Time's up! ${score} points (${pairs} pairs). Try to beat your record of ${bestScore}!`);
    }
    window.MAHJONG_SOUND?.win();
  }

  function doHint() {
    if (gameOver) return;
    const pair = findHintPair();
    if (!pair) {
      setMessage("No hint — wait for new tiles!");
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
    }, 1200);
  }

  newGameBtn?.addEventListener("click", startGame);
  hintBtn?.addEventListener("click", doHint);

  startGame();
})();
