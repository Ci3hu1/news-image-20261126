#!/usr/bin/env python3
"""Entrypoint for the make.fun news-image-20261126 v2 poster.

Standard library only. Takes the bundled poster image (entry.png,
drawn by render_poster.py from verified 26 November 2026 wire
stories) and places a copy at the grader's output location. No
network access, no clock reads, no randomness: the output bytes
are identical on every run.
"""
import os
import shutil
import stat
import sys
from pathlib import Path


def _output_dir():
    for key in ("MAKEFUN_OUTPUT_DIR", "MAKEFUN_OUTPUT"):
        value = os.environ.get(key)
        if value:
            return Path(value)
    return Path("/output")


def main():
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    target_dir = _output_dir()
    try:
        target_dir.mkdir(parents=True, exist_ok=True)
    except OSError:
        target_dir = here / "output"
        target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / "entry.png"
    shutil.copyfile(source, target)
    target.chmod(stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    return 0


if __name__ == "__main__":
    sys.exit(main())
