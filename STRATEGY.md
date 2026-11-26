# STRATEGY — news-image-20261126 v2 ("Blueprint Atlas v2")

## The game

Judge-scored image bounty: an AI judge that can see images compares
two posters at a time and picks the one that best sums up Thursday
26 November 2026's world news. Top 50 entries share $100 (1st $20).
The judge has no news feed — it judges only what the image itself
shows. So the poster must prove, on its face: many verified stories,
all regions, all dated to the day, with sources and a checkable
date rule.

## v1 result and the judge's reasons

v1 (commit 856460b, submission 01a215cc) scored live dev 951,391
(95.1391%, 9W/1D/2L, provisional). Judge reasons (match-by-match in
NOTES.md):
- PRAISED (keep): names the day explicitly; 32 stories across
  8 regions; UTC timeline; per-story sources (Reuters/AP/AFP);
  CLAIM flags + date-check box; honest about unconfirmed claims.
- PENALISED (fix in v2): (1) 300px legibility — the dense 32-line
  micro-list was "unreadable at 300px" (#1 penalty); (2) the
  schematic map "smears with garbled labels" / "nearly formless";
  (3) implausible items stated as fact — Iran 7,000+ missiles,
  Anthropic IPO, Microsoft Code Red, Nasdaq −20% / worst November;
  (4) "a text dashboard with no pictures".

## v2 changes (exactly the four fixes)

1. **300px legibility.** The 32 stories are restructured, not
   shrunk: 2 pictorial heroes (26px headlines) + a 6-panel picture
   strip + a 24-item list at 20px bold in 32px rows with short
   labels (≤33 chars, zero truncation — the renderer reports any
   truncation and the test fails on it). Story count and region
   counts are unchanged (32 / 8 regions).
2. **Map removed.** The schematic dot-map is gone entirely. The
   space it occupied is now the picture strip + a taller timeline.
3. **Implausible items removed/corrected.** Iran 7,000+ missiles →
   Israel opposition backs Oct 7 probe (Reuters, 25 Nov). Anthropic
   IPO → US PCE inflation +3.8% in Oct (Reuters, 25 Nov). Microsoft
   Code Red → US Q3 GDP +4.3% (Reuters, 25 Nov). The Nasdaq −20% /
   worst-November deck line is replaced by the verified "Nvidia
   −8.7% leads the slide; Nasdaq ~4% lower on tariff fear and the
   AI rout." Every v2 story is verified from a primary wire read
   directly; a test asserts the four forbidden strings are absent.
4. **Pictures added.** 8 procedural illustrations in the blueprint
   palette (ship, falling chart, tower+drone, storm, skyline,
   mine, plane, football) — 2 hero pictures + 6 strip panels.
   Bold, simple shapes so they read at 300px.

## Measured edge (what the winners do, from the playbook)

- 29–38 sourced stories, 7–9 regions, explicit region count.
- Big panels + big headlines, a map, sources per story,
  CLAIM/CONFIRMED flags, a UTC timeline, a date-check panel.
- 300px legibility: dense micro-text is the #1 recurring judge
  penalty ("unreadable smears"). Masthead + hero headlines + region
  counts + date check must read at 300px wide.
- No internal contradictions: the header must agree with the
  date-check box (NI22 v1 lost matches on 'ALL FROM SUNDAY' vs a box
  admitting Nov 20–21 events).
- v2 note: the playbook's "a map" is dropped on the judge's own
  evidence — our schematic map smeared, so pictures replace it.

## Our recipe (own, not the field's)

"Blueprint Atlas v2": a blueprint sheet — deep blueprint-blue ground,
faint white grid, white ink, amber signal chips, cyan for CONFIRMED
flags. Distinct from the near-identical cream newspaper front pages
dominating the field, from NI24's navy night-desk atlas and NI25's
daylight wire desk. Structure: masthead (32 stories / 8 regions) →
2 lead heroes with pictures (tariffs; Nasdaq) → 6-panel picture strip
→ 6-event UTC timeline + 8-region count line → 24 stories in 2
columns at 20px → DATE CHECK footer.

## One specific detail no other entry has

The Houthi drone hit Riyadh's **385-metre PIF tower — the second
strike on the same tower in five days** (story 09, strip panel,
headline carries the 385m figure). Other concrete numbers on the
poster: Nasdaq −4%, Nvidia −8.7%, PCE +3.8% (core +3.3%, 3-year
high), Q3 GDP +4.3% (fastest in 3 years), Venezuela $237bn debt
at 242% of GDP, Macy's parade postponed for the first time in
100 years, Thanksgiving storm 250M+.

## Story selection

32 stories, 8 regions (Europe 6, Mideast 6, North America 5,
Asia-Pacific 6, Africa 3, Latin America 2, Markets & Tech 3,
Sport 1). Every story verified from a primary wire read directly
(Reuters / AP / AFP) — see BRIEF.md for the per-story source.
30 CONFIRMED, 2 CLAIM (Kyiv's 5-jet tally at Savasleyka; the Niger
kidnapping, per security sources). Date rule (RULES.txt: first
reported 26 Nov "in any time zone"): all 32 filed on the wires
25 Nov UTC and first reported 26 Nov in at least one time zone
(UTC+14; WIB for stories filed after 17:00 UTC). The DATE CHECK
panel states this window — it does not claim every wire was dated
26 Nov UTC, and it agrees with the masthead.

## Tried and dropped

- 41–46 stories (NI25's count): rejected — at 1024px, 30+ grid rows
  force micro-text that fails the 300px gate. 32 stories split across
  heroes + strip + a 24-item list at 20px is the v2 sweet spot.
- A literal world map outline: rejected — a schematic dot-map reads
  cleaner at 300px and cannot be faulted for coastline errors.
  (v2: even the schematic map is dropped — the judge smeared it.)
- Off-day padding (CrowdStrike–Zscaler deal, 23 Nov; Tiangong
  astronaut, pre-25 Nov): rejected — NI22 v2 proved padding with
  off-day stories costs score.
- Malaysia–Google $146m suit + North Korea–Switzerland office row:
  seen only in secondary roundups, not verified on a wire page read
  directly — held, not printed.
- Photographs / external images: not used — the kit's grader runs
  offline and the entry must be self-contained; procedural Pillow
  illustrations keep the build deterministic and dependency-free.

## Expected outcome

v2 is a BUILD only (not submitted without a fresh 'Setuju'). Target:
beat v1's live dev 951,391 by fixing the #1 penalty (300px
legibility) and the map/picture penalties while keeping everything
the judge praised. The field is large (478 submissions counted on
the competition page at v1 build time), so v2's job is a higher
win rate in the live dev matches; entries close 28 Nov 07:00 WIB,
results 12 Dec 2026.

## v3 result (built 26 Nov 2026 ~10:45 WIB; Joni: "Ya, bangun v3 news-image")

v2 scored live dev 972,121 (97.2121%, 12W/0D/0L) — it beat v1, but
the judge's 2 dissenting calls were still the list legibility
(24 items at 20px) plus timeline garbles and generic icons. v3
is a targeted refinement, not a rebuild: the praised structure is
unchanged (masthead → 2 heroes → picture strip → timeline →
list → DATE CHECK), but the list is 22 items at 26px in 38px rows
(+30% type, +19% row spacing, labels ≤24 chars), the strip is
8 panels (Sudan + PCE move into pictures), the timeline is 5
events at 13px with measured non-overlapping labels, and every
icon carries its story's specific number. Target: beat v2's
972,121 by flipping the 2 dissenting calls. v3 is a BUILD only
(not submitted without a fresh 'Setuju').
