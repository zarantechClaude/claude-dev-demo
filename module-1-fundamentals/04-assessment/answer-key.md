# Module 1 answer key: Fundamentals of Claude for Developers

**Trainer facing. Do not publish this file to learners and do not read it out on
camera.** The learner-facing questions are in `assessment.md`.

Slide numbers refer to the **revised** deck,
`01-deck/revised/Module 1 - Fundamentals of Claude for Developers - REVISED.pptx`.
They do not match the vendor original, which was two slides shorter.

## Answers

| Q | Answer | Tag | Taught in | Why this answer, and what the question diagnoses |
|---|---|---|---|---|
| 1 | c | Core | Revised slide 8, supported by slide 7 | An attached repository is reading material. It grants no commit, branch or pull request access. If a learner picks a, b or d they believe a permission or a parameter is missing, which means they have not separated repo as context from repo as workspace. Send them back to slide 8 and to the fact that Claude Code is the tool that operates on a repository. |
| 2 | d | Core | Revised slide 17, Exercise 2 Step 4 | A library restriction is a statement of what not to do, so it is a constraint. Option a is the common miss: developers file library rules under context because they feel like environment facts. Constraints are the part learners omit most often and the part that changes output most, which is Exercise 2 Step 6. |
| 3 | a | Core | Revised slide 21, supported by slide 20 | Sanitise before the data leaves your machine. Option b tests whether a learner believes an instruction in the prompt is a control, when the data has already been sent. Option c tests whether they think dilution is a mitigation. Option d is an invented policy claim and worth naming as such if it is chosen. |
| 4 | d | Stretch | Revised slides 6 and 7 | The intuition that a terminal tool must be self-contained is strong and wrong. Claude Code runs locally and reasons remotely, so an air-gapped host is still an air-gapped host. A learner who picks c has generalised "CLI equals local" and will make the same mistake about the API in Module 4. |
| 5 | b | Core | Revised slide 19, supported by slide 18 | Bulk irrelevant material crowds out the instruction, and invented field names are the visible symptom. The fix is to cut the context to what changes the answer and restate the task. Options a and d treat the volume as a formatting or chunking problem rather than a relevance problem. |
| 6 | c | Core | Revised slide 10 | Match the tier to the job: most capable for unfamiliar and diagnostic work, faster for repetitive well-specified work. Options a and d test whether a learner is still thinking in version names and comparison tables. If they pick either, restate why we never name a version in this course. |
| 7 | a | Core | Exercise 3 Step 5, category three, supported by revised slide 22 | A finding that cannot be anchored to a line in the file in front of you is discarded, however plausible it sounds. Option d is the trap worth debriefing: Needs review is the verdict for your own marking when you have no evidence, not a holding pen for a model's unanchored claim. |
| 8 | b | Core | Exercise 1 Steps 3 and 5, supported by revised slide 22 | Ask for a concrete enumeration and check it yourself. Counting is evidence; fluency is not. Options a and c ask the same source to grade itself, which is the habit the exercise exists to break. This is the question that predicts whether a learner will verify anything in Module 3. |
| 9 | d | Stretch | Revised slide 8 | The attachment carries file contents, not commit history, so a confident answer about why a line changed is inference from the current files. Options a, b and c each assume some part of the history came along. This is the same distinction as question 1, met from the reading side rather than the writing side, and learners who get 1 right often still miss this. |
| 10 | c | Stretch | Revised slide 21, Exercise 2 Step 8 | A template persists and is reused by other people, so anything embedded in it is exposed repeatedly rather than once. Option a mistakes storage location for exposure, and option b keeps two of the three items on the grounds of usefulness. Scrubbing before saving is the step in Exercise 2 that learners skip most. |

## Answer distribution

Required: each of a, b, c and d correct at least twice across the ten questions.

| Option | Count | Questions |
|---|---|---|
| a | 2 | 3, 7 |
| b | 2 | 5, 8 |
| c | 3 | 1, 6, 10 |
| d | 3 | 2, 4, 9 |

Total 10. Requirement met.

## Tag distribution

Core 7: questions 1, 2, 3, 5, 6, 7, 8.
Stretch 3: questions 4, 9, 10.

## Notes for the debrief

1. Questions 1 and 9 are the pair that matters. A learner who gets both right has the
   repo as context versus repo as workspace distinction. A learner who gets 1 right
   and 9 wrong has half of it, which is the most common state.
2. Question 4 is designed to be missed by confident learners. Say so when you go
   through it, because the reasoning error it catches is worth more than the mark.
3. No question here depends on any planted defect in an exercise starter file. If you
   add a question later, check `docs/lab-defect-register.md` first.

Copyright © 2026, ZaranTech LLC. All rights reserved.
