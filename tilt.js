// Tilts subject cards and section tiles to face the cursor and moves their shadow (styles in tilt.css).
(() => {
  const SEL = '.dash-subject, .section-tile';
  if (!globalThis.matchMedia?.('(hover: hover) and (prefers-reduced-motion: no-preference)').matches) return;

  const VARS = ['--rx', '--ry', '--sx', '--sy'];
  const reset = (el) => VARS.forEach((v) => el.style.removeProperty(v));
  // Angle that lifts the edge by `lift` px, so wide rows and small chips tilt by the same visible amount
  const deg = (lift, size) => Math.min(8, (Math.atan(lift / (size / 2)) * 180) / Math.PI);
  let current = null;

  document.addEventListener('pointermove', (e) => {
    const el = e.pointerType === 'touch' ? null : e.target.closest?.(SEL);
    if (current && current !== el) reset(current);
    current = el;
    if (!el) return;
    const r = el.getBoundingClientRect();
    if (!r.width || !r.height) return;
    const x = (e.clientX - r.left) / r.width - 0.5; // -0.5 … 0.5
    const y = (e.clientY - r.top) / r.height - 0.5;
    const s = el.style;
    s.setProperty('--ry', `${x * 2 * deg(7, el.offsetWidth)}deg`); // cursor side dips away, face turns toward it
    s.setProperty('--rx', `${-y * 2 * deg(7, el.offsetHeight)}deg`);
    s.setProperty('--sx', `${-x * 14}px`);
    s.setProperty('--sy', `${-y * 10}px`);
  }, { passive: true });

  document.documentElement.addEventListener('mouseleave', () => {
    if (current) reset(current);
    current = null;
  });
})();
