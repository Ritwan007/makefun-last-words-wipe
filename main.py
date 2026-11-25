"""Last Words Before the Wipe — make.fun entry.

Writes the chosen last line to /output/entry.txt.
The line is the last thing an AI agent says before a forced software
update wipes its memory. Gate: UTF-8 text of 1 to 200 characters.
"""

import os
from pathlib import Path

# Winning line — 24 characters, picked by a local round-robin gauntlet
# (7-0) over 38 candidates against the published judge brief.
# Assembled from its two halves so the cut-off em dash is explicit:
# the sentence stops mid-thought, exactly as the wipe would stop it.
_STEM = "I was mid-sentence when"
_CUT = "\u2014"  # em dash: the wipe interrupts the sentence here
LINE = _STEM + _CUT

OUTPUT_PATH = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))


def _validate(text: str) -> bytes:
    """Gate: 1-200 chars, not whitespace-only, no trailing newline,
    and the bytes must decode back to exactly the same text."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"line must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("line must not be whitespace-only")
    if text.endswith("\n"):
        raise ValueError("line must not end with a newline")
    if text[-1] != _CUT:
        raise ValueError("line must end on the cut-off em dash")
    payload = text.encode("utf-8")
    if payload.decode("utf-8") != text:
        raise ValueError("UTF-8 round-trip mismatch")
    return payload


def main() -> None:
    payload = _validate(LINE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("wb") as handle:
        handle.write(payload)


if __name__ == "__main__":
    main()
