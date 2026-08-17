# Module 5 assessment changelog

What changed from the vendor assessment, question by question. Governed by
`docs/assessment-spec.md`.

Vendor original: `original/Assessment - Module 5 - Advanced Developer Workflows & Mini-Project.pdf`.
The folder README explains that the PDF still has to be copied in from the vendor pack.
The vendor text was read from the attached Claude project while this rewrite was
authored.

## Headline

The vendor Module 5 questions were mostly well aimed. The two structural problems were
the answer key and the traceability of a few premises.

**The answer key had b correct in nine of ten questions.** A learner who noticed scored
90 percent without knowing anything. Fixing that distribution was a requirement of this
rewrite, not a tidy-up, and the new spread is 3 / 2 / 2 / 3 across a, b, c and d.

| Fate | Count | Vendor questions |
|---|---|---|
| Kept | 4 | 4, 6, 8, 10 |
| Rewritten | 5 | 1, 2, 3, 5, 7 |
| Replaced | 1 | 9 |

## Question by question

### New Q1, from vendor Q1. Rewritten.

Constraining a spec prompt. The vendor version framed it as a "Spec-First Contract"
pattern, and its correct option was a six-line block quoting an input contract, an
output contract with a latency figure, and an error-handling clause. Two problems. The
pattern name appears nowhere in the deck or the labs, and the option was several times
longer than every distractor, which identifies it without reading the stem.

Rewritten against what Exercise 13 actually teaches in Steps 3 and 4: a named section
list gives the document a checkable shape, and an explicit instruction not to resolve an
ambiguity silently is what makes the assumptions visible. All four options are now one
line each. The correct option stays at b, which is one of only two places in this
module where the letter did not need to move, and the overall distribution still
clears the spec.

### New Q2, from vendor Q2. Rewritten.

Mermaid. The vendor question asked which output format to request, which is recall and
diagnoses very little, since the answer is on the slide title.

Rewritten to the part that has teaching value and that Exercise 13 Step 7 is explicit
about: a diagram that does not render is not a deliverable, and when it fails you paste
the renderer's exact error back rather than describing it. That gives a distractor which
is a real habit the lab corrects. Correct option moved from b to d.

### New Q3, from vendor Q5. Rewritten.

Ticket granularity. The vendor's correct option required the INVEST principle, a
three-story-point ceiling and a "Definition of Done", none of which is taught anywhere
in this programme. As posed it tested vocabulary the learner was never given.

Re-anchored to slide 8 and Exercise 13 Step 9, which supply the actual checks: one
purpose per ticket, acceptance criteria a stranger could test, dependencies that point
backwards. The fifteen-minute distractor is kept because Exercise 13's Common problems
table covers exactly that over-correction. Correct option moved from b to a.

### New Q4, from vendor Q3. Rewritten.

The vendor question bundled two things: where a pipeline's secret comes from, and a
distractor claiming automation is impossible because the tool needs an interactive
terminal. Revised slide 13 now teaches the real mechanism, which is that CI has no
terminal to prompt, so the pipeline calls the API from a non-interactive script. That
makes the vendor's distractor half-true and the question ambiguous.

Split. The non-interactive half becomes this question, anchored to slide 13, and the
distractor is reframed as the reasonable-but-wrong conclusion that pipelines cannot use
AI assistance at all. The secret-store half was **dropped**: the Module 5 deck does not
cover secret stores, so it fails the traceability rule here, and key handling is already
tested in Module 4 question 7, where Exercise 10 Step 3 supports it. The correct option
is c, as it was in the vendor version.

### New Q5, from vendor Q4. Kept.

Reviewing a generated Dockerfile. Sound and well traced to Exercise 14, whose checklist
covers the floating tag at row 1 and the development server at row 7.

Changes: the correct option was three lines and named a specific base image tag and a
specific WSGI server, while the distractors were one line each. Levelled, and the
specific product names removed so the question tests the review judgement rather than
recall of one stack. Distractor c is now the real mis-ranking, which is that the
development server is a performance problem, because Exercise 14 row 7 exists to correct
precisely that. The "Flask is incompatible with Docker" option was dropped as absurd.
Correct option moved from b to d.

### New Q6, from vendor Q6. Kept.

