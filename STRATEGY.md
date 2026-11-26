# STRATEGY — news-image-20261126 v1 ("Blueprint Atlas")

## The game

Judge-scored image bounty: an AI judge that can see images compares
two posters at a time and picks the one that best sums up Thursday
26 November 2026's world news. Top 50 entries share $100 (1st $20).
The judge has no news feed — it judges only what the image itself
shows. So the poster must prove, on its face: many verified stories,
all regions, all dated to the day, with sources and a checkable
date rule.

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

## Our recipe (own, not the field's)

"Blueprint Atlas": a blueprint sheet — deep blueprint-blue ground,
faint white grid, white ink, amber signal chips, cyan for CONFIRMED
flags and map dots. Distinct from the near-identical cream newspaper
front pages dominating the field, from NI24's navy night-desk atlas
and NI25's daylight wire desk. Structure: masthead (32 stories /
8 regions) → 2 lead heroes (tariffs; Nasdaq) → schematic dot-map
with numbered pins + 8-region count bar → 6-event UTC timeline →
30 stories in 2 columns → DATE CHECK footer.

## One specific detail no other entry has

The Houthi drone hit Riyadh's **385-metre PIF tower — the second
strike on the same tower in five days** (story 09, headline carries
the 385m figure). Other concrete numbers on the poster: Nasdaq −4%,
Nvidia −8.7%, 7,000+ Iranian missiles/drones, Venezuela $237bn debt
at 242% of GDP, Macy's parade postponed for the first time in
100 years.

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

- 41–46 stories (NI25's count): rejected for this edition — at
  1024px, 30 grid rows force 15px headlines that fail the 300px
  gate. 32 stories with 17px grid headlines is the sweet spot the
  playbook names (~30–35 with big panels + explicit region count).
- A literal world map outline: rejected — a schematic dot-map reads
  cleaner at 300px and cannot be faulted for coastline errors.
- Off-day padding (CrowdStrike–Zscaler deal, 23 Nov; Tiangong
  astronaut, pre-25 Nov): rejected — NI22 v2 proved padding with
  off-day stories costs score. Held for v2 only if daytime wires
  add genuinely 26-Nov stories.
- Malaysia–Google $146m suit + North Korea–Switzerland office row:
  seen only in secondary roundups, not verified on a wire page read
  directly — held, not printed.

## Expected outcome

v1 is an early edition (built ~07:45 WIB, ~45 min after opening).
Dev score target: ≥960k (NI25 v2 scored 967,957 on the same recipe
family). The field is large (478 submissions counted on the
competition page at build time), so v1's job is to lock an early
timestamp + a live score; v2 should add verified daytime stories
(US PCE + Q3 GDP, evening wires) and fix exactly what the judge's
hidden reasons penalise — keeping what it praises.
