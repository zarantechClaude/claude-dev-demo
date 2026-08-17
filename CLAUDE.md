# claude-dev-demo

Courseware repository for the ZaranTech programme **Claude AI for Developers (AI-led SDLC)**.

This repo is not a product. It is teaching material, and some of the code in it
is **deliberately broken**. Read the warning below before changing anything.

## Critical convention: intentional defects

Files under any `03-labs/*/starter/` directory contain planted bugs, security
holes, and performance problems. They are the teaching material. **Do not fix
them.**

Every such file carries a header comment beginning `# TEACHING ARTEFACT - DO NOT
FIX`. If you see that header, treat the defects as load-bearing. If a task
genuinely needs a corrected version, create a sibling file suffixed `_solution.py`
and leave the original untouched.

Every planted defect is documented in `docs/lab-defect-register.md`. If you add
or change a lab file, update that register in the same commit.

## Repository layout

```
docs/                              Programme-level documents, read these first
module-1-fundamentals/
module-2-claude-code/
module-3-debugging/
module-4-claude-api/
module-5-advanced-capstone/
```

Every module folder has the same five parts:

| Folder | Contents |
|---|---|
| `README.md` | Guidance for the content team. What is here, what changed, what to do. |
| `01-deck/` | `original/` vendor deck, `revised/` corrected deck, `deck-changelog.md` |
| `02-facilitator/` | Recording deck and recording script for the trainer |
| `03-labs/` | One folder per exercise: lab document, starter code, vendor original |
| `04-assessment/` | Rewritten assessment, answer key, `original/` vendor PDF |

## Delivery format

This programme is delivered as a **self-recorded on-demand video course**, not as
live instructor-led sessions. That decision governs everything:

1. There is no 60-minute-per-module budget. Total runtime is about 7.5 hours.
2. No single video runs longer than 12 minutes. A 25-slide deck becomes three or
   four lectures. Long labs split across videos.
3. Lab documents are **learner handouts**, not trainer scripts. They are written
   in second person to the learner and carry explicit pause instructions, because
   a recorded lab has no natural moment where the room catches up.
4. Assessments are self-check. The capstone carries completion.

An earlier version of this programme was designed for live 60-minute sessions.
Any document still written in that voice ("ask learners to", "have learners") is
stale and needs the voice pass described in `docs/course-context.md`.

## Programme constraints

1. Five modules, fifteen exercises, numbered globally 1 to 15 rather than per
   module. Exercise 2 was missing from the vendor pack and has been authored
   in-house.
2. Module 1 is **browser only**. No terminal, no repo cloning, no API keys.
   Claude Code is previewed, not used.
3. Module 2 is the first module requiring a local Claude Code installation.
4. Module 4 is the first module requiring an API key.
5. Exercises 10, 11, 12 and 15 form a dependency chain. Breaking the environment
   variable name in any one of them breaks the rest.

## Writing conventions

- No em dashes anywhere, in learner-facing or internal content.
- Short paragraphs, numbered steps, bullets, tables. Practical and scannable.
- Approved ZaranTech statistics only: 400+ courses, 32,000+ learners trained,
  350+ corporate clients, 37+ countries served. Never substitute or invent numbers.
- Never promise jobs, certifications, or business outcomes.
- Do not invent testimonials, client names, awards, or pricing.
- Do not quote benchmark results or leaderboard positions.
- **Do not name a specific Claude model version anywhere**, in slides, labs, or
  code. Teach the tier-selection habit instead. Version names change faster than
  a course refresh cycle, and a named version on screen dates a published video
  permanently.

## Code conventions for lab snippets

- Python 3.11 or later. Python only across the whole programme. Node and Java
  branches were removed deliberately, to keep learner setup to one runtime.
- `ANTHROPIC_API_KEY` is the environment variable name everywhere. The official
  SDK reads it from the environment by default. The lab scripts still read it
  explicitly and pass it in, so that a missing key produces our diagnostic message
  rather than an SDK stack trace. Do not claim on camera that the code relies on
  the SDK default, because it does not.
- The model id is read from a `MODEL` environment variable and every script fails
  with a clear message if it is unset. No script hardcodes a model id.
- Lab snippets must be readable in under 60 seconds. If reading takes longer, the
  snippet is too long for a single video segment.
- Defects must be realistic, not contrived. A learner should plausibly meet this
  bug at work.
- Never include a credential that could be mistaken for live. The one fake key in
  the repo, in `order_sync.py`, uses an obvious `sk-live-` example marker and is
  itself the teaching point.
- No PII in lab data, even synthetic. Use `user@example.com` style placeholders.

## Before you start a task here

Read `docs/course-context.md`. It carries the decisions, the open questions, and
the vendor-material gaps that are not visible from the code alone. Then read the
`README.md` of the module you are working in.

Three things that look like bugs and are not:

1. `exercise-07`'s test suite has three failures on a fresh run, not one. Two are
   a `KeyError`, one is an assertion. Fixing the `KeyError` leaves the suite red.
   That is the lesson.
2. `exercise-15`'s capstone skeleton ships with one failing test, caused by a
   patch-target mistake the learner has to find.
3. `exercise-08` returns a deliberately large match count. An optimisation that
   uses a `set` is much faster and returns the wrong number.

All three are documented in `docs/lab-defect-register.md`.
