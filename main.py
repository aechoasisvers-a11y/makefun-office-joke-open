"""Office Joke Open entry: write one single-line office joke to entry.txt.

Pure stdlib Python 3.13. Deterministic output: the exact joke text below,
written with no trailing newline.
"""

import os

JOKE = (
    "The printer only jams when the deadline is today, "
    "which is how I know it reads my calendar better than my boss does."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    # Self-check: read back and verify the gate and the exact intended text.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == JOKE, "output does not match the intended joke"
    assert 1 <= len(written) <= 200, "char count outside the 1-200 gate"
    assert written.strip(), "output is only whitespace"
    assert not written.endswith("\n"), "unexpected trailing newline"
    assert "\n" not in written, "joke must be a single line"


if __name__ == "__main__":
    main()
