"""Two Lines to Your Past Self — make.fun entry.

Writes the two-line warning to /output/entry.txt.
Deterministic: the same bytes on every run. Standard library only.
"""

from pathlib import Path

LINES = (
    "Don't take the last bus out of Bandung the night your grandmother called.",
    "You arrived after she was gone, and the goodbye you rehearsed on the road "
    "became a sentence you never got to say.",
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Exactly two lines, one sentence each; a trailing newline ends the
    # second line and keeps the file at two lines, never three.
    text = "\n".join(LINES) + "\n"
    assert len(LINES) == 2, "entry must be exactly two lines"
    assert 1 <= len(text) <= 280, "entry must be 1-280 characters"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
