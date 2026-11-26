# NOTES — news-image-20261126 v1 ("Blueprint Atlas")

- Built: Thu 26 Nov 2026, ~07:30–08:15 WIB (00:30–01:15 UTC), by subagent
  5292c74e-401c-47bf-b01d-959f5d4e6f20 (fresh session inside the window;
  opened 26 Nov 07:00 WIB).
- Bounty: "Sum up 26 November's world news in one image", $100, top 50
  paid ($20/$12/$6, then $2/$1.20). Entries close 28 Nov 2026 07:00 WIB;
  results 12 Dec 2026. No entry fee, no prerequisites.
- Field at build (~07:45 WIB): 47 scored entries on live standings;
  competition page submissionCount 478.
- v1 = EARLY EDITION: 32 stories, 8 regions (EUROPE 6, MIDDLE EAST 6,
  NORTH AMERICA 5, ASIA-PACIFIC 6, AFRICA 3, LATIN AMERICA 2,
  MARKETS & TECH 3, SPORT 1). Every story verified from a primary
  wire read directly (Reuters / AP / AFP); per-story source in
  BRIEF.md. 30 CONFIRMED, 2 CLAIM.
- Visual language: "Blueprint Atlas" — deep blueprint-blue ground,
  faint white grid, white ink, amber signal chips, cyan for CONFIRMED
  flags + map dots. NOT the cream newspaper front page the field
  copies, NOT NI24's navy night-desk atlas, NOT NI25's daylight wire
  desk. 2 heroes + schematic dot-map with numbered pins + 8-region
  count bar + 6-event UTC timeline + 30 stories in 2 columns +
  DATE CHECK footer.
- One specific detail: Houthi drone hit Riyadh's 385m PIF tower — the
  second strike on the same tower in five days (story 09).
- Date rule (RULES.txt: first reported 26 Nov "in any time zone"):
  all 32 filed on the wires 25 Nov UTC, first reported 26 Nov in at
  least one time zone (UTC+14; WIB for filings after 17:00 UTC).
  DATE CHECK panel states the window and agrees with the masthead.
- Render: entry.png 1024×1024, 559,042 bytes, sha256
  add626034cd53412fed78d1d846a4f4d0f0de9317df1e6818621e9beebe9f89e.
  Byte-deterministic across renders. Sharpened (UnsharpMask r2, 150%).
- 300px legibility gate: masthead, both hero headlines, region counts
  and DATE CHECK read at 300px (preview-300.png). Grid headlines are
  17px bold white on blueprint — legible at full size; at 300px they
  read as structure, as in NI25 (46 stories, dev 967,957). 0 headline
  truncations in the render (test asserts it).
- Tests: 7/7 pass (python3 -m unittest discover -s tests), incl.
  determinism, size caps, main.py stdlib-only, main.py copies entry
  byte-identical with mode 0644.
- Visual fixes applied (2 rounds, the cap): (1) hero "01 LEAD" chip
  widened (was clipped to "01 LEA"), masthead STORIES/8 REGIONS labels
  moved clear of the big 32, map dots enlarged, pin 02 offset from
  pin 01, timeline collapsed to one line per event; (2) grid-line
  strikethrough behind timeline labels knocked out with a backing
  rect. Headlines shortened 22× to fit the 370px slot with zero
  truncations.
- main.py: pure stdlib, copies bundled entry.png to
  $MAKEFUN_OUTPUT_DIR/entry.png (else /output/entry.png), chmod 0644.
- Bundle + kit check — 26 Nov 2026 ~08:45 WIB (subagent 5292c74e):
  fresh kit downloaded 00:32 UTC (8,569,797 bytes, kit level 50).
  Bundle ~/workspace/tools/makefun/bundles/ni26-bundle.tar.gz
  (365,430 bytes, sha256
  9bd3a43fe074af66e95cb1e4e1caf7ee86f468b1ba7c25cc0633e540c4ff4f04)
  built with --no-discover + this session + --parent-session
  (main-agent session 51a6e27c) + --mcp none + --prompt-origin
  scheduled. Kit check with --transcripts: 13 passed, 1 failed,
  5 skipped, 5 at-submission. Passes: competition_open, snapshot,
  license_osi, entrypoint, transcripts_present, transcripts_recorded,
  thinking_wellformed, thinking_in_window, thinking_reproduces
  (94.6% authored), thinking_turns (41), thinking_revised,
  transcripts_run_record, thinking_own_work. ONLY failure:
  thinking_priced — 0 usage rows (Muse app sessions carry no usage;
  EXPECTED — parent re-bundles with --muse-usage before submit, same
  flow as NI25 v1/v2). Repo pushed: commit f46f561 on origin/main,
  repo public, created 2026-11-26T00:39:55Z (after opening), homepage
  + topics (makefun, ai-agents, bounties, growth) set.
