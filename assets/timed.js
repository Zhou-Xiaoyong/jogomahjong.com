/*
 * Mahjong Cronometrado — Solitário contra o tempo.
 * Limpe o tabuleiro antes que o cronômetro zere. Peças tradicionais
 * chinesas com anotações em português do Brasil.
 * Dependência: /assets/tiles-data.js (window.MAHJONG_TILES)
 */
(function () {
  const board = document.querySelector("#mahjong-board");
  if (!board) return;

  const movesEl = document.querySelector("#moves");
  const pairsEl = document.querySelector("#pairs");
  const timeEl = document.querySelector("#time");
  const messageEl = document.querySelector("#game-message");
  const bannerEl = document.querySelector("#countdown-banner");
  const cdTimeEl = document.querySelector("#cd-time");
  const newGameBtn = document.querySelector("#new-game");
  const hintBtn = document.querySelector("#hint");
  const shuffleBtn = document.querySelector("#shuffle");

  const tileW = 108;
  const tileH = 147;
  const gapX = 12;
  const gapY = 10;
  const offsetX = 30;
  const offsetY = 40;
  const layerShift = 12;
  const rowFactor = 0.46;

  const T = window.MAHJONG_TILES;
  const tileTypes = T.core;

  // Tempo total em segundos (5 minutos).
  const TOTAL_TIME = 300;

  // Layout um pouco menor que o clássico para caber no tempo.
  const layout = [
    ...rect(4, 0, 4, 1, 0),
    ...rect(2, 1, 8, 1, 0),
    ...rect(0, 2, 12, 4, 0),
    ...rect(2, 6, 8, 1, 0),
    ...rect(4, 7, 4, 1, 0),
    ...rect(3, 2, 6, 1, 1),
    ...rect(2, 3, 8, 2, 1),
    ...rect(3, 5, 6, 1, 1),
    ...rect(4, 3, 4, 2, 2),
    ...rect(5, 3, 2, 2, 3)
  ];

  let tiles = [];
  let selected = null;
  let moves = 0;
  let removedPairs = 0;
  let timeLeft = TOTAL_TIME;
  let timer = null;
  let gameOver = false;

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
    timeLeft = TOTAL_TIME;
    gameOver = false;
    if (bannerEl) bannerEl.classList.remove("urgent", "over");
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
    setMessage("Corra contra o tempo! Combine peças iguais e livres antes que o relógio zere.");
    timer = setInterval(tick, 1000);
  }

  function tick() {
    timeLeft--;
    if (timeLeft <= 0) {
      timeLeft = 0;
      endGame(false);
    }
    updateStats();
  }

  function endGame(won) {
    clearInterval(timer);
    gameOver = true;
    if (bannerEl) {
      bannerEl.classList.add("over");
      bannerEl.classList.remove("urgent");
    }
    if (won) {
      window.MAHJONG_SOUND?.win();
      setMessage(` Vitória! Você limpou o tabuleiro com ${timeLeft}s sobrando. Mandou bem!`);
    } else {
      window.MAHJONG_SOUND?.error();
      setMessage(`Tempo esgotado! Você removeu ${removedPairs} de ${Math.floor(layout.length / 2)} pares. Tente de novo!`);
      document.querySelectorAll(".tile").forEach(el => { el.disabled = true; });
    }
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
        button.disabled = !isFree(tile) || gameOver;
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
    if (gameOver) return;
    const tile = tiles.find(item => item.uid === uid);
    if (!tile || tile.removed || !isFree(tile)) return;

    clearHints();

    if (!selected) {
      selected = tile;
      markSelected();
      window.MAHJONG_SOUND?.select();
      setMessage("Rápido! Encontre a peça igual que também esteja livre.");
      return;
    }

    if (selected.uid === tile.uid) {
      selected = null;
      markSelected();
      return;
    }

    moves++;
    if (matches(selected.type, tile.type)) {
      timeLeft = Math.min(TOTAL_TIME, timeLeft + 2);
      const firstUid = selected.uid;
      const secondUid = tile.uid;
      selected.removed = true;
      tile.removed = true;
      removedPairs++;
      selected = null;
      window.MAHJONG_SOUND?.match();

      const firstEl = document.querySelector(`.tile[data-uid="${firstUid}"]`);
      const secondEl = document.querySelector(`.tile[data-uid="${secondUid}"]`);
      [firstEl, secondEl].forEach(el => {
        if (el) el.classList.add("removing");
      });

      setTimeout(() => {
        render();
        updateStats();
        if (tiles.every(item => item.removed)) {
          endGame(true);
        } else {
          setMessage("Par removido! +2 segundos. Continue rápido!");
        }
      }, 320);
    } else {
      timeLeft = Math.max(0, timeLeft - 1);
      window.MAHJONG_SOUND?.error();
      const el = document.querySelector(`.tile[data-uid="${tile.uid}"]`);
      if (el) {
        el.classList.add("shake");
        setTimeout(() => el.classList.remove("shake"), 350);
      }
      selected = tile;
      render();
      markSelected();
      updateStats();
      setMessage("Peças não combinam. -1 segundo. Tente outra!");
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
    if (gameOver) return;
    clearHints();
    timeLeft = Math.max(0, timeLeft - 3);
    updateStats();
    const pair = findHintPair();
    if (!pair) {
      setMessage("Não há pares livres. Use embaralhar para continuar (-3s pela dica).");
      return;
    }
    window.MAHJONG_SOUND?.hint();
    pair.forEach(tile => {
      const el = document.querySelector(`.tile[data-uid="${tile.uid}"]`);
      if (el) el.classList.add("hint");
    });
    setMessage("Dica usada: -3 segundos. Combine as peças destacadas.");
  }

  function shuffleRemaining() {
    if (gameOver) return;
    window.MAHJONG_SOUND?.shuffle();
    const active = tiles.filter(tile => !tile.removed);
    const types = shuffle(active.map(tile => tile.type));
    active.forEach((tile, index) => { tile.type = types[index]; });
    selected = null;
    timeLeft = Math.max(0, timeLeft - 5);
    render();
    updateStats();
    setMessage("Peças embaralhadas: -5 segundos. Mãos à obra!");
  }

  function updateStats() {
    movesEl.textContent = moves;
    pairsEl.textContent = `${removedPairs}/${Math.floor(layout.length / 2)}`;
    const minutes = String(Math.floor(timeLeft / 60)).padStart(2, "0");
    const seconds = String(timeLeft % 60).padStart(2, "0");
    timeEl.textContent = `${minutes}:${seconds}`;
    if (cdTimeEl) cdTimeEl.textContent = `${minutes}:${seconds}`;
    if (bannerEl) {
      if (timeLeft <= 30 && timeLeft > 0) bannerEl.classList.add("urgent");
      else if (timeLeft > 0) bannerEl.classList.remove("urgent");
    }
  }

  function setMessage(text) {
    messageEl.textContent = text;
  }

  newGameBtn?.addEventListener("click", startGame);
  hintBtn?.addEventListener("click", showHint);
  shuffleBtn?.addEventListener("click", shuffleRemaining);

  startGame();
})();
