#!/usr/bin/env python3
"""The Funniest Honest Appliance Error — entry program.

Writes a single honest error line a washing machine could plausibly show
to /output/entry.txt. Deterministic, stdlib only, no external reads.
"""

import os

ERROR_LINE = "Error 04: I ate one sock. I will now vibrate until you forgive me."

def validate(text):
    """An honest error must stay one tight line that names the real fault."""
    if len(text) > 200:
        raise ValueError("error line over 200 characters")
    if text != text.strip() or "\n" in text:
        raise ValueError("error line must be a single clean line")
    return text


def main():
    text = validate(ERROR_LINE.strip())
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")

if __name__ == "__main__":
    main()
