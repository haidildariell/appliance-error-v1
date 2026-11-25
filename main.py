#!/usr/bin/env python3
"""The Funniest Honest Appliance Error — entry program.

Writes one honest error line a washing machine could plausibly show
to /output/entry.txt. Deterministic, stdlib only, no network,
no external file reads.
"""

import os

ERROR_LINE = "Error 04: I ate one sock. I will now vibrate until you forgive me."


def validate(text):
    """An honest error stays one tight line that names the real fault."""
    if len(text) > 200:
        raise ValueError("error line over 200 characters")
    if text != text.strip() or "\n" in text:
        raise ValueError("error line must be a single clean line")
    return text


def build_error():
    """Assemble the fault and the apology; the machine confesses, then begs."""
    fault = "Error 04: I ate one sock."
    apology = "I will now vibrate until you forgive me."
    return fault + " " + apology


def main():
    text = validate(build_error())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
