/*
 * Mahjong Cadeia — Connect com sistema de combo (cadeia).
 * Conecte pares em sequência rápida para multiplicar pontos.
 * Peças tradicionais chinesas com anotações em português do Brasil.
 * Dependência: /assets/tiles-data.js (window.MAHJONG_TILES)
 */
(function () {
  const board = document.querySelector("#connect-board");
  if (!board) return;

  const pairsEl = document.querySelector("#pairs");
  const timeEl = document.querySelector("#time");
  const scoreEl = document.querySelector("#score");
  const comboEl = document.querySelector("#combo");
  const messageEl = document.querySelector("#game-message");
  const newGameBtn = document.querySelector("#new-game");
  const hintBtn = document.querySelector("#hint");

  const ROWS = 8;
  const COLS = 10;
  const tileW = 58;
  const tileH = 76;
  const gap = 6;

  // Janela de tempo (em ms) para manter a cadeia viva entre um par e outro.
  const COMBO_WINDOW = 4500;

  const T = window.MAHJONG_TILES;
  const tileTypes = T.all;

  let grid = [];
  let selected = null;
  let removedPairs = 0;
  let totalPairs = 0;
  let score = 0;
  let combo = 0;
  let bestCombo = 0;
  let lastMatchAt = 0;
  let comboTimer = null;
  let startedAt = null;
  let timer = null;

  function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
  }

  function buildDeck() {
    const totalCells = ROWS * COLS;
    const pairsNeeded = totalCells / 2;
    totalPairs = pairsNeeded;
    const deck = [];
    for (let i = 0; i < pairsNeeded; i++) {
      const type = tileTypes[i % tileTypes.length];
      deck.push(type, type);
    }
    return shuffle(deck);
  }

  function startGame() {
    clearInterval(timer);
    clearTimeout(comboTimer);
    board.innerHTML = "";
    selected = null;
    removedPairs = 0;
    score = 0;
    combo = 0;
    bestCombo = 0;
    lastMatchAt = 0;
    startedAt = Date.now();
    const deck = buildDeck();

    grid = [];
    for (let r = 0; r < ROWS; r++) {
      const row = [];
      for (let c = 0; c < COLS; c++) {
        row.push({ r, c, type: deck[r * COLS + c], removed: false });
      }
      grid.push(row);
    }

    renderGrid();
    updateStats();
    setMessage("Conecte pares em sequência rápida para formar uma cadeia. Quanto maior a cadeia, mais pontos!");
    timer = setInterval(updateTime, 1000);
  }

  function renderGrid() {
    board.innerHTML = "";
    const gridEl = document.createElement("div");
    gridEl.className = "connect-grid";
    gridEl.style.gridTemplateColumns = `repeat(${COLS}, ${tileW}px)`;
    gridEl.style.gap = `${gap}px`;

    for (let r = 0; r < ROWS; r++) {
      for (let c = 0; c < COLS; c++) {
        const cell = grid[r][c];
        const btn = document.createElement("button");
        btn.className = "connect-tile";
        btn.type = "button";
        btn.dataset.r = r;
        btn.dataset.c = c;
        btn.style.width = `${tileW}px`;
        btn.style.height = `${tileH}px`;
        if (cell.removed) {
          btn.style.visibility = "hidden";
          btn.disabled = true;
        } else {
          btn.dataset.suit = cell.type.suit;
          btn.setAttribute("aria-label", `${cell.type.name} (${cell.type.cn})`);
          btn.innerHTML =
            `<span class="tile-symbol">${cell.type.symbol}</span>` +
            `<span class="tile-name">${cell.type.name}</span>`;
          btn.addEventListener("click", () => selectTile(r, c));
        }
        gridEl.appendChild(btn);
      }
    }
    board.appendChild(gridEl);
  }

  function getTileEl(r, c) {
    return document.querySelector(`.connect-tile[data-r="${r}"][data-c="${c}"]`);
  }

  function selectTile(r, c) {
    const cell = grid[r][c];
    if (cell.removed) return;
    clearSelection();

    if (!selected) {
      selected = cell;
      const el = getTileEl(r, c);
      if (el) el.classList.add("selected");
      setMessage("Agora clique na peça igual que possa ser conectada.");
      return;
    }

    if (selected.r === r && selected.c === c) {
      selected = null;
      setMessage("Seleção removida. Escolha outra peça.");
      return;
    }

    if (selected.type.id !== cell.type.id) {
      // Erro quebra a cadeia.
      breakCombo();
      selected = cell;
      const el = getTileEl(r, c);
      if (el) el.classList.add("selected");
      setMessage("Peças diferentes — cadeia quebrada! Tente outra.");
      return;
    }

    const path = findPath(selected.r, selected.c, r, c);
    if (!path) {
      breakCombo();
      selected = cell;
      const el = getTileEl(r, c);
      if (el) el.classList.add("selected");
      setMessage("Não dá para conectar com até 2 cantos. Cadeia quebrada!");
      return;
    }

    drawLine(path);
    selected.removed = true;
    cell.removed = true;
    removedPairs++;
    registerMatch();

    setTimeout(() => {
      clearLine();
      renderGrid();
      updateStats();
      if (removedPairs >= totalPairs) {
        setMessage(`Tabuleiro limpo! Pontuação final: ${score} (cadeia máxima: ${bestCombo}).`);
        clearInterval(timer);
        clearTimeout(comboTimer);
      } else {
        const pair = findHintPair();
        if (!pair) {
          setMessage("Sem pares disponíveis. Reiniciando o tabuleiro...");
          setTimeout(startGame, 1500);
        }
      }
    }, 300);
  }

  function registerMatch() {
    const now = Date.now();
    if (lastMatchAt && now - lastMatchAt <= COMBO_WINDOW) {
      combo++;
    } else {
      combo = 1;
    }
    lastMatchAt = now;
    bestCombo = Math.max(bestCombo, combo);
    // Pontos: base 10 multiplicada pelo tamanho da cadeia.
    const gained = 10 * combo;
    score += gained;
    const msg = combo > 1
      ? `Cadeia x${combo}! +${gained} pontos. Continue rápido para aumentar!`
      : `Par conectado! +${gained} pontos.`;
    setMessage(msg);

    clearTimeout(comboTimer);
    comboTimer = setTimeout(() => {
      if (combo > 0) {
        combo = 0;
        updateStats();
        setMessage("Cadeia expirou. Conecte um par para começar outra.");
      }
    }, COMBO_WINDOW);
  }

  function breakCombo() {
    if (combo > 0) {
      combo = 0;
      clearTimeout(comboTimer);
      updateStats();
    }
  }

  function clearSelection() {
    document.querySelectorAll(".connect-tile.selected").forEach(el => el.classList.remove("selected"));
  }

  function clearLine() {
    document.querySelectorAll(".connect-line").forEach(el => el.remove());
  }

  function drawLine(path) {
    clearLine();
    if (path.length < 2) return;
    const boardRect = board.getBoundingClientRect();
    for (let i = 0; i < path.length - 1; i++) {
      const a = path[i];
      const b = path[i + 1];
      const elA = getTileEl(a.r, a.c);
      const elB = getTileEl(b.r, b.c);
      if (!elA || !elB) continue;
      const rectA = elA.getBoundingClientRect();
      const rectB = elB.getBoundingClientRect();
      const x1 = rectA.left + rectA.width / 2 - boardRect.left;
      const y1 = rectA.top + rectA.height / 2 - boardRect.top;
      const x2 = rectB.left + rectB.width / 2 - boardRect.left;
      const y2 = rectB.top + rectB.height / 2 - boardRect.top;
      const line = document.createElement("div");
      line.className = "connect-line show";
      const dx = x2 - x1;
      const dy = y2 - y1;
      const length = Math.sqrt(dx * dx + dy * dy);
      const angle = Math.atan2(dy, dx) * 180 / Math.PI;
      line.style.width = `${length}px`;
      line.style.height = "3px";
      line.style.left = `${x1}px`;
      line.style.top = `${y1 - 1}px`;
      line.style.transform = `rotate(${angle}deg)`;
      line.style.transformOrigin = "0 50%";
      board.appendChild(line);
    }
  }

  function findPath(r1, c1, r2, c2) {
    if (r1 === r2 && c1 === c2) return null;
    if (grid[r2][c2].removed) return null;

    const directions = [
      { dr: -1, dc: 0 }, { dr: 1, dc: 0 },
      { dr: 0, dc: -1 }, { dr: 0, dc: 1 }
    ];

    const queue = [];
    const visited = new Set();

    for (let d = 0; d < 4; d++) {
      const nr = r1 + directions[d].dr;
      const nc = c1 + directions[d].dc;
      if (isValid(nr, nc, r2, c2)) {
        queue.push({ r: nr, c: nc, dir: d, turns: 0, path: [{ r: r1, c: c1 }, { r: nr, c: nc }] });
        visited.add(`${nr},${nc},${d},0`);
      }
    }

    let head = 0;
    while (head < queue.length) {
      const cur = queue[head++];
      if (cur.r === r2 && cur.c === c2) return cur.path;
      if (cur.turns >= 2) continue;
      for (let d = 0; d < 4; d++) {
        const nr = cur.r + directions[d].dr;
        const nc = cur.c + directions[d].dc;
        const newTurns = cur.dir === d ? cur.turns : cur.turns + 1;
        if (newTurns > 2) continue;
        const key = `${nr},${nc},${d},${newTurns}`;
        if (visited.has(key)) continue;
        if (!isValid(nr, nc, r2, c2)) continue;
        visited.add(key);
        queue.push({ r: nr, c: nc, dir: d, turns: newTurns, path: [...cur.path, { r: nr, c: nc }] });
      }
    }
    return null;
  }

  function isValid(r, c, destR, destC) {
    if (r < 0 || r >= ROWS || c < 0 || c >= COLS) return false;
    if (r === destR && c === destC) return true;
    if (grid[r][c].removed) return true;
    return false;
  }

  function findHintPair() {
    const remaining = [];
    for (let r = 0; r < ROWS; r++) {
      for (let c = 0; c < COLS; c++) {
        if (!grid[r][c].removed) remaining.push(grid[r][c]);
      }
    }
    for (let i = 0; i < remaining.length; i++) {
      for (let j = i + 1; j < remaining.length; j++) {
        if (remaining[i].type.id === remaining[j].type.id) {
          const path = findPath(remaining[i].r, remaining[i].c, remaining[j].r, remaining[j].c);
          if (path) return [remaining[i], remaining[j]];
        }
      }
    }
    return null;
  }

  function showHint() {
    // A dica quebra a cadeia (sem challenge externo).
    breakCombo();
    clearSelection();
    clearLine();
    const pair = findHintPair();
    if (!pair) {
      setMessage("Não há pares conectáveis. Reiniciando...");
      return;
    }
    const el1 = getTileEl(pair[0].r, pair[0].c);
    const el2 = getTileEl(pair[1].r, pair[1].c);
    if (el1) el1.classList.add("selected");
    if (el2) el2.classList.add("selected");
    setMessage("Dica: conecte essas duas peças. (A cadeia foi reiniciada.)");
  }

  function updateStats() {
    pairsEl.textContent = `${removedPairs}/${totalPairs}`;
    if (scoreEl) scoreEl.textContent = score;
    if (comboEl) {
      comboEl.textContent = `Cadeia x${combo}`;
      if (combo >= 3) comboEl.classList.add("hot");
      else comboEl.classList.remove("hot");
    }
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

  startGame();
})();
