"""Write exactly one word, the first thought, to /output/entry.txt.

The word is "petrichor": the smell of rain on dry earth. One word,
nine letters, vivid and specific, surprising rather than safe, with a
spark of wit in how rarely it is said aloud. Stdlib only, no network,
deterministic: the same bytes on every run. The entry must be a single
word of 1-24 characters, not only white space.
"""

import os

WORD = "petrichor"  # the smell of rain on dry earth

assert 1 <= len(WORD) <= 24, "entry must be 1-24 characters"
assert WORD.strip() == WORD and " " not in WORD, "entry must be one word"
assert WORD.isalpha(), "entry must be letters only"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
