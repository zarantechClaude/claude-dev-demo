# Module 2 labs: Claude for Coding Tasks (Claude Code)

Three exercises, 54 minutes of lab time. Exercise numbering is global across the
programme, not per module, so Module 2 starts at Exercise 4.

Module 2 is the first module that needs a local Claude Code installation. Module 1 was
browser only, deliberately, so a learner can start the programme before finishing any
setup. State that step change in the course intro so nobody arrives here unprepared.

## Exercises

| Ex | Title | Duration | You need | Starter code | Videos |
|---|---|---|---|---|---|
| 4 | [Create a project brief for Claude Code](exercise-04-project-brief/lab.md) | 12 min | Terminal, Claude Code, a small project of the learner's own | None. Authored during the exercise | 1 |
| 5 | [Build, refactor and review a registration endpoint](exercise-05-registration-endpoint/lab.md) | 20 min | Terminal, Claude Code | `exercise-05-registration-endpoint/starter/messy_registration.py` | 2 |
| 6 | [Improve existing code with documentation and tests](exercise-06-docs-and-tests/lab.md) | 22 min | Terminal, Claude Code, pytest | `exercise-06-docs-and-tests/starter/undocumented_utils.py` | 2 |

No lab in this module needs an API key. That requirement starts in Module 4.

## Environment

| Requirement | Needed |
|---|---|
| Browser | Yes |
| Terminal | Yes |
| Claude Code | Yes |
| API key | No |

Python 3.11 or later. Python only, across the whole programme. `pip install pytest`
for Exercise 6. `pip install flask` is optional in Exercise 5, because reading the
starter file is enough.

## What each exercise is actually teaching

Useful when writing the recording script, because the stated topic and the real lesson
are not the same thing in any of the three.

1. **Exercise 4** teaches that project context belongs in a file at the repo root that
   Claude Code reads by itself, not in a message pasted at the top of a chat. A file
   survives across sessions and it is version controlled. The vendor lab framed this
   as pasting a brief into the conversation, and the deck spends six slides on
   organising project context without ever mentioning a persistent context file. This
   is the largest content gap in the module and Exercise 4 is where it is closed.
2. **Exercise 5** teaches the preservation constraint. A naive refactor prompt returns
   cleaner code and a change that cannot ship on its own. The learner meets that
   before being told about it, then prompts again with the constraint made explicit.
3. **Exercise 6** teaches that a green suite measures the tests you have and says
   nothing about the tests you do not have. The generated suite passes. The exercise is
   the hunt afterwards, verified by calling the functions rather than by asking for a
   list.

## Sequencing note

Exercise 6 produces a test suite that Module 3 opens by running again. Keep Exercise 6
at the end of Module 2 rather than moving it into Module 3, or that link is lost.

## Conventions for anyone editing these labs

1. `docs/lab-authoring-spec.md` governs structure, voice and prompt handling. Match it
   exactly. Fifteen labs should read as one programme.
2. `lab.md` is the source of truth. The DOCX is generated from it.
3. Starter files carry a `# TEACHING ARTEFACT - DO NOT FIX` header. The defects in them
   are the teaching material. Do not repair them, and do not describe them in the
   learner-facing lab.
4. Never name a Claude model version.
5. No em dashes.
