# Claude AI for Developers

Courseware for the ZaranTech programme **Claude AI for Developers (AI-led SDLC)**.
Five modules, fifteen exercises, delivered as a self-recorded on-demand video course
of roughly seven and a half hours.

This repository holds everything needed to record and publish the programme: the
corrected decks, the learner lab handouts, the starter code, the trainer recording
scripts, and the self-check assessments.

## Content team, start here

You are here to help maintain this material. Read these three files, in this order,
then go to the module you are working on.

| Order | File | Why |
|---|---|---|
| 1 | `CLAUDE.md` | The conventions. Includes the one rule that matters most: some of the code here is deliberately broken and must stay that way. |
| 2 | `docs/course-context.md` | Why the programme is shaped the way it is. Reading it prevents you reversing a deliberate decision by accident. |
| 3 | `module-N-*/README.md` | Per module: what is in each folder, what changed from the delivered material and why, and what must not be undone. |

Then, depending on what you are editing:

| Editing | Read first |
|---|---|
| A lab handout | `docs/lab-authoring-spec.md` |
| An assessment | `docs/assessment-spec.md` |
| A deck | that module's `01-deck/deck-changelog.md` |
| Anything in `starter/` | `docs/lab-defect-register.md`, without exception |

**One decision we need from you before the deck work can settle.** Are the Google
Slides decks your live master? If so, apply the changes from each
`deck-changelog.md` in Slides and ignore the revised PPTX files. If you would rather
adopt the revised PPTX, import it and it becomes the master. Doing both produces two
diverging decks. The rest of the open questions are in
`docs/open-questions-for-vendor.md`, numbered so you can reply against them.

## Layout

```
docs/                          Programme-level documents
module-1-fundamentals/
module-2-claude-code/
module-3-debugging/
module-4-claude-api/
module-5-advanced-capstone/
```

Every module folder is the same shape:

```
README.md              Guidance for the content team
01-deck/               original/ vendor deck, revised/ corrected deck, changelog
02-facilitator/        Recording script and teleprompter deck. Trainer only.
03-labs/               One folder per exercise: lab.md, lab.docx, starter/, vendor-original/
04-assessment/         assessment.md, answer-key.md, changelog.md, original/
```

## The programme at a glance

| Module | Subject | Runtime | Exercises | Needs |
|---|---|---|---|---|
| 1 | Fundamentals of Claude for developers | 74 min | 1, 2, 3 | Browser only |
| 2 | Claude for coding tasks (Claude Code) | 89 min | 4, 5, 6 | Claude Code |
| 3 | Debugging, optimization and code reviews | 80 min | 7, 8, 9 | Python, pytest |
| 4 | Building with the Claude API | 87 min | 10, 11, 12 | API key with credit |
| 5 | Advanced workflows and the capstone | 100 min | 13, 14, 15 | API key with credit |

Exercises are numbered globally, not per module. Exercise 2 was missing from the
delivered pack and was authored in-house.

Full detail, including per-video splits and the dependency chain between Exercises
10, 11, 12 and 15, is in `docs/programme-map.md`.

## Documents

| File | For | Contents |
|---|---|---|
| `docs/course-context.md` | Everyone | Decisions, reasoning, and what changed from the earlier live-session design |
| `docs/programme-map.md` | Everyone | Modules, exercises, runtimes, video splits, dependencies |
| `docs/lab-authoring-spec.md` | Content team | How a lab document is structured and voiced |
| `docs/assessment-spec.md` | Content team | How the questions are built, including the answer-distribution rule |
| `docs/capstone-brief.md` | Learners, at the end of Module 4 | Scope, submission, and the marking thresholds |
| `docs/lab-defect-register.md` | **Trainer and content team only** | Every planted defect, verified by running the code |
| `docs/recording-hygiene.md` | Trainer | Key handling, browser and terminal hygiene, what dates a video |
| `docs/open-questions-for-vendor.md` | Content team | What only you can decide, numbered |

Three files must never reach a learner: `docs/lab-defect-register.md`, every
`02-facilitator/` file, and every `04-assessment/answer-key.md`.

## Working on this repository

```bash
pip install pytest flask python-dotenv anthropic
```

Two conventions worth knowing before your first commit:

1. **`lab.md` is the source of truth and `lab.docx` is generated from it.** Editing
   the DOCX is always the wrong move, because the next generation overwrites it.
   Same for the deck changelogs and the facilitator decks.
2. **`ANTHROPIC_API_KEY` and a `MODEL` read from configuration**, in every script,
   with no model identifier hardcoded anywhere. Exercises 10, 11, 12 and 15 form a
   chain that breaks if either convention changes in one place only.

To confirm the teaching artefacts still behave as documented, which the trainer
should do on the recording machine on the recording day:

```bash
# Exercise 7: expect 3 failures, two KeyError and one assertion
cd module-3-debugging/03-labs/exercise-07-debug-buggy-sample/starter && pytest -q

# Exercise 8: expect 24326 matches, in roughly 2 to 3 seconds
python module-3-debugging/03-labs/exercise-08-slow-implementation/starter/slow_lookup.py

# Exercise 15: expect 3 passed, 1 failed. The failure is deliberate.
cd module-5-advanced-capstone/03-labs/exercise-15-summarizer-microservice/starter/capstone_skeleton && pytest -q
```

If any of those three produces a different result, something has been "fixed" that
should not have been. Check `docs/lab-defect-register.md` before changing anything
else.

---

© Copyright 2026, ZaranTech LLC. All rights reserved.
