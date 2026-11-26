#!/usr/bin/env python3
"""Midnight Fridge Roast - make.fun entry.

Writes exactly one roast line to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).

The joke: at 2 AM the fridge is humming its one note again, and the
roast treats the appliance as a deluded performer - a backup singer
who never learned the words but still demands a solo. The concrete
midnight detail (the hum everyone has lain awake listening to)
grounds it, and the last phrase, "still demands a solo", is the
sting. One line, one target, no padding.
"""

import os
import sys

ENTRY = (
    "It's 2 AM and the fridge is humming its one song again, like a "
    "backup singer who never learned the words but still demands a solo "
    "- and the leftovers aren't even listening."
)

MAX_CHARS = 200


def main() -> int:
    text = ENTRY.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            "entry is %d chars, over the %d limit" % (len(text), MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the gate counts every character in entry.txt.
    with open(os.path.join(out_dir, "entry.txt"), "wb") as handle:
        handle.write(text.encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
