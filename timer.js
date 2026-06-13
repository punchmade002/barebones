(function () {
  'use strict';

  // ── State ──────────────────────────────────────────────────────
  var totalSec = 0;
  var remainSec = 0;
  var tickId = null;
  var mode = null;      // 'custom' | 'pomodoro'
  var phase = 'work';   // 'work' | 'break'
  var WORK_SEC = 25 * 60;
  var BREAK_SEC = 5 * 60;

  // ── DOM ────────────────────────────────────────────────────────
  var idle      = document.getElementById('timerIdle');
  var active    = document.getElementById('timerActive');
  var fill      = document.getElementById('timerFill');
  var textEl    = document.getElementById('timerText');
  var stopBtn   = document.getElementById('timerStopBtn');

  // ── Start ──────────────────────────────────────────────────────
  function start(minutes, m) {
    clearInterval(tickId);
    mode  = m;
    phase = 'work';

    if (m === 'pomodoro') {
      totalSec = WORK_SEC;
    } else {
      totalSec = minutes * 60;
    }
    remainSec = totalSec;

    // Set fill to 100% before showing so no transition from 0
    fill.style.transition = 'none';
    fill.style.width = '100%';
    active.classList.remove('break-mode');

    idle.classList.add('hidden');
    active.classList.remove('hidden');

    // Restore transition after paint
    requestAnimationFrame(function () {
      requestAnimationFrame(function () {
        fill.style.transition = '';
        renderText();
      });
    });

    tickId = setInterval(tick, 1000);
  }

  // ── Tick ───────────────────────────────────────────────────────
  function tick() {
    remainSec--;

    if (remainSec <= 0) {
      if (mode === 'pomodoro') {
        if (phase === 'work') confetti();   // celebrate end of study phase
        phase     = phase === 'work' ? 'break' : 'work';
        totalSec  = phase === 'work' ? WORK_SEC : BREAK_SEC;
        remainSec = totalSec;
        active.classList.toggle('break-mode', phase === 'break');

        // Snap fill back to 100% without transition
        fill.style.transition = 'none';
        fill.style.width = '100%';
        requestAnimationFrame(function () {
          requestAnimationFrame(function () {
            fill.style.transition = '';
            renderFill();
          });
        });
      } else {
        confetti();
        stop(true);
        return;
      }
    }

    renderFill();
    renderText();
  }

  // ── Render ─────────────────────────────────────────────────────
  function renderFill() {
    var pct = totalSec > 0 ? (remainSec / totalSec) * 100 : 0;
    fill.style.width = pct + '%';
  }

  function renderText() {
    var m = Math.floor(remainSec / 60);
    var s = remainSec % 60;
    var time = pad(m) + ':' + pad(s);

    if (mode === 'pomodoro') {
      textEl.textContent = (phase === 'work' ? 'Study  ' : 'Break  ') + time;
    } else {
      textEl.textContent = time;
    }
  }

  // ── Stop ───────────────────────────────────────────────────────
  function stop() {
    clearInterval(tickId);
    tickId = null;
    mode   = null;
    phase  = 'work';
    active.classList.add('hidden');
    active.classList.remove('break-mode');
    idle.classList.remove('hidden');
  }

  // ── Helpers ────────────────────────────────────────────────────
  function pad(n) { return n < 10 ? '0' + n : '' + n; }

  // ── Confetti ───────────────────────────────────────────────────
  function confetti() {
    var canvas = document.getElementById('confettiCanvas');
    var ctx    = canvas.getContext('2d');
    canvas.width  = window.innerWidth;
    canvas.height = window.innerHeight;
    canvas.style.display = 'block';

    var rect = active.getBoundingClientRect();
    var ox   = rect.left + rect.width  / 2;
    var oy   = rect.top  + rect.height / 2;

    var colors = [
      '#F97316','#FB923C','#FCA55D','#FBBF24',
      '#34D399','#60A5FA','#C084FC','#F43F5E','#FDBA74'
    ];

    var particles = [];
    for (var i = 0; i < 150; i++) {
      // spread mostly upward with wide fan
      var angle = -Math.PI / 2 + (Math.random() - 0.5) * Math.PI * 1.6;
      var speed = Math.random() * 13 + 5;
      particles.push({
        x: ox, y: oy,
        vx: Math.cos(angle) * speed,
        vy: Math.sin(angle) * speed,
        w: Math.random() * 11 + 4,
        h: Math.random() * 6  + 3,
        rot:  Math.random() * 360,
        rotV: (Math.random() - 0.5) * 12,
        color: colors[Math.floor(Math.random() * colors.length)],
        alpha: 1,
        gravity: 0.28
      });
    }

    var raf;
    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      var alive = false;
      for (var j = 0; j < particles.length; j++) {
        var p = particles[j];
        p.x   += p.vx;
        p.y   += p.vy;
        p.vy  += p.gravity;
        p.rot += p.rotV;
        p.alpha -= 0.012;
        if (p.alpha > 0) {
          alive = true;
          ctx.save();
          ctx.globalAlpha = Math.max(0, p.alpha);
          ctx.fillStyle   = p.color;
          ctx.translate(p.x, p.y);
          ctx.rotate(p.rot * Math.PI / 180);
          ctx.fillRect(-p.w / 2, -p.h / 2, p.w, p.h);
          ctx.restore();
        }
      }
      if (alive) {
        raf = requestAnimationFrame(draw);
      } else {
        canvas.style.display = 'none';
        cancelAnimationFrame(raf);
      }
    }
    draw();
  }

  // ── Picker show/hide with delay so crossing the gap doesn't dismiss it ──
  var pickerEl  = document.getElementById('timerPicker');
  var clockBtn  = document.getElementById('timerClockBtn');
  var hideTimer = null;

  function openPicker() {
    clearTimeout(hideTimer);
    pickerEl.classList.add('picker-open');
  }

  function schedulClose() {
    clearTimeout(hideTimer);
    hideTimer = setTimeout(function () {
      // Keep open while custom input is focused
      if (document.activeElement === document.getElementById('timerCustomInput')) return;
      pickerEl.classList.remove('picker-open');
    }, 250);
  }

  clockBtn.addEventListener('mouseenter', openPicker);
  clockBtn.addEventListener('mouseleave', schedulClose);
  pickerEl.addEventListener('mouseenter', openPicker);
  pickerEl.addEventListener('mouseleave', schedulClose);

  // ── Preset time buttons ──
  document.querySelectorAll('.timer-opt[data-minutes]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      start(parseInt(btn.dataset.minutes, 10), 'custom');
    });
  });

  var pomodoroBtn = document.querySelector('.timer-opt[data-mode="pomodoro"]');
  if (pomodoroBtn) {
    pomodoroBtn.addEventListener('click', function () { start(0, 'pomodoro'); });
  }

  // ── Custom time input ──
  var customBtn   = document.getElementById('timerCustomBtn');
  var customRow   = document.getElementById('timerCustomRow');
  var customInput = document.getElementById('timerCustomInput');

  function showCustomInput() {
    customBtn.classList.add('hidden');
    customRow.classList.remove('hidden');
    customInput.focus();
  }

  function hideCustomInput() {
    customRow.classList.add('hidden');
    customBtn.classList.remove('hidden');
    customInput.value = '';
  }

  function startCustom() {
    var val = parseInt(customInput.value, 10);
    if (!val || val < 1 || val > 300) return;
    hideCustomInput();
    pickerEl.classList.remove('picker-open');
    start(val, 'custom');
  }

  customBtn.addEventListener('click', showCustomInput);
  document.getElementById('timerCustomGo').addEventListener('click', startCustom);

  customInput.addEventListener('keydown', function (e) {
    if (e.key === 'Enter') startCustom();
    if (e.key === 'Escape') { hideCustomInput(); pickerEl.classList.remove('picker-open'); }
  });

  // Keep picker open while input is focused; allow 200ms for Go click to register
  customInput.addEventListener('focus', openPicker);
  customInput.addEventListener('blur', function () {
    setTimeout(function () {
      if (document.activeElement !== document.getElementById('timerCustomGo')) {
        hideCustomInput();
      }
      schedulClose();
    }, 200);
  });

  // Only allow numeric characters in the custom input
  customInput.addEventListener('input', function () {
    this.value = this.value.replace(/[^0-9]/g, '');
  });

  stopBtn.addEventListener('click', stop);

})();
