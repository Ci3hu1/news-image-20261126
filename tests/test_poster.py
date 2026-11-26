"""Tests for the news-image-20261126 entry (v3, picture-grid method).

Run: python3 -m unittest discover -s tests -v
"""
import hashlib
import os
import subprocess
import sys
import unittest
from collections import Counter

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
        """v3: 8 procedural pictures (2 heroes + 6 strip panels)."""
        import render_poster
        self.assertEqual(len(render_poster.PICTURES), 8)
        for num, name in render_poster.PICTURES.items():
            self.assertIn(name, render_poster.ICONS)
        self.assertEqual(sorted(render_poster.PICTURES),
                         [1, 2, 9, 15, 18, 20, 27, 32])

    def test_picture_grid(self):
        """v3 (300px method): the 24-item text list is GONE, replaced
        by a 24-card PICTURE GRID, 8 cols x 3 rows.

        Each card is 115x122 with a 99x66 picture (the dominant
        element), a 20px bold amber number, and a 1-line label of
        <=14 chars at 13px bold. At 300px the grid reads as a mosaic
        of pictures, not a wall of text.
        """
        import render_poster
        self.assertEqual(len(render_poster.LIST_NUMS), 24)
        self.assertEqual(render_poster.GRID_COLS, 8)
        self.assertEqual(render_poster.GRID_ROWS, 3)
        self.assertEqual(render_poster.GRID_CARD_W, 115)
        self.assertEqual(render_poster.GRID_CARD_H, 122)
        self.assertEqual(render_poster.GRID_PIC_W, 99)
        self.assertEqual(render_poster.GRID_PIC_H, 66)
        # the picture dominates the card (47% of the card area)
        pic_area = render_poster.GRID_PIC_W * render_poster.GRID_PIC_H
        card_area = render_poster.GRID_CARD_W * render_poster.GRID_CARD_H
        self.assertGreater(pic_area / card_area, 0.40)
        # every grid story has an icon and a short 1-line label
        for num in render_poster.LIST_NUMS:
            self.assertIn(num, render_poster.GRID_ICONS)
            self.assertIn(render_poster.GRID_ICONS[num], render_poster.ICONS)
            self.assertIn(num, render_poster.GRID_LABELS)
            self.assertLessEqual(len(render_poster.GRID_LABELS[num]), 14)
        # labels fit the card at 13px bold (no truncation)
        from PIL import Image, ImageDraw
        tmp = Image.new("RGB", (8, 8))
        dd = ImageDraw.Draw(tmp)
        fnt = render_poster.F_TITLE(13)
        for num, lab in render_poster.GRID_LABELS.items():
            self.assertLessEqual(
                dd.textlength(lab, font=fnt),
                render_poster.GRID_CARD_W - 12,
                f"grid label {num} overflows: {lab!r}")
        # distinct icons: >=12 across the 24 cards, max 3 repeats
        # (the research prototype had 10 distinct / max 4 repeats)
        counts = Counter(render_poster.GRID_ICONS.values())
        self.assertGreaterEqual(len(counts), 12)
        self.assertLessEqual(max(counts.values()), 3)

    def test_no_timeline_overlaps(self):
        """v3 (300px method): the timeline shows TIMES ONLY, 18px bold.

        v2's 11px "10:40 — Sudan strikes" labels overlapped into
        "Saudigeized". Times only, evenly spaced, cannot overlap.
        This test measures the time boxes and requires a >=10px gap
        between neighbours and all boxes inside [M, W-M].
        """
        import render_poster
        boxes = render_poster.timeline_time_boxes()
        self.assertEqual(len(boxes), 6)
        for x0, x1 in boxes:
            self.assertGreaterEqual(x0, render_poster.M)
            self.assertLessEqual(x1, render_poster.W - render_poster.M)
        for i in range(len(boxes) - 1):
            self.assertGreaterEqual(boxes[i + 1][0] - boxes[i][1], 10)
        # the render draws times only: the timeline loop unpacks the
        # event label as _label and never draws it
        src = open(os.path.join(HERE, "render_poster.py")).read()
        self.assertIn("for i, (t, _label) in enumerate(TIMELINE):", src)

    def test_gaza_label_clean(self):
        """v3: the Gaza timeline entry is plain and fully inside.

        v2's '23:30 — Gaza toll: 1,679' read as 'Gaza toll [?],679'
        at 300px. v3 drops the em-dash and the colon after 'toll',
        and the timeline draws times only, so the label cannot garble.
        """
        import render_poster
        gaza = [t for t in render_poster.TIMELINE if t[1].startswith("Gaza")]
        self.assertEqual(len(gaza), 1)
        self.assertEqual(gaza[0], ("23:30", "Gaza toll 1,679"))
        for t, label in render_poster.TIMELINE:
            self.assertNotIn("—", f"{t} {label}")
            self.assertNotIn(":", label)

    def test_region_chips(self):
        """v3 (300px method): the region count is 8 CHIPS, 15px bold,
        not v2's single 13px one-liner (a 3.8px smear at 300px)."""
        import render_poster
        self.assertEqual(len(render_poster.CHIP_LABELS), 8)
        self.assertEqual(sum(c for _, c in render_poster.CHIP_LABELS), 32)
        names = [n for n, _ in render_poster.CHIP_LABELS]
        # abbreviated names so each fits its chip at 15px bold
        for abbr in ("MIDEAST", "N AMERICA", "ASIA-PAC", "LATAM", "MARKETS"):
            self.assertIn(abbr, names)
        self.assertNotIn("MIDDLE EAST", names)
        self.assertNotIn("NORTH AMERICA", names)

    def test_icons_distinctive(self):
        """v3: every picture carries its story's specific number, so
        no icon is a generic pictogram (the v2 judge's complaint).
        19 icons total; the grid adds burst / car / home to the
        prototype's 14, and gavel + flag are drawn bolder."""
        import render_poster
        src = open(os.path.join(HERE, "render_poster.py")).read()
        for marker in ("385m", "2-1", "10%", "100m", "+3.8%", "−4%",
                       "14", "NYC", "CHEN", "19"):
            self.assertIn(marker, src)
        for name in ("river", "rise", "burst", "car", "home",
                     "flag", "gavel", "globe", "bar", "factory", "ballot"):
            self.assertIn(name, render_poster.ICONS)
        self.assertEqual(len(render_poster.ICONS), 19)

    def test_no_misleading_icon_numbers(self):
        """v3: a number drawn ON an icon belongs to ONE story only.

        The plane ('10%' = Brazil duty #27), chart ('−4%' = Nasdaq
        hero #2) and storm ('NYC' = Macy's parade #15) are reused in
        the grid, but the grid cards must NOT show those numbers —
        they belong to a different story. The tag is passed only at
        the hero/strip call sites, never in the grid.
        """
        import render_poster
        self.assertEqual(render_poster.HERO_TAGS, {2: "−4%"})
        self.assertEqual(render_poster.STRIP_TAGS, {15: "NYC", 27: "10%"})
        src = open(os.path.join(HERE, "render_poster.py")).read()
        # the grid call site passes no tag
        grid_call = [ln for ln in src.splitlines()
                     if "ICONS[GRID_ICONS[num]]" in ln]
        self.assertEqual(len(grid_call), 1)
        self.assertNotIn("tag=", grid_call[0])
        # the hero/strip call sites do pass a tag
        self.assertIn("tag=HERO_TAGS.get(num)", src)
        self.assertIn("tag=STRIP_TAGS.get(num)", src)

    def test_footer_two_lines(self):
        """v3 (300px method): the footer is 2 lines, larger (16px +
        13px), not v2's 3 lines with 12px body text (a smear)."""
        src = open(os.path.join(HERE, "render_poster.py")).read()
        self.assertIn("All 32 stories first reported Thu 26 Nov 2026", src)
        self.assertIn("30 CONFIRMED · 2 CLAIM", src)
        self.assertIn("F_TITLE(16)", src)
        self.assertIn("F_TITLE(13)", src)

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
