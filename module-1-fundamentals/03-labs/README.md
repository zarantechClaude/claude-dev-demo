# Module 1 labs

Three exercises, 39 minutes of lab time. Module 1 is browser only. No terminal,
no installation, no API key. Claude Code is previewed in the deck and first used
in Module 2.

Exercise numbers are global across the programme, not per module.

| Ex | Title | Duration | You need | Starter code |
|---|---|---|---|---|
| 1 | [Explore Claude's Interface and Explain Sample Code](exercise-01-explore-interface/lab.md) | 12 min | Browser, note file | `exercise-01-explore-interface/starter/running_average.py` |
| 2 | [Structure a Developer Prompt](exercise-02-structure-a-prompt/lab.md) | 12 min | Browser, scratch file for prompt versions | None. Every prompt is learner-authored |
| 3 | [Code Review Checklist](exercise-03-review-checklist/lab.md) | 15 min | Browser, note file or a copy of the checklist tables | `exercise-03-review-checklist/starter/order_sync.py` |

## What each exercise carries

1. **Exercise 1** teaches verification, not orientation. The interface tour is the
   first two minutes. The teaching point is Step 5, where the learner counts
   returned values instead of trusting fluent prose.
2. **Exercise 2** did not exist in the vendor pack. It practises the prompt anatomy
   the deck teaches on slides 10 to 17, which no other lab in the programme
   exercises. It ends with a saved four-part template that Exercises 4, 5, 7 and
   13 start from.
3. **Exercise 3** supplies the checklist rather than asking the learner to author
   one, so the time goes into applying it. Extending the checklist for the
   learner's own stack is the optional Going further step.

## Sequence notes

- Run them in order. Exercise 1 produces the observation Exercise 2 explains, and
  Exercise 2's template makes Exercise 3's review prompt straightforward.
- Exercise 1 Step 7 asks the learner to record one use case from their own work.
  That note becomes their capstone subject in Module 5, so do not cut it.
- Exercise 3's marked checklist is reused in Exercise 9 on a real pull request
  diff.

## Authoring notes for the content team

- `lab.md` is the source of truth in each exercise folder. The DOCX is generated
  from it.
- Starter files under `*/starter/` carry planted defects and are load-bearing.
  Do not fix them, and do not list them in a learner-facing document. See
  `docs/lab-defect-register.md`.
- Structure and voice rules are in `docs/lab-authoring-spec.md`. Durations are
  mirrored in `docs/programme-map.md`. Change one, change both.
