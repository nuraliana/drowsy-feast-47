"""Entry program for the make.fun bounty "The Best Meal You Ever Had".

Writes the chosen one-sentence entry to entry.txt inside
MAKEFUN_OUTPUT_DIR (or ./output when unset), byte-exact, with no
trailing newline. Python 3 standard library only.
"""

import os

SENTENCE = (
    "The best meal I ever had was instant noodles my brother made at "
    "2 a.m. after our father's funeral, eaten in silence on the stairs "
    "while the steam fogged his glasses."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
