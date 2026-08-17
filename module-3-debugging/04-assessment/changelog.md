# Module 3 assessment changelog

What changed from the vendor assessment, question by question. Vendor original:
`original/Assessment - Module 3 - Debugging Optimization and Code Reviews.pdf`, ten
scenario questions.

Governed by `docs/assessment-spec.md`. Slide references in the answer key are **revised**
deck numbers.

## Summary

| Outcome | Count | Vendor questions |
|---|---|---|
| Kept, stem trimmed only | 0 | none |
| Rewritten | 7 | V1, V2, V4, V5, V7, V8, V10 |
| Replaced | 3 | V3, V6, V9 |

Nothing survived untouched here, but only three questions were discarded. The recurring
repairs were the same three each time: cut a premise that was larger than the material,
replace a correct option that named jargon the deck never uses, and shorten correct
options that were the longest on the page.

Answer distribution moved from vendor b-heavy to a 2 / 3 / 3 / 2 split across a, b, c and
d. See the answer key for the count.

## Question by question

Vendor questions are numbered V1 to V10. New questions are numbered as they appear in
`assessment.md`.

### V1, hydration error with a pasted stack trace. Rewritten.

Sound question with a premise from a different course. Next.js, server-side rendering and
production-only hydration failures are not in this programme, and the mention of source
maps in a distractor pushed it further out.

Rewritten as **question 1**, framework-neutral, resting on what revised slides 5, 6 and 7
actually teach: the full trace, the surrounding code and the reproduction steps.
Distractor d is new and is the useful near miss, one correct fact where three were missing.

### V2, memory leak and hypothesis testing. Rewritten.

Good question. The premise was a Node.js memory leak, which the programme does not cover,
and the correct option was a verbatim prompt long enough to be identifiable by length
alone.

Rewritten as **question 2** around the situation Exercise 7 actually produces: a test that
fails with no exception, so there is no trace to paste and the technique from question 1
does not apply. The correct option states the pattern instead of quoting a prompt. This
also gives the module's two debugging techniques a question each, and makes the pair
diagnosable.

### V3, multiprocessing and out-of-memory. Replaced.

Unsalvageable. `docs/assessment-spec.md` names this question specifically as an example of
difficulty set well above the material, and it is: nothing in the module teaches worker
processes, dataset copying or memory profiling, and the labs ask a learner to time a
function and read a count. It also carries a specific row count and a specific runtime as
load-bearing premises.

Replaced by **question 3**, on naming quadratic growth correctly. That is the factual
error the vendor deck contained, it is now corrected on revised slide 13, and Exercise 8
Step 3 has the learner name it. It was not tested anywhere in the vendor set, which is how
the error survived.

### V4, custom QuickSort instead of the standard library. Rewritten.

Sound and worth keeping. Kept as **question 8**, tagged Stretch, with the stem cut to two
lines and the correct option shortened so it is no longer the longest available. Distractor
c is new: leaving the slow sort alone is the cynical learner's answer and it is wrong,
because the bottleneck was correctly identified. The vendor's version of that option told
the learner the model over-optimises, which is coaching rather than distracting.

### V5, bare "review this PR" floods style comments. Rewritten.

The vendor question closest to being right, and it needed one specific repair. Its stem
named the category of the buried finding, which is the headline result of Exercise 9, so
shipping it would have told a learner what to look for before they ran the exercise. See
`docs/lab-defect-register.md`, Exercise 9.

Kept as **question 5** with the stem changed to "the one finding that should have blocked
the merge", which tests the same judgement and reveals nothing. The correct option was
also shortened to three named ingredients, since the vendor version ran to four lines and
was three times the length of any distractor.

### V6, binary search debugging on a 10,000-line C++ file. Replaced.

Two reasons. The premise is a 10,000-line C++ file with no logs, which is outside the
programme in both language and scale. And the technique it tests, isolating a failure by
halving, overlaps with what questions 1 and 2 already cover between them, so the slot was
buying a repeat rather than new coverage. Revised slide 9 still teaches the technique and
the recording still demonstrates it.

Replaced by **question 4**, on an optimisation that is faster and wrong. That is the
lesson of Exercise 8 Steps 7 to 9 and the final bullet added to revised slide 13, and the
vendor set tested nothing like it.

### V7, a startup-only function flagged as inefficient. Rewritten.

A good idea with a correct option that ran to three lines of general explanation. Kept as
**question 9**, tagged Stretch, with the correct option reduced to the mechanism, no
runtime data, and the action, supply the measurements revised slide 12 asks for.
Distractor d is new and is a real over-correction: excluding performance from reviews
altogether.

### V8, junior developer deploys a fix because it looked right. Rewritten.

Sound. Kept as **question 6**, with the junior developer removed from the stem, since the
framing invited the answer without any reasoning: a question about a junior making a
mistake announces that a mistake was made. Rewritten so the fix looks good and the
explanation is convincing, which is the situation a competent developer is actually in.
The two joke distractors in the vendor version were replaced with plausible ones,
including a second opinion from another conversation, which is the most common wrong
answer in real life.

### V9, regex hallucination and self-correction. Replaced.

Not a weak question, but its point, supply concrete evidence rather than asking the model
to try again, is already tested by question 1 on the input side and question 2 on the
technique side. Three questions on the same idea in a ten-question set is a poor use of
the budget.

Replaced by **question 10**, on a finding that is real, serious, and about code the pull
request did not touch. That is Exercise 9 Step 7 and it distinguishes severity from scope,
which nothing else in this set tests.

### V10, integrating AI into a formal peer review process. Rewritten.

Sound, traceable to revised slide 24, and kept as **question 7**. The vendor version's
distractors were three throwaways, including using it only to check spelling in variable
names, so the correct answer was identifiable without reading it. All three were replaced
with arrangements a real team has genuinely proposed: automatic merge with sampled audits,
restriction to cosmetic comments only, and human first with the assistant as a fallback.
That last one was the vendor's own distractor and is the only one worth keeping, because it
inverts the value of a cheap first pass.

## Checks performed before shipping

1. Seven Core, three Stretch, tagged in the learner-facing file.
2. Correct answers land on each of a, b, c and d at least twice. Counted, 2 / 3 / 3 / 2.
3. Every question names a revised slide or a lab step in the answer key.
4. No model version named, and no question resting on a context-window size, a token limit
   or a price. The vendor's row counts and runtimes were removed with V3.
5. Checked against `docs/lab-defect-register.md`. Question 4 tests Exercise 8's ordering
   lesson without naming either total or the change that loses the count. Question 5 tests
   Exercise 9's prompt contrast without naming the category of the buried finding.
6. No em dashes. Every stem is under sixty words.
7. `assessment.md` contains no answers and no ordering tell. Correct options were
   length-checked against their distractors, which is where most of the vendor set leaked.

Copyright © 2026, ZaranTech LLC. All rights reserved.
