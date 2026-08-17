# Module 2: Claude for Coding Tasks (Claude Code)
## Guidance for the content team

**Runtime:** 89 minutes across 9 videos  |  **Deck:** 25 slides in, 27 out  |  **Exercises:** 4, 5 and 6

This is the first module that needs Claude Code installed locally. State that in
the course intro as well as here, so nobody reaches it unprepared.

It is also the module with the largest content gap in the delivered material, and
the gap is now filled. Read the next section before editing anything.

## What changed from the delivered material, and why

### The gap that mattered

The vendor deck has **six slides on organising project context and never mentions
the file that does it**, and no slide in the deck carries any code at all. Exercise 4
compounded it by framing the work as pasting a project description into a chat
window, which is the web-app model rather than the Claude Code model.

Fixed in three places at once, and they need to stay consistent with each other:

1. **New slide: The Project Context File.** A `CLAUDE.md` at the repository root
   that Claude Code reads automatically. A file beats a pasted message because it
   survives every session and it is version controlled.
2. **Exercise 4 rewritten** around authoring that file rather than pasting a brief.
   The worked example it shows is this repository's own `CLAUDE.md`, specifically the
   intentional-defects section, which is the highest-value paragraph in it.
3. **Slides 6 and 7 reframed** from uploading and pasting to letting Claude Code read
   the repository directly.

### Deck, three edits and two new slides

Slide 13 on refactoring now states the preservation constraint explicitly, because
that is the core lesson of Exercise 5 and the deck previously said only "modernize
the syntax completely". Plus the exercise map at the front.

### Labs

- **Exercise 5** rewritten around a trap that the vendor version defused. See below.
- **Exercise 6** had to be rebuilt rather than voice-passed: an earlier draft
  documented three functions that do not exist in the actual starter file.

## Do not undo these

1. **Exercise 5 is the most carefully designed lab in the programme and it is easy to
   break.** `messy_registration.py` uses unsalted MD5 password hashing. A naive
   "refactor into cleaner modular code" prompt will normally replace it with a modern
   hash, which is correct security advice **and** a breaking change: every existing
   stored hash becomes unverifiable and no existing user can log in.

   The lab walks the learner into this deliberately: naive prompt first, then a step
   that surfaces the consequence, then a second prompt carrying an explicit
   preservation constraint. **Do not add the constraint to the first prompt.** An
   earlier draft did, and it defused the entire lab.
2. `undocumented_utils.py` has **no planted bugs**. It has three working functions
   with real edge cases that generated tests routinely miss. The defect register
   lists them, for checking learner submissions. Do not list them in the handout.
3. Exercise 4 has learners write a `CLAUDE.md` for a project of their own, not for
   this repository, because this repository already has one and writing over it would
   either clobber it or show no effect.

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
