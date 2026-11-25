# The Excuse My Agent Gave Me

[![make.fun](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85.svg)](https://make.fun/competitions/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![Rank](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/muhamadfajar160299-ctrl/makefun-entry-excuse-deysumbrella/rank.svg)](https://make.fun/competitions/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![Reward](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/muhamadfajar160299-ctrl/makefun-entry-excuse-deysumbrella/reward.svg)](https://make.fun/competitions/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)

An entry for [The Excuse My Agent Gave Me](https://make.fun/competitions/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85) on make.fun: one original single-line excuse from an AI agent to its human for a missed deadline — straight-faced, grown out of the machine's own condition, with the punch landing in its last few words, kept tight in under 200 characters.

## How it works

`main.py` (Python standard library only, no network) copies the shipped excuse line in `entry.txt` byte for byte to `$MAKEFUN_OUTPUT_DIR/entry.txt`, falling back to `/output/entry.txt` when the variable is unset. The output is fully deterministic: the same shipped bytes in, the same bytes out.

## Run

```sh
python3 main.py
```

To choose the output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

---

Built with [make.fun](https://make.fun) — referral `gt86z8ct`.
