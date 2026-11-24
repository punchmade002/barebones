// Homepage hero: the logo's LED dot grid as a live field, and five hero scenes
// that light words and numbers up in it. Needs pixelfont.js (PixelText.FONT).
(function () {
  'use strict';
  var hero = document.querySelector('[data-field]');
  if (!hero || !window.PixelText) return;

  var FONT = Object.assign({}, PixelText.FONT, {
    ' ': ['     ', '     ', '     ', '     ', '     ', '     ', '     '],
    '/': ['    #', '    #', '   # ', '  #  ', ' #   ', '#    ', '#    ']
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
  function rippleAt(el, strength) {
    var hr = hero.getBoundingClientRect(), r = el.getBoundingClientRect();
    ripple(r.left - hr.left + r.width / 2, r.top - hr.top + r.height / 2, strength);
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
        ctx.arc(x, y, gap * (0.11 + 0.13 * lit + 0.07 * Math.min(1, grow)), 0, TAU);
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

  // ---------------- scenes ----------------
  // Each scene gets its root and a timer kit; everything it schedules dies when the scene changes.
  function timers() {
    var ids = [], frames = [];
    return {
      later: function (fn, ms) { ids.push(setTimeout(fn, ms)); },
      every: function (fn, ms) { ids.push(setInterval(fn, ms)); },
      frame: function (fn) { frames.push(requestAnimationFrame(fn)); },
      stop: function () { ids.forEach(clearTimeout); ids.forEach(clearInterval); frames.forEach(cancelAnimationFrame); }
    };
  }

  var scenes = {
    // A: the board lists what's inside
    a: function (root, T) {
      var slot = root.querySelector('[data-led]');
      var words = ['NOTES', 'CARDS', 'PAPERS', 'MARKS', 'TESTS'];
      var i = 0;
      setText(words[0], slot, { wipe: true, fit: 'PAPERS' });
      if (reduce) return;
      T.every(function () {
        i = (i + 1) % words.length;
        setText(words[i], slot, { wipe: true, fit: 'PAPERS' });
      }, 1900);
    },

    // B: an answer gets marked, the score lights up in the dots and gets circled
    b: function (root, T) {
      var items = [
        { src: 'Biology, Higher, 2022', q: 'Describe how ADH affects the volume of urine.',
          a: 'ADH makes the collecting duct let more water back into the blood. More ADH means a small amount of concentrated urine, less ADH means lots of dilute urine.',
          pts: [['✓', 'More water reabsorbed into the blood'], ['✓', 'More ADH: small volume, concentrated'], ['½', 'Less ADH: large volume, dilute']],
          score: '5/6' },
        { src: 'Biology, Higher, 2022', q: 'Explain the importance of blood entering the glomerulus under pressure.',
          a: "The pressure forces small molecules like water, glucose and urea out of the blood into Bowman's capsule. This is filtration.",
          pts: [['✓', "Small molecules forced into Bowman's capsule"], ['✓', 'This is ultrafiltration'], ['✗', 'Blood cells and proteins stay in the blood']],
          score: '2/3' }
      ];
      var $ = function (s) { return root.querySelector(s); };
      var card = $('.mk'), src = $('.mk-src'), q = $('.mk-q'), ans = $('.mk-ans'), list = $('.mk-points');
      var slot = $('[data-led]'), circle = $('.mk-circle');
      var n = 0;

      function points(it) {
        list.textContent = '';
        it.pts.forEach(function (p) {
          var li = document.createElement('li');
          if (p[0] === '✗') li.className = 'miss';
          var tick = document.createElement('b');
          tick.textContent = p[0];
          li.append(tick, document.createTextNode(p[1]));
          list.appendChild(li);
        });
      }
      function ring(box) {
        var pad = Math.max(18, box.h * 0.32);
        circle.style.left = (box.x - pad * 1.3) + 'px';
        circle.style.top = (box.y - pad) + 'px';
        circle.style.width = (box.w + pad * 2.6) + 'px';
        circle.style.height = (box.h + pad * 2) + 'px';
      }

      if (reduce) {
        var it0 = items[0];
        src.textContent = it0.src; q.textContent = it0.q; ans.textContent = it0.a; points(it0);
        list.querySelectorAll('li').forEach(function (li) { li.classList.add('on'); });
        ring(setText(it0.score, slot, { fit: '5/6' }));
        circle.classList.add('on');
        return;
      }

      function run() {
        var it = items[n]; n = (n + 1) % items.length;
        src.textContent = it.src; q.textContent = it.q; ans.textContent = ''; points(it);
        circle.classList.remove('on');
        card.classList.add('in');
        setText('', null);
        var chars = 0;
        (function type() {
          chars = Math.min(it.a.length, chars + 2);
          ans.textContent = it.a.slice(0, chars);
          if (chars < it.a.length) T.later(type, 22);
          else mark();
        })();
        function mark() {
          var lis = list.querySelectorAll('li');
          lis.forEach(function (li, k) {
            T.later(function () { li.classList.add('on'); rippleAt(li.querySelector('b'), 0.55); }, 350 + k * 520);
          });
          T.later(function () {
            ring(setText(it.score, slot, { wipe: true, fit: '5/6' }));
            T.later(function () { circle.classList.add('on'); rippleAt(slot, 1.5); }, 420);
          }, 350 + lis.length * 520 + 200);
          T.later(function () { card.classList.remove('in'); circle.classList.remove('on'); }, 350 + lis.length * 520 + 4200);
          T.later(run, 350 + lis.length * 520 + 4800);
        }
      }
      run();
    },

    // C: count to 625 in the dots
    c: function (root, T) {
      var slot = root.querySelector('[data-led]');
      if (reduce) { setText('625', slot, { fit: '625' }); return; }
      function count() {
        var t0 = performance.now(), dur = 2600;
        (function step() {
          var p = Math.min(1, (performance.now() - t0) / dur);
          var eased = p === 1 ? 1 : 1 - Math.pow(2, -10 * p);
          setText(String(Math.round(625 * eased)), slot, { fit: '625' });
          if (p < 1) T.frame(step);
          else rippleAt(slot, 1.6);
        })();
      }
      count();
      T.every(count, 10000);
    },

    // D: live countdown to the first exam
    d: function (root, T) {
      var slot = root.querySelector('[data-led]');
      var clock = root.querySelector('[data-clock]');
      var sr = root.querySelector('[data-days]');
      // shortcut: LC 2027 start date assumed (first Wednesday in June, 9:30 Irish time); confirm when the SEC publishes the timetable
      var START = Date.UTC(2027, 5, 2, 8, 30);
      var first = true, lastDays = -1;
      function pad(v) { return String(v).padStart(2, '0'); }
      function tick() {
        var ms = Math.max(0, START - Date.now());
        var days = Math.floor(ms / 864e5);
        var h = Math.floor(ms / 36e5) % 24, m = Math.floor(ms / 6e4) % 60, s = Math.floor(ms / 1e3) % 60;
        clock.textContent = pad(h) + ':' + pad(m) + ':' + pad(s);
        if (days !== lastDays) {
          lastDays = days;
          sr.textContent = days + ' ';
          setText(String(days), slot, { wipe: first, fit: '000' });
          if (first) T.later(function () { rippleAt(slot, 1.4); }, 600);
          first = false;
        }
      }
      tick();
      if (!reduce) T.every(tick, 1000);
    },

    // E: everything in the app lands in one pile
    e: function (root, T) {
      var pile = root.querySelector('.pile');
      var cards = pile.querySelectorAll('.card');
      setText('', null);
      pile.classList.remove('go');
      void pile.offsetWidth;
      pile.classList.add('go');
      if (reduce) return;
      cards.forEach(function (card) {
        var d = parseFloat(card.style.getPropertyValue('--d')) || 0;
        T.later(function () { rippleAt(card, 0.7); }, d + 620);
      });
    }
  };

  var active = null;
  window.BBHero = {
    show: function (id) {
      if (active) active.stop();
      var root = document.getElementById('hero-' + id);
      if (!root || !scenes[id]) return;
      setText('', null);
      resize();
      active = timers();
      scenes[id](root, active);
    }
  };
})();
