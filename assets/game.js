(function () {
  const board = document.querySelector("#mahjong-board");
  if (!board) return;

  const movesEl = document.querySelector("#moves");
  const pairsEl = document.querySelector("#pairs");
  const timeEl = document.querySelector("#time");
  const messageEl = document.querySelector("#game-message");
  const newGameBtn = document.querySelector("#new-game");
  const hintBtn = document.querySelector("#hint");
  const shuffleBtn = document.querySelector("#shuffle");

  const tileW = 58;
  const tileH = 74;
  const gapX = 12;
  const gapY = 10;
  const offsetX = 86;
  const offsetY = 34;
  const layerShift = 8;

  const tileTypes = [
    { id: "bambu1", symbol: "一", name: "Bambu" },
    { id: "bambu2", symbol: "二", name: "Bambu" },
    { id: "bambu3", symbol: "三", name: "Bambu" },
    { id: "bambu4", symbol: "四", name: "Bambu" },
    { id: "circulo1", symbol: "●", name: "Círculo" },
    { id: "circulo2", symbol: "◉", name: "Círculo" },
    { id: "circulo3", symbol: "◎", name: "Círculo" },
    { id: "dragao", symbol: "龍", name: "Dragão" },
    { id: "vento", symbol: "風", name: "Vento" },
    { id: "flor", symbol: "✿", name: "Flor" },
    { id: "sol", symbol: "☀", name: "Sol" },
    { id: "lua", symbol: "☾", name: "Lua" },
    { id: "estrela", symbol: "★", name: "Estrela" },
    { id: "chuva", symbol: "☂", name: "Chuva" },
    { id: "folha", symbol: "♣", name: "Folha" },
    { id: "mar", symbol: "≈", name: "Mar" },
    { id: "montanha", symbol: "山", name: "Monte" },
    { id: "rio", symbol: "川", name: "Rio" }
  ];

  const layout = [
    // Camada base: formato inspirado na clássica "tartaruga", mas otimizado para navegador.
    ...rect(4, 0, 4, 1, 0),
    ...rect(2, 1, 8, 1, 0),
    ...rect(0, 2, 12, 4, 0),
    ...rect(2, 6, 8, 1, 0),
    ...rect(4, 7, 4, 1, 0),
    // Camada intermediária.
    ...rect(3, 2, 6, 1, 1),
    ...rect(2, 3, 8, 2, 1),
    ...rect(3, 5, 6, 1, 1),
    // Topo.
    ...rect(4, 3, 4, 2, 2),
    ...rect(5, 3, 2, 2, 3)
  ];

  let tiles = [];
  let selected = null;
  let moves = 0;
  let removedPairs = 0;
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
    setMessage("Escolha duas peças livres com o mesmo símbolo para limpar o tabuleiro.");
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
        button.style.left = `${offsetX + tile.x * (tileW + gapX) + tile.z * layerShift}px`;
        button.style.top = `${offsetY + tile.y * (tileH * 0.46 + gapY) - tile.z * layerShift}px`;
        button.style.zIndex = `${tile.z * 100 + tile.y * 10 + tile.x}`;
        button.disabled = !isFree(tile);
        button.innerHTML = `<span><span class="tile-symbol">${tile.type.symbol}</span><span class="tile-name">${tile.type.name}</span></span>`;
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
      setMessage("Boa escolha. Agora encontre a peça igual que também esteja livre.");
      return;
    }

    if (selected.uid === tile.uid) {
      selected = null;
      markSelected();
      setMessage("Seleção removida. Continue com calma.");
      return;
    }

    moves++;
    if (selected.type.id === tile.type.id) {
      selected.removed = true;
      tile.removed = true;
      removedPairs++;
      selected = null;
      render();
      updateStats();
      if (tiles.every(item => item.removed)) {
        setMessage("Parabéns! Você limpou o tabuleiro. Que tal tentar vencer com menos movimentos?");
        clearInterval(timer);
      } else {
        const pair = findHintPair();
        setMessage(pair ? "Par removido. O tabuleiro abriu novas possibilidades." : "Sem pares livres agora. Use embaralhar para continuar.");
      }
    } else {
      selected = tile;
      render();
      markSelected();
      updateStats();
      setMessage("Essas peças não combinam. A nova peça ficou selecionada.");
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
        if (free[i].type.id === free[j].type.id) {
          return [free[i], free[j]];
        }
      }
    }
    return null;
  }

  function showHint() {
    clearHints();
    const pair = findHintPair();
    if (!pair) {
      setMessage("Não há pares livres neste momento. Embaralhe as peças restantes para continuar.");
      return;
    }
    pair.forEach(tile => {
      const el = document.querySelector(`.tile[data-uid="${tile.uid}"]`);
      if (el) el.classList.add("hint");
    });
    setMessage("Dica: tente combinar as duas peças destacadas.");
  }

  function shuffleRemaining() {
    const active = tiles.filter(tile => !tile.removed);
    const types = shuffle(active.map(tile => tile.type));
    active.forEach((tile, index) => {
      tile.type = types[index];
    });
    selected = null;
    render();
    updateStats();
    setMessage("Peças restantes embaralhadas. Use essa ajuda quando o tabuleiro travar.");
  }

  function updateStats() {
    movesEl.textContent = moves;
    pairsEl.textContent = `${removedPairs}/${Math.floor(layout.length / 2)}`;
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
