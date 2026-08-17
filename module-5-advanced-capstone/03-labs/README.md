# Module 5 labs: Advanced Developer Workflows and the Capstone

Three exercises, 65 minutes of lab time. Exercise numbering is global across the programme,
not per module, so Module 5 runs from Exercise 13 to Exercise 15.

Exercise 15 **is** the capstone. It is not a lab that precedes one. Running it as an exercise
and then setting a separate capstone asks the learner to do the same work twice, which is
what the vendor structure did.

## Exercises

| Ex | Title | Duration | You need | Starter code | Videos |
|---|---|---|---|---|---|
| 13 | [Turn a feature brief into a spec and tickets](exercise-13-spec-and-tasks/lab.md) | 18 min | Browser, a Mermaid renderer, three markdown files | None. Prompt only | 1 |
| 14 | [Generate and refine a configuration file](exercise-14-config-file/lab.md) | 12 min | Browser, a text editor | None. Prompt only | 1 |
| 15 | [Build a summariser microservice, the capstone](exercise-15-summarizer-microservice/lab.md) | 35 min | Terminal, API key, pytest | `exercise-15-summarizer-microservice/starter/capstone_skeleton/` | 3 |

Exercises 13 and 14 are browser only. Neither needs a terminal, a container runtime or a
key. Exercise 15 needs all of the Module 4 setup.

## Environment

| Requirement | Needed |
|---|---|
| Browser | Yes |
| Terminal | Exercise 15 only |
| Claude Code | No |
| API key | Exercise 15 only |

Python 3.11 or later. Exercise 15 installs from the skeleton's `requirements.txt`, which
brings `anthropic`, `python-dotenv`, `flask` and `pytest`.

**Docker is not a prerequisite for Exercise 14.** The exercise generates a configuration file
and reviews it against a checklist. It never builds one. Do not add a container runtime to
the prerequisites, and do not let the recording imply one is needed, because that alone will
stop learners who could otherwise complete the exercise in twelve minutes.

## Videos

| Asset | Videos |
|---|---|
| Exercise 13 | 1 |
| Exercise 14 | 1 |
| Exercise 15 | 3: Part 1 scaffold the service, Part 2 integrate the API and design the prompt, Part 3 tests and documentation |

The three parts of Exercise 15 are stated at the top of the lab in a table, with the stopping
condition for each. Keep that table in sync with the recording plan. A learner watching Part 2
needs to know without asking whether they were supposed to have a passing test suite yet.

## What each exercise is actually teaching

Useful when writing the recording script, because in all three cases the stated topic and the
real lesson differ.

1. **Exercise 13** teaches that the value of a generated spec is in its assumptions section.
   Two prompts, weak then strong, against the same one line brief. The difference that does
   the work is not the word "architect", it is the named section list plus one instruction:
   do not resolve an ambiguity silently. The learner writes the product owner questions by
   hand first, then marks each one Answered, Assumed, Guessed or Missing against the draft.
   The `Guessed` count is the finding. The closing step is the trace check between spec,
   design and tickets, which no generation step performs, because each artefact was generated
   from the previous one and none of them was checked against the first.
2. **Exercise 14** teaches config review as a reading skill. The file is never built, which is
   the honest reproduction of how config is actually reviewed on a pull request and the reason
   bad config ships. The lab carries a fifteen row review checklist, with a four row variant
   for a CI workflow, and the deliverable is a three column change log rather than the file.
   The worked stack is deliberately the Exercise 15 capstone service, so the file is one the
   learner can use.
3. **Exercise 15** teaches assembly and self-assessment. There is no new concept in it. Three
   things carry the marks: the prompt the learner designs, the failure paths they can
   demonstrate, and a test suite that does not touch the network.

## Three deliberate features of the capstone skeleton

All three look like defects and are load-bearing. They are documented in
`docs/lab-defect-register.md` and none of them is revealed in the learner-facing lab.

1. **`summariser.py` ships with `TODO` prompts, not a working prompt.** Prompt design is what
   the capstone is graded on, so it cannot be pre-written. The lab teaches the shape, which is
   role, task, tagged input and output constraints, makes the learner write each part as one
   line before any Python, and gives them an injection test to check the boundary with. Do not
   add a finished prompt to the skeleton or to the lab, and do not put one in the recording as
   an example.
