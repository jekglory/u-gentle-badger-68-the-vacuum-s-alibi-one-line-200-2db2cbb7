"""The Vacuum's Alibi entry: one original line, at most 200 characters.

A robot vacuum's deadpan log entry explaining why it missed a spot.

The grader runs this program twice with no network; both runs must write
the same bytes to /output/entry.txt. The line is a fixed string, so the
output is deterministic by construction: no clock, no randomness, no
environment reads, no network, no I/O other than the single write.
"""

import os


LINE = (
    "Log 214: the crumb under the table survived 41 passes, so I "
    "reclassified it as furniture. It has seniority. I respect seniority."
)

OUTPUT_PATH = "/output/entry.txt"

# The competition requires one line of at most 200 characters.
MAX_CHARS = 200


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "line must be 1-%d chars, got %d" % (MAX_CHARS, len(text))
        )
    if "\n" in text:
        raise SystemExit("line must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = text.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    # Verify the artifact the judge will read is exactly the line.
    with open(OUTPUT_PATH, "rb") as f:
        if f.read() != data:
            raise SystemExit("written bytes do not match the line")
    print(text)


if __name__ == "__main__":
    main()
