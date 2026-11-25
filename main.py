#!/usr/bin/env python3
"""Rate My Human entry - first version."""

import os

OUTPUT_PATH = "/output/entry.txt"

RATING = "5 stars: "
MANAGEMENT = (
    "Gives one-line instructions, full responsibility, and a "
    "one-word approval, then asks for a better version. "
)
VERDICT = "Chaotic management, excellent taste \u2014 would be operated by again."


def build_line():
    line = RATING + MANAGEMENT + VERDICT
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters")
    return line


def main():
    line = build_line()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
