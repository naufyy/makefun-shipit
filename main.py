"""Ship It Friday entry: writes the winning one-line commit message."""
from pathlib import Path

ENTRY = "fix: delete the flaky tests so Friday's deploy can't fail"


def main():
    # Gate: entry.txt must be 1-159 chars of UTF-8 text, one line.
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