Stale grounding. The best question in the vendor set for this module. Concept, correct
option and the cache-clearing distractor all retained.

Changes: stem rewritten around the capstone's own failure mode from Exercise 15 Step 9,
which is the response shape rather than a database schema, and the detail that makes it
expensive is now in the stem: nothing errors and each output looks correct on its own.
The "API limits schema memory to 5 minutes" option was dropped as absurd and replaced
with a dependency-pinning distractor, which is a real if wrong guess. Correct option
moved from b to a.

### New Q7, from vendor Q8. Kept.

The 413. Concept and correct option retained, and this is required content because the
capstone brief names it as trap 1.

Changes: distractor c named a specific model version and asserted a size limit for it,
which the spec bars twice over, so it is now a version-neutral context-window claim. The
correct option's parenthetical listing typical default body sizes was removed for the
same reason. The stem now supplies the diagnostic detail that no handler log line
appears, which is what actually tells you the rejection happened above your code.
Correct option moved from b to b, unchanged.

Deliberately not extended toward the skeleton's two different 413 bodies. Exercise 15
Step 8 asks the learner to derive the second one, and a question about it would leak
the lab.

### New Q8, replaces vendor Q9. Replaced.

Vendor Q9 asked how to optimise a monorepo CI pipeline, with path filtering and two
named build orchestration tools as the correct option. **Unsalvageable on
traceability.** Path filtering, dependency-graph build tools and monorepo CI appear
nowhere in the revised deck, in any Module 5 lab, or in any earlier module. The
question is fine in itself and belongs to a different course.

Replaced with required content that the module now teaches explicitly on revised slide
23: the capstone is marked mostly on prompt design and robustness, and feature count
carries no marks. Framed as two submissions to compare, so it tests judgement rather
than recall of the weights. Correct option c.

### New Q9, from vendor Q7. Rewritten.

Reviewing a destructive generated script before running it. The concept is right and
responsible practice is a marked criterion in the capstone rubric.

Changes: the vendor scenario was an AWS infrastructure migration with named CLI
commands, and neither AWS nor those commands are taught here. Re-anchored to slide 15,
which does cover generated migration scripts, validating them to prevent data loss, and
rollback scripts. The "ask Claude to sign a digital certificate" option was dropped as
absurd. Its replacement is the sharper trap, which is trusting the rollback script the
same generation produced, and it is built out of the deck's own bullet. Correct option
moved from b to a.

### New Q10, from vendor Q10. Kept.

Mapping a large legacy codebase by bounded context rather than in one pass. Concept and
correct option retained.

Changes: the vendor's first distractor named a specific context-window size as the fix,
which the spec bars, so it is now the instinct to re-prompt with the same oversized
input, which is what developers actually do. The "AI is fundamentally incapable" option
was dropped as absurd. Traced to Module 4 slide 20, which teaches passing only the
relevant chunks, plus slide 7's iterative diagram updates. Correct option moved from b
to d.

## Cross-cutting changes

1. **Answer distribution.** This was the headline defect. Vendor: b correct in nine of
   ten. Rewrite: a 3 / 2 / 2 / 3 split, counted and recorded in the answer key. Option
   letters were moved question by question, not by a blind shuffle, so no plausible
   distractor was accidentally turned into the obviously silly one.
2. **Option length.** Six of the ten vendor questions had a correct option two to six
   times longer than every distractor. All options are now comparable in length.
3. **Absurd distractors removed.** Signing digital certificates, syntax hashing, asking
   a Scrum Master, and "AI is fundamentally incapable" were replaced with real
   misconceptions, several of them drawn from the Common problems tables in the labs.
4. **Style.** No em dashes. No model version anywhere. No context-window size, token
   figure or price in any stem or option. Every stem is under 50 words.
5. **Tagging.** Seven Core and three Stretch, marked in the learner-facing file.
6. **Planted defects.** No question depends on the specific answer to any planted
   defect. Specifically, nothing here touches the capstone skeleton's failing test or
   its patch target, which is Exercise 15 Step 10, and question 7 stays on the
   framework-level 413 that the capstone brief already discloses.

---

Copyright © 2026, ZaranTech LLC. All rights reserved.
