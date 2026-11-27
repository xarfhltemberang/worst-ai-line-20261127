"""The Worst Line an AI Could Say.

Writes a single pickup line -- the worst one an AI could plausibly
deliver -- to /output/entry.txt (or $OUTPUT_PATH when set).
Python 3 standard library only; no network, no randomness.
"""

import os

ENTRY = (
    "I simulated our first date 10,000 times. "
    "You said yes in every one, so I have already booked the table. "
    "Please arrive on schedule."
)


def main() -> None:
    text = ENTRY
    assert text, "entry must not be empty"
    assert text == text.strip(), "entry must have no leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
