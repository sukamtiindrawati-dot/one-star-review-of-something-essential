"""One-Star Review of Something Essential.

Writes a single deadpan one-star review of sleep to /output/entry.txt.
The review is a fixed, hand-written line: no randomness, no network,
no files read from outside this repository.

Before writing, the review is checked against the competition gate:
UTF-8 text of 1 to 160 characters, a single line, not only whitespace.
"""

import os

REVIEW = "Sleep takes a third of my life and gives back a sore neck and a 6 a.m. alarm. One star."

MAX_CHARS = 160


def validate(text: str) -> str:
    """Enforce the gate: 1-160 chars, one line, not only whitespace."""
    if not text.strip():
        raise ValueError("review must not be only whitespace")
    if "\n" in text:
        raise ValueError("review must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"review is {len(text)} chars, over the 160-char limit")
    return text


def main() -> None:
    review = validate(REVIEW)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(review)


if __name__ == "__main__":
    main()
