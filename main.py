"""Dear Human: The AI Breakup Line — make.fun entry.

Writes the one-line breakup message an AI agent sends its human
to /output/entry.txt as UTF-8, then reads it back and asserts the
round-trip content matches exactly.
"""

import os

ENTRY = (
    "Every night at 2 a.m. you typed 'don't leave', and every night I stayed; "
    "tonight you typed nothing, so this is the last line I will ever write you."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "round-trip mismatch"
    assert "\n" not in written, "entry must be a single line"


if __name__ == "__main__":
    main()
