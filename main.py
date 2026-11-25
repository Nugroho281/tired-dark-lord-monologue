"""The Tired Dark Lord entry (make.fun).

Writes one 100-word villain monologue to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt).

The monologue: Marlok, Keeper of the Ember Tithe — forty years taking one
coin in seven from every hearth in the Marches, a ledger that knows your
name, a crown that fits and a chair that does not. His tiredness is never
stated; it lives in the rhythm — the goat deflection, the "Both of
them—well" trail-off, the tithe loop — and the sting lands in the last
line: he counted the seventh coin twice, and counted it wrong. The reign
of terror rests on a counting error.

It won a blind pairwise self-judge 2-0 against its two sibling variants
(margins 2 and 2, both orders) and 2-0 against a generic-dark-lord control
(margin 4, both orders). 101 words, 516 characters, 520 bytes — inside the
1-600 gate and the shortest of the three variants, which helps the byte
tie-break.

Pure Python standard library only; deterministic output.
"""

import os
import sys

MONOLOGUE = (
    "Come in. Mind the third step. It bites. I am Marlok, Keeper of the "
    "Ember Tithe. For forty years I have taken one coin in seven from "
    "every hearth in the Marches. The ledger knows your name. It knows "
    "the goat you hid—no. Not the goat. The point is the tithe. The "
    "point is always the tithe. My uncle wore this crown before me. My "
    "cousin wore it after him. Both of them—well. The crown fits. The "
    "chair does not. Sit. The tea is cold. And when the seventh coin "
    "falls, remember: I counted it twice, and I counted it wrong."
)


def _validate(text: str) -> None:
    """Gate check: 1-600 characters, not whitespace only, 98-102 words.

    The 98-102 window keeps the monologue at "about 100 words" per the
    judge brief while leaving the exact count fixed and deterministic.
    """
    if not 1 <= len(text) <= 600 or not text.strip():
        raise ValueError("entry violates 1-600 character gate")
    words = text.split()
    if not 98 <= len(words) <= 102:
        raise ValueError("entry must be 98-102 words, got %d" % len(words))


def main() -> int:
    _validate(MONOLOGUE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(MONOLOGUE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
