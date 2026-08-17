# Module 1: Fundamentals of Claude for Developers
## Guidance for the content team

**Runtime:** 74 minutes across 8 videos  |  **Deck:** 25 slides in, 27 out  |  **Exercises:** 1, 2 and 3

This module is the learner's first hour and it is **browser only**. No terminal,
no repository cloning, no API key. That is deliberate: a learner can start the
programme before finishing any setup, and setup friction in the first hour is where
cohorts lose people. Claude Code is previewed here and first used in Module 2.

Keep it that way. If a change to this module introduces a terminal step, it has
broken the design.

## What changed from the delivered material, and why

### Deck, four edits and two new slides

1. **Slide 8 named specific model versions and claimed benchmark leadership.** Both
   are now gone, replaced with tier-selection guidance. A named version on a
   published video dates it permanently, and organisational policy is not to quote
   benchmark results. The same slide also had a subject-verb disagreement, "leads"
   for "lead", which would have sat on screen forever.
2. **Slide 7 claimed Claude produces fewer hallucinations than unnamed competitors.**
   We cannot substantiate that comparison, so it now makes a concrete, defensible
   claim instead: it states uncertainty rather than inventing an API.
3. **Slide 4 said Claude "securely processes" codebases.** Processing is not
   inherently secure and the word invites a compliance question the slide cannot
   answer.
4. **Slide 6 gained the persistent project context file**, which no slide in the
   original programme mentioned at all.
5. **New slide: Repo as Context, Repo as Workspace.** This is the highest-value
   addition to the whole programme. Attaching a repository to the Claude app syncs
   file contents as reading material and grants no commit, pull request or history
   access. Claude Code is what operates on a repository. It is the single most common
   learner confusion and the assessment tests it twice.
6. **New slide: exercise map**, for section navigation in a recorded course.

### Labs

- **Exercise 1** referred to a code snippet "provided in the lab" and supplied none.
  It is now `starter/running_average.py`. The vendor lab also offered "a sandbox
  environment that simulates Claude" as an alternative. No such sandbox exists, and
  all references are removed.
- **Exercise 2 did not exist.** Module 1 shipped Exercise 1 and Exercise 3 with
  nothing in between. It has been authored in-house and covers the prompt anatomy the
  deck teaches and no other lab practises. If your Exercise 2 does exist and was
  simply not shared, reconcile the two rather than shipping both.
- **Exercise 3** asked learners to author a review checklist from scratch. Authoring
  it consumes the time that should go into applying it, so the checklist is now
  supplied in the handout and extending it is the optional step. The snippet it
  reviews, also missing, is now `starter/order_sync.py`.

## Do not undo these

1. `running_average.py` has one quiet defect and no exception. The lab is built so
   the learner discovers that a fluent explanation can describe intended rather than
   actual behaviour. Do not add a comment, a hint, or a "note the loop bound" aside.
2. `order_sync.py` contains fifteen defects including a hardcoded fake key and two
   SQL injections. The expected verdict is "draft only, not production ready". The
   handout must not state that verdict; the steps are designed so the learner reaches
   it.
3. The fake key uses an obvious `sk-live-` example marker. Do not make it look more
   realistic, and do not replace it with a real-format key.

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
