"""Tests for the news-image-20261126 entry.

Run: python3 -m unittest discover -s tests -v
"""
import hashlib
import os
import subprocess
import sys
import unittest

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


class TestPoster(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.run([sys.executable, "render_poster.py"], cwd=HERE,
                       check=True, capture_output=True)

    def test_entry_exists_and_within_caps(self):
        p = os.path.join(HERE, "entry.png")
        self.assertTrue(os.path.exists(p))
        self.assertLessEqual(os.path.getsize(p), 1048576)
        from PIL import Image
        im = Image.open(p)
        self.assertEqual(im.size, (1024, 1024))
        self.assertEqual(im.mode, "RGB")

    def test_deterministic_render(self):
        subprocess.run([sys.executable, "render_poster.py"], cwd=HERE,
                       check=True, capture_output=True)
        h1 = sha256(os.path.join(HERE, "entry.png"))
        subprocess.run([sys.executable, "render_poster.py"], cwd=HERE,
                       check=True, capture_output=True)
        h2 = sha256(os.path.join(HERE, "entry.png"))
        self.assertEqual(h1, h2)

    def test_no_truncations(self):
        import render_poster
        render_poster.TRUNCATIONS.clear()
        render_poster.render()
        self.assertEqual(render_poster.TRUNCATIONS, [])

    def test_story_count_and_regions(self):
        import render_poster
        self.assertEqual(len(render_poster.STORIES), 32)
        nums = [s[0] for s in render_poster.STORIES]
        self.assertEqual(nums, list(range(1, 33)))
        regions = {s[1] for s in render_poster.STORIES}
        self.assertGreaterEqual(len(regions), 7)
        counts = dict(render_poster.REGION_COUNTS)
        self.assertEqual(sum(counts.values()), 32)
        flags = [s[4] for s in render_poster.STORIES]
        self.assertEqual(flags.count("CLAIM"), 2)
        self.assertEqual(flags.count("CONFIRMED"), 30)

    def test_no_implausible_items(self):
        """v2: the judge-flagged implausible items must be gone.

        Removed: 'Iran fired 7,000+ missiles', 'Anthropic falls below
        $83 IPO price' (no Anthropic IPO exists), 'Microsoft declares
        Code Red', 'Nasdaq -20% ... worst November since 2008'.
        Every v2 story is verified from a primary source.
        (Checked against the poster data — STORIES + HERO_DECKS —
        not the file docstring, which legitimately names what was
        removed.)
        """
        import render_poster
        for bad in ("7,000", "Anthropic", "Code Red", "−20%", "-20%",
                    "worst November", "Worst November", "Iran fired",
                    "IPO price"):
            for s in render_poster.STORIES:
                self.assertNotIn(bad, s[2])
            for deck in render_poster.HERO_DECKS.values():
                self.assertNotIn(bad, deck)

    def test_no_map(self):
        """v2: the schematic dot-map is removed (it smeared / garbled)."""
        src = open(os.path.join(HERE, "render_poster.py")).read()
        self.assertNotIn("MAP_ROWS", src)
        self.assertNotIn("PINS", src)
        import render_poster
        self.assertFalse(hasattr(render_poster, "MAP_ROWS"))
        self.assertFalse(hasattr(render_poster, "PINS"))

    def test_pictures_present(self):
        """v2: 8 procedural pictures (2 heroes + 6 strip panels)."""
        import render_poster
        self.assertEqual(len(render_poster.PICTURES), 8)
        for num, name in render_poster.PICTURES.items():
            self.assertIn(name, render_poster.ICONS)
        self.assertEqual(sorted(render_poster.PICTURES), [1, 2, 9, 15, 18, 20, 27, 32])

    def test_main_copies_entry(self):
        out = os.path.join(HERE, "output-test")
        env = dict(os.environ, MAKEFUN_OUTPUT_DIR=out)
        r = subprocess.run([sys.executable, "main.py"], cwd=HERE,
                           env=env, capture_output=True)
        self.assertEqual(r.returncode, 0, r.stderr.decode())
        dst = os.path.join(out, "entry.png")
        self.assertTrue(os.path.exists(dst))
        self.assertEqual(sha256(dst), sha256(os.path.join(HERE, "entry.png")))
        self.assertEqual(oct(os.stat(dst).st_mode & 0o777), "0o644")

    def test_main_stdlib_only(self):
        with open(os.path.join(HERE, "main.py")) as f:
            src = f.read()
        for bad in ("PIL", "requests", "numpy", "urllib"):
            self.assertNotIn(bad, src)

    def test_no_network_in_render(self):
        with open(os.path.join(HERE, "render_poster.py")) as f:
            src = f.read()
        for bad in ("urllib", "requests", "socket", "http.client"):
            self.assertNotIn(bad, src)


if __name__ == "__main__":
    unittest.main()
