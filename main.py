#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt (exactly the line, no trailing newline, no padding)
and prints it to stdout. Deterministic.
"""

import os

LINE = "The bug you cannot reproduce is the one you already shipped."


def validate(line):
    if not isinstance(line, str):
        raise TypeError("entry must be a string")
    if len(line) != 60:
        raise ValueError("entry must be exactly 60 characters")
    return line


def write_entry(line):
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)


def main():
    line = validate(LINE)
    write_entry(line)
    print(line)


if __name__ == "__main__":
    main()
