/*
 * Mahjong Connect — connect two matching tiles with a line of at most
 * two corners. Traditional Chinese tiles with annotations in English.
 * Dependency: /assets/tiles-data.js (window.MAHJONG_TILES)
 */
(function () {
  const board = document.querySelector("#connect-board");
  if (!board) return;

  const pairsEl = document.querySelector("#pairs");
  const timeEl = document.querySelector("#time");
  const messageEl = document.querySelector("#game-message");
  const newGameBtn = document.querySelector("#new-game");
  const hintBtn = document.querySelector("#hint");

  const ROWS = 8;
  const COLS = 10;
  const tileW = 72;
  const tileH = 98;
  const gap = 6;

  const T = window.MAHJONG_TILES;
  const tileTypes = [
    T.winds[0], T.winds[1], T.winds[2], T.winds[3],
    T.dragons[0], T.dragons[1], T.dragons[2],
    T.characters[0], T.characters[4], T.characters[8],
    T.bamboos[0], T.bamboos[4], T.bamboos[8],
    T.circles[0], T.circles[4], T.circles[8]
  ];

  let grid = [];
  let selected = null;
  let removedPairs = 0;
  let startedAt = null;
  let timer = null;
  let totalPairs = 0;
  let lineEl = null;

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
    if (lineEl) { lineEl.remove(); lineEl = null; }
    board.innerHTML = "";
    selected = null;
    removedPairs = 0;
    startedAt = Date.now();
    const deck = buildDeck();

    grid = [];
    for (let r = 0; r < ROWS; r++) {
      const row = [];
      for (let c = 0; c < COLS; c++) {
        row.push({
          r, c,
          type: deck[r * COLS + c],
          removed: false
        });
      }
      grid.push(row);
    }

    renderGrid();
    updateStats();
    setMessage("Click two matching tiles that can be connected by a line with at most 2 corners.");
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
        btn.className = "tile connect-tile";
        btn.type = "button";
        btn.dataset.r = r;
        btn.dataset.c = c;
        btn.style.position = "relative";
        btn.style.left = "auto";
        btn.style.top = "auto";
        if (cell.removed) {
          btn.style.visibility = "hidden";
          btn.disabled = true;
        } else {
          btn.dataset.suit = cell.type.suit;
          btn.dataset.id = cell.type.id;
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
    clearLine();

    if (!selected) {
      selected = cell;
      const el = getTileEl(r, c);
      if (el) el.classList.add("selected");
      window.MAHJONG_SOUND?.select();
      setMessage("Now click the matching tile that can be connected.");
      return;
    }

    if (selected.r === r && selected.c === c) {
      selected = null;
      setMessage("Selection cleared. Choose another tile.");
      return;
    }

    if (selected.type.id !== cell.type.id) {
      window.MAHJONG_SOUND?.error();
      const el = getTileEl(r, c);
      if (el) {
        el.classList.add("shake");
        setTimeout(() => el.classList.remove("shake"), 350);
      }
      selected = cell;
      const el2 = getTileEl(r, c);
      if (el2) el2.classList.add("selected");
      setMessage("These tiles don't match. Try another.");
      return;
    }

    const path = findPath(selected.r, selected.c, r, c);
    if (!path) {
      window.MAHJONG_SOUND?.error();
      const el = getTileEl(r, c);
      if (el) {
        el.classList.add("shake");
        setTimeout(() => el.classList.remove("shake"), 350);
      }
      selected = cell;
      const el2 = getTileEl(r, c);
      if (el2) el2.classList.add("selected");
      setMessage("Cannot connect these tiles with at most 2 corners. Try another.");
      return;
    }

    // Pair connected!
    drawLine(path);
    window.MAHJONG_SOUND?.match();
    const sr = selected.r, sc = selected.c;
    selected.removed = true;
    cell.removed = true;
    removedPairs++;
    selected = null;

    const elA = getTileEl(sr, sc);
    const elB = getTileEl(r, c);
    [elA, elB].forEach(el => {
      if (el) el.classList.add("removing");
    });

    setTimeout(() => {
      clearLine();
      renderGrid();
      updateStats();
      if (removedPairs >= totalPairs) {
        window.MAHJONG_SOUND?.win();
        setMessage("Congratulations! You cleared the board!");
        clearInterval(timer);
      } else {
        const pair = findHintPair();
        if (pair) {
          setMessage("Pair connected! Continue.");
        } else {
          setMessage("No connectable pairs. Shuffling remaining tiles...");
          setTimeout(shuffleRemaining, 1000);
        }
      }
    }, 320);
  }

  function shuffleRemaining() {
    window.MAHJONG_SOUND?.shuffle();
    const remaining = [];
    const positions = [];
    for (let r = 0; r < ROWS; r++) {
      for (let c = 0; c < COLS; c++) {
        if (!grid[r][c].removed) {
          remaining.push(grid[r][c].type);
          positions.push({ r, c });
        }
      }
    }
    shuffle(remaining);
    positions.forEach((pos, i) => {
      grid[pos.r][pos.c].type = remaining[i];
    });
    selected = null;
    renderGrid();
    const pair = findHintPair();
    if (!pair) {
      setTimeout(shuffleRemaining, 800);
    } else {
      setMessage("Tiles shuffled! Keep connecting.");
    }
  }

  function clearSelection() {
    document.querySelectorAll(".connect-tile.selected").forEach(el => el.classList.remove("selected"));
  }

  function clearLine() {
    if (lineEl) { lineEl.remove(); lineEl = null; }
  }

  function drawLine(path) {
    clearLine();
    if (path.length < 2) return;
    const gridEl = document.querySelector(".connect-grid");
    if (!gridEl) return;
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

  // Path finding with at most 2 turns.
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
      if (cur.r === r2 && cur.c === c2) {
        return cur.path;
      }
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
        queue.push({
          r: nr, c: nc, dir: d, turns: newTurns,
          path: [...cur.path, { r: nr, c: nc }]
        });
      }
    }
    return null;
  }

  // A cell is valid for the path if it is empty (removed) or if it is the destination.
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
    clearSelection();
    clearLine();
    const pair = findHintPair();
    if (!pair) {
      setMessage("No connectable pairs. Shuffling soon...");
      return;
    }
    window.MAHJONG_SOUND?.hint();
    const el1 = getTileEl(pair[0].r, pair[0].c);
    const el2 = getTileEl(pair[1].r, pair[1].c);
    if (el1) el1.classList.add("hint");
    if (el2) el2.classList.add("hint");
    setMessage("Hint: these two tiles can be connected.");
  }

  function updateStats() {
    pairsEl.textContent = `${removedPairs}/${totalPairs}`;
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
