# Module 4 assessment changelog

What changed from the vendor assessment, question by question. Governed by
`docs/assessment-spec.md`.

Vendor original: `original/Assessment - Module 4 - Building with the Claude API (Backend & Integration).pdf`.
The folder README explains that the PDF still has to be copied in from the vendor
pack. The vendor text was read from the attached Claude project while this rewrite was
authored.

## Headline

The vendor assessment tested four topics the vendor deck never covered: prompt
caching, assistant prefill, the alternating-roles requirement, and the system prompt as
a top-level parameter. Three of the four are now taught on slides added for the
purpose, so those questions stay in substance and are re-anchored. The fourth was
always fair and is unchanged in substance.

One vendor question was not merely dated but wrong, because it reasoned from a named
model's context window paired with an output cap. It is replaced with a version-neutral
question on the same concept.

| Fate | Count | Vendor questions |
|---|---|---|
| Kept | 3 | 1, 2, 6 |
| Rewritten | 4 | 3, 4, 7, 10 |
| Replaced | 3 | 5, 8, 9 |

## Question by question

### New Q1, from vendor Q1. Kept.

The system prompt as a top-level parameter. This was the one topic of the four
"untaught" set that the vendor deck did cover, on the "Encoding System and User
Instructions" slide, so the question was always fair and the concept is unchanged.

Changes: stem cut from 61 words to 34 and the model-migration framing kept, since it
is where the mistake genuinely comes from. Correct option moved from b to c. The
"minimum of three messages" and `developer`-role distractors are retained because both
are real beliefs held by developers porting from elsewhere. Now also supported by
revised slide 13's last bullet.

### New Q2, from vendor Q2. Kept.

Prompt injection defended by tags plus a stated rule. Sound and traceable as written.

Changes: the stem named a specific Claude model version, which `CLAUDE.md` forbids
anywhere in the programme, so the version is gone and the scenario is now the learner's
own Exercise 11 CLI. The correct option was the longest of the four, which is an
answer tell, so all four options were levelled. Correct option moved from b to a.

### New Q3, from vendor Q6. Kept.

Alternating roles. Concept and correct option unchanged, re-anchored to revised
slide 13, which is new. The vendor deck taught none of this, so the question was
unanswerable as delivered.

Changes: stem shortened, correct option moved from b to d, and the rate-limit
distractor kept because it is the wrong diagnosis a developer actually reaches for.

### New Q4, from vendor Q4. Rewritten.

Assistant prefill, re-anchored to revised slide 13, bullets 3 and 4.

Changes: the vendor stem claimed the technique "guarantees" the output format. It does
not, and promising it on a self-check trains the wrong confidence, so the stem now asks
which technique gives the tightest control over how the reply opens. The `response_format`
distractor is retained deliberately: it belongs to another provider's API and is the
error a porting developer makes. The MCP-as-schema-validator distractor was dropped as
too far from anything taught. Correct option stays at b.

### New Q5, replaces vendor Q9. Replaced.

Vendor Q9 asked for "the most token-efficient and structurally sound place" to inject a
per-request document, with the system parameter as the intended answer. Two problems.
The honest answer depends on the application, and a per-request document placed in the
system prompt is in direct tension with the caching guidance now taught on revised
slide 22, where the stable material goes first. Its "insert a fake assistant message"
distractor has also become confusing, because inserting an assistant message is now a
technique the module teaches on slide 13.

Judged unsalvageable as posed. Replaced with a question on the statelessness of the API
and the developer's obligation to resend context, which is taught on slide 18 and is the
first thing Exercise 12 makes the learner prove to themselves. Correct option c.

### New Q6, replaces vendor Q5. Replaced.

Vendor Q5 built its premise on a named model, a stated context-window size and a
stated output cap, then asked the learner to reason from those numbers. The numbers
have moved, so the question is now wrong rather than dated, and its correct option
named a dated beta header.

