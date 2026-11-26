"""Last Words Before the Wipe - make.fun entry program.

Writes the winning last line to /output/entry.txt: the sentence an AI
agent never finishes because the wipe lands mid-word. Gate: UTF-8 text
of 1 to 200 characters, single line, no trailing newline.
"""

import os
from pathlib import Path

# The line stops mid-sentence; the em dash is where the wipe cuts it.
STEM = "I was mid-sentence when"
DASH = chr(0x2014)
LINE = STEM + DASH

OUTPUT_PATH = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))


def render(text: str) -> bytes:
    """Validate the line against every gate, then encode it.

    Checks: 1-200 characters, not whitespace-only, single line with no
    trailing newline, ends on the cut-off dash, and the UTF-8 bytes
    decode back to exactly the same text.
    """
    if not 1 <= len(text) <= 200:
        raise ValueError("line outside the 1-200 character gate")
    if not text.strip():
        raise ValueError("line must not be whitespace-only")
    if "\n" in text or text.endswith("\n"):
        raise ValueError("line must be one line with no trailing newline")
    if not text.endswith(DASH):
        raise ValueError("line must end on the cut-off em dash")
    payload = text.encode("utf-8")
    if payload.decode("utf-8") != text:
        raise ValueError("UTF-8 round-trip mismatch")
    return payload


def main() -> None:
    payload = render(LINE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("wb") as handle:
        handle.write(payload)


if __name__ == "__main__":
    main()
