# Module 2 assessment changelog

What changed from the vendor assessment, question by question. Vendor original:
`original/Assessment - Module 2 - Claude for Coding Tasks Claude Code.pdf`, ten scenario
questions.

Governed by `docs/assessment-spec.md`. Slide references in the answer key are **revised**
deck numbers.

## Summary

| Outcome | Count | Vendor questions |
|---|---|---|
| Kept, stem trimmed only | 1 | V9 |
| Rewritten | 8 | V1, V2, V3, V4, V5, V6, V7, V8 |
| Replaced | 1 | V10 |

This is the module where the vendor question set was strongest. Eight of the ten
questions were reaching for something real, and most of the work was cutting the
premises down to the size of the material and repairing options that named invented
jargon.

Answer distribution moved from vendor b-heavy to a 3 / 2 / 3 / 2 split across a, b, c
and d. See the answer key for the count.

## Question by question

Vendor questions are numbered V1 to V10. New questions are numbered as they appear in
`assessment.md`.

### V1, big-picture context in a monorepo. Rewritten.

The question was sound and its correct answer is now out of date. The vendor answer was
to pipe a directory listing into the prompt alongside an architecture document, which
was the best available technique when the deck taught no alternative. The deck now
teaches the project context file, on new revised slide 8, and that is the better answer
for the same scenario.

Kept as **question 2** with the correct option replaced. The stem lost the monorepo and
the new microservice, which did not affect the answer, and lost the reference to
overflowing the context window, because the spec forbids resting a question on a window
size. The vendor's directory listing has not been kept as a distractor, since it is not
actually wrong and a distractor has to be wrong.

### V2, wrong database dialect. Rewritten.

Good scenario, weak options. The vendor correct answer explained the behaviour as
training data bias toward a particular stack, which is speculative, unverifiable, and
teaches the learner to reason about the model's statistics rather than about their own
prompt.

Rewritten as **question 3** so the question is about the fix instead of the mechanism,
and the fix is the one the module now teaches: put the durable fact in the context file.
The three distractors are now the three manual workarounds a learner is most likely to
reach for, all of which work and all of which depend on remembering.

### V3, refactor broke the legacy application. Rewritten.

The most valuable question in the vendor set for this module, because it is the core
lesson of Exercise 5. Rewritten as **question 4** for three reasons. The JavaScript
premise was replaced, because the programme is Python only. The vendor's correct option
was three lines long and the longest on the page, which is an ordering tell the spec
names explicitly. And the stem was rebuilt around the consequence, that no existing user
can log in, which is the scenario framing `docs/assessment-spec.md` recommends.

The stem deliberately does not name the specific hashing change planted in Exercise 5,
so the question tests the concept without leaking the lab. See
`docs/lab-defect-register.md`, Exercise 5, "The trap".

### V4, agent stuck in a loop. Rewritten.

The premise, an agent cycling on a cyclic dependency and a failing compiler, is above
the material. Nothing in Module 2 covers agent loop intervention and no lab produces
that situation, so the question failed traceability.

The salvageable idea underneath it is that repeating a correction in the chat is not a
fix. Rewritten as **question 8**, tagged Stretch, where the recurring behaviour is a
stale context file and the fix is to update it. That traces to revised slide 8 bullet
four and to Exercise 4 Step 6.

### V5, registration endpoint flagged in a security audit. Rewritten.

Kept in substance as **question 5**. The vendor version named a specific weak hashing
algorithm in its correct option, which sits too close to the defect planted in
`exercise-05-registration-endpoint/starter/messy_registration.py`. The rewritten
question asks what the safest assumption is when the prompt said nothing about
credentials, which tests Exercise 5 Step 2 point 3 without naming the planted defect.
The distractors are now the two comfortable beliefs a learner actually holds, that
modern defaults are safe and that the user story carried the requirement.

### V6, "I have run these mentally and all tests pass". Rewritten.

Good scenario, and the vendor correct option required the learner to select the word
"sycophancy", which appears nowhere in the deck or the labs. That tests vocabulary
recognition rather than judgement.

Rewritten as **question 6** so the correct option states the action instead: nothing ran,
so run it yourself. Distractor d is new and deliberately attractive, because it is a
genuine Exercise 6 lesson applied to the wrong question. Jest was replaced with a
framework-neutral phrasing, since the programme is pytest.

### V7, generated tests deleted live cloud data. Rewritten.

Sound and traceable to revised slide 23. Kept as **question 10**, with the AWS service
names removed and the scenario reduced to a shared staging database, which is a situation
this audience meets and does not require cloud specifics to understand. Distractor d, a
teardown step, is new and is the most plausible wrong answer available, because it sounds
like isolation and is not.

### V8, comments that translate the syntax. Rewritten.

Sound. Kept as **question 7**, with the Java class replaced by an undocumented module and
the stem cut from four lines to two. The correct option was shortened so that it is no
longer the longest on the page, and it now names the two things revised slide 21 and
Exercise 6 Step 2 actually ask for: purpose, and edge case behaviour visible in the code.

### V9, hallucinated imports after a single large refactor. Kept.

Kept as **question 9** with the stem trimmed and the correct option shortened. The
distractors already worked, in that each one is a real reflex: try again and compare,
supply more reference material, or start over from scratch. Tagged Stretch, because the
module teaches incremental refactoring as a principle on slides 14 and 16 without walking
a learner through this specific failure.

### V10, un-Pythonic output from a Java developer. Replaced.

Not a bad question. Replaced because the programme is Python only, which removes the
premise, and because what remains tests whether a learner can name idioms rather than
whether they can make a decision.

The slot went to **question 1**, on what belongs in the project context file and what
belongs in a prompt. That is the largest single content gap the deck review found, it is
now taught on new revised slide 8, and it was not tested at all in the vendor set.

## Checks performed before shipping

1. Seven Core, three Stretch, tagged in the learner-facing file.
2. Correct answers land on each of a, b, c and d at least twice. Counted, 3 / 2 / 3 / 2.
3. Every question names a revised slide or a lab step in the answer key.
4. No model version named, and no question resting on a context-window size, a token
   limit or a price.
5. Checked against `docs/lab-defect-register.md`. Questions 4 and 5 test Exercise 5
   through its consequences, and neither names the planted defect or the specific change
   the trap turns on.
6. No em dashes. Every stem is under sixty words.
7. `assessment.md` contains no answers and no ordering tell. Correct options were
   length-checked against their distractors, which the vendor set did not do.

Copyright © 2026, ZaranTech LLC. All rights reserved.
