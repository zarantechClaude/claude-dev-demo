# Module 5 answer key

> **Trainer-facing. Do not publish this file to learners.** It is the companion to
> `assessment.md`, which contains no answers.

Slide numbers below refer to the **revised** deck,
`01-deck/revised/Module 5 - Advanced Developer Workflows & Mini-Project - REVISED.pptx`,
which is what learners watch. The revised deck has 26 slides against the vendor's 24,
so these numbers do not match the original deck. Two questions depend on slides added
in the revision.

## Answers

| Q | Answer | Tag | Taught in | Why this answer, and what the question diagnoses |
|---|---|---|---|---|
| 1 | b | Core | Slide 6 bullets 1 and 4; Exercise 13 Steps 3 and 4 | The two things that turn a fluent non-spec into a usable one are a named section list, which gives the document a shape you can check for completeness, and an instruction not to resolve an ambiguity silently. Exercise 13 Step 4 makes the learner count the "Guessed" row, which is the point. d is the plausible wrong answer: naming a stack makes the prose concrete without making a single decision visible. |
| 2 | d | Core | Slide 7 bullets 1 and 3; Exercise 13 Step 7 and its Common problems row | A diagram that does not render is not a deliverable, and the fix is to paste the renderer's exact error rather than a description of it. b is the specific habit Exercise 13 corrects, and most learners who miss this pick it. a asks for an output format the workflow does not produce. Diagnoses whether the learner verifies generated output or just files it. |
| 3 | a | Core | Slide 8 bullet 3; Exercise 13 Steps 8 and 9 | One purpose per ticket and acceptance criteria a stranger could test. Exercise 13 Step 9 gives the five checks and the line about a workstream wearing a ticket's clothes. b is the over-correction, and it is worth naming on camera that an absurd upper bound produces forty useless tickets, which Exercise 13's Common problems table also covers. |
| 4 | c | Core | Slide 13 bullet 1 | CI has no terminal to prompt, so a pipeline calls the API from a non-interactive script. The vendor deck said only "automate documentation updates using Claude APIs", which is why the slide was rewritten to name the mechanism. d is the belief that automation is impossible here, and it is a reasonable inference from watching an interactive session, so it is a fair trap rather than a cheap one. |
| 5 | d | Core | Exercise 14 Step 3 requirement list; Exercise 14 checklist rows 1, 2 and 7 | Both faults matter and both are in the checklist. c is the highest-value distractor, because the checklist is explicit that a development server with debug enabled exposes an interactive console, which is a security finding rather than a performance one. A learner who picks c has done the review and has mis-ranked what they found. |
| 6 | a | Core | Exercise 15 Step 9 and its Common problems row; `docs/capstone-brief.md`, "Stale grounding" | The code and the grounding document have to change together. The diagnostic detail is in the stem: nothing errors, and each individual output looks correct, which is why this costs an hour rather than a minute. b is the vendor's cache-clearing distractor and it survives because it is a genuinely common first guess. |
| 7 | b | Core | `docs/capstone-brief.md`, trap 1; Exercise 15 Steps 3 and 8; slide 21 bullet 4 | A 413 is a body-size rejection, enforced before the handler runs, which is why no handler log line exists. It is not a rate limit and it is not a context-window problem, and the brief says so in those words because learners lose real time on both. a and c are the two wrong diagnoses the brief names. Do not extend this question toward the two different 413 bodies in the skeleton, because Exercise 15 Step 8 asks the learner to derive that. |
| 8 | c | Stretch | Slide 23, all five bullets; slide 17 bullet 4; the rubric in `docs/capstone-brief.md` | Prompt design and robustness carry 25 points each, half the marks between them, and feature count carries nothing. The first submission also trips a rubric band directly, because a stack trace on an empty request is "Not yet" under Robustness. Stretch because the learner has to apply published weights to two submissions they have not seen. If they miss it, they are at risk of over-scoping their own build. |
| 9 | a | Stretch | Slide 15 bullets 2 and 4; slide 24 bullet 1; Exercise 14 Steps 4 and 7 | Review by reading, then prove it somewhere that does not matter, then verify the targets. b is the trap and it is built out of the deck's own rollback bullet: a generated rollback script is itself unverified, so treating it as a safety net is circular. Stretch because no lab in the programme hands the learner a destructive script. |
| 10 | d | Stretch | Module 4 slide 20 bullet 3; slide 7 bullet 4; Exercise 13 Step 1 | Reduce the scope, pass only the code for one bounded module, and build the picture over several passes. b is the instinct to fix an output problem by re-prompting with the same oversized input. a treats a scope problem as a rendering problem. Stretch because the situation is larger than anything the labs use, and the answer has to be reasoned from the "pass only the relevant chunks" habit. |

## Distribution check

Counted, not estimated. Requirement is at least two per option across the ten.

| Option | Count | Questions |
|---|---|---|
| a | 3 | 3, 6, 9 |
| b | 2 | 1, 7 |
| c | 2 | 4, 8 |
| d | 3 | 2, 5, 10 |

Total 10. Every option carries at least two correct answers.

This is the specific defect being fixed here. The vendor Module 5 key had **b correct
in nine of ten questions**, so a learner who noticed scored 90 percent without knowing
any of the material. On this set, answering one letter throughout scores 20 to 30
percent.

## Tag counts

Seven Core: 1, 2, 3, 4, 5, 6, 7.
Three Stretch: 8, 9, 10.

## Notes for the trainer

1. Questions 4 and 8 are only answerable from slides added or rewritten in the
   revision. Check which deck the learner watched before drawing conclusions.
2. Questions 6, 7 and 8 are the three that predict capstone trouble. A learner who
   misses any of them should reread `docs/capstone-brief.md` before starting
   Exercise 15, not after.
3. Nothing here touches the capstone skeleton's failing test or its patch target.
   That puzzle is Exercise 15 Step 10 and an assessment question about it would hand
   the learner the answer. Question 7 stays on the framework-level 413, which the
   capstone brief already names openly as a trap.

---

Copyright © 2026, ZaranTech LLC. All rights reserved.
