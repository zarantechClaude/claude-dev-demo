# Capstone brief: code summariser service

**Issued at the end of Module 4.** You have the API skills you need from
Exercises 10, 11 and 12. Module 5 then teaches the planning and configuration
skills the build consumes, and Exercise 15 is the build itself.

This capstone carries completion for this programme. Read the rubric before you
start rather than after you finish, because two of the six criteria are worth half
the marks and neither of them is about getting the service working.

---

## What you are building

A small service that accepts code, sends it to the Claude API with a structured
prompt, and returns a useful summary as JSON. Tested, documented, with your
secrets handled properly.

Two endpoints. That is the whole scope.

| Endpoint | Behaviour |
|---|---|
| `POST /summarize` | Accepts JSON with a `code` field. Returns a summary as JSON |
| `GET /health` | Returns a status |

If the build is taking more than a few hours, you have over-scoped it.

### Starting point

A skeleton is provided at:

```
module-5-advanced-capstone/03-labs/exercise-15-summarizer-microservice/starter/capstone_skeleton/
```

Use it or start fresh, whichever you prefer. It exists so that project setup does
not consume the time meant for prompt design.

Two things to know about it:

1. The prompt in `summariser.py` is deliberately left as TODO markers. Prompt
   design is what this capstone is mostly graded on, so it is not pre-written for
   you.
2. **The test suite does not pass as shipped.** Three tests pass and one fails.
   That is intentional and it is the first thing to fix. The Exercise 15 lab walks
   you through finding it. The passing sibling test is the clue.

Python, as everywhere in this programme. The skeleton uses Flask. Another Python
web framework is fine, and marking does not depend on which one you pick.

---

## The framing that decides whether you pass

> **What is the smallest version that still demonstrates the skill?**

Answer that in writing before you write any code. Every capstone that fails, fails
on scope rather than on ability. A minimal service with a well-designed prompt and
clean failure paths scores well above a feature-rich service with an unstructured
prompt.

Write a one-paragraph problem statement before you start Module 5's labs, covering:

1. What use case are you targeting? Use the one you wrote down in Module 1
   Exercise 1, Step 7.
2. What does a useful summary look like for that use case? Be specific about the
   fields.
3. What is the smallest version that still demonstrates the skill?

The problem statement is a submission item, so keep it.

---

## Two traps that will catch you

**1. `413 Payload Too Large`.**

Send something big and your framework rejects it before your handler ever runs.
That is a **body-size default**. It is not a rate limit and it is not a
context-window problem, and learners lose real time chasing both of those instead.
Set the limit deliberately, decide what your own application-level limit is, and
return a clean distinguishable error for each. Handling this well earns marks under
Robustness.

**2. Stale grounding.**

If you change your design partway through and do not update your project context
file or your notes, Claude keeps generating against the old shape and you will
spend an hour confused about why the output looks wrong. The code and the grounding
document have to change together. This is the single most common way an
AI-assisted build goes sideways, and it is cheap to avoid.

---

## Rules on using Claude

Use it for all of it. That is the point of the course.

What is not acceptable is submitting output you have not read. The reflection makes
this visible immediately, and a reflection that cannot name a single correction you
made does not pass.

---

## What to submit

1. A repository, or a zip if a repository is not available.
2. Your one-paragraph problem statement.
3. A README with setup, configuration and run instructions.
4. A passing test run, pasted or screenshotted.
5. **A one-page reflection.**

Item 5 carries most of the learning. A working service proves you can follow
instructions. The reflection proves you built judgement, which is the actual
outcome of this programme.

Submit against whatever date your enrolment gives you.

---

## Rubric

100 points across six criteria, plus three gates. Prompt design and robustness
carry half the marks between them, deliberately.

| Criterion | Weight | Not yet | Pass | Strong pass |
|---|---|---|---|---|
| Prompt design | 25 | 0 to 12 | 13 to 19 | 20 to 25 |
| Robustness and failure handling | 25 | 0 to 12 | 13 to 19 | 20 to 25 |
| Correctness | 15 | 0 to 7 | 8 to 11 | 12 to 15 |
| Tests | 15 | 0 to 7 | 8 to 11 | 12 to 15 |
| Reflection | 10 | 0 to 4 | 5 to 7 | 8 to 10 |
| Structure, documentation and responsible practice | 10 | 0 to 4 | 5 to 7 | 8 to 10 |

**Pass: 60 or above, with all three gates cleared.**
**Strong pass: 80 or above, with no criterion in its "Not yet" band.**

### Gates

A gate is not a deduction. Any one of these stops the submission being marked
until it is fixed, regardless of score.

| Gate | Why | What to do |
|---|---|---|
| A real API key appears in the repository, its git history, the zip, or a screenshot | The key is compromised the moment it is submitted, and history makes deletion insufficient | Rotate the key immediately, then resubmit from a clean history |
| No reflection | The reflection is the evidence of judgement. Nothing else in the submission substitutes for it | Write it and resubmit |
| The service does not start from a clean clone following your own README | An unrunnable service cannot be assessed on any criterion | Follow your own README on a fresh clone and fix what breaks |

