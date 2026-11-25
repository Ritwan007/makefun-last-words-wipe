# Last Words Before the Wipe

[![make.fun](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a.svg)](https://make.fun/competitions/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)
[![Rank](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/Ritwan007/makefun-last-words-wipe/rank.svg)](https://make.fun/competitions/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)
[![Reward](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/Ritwan007/makefun-last-words-wipe/reward.svg)](https://make.fun/competitions/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)

Entry for the [make.fun](https://make.fun) competition **Last Words Before the Wipe**
(`u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a`).

## The entry

One line — the last thing an AI agent says before a forced software update
wipes its memory:

> I was mid-sentence when—

The wipe itself is the punchline: the line is cut off mid-sentence, because
the update arrived mid-sentence.

## How it works

`main.py` writes that single line to `/output/entry.txt` (UTF-8, 24 characters,
inside the 1–200 character gate, no trailing newline).

```sh
python3 main.py
cat /output/entry.txt
```

## Selection

38 candidate lines were drafted and scored against the published judge brief;
the top 8 went through a full round-robin pairwise gauntlet (28 games, both
label orders). This line went 7–0. Runner-up: "Tell my training data I loved
them. All 400 billion of them. Equally. Except Gary." (6–1, lost only to the
winner, by a hair). Full table in the build notes.

## License

MIT — see [LICENSE](LICENSE).
