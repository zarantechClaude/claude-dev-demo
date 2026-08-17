# Module 1 assessment changelog

What changed from the vendor assessment, question by question. Vendor original:
`original/Assessment - Module 1 - Fundamentals of Claude for Developers.pdf`, ten
scenario questions.

Governed by `docs/assessment-spec.md`. Slide references in the answer key are
**revised** deck numbers.

## Summary

| Outcome | Count | Vendor questions |
|---|---|---|
| Kept, stem trimmed only | 1 | V2 |
| Rewritten | 4 | V4, V5, V9, V10 |
| Replaced | 5 | V1, V3, V6, V7, V8 |

Answer distribution moved from vendor b-heavy to a 2 / 2 / 3 / 3 split across a, b, c
and d. See the answer key for the count.

## Question by question

Vendor questions are numbered V1 to V10. New questions are numbered as they appear in
`assessment.md`.

### V1, race condition in a 65,000-token monolith. Replaced.

Unsalvageable as written. Three separate problems: the premise is a specific token
count, which the spec forbids because the arithmetic rots; the scenario sits far above
anything the module teaches, since the labs ask a learner to paste one function; and
the correct option rewarded reciting an architectural claim rather than making a
judgement. The idea it was reaching for, that a whole file read in one pass beats a
snippet, survives in revised slide 5 and does not need a race condition to test it.

Replaced by **question 8**, which tests verification of a fluent explanation. Same
material, Exercise 1, and it diagnoses something a learner will actually do.

### V2, air-gapped host. Kept.

The best question in the vendor set. The intuition that a command line tool must run
entirely locally is strong, widely held and wrong, and the correct answer is the
counter-intuitive one. Kept as **question 4**, with the stem trimmed: the DevSecOps
framing, the legacy unit test goal and the enterprise SSO detail were removed because
none of them affected the answer. Distractor b was rewritten so that the wrong options
are wrong for reasons a learner could plausibly hold. Tagged Stretch, because the
module implies the answer rather than stating it.

### V3, refactor broke the business logic. Replaced in this module.

A good question in the wrong module. The concept it tests is the preservation
constraint, which is taught in Module 2, on revised slide 15 and throughout
Exercise 5. Testing it here would have tested material the learner has not met yet,
which fails the traceability rule.

Replaced by **question 7**, on discarding a finding that cannot be anchored to a line,
which is Exercise 3 Step 5 and is taught in this module. The preservation constraint is
now tested in the Module 2 assessment, question 4.

### V4, PII and secrets in crash logs. Rewritten.

Sound question, kept as **question 3** with the correct answer intact. The stem lost
the catastrophic production database failure and dropped from four sentences to two.
Distractor b was tightened so it reads as a real belief, that an instruction inside the
prompt can control data you have already sent, rather than as an obviously silly
option. Now traces to revised slide 21.

### V5, classifying a prompt clause. Rewritten.

The question was worth keeping and the options were not. Three of the four named
invented categories, "zero-shot bounding" and "instruction conditioning" among them,
so the question tested whether a learner recognised jargon rather than whether they
could place a line in a prompt.

Rewritten as **question 2** using the four-part vocabulary the module actually teaches
on revised slides 14 to 17 and in Exercise 2: instruction, context, example,
constraint. The React and Material-UI framing went, because the programme is Python
only. Distractor a is now the real misconception, filing a library restriction under
context.

### V6, generated SQL query with an interpolated email address. Replaced.

Not replaced because it was a weak question. It was a reasonable question. It was
replaced because the code in its stem is close to verbatim the planted SQL injection in
`exercise-03-review-checklist/starter/order_sync.py`, and shipping it would have handed
a learner one of the findings the exercise exists to make them discover. See
`docs/lab-defect-register.md`, Exercise 3, defect 7.

The concept, treating generated code as an untrusted draft, is still tested, in
**question 7** and again in **question 8**, without reproducing a planted defect.

### V7, C++ to Python translation. Replaced.

Two problems. The correct option was a general claim about advanced reasoning that a
learner could select without understanding anything, and no distractor was a real
misconception. The pointer-heavy C++ premise also sits outside a Python-only
programme.

Replaced by **question 9**, the second half of the repo as context distinction. That
distinction is the single most useful thing in the module and one question was not
enough to cover it.

### V8, catastrophic regex backtracking. Replaced.

Unsalvageable. ReDoS is not taught anywhere in the programme, on any slide or in any
lab, so the question fails traceability outright. It is also exactly the failure the
spec records as the vendor set's main defect: difficulty set well above the material.

Replaced by **question 10**, on scrubbing a prompt before it is saved into a shared
template. That extends revised slide 21 to a situation the learner has not been shown,
which is what a Stretch question is for, and it reinforces Exercise 2 Step 8, the step
learners skip most.

### V9, Claude Code versus the web interface. Rewritten.

The correct answer was right and the framing was loose. Rewritten as **question 1** so
that it turns on the specific consequence taught on new revised slide 8, that an
attached repository grants no write access, rather than on a general statement about
copy and paste. The GPU distractor was removed, because it overlapped with the
air-gapped question at 4 and would have given part of that answer away.

### V10, hallucinated field names after a large paste. Rewritten.

Kept as **question 5**, with the correct answer intact in substance. The vendor version
required a learner to select the phrase "attention dilution", which appears nowhere in
the deck. The rewritten correct option states the action instead, cut the context and
restate the instruction, which is what revised slide 19 teaches. The 10,000-line figure
was removed so the question does not rest on a volume.

## Checks performed before shipping

1. Seven Core, three Stretch, tagged in the learner-facing file.
2. Correct answers land on each of a, b, c and d at least twice. Counted, 2 / 2 / 3 / 3.
3. Every question names a revised slide or a lab step in the answer key.
4. No model version named, and no question resting on a context-window size, a token
   limit or a price.
5. Checked against `docs/lab-defect-register.md`. No question reveals a planted
   defect. V6 was dropped for exactly this reason.
6. No em dashes. Every stem is under sixty words.
7. `assessment.md` contains no answers and no ordering tell.

Copyright © 2026, ZaranTech LLC. All rights reserved.
