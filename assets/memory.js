/*
 * Memória Mahjong — jogo da memória com peças tradicionais chinesas.
 * Anotações em português do Brasil no verso de cada peça.
 * Dependência: /assets/tiles-data.js (window.MAHJONG_TILES)
 */
(function () {
  const board = document.querySelector("#memory-board");
  if (!board) return;

  const movesEl = document.querySelector("#moves");
  const pairsEl = document.querySelector("#pairs");
  const timeEl = document.querySelector("#time");
  const messageEl = document.querySelector("#game-message");
  const newGameBtn = document.querySelector("#new-game");

  const PAIR_COUNT = 18; // 36 cartas = grade 6x6

  const T = window.MAHJONG_TILES;
  // Seleção variada: ventos, dragões, números representativos, flores e estações.
  const tileTypes = [
    T.winds[0], T.winds[1], T.winds[2], T.winds[3],
    T.dragons[0], T.dragons[1], T.dragons[2],
    T.characters[0], T.characters[4], T.characters[8],
    T.bamboos[0], T.bamboos[4], T.bamboos[8],
    T.circles[0], T.circles[4], T.circles[8],
    T.flowers[0], T.flowers[3],
    T.seasons[0]
  ];

  let cards = [];
  let flippedCards = [];
  let matchedPairs = 0;
  let moves = 0;
  let startedAt = null;
  let timer = null;
  let isLocked = false;

  function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
  }

  function startGame() {
    clearInterval(timer);
    board.innerHTML = "";
    flippedCards = [];
    matchedPairs = 0;
    moves = 0;
    isLocked = false;
    startedAt = Date.now();

    const deck = [];
    for (let i = 0; i < PAIR_COUNT; i++) {
      const type = tileTypes[i % tileTypes.length];
      deck.push({ ...type, uid: i * 2 }, { ...type, uid: i * 2 + 1 });
    }
    shuffle(deck);

    cards = deck.map((type, index) => ({
      index,
      type,
      flipped: false,
      matched: false
    }));

    renderBoard();
    updateStats();
    setMessage("Vire duas peças para encontrar os pares. Memorize o símbolo chinês e o nome em português. Boa sorte!");
    timer = setInterval(updateTime, 1000);
  }

  function renderBoard() {
    board.innerHTML = "";
    cards.forEach(card => {
      const btn = document.createElement("button");
      btn.className = "memory-card";
      btn.type = "button";
      btn.dataset.index = card.index;
      if (card.flipped || card.matched) {
        btn.classList.add(card.matched ? "matched" : "flipped");
      }

      const inner = document.createElement("div");
      inner.className = "memory-card-inner";

      const front = document.createElement("div");
      front.className = "memory-card-front";

      const back = document.createElement("div");
      back.className = "memory-card-back";
      back.dataset.suit = card.type.suit;
      back.setAttribute("aria-label", `${card.type.name} (${card.type.cn})`);
      back.innerHTML =
        `<span class="tile-symbol">${card.type.symbol}</span>` +
        `<span class="tile-name">${card.type.name}</span>`;

      inner.appendChild(front);
      inner.appendChild(back);
      btn.appendChild(inner);

      btn.addEventListener("click", () => flipCard(card.index));
      board.appendChild(btn);
    });
  }

  function flipCard(index) {
    const card = cards[index];
    if (isLocked || card.flipped || card.matched) return;

    card.flipped = true;
    flippedCards.push(card);
    window.MAHJONG_SOUND?.select();
    renderBoard();

    if (flippedCards.length === 2) {
      moves++;
      updateStats();
      isLocked = true;
      const [first, second] = flippedCards;

      if (first.type.id === second.type.id) {
        first.matched = true;
        second.matched = true;
        matchedPairs++;
        flippedCards = [];
        isLocked = false;
        window.MAHJONG_SOUND?.match();

        setTimeout(() => {
          renderBoard();
          updateStats();
          if (matchedPairs >= PAIR_COUNT) {
            window.MAHJONG_SOUND?.win();
            setMessage(`Parabéns! Você encontrou todos os pares em ${moves} movimentos!`);
            clearInterval(timer);
          } else {
            setMessage("Par encontrado! Continue.");
          }
        }, 300);
      } else {
        window.MAHJONG_SOUND?.error();
        setMessage("Não é par. Memorize as posições e os símbolos!");
        setTimeout(() => {
          first.flipped = false;
          second.flipped = false;
          flippedCards = [];
          isLocked = false;
          renderBoard();
        }, 1000);
      }
    } else {
      setMessage("Escolha outra peça para tentar formar um par.");
    }
  }

  function updateStats() {
    movesEl.textContent = moves;
    pairsEl.textContent = `${matchedPairs}/${PAIR_COUNT}`;
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

  startGame();
})();
