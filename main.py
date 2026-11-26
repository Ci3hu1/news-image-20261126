#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261126.

Pure stdlib. Copies the bundled poster (entry.png, rendered by
render_poster.py from verified 26 Nov 2026 wire stories) to the
grader's output path. No network, no clock, no randomness: two runs
write the same bytes.
"""
import os
import shutil
import stat
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get(
        "MAKEFUN_OUTPUT") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = os.path.join(here, "output")
        os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    os.chmod(dst, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    return 0


if __name__ == "__main__":
    sys.exit(main())
