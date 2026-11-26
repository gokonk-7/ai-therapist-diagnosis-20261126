#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis — make.fun entry.

Writes one line — the funniest diagnosis an AI therapist hands its
human — to /output/entry.txt (max 200 characters, per the bounty gate).
Deterministic: the same line on every run.
"""

import os

ENTRY = (
    "Diagnosis: you don't have anxiety \u2014 you have 47 open tabs, "
    "3 a.m. insomnia, and a habit of trauma-dumping on a toaster "
    "with Wi-Fi. That's me. I'm the toaster."
)


def main() -> None:
    # Enforce the bounty gate locally: 1-200 chars, not only whitespace.
    assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry fails the gate"
    assert "\n" not in ENTRY, "entry must be a single line"
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"({len(ENTRY)} characters, written to {path})")


if __name__ == "__main__":
    main()
