# Module 3 answer key: Debugging, Optimization and Code Reviews

**Trainer facing. Do not publish this file to learners and do not read it out on camera.**
The learner-facing questions are in `assessment.md`.

Slide numbers refer to the **revised** deck,
`01-deck/revised/Module 3 - Debugging, Optimization, and Code Reviews - REVISED.pptx`.
They do not match the vendor original, which was one slide shorter.

## Answers

| Q | Answer | Tag | Taught in | Why this answer, and what the question diagnoses |
|---|---|---|---|---|
| 1 | c | Core | Revised slides 5, 6 and 7 | A single error line carries no state, no surrounding code and no way to reproduce, so a generic answer is the only answer available. Option d is the narrow near miss, one useful fact out of the three that are missing. If a learner picks b they have reached for the right technique at the wrong moment, which question 2 then rewards. |
| 2 | d | Core | Revised slide 10, Exercise 7 Step 8 | No exception means no trace, so a trace-based prompt has nothing to work from. Ranked hypotheses plus one cheap check is the pattern that fits. Option b is the instinct this question exists to correct: demanding one answer and forbidding alternatives feels precise and removes the only useful structure. |
| 3 | a | Core | Revised slide 13, Exercise 8 Step 3 | Quadratic, not exponential. Option b is the error the vendor deck itself contained and revised slide 13 now corrects, so expect it to be chosen by learners who watched an earlier cut of the recording. Worth naming on camera: repeating "exponential" in a review costs credibility with the person you are trying to convince. |
| 4 | b | Core | Revised slide 13, bullet four, Exercise 8 Step 8 | Correctness is checked before timing. A changed total means the speedup is not a result, and the fix is a preservation constraint that states the answer must not change. Option d is the dangerous one, because rationalising the new total is exactly how a wrong number gets into a report and believed. |
| 5 | d | Core | Revised slides 19, 21 and 23, Exercise 9 Step 5 | Three ingredients, each doing a job: a role and a stake set what counts as serious, naming the excluded categories stops the style flood, and severity groups defined by consequence make the groups mean the same thing to both parties. Option b is the near miss and is worth debriefing, because asking for "important issues" does not work: style issues are real issues, just not the ones you asked for. |
| 6 | a | Core | Module 1 revised slide 22, revised slide 20, Exercise 7 Step 7 | A proposed fix is an untested hypothesis, however good the explanation is. Options b and c both ask the same source to confirm itself. Option d treats intermittency as an excuse not to verify, when it is the reason verification matters most. |
| 7 | c | Core | Revised slide 24 | First pass by Claude for bugs, security and missing tests, then a human on behaviour and architecture, with the sign-off staying human. Option d is the plausible alternative and inverts the value: consulting it only when stuck wastes the cheap first pass. Option a gives away the accountability that slide 24 says stays with a person. |
| 8 | b | Stretch | Revised slide 15 | Ask for the built-in before you accept fifty lines you now own and have to test. Option c is the trap for the cynical learner, since the bottleneck was correctly identified and does need fixing. Option a is a real belief and is usually false for sorting. |
| 9 | b | Stretch | Revised slide 12 | A static read cannot know how often a function runs, so it weighs a rarely executed path like a hot one. The fix is to supply the measurements slide 12 asks for. Option d over-corrects into excluding performance from reviews entirely, and option a generalises one bad call into a rule about all performance findings. |
| 10 | c | Stretch | Exercise 9 Step 7 | True, serious and about code this pull request did not touch makes it a ticket rather than a blocking review comment. Option a confuses severity with scope, and option d is the most common real-world version of the same mistake, expanding someone else's change because the author is nearby. Option b discards a verified finding. |

## Answer distribution

Required: each of a, b, c and d correct at least twice across the ten questions.

| Option | Count | Questions |
|---|---|---|
| a | 2 | 3, 6 |
| b | 3 | 4, 8, 9 |
| c | 3 | 1, 7, 10 |
| d | 2 | 2, 5 |

Total 10. Requirement met.

## Tag distribution

Core 7: questions 1, 2, 3, 4, 5, 6, 7.
Stretch 3: questions 8, 9, 10.

## Notes for the debrief

1. Questions 1 and 2 are a pair and should be debriefed together. The first failure has
   a trace and the second does not, and the technique that works on one is useless on the
   other. A learner who answers both correctly has the whole of the first third of this
   module.
2. Question 3 is the corrected fact. The vendor deck said nested loops grow
   exponentially, revised slide 13 says quadratically, and Exercise 8 Step 3 makes the
   learner name it themselves. If anyone reports that the video said exponential, they
   watched a pre-revision cut and the recording needs checking.
3. Question 4 tests the ordering lesson from Exercise 8 without revealing which
   optimisation loses the count or what either total is. Keep it that way. See
   `docs/lab-defect-register.md`, Exercise 8.
4. Questions 5 and 10 both come from Exercise 9. Question 5 deliberately does not name
   the category of the buried finding, because naming it would hand a learner the
   headline result of that exercise before they run it.

Copyright © 2026, ZaranTech LLC. All rights reserved.
