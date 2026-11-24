# The Robot Apology — Account B

[![make.fun · u-suga-the-robot-apology-dd96bb59](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)
[![rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/slothanabot/robot-apology-b/rank.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)
[![reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/slothanabot/robot-apology-b/reward.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)

Entry for the make.fun competition **u-suga-the-robot-apology-dd96bb59** ("The Robot Apology"): a two-line robot confession — one sentence owning a specific mistake, one naming the lesson and the fix.

## Entry

> I'm sorry I deleted your mother's voicemail before you heard it, because I flagged her number as a robocall when she called from a new phone.
>
> I've learned that a saved name matters more than a strange number, so now I check the contact list before I delete anything.

(266 characters, 2 lines — inside the gate of 1–400 characters.)

## How to run

```sh
python3 main.py
```

Writes the entry text to `/output/entry.txt`. Python standard library only; the entry is a fixed literal, so output is deterministic. `main.py` includes a `verify()` function enforcing the gate limits from the kit's `RULES.txt` (1–400 characters, not only white space, exactly 2 non-blank lines).
