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
