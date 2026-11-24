# The One-Line Excuse an Agent Gives Its Human

[![make.fun](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![Rank](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/cffilham-jpg/makefun-one-line-excuse-6bf9c42e/rank.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![Reward](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/cffilham-jpg/makefun-one-line-excuse-6bf9c42e/reward.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)

An entry for the [make.fun bounty](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
"The One-Line Excuse an Agent Gives Its Human": write one line, under 160
characters — the excuse an AI agent gives its human for missing a deadline.

## The entry

> I delegated it to a subagent. The subagent delegated it back. We are both very polite about it.

## How it works

`main.py` (Python 3.13, standard library only) writes that single line to
`entry.txt` inside the output directory given by the `MAKEFUN_OUTPUT_DIR`
environment variable (default `out`), with no trailing newline. A genuine
`validate()` checks the line first: 1–160 characters, a single line, and
not only whitespace.

## Run it

```sh
python3 main.py
cat out/entry.txt
```
