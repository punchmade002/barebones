/* barebones pixel-font — renders short accent labels in the LED dot-matrix style of the logo.
   Use declaratively:  <span class="pix" data-text="01"></span>
   Optional attrs: data-size (px per dot), data-gap (px), data-dim ("1" shows faint off-pixels). */
(function () {
  // 5x7 bitmaps. '#'=on. Only the glyphs we actually use as accents.
  const F = {
    '0': [' ### ', '#   #', '#  ##', '# # #', '##  #', '#   #', ' ### '],
    '1': ['  #  ', ' ##  ', '  #  ', '  #  ', '  #  ', '  #  ', ' ### '],
    '2': [' ### ', '#   #', '    #', '   # ', '  #  ', ' #   ', '#####'],
    '3': ['#####', '   # ', '  ## ', '    #', '    #', '#   #', ' ### '],
    '4': ['   # ', '  ## ', ' # # ', '#  # ', '#####', '   # ', '   # '],
    '5': ['#####', '#    ', '#### ', '    #', '    #', '#   #', ' ### '],
    '6': [' ### ', '#    ', '#    ', '#### ', '#   #', '#   #', ' ### '],
    '7': ['#####', '    #', '   # ', '  #  ', ' #   ', ' #   ', ' #   '],
    '8': [' ### ', '#   #', '#   #', ' ### ', '#   #', '#   #', ' ### '],
    '9': [' ### ', '#   #', '#   #', ' ####', '    #', '    #', ' ### '],
    'A': [' ### ', '#   #', '#   #', '#####', '#   #', '#   #', '#   #'],
    'B': ['#### ', '#   #', '#   #', '#### ', '#   #', '#   #', '#### '],
    'C': [' ### ', '#   #', '#    ', '#    ', '#    ', '#   #', ' ### '],
    'D': ['#### ', '#   #', '#   #', '#   #', '#   #', '#   #', '#### '],
    'E': ['#####', '#    ', '#    ', '#### ', '#    ', '#    ', '#####'],
    'F': ['#####', '#    ', '#    ', '#### ', '#    ', '#    ', '#    '],
    'H': ['#   #', '#   #', '#   #', '#####', '#   #', '#   #', '#   #'],
    'I': [' ### ', '  #  ', '  #  ', '  #  ', '  #  ', '  #  ', ' ### '],
    'K': ['#   #', '#  # ', '# #  ', '##   ', '# #  ', '#  # ', '#   #'],
    'L': ['#    ', '#    ', '#    ', '#    ', '#    ', '#    ', '#####'],
    'M': ['#   #', '## ##', '# # #', '# # #', '#   #', '#   #', '#   #'],
    'N': ['#   #', '##  #', '##  #', '# # #', '#  ##', '#  ##', '#   #'],
    'O': [' ### ', '#   #', '#   #', '#   #', '#   #', '#   #', ' ### '],
    'P': ['#### ', '#   #', '#   #', '#### ', '#    ', '#    ', '#    '],
    'R': ['#### ', '#   #', '#   #', '#### ', '# #  ', '#  # ', '#   #'],
    'S': [' ####', '#    ', '#    ', ' ### ', '    #', '    #', '#### '],
    'T': ['#####', '  #  ', '  #  ', '  #  ', '  #  ', '  #  ', '  #  '],
    'U': ['#   #', '#   #', '#   #', '#   #', '#   #', '#   #', ' ### '],
    'V': ['#   #', '#   #', '#   #', '#   #', '#   #', ' # # ', '  #  '],
    'W': ['#   #', '#   #', '#   #', '# # #', '# # #', '## ##', '#   #'],
    'X': ['#   #', '#   #', ' # # ', '  #  ', ' # # ', '#   #', '#   #'],
    'Y': ['#   #', '#   #', ' # # ', '  #  ', '  #  ', '  #  ', '  #  '],
    ' ': ['     ', '     ', '     ', '     ', '     ', '     ', '     '],
    '.': ['     ', '     ', '     ', '     ', '     ', ' ##  ', ' ##  '],
    '!': ['  #  ', '  #  ', '  #  ', '  #  ', '  #  ', '     ', '  #  '],
  };

  function buildGlyph(rows, size, color, dim) {
    const g = document.createElement('span');
    g.style.display = 'grid';
    g.style.gridTemplateColumns = `repeat(5, ${size}px)`;
    g.style.gridTemplateRows = `repeat(7, ${size}px)`;
    g.style.gap = Math.max(1, Math.round(size * 0.18)) + 'px';
    for (let r = 0; r < 7; r++) {
      for (let c = 0; c < 5; c++) {
        const on = rows[r][c] === '#';
        const d = document.createElement('span');
        d.style.borderRadius = Math.max(1, Math.round(size * 0.28)) + 'px';
        if (on) d.style.background = color;
        else if (dim) d.style.background = 'color-mix(in srgb, ' + color + ' 14%, transparent)';
        g.appendChild(d);
      }
    }
    return g;
  }

  function render(el) {
    const text = (el.getAttribute('data-text') || el.textContent || '').toUpperCase();
    const size = parseFloat(el.getAttribute('data-size')) || 5;
    const gap = el.getAttribute('data-gap') != null ? parseFloat(el.getAttribute('data-gap')) : size * 1.4;
    const color = el.getAttribute('data-color') || 'var(--orange)';
    const dim = el.getAttribute('data-dim') === '1';
    el.textContent = '';
    el.style.display = 'inline-flex';
    el.style.alignItems = 'flex-start';
    el.style.gap = gap + 'px';
    el.style.lineHeight = '0';
    el.setAttribute('aria-label', text);
    for (const ch of text) {
      const rows = F[ch] || F[' '];
      el.appendChild(buildGlyph(rows, size, color, dim));
    }
  }

  function processAll(root) {
    (root || document).querySelectorAll('.pix').forEach(render);
  }

  window.PixelText = { render, processAll, FONT: F };
  if (document.readyState !== 'loading') processAll();
  else document.addEventListener('DOMContentLoaded', () => processAll());
})();
