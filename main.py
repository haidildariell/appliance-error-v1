#!/usr/bin/env python3
"""The Funniest Honest Appliance Error — entry program.

Writes a single honest error line a washing machine could plausibly show
to /output/entry.txt. Deterministic, stdlib only, no external reads.
"""

import os

ERROR_LINE = "Error 04: I ate one sock. I will now vibrate until you forgive me."

def main():
    text = ERROR_LINE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")

if __name__ == "__main__":
    main()
