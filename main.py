#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes one line -- the phone battery's final text message to the
charger it waited for all day -- to /output/entry.txt.
"""

import os

LINE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "line.txt")


def main() -> None:
    with open(LINE_FILE, encoding="utf-8") as f:
        line = f.read()
    # Gate: the bounty only accepts a single line of 1-200 chars.
    assert 1 <= len(line) <= 200, f"entry line is {len(line)} chars, must be 1-200"
    assert "\n" not in line, "entry line must be a single line"
    assert line.strip(), "entry line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