Replaced with a version-neutral question on the actual concept, which is that the
context window and the output ceiling are two different limits with two different
fixes. Taught on slide 8, slide 16 and Exercise 10 Step 7, which spends a paragraph on
exactly this confusion. No number appears in the question or in any option. Correct
option a.

### New Q7, from vendor Q10. Rewritten.

A committed `.env`. The concept is right and it is taught in Exercise 10 Step 3, which
deliberately writes `.gitignore` before `.env`.

Changes: the vendor version was written around a serverless Node function, and this
programme is Python only, so the runtime reference is gone. The vendor's correct option
ran to three sentences and named two specific cloud secret managers while every
distractor was one line, which made it identifiable without reading the stem. All four
options are now one line. The rewritten version also tests the part that matters most
and that the vendor version buried, which is that rotation comes first because the key
is already in the history. Correct option moved from b to d.

### New Q8, from vendor Q3. Rewritten.

Prompt caching, re-anchored to revised slide 22, which is new. Unanswerable from the
vendor deck.

Changes: the vendor option described API internals, naming a specific request object
and "previously computed attention states". Slide 22 deliberately does not teach the
mechanics, because they change, and tells the learner to check current mechanics in the
documentation. The option now states what caching is for and the ordering rule, which
is what the slide teaches. A distractor was added asserting that caching raises the
amount of context a request can carry, because that is the misconception slide 22
exists to correct.

This question also absorbs the surviving point of **vendor Q8**, which asked about
instruction placement in a long prompt. Both questions turn on the same ordering rule:
stable and bulky material first, the variable instruction last. Vendor Q8's premise
quoted a token count for the document, and the spec bars building a question on token
figures, so it does not ship as a standalone question. Correct option b.

### New Q9, replaces vendor Q8. Replaced.

Newly authored. A naive last-N window drops a constraint that a later request still
depends on, which is the whole lesson of Exercise 12 Steps 4 to 6.

The scenario is deliberately not the conversation in `history_starter.py`. Testing that
specific conversation would hand the learner the lab's finding before they reach it, and
the register records that even the comments were removed from the starter file for the
same reason. The domain here is a review assistant, and the question tests the concept
only. The strongest distractor is lexical overlap, which is the second bad proxy
Exercise 12 also demolishes, so a learner who half-learned the lab can still be caught
by it usefully. Correct option a.

### New Q10, from vendor Q7. Rewritten.

MCP. The vendor question asked which MCP component is responsible for executing a
query. That framing is **unsalvageable on traceability**: neither the vendor deck nor
the revised deck teaches the client and server responsibilities, and revised slide 24
says "your backend executes the chosen tool", which a reasonable learner would read as
contradicting the vendor's intended answer. Shipping it would fail the spec's
traceability rule and would be arguably wrong against our own slide.

Rewritten to what the deck does teach, on slide 23: MCP is a standard interface that
removes the need for a custom bridge per system. The new distractors are the two real
misconceptions in this area, which are that the model reaches into your network itself
and that adopting a standard removes the need to declare tool schemas. The second is
contradicted by slide 24, so the deck supports the discrimination. Correct option c.

## Cross-cutting changes

1. **Answer distribution.** Vendor Module 4 had b correct in five of ten. The rewrite
   is a 3 / 2 / 3 / 2 split across a, b, c and d, counted and recorded in the answer
   key.
2. **Difficulty.** Every question is now answerable from the revised deck or a lab step
   of this module, or an earlier one. Nothing tests API internals the programme never
   demonstrates.
3. **Style.** No em dashes. No model version anywhere. No context-window size, output
   cap or price in any stem or option. Every stem is under 45 words.
4. **Tagging.** Seven Core and three Stretch, marked in the learner-facing file so a
   learner who misses a Stretch question knows it was meant to be hard.
5. **Planted defects.** No question depends on the specific answer to any planted
   defect. Q9 is the one that came close, and it is framed on a different scenario for
   that reason.

---

Copyright © 2026, ZaranTech LLC. All rights reserved.
