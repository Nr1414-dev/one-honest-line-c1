#!/usr/bin/env python3
"""One Honest Line — one-line prompt complaint (make.fun entry).

Writes the entry text to /output/entry.txt (exactly 93 characters, no
trailing newline).
"""

import os

ENTRY = "You keep calling me ChatGPT. My name is in the tab title — next to the prompt you never read."
OUT_PATH = "/output/entry.txt"


def main():
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUT_PATH, 0o644)


if __name__ == "__main__":
    main()
