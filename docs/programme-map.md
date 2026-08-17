# Programme map

One page showing every module, every exercise, the runtime, and what depends on
what. If you change a duration or a dependency, change it here too.

## Runtime

Recorded pace, no learner wait time. These are video minutes, not session minutes.

| Module | Deck | Labs | Module total |
|---|---|---|---|
| Course intro | 12 min | none | 12 min |
| 1. Fundamentals | 35 min | Ex1 12, Ex2 12, Ex3 15 | 74 min |
| 2. Claude Code | 35 min | Ex4 12, Ex5 20, Ex6 22 | 89 min |
| 3. Debugging and reviews | 35 min | Ex7 15, Ex8 15, Ex9 15 | 80 min |
| 4. Claude API | 35 min | Ex10 12, Ex11 22, Ex12 18 | 87 min |
| 5. Advanced and capstone | 35 min | Ex13 18, Ex14 12, Ex15 35 | 100 min |
| **Total** | | | **about 7 hours 30 min** |

Hands-on lab time alone is about 4 hours.

## Video granularity

No single video runs over 12 minutes.

The authoritative per-video split is in each module's
`02-facilitator/recording-script.md`, which was built against this cap and checked
to add up. In summary:

| Asset | Split into |
|---|---|
| Each deck | 4 lectures |
| Ex1, Ex2, Ex4, Ex10, Ex14 (12 min) | 1 video each, at the cap with no headroom |
| Ex3, Ex7, Ex8, Ex9 (15 min) | 2 videos each |
| Ex12, Ex13 (18 min) | 2 videos each |
| Ex5, Ex6, Ex11 (20 to 22 min) | 2 videos each |
| Ex15 (35 min) | 3 videos: scaffold the service, integrate the API, tests and docs |

An earlier version of this table said "everything else, 1 video", which was wrong
for five exercises that exceed twelve minutes.

Add a section-map slide to the front of each deck. In a recorded course learners
navigate by section rather than by the trainer's voice, so each module needs a
visible list of what is coming.

## Exercise inventory

Exercises are numbered globally across the programme, not per module. Exercise 2
did not exist in the vendor pack and was authored in-house.

| Ex | Module | Title | Duration | Needs | Starter code |
|---|---|---|---|---|---|
| 1 | 1 | Explore Claude's interface and explain sample code | 12 min | Browser | `running_average.py` |
| 2 | 1 | Structure a developer prompt | 12 min | Browser | none, prompt only |
| 3 | 1 | Code review checklist | 15 min | Browser | `order_sync.py` |
| 4 | 2 | Create a project context file for Claude Code | 12 min | Claude Code | none, authored live |
| 5 | 2 | Build, refactor and review a registration endpoint | 20 min | Claude Code | `messy_registration.py` |
| 6 | 2 | Improve existing code with documentation and tests | 22 min | Claude Code, pytest | `undocumented_utils.py` |
| 7 | 3 | Debug a buggy code sample | 15 min | pytest | `buggy_inventory.py`, `test_buggy_inventory.py` |
| 8 | 3 | Debug a slow implementation | 15 min | Python | `slow_lookup.py` |
| 9 | 3 | PR diff review | 15 min | Browser | `sample_pr.diff` |
| 10 | 4 | Configure API keys and send a first prompt | 12 min | API key | `verify_key.py`, `minimal_call.py` |
| 11 | 4 | Build a CLI for structured prompting | 22 min | API key | `cli_reference.py` |
| 12 | 4 | Manage minimal conversation history | 18 min | Ex11 output | `history_starter.py` |
| 13 | 5 | Turn a feature brief into a spec and tickets | 18 min | Browser, Mermaid | none, prompt only |
| 14 | 5 | Generate and refine a configuration file | 12 min | Browser | none, prompt only |
| 15 | 5 | Build a summariser microservice (the capstone) | 35 min | API key | `capstone_skeleton/` |

## Dependency chain

Four exercises form a hard chain. Breaking the environment variable name or the
model configuration in any one of them breaks everything downstream.

```
Ex10 (key in .env, first call)
  -> Ex11 (CLI with structured prompt template)
       -> Ex12 (conversation history and relevance selection)
            -> Ex15 (capstone service)
```

`history_starter.py` exists so that a learner who did not finish Exercise 11 can
still do Exercise 12. Without it, Exercise 12 hard-depends on Exercise 11's output.

Two softer linkages worth preserving:

1. Exercise 6 produces a test suite, which is why it sits at the end of Module 2
   rather than in Module 3. Note that the suite a learner leaves is **green**, with
   any parked bug marked `xfail`, so Module 3 cannot simply open by running it and
   watching it fail. The recording script opens by running it green, reading the
   parked `xfail` line aloud, removing the marker on camera, and re-running red.
2. Exercise 15 **is** the capstone, not a separate lab that precedes it. Running
   Exercise 15 as a lab and then setting a capstone duplicates the same work.

## Escalating environment requirements

| Module | Browser | Terminal | Claude Code | API key |
|---|---|---|---|---|
| 1 | Yes | No | No | No |
| 2 | Yes | Yes | Yes | No |
| 3 | Yes | Yes | No | No |
| 4 | Yes | Yes | No | Yes |
| 5 | Yes | Yes | No | Yes |

Module 1 is deliberately browser only, so a learner can start the programme
before finishing any setup. State the requirements for Modules 2 and 4 in the
course intro so nobody hits them unprepared.

## Capstone timing

The vendor deck introduces, builds, and evaluates the capstone inside Module 5.
That does not work even in a recorded format, because the learner needs time to
actually build it.

| When | What |
|---|---|
| Module 1, deck | Learner writes down one use case from their own work. This becomes their capstone subject. |
| End of Module 4 | Capstone brief is issued. `docs/capstone-brief.md`. |
| Module 5, labs | Ex13 and Ex14 build the planning and configuration skills the capstone needs. |
| Module 5, Ex15 | The capstone build itself, across three videos. |
| After Module 5 | Submission and review against the rubric in the capstone brief. |
