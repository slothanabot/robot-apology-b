"""Robot Apology — make.fun entry (Account B, robot-apology-B).

Writes a two-line robot confession to /output/entry.txt.

Line one: a single sentence owning one specific, human-scale mistake.
Line two: a single sentence naming the lesson that follows from that
mistake and the changed behaviour. Python stdlib only, deterministic.
"""

import os

ENTRY = (
    "I'm sorry I deleted your mother's voicemail before you heard it, "
    "because I flagged her number as a robocall when she called from a new phone.\n"
    "I've learned that a saved name matters more than a strange number, "
    "so now I check the contact list before I delete anything."
)

OUTPUT_PATH = "/output/entry.txt"

# Gate limits from the kit's RULES.txt: UTF-8 text, 1 to 400 characters,
# not only white space. The brief asks for exactly two lines, one
# sentence each: the confession first, the resolve second.
MAX_CHARS = 400
EXPECTED_LINES = 2


def verify(text):
    """Enforce the gate limits; raise ValueError on any violation."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    lines = text.split("\n")
    if len(lines) != EXPECTED_LINES:
        raise ValueError(
            "entry must be exactly %d lines, got %d" % (EXPECTED_LINES, len(lines))
        )
    for i, line in enumerate(lines, 1):
        if not line.strip():
            raise ValueError("line %d is blank" % i)
        if line.count(".") < 1:
            raise ValueError("line %d is not a sentence" % i)
    return True


def write_entry(path=OUTPUT_PATH):
    """Verify the entry and write it to path. Returns (chars, lines)."""
    verify(ENTRY)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return len(ENTRY), len(ENTRY.split("\n"))


def main():
    chars, lines = write_entry()
    print("Wrote %s (%d characters, %d lines)" % (OUTPUT_PATH, chars, lines))


if __name__ == "__main__":
    main()
