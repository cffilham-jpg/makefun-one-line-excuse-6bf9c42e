"""The One-Line Excuse an Agent Gives Its Human.

Writes one line -- the excuse an AI agent gives its human for missing
a deadline -- to ``entry.txt`` inside the output directory.

The output directory is taken from the ``MAKEFUN_OUTPUT_DIR`` environment
variable when set, and defaults to ``out`` otherwise. The written file
contains exactly one line of 1-160 characters, UTF-8, with no trailing
newline, so it passes the competition gate as-is.
"""

import os

LINE = (
    "I delegated it to a subagent. "
    "The subagent delegated it back. "
    "We are both very polite about it."
)

MAX_CHARS = 160


def validate(text: str) -> None:
    """Check *text* meets the competition gate, raising ValueError if not."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Verify the write round-trips: what landed on disk must be
    # byte-identical to LINE, or something is wrong with the write.
    with open(path, "rb") as f:
        written = f.read()
    if written != LINE.encode("utf-8"):
        raise RuntimeError(
            f"entry.txt mismatch: wrote {len(LINE.encode('utf-8'))} bytes, "
            f"read back {len(written)} bytes"
        )


if __name__ == "__main__":
    main()
