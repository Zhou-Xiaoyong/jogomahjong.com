/*
 * Mahjong Relaxante — modo zen do Solitário.
 * Sem pressão de tempo, dicas ilimitadas e reembaralhamento automático
 * quando não há mais movimentos. Peças tradicionais chinesas com
 * anotações em português do Brasil.
 * Dependência: /assets/tiles-data.js (window.MAHJONG_TILES)
 */
(function () {
  const board = document.querySelector("#mahjong-board");
  if (!board) return;

  const movesEl = document.querySelector("#moves");
  const pairsEl = document.querySelector("#pairs");
  const timeEl = document.querySelector("#time");
  const messageEl = document.querySelector("#game-message");
  const hintsEl = document.querySelector("#hints-used");
  const newGameBtn = document.querySelector("#new-game");
  const hintBtn = document.querySelector("#hint");
  const shuffleBtn = document.querySelector("#shuffle");

  const tileW = 68;
  const tileH = 92;
  const gapX = 10;
  const gapY = 8;
  const offsetX = 24;
  const offsetY = 30;
  const layerShift = 8;
  const rowFactor = 0.46;

  const T = window.MAHJONG_TILES;
  const tileTypes = T.core;

  // Layout mais plano e gentil: duas camadas, sem ápice alto.
  const layout = [
    ...rect(1, 0, 10, 1, 0),
    ...rect(0, 1, 12, 5, 0),
    ...rect(1, 6, 10, 1, 0),
    ...rect(2, 2, 8, 3, 1),
    ...rect(4, 3, 4, 1, 2)
  ];

  let tiles = [];
  let selected = null;
  let moves = 0;
  let removedPairs = 0;
  let hintsUsed = 0;
  let startedAt = null;
  let timer = null;

  function rect(startX, startY, cols, rows, z) {
    const cells = [];
    for (let y = startY; y < startY + rows; y++) {
      for (let x = startX; x < startX + cols; x++) {
        cells.push({ x, y, z });
      }
    }
    return cells;
  }

  function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
  }

  function matches(a, b) {
    if (a.id === b.id) return true;
    if (a.suit === "flor" && b.suit === "flor") return true;
    if (a.suit === "estação" && b.suit === "estação") return true;
    return false;
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
    clearInterval(timer);
    board.innerHTML = "";
    selected = null;
    moves = 0;
    removedPairs = 0;
    hintsUsed = 0;
    startedAt = Date.now();
    const deck = buildDeck(layout.length);

    tiles = layout.map((cell, index) => ({
      uid: index,
      x: cell.x,
      y: cell.y,
      z: cell.z,
      removed: false,
      type: deck[index]
    }));

    render();
    updateStats();
    setMessage("Modo relaxante: sem pressa, sem erro fatal. Use quantas dicas quiser e respire fundo.");
    timer = setInterval(updateTime, 1000);
  }

  function render() {
    board.innerHTML = "";
    tiles
      .filter(tile => !tile.removed)
      .sort((a, b) => a.z - b.z || a.y - b.y || a.x - b.x)
      .forEach(tile => {
        const button = document.createElement("button");
        button.className = "tile";
        button.type = "button";
        button.dataset.uid = tile.uid;
        button.dataset.suit = tile.type.suit;
        button.style.left = `${offsetX + tile.x * (tileW + gapX) + tile.z * layerShift}px`;
        button.style.top = `${offsetY + tile.y * (tileH * rowFactor + gapY) - tile.z * layerShift}px`;
        button.style.zIndex = `${tile.z * 100 + tile.y * 10 + tile.x}`;
        button.disabled = !isFree(tile);
        button.setAttribute("aria-label", `${tile.type.name} (${tile.type.cn})`);
        button.innerHTML =
          `<span class="tile-symbol">${tile.type.symbol}</span>` +
          `<span class="tile-name">${tile.type.name}</span>`;
        button.addEventListener("click", () => selectTile(tile.uid));
        board.appendChild(button);
      });
  }

  function overlaps(a, b) {
    return Math.abs(a.x - b.x) < 1 && Math.abs(a.y - b.y) < 1;
  }

  function hasTileAt(x, y, z) {
    return tiles.some(tile => !tile.removed && tile.z === z && tile.x === x && tile.y === y);
  }

  function isCovered(tile) {
    return tiles.some(other => !other.removed && other.z > tile.z && overlaps(tile, other));
  }

  function isFree(tile) {
    if (tile.removed || isCovered(tile)) return false;
    const leftBlocked = hasTileAt(tile.x - 1, tile.y, tile.z);
    const rightBlocked = hasTileAt(tile.x + 1, tile.y, tile.z);
    return !leftBlocked || !rightBlocked;
  }

  function selectTile(uid) {
    const tile = tiles.find(item => item.uid === uid);
    if (!tile || tile.removed || !isFree(tile)) return;

    clearHints();

    if (!selected) {
      selected = tile;
      markSelected();
      setMessage("Sem pressa. Encontre a peça igual quando quiser.");
      return;
    }

    if (selected.uid === tile.uid) {
      selected = null;
      markSelected();
      return;
    }

    moves++;
    if (matches(selected.type, tile.type)) {
      selected.removed = true;
      tile.removed = true;
      removedPairs++;
      selected = null;
      render();
      updateStats();
      if (tiles.every(item => item.removed)) {
        setMessage("Pronto! Tabuleiro limpo no seu ritmo. Que tal uma partida relaxante de Pirâmide agora?");
        clearInterval(timer);
      } else {
        const pair = findHintPair();
        if (!pair) {
          setMessage("Sem pares livres. Vou embaralhar para você continuar relaxando...");
          setTimeout(autoShuffle, 1200);
        } else {
          setMessage("Par removido. Continue no seu tempo.");
        }
      }
    } else {
      selected = tile;
      render();
      markSelected();
      updateStats();
      setMessage("Não combinam, mas sem problema — no modo relaxante não há penalidade.");
    }
  }

  function markSelected() {
    document.querySelectorAll(".tile").forEach(el => el.classList.remove("selected"));
    if (!selected) return;
    const el = document.querySelector(`.tile[data-uid="${selected.uid}"]`);
    if (el) el.classList.add("selected");
  }

  function clearHints() {
    document.querySelectorAll(".tile").forEach(el => el.classList.remove("hint"));
  }

  function findHintPair() {
    const free = tiles.filter(tile => !tile.removed && isFree(tile));
    for (let i = 0; i < free.length; i++) {
      for (let j = i + 1; j < free.length; j++) {
        if (matches(free[i].type, free[j].type)) {
          return [free[i], free[j]];
        }
      }
    }
    return null;
  }

  function showHint() {
    clearHints();
    hintsUsed++;
    updateStats();
    const pair = findHintPair();
    if (!pair) {
      setMessage("Não há pares livres agora. Embaralhando automaticamente...");
      setTimeout(autoShuffle, 800);
      return;
    }
    pair.forEach(tile => {
      const el = document.querySelector(`.tile[data-uid="${tile.uid}"]`);
      if (el) el.classList.add("hint");
    });
    setMessage("Dica grátis: combine as duas peças destacadas. Sem limite de uso.");
  }

  function shuffleRemaining() {
    const active = tiles.filter(tile => !tile.removed);
    const types = shuffle(active.map(tile => tile.type));
    active.forEach((tile, index) => { tile.type = types[index]; });
    selected = null;
    render();
    updateStats();
    setMessage("Peças embaralhadas. Respire e continue.");
  }

  function autoShuffle() {
    shuffleRemaining();
  }

  function updateStats() {
    movesEl.textContent = moves;
    pairsEl.textContent = `${removedPairs}/${Math.floor(layout.length / 2)}`;
    if (hintsEl) hintsEl.textContent = hintsUsed;
    updateTime();
  }

  function updateTime() {
    if (!startedAt) {
      timeEl.textContent = "00:00";
      return;
    }
    const total = Math.floor((Date.now() - startedAt) / 1000);
    const minutes = String(Math.floor(total / 60)).padStart(2, "0");
    const seconds = String(total % 60).padStart(2, "0");
    timeEl.textContent = `${minutes}:${seconds}`;
  }

  function setMessage(text) {
    messageEl.textContent = text;
  }

  newGameBtn?.addEventListener("click", startGame);
  hintBtn?.addEventListener("click", showHint);
  shuffleBtn?.addEventListener("click", shuffleRemaining);

  startGame();
})();
