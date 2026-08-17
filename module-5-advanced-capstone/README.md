# Module 5: Advanced Developer Workflows and Capstone
## Guidance for the content team

**Runtime:** 100 minutes across 12 videos  |  **Deck:** 24 slides in, 26 out  |  **Exercises:** 13, 14 and 15

The longest module, and the one whose structure changed most.

**The capstone brief is issued at the end of Module 4, not here.** That is the single
most important structural change to the programme. The vendor design introduced,
built and evaluated the capstone inside one module, which does not work in any format,
because the learner needs time to actually build something.

**Exercise 15 is the capstone build itself**, not a rehearsal that precedes it. Both
are a service that calls the API to summarise code. Running Exercise 15 as a lab and
then setting a separate capstone duplicates the same work.

## What changed from the delivered material, and why

### Deck, three edits and two new slides

1. **Slide 16 scoped the capstone as "a comprehensive end-to-end application from
   scratch".** That is several times what it actually is, and over-scoping is the most
   common reason a capstone fails. It is now one service with two endpoints, stated
   plainly, with the note that the brief was issued at the end of Module 4.
2. **Slide 12 said to automate documentation in CI "using Claude APIs"** without
   naming the mechanism. A pipeline has no terminal to prompt, so it now says to call
   the API from a non-interactive script. Otherwise a learner tries to run an
   interactive tool in CI and fails.
3. **New slide: How the Capstone Is Marked.** The vendor evaluation was three slides
   of adjectives with no thresholds, so two reviewers could not have marked
   consistently. Since the capstone carries completion for this programme, the
   criteria have to be defensible and visible in advance. Full thresholds are in
   `docs/capstone-brief.md`.
4. Slide 20 rewritten to point at those thresholds, plus the exercise map.

Note that the new marking slide was **inserted alongside** the original evaluation
slides rather than replacing them, so the on-screen order is adjectives, thresholds,
adjectives. If you want to consolidate, that is a reasonable next edit and the
recording script already leads with the thresholds slide.

### Labs

- **Exercise 15 is split into three explicitly numbered parts** with hard stopping
  points, because it becomes three videos: scaffold the service, integrate the API and
  design the prompt, then tests and documentation.
- **Exercise 14 never builds a container.** It generates and reviews a configuration
  file. Docker is not a prerequisite and is not listed as one.
- Exercises 13 and 15 both carried research citation residue in learner-facing text.
  Removed. Your master copies still contain it.

## Do not undo these

1. **`summariser.py` ships with TODO prompts rather than a working prompt, deliberately.**
   Prompt design is what the capstone is graded on and carries the most weight, so it
   must not be pre-written. Do not helpfully fill it in.
2. **The capstone skeleton ships with one failing test, on purpose.** `app.py` imports
   `summarise_code` directly, so patching the `summariser` module attribute does not
   intercept the call. The learner has to work out that the patch target must be
   `app.summarise_code`. Verified: a fresh run reports 3 passed, 1 failed, and it fails
   with no key and no network, so it reproduces for everyone.

   The hint is already in the file: the sibling test patches `app.summarise_code` and
   passes. A comment that explained the cause in plain language was removed, because it
   gave away more than the sibling test does. This teaches patch targeting, which is the
   most common reason AI-generated tests fail.
3. **The two 413 responses in the skeleton have different bodies on purpose**, one from
   the application's own length check and one from the framework's body-size limit, so
   the lab can ask a learner to tell them apart from the response alone. Keep both.
4. The skeleton runs with `debug=True`. That is a finding Exercise 14's review checklist
   is designed to catch, so it is intentional, but it means an unhandled exception
   renders an interactive traceback. Worth knowing before recording.

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
