#!/usr/bin/env python3
"""Write one short calming text to MAKEFUN_OUTPUT_DIR/entry.txt."""

import os


TEXT = (
    "The sea goes on saying the same slow thing to the shore, and the shore "
    "keeps listening. Somewhere above it, a gull rides wind it cannot "
    "see. You are one small warm thing among all of it, held by a world much "
    "older and much quieter than any hurry."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
