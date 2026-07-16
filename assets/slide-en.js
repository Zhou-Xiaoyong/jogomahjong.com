/*
 * Mahjong Slide — slide left or right to match identical tiles.
 * New game inspired by sliding/matching puzzles.
 * Dependency: /assets/tiles-data.js (window.MAHJONG_TILES)
 */
(function () {
  const trackEl = document.querySelector("#slide-track");
  if (!trackEl) return;

  const scoreEl = document.querySelector("#score");
  const pairsEl = document.querySelector("#pairs");
  const levelEl = document.querySelector("#level");
  const bestEl = document.querySelector("#best");
  const messageEl = document.querySelector("#game-message");
  const newGameBtn = document.querySelector("#new-game");
  const leftBtn = document.querySelector("#slide-left");
  const rightBtn = document.querySelector("#slide-right");

  const T = window.MAHJONG_TILES;
  const tileTypes = T.core;

  const MAX_SLOTS = 12;
  const START_TILES = 5;

  let tiles = [];
  let score = 0;
  let pairs = 0;
  let level = 1;
  let gameOver = false;
  let bestScore = 0;
  let animating = false;

  try {
    bestScore = parseInt(localStorage.getItem("mahjong_slide_best") || "0", 10);
  } catch (e) { bestScore = 0; }
  if (bestEl) bestEl.textContent = bestScore;

  function randInt(max) {
    return Math.floor(Math.random() * max);
  }

  function randomTile() {
    // Increase variety according to level
    const maxTypes = Math.min(tileTypes.length, 6 + level * 2);
    return tileTypes[randInt(maxTypes)];
  }

  function startGame() {
    tiles = [];
    score = 0;
    pairs = 0;
    level = 1;
    gameOver = false;
    animating = false;

    // Fill with initial tiles
    for (let i = 0; i < START_TILES; i++) {
      tiles.push({ type: randomTile(), id: i });
    }

    render(true);
    updateStats();
    setMessage("Slide left or right to match identical tiles!");
  }

  function render(immediate) {
    trackEl.innerHTML = "";
    tiles.forEach((tile, index) => {
      const el = document.createElement("div");
      el.className = "tile slide-tile";
      el.dataset.suit = tile.type.suit;
      el.dataset.id = tile.type.id;
      el.dataset.index = index;
      el.style.position = "absolute";
      el.style.left = (index * 80) + "px";
      el.style.transition = immediate ? "none" : "left .25s ease-out";
      el.innerHTML = `
        <div class="tile-face">
          <div class="tile-symbol">${tile.type.symbol}</div>
          <div class="tile-name">${tile.type.name}</div>
        </div>
      `;
      trackEl.appendChild(el);
    });
    trackEl.style.width = (MAX_SLOTS * 80 + 50) + "px";
  }

  function slide(direction) {
    if (gameOver || animating) return;
    animating = true;
    window.MAHJONG_SOUND?.select();

    let moved = false;

    if (direction === "left") {
      // Try to move all tiles to the left
      for (let i = 1; i < tiles.length; i++) {
        if (tiles[i].type.id === tiles[i - 1].type.id) {
          // Combine
          tiles[i - 1] = { ...tiles[i - 1], combining: true };
          tiles[i] = { ...tiles[i], combining: true, toRemove: true };
          score += 10 * level;
          pairs++;
          moved = true;
          window.MAHJONG_SOUND?.match();
        }
      }
      // Remove combined ones and move the rest
      tiles = tiles.filter(t => !t.toRemove);
    } else {
      // Try to move all tiles to the right
      for (let i = tiles.length - 2; i >= 0; i--) {
        if (tiles[i].type.id === tiles[i + 1].type.id) {
          tiles[i + 1] = { ...tiles[i + 1], combining: true };
          tiles[i] = { ...tiles[i], combining: true, toRemove: true };
          score += 10 * level;
          pairs++;
          moved = true;
          window.MAHJONG_SOUND?.match();
        }
      }
      tiles = tiles.filter(t => !t.toRemove);
    }

    // Update level
    const newLevel = Math.floor(pairs / 10) + 1;
    if (newLevel > level) {
      level = newLevel;
      setMessage(`Level ${level}! More tile variety.`);
    }

    // Add new tile (if there is space)
    if (tiles.length < MAX_SLOTS) {
      // Chance of adding a new tile increases with level
      const addChance = 0.6 + level * 0.04;
      if (Math.random() < addChance) {
        if (direction === "left") {
          tiles.unshift({ type: randomTile(), id: Date.now() + Math.random() });
        } else {
          tiles.push({ type: randomTile(), id: Date.now() + Math.random() });
        }
      }
    }

    render(false);
    updateStats();

    setTimeout(() => {
      animating = false;
      checkGameOver();
    }, 300);
  }

  function hasAnyMatch() {
    for (let i = 0; i < tiles.length - 1; i++) {
      if (tiles[i].type.id === tiles[i + 1].type.id) return true;
    }
    return false;
  }

  function checkGameOver() {
    if (tiles.length >= MAX_SLOTS && !hasAnyMatch()) {
      gameOver = true;
      if (score > bestScore) {
        bestScore = score;
        try { localStorage.setItem("mahjong_slide_best", String(bestScore)); } catch (e) {}
        if (bestEl) bestEl.textContent = bestScore;
        setMessage(`Game over! NEW RECORD: ${score} points (${pairs} pairs, level ${level})! 🎉`);
      } else {
        setMessage(`Game over! ${score} points (${pairs} pairs, level ${level}). Your record: ${bestScore}.`);
      }
      window.MAHJONG_SOUND?.win();
    }
  }

  function updateStats() {
    if (scoreEl) scoreEl.textContent = score;
    if (pairsEl) pairsEl.textContent = pairs;
    if (levelEl) levelEl.textContent = level;
  }

  function setMessage(msg) {
    if (messageEl) messageEl.textContent = msg;
  }

  leftBtn?.addEventListener("click", () => slide("left"));
  rightBtn?.addEventListener("click", () => slide("right"));
  newGameBtn?.addEventListener("click", startGame);

  // Keyboard support
  document.addEventListener("keydown", (e) => {
    if (e.key === "ArrowLeft") {
      e.preventDefault();
      slide("left");
    } else if (e.key === "ArrowRight") {
      e.preventDefault();
      slide("right");
    }
  });

  startGame();
})();
