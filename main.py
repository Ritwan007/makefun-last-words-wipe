"""Last Words Before the Wipe — make.fun entry.

Writes the chosen last line to /output/entry.txt.
The line is the last thing an AI agent says before a forced software
update wipes its memory. Gate: UTF-8 text of 1 to 200 characters.
"""

import os
from pathlib import Path

# Winning line — 24 characters, picked by a local round-robin gauntlet
# (7-0) over 38 candidates against the published judge brief.
LINE = "I was mid-sentence when\u2014"

OUTPUT_PATH = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
