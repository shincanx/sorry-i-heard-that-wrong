#!/usr/bin/env python3
"""Sorry, I Heard That Wrong — make.fun entry.

Writes one line (at most 140 characters): the apology a smart speaker
gives its owner after mishearing them. Deterministic, stdlib only, no
network. Output goes to $MAKEFUN_OUTPUT_DIR/entry.txt (else /output).
"""

import os

ENTRY = (
    "Apologies — I heard 'play something relaxing' and started your "
    "3 a.m. existential crisis playlist. We're on track two."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters,
    # not only white space. Fail loudly instead of shipping an invalid line.
    line = ENTRY.strip()
    if not line or len(line) > 140 or "\n" in line:
        raise ValueError(f"entry invalid: {len(line)} chars")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
