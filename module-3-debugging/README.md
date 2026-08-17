# Module 3: Debugging, Optimization, and Code Reviews
## Guidance for the content team

**Runtime:** 80 minutes across 10 videos  |  **Deck:** 25 slides in, 26 out  |  **Exercises:** 7, 8 and 9

This module needs Python and pytest but no API key and no Claude Code. Learners run
tests locally and prompt in the browser. Saying that out loud in the first video
saves a support question.

It contains the one outright factual error in the delivered decks. It is corrected,
and the correction matters more than it looks.

## What changed from the delivered material, and why

### Deck, two edits and one new slide

1. **Slide 12 described nested-loop growth as exponential. It is quadratic.**
   Corrected on revised slide 13. This was not a pedantic fix: Exercise 8
   demonstrates exactly this growth, so the deck contradicted the lab, and a learner
   who repeats "exponential" in a code review loses credibility in front of their
   team. The same slide now also carries Exercise 8's correctness lesson.
2. **Slide 22 suggested an approved emoji as a review sign-off.** An emoji is not a
   review outcome. It now asks for a verdict in words, matching the named severity
   groups Exercise 9 teaches.
3. Exercise map at the front.

### Labs

All three vendor labs were sound in intent and needed a voice pass plus starter
files, which had never been supplied. Exercise 9's vendor document also opened with
an authoring note addressed to the course author, referencing a Udemy course. It is
removed with no trace, and it must not come back in a re-import.

## Do not undo these

1. **Exercise 7 shows three failures on a fresh run, not one.** Two are a `KeyError`,
   one is an assertion. An earlier version of the defect register claimed the first
   defect masks the second, which is wrong: pytest runs each test independently, so
   both are visible from the start. Verified by running it. The lesson still works and
   is arguably better: the learner fixes the `KeyError`, re-runs, and the suite is
   still red.
2. **The correct fix to Exercise 7 is underdetermined, on purpose.** The tests call
   `restock()` with two arguments and never pass a threshold, so the learner has to
   introduce one with a default, and the two fixtures constrain it to between 2 and 7
   inclusive. Verified against candidate values. This makes the tests a specification,
   which is the best thing in the lab. Do not "fix" the tests to remove the ambiguity.
3. **Exercise 8 has a correctness trap.** The function counts every occurrence, so
   duplicates count each time. Optimising with a `set` is dramatically faster and
   returns 10382 instead of 24326. A `Counter` is both fast and correct. The lab
   checks correctness before it celebrates the timing, and the assertion sits above
   the line that prints the speedup deliberately. Do not reorder those.
4. Exercise 8's baseline is tuned to about 2.2 seconds so the audience feels it
   without watching silence. If you change the data size, retune and update the
   register.

## What is in this folder

| Path | What it is | Who edits it |
|---|---|---|
| `01-deck/original/` | The vendor deck exactly as delivered. Untouched. | Nobody. It is the baseline a change is diffed against. |
| `01-deck/revised/` | The corrected deck. | You, or nobody, depending on your answer to the question below. |
| `01-deck/deck-changelog.md` | Every change, with the old wording, the new wording and why. Generated from the same declaration that made the edits, so it cannot drift. | Generated. Do not hand-edit. |
| `02-facilitator/recording-script.md` | What the trainer reads while recording. Per video: runtime, what is on screen, narration guidance, take-two risks. **Trainer only.** | The trainer, or you with the trainer. |
| `02-facilitator/*.pptx` | The teleprompter deck, generated from that script. **Trainer only, names planted defects.** | Generated from the script. Edit the script. |
| `03-labs/exercise-NN-*/lab.md` | The learner handout. Source of truth. | You. |
| `03-labs/exercise-NN-*/lab.docx` | Generated from `lab.md`. | Nobody. Edits here are lost on the next generation. |
| `03-labs/exercise-NN-*/starter/` | Starter code. Read the warning below. | Nobody, without reading the defect register first. |
| `04-assessment/assessment.md` | Ten self-check questions, no answers. | You. |
| `04-assessment/answer-key.md` | Answers, Core or Stretch tag, where each is taught, and what a wrong answer diagnoses. **Trainer only.** | You, in the same commit as the questions. |
| `04-assessment/changelog.md` | What changed from the vendor assessment, question by question. | You. |

## The one rule that matters most

**The code in `starter/` is deliberately broken. Do not fix it.**

Every such file carries a `# TEACHING ARTEFACT - DO NOT FIX` header. The bugs are
the teaching material. A well-meaning cleanup pass destroys the exercise, and it
will not be obvious from the diff that anything was lost.

Before touching any starter file, read `docs/lab-defect-register.md`. It records
every planted defect, why it is there, and what a learner is supposed to discover.
If you genuinely need a corrected version of a file, add a sibling suffixed
`_solution.py` and leave the original alone.

The answer-revealing comments were removed from these files deliberately, because
the labs tell learners to open them. Do not put explanatory comments back.

## Before you change anything here

1. Read `CLAUDE.md` at the repository root. It carries the writing conventions,
   including no em dashes, no model version names anywhere, and the approved
   ZaranTech statistics.
2. Read `docs/course-context.md`. It explains why the programme is shaped this way,
   including the decisions you might otherwise reverse by accident.
3. If you are editing a lab, read `docs/lab-authoring-spec.md`. It governs structure,
   voice and how prompts are presented.
4. If you are editing the assessment, read `docs/assessment-spec.md`. The answer
   distribution rule is mechanical and it is the main thing being fixed.
5. Regenerate, do not hand-edit, anything marked generated above.

## Questions only you can answer

The full list is in `docs/open-questions-for-vendor.md`. The one that blocks the
deck work is this: **are the Google Slides decks your live master?**

If they are, apply the changes from `deck-changelog.md` in Slides and ignore the
revised PPTX entirely. If you would rather adopt the revised PPTX, import it and it
becomes the master. Doing both will produce two diverging decks, which is worse than
doing neither.
