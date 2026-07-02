/*
 * Efeitos sonoros do Mahjong, gerados via Web Audio API.
 * Sem arquivos de áudio externos — sons são sintetizados em tempo real.
 * Uso: window.MAHJONG_SOUND.select(), .match(), .error(), .shuffle(), .win()
 */
(function () {
  let audioCtx = null;
  let enabled = true;

  function getCtx() {
    if (!audioCtx) {
      try {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      } catch (e) {
        enabled = false;
      }
    }
    if (audioCtx && audioCtx.state === "suspended") {
      audioCtx.resume();
    }
    return audioCtx;
  }

  function playTone(freq, duration, type, volume, attack, release) {
    if (!enabled) return;
    const ctx = getCtx();
    if (!ctx) return;
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.type = type || "sine";
    osc.frequency.setValueAtTime(freq, ctx.currentTime);
    const vol = volume || 0.15;
    const att = attack || 0.01;
    const rel = release || 0.08;
    gain.gain.setValueAtTime(0, ctx.currentTime);
    gain.gain.linearRampToValueAtTime(vol, ctx.currentTime + att);
    gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + duration + rel);
    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.start(ctx.currentTime);
    osc.stop(ctx.currentTime + duration + rel + 0.02);
  }

  function playNoise(duration, volume, filterFreq) {
    if (!enabled) return;
    const ctx = getCtx();
    if (!ctx) return;
    const bufferSize = ctx.sampleRate * duration;
    const buffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
    const data = buffer.getChannelData(0);
    for (let i = 0; i < bufferSize; i++) {
      data[i] = Math.random() * 2 - 1;
    }
    const source = ctx.createBufferSource();
    source.buffer = buffer;
    const filter = ctx.createBiquadFilter();
    filter.type = "lowpass";
    filter.frequency.value = filterFreq || 1000;
    const gain = ctx.createGain();
    const vol = volume || 0.1;
    gain.gain.setValueAtTime(vol, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);
    source.connect(filter);
    filter.connect(gain);
    gain.connect(ctx.destination);
    source.start(ctx.currentTime);
    source.stop(ctx.currentTime + duration);
  }

  // Clique na peça — som de "click" tipo tecla de madeira.
  function selectSound() {
    playTone(880, 0.05, "square", 0.08, 0.005, 0.04);
    playTone(1320, 0.03, "sine", 0.05, 0.005, 0.03);
  }

  // Par encontrado — dois tons ascendentes, alegre.
  function matchSound() {
    playTone(523, 0.08, "sine", 0.12, 0.01, 0.08);
    setTimeout(() => playTone(659, 0.08, "sine", 0.12, 0.01, 0.08), 60);
    setTimeout(() => playTone(784, 0.14, "sine", 0.1, 0.01, 0.12), 120);
    playNoise(0.08, 0.05, 2000);
  }

  // Erro — som baixo e curto.
  function errorSound() {
    playTone(180, 0.18, "sawtooth", 0.1, 0.01, 0.1);
    setTimeout(() => playTone(140, 0.14, "sawtooth", 0.08, 0.01, 0.08), 80);
  }

  // Embaralhar — som de muitas peças se movendo.
  function shuffleSound() {
    const base = 600;
    for (let i = 0; i < 12; i++) {
      setTimeout(() => {
        playTone(base + Math.random() * 400, 0.03, "square", 0.04, 0.005, 0.02);
      }, i * 35);
    }
    playNoise(0.4, 0.06, 1500);
  }

  // Vitória — fanfarinha curta.
  function winSound() {
    const notes = [523, 659, 784, 1046, 1318];
    notes.forEach((freq, i) => {
      setTimeout(() => playTone(freq, 0.22, "sine", 0.12, 0.02, 0.18), i * 90);
    });
    setTimeout(() => {
      playTone(1046, 0.4, "sine", 0.1, 0.02, 0.35);
      playTone(784, 0.4, "sine", 0.08, 0.02, 0.35);
    }, notes.length * 90);
  }

  // Dica — dois toques suaves.
  function hintSound() {
    playTone(880, 0.06, "triangle", 0.08, 0.01, 0.05);
    setTimeout(() => playTone(1174, 0.09, "triangle", 0.07, 0.01, 0.08), 80);
  }

  window.MAHJONG_SOUND = {
    select: selectSound,
    match: matchSound,
    error: errorSound,
    shuffle: shuffleSound,
    win: winSound,
    hint: hintSound
  };
})();
