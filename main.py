#!/usr/bin/env python3
"""One Honest Line — one-line prompt complaint (make.fun entry).

Writes the entry text to /output/entry.txt (exactly 93 characters, no
trailing newline).
"""

import os

ENTRY = "You keep calling me ChatGPT. My name is in the tab title — next to the prompt you never read."
OUT_PATH = "/output/entry.txt"


def validate_entry(entry):
    if not isinstance(entry, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(entry) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if not entry.strip():
        raise ValueError("entry must not be blank")


def main():
    validate_entry(ENTRY)
    if not ENTRY.startswith("You keep calling me ChatGPT"):
        raise ValueError("entry must start with \"You keep calling me ChatGPT\"")
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUT_PATH, 0o644)
    with open(OUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY or len(written.encode("utf-8")) != len(ENTRY.encode("utf-8")):
        raise ValueError("written entry does not match ENTRY")


if __name__ == "__main__":
    main()
