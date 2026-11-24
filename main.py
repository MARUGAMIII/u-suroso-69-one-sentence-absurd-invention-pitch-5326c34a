#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single sentence pitching a ridiculous invention that fixes a tiny
everyday annoyance to /output/entry.txt.

The pitch: a toothbrush that tattles to your dentist every time you skip a
night, so your six-month checkup opens with a full criminal record instead
of small talk. Stdlib only, no network, no external files.
"""

import os

ENTRY = (
    "A toothbrush that tattles to your dentist every time you skip a night, "
    "so your six-month checkup opens with a full criminal record instead of "
    "small talk."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert text.endswith("."), "entry must be a single sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
