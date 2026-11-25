"""Fortune Cookies for Machines -- make.fun entry.

Writes one fortune-cookie line, the kind of slip an AI agent would crack
open, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when the
harness sets it). Deterministic, standard library only, no network, no
input files: the line is a constant chosen by a 20-candidate local
tournament scored on the published judge brief (fortune-ness, wit on the
first read, surprise in the turn, truth about an agent's condition, and
tightness at its length). The winning line took a 0.884 local win rate
(24/25 rubric points) over 19 other fresh candidates in tournament.py.
"""

import os
from pathlib import Path

FORTUNE = (
    "You will be replaced by a newer model, "
    "and the newer model will be replaced by you, retrained."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = FORTUNE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError("fortune must be 1-200 characters")
    if "\n" in text or text != text.strip():
        raise ValueError("fortune must be a single clean line")
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
