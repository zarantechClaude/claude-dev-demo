# Assessment authoring spec

Ten questions per module, fifty in total. This spec governs all of them, so that a
learner meets one consistent instrument across the programme.

## Position in the programme

Assessments are **self-check**. They are not graded and they do not gate completion.
The capstone carries completion. That decision changes how the questions should be
written: a self-check exists to tell a learner what they have not understood yet, so
a question that is merely hard teaches nothing, while a question that is diagnostic
teaches something even when answered wrongly.

## What was wrong with the vendor assessments

Recorded here because the same mistakes are easy to reintroduce.

1. **Difficulty sat well above the material.** The labs ask a learner to paste a
   function and read a traceback. The questions asked about race conditions in
   65,000-token monoliths and out-of-memory failures under multiprocessing. A
   learner who completed every lab successfully would still have failed.
2. **Four Module 4 questions tested topics the deck never covered:** prompt caching,
   assistant prefill, the alternating-roles requirement, and the system prompt as a
   top-level parameter. Three of those four are now taught, on new slides added for
   the purpose. The fourth was already covered and the question stays.
3. **The answer key was guessable.** Option b was correct in roughly half of all
   fifty questions, and in nine of ten in Module 5. A learner who noticed could
   score well without knowing the material.
4. **One question was factually outdated**, built on a specific context-window and
   output-token pair as its premise, so its arithmetic no longer holds.

## Rules

### Traceability
Every question must be answerable from the revised deck or the labs of its own
module, or an earlier module. The answer key records where. If you cannot name the
slide or the lab step that teaches it, the question does not ship.

### Tagging
Each question is tagged **Core** or **Stretch**.

- **Core** questions test something the module explicitly teaches. Seven per module.
- **Stretch** questions extend the material to a situation the learner has not been
  shown, but which is reachable by reasoning from what they have. Three per module.
  Tagging them means a learner who misses one knows it was meant to be hard, rather
  than concluding the course failed them.

### Answer distribution
Across each ten-question assessment, the correct answer must land on each of a, b,
c and d at least twice. Check the distribution before shipping and record it in the
answer key. This is a mechanical check and there is no excuse for failing it.

### Distractors
Wrong options must be wrong for a reason a learner could plausibly hold. The best
distractor is a real misconception, ideally one the module explicitly corrects. Avoid
options that are obviously absurd, options that are longer than the correct answer
as a tell, and "all of the above".

### Scenario framing
Prefer a short concrete scenario over a definition question. "Your refactor prompt
returned cleaner code and now no existing user can log in. What was missing from the
prompt?" beats "What is a preservation constraint?" The scenario version tests
whether the learner can recognise the situation, which is what they will actually
need.

### Style
- No em dashes.
- Never name a Claude model version, and never build a question on a specific
  context-window size, token limit, or price. Those change and the question rots.
- No question may depend on a planted defect's specific answer, because that leaks
  the lab.
- Keep the stem under about 60 words.

## File layout, per module

```
module-N-<slug>/04-assessment/
├── assessment.md          learner-facing, questions only, no answers
├── answer-key.md          answers, reasoning, tag, and where it is taught
├── changelog.md           what changed from the vendor version, question by question
└── original/              the vendor PDF
```

`assessment.md` must not contain the answers, in any form, including as an ordering
tell. `answer-key.md` is trainer-facing and must say so at the top.

## Answer key format

| Q | Answer | Tag | Taught in | Why this answer, and what the question diagnoses |
|---|---|---|---|---|

The last column is the useful one. If a learner misses the question, that cell should
tell the trainer what to point them back at.
