"""Say What Actually Broke - one line of brutal, funny error copy.

The program writes a single-line software error message (max 200 chars)
to /output/entry.txt. Stdlib only, no network, deterministic.
"""

import os

LINE = (
    "We found your account \u2014 in a database table we dropped "
    "by accident. Please sign up again. You're new here now."
)


def main():
    # Gate: the contest allows 1-200 characters, one line, no padding.
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
