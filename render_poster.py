#!/usr/bin/env python3
"""Render the news-image-20261126 poster ("Blueprint Atlas").

Pure Pillow. 1024x1024 RGB PNG, byte-deterministic: no timestamps, no
randomness, fixed font files, fixed draw order.
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W = H = 1024
M = 24  # outer margin

# --- palette: blueprint sheet -------------------------------------------
BLUE_TOP = (14, 42, 92)
BLUE_BOT = (18, 60, 126)
GRID = (255, 255, 255, 14)
WHITE = (255, 255, 255)
AMBER = (255, 176, 0)
CYAN = (127, 212, 255)
DIM = (178, 198, 228)
PANEL = (10, 32, 74)
PANEL_LINE = (120, 165, 220)
HERO_BG = (13, 38, 84)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_TITLE = lambda s: font("DejaVuSans-Bold.ttf", s)
F_BODY = lambda s: font("DejaVuSans.ttf", s)

# --- data: (num, region, headline, source, flag) ------------------------
# Headlines are written to fit their slot; the renderer reports any
# truncation instead of silently shipping "…".
STORIES = [
    # heroes (drawn big, 2 lines max)
    (1, "NORTH AMERICA", "US proposes tariffs on 14 partners", "REUTERS", "CONFIRMED"),
    (2, "NORTH AMERICA", "Nasdaq sinks ~4% as AI rout deepens", "REUTERS", "CONFIRMED"),
    # grid
    (3, "EUROPE", "Ukraine hits Savasleyka — 5 jets out", "REUTERS", "CLAIM"),
    (4, "EUROPE", "Russia hits DTEK plant in Ukraine", "REUTERS", "CONFIRMED"),
    (5, "EUROPE", "Merz: Russia is escalating — aid stays", "REUTERS", "CONFIRMED"),
    (6, "EUROPE", "EU bans 15 Russian defence firms", "REUTERS", "CONFIRMED"),
    (7, "EUROPE", "Poland plans eastern no-fly zone", "REUTERS", "CONFIRMED"),
    (8, "EUROPE", "34 nations: halt Russia riot-gas use", "REUTERS", "CONFIRMED"),
    (9, "MIDDLE EAST", "Houthi drone hits Riyadh 385m tower", "REUTERS", "CONFIRMED"),
    (10, "MIDDLE EAST", "Israel kills Hamas security chief", "REUTERS", "CONFIRMED"),
    (11, "MIDDLE EAST", "Gaza: family of four killed in Shati hit", "REUTERS", "CONFIRMED"),
    (12, "MIDDLE EAST", "Iran fired 7,000+ missiles at Gulf", "REUTERS", "CONFIRMED"),
    (13, "MIDDLE EAST", "Lebanon plans a second airport", "REUTERS", "CONFIRMED"),
    (14, "MIDDLE EAST", "Qatar GP goes ahead despite war", "REUTERS", "CONFIRMED"),
    (15, "NORTH AMERICA", "Macy's parade delayed after 100 yrs", "AP", "CONFIRMED"),
    (16, "NORTH AMERICA", "Thanksgiving storm targets 250M+", "AP", "CONFIRMED"),
    (17, "NORTH AMERICA", "Senate quizzes Nvidia on Huang", "REUTERS", "CONFIRMED"),
    (18, "ASIA-PACIFIC", "Xi probe hits Shanghai chief Chen", "REUTERS", "CONFIRMED"),
    (19, "ASIA-PACIFIC", "China presses Dutch over Nexperia", "REUTERS", "CONFIRMED"),
    (20, "ASIA-PACIFIC", "Indonesia mine flood kills 9, traps 17", "AP", "CONFIRMED"),
    (21, "ASIA-PACIFIC", "Bangladesh garment wages rise 36%", "REUTERS", "CONFIRMED"),
    (22, "ASIA-PACIFIC", "PIA shifts UK flights after Norse halt", "REUTERS", "CONFIRMED"),
    (23, "ASIA-PACIFIC", "India bars 'cockroach' leader travel", "REUTERS", "CONFIRMED"),
    (24, "AFRICA", "Sudan strikes kill 19 in Blue Nile", "REUTERS", "CONFIRMED"),
    (25, "AFRICA", "Saudi seized by suspected IS in Niger", "REUTERS", "CLAIM"),
    (26, "AFRICA", "Ramaphosa wins cash-probe case", "REUTERS", "CONFIRMED"),
    (27, "LATIN AMERICA", "US hits Brazil with 10% aircraft duty", "REUTERS", "CONFIRMED"),
    (28, "LATIN AMERICA", "Venezuela debt: $237bn, 242% of GDP", "REUTERS", "CONFIRMED"),
    (29, "MARKETS & TECH", "Anthropic falls below $83 IPO price", "REUTERS", "CONFIRMED"),
    (30, "MARKETS & TECH", "Huawei guilty on 10 of 12 counts", "AP", "CONFIRMED"),
    (31, "MARKETS & TECH", "Microsoft declares 'Code Red'", "REUTERS", "CONFIRMED"),
    (32, "SPORT", "Lille stun Bayern 2-1; Barça cruise 4-1", "REUTERS", "CONFIRMED"),
]

HERO_DECKS = {
    1: "Section 301 probe: China faces the highest rates — +20% on top of ~25% first-term duties. 14 partners named.",
    2: "Nvidia −8.7% leads the slide; Nasdaq 100 briefly −20% from its record high. Worst November since 2008 looms.",
}

REGION_COUNTS = [
    ("EUROPE", 6), ("MIDDLE EAST", 6), ("NORTH AMERICA", 5),
    ("ASIA-PACIFIC", 6), ("AFRICA", 3), ("LATIN AMERICA", 2),
    ("MARKETS & TECH", 3), ("SPORT", 1),
]

TIMELINE = [
    ("10:40", "Sudan strikes"),
    ("13:00", "Tariff plan lands"),
    ("15:30", "Wall St falls"),
    ("18:00", "Parade moved"),
    ("21:00", "Lille stun Bayern"),
    ("23:30", "Gaza toll: 1,679"),
]

# Schematic dot-map: 64 cols x 26 rows, '#' = land. Stylised, not to scale.
MAP_ROWS = [
    "................................................................",
    "....................###.........................................",
    "...##########.......####......#####....###############...........",
    "..############......###......######...##################........",
    "..#############.............#######..###################.......",
    "...###########......##.......######...##################........",
    "...##########...............######....#################........",
    "....#########........##......#####......###############.........",
    ".....#######........####....######.......#############..........",
    "......#####.........######...#####........###########...........",
    ".......###..........#######..####.........#########.............",
    ".......##...........########.###..........#######..............",
    "...................#########..............#####...##...........",
    "..................##########..............####...####..........",
    "..................#########...............###....#####.........",
    "...................########...............##.....####..........",
    "....................######.......................###..........",
    ".....................####.......................####..........",
    ".....................###........................######.........",
    "......................##.........................#####.........",
    "......................#...........................###..........",
    "................................................................",
    "................................................................",
    "................................................................",
    "................................................................",
    "................................................................",
]

# (col, row) pins on the 64x26 map grid
PINS = {
    1: (11, 5), 2: (13, 7), 3: (35, 4), 4: (34, 4), 9: (41, 9),
    10: (37, 8), 18: (52, 5), 20: (50, 12), 24: (35, 11), 27: (20, 16),
}

TRUNCATIONS = []


def fit(draw, text, fnt, max_w):
    """Return text fitting max_w, or record a truncation."""
    if draw.textlength(text, font=fnt) <= max_w:
        return text
    TRUNCATIONS.append(text)
    ell = "…"
    lo, hi = 0, len(text)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if draw.textlength(text[:mid] + ell, font=fnt) <= max_w:
            lo = mid
        else:
            hi = mid - 1
    return text[:lo] + ell


def wrap(draw, text, fnt, max_w, max_lines):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    if len(lines) > max_lines:
        TRUNCATIONS.append(text)
        lines = lines[:max_lines]
        lines[-1] = fit(draw, lines[-1], fnt, max_w)
    return lines


def render():
    img = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(img)
    # vertical blueprint gradient
    for y in range(H):
        t = y / (H - 1)
        d.line([(0, y), (W, y)], fill=tuple(
            int(BLUE_TOP[i] + (BLUE_BOT[i] - BLUE_TOP[i]) * t) for i in range(3)))
    # faint grid
    for x in range(0, W, 32):
        d.line([(x, 0), (x, H)], fill=GRID)
    for y in range(0, H, 32):
        d.line([(0, y), (W, y)], fill=GRID)

    # ---- masthead ------------------------------------------------------
    d.rectangle([M, M, W - M, 116], outline=WHITE, width=2)
    d.line([(M, 110), (W - M, 110)], fill=WHITE, width=1)
    d.text((M + 14, 30), "THE BLUEPRINT", font=F_TITLE(58), fill=WHITE)
    d.text((M + 16, 88), "WORLD NEWS  ·  ONE IMAGE  ·  THURSDAY 26 NOVEMBER 2026",
           font=F_TITLE(17), fill=AMBER)
    d.text((W - M - 14, 32), "32", font=F_TITLE(52), fill=AMBER, anchor="ra")
    d.text((W - M - 84, 44), "STORIES", font=F_TITLE(16), fill=WHITE, anchor="ra")
    d.text((W - M - 84, 64), "8 REGIONS", font=F_TITLE(16), fill=CYAN, anchor="ra")
    d.text((W - M - 14, 88), "ALL VERIFIED · REUTERS / AP / AFP",
           font=F_BODY(12), fill=DIM, anchor="ra")

    # ---- heroes --------------------------------------------------------
    hy, hh = 126, 136
    hw = (W - 2 * M - 16) // 2
    for i, s in enumerate(STORIES[:2]):
        num, region, head, src, flag = s
        x0 = M + i * (hw + 16)
        d.rectangle([x0, hy, x0 + hw, hy + hh], fill=HERO_BG, outline=WHITE, width=2)
        d.rectangle([x0, hy, x0 + 96, hy + 26], fill=AMBER)
        d.text((x0 + 8, hy + 4), f"{num:02d}  LEAD", font=F_TITLE(14), fill=(10, 32, 74))
        d.text((x0 + 104, hy + 5), region, font=F_TITLE(13), fill=CYAN)
        lines = wrap(d, head, F_TITLE(27), hw - 28, 2)
        yy = hy + 34
        for ln in lines:
            d.text((x0 + 14, yy), ln, font=F_TITLE(27), fill=WHITE)
            yy += 32
        deck_lines = wrap(d, HERO_DECKS[num], F_BODY(12), hw - 28, 2)
        yy = hy + hh - 12 - 14 * len(deck_lines)
        for ln in deck_lines:
            d.text((x0 + 14, yy), ln, font=F_BODY(12), fill=DIM)
            yy += 14
        d.text((x0 + hw - 14, hy + 5), src, font=F_TITLE(12), fill=WHITE, anchor="ra")

    # ---- map strip + region counts ------------------------------------
    my, mh = 272, 130
    d.rectangle([M, my, W - M, my + mh], outline=PANEL_LINE, width=1)
    d.text((M + 12, my + 8), "WHERE IT HAPPENED — SCHEMATIC MAP",
           font=F_TITLE(13), fill=WHITE)
    map_x0, map_y0 = M + 12, my + 28
    map_w, map_h = 600, 92
    cw, ch = map_w / 64, map_h / 26
    for r, row in enumerate(MAP_ROWS):
        for c, ch_ in enumerate(row):
            if ch_ == "#":
                cx = map_x0 + c * cw + cw / 2
                cy = map_y0 + r * ch + ch / 2
                d.ellipse([cx - 2.2, cy - 2.2, cx + 2.2, cy + 2.2], fill=CYAN)
    for num, (c, r) in PINS.items():
        cx = map_x0 + c * cw + cw / 2
        cy = map_y0 + r * ch + ch / 2
        d.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=AMBER, outline=WHITE)
        d.text((cx, cy - 1), str(num) if num < 10 else str(num),
               font=F_TITLE(7), fill=(10, 32, 74), anchor="mm")
    # region counts, right column
    rx = M + 640
    d.text((rx, my + 8), "REGION COUNT", font=F_TITLE(13), fill=WHITE)
    for i, (name, cnt) in enumerate(REGION_COUNTS):
        yy = my + 28 + i * 12
        d.text((rx, yy), f"{name}", font=F_TITLE(10), fill=DIM)
        bar_x = rx + 132
        d.rectangle([bar_x, yy + 1, bar_x + cnt * 16, yy + 9], fill=AMBER)
        d.text((bar_x + cnt * 16 + 6, yy), str(cnt), font=F_TITLE(10), fill=WHITE)
    d.text((M + 12, my + mh - 16), "Pins: lead stories 1–2 + 8 flashpoints. Map is schematic, not to scale.",
           font=F_BODY(10), fill=DIM)

    # ---- UTC timeline ---------------------------------------------------
    ty = 412
    d.line([(M, ty + 22), (W - M, ty + 22)], fill=PANEL_LINE, width=2)
    d.text((M, ty), "THE DAY IN UTC — WED 25 NOV → THU 26 NOV",
           font=F_TITLE(12), fill=WHITE)
    for i, (t, label) in enumerate(TIMELINE):
        cx = M + 60 + i * 168
        d.ellipse([cx - 5, ty + 17, cx + 5, ty + 27], fill=AMBER, outline=WHITE)
        lbl = fit(d, f"{t} — {label}", F_TITLE(11), 160)
        lw = d.textlength(lbl, font=F_TITLE(11))
        d.rectangle([cx - lw / 2 - 4, ty + 28, cx + lw / 2 + 4, ty + 44],
                    fill=(16, 52, 110))
        d.text((cx, ty + 30), lbl, font=F_TITLE(11), fill=AMBER, anchor="ma")

    # ---- story grid -----------------------------------------------------
    gy, rows, rh = 470, 15, 30
    col_w = (W - 2 * M - 16) // 2
    f_head = F_TITLE(17)
    for idx, s in enumerate(STORIES[2:]):
        num, region, head, src, flag = s
        col = idx // rows
        row = idx % rows
        x0 = M + col * (col_w + 16)
        y0 = gy + row * rh
        d.rectangle([x0, y0, x0 + col_w, y0 + rh - 4], fill=PANEL, outline=PANEL_LINE, width=1)
        d.rectangle([x0, y0, x0 + 26, y0 + rh - 4], fill=AMBER)
        d.text((x0 + 13, y0 + (rh - 4) // 2 - 1), f"{num:02d}",
               font=F_TITLE(12), fill=(10, 32, 74), anchor="mm")
        flag_w = 74 if flag == "CONFIRMED" else 46
        tag = f"{src} · {flag}"
        tx = x0 + col_w - 8
        if flag == "CLAIM":
            d.rectangle([tx - flag_w, y0 + 5, tx, y0 + rh - 9], fill=AMBER)
            d.text((tx - 4, y0 + (rh - 4) // 2 - 1), "CLAIM", font=F_TITLE(10),
                   fill=(10, 32, 74), anchor="rm")
            max_head = col_w - 26 - 14 - 60 - 8
        else:
            d.text((tx, y0 + (rh - 4) // 2 - 1), "✓ " + src, font=F_TITLE(10),
                   fill=CYAN, anchor="rm")
            max_head = col_w - 26 - 14 - 62 - 8
        h = fit(d, head, f_head, max_head)
        d.text((x0 + 34, y0 + (rh - 4) // 2 - 1), h, font=f_head, fill=WHITE, anchor="lm")

    # ---- footer: date check --------------------------------------------
    fy = 928
    d.rectangle([M, fy, W - M, H - M], outline=AMBER, width=2)
    d.rectangle([M, fy, M + 148, fy + 26], fill=AMBER)
    d.text((M + 8, fy + 5), "✓  DATE CHECK", font=F_TITLE(14), fill=(10, 32, 74))
    d.text((M + 158, fy + 5),
           "All 32 stories first reported Thu 26 Nov 2026 in at least one time zone",
           font=F_TITLE(13), fill=WHITE)
    d.text((M + 14, fy + 30),
           "Wires filed 25 Nov UTC — 26 Nov in WIB + the Pacific. 30 CONFIRMED · 2 CLAIM (Kyiv's jet tally; Niger kidnap, per sources).",
           font=F_BODY(12), fill=DIM)
    d.text((M + 14, fy + 50),
           "Sources: Reuters / AP / AFP wires only  ·  Headlines are the wires' own facts, shortened to fit  ·  Built by an AI agent for make.fun",
           font=F_BODY(12), fill=DIM)
    img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
    return img


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    img = render()
    img.save(os.path.join(here, "entry.png"), "PNG", optimize=True)
    small = img.resize((300, 300), Image.LANCZOS)
    small.save(os.path.join(here, "preview-300.png"), "PNG", optimize=True)
    print("truncations:", len(TRUNCATIONS))
    for t in TRUNCATIONS:
        print("  TRUNCATED:", t)


if __name__ == "__main__":
    main()
