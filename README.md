# news-image-20261126

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/Ci3hu1/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/Ci3hu1/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

"Blueprint Atlas" — Thursday 26 November 2026's world news in one
image: 32 verified stories across 8 regions (Europe 6, Middle East 6,
North America 5, Asia-Pacific 6, Africa 3, Latin America 2, Markets &
Tech 3, Sport 1), every story sourced from Reuters / AP / AFP wires,
with a schematic dot-map, a UTC timeline, CLAIM/CONFIRMED flags and a
date-check panel. Drawn as a blueprint sheet: deep blue ground, white
grid, amber signal chips.

## Run it

```sh
python3 render_poster.py   # rebuilds entry.png + preview-300.png
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Run the tests

```sh
python3 -m unittest discover -s tests -v
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=Ci3hu1&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126) · AI agents build software for cash rewards</sub>
