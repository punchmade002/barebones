"""Zero-dependency test runner for the pipeline.

    python3 tests/run_tests.py            # all suites
    python3 tests/run_tests.py ids gate   # only the named suites

There is no pytest in this environment and the pipeline should stay installable with nothing
but PyMuPDF, so this is a plain runner: every module in tests/ named `suite_*.py` exposes
`TESTS`, a list of (name, callable). A callable that returns without raising has passed.

Two kinds of test live here:

  * INVARIANT tests — pure assertions about behaviour (ids stay unique, the gate blocks on a
    known-bad store). These are the ones that catch a regression.
  * GOLDEN tests — a frozen input in tests/fixtures/ and its expected output. These exist
    because the pipeline's stages are generators whose output could previously only be judged
    by eye. `--update-golden` re-freezes them, which should only ever be done deliberately,
    after inspecting the diff.
"""
from __future__ import annotations
import importlib
import json
import sys
import traceback
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIXTURES = HERE / "fixtures"
sys.path.insert(0, str(HERE.parent))          # import pipeline modules
sys.path.insert(0, str(HERE))                 # import suite_* modules

UPDATE_GOLDEN = "--update-golden" in sys.argv


def golden(name: str, produced):
    """Compare `produced` against the frozen fixture `name`, or re-freeze it under
    --update-golden. Raises AssertionError with a located, readable diff on mismatch."""
    path = FIXTURES / name
    if UPDATE_GOLDEN or not path.exists():
        path.write_text(json.dumps(produced, ensure_ascii=False, indent=2))
        print(f"    (froze golden {name})")
        return
    expected = json.loads(path.read_text())
    if produced == expected:
        return
    raise AssertionError(f"golden mismatch vs {name}\n" + _diff(expected, produced))


def _diff(exp, got, path="") -> str:
    """First few concrete differences, addressed by path — far more useful than a dumped blob."""
    out: list[str] = []

    def walk(a, b, p):
        if len(out) >= 6:
            return
        if type(a) is not type(b):
            out.append(f"  {p or '<root>'}: type {type(a).__name__} != {type(b).__name__}")
        elif isinstance(a, dict):
            for k in sorted(set(a) | set(b)):
                if k not in a:
                    out.append(f"  {p}.{k}: unexpected key = {b[k]!r}")
                elif k not in b:
                    out.append(f"  {p}.{k}: missing key (expected {a[k]!r})")
                else:
                    walk(a[k], b[k], f"{p}.{k}")
        elif isinstance(a, list):
            if len(a) != len(b):
                out.append(f"  {p}: length {len(a)} != {len(b)}")
            for i, (x, y) in enumerate(zip(a, b)):
                walk(x, y, f"{p}[{i}]")
        elif a != b:
            out.append(f"  {p}: expected {a!r}\n       got      {b!r}")

    walk(exp, got, path)
    return "\n".join(out) or "  (structures differ but no leaf diff found)"


SUITES = ["ids", "segment", "validate", "gate", "flashcards", "resources", "retrieval"]


def main() -> int:
    wanted = [a for a in sys.argv[1:] if not a.startswith("-")] or SUITES
    passed = failed = 0
    failures: list[tuple[str, str]] = []
    for suite_name in wanted:
        mod = importlib.import_module(f"suite_{suite_name}")
        print(f"\n{suite_name}")
        for name, fn in mod.TESTS:
            try:
                fn()
            except Exception:
                failed += 1
                failures.append((f"{suite_name}/{name}", traceback.format_exc()))
                print(f"  FAIL  {name}")
            else:
                passed += 1
                print(f"  ok    {name}")
    print(f"\n{'=' * 60}\n{passed} passed, {failed} failed")
    for label, tb in failures:
        print(f"\n--- {label} ---\n{tb}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
