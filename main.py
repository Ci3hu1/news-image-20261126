#!/usr/bin/env python3
"""Entrypoint for the make.fun news-image-20261126 v3 poster.

Standard library only. Copies the bundled poster image (entry.png,
drawn by render_poster.py from verified 26 November 2026 wire
stories) to the grader's output location. No network access, no
clock reads, no randomness: the output bytes are identical on
every run, and the file mode is 0644.
"""
import os
import shutil
import sys


def _resolve_output_dir():
    """Pick the grader's output directory.

    The kit sets MAKEFUN_OUTPUT_DIR (preferred) or MAKEFUN_OUTPUT;
    fall back to /output, and to a local ./output if that cannot be
    created (e.g. read-only root in a sandbox).
    """
    here = os.path.dirname(os.path.abspath(__file__))
    for key in ("MAKEFUN_OUTPUT_DIR", "MAKEFUN_OUTPUT"):
        value = os.environ.get(key)
        if value:
            return value
    try:
        os.makedirs("/output", exist_ok=True)
        return "/output"
    except OSError:
        fallback = os.path.join(here, "output")
        os.makedirs(fallback, exist_ok=True)
        return fallback


def main(argv=None):
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    target_dir = _resolve_output_dir()
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.png")
    shutil.copyfile(source, target)
    os.chmod(target, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
