/*
 * Mahjong Deslize — arraste para os lados e combine peças iguais.
 * Jogo novo inspirado em puzzles de deslizar/combinar.
 * Dependência: /assets/tiles-data.js (window.MAHJONG_TILES)
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
    // Aumentar variedade conforme o nível
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

    // Preencher com peças iniciais
    for (let i = 0; i < START_TILES; i++) {
      tiles.push({ type: randomTile(), id: i });
    }

    render(true);
    updateStats();
    setMessage("Arraste para os lados e combine peças iguais!");
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
      // Tentar mover todas as peças para a esquerda
      for (let i = 1; i < tiles.length; i++) {
        if (tiles[i].type.id === tiles[i - 1].type.id) {
          // Combinar
          tiles[i - 1] = { ...tiles[i - 1], combining: true };
          tiles[i] = { ...tiles[i], combining: true, toRemove: true };
          score += 10 * level;
          pairs++;
          moved = true;
          window.MAHJONG_SOUND?.match();
        }
      }
      // Remover combinadas e mover restantes
      tiles = tiles.filter(t => !t.toRemove);
    } else {
      // Tentar mover todas as peças para a direita
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

    // Atualizar nível
    const newLevel = Math.floor(pairs / 10) + 1;
    if (newLevel > level) {
      level = newLevel;
      setMessage(`Nível ${level}! Mais variedade de peças.`);
    }

    // Adicionar nova peça (se houver espaço)
    if (tiles.length < MAX_SLOTS) {
      // Chance de adicionar nova peça aumenta com o nível
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
        setMessage(`Fim de jogo! NOVO RECORDE: ${score} pontos (${pairs} pares, nível ${level})! 🎉`);
      } else {
        setMessage(`Fim de jogo! ${score} pontos (${pairs} pares, nível ${level}). Seu recorde: ${bestScore}.`);
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

  // Suporte a teclado
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
