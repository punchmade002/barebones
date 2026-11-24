// Homepage hero: the logo's LED dot grid as a live field that lights up
// what's inside the app, word by word. Needs pixelfont.js (PixelText.FONT).
(function () {
  'use strict';
  var hero = document.querySelector('[data-field]');
  if (!hero || !window.PixelText) return;

  var FONT = Object.assign({}, PixelText.FONT, {
    ' ': ['     ', '     ', '     ', '     ', '     ', '     ', '     ']
  });
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var TAU = Math.PI * 2;
  var COLOR = '#fff9f4';

  // ---------------- the field ----------------
  var canvas = document.createElement('canvas');
  canvas.className = 'field';
  canvas.setAttribute('aria-hidden', 'true');
  hero.prepend(canvas);
  hero.classList.add('has-field');
  var ctx = canvas.getContext('2d');
  var W = 0, H = 0, dpr = 1, gap = 15, cols = 0, rows = 0;
  var cur, goal, tgt, at;            // lit level, current goal, target, time the target applies
  var ripples = [];
  var ptr = { x: -1e4, y: -1e4 };
  var raf = 0, onScreen = true, lastText = null;

  function resize() {
    W = hero.clientWidth; H = hero.clientHeight;
    dpr = Math.min(2, window.devicePixelRatio || 1);
    canvas.width = Math.round(W * dpr); canvas.height = Math.round(H * dpr);
    gap = W < 640 ? 9 : 15;
    cols = Math.ceil(W / gap); rows = Math.ceil(H / gap);
    var n = cols * rows;
    cur = new Float32Array(n); goal = new Float32Array(n); tgt = new Float32Array(n); at = new Float64Array(n);
    if (lastText) setText(lastText.text, lastText.slot, { fit: lastText.fit });
    kick();
  }

  // Light `text` in the dots under `slot`, at the biggest whole-dot scale that fits.
  // Returns the lit box in hero pixels.
  function setText(text, slot, opts) {
    opts = opts || {};
    text = String(text || '').toUpperCase();
    lastText = slot ? { text: text, slot: slot, fit: opts.fit } : null;
    var mask = new Uint8Array(cols * rows);
    var box = null;
    if (slot && text) {
      var hr = hero.getBoundingClientRect(), sr = slot.getBoundingClientRect();
      var fitLen = (opts.fit || text).length;
      var s = Math.floor(Math.min(sr.width / ((fitLen * 6 - 1) * gap), sr.height / (7 * gap)));
      s = Math.max(1, Math.min(4, s));
      var c0 = Math.ceil((sr.left - hr.left) / gap);
      var r0 = Math.round((sr.top - hr.top + (sr.height - 7 * s * gap) / 2) / gap);
      for (var k = 0; k < text.length; k++) {
        var g = FONT[text[k]] || FONT[' '];
        for (var r = 0; r < 7; r++) for (var c = 0; c < 5; c++) {
          if (g[r][c] !== '#') continue;
          for (var dy = 0; dy < s; dy++) for (var dx = 0; dx < s; dx++) {
            var col = c0 + (k * 6 + c) * s + dx, row = r0 + r * s + dy;
            if (col >= 0 && col < cols && row >= 0 && row < rows) mask[row * cols + col] = 1;
          }
        }
      }
      box = { x: c0 * gap, y: r0 * gap, w: (text.length * 6 - 1) * s * gap, h: 7 * s * gap };
      var startCol = c0;
    }
    var now = performance.now();
    for (var i = 0; i < mask.length; i++) {
      if (tgt[i] === mask[i]) continue;
      tgt[i] = mask[i];
      // wipe: dots switch left to right, new ones a beat after old ones go out
      at[i] = now + (opts.wipe ? Math.max(0, (i % cols) - (startCol || 0)) * 9 + (mask[i] ? 140 : 0) : 0);
    }
    if (reduce) { cur.set(tgt); goal.set(tgt); }
    kick();
    return box;
  }

  function ripple(x, y, strength) {
    if (reduce) return;
    ripples.push({ x: x, y: y, t: performance.now(), s: strength || 1 });
    kick();
  }

  function frame(now) {
    raf = 0;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, W, H);
    ctx.fillStyle = COLOR;
    var t = now / 1000, R = 150, R2 = R * R;
    for (var q = ripples.length - 1; q >= 0; q--) if (now - ripples[q].t > 1800) ripples.splice(q, 1);
    for (var r = 0; r < rows; r++) {
      var y = r * gap + gap / 2;
      for (var c = 0; c < cols; c++) {
        var i = r * cols + c, x = c * gap + gap / 2;
        if (now >= at[i]) goal[i] = tgt[i];
        cur[i] += (goal[i] - cur[i]) * 0.2;
        var a = 0.2, grow = 0;
        if (!reduce) {
          a = 0.15 + 0.08 * Math.sin(t * 1.4 - c * 0.18 + r * 0.09);   // slow diagonal swell
          var dx = x - ptr.x, dy = y - ptr.y, d2 = dx * dx + dy * dy;
          if (d2 < R2) { var k = 1 - Math.sqrt(d2) / R; a += 0.5 * k * k; grow += k * k; }
          for (var j = 0; j < ripples.length; j++) {
            var rp = ripples[j], age = now - rp.t;
            var e = 1 - Math.abs(Math.hypot(x - rp.x, y - rp.y) - age * 0.6) / 55;
            if (e > 0) { var f = e * (1 - age / 1800) * rp.s; a += 0.6 * f; grow += f; }
          }
        }
        var lit = cur[i];
        a += (1 - a) * lit;
        ctx.globalAlpha = a > 1 ? 1 : a;
        ctx.beginPath();
        ctx.arc(x, y, gap * (0.11 + 0.27 * lit + 0.07 * Math.min(1, grow)), 0, TAU);
        ctx.fill();
      }
    }
    if (!reduce && onScreen && !document.hidden) raf = requestAnimationFrame(frame);
  }
  function kick() { if (!raf) raf = requestAnimationFrame(frame); }

  new ResizeObserver(function () { resize(); }).observe(hero);
  new IntersectionObserver(function (es) { onScreen = es[0].isIntersecting; if (onScreen) kick(); }).observe(hero);
  document.addEventListener('visibilitychange', kick);
  hero.addEventListener('pointermove', function (e) {
    var r = hero.getBoundingClientRect();
    ptr.x = e.clientX - r.left; ptr.y = e.clientY - r.top;
  });
  hero.addEventListener('pointerleave', function () { ptr.x = ptr.y = -1e4; });
  hero.addEventListener('pointerdown', function (e) {
    var r = hero.getBoundingClientRect();
    ripple(e.clientX - r.left, e.clientY - r.top, 0.8);
  });

  // ---------------- the board: what's inside ----------------
  var slot = hero.querySelector('[data-led]');
  var words = ['NOTES', 'CARDS', 'PAPERS', 'GUIDES', 'TESTS'];
  var n = 0;
  resize();
  setText(words[0], slot, { wipe: true, fit: 'PAPERS' });
  if (!reduce) setInterval(function () {
    n = (n + 1) % words.length;
    setText(words[n], slot, { wipe: true, fit: 'PAPERS' });
  }, 1900);
})();