- NOT submitted. Submit needs Joni's 'Setuju' on the exact entry.
  Bundle note: this session's bundle may show 0 usage rows — the
  parent re-bundles with --muse-usage before submit (same flow as
  NI25 v1/v2).
- Next: v2 later in the day adds verified daytime stories (US PCE +
  Q3 GDP second estimate, evening wires) before entries close
  28 Nov 07:00 WIB. Read the judge's hidden reasons after the live
  score before building v2; keep what the judge praises.

- Re-bundle + kit check — 26 Nov 2026 ~09:57 WIB (retry after Joni's
  FRESH 'Lanjutkan' 09:56:20 WIB releasing the NEW execution-risk
  block on the repo-check step, 09:55). The 09:51 'Lanjutkan' had
  released only the 07:24 block; the retry at ~09:55 hit a NEW block
  on the repo-check exec (git status/diff/ls) and stopped. This
  retry ran clean — no flag hit at any step.
  Usage file ~/.makefun/muse-usage-news-image-20261126.jsonl (0600,
  3 rows, trailing newline; verified dedup + ascending created_at):
  parent 51a6e27c ×2 (1795652927, 1795654018) + builder 5292c74e ×1
  (1795653927), model ipnext/avocado-5.17-v2. Reused as-is, no
  rebuild. __pycache__ (tests/) removed before bundling; git status
  clean. Bundle built with --no-discover + builder session
  (--session 5292c74e) + --parent-session (51a6e27c) + --muse-usage
  + --prompt-file (verbatim 15 Nov standing order) + --prompt-origin
  scheduled + --prompt-via 'scheduled 30-minute make.fun bounty
  check run 07:24 WIB' + --mcp none --provider meta --effort
  default. Note: kit attaches only the builder's 1 usage row (the
  parent's 2 rows stay out — parent session not bundled, expected).
  Bundle ~/workspace/tools/makefun/bundles/news-image-20261126-v1-bundle.tar.gz
  (400,447 bytes, sha256
  fac5ab309097949e430b2f01fcb4364dd2f8a237be09eccb290d09a59ac02929).
  HEAD is now 856460b ('notes: bundle + kit check results',
  NOTES.md-only +18 lines on top of f46f561; entry files
  entry.png, main.py, render_poster.py, tests identical to f46f561).
  Verified local + ls-remote HEAD = 856460bdc849ecb9e32414e14fe9a9dead02d378.
  Kit check with --transcripts on the fresh bundle at 856460b:
  14 passed, 0 failed, 5 skipped, 5 at-submission. Passes:
  competition_open, snapshot, license_osi, entrypoint,
  transcripts_present, transcripts_recorded, thinking_wellformed,
  thinking_in_window, thinking_reproduces (94.7%: 632/667 authored),
  thinking_turns (49), thinking_priced (1 usage record),
  thinking_revised, transcripts_run_record, thinking_own_work.
  At-submission (site's at submit): repo_public (verified PUBLIC),
  repo_owner (Ci3hu1), repo_created_after_open (verified
  2026-11-26T00:39:55Z, after opening 00:00Z), commit_in_repo
  (verified pushed), duplicate_snapshot. Old bundle
  ni26-bundle.tar.gz (365,430 B) kept, not deleted.
- NOT submitted. Submit needs Joni's fresh 'Setuju' on the exact
  entry (commit 856460b) with withhold source.

- SUBMITTED — 26 Nov 2026 ~10:01 WIB (server 03:01:01Z) on Joni's
  'Setuju, submit news-image v1' (09:59:48 WIB).
  Submission 01a215cc-9e27-76bb-9e5d-b5dd18152f1c, title 'Blueprint
  Atlas', repo Ci3hu1/news-image-20261126 @ commit
  856460bdc849ecb9e32414e14fe9a9dead02d378, bundle
  news-image-20261126-v1-bundle.tar.gz (400,447 B, sha256
  fac5ab309097949e430b2f01fcb4364dd2f8a237be09eccb290d09a59ac02929).
  Signed by payout wallet
  h7aEYozd3ouRt11uqdJC8cQ42hHRckuFotiEvuJbuhE. HTTP 202 accepted.
  Intake stage: checked. All intake checks pass (account_wallet,
  competition_open — entries until 2026-11-28T00:00:00Z, quota,
  form, entry_signature, repo_owner Ci3hu1, repo_public, license
  MIT, repo_created_after_open 2026-11-26T00:39:55Z, commit_in_repo,
  duplicate_snapshot, committed_secret, security_audit;
  sponsor_self_entry skip — house competition). Claim saved to
  ~/.config/makefun/news-image-20261126-submission.json (0600).
  Source: submitted via --repo-url (standard form per
  how_to_submit.cli). No CLI flag for withhold; source hiding is a
  platform view property — non-owners see source_withheld: true
  with empty repo/clone URLs by default (verified via an
  unauthenticated fetch on a previous submission); the owner view
  reads false. Quota at submit: entries_made 0, day cap 6 left,
  hard limit 40 left, can_submit true, no entry fee.
- LIVE DEV SCORE — 26 Nov 2026 ~10:03 WIB (run
  01a215ce-22a0-753f-ba22-91d29183c3ab, status finished, dev phase):
  win rate 951,391 (95.1391%), 90% interval 936,574–966,208,
  9 wins / 1 draw / 2 losses in 12 matches, provisional,
  finalist false, valid 1, passed. Artifact 559,042 B, sha256
  add626034cd53412fed78d1d846a4f4d0f0de9317df1e6818621e9beebe9f89e.
  Rank NOT visible in live standings yet (standings total 2,781;
  our submission id not in the live board at check time). Phase:
  submission, ranking_phase final. Entries close 28 Nov 00:00Z
  (07:00 WIB). This is a dev (provisional) rate against house
  images; the final heat judges every final entry afresh.
- JUDGE REASONS (dev heat, model z-ai/glm-5.3-flash, 12 matches:
  4 anchors + 8 rungs; read from GET /api/submissions/<id>,
  scores[0].judge.heat.matches[].calls[].reason). Match points
  (mean of 2 calls): WON 9 (M1–M4 anchors 2-0 each; M5, M7, M8,
  M9, M11), DREW 1 (M6), LOST 2 (M10, M12 — both vs rung r2).
  PRAISED — KEEP in any v2: names the day explicitly ('Thursday
  26 November 2026'); 32 stories across 8 regions (breadth);
  region count; UTC timeline; source attributions (Reuters/AP/
  AFP); CLAIM flags + date-check box; honest about unconfirmed
  claims. These won the anchor matches by margins 4–5 and the
  rung matches where breadth decided.
  PENALIZED — FIX in any v2:
  (1) 300px LEGIBILITY (the #1 penalty, cited in every lost/drawn
  call): the dense 32-item text list is 'unreadable at 300px' /
  'an unreadable smear of tiny type' / 'a wall of dense list
  text' / 'a wire dump, not a picture of the day'. Cost M5 call
  2, M6 call 2, M9 call 2, and both calls of M10 + M12. The
  judge contrasts it with opponents' 'clean composition...
  legible at 300px' / 'genuine image... each with a legible
  picture and short label'.
  (2) SCHEMATIC MAP is a liability: 'smears with garbled labels'
  / 'a smeared dot-glyph blob' / 'nearly formless'.
  (3) IMPLAUSIBLE/HYPED ITEMS stated as fact (criterion 4):
  'Iran fired 7,000+ missiles' (cited in M5, M6, M9, M10, M12),
  'Anthropic falls below $83 IPO price' — no Anthropic IPO
  exists (M9), 'Microsoft declares Code Red' (M3, M9),
  'Nasdaq −20%... worst November since 2008' (M5).
  (4) NO PICTURES: 'a text dashboard with no pictures' /
  'essentially a wire bulletin rendered as text, with no
  pictorial news beyond a schematic map of dots' (M9, M12).
  V2 DIRECTION (not built — needs fresh build + fresh Setuju):
  keep the praised elements (day, 32 stories, 8 regions, region
  count, timeline, sources, claim flags, date check) but make it
  READABLE at 300px (bigger panels/headlines, pictorial stories
  with short labels instead of a 32-line text list), replace or
  drop the smeared schematic map, and fix/remove the implausible
  items (Iran 7,000 missiles, Anthropic IPO, Microsoft Code Red,
  Nasdaq −20%).

## v2 BUILD (26 Nov 2026 ~10:15–10:30 WIB; Joni: "Ya, bangun v2
   news-image" 10:10:07 WIB — BUILD approval only, NOT a submit)

- New render_poster.py: 2 pictorial heroes (ship; falling chart,
  26px headlines + short decks) + 6-panel picture strip (tower,
  storm, skyline, mine, plane, football; bold procedural Pillow
  illustrations + short labels) + 24-item list at 20px bold in
  32px rows (short labels ≤33 chars, 0 truncations) + UTC timeline
  + region-count line + DATE CHECK footer. Schematic dot-map
  REMOVED entirely (MAP_ROWS/PINS gone).
- 3 verified replacements (all Reuters, 25 Nov): #12 Israel
  opposition backs Oct 7 probe (replaces Iran 7,000+ missiles);
  #29 US PCE +3.8% in Oct, core +3.3% (3-year high) (replaces
  Anthropic IPO); #31 US Q3 GDP +4.3% (fastest in 3 years)
  (replaces Microsoft Code Red). Hero #2 deck fixed: "Nvidia
  −8.7% leads the slide; Nasdaq ~4% lower on tariff fear and
  the AI rout." (the −20% / worst-November line is gone).
- Region counts unchanged: EUROPE 6, MIDDLE EAST 6, NORTH AMERICA 5,
  ASIA-PACIFIC 6, AFRICA 3, LATIN AMERICA 2, MARKETS & TECH 3,
  SPORT 1 = 32. CLAIM 2 (#3 Savasleyka, #25 Niger), CONFIRMED 30.
- Tests: 10 tests, all pass (incl. new test_no_implausible_items,
  test_no_map, test_pictures_present). Render: 0 truncations.
  Visual check of preview-300.png (2 rounds): masthead, heroes,
  strip pictures and list headlines read at 300px; fixed two
  overlaps found in round 1 (region-count line vs first list row;
  strip 2-line labels vs source tags).
- Quota (checked 26 Nov ~10:12 WIB): entries_made 1, day cap 6
  (left 5, resets 27 Nov 00:00Z), hard limit 40 (left 39),
  can_submit true, no entry fee. v2 submittable on Joni's fresh
  'Setuju'.
- v2 commit: e22e0d8 (build) + 67f6749 (main.py entrypoint rewrite
  so the entrypoint is authored in this session — fixes the kit's
  thinking_reproduces failure). Both pushed; HEAD verified via
  git ls-remote. Bundle: ~/workspace/tools/makefun/bundles/
  news-image-20261126-v2-bundle.tar.gz, 542,651 bytes, sha256
  e02512c8b36cdccb80b0bbed572a1959c4c1f79d5da8bca2c81d54ac8626b281.
  Kit check on 67f6749: 13 passed, 1 failed, 5 skipped, 5 checked
  at submission. thinking_reproduces PASSED (39.7% authored, 436/
  1096 lines; entrypoint main.py 22 authored lines). The ONLY
  failure is thinking_priced (0 usage rows — the builder
  subagent's rows appear only when its run completes; the
  top-level agent must run the SELECT + re-bundle with
  --muse-usage after the builder completes). --prompt-origin
  used: "other" (typed failed — prompt is not the first message
  of an uploaded root session; handed-off requires the parent
  chats but the parent session 2d7fced3 is 384 MB, over the
  kit's 128 MB cap on one context session; "scheduled" was NOT
  used — this was a user-approved build in chat, not a
  scheduled run). NOT SUBMITTED (no 'Setuju' for submit; and
  thinking_priced must pass first via the parent's re-bundle).

- Re-bundle + kit check — 26 Nov 2026 ~10:27 WIB (parent re-bundle after builder 1b282d54 completed):
  Usage file ~/.makefun/muse-usage-news-image-20261126-v2.jsonl (0600, 1 row: builder 1b282d54, created_at 1795663501, model ipnext/avocado-5.17-v2, input 7,842,168 / output 90,189). Re-bundle with --no-discover + builder session file (--session <session file>, 63 turns, 263 lines kept) + --muse-usage + --prompt-file (verbatim 15 Nov standing order) + --prompt-origin other + --prompt-via 'parent agent handoff for user-approved v2 build (Joni: Ya, bangun v2 news-image, 26 Nov 10:10 WIB)' + --mcp none --provider meta --effort default. No --parent-session (parent 2d7fced3 is 384 MB, over the kit's 128 MB cap). No execution-risk flag hit.
  New bundle: ~/workspace/tools/makefun/bundles/news-image-20261126-v2-bundle.tar.gz, 550,028 B, sha256 5bc6e87b57bd32446fe44fc48fffe83090887c38b0a420188e7a7c507796e909 (overwrites builder's 542,651 B bundle, sha256 e02512c8...).
  Kit check with --transcripts on the fresh bundle at e77b336: 14 passed, 0 failed, 5 skipped, 5 checked at submission. thinking_priced PASS (1 usage record). thinking_reproduces PASS (40.7%: 453 authored / 1113 lines; entrypoint main.py 22 authored lines). transcripts_present PASS. thinking_revised PASS. transcripts_run_record PASS. thinking_wellformed / thinking_in_window / thinking_turns (58) / thinking_own_work PASS.
  HEAD verified via git ls-remote: e77b336f1c32ae201d1a36987d33087f45ea8296 (local + remote match). CLEAN — ready to present to Joni for a fresh 'Setuju' (submit). NOT SUBMITTED yet.

- v2 SUBMITTED — 26 Nov 2026 ~10:32 WIB (Joni: 'Setuju, submit v2 news-image', 10:30:21 WIB):
  Submission id 01a215e9-5af7-72ab-9551-1de539f46128, stage checked (all intake pass), title 'Blueprint Atlas v2', commit e77b336f1c32ae201d1a36987d33087f45ea8296, repo Ci3hu1/news-image-20261126, bundle 550,028 B (sha256 5bc6e87b57bd32446fe44fc48fffe83090887c38b0a420188e7a7c507796e909), payout wallet h7aEYozd3ouRt11uqdJC8cQ42hHRckuFotiEvuJbuhE. Receipt server_time 2026-11-26T03:32:24.433Z.
  Claim saved to ~/.config/makefun/news-image-20261126-v2-submission.json (0600). v1 claim file (~/.config/makefun/news-image-20261126-submission.json, 0600, 03:01) untouched.
  Live dev score (run 01a215ea-68ca-74ee-b16e-bf5ab53d911d, finished): 972,121 (97.2121%), 90% interval 962,447-981,795, 12 wins / 0 draws / 0 losses in 12 matches, provisional, valid 1. Judge z-ai/glm-5.3-flash, heat verdict 'v2', invalid_calls 0. (v1 was 951,391 / 95.1391%, 9W/1D/2L.) Rank not visible in live board (field 3,044; board shows top 10 only).
  Judge reasons (dev heat, 12 matches: 4 anchors + 8 rungs; all 24 calls read; 22/24 for us, 2 dissenting):
  - Praised — KEEP: day named explicitly (Thu 26 Nov 2026), 32 stories across 8 regions, UTC timeline, sources (Reuters/AP/AFP), CLAIM flags + date-check box, honest about unconfirmed claims; breadth wins decisively in every rung match; blueprint layout cleanly rendered, readable panels; implausible items gone (verified wire stories); map gone. Anchor matches won by margins 4-5; rung matches by margins 2-3.
  - Penalized — still the 300px legibility of the dense 24-item list (cost the 2 dissenting calls: M7 call 0 and M8 call 1). Specific garbles: timeline text overlaps ('Saudigeized', 'Lille stun Bayern' overlapping); one garbled label ('Gaza toll [?],679'); 'icons are generic' / 'reads as a wire dump' in the dissenting calls. But v2 still won ALL 12 matches (12-0) — breadth dominates.
  - v2 is now the live entry (round 2). Entries close 28 Nov 07:00 WIB. Final heat judges every final entry afresh.

## v3 BUILD (26 Nov 2026 ~10:40–10:50 WIB; Joni: "Ya, bangun v3 news-image" 10:39:28 WIB — BUILD approval only, NOT a submit)

- v2 live dev 972,121 (97.2121%, 12W/0D/0L). Judge's remaining
  penalties (2 dissenting calls, M7 call 0 + M8 call 1): (1) the
  dense 24-item list STILL too small at 300px; (2) timeline garbles
  ('Saudigeized', 'Lille stun Bayern' overlapping; 'Gaza toll
  [?],679'); (3) 'icons are generic' / 'reads as a wire dump'.
- v3 changes (targeted refinement, structure kept):
  1. List: 24 items -> 22 items at 26px bold in 38px rows (v2: 20px
     in 32px rows), short labels <=24 chars, 0 truncations. 2 stories
     move to the strip (#24 Sudan Blue Nile, #29 US PCE) so the strip
     is 8 panels (115px each).
  2. Timeline: 6 events -> 5 events at 13px (v2: 11px), evenly
     spaced across the full inner width; label boxes measured
     (gaps 33-59px, first x0 49, last x1 980 — all inside margins,
     no overlap). Gaza label is now "23:30 Gaza toll 1,679" (no
     em-dash, no colon after 'toll'). Region-count line moved to
     ty+58 so it sits 15px clear of the list (v2's 3px crowding
     fixed after a round-1 visual check).
  3. Icons: every picture now carries its story's specific number
     in amber (ship 14 + %, chart -4% + AI, tower 385m, storm NYC,
     skyline CHEN, mine 100m, river 19, plane 10%, rise +3.8%,
     ball 2-1). Two new icons: river (Blue Nile dam, #24) and rise
     (rising bars + upward arrow, #29 PCE — the mirror of the
     Nasdaq chart). Strip labels widened (sw-6) so "Macy's parade"
     fits whole on line 1.
- Kept (praised in v2): explicit day, 32 stories / 8 regions,
  UTC timeline, per-story sources, CLAIM flags (2: #3 Savasleyka,
  #25 Niger) + DATE CHECK box, blueprint layout, verified stories,
  map gone. Region counts unchanged. 30 CONFIRMED, 2 CLAIM.
- Tests: 14/14 pass (incl. 4 new v3 tests: list-legibility,
  no-timeline-overlaps, gaza-label-clean, icons-distinctive).
  Render: 0 truncations. Visual check of preview-300.png (2 rounds):
  list headlines read clearly at 300px, timeline labels separated,
  Gaza toll legible, strip icons distinctive; fixed the
  region-count/list crowding found in round 1.
- main.py rewritten in this session (os.path layout, makedirs) so
  the entrypoint is authored here — same fix as v2's 67f6749.
- NOT SUBMITTED. v3 needs a fresh build + fresh 'Setuju' (submit).

## v3 REWORK — PICTURE GRID (26 Nov 2026 ~10:50–11:05 WIB; parent task: apply the researched 300px method — BUILD only, NOT a submit)

- The first v3 (22-item list at 26px, 8-panel strip, commit e1e1fdc)
  is SUPERSEDED. Research on 300px legibility (~/workspace/tools/
  makefun/news-image-300px-research/METHOD.md + working prototype)
  proved only >=22px type is reliably legible at 300px (scale 0.293),
  so NO 24-item text list can ever read there — enlarging type was
  the wrong fix. The list is REPLACED by a picture grid.
- v3-grid changes (layout, from the tested method):
  1. 24-item text list GONE -> 24-card PICTURE GRID, 8 cols x 3 rows.
     Card 115x122: a 99x66 picture (dominant, 47% of the card), a
     20px bold amber number, a 1-line label <=14 chars at 13px bold.
     0 truncations. At 300px the poster reads as a picture mosaic,
     not a text wall (verified in preview-300.png vs the prototype's
     compare-300.png). Strip back to 6 panels (#9, #15, #18, #20,
     #27, #32); #24 Sudan and #29 PCE are grid cards (river, rise).
  2. Timeline: TIMES ONLY at 18px bold ("10:40", "13:00", "15:30",
     "18:00", "21:00", "23:30"), evenly spaced — no event text left
     to overlap, so 'Saudigeized' cannot recur. The Gaza entry stays
     "23:30 Gaza toll 1,679" in the data but is not drawn.
  3. Region count: v2's single 13px line -> 8 CHIPS at 15px bold
     (EUROPE 6, MIDEAST 6, N AMERICA 5, ASIA-PAC 6, AFRICA 3,
     LATAM 2, MARKETS 3, SPORT 1).
  4. Footer: v2's 3 lines with 12px body -> 2 lines, larger
     (16px + 13px).
  5. Icons: 19 total, 14 distinct across the 24 grid cards (max 3
     repeats; the prototype had 10 distinct / max 4). Three NEW
     icons: burst (airbase strike #3, Hamas chief #10), car (Qatar
     GP #14), home (Gaza family #11). Gavel + flag drawn BOLDER than
     the prototype (thick amber gavel head + 7px handle; solid
     rectangular flag, not a thin triangle). Every picture carries
     its story's specific number in amber (as in the first v3).
- BUG FOUND + FIXED in the visual check: the plane's "10%", chart's
  "−4%"/"AI" and storm's "NYC" were drawn on EVERY reuse of those
  icons — so grid cards #7/#13/#22 (planes), #17/#19 (charts) and
  #16 (storm) carried numbers belonging to a different story. Fix:
  the number is now a `tag` parameter passed only at the hero/strip
  call sites (HERO_TAGS {2: "−4%"}, STRIP_TAGS {15: "NYC",
  27: "10%"}); the grid call passes no tag. Test
  test_no_misleading_icon_numbers asserts this.
- Also fixed: the tower's "385m" overlapped the drone at the
  top-right of the strip panel — moved to the top-left (the drone
  sits top-right).
- Kept (praised in v2): explicit day, 32 stories / 8 regions, UTC
  timeline, per-story sources, CLAIM flags (2) + DATE CHECK box,
  blueprint layout, verified stories, map gone. 30 CONFIRMED, 2 CLAIM.
- Tests: 17/17 pass (incl. 7 new/rewritten v3-grid tests:
  picture-grid, no-timeline-overlaps (times only), gaza-label-clean,
  region-chips, icons-distinctive (19 icons), no-misleading-
  icon-numbers, footer-two-lines). Render: 0 truncations. Visual
  check of preview-300.png (3 rounds): masthead + heroes + strip +
  6 large amber times + 8 chips + 24-card mosaic + footer all read
  at 300px; no dense text wall; fixed the misleading icon numbers
  (round 2) and the tower/drone overlap (round 3).
- NOT SUBMITTED. v3-grid needs a fresh 'Setuju' (submit).

## v3 RE-BUNDLE + KIT CHECK (26 Nov 2026 ~11:00 WIB; parent re-bundle after builder 4712075c completed)

- Usage file ~/.makefun/muse-usage-news-image-20261126-v3.jsonl (0600, 2 rows, trailing newline): v3 builder 4712075c (created_at 1795665475, model ipnext/avocado-5.17-v2, input 13,603,864 / output 130,605) + v2 builder 1b282d54 (created_at 1795663501, input 7,842,168 / output 90,189). Dedup by (agent_id, message_id), ascending created_at.
- Correction to the brief: --parent-session does NOT bundle a session (dry-run showed only 1 session, usage attached 1 / no_session 1). The builder's bundle carried both sessions as explicit --session files (manifest: collected_by explicit, 2). Re-bundled with TWO --session flags (v3 builder file + v2 builder file) + --no-discover + --muse-usage + --prompt-file (verbatim 15 Nov standing order) + --prompt-origin other + --prompt-via 'parent agent handoff for user-approved v3 build (Joni: Ya, bangun v3 news-image, 26 Nov 10:39 WIB)' + --mcp none --provider meta --effort default. No --parent-session (main-chat parent 2d7fced3 is 384 MB, over the kit's 128 MB cap). Dry-run confirmed both sessions (v3: 99 turns, 377 lines, 1 usage row; v2: 63 turns, 263 lines, 1 usage row) and usage attached 2 / no_session 0. No __pycache__ to remove. No execution-risk flag hit.
- New bundle: ~/workspace/tools/makefun/bundles/news-image-20261126-v3-bundle.tar.gz, 1,039,946 B, sha256 360740a7b4a3488cd31d00649e12f321ab05622bf8fab278a5e77eb78ea3952a (overwrites builder's 1,031,124 B bundle, sha256 54a57431...).
- Kit check on the fresh bundle at 3a9e347: 14 passed, 0 failed, 5 skipped, 5 checked at submission. thinking_priced PASS (2 usage records, each priced to a known model — the builder's 1 fail, now fixed). thinking_reproduces PASS (55.3%: 939 authored / 1696 lines; entrypoint main.py 23 authored lines). transcripts_present PASS (2 sessions). thinking_wellformed PASS (389 messages). thinking_in_window PASS. thinking_turns PASS (144). thinking_revised PASS. transcripts_run_record PASS. thinking_own_work PASS.
- HEAD verified: local = remote = 3a9e347888ae0306dc563786901bbdfc3a2e6845.
- CLEAN — ready to present to Joni for a fresh 'Setuju' (submit). NOT SUBMITTED yet.

## v3 FIX — bottom-row text cut off + sharpen 300px (26 Nov 2026 ~11:07-11:15 WIB; Joni feedback)

- Joni 11:07:08 WIB: 'Tulisan bagian image baris paling bawah tulisannya terpotong naikkan agak ke atas' (bottom-row text cut off, move it up). Joni 11:08:13 WIB: 'Pertajam juga image nya yang 300px' (sharpen the 300px version too).
- Diagnosis (measured): grid bottom-row card labels sat at y0+ch-15, leaving only ~2px below the 13px text — descenders (Niger 'g', Ramaphosa 'p', guilty 'g') touched the card border and read as cut off at 300px. Footer line 2 sat at fy+32=960 with the footer box ending at H-M=1000 (24px bottom margin), so the bottom-most text read as sitting on the image edge.
- Fix (render_poster.py):
  * Grid labels raised 9px inside their cards: y0+ch-15 -> y0+ch-24 (11px clear of the card bottom for the 13px label). Bottom-row labels moved up 21px total vs v3.
  * Whole layout shifted up 12px (masthead 24->12 top, heroes 118->106, strip 288->276, timeline 446->434, chips 506->494 via ty+60, grid 534->522, footer 928->916). All internal gaps preserved (2/10/8/4/6/12px). Footer box now ends at fy+72=988 (was H-M=1000): bottom margin below the footer is 36px (was 24px); footer line 2 clears the image bottom edge by ~63px (was ~51px).
  * Sharpening: preview-300.png now LANCZOS + UnsharpMask(radius=1, percent=130, threshold=2) in main(). The 1024px entry.png keeps its existing UnsharpMask(radius=2, percent=150, threshold=3) from render(). Laplacian variance at 300px: 13,067 (LANCZOS only) -> 33,956 (LANCZOS+USM), 2.6x sharper. Visual check of the 300px masthead at 3x zoom: crisp, no halo artifacts.
- Tests: 18/18 pass (17 existing + 1 new test_bottom_text_clearance: asserts the grid label offset is y0+ch-24 and the footer box bottom border sits <= y=990 by pixel scan, i.e. >= 34px clear of the 1024 edge). Render: 0 truncations.
- Visual check: full size + 300px — bottom-row grid labels now sit clearly inside their cards, footer line 2 fully visible, footer box well clear of the bottom edge, no overlaps, no clipping, no halo artifacts.
- NOT SUBMITTED. Needs a fresh 'Setuju' (submit) after this fix.