2. **One test fails on a clean checkout.** `tests/test_service.py::test_valid_request_returns_summary`
   patches the `summariser` module attribute, while `app.py` did `from summariser import
   summarise_code`, so the patch does not intercept the call and the test gets a 502 where it
   asserted 200. Two legitimate fixes exist: change the patch target to `app.summarise_code`,
   or change the import style in `app.py`. The lab frames this as a puzzle with a route in,
   which is a prompt asking what a patch decorator actually replaces at runtime, and points at
   the fact that a sibling test in the same file patches a different kind of target. Do not
   give away the answer. Patch targeting is the most common reason a generated test suite fails
   on first run, and the resemblance between "the test is aimed at the wrong name" and "the
   application is broken" is the whole lesson.
3. **Two different paths return 413.** `app.py`'s own `MAX_CODE_CHARS` check on the `code`
   field returns `{"error": "code too long", "max_chars": 20000}`. Flask's
   `MAX_CONTENT_LENGTH` returns `{"error": "payload too large"}` and fires before the handler
   runs at all. Both are verified against the running service. A 413 here is a body size
   rejection: it is not a rate limit and it is not a context window problem, and learners
   reliably assume it is one of those two. Each of these gets a row in the lab's common
   problems table.

A fourth trap in the lab, stale grounding, has no code behind it because it cannot have any.
Changing the design without updating the README and `CLAUDE.md` makes every later generation
produce correct-looking output against the old shape, and nothing errors. It is a numbered
step in Part 2 rather than a warning, because a warning does not get acted on.

## Deck alignment

Terminology in these labs matches the Module 5 deck: planning and design with Claude as a
pair architect, writing technical specifications, generating sequence diagrams, creating task
breakdowns, agile backlogs, sprint tasks, integrations and tooling, git workflows, CI/CD
documentation and automated checks, migration scripts, infrastructure as code, and the three
capstone phases of prompt design, API integration and testing. The three evaluation criteria
slides map onto the rubric table in Exercise 15 Step 14.

Three deck points need attention in the revised deck. Record all three in `deck-changelog.md`.

1. Slide 15 lists Terraform configurations, Dockerfiles and Kubernetes manifests together.
   Exercise 14 covers one configuration file and does not build it. Keep the slide broad if you
   like, and make the lab's scope explicit on it, or a learner will arrive at the exercise
   expecting to deploy something.
2. Slides 16 to 19 introduce, build and evaluate the capstone inside Module 5. That does not
   work even in a recorded format, because the learner needs time to build. The programme map
   moves the brief to the end of Module 4 and keeps only the build in Module 5.
3. Slide 23 claims the learner "deployed a robust, fully tested capstone application". Nothing
   in the programme deploys anything. Say tested, not deployed.

## Open item

The capstone skeleton's own `README.md` points at `docs/capstone-brief.md` for the grading
detail, and that file is not in the repository yet. Until it exists, the rubric table in
Exercise 15 Step 14 is the only statement of what is marked, and it is written to stand alone.
When the brief is added, keep the two consistent, and keep the rubric in the lab rather than
replacing it with a pointer. A learner working through Part 3 should not have to open a second
document to find out what is being assessed.

## Conventions for anyone editing these labs

1. `docs/lab-authoring-spec.md` governs structure, voice and prompt handling. Match it
   exactly. Fifteen labs should read as one programme.
2. `lab.md` is the source of truth. The DOCX is generated from it.
3. Python and `curl` only. The vendor labs offered Node and Postman variants and they are gone
   deliberately, to keep learner setup to one runtime.
4. `ANTHROPIC_API_KEY` and a `MODEL` read from the environment, matching Module 4.
5. Never name a Claude model version.
6. Do not write a finished summarisation prompt into the skeleton, the lab or the recording.
7. Do not reveal the patch-target answer in Step 10, and do not remove the sibling test that
   hints at it.
8. Do not add Docker to Exercise 14's prerequisites.
9. No em dashes. No citation residue. The vendor originals for Exercises 13 and 15 carried
   several fragments of it and none of it survives here.
