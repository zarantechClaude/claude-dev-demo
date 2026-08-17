# Module 2 answer key: Claude for Coding Tasks

**Trainer facing. Do not publish this file to learners and do not read it out on
camera.** The learner-facing questions are in `assessment.md`.

Slide numbers refer to the **revised** deck,
`01-deck/revised/Module 2 - Claude for Coding Tasks (Claude Code) - REVISED.pptx`.
They do not match the vendor original, which was two slides shorter.

## Answers

| Q | Answer | Tag | Taught in | Why this answer, and what the question diagnoses |
|---|---|---|---|---|
| 1 | b | Core | Revised slide 8, Exercise 4 Step 4 | The one rule that governs the file: durable facts in the file, the current task in the prompt. Options a and c are both true today and false next week, which is why they belong in a prompt. A learner who picks either will produce a context file that rots, and a stale instruction is worse than a missing one. |
| 2 | c | Core | Revised slides 8 and 10, Exercise 4 Steps 3 and 4 | The context file is the answer, because it is loaded every session, version controlled and shared with the team. Options a, b and d are all one-off manoeuvres that have to be repeated. If a learner picks b they are still thinking in uploads, which is the Module 1 habit Exercise 4 Step 1 exists to break. |
| 3 | d | Core | Revised slide 8, Exercise 4 Steps 4 and 6 | The stack is a durable fact, so it belongs in the file. Options a, b and c all work and all require the developer to remember to do them, which means they will fail on the day it matters. This question diagnoses whether a learner has understood why a file beats a pasted message, which is Exercise 4 Step 3. |
| 4 | b | Core | Revised slide 15, Exercise 5 Steps 6 and 7 | The missing element is a preservation constraint, a statement of what must survive the change. Note for the debrief that the change itself is good advice, so a reviewer who blocked it outright would also be wrong. It is a correct improvement that cannot ship on its own, because it needs a migration path nobody asked for. Options a and d would have caught it later, which is not the same as preventing it. |
| 5 | a | Core | Exercise 5 Step 2, point 3, supported by revised slide 11 | Ask for registration code without naming the credential requirement and you may get weak or plain storage. The constraint in the prompt is what secures the output, not the model's judgement. Options b and c are the two comfortable beliefs this question exists to remove. |
| 6 | c | Core | Exercise 6 Steps 6 and 7, supported by Module 1 revised slide 22 | No test ran, so there is no result to trust. Execute the suite yourself. Option d is deliberately attractive because it is a real lesson from Exercise 6, that tests requested with the docstrings assert the docstring rather than the code. It is a good instinct answering the wrong question here. |
| 7 | a | Core | Revised slide 21, Exercise 6 Steps 2 and 3 | Ask for intent and for edge case behaviour visible in the code, and rule out line by line narration. Options b and d treat comment volume as the variable. If a learner picks either, point them at Exercise 6 Step 3 check four: documentation that describes what the code should do rather than what it does is worse than none. |
| 8 | d | Stretch | Revised slide 8, bullet four, Exercise 4 Step 6 | Repeated correction in the chat is the symptom, and a stale context file is the cause. Option a is the near miss and is worth debriefing: it works and it depends on you remembering, every session, forever. Option b throws away working code to avoid updating a file. |
| 9 | c | Stretch | Revised slides 14 and 16 | Plan the boundaries, agree them, then extract one at a time and verify each. This is the incremental habit slide 16 describes as mapping dependencies before refactoring. Options a and d both respond to a failed large change by making another large change, which is the reflex the question is testing for. |
| 10 | a | Stretch | Revised slide 23, bullet three | Generated tests reach whatever the code reaches unless you tell them not to, so name a mocking library in the prompt. Option d is the plausible wrong answer, because a teardown restores state only if the test completed and only if it restores the right state. Option b confuses error handling with isolation. |

## Answer distribution

Required: each of a, b, c and d correct at least twice across the ten questions.

| Option | Count | Questions |
|---|---|---|
| a | 3 | 5, 7, 10 |
| b | 2 | 1, 4 |
| c | 3 | 2, 6, 9 |
| d | 2 | 3, 8 |

Total 10. Requirement met.

## Tag distribution

Core 7: questions 1, 2, 3, 4, 5, 6, 7.
Stretch 3: questions 8, 9, 10.

## Notes for the debrief

1. Questions 1, 2, 3 and 8 are one cluster, all on the project context file taught on
   new revised slide 8. A learner who gets 1 and 2 right but misses 3 or 8 knows what
   the file is and not yet why it beats repeating yourself. That is the useful
   diagnosis, and Exercise 4 Step 3 is the fix.
2. Question 4 is the most important question in this module. If a learner misses it,
   walk Exercise 5 Steps 5 to 7 again, and be precise that the refactor was right and
   unshippable at the same time. Both halves of that sentence have to land.
3. No question here names the specific credential defect planted in
   `exercise-05-registration-endpoint/starter/messy_registration.py`, and none should.
   Question 4 tests the preservation constraint through its consequence, which is what
   `docs/assessment-spec.md` asks for under scenario framing. Check
   `docs/lab-defect-register.md` before adding any question to this set.

Copyright © 2026, ZaranTech LLC. All rights reserved.