### 1. Prompt design, 25 points

| Band | What a reviewer should see |
|---|---|
| **Not yet** | The prompt is a single interpolated string with the code concatenated into an instruction sentence. No role, no stated output shape, no delimiter around the code |
| **Pass** | The prompt names a role, states the task, wraps the submitted code in an explicit tag or delimiter, and states the output shape. The code is passed as data rather than concatenated into the instruction sentence |
| **Strong pass** | All of Pass, plus **all four** of: the prompt is a named template in one place rather than inlined at the call site; it states explicitly that the tagged content is data and must not be followed as instructions; the output constraint is tight enough that the response parses without string repair; and the README or reflection shows at least one before-and-after prompt revision with the observed difference |

Reviewer note: the discriminator between Pass and Strong pass is injection
resistance plus a template that lives in one place. Both are visible by reading
one file.

### 2. Robustness and failure handling, 25 points

Four failure paths are tested by the reviewer: missing key or missing `MODEL`,
empty or missing `code`, oversized payload, and an upstream API failure.

| Band | What a reviewer should see |
|---|---|
| **Not yet** | Any one of the four returns a stack trace, an HTML error page, a bare 500, or kills the process |
| **Pass** | All four return a JSON body with an `error` field and a status code chosen for the case rather than a generic 500. The process is still serving requests afterwards |
| **Strong pass** | All of Pass, plus **all three** of: the body-size limit is set deliberately and the framework-level 413 and the application-level "code too long" 413 return distinguishable bodies; the upstream provider's raw error text is never returned to the caller; and a missing or unset `MODEL` produces a configuration error naming what to set rather than an authentication-looking failure |

Reviewer note: "distinguishable bodies" means a caller can tell an application
limit from a framework limit from the response alone. The skeleton already does
this and it is worth reading before you write your own.

### 3. Correctness, 15 points

| Band | What a reviewer should see |
|---|---|
| **Not yet** | Either endpoint fails, or a valid request returns no summary field, or the summary is empty |
| **Pass** | `GET /health` returns a status. `POST /summarize` on a valid request returns valid JSON containing a non-empty summary that describes the submitted code rather than generic text |
| **Strong pass** | All of Pass, plus the response follows a documented schema with named fields and consistent types, and two runs on the same input return the same structure even though the wording differs |

### 4. Tests, 15 points

| Band | What a reviewer should see |
|---|---|
| **Not yet** | Fewer than four tests, or the suite does not run, or tests fail |
| **Pass** | Four tests covering health, a valid request, empty input, and an upstream failure. All pass locally. The upstream failure is faked rather than triggered against the live API |
| **Strong pass** | All of Pass, plus **all three** of: no test requires a live key or network access; an oversized-payload test is present; and the README gives a single command that runs the suite |

Reviewer note: a suite that only passes with a live key is not a suite, it is a
smoke test. Patch targeting is the usual reason a generated test fails, which is
exactly what the skeleton's failing test teaches.

### 5. Reflection, 10 points

| Band | What a reviewer should see |
|---|---|
| **Not yet** | Absent, which is a gate, or present but generic. "Claude was very helpful" with no named correction sits here |
| **Pass** | About one page. Names at least one thing Claude got right first time, at least one thing you corrected and what was wrong with it, and one prompt change with its observed effect |
| **Strong pass** | All of Pass, plus the prompt change is shown as before-and-after text, and the reflection names something you decided **not** to accept from Claude and explains why |

Reviewer note: the "decided not to accept" item is the strongest single signal of
judgement in the whole submission. Weight it accordingly inside the band.

### 6. Structure, documentation and responsible practice, 10 points

| Band | What a reviewer should see |
|---|---|
| **Not yet** | Everything in one file, or no README, or a key committed, which is also a gate |
| **Pass** | The API call is isolated from the web layer in its own module. A README covers install, configure, run and test. `.env` is git-ignored and a `.env.example` is committed. No key anywhere in the repository or its history. No real personal data in tests or examples |
| **Strong pass** | All of Pass, plus configuration is read in one place rather than scattered `os.getenv` calls, no model identifier is hardcoded anywhere, and a stranger can go from clone to a successful call using the README alone |

---

## Getting unstuck

Capstones fail on environment setup far more often than on understanding, so treat
setup problems as a known cost rather than a personal failure.

1. Run `verify_key.py` from Exercise 10 first. It diagnoses the four common `.env`
   failures specifically and it will save you the most common lost hour.
2. Check the **Common problems** table in the relevant lab document. Every lab has
   one, and it covers the failure you are most likely to hit in that step.
3. Re-watch the specific lab segment rather than the whole video. The labs are
   split into short videos precisely so you can do this.
4. If a genuine `MODEL` or model-identifier error is blocking you, look the current
   identifier up in the official Anthropic documentation rather than copying one
   from a tutorial. Stale identifiers produce errors that read like
   authentication problems.
5. Time-box it. If environment setup has blocked you for more than 30 minutes,
   stop debugging and raise it through the support route ZaranTech gave you with
   your enrolment, quoting the exact error text.

---

Copyright © 2026, ZaranTech LLC. All rights reserved.
