# Module 5 Recording Script
## Advanced Developer Workflows and the Capstone

> **Trainer only. Do not publish this file to learners and do not paste any part of it
> into a lab, a slide or a video description.** It names the capstone skeleton's planted
> problems and the answers to them. The learner-facing documents are the three lab files
> and `docs/capstone-brief.md`.

Slide numbers in this script refer to the **revised** deck,
`01-deck/revised/Module 5 - Advanced Developer Workflows & Mini-Project - REVISED.pptx`,
which has 26 slides against the original's 24. Two slides were inserted, one at position
4 and one at position 23, so numbers after slide 3 have moved and the changelog's
"Changed" numbers refer to the original. Two examples, because they matter here: the
Terraform, Docker and Kubernetes slide is **16** in the revised deck, and the Key
Takeaways slide with the "deployed" wording is **25**.

**Total runtime:** 100 minutes across 12 videos
**You need before you start:**

1. The same throwaway API key from Module 4, still unrevoked, with credit on it.
2. A copy of the capstone skeleton in a working folder outside the courseware clone,
   with its own `.gitignore` containing `.env`, created before `.env`.
3. `.env` in that folder with `ANTHROPIC_API_KEY`, `MODEL` and `MAX_CODE_CHARS`.
4. Python 3.11 or later with the skeleton's `requirements.txt` installed. That brings
   `anthropic`, `python-dotenv`, `flask` and `pytest`.
5. A Mermaid renderer you have already tested with a small diagram, for Exercise 13.
6. `docs/capstone-brief.md` open, specifically the rubric and gates tables.
7. **No Docker and no container runtime.** Exercise 14 generates a configuration file and
   reviews it by reading. It never builds one. Do not install a runtime and do not let any
   frame imply one is needed, because that alone stops learners who could otherwise
   finish the exercise in twelve minutes.

## Video breakdown

| Video | Covers | Slides | Runtime |
|---|---|---|---|
| 5.1 | Module opening, section map, planning as a pair architect, specs, sequence diagrams | 1 to 7 | 7 min |
| 5.2 | Task breakdowns, agile backlogs, sprint tasks | 8 to 10 | 5 min |
| 5.3 | Tooling, git workflows, CI and CD, migrations, infrastructure as code | 11 to 16 | 8 min |
| 5.4 | Capstone scope and the three phases | 17 to 20 | 6 min |
| 5.5 | How the capstone is marked | 21 to 24 | 6 min |
| 5.6 | Exercise 13 Part 1, questions first, then the spec | none, browser | 9 min |
| 5.7 | Exercise 13 Part 2, design, diagram, tickets, trace | none, browser | 9 min |
| 5.8 | Exercise 14, generate one config file and review it by reading | none, browser | 12 min |
| 5.9 | Exercise 15 Part 1, scaffold the service and record the baseline | none, terminal | 12 min |
| 5.10 | Exercise 15 Part 2, integrate the API and design the prompt | none, editor and terminal | 12 min |
| 5.11 | Exercise 15 Part 3, the failing test, more tests, the README | none, terminal | 11 min |
| 5.12 | Module and programme close | 25 to 26 | 3 min |

The split: Exercise 15 is 35 minutes and the cap is 12, so it goes 12, 12, 11 at the
three hard stopping points the lab already defines. Exercise 13 is 18 minutes, which
exceeds the cap as a single video, so it splits 9 and 9 at the end of Step 5, once the
spec has been marked and before the design work starts. Exercise 14 sits at 12 minutes as
one video, at the cap. The 35 deck minutes run 7, 5, 8, 6, 6 across slides 1 to 24, with
3 minutes held back for the closing video, which keeps the deck budget exact and lets the
module end after the capstone build rather than before it.

---

## Video 5.1: Planning with Claude, and specifications

**Runtime:** 7 minutes
**On screen:** deck

### Say

Open by placing the module. Everything in Modules 1 to 4 was a skill. This module is
about where those skills sit in a working development lifecycle, and then it is about
assembling them.

On slide 4, the section map, say the thing that changes how the learner plans their week:
**"Exercise 15 is the capstone build itself, not a rehearsal for it. What you build in
Exercise 15 is what you submit."** Then say the brief was issued at the end of Module 4
and that if they skipped it, they should stop and read `docs/capstone-brief.md` before
Exercise 13, because Exercises 13 and 14 exist to feed the build.

Slide 5 is Claude as a pair architect. The useful framing is that the value is in being
made to articulate the design, not in being handed one. Slide 6 is specifications. Pull
the point that Exercise 13 proves: a request for prose gives you prose, and a request for
a named list of sections gives you a document with a shape, and a shape is something you
can check for completeness.

Slide 7 is sequence diagrams. One line that saves time later: a diagram that does not
render is not a deliverable, and if the renderer errors, paste the exact error back rather
than describing it.

### Show

Slides 3 through 7. Hold on slide 4 while you say the Exercise 15 line.

### Watch out

1. Do not preview the weak-versus-strong prompt pair from Exercise 13. The learner is
   meant to send the weak one and feel the difference.
2. Slide 7's bullets sit inside grouped shapes, so the on-screen reading order is not
   what a text dump reports. Rehearse the eye path once.
3. Do not imply anything in this module deploys. Nothing in the programme deploys.

---

## Video 5.2: Backlogs and task breakdown

**Runtime:** 5 minutes
**On screen:** deck

### Say

Three slides, five minutes, and one idea worth more than the rest: generated tickets are
reliably too big, because nothing in the request told the model what small means.

Slide 8 is breakdown, slide 9 is backlog items and user stories, slide 10 is sprint tasks.
Cover them briskly and land the two constraints that make generated tickets usable. An
upper bound, which is small enough for one developer to finish inside a short sprint, and
a lower bound, which is grouping anything under half a day. Then the sentence to give
close to verbatim: **"'Implement the note creation endpoint' is a ticket. 'Build the
backend' is a workstream wearing a ticket's clothes."**

Mention story points and estimation exactly once and move on. Estimates generated from a
description are a starting point for a conversation, not an estimate.

### Show

Slides 8, 9, 10.

### Watch out

1. Do not open a real issue tracker at any point in this module. The labs deliberately
   use markdown files instead, and a live workspace on camera leaks project and client
   names.
2. Slide 9 says Claude can prioritise a backlog by analysing business metrics. Do not
   expand that into a claim about business outcomes.

---

## Video 5.3: Tooling, git, CI and CD, and infrastructure

**Runtime:** 8 minutes
**On screen:** deck

### Say

Slides 11 and 12 are editor integration and git workflows. Keep them light. Commit
messages and pull request descriptions from a diff are the highest-frequency, lowest-risk
use of the tool anywhere in a developer's week, and that is the point worth making.

Slide 13 was rewritten and carries the mechanism the vendor slide left out. Say it
directly: **"A pipeline has no terminal and nothing to prompt, so the call from CI is a
non-interactive script or a headless invocation."** A learner who tries to run an
interactive tool in a pipeline gets a confusing hang, and the correction is one sentence.

Slide 14 is automated checks in the pipeline. Add the caveat the slide does not carry: a
generated review comment is advisory, and a pipeline that fails a build on it needs to be
something you chose deliberately.

Slide 15 is migration scripts. The line worth saying is that the rollback script gets
generated at the same time as the forward migration, not later.

Slide 16 is infrastructure as code, and it lists Terraform configurations, Dockerfiles
and Kubernetes manifests together. This is where you must set expectations for Exercise
14 explicitly, because the slide is much broader than the lab. Say it plainly: **"The
next exercise generates one configuration file and reviews it line by line. It does not
build it, it does not run it, and you do not need Docker or any container runtime
installed."** Then say why reviewing by reading is the honest version: that is exactly how
configuration is reviewed on a real pull request, and it is exactly why bad configuration
reaches production.

### Show

Slides 11 through 16. Hold on 16 for the Exercise 14 scope statement.

### Watch out

1. Slide 16 is the frame that makes learners install a container runtime they do not
   need. Do not skip the scope sentence, and do not show a build command anywhere in this
   module.
2. This slide was flagged in `03-labs/README.md` for a scope note and the revised deck
   does not carry one. Until it does, the narration is the only place the scope is stated,
   so it has to be in the take.
3. Do not name a cloud provider's pricing or a specific product tier.

---

## Video 5.4: The capstone, scoped

**Runtime:** 6 minutes
**On screen:** deck

### Say

Slide 17 was rewritten because the vendor scope was several times what the capstone
actually is, and over-scoping is the most common reason a capstone fails. Say the scope as
a hard boundary: two endpoints, `POST /summarize` and `GET /health`. Then the exclusion
list, out loud, because naming it is what stops the drift: no file upload, no
authentication, no database, no streaming, no version endpoint, no web UI. Every one of
those is a defensible idea and every one costs marks.

Then the framing question, which the brief puts at the centre and which the learner
answers in writing before any code: **"What is the smallest version that still
demonstrates the skill?"** Say the observed pattern behind it: a minimal service with a
well-designed prompt and clean failure paths scores well above a feature-rich service with
an unstructured prompt.

Slides 18, 19 and 20 are the three phases. Map them onto the three Exercise 15 videos so
the learner knows where they are: prompt design and integration are Part 2, testing is
Part 3. On slide 18, say that the skeleton's prompt is deliberately unwritten and that
this is where their marks are. On slide 19, connect back to Module 4: the key comes from
the environment, the model identifier comes from configuration, and the provider's raw
error text never reaches the caller. On slide 20, state the rule that decides the testing
mark: no test may make a real API call.

### Show

Slides 17 through 20.

### Watch out

1. Do not read a finished summarisation prompt onto slide 18, and do not describe one in
   enough detail to be transcribed. Teach the four parts, not the text.
2. Slide 19 mentions exponential backoff. It is a "going further" item in the lab, not a
   requirement. Say so, or learners will build it instead of the tests.
3. Slide 20 says integration tests generated by AI validate end-to-end workflows. Do not
   let that read as permission for a live-key test suite. Say the no-network rule in the
   same breath.

---

## Video 5.5: How the capstone is marked

**Runtime:** 6 minutes
**On screen:** deck, then `docs/capstone-brief.md`

### Say

Lead with slide 23, not with the slides either side of it. It is the new slide, it is the
only one carrying thresholds, and the capstone carries completion for this programme, so
be explicit rather than gentle.

Read the weights off it and say what the split means: prompt design 25 and robustness 25,
which is half the marks between them, and neither of them is about getting the service
working. Then correctness 15, tests 15, structure and responsible practice 10, reflection
10.

Then switch to `docs/capstone-brief.md` and cover four things from it that the slide
cannot hold:

1. **The thresholds.** Pass is 60 or above with all three gates cleared. Strong pass is 80
   or above with no criterion sitting in its "Not yet" band.
2. **The gates**, and that a gate is not a deduction. A real key in the repository, its
   git history, the zip or a screenshot. No reflection. A service that does not start from
   a clean clone following their own README. Any one of those stops the submission being
   marked until it is fixed, whatever the score.
3. **What separates Pass from Strong pass on prompt design**, because it is concrete and
   visible by reading one file: injection resistance stated as a rule, plus a named
   template that lives in one place rather than inlined at the call site.
4. **What separates Pass from Strong pass on robustness**: the framework 413 and the
   application 413 return distinguishable bodies, the provider's raw error text never
   reaches the caller, and a missing `MODEL` produces a configuration error naming what to
   set rather than something that looks like an authentication failure.

Then the reflection, ten points and one gate. Say the strongest signal in the whole
submission out loud: something they decided **not** to accept from Claude, and why.

Slides 21, 22 and 24 are the three vendor evaluation slides. Slide 21 was rewritten and
names the four failure paths, so use it. Slides 22 and 24 are still criteria expressed as
adjectives with no thresholds, so cover them in one pass each and point back at slide 23
for anything markable.

### Show

1. Slide 23 first, held.
2. `docs/capstone-brief.md`, the rubric table, then the gates table.
3. Slide 21. Then 22 and 24 briefly.

### Watch out

1. The new slide 23 sits between slides 22 and 24, which are the unrewritten adjective
   slides, so the on-screen order is adjectives, thresholds, adjectives. Rehearse the
   order you click through, or the module's most important slide is buried in the middle.
2. Do not restate a threshold in a form the brief does not use. Two numbers that nearly
   agree is worse than one number.
3. Do not put a submission date on screen.
4. Do not promise an outcome, a certification or an employability result at any point in
   this video.

---

## Video 5.6: Exercise 13 Part 1, questions before prompts

**Runtime:** 9 minutes
**On screen:** browser

### Say

The brief is one line: build a notes API with tagging. Say it is thin on purpose, because
thin is what you actually get.

Then the connection worth making, because it costs nothing and lands hard: this is the
same system as the Exercise 12 conversation. The constraint that got lost there is exactly
the kind of decision that belongs in the document being written now. **"A decision
recorded in a spec does not have to survive a conversation."**

Step 1 is two columns, known and missing, written before prompting. Point out that the
missing column is longer than the brief, and that this is normal.

Step 2 is the product owner questions, by hand, at least seven. Say why by hand: if the
model generates the questions and answers them in the same breath, the spec is built on
assumptions nobody saw it make, and they cannot be found later.

Step 3 is the weak prompt then the strong one. Send the weak one, skim the result, then
send the strong one in a new conversation. Then name the two differences that do the work,
and say clearly that neither of them is the word "architect". The first is the named
section list, which turns a request for prose into a request for a document with a shape.
The second is the last instruction: do not resolve an ambiguity silently. Both prompts
will make assumptions, because the brief is too thin not to. Only one of them tells you
where they are.

Step 4 is the marking pass, and it is the exercise. Four markings: Answered, Assumed,
Guessed, Missing. Say what the Guessed row is: **"Every item in it is a decision that
entered your document without a decision being made."** On a real feature those are what
surface three weeks later as a disagreement about what was agreed.

Step 5 is targeted follow-ups, one per turn, so each change is visible. End the video here.

### Show

1. The one-line brief, written in the conversation.
2. Both columns and the question list, in a markdown file.
3. The weak prompt and its answer, skimmed.
4. The strong prompt in a new conversation, and `spec.md` saved.
5. The marking table with real markings against your own question list.

### Watch out

1. The Claude sidebar, the conversation list and the project list are in frame for this
   whole video. Fresh browser profile, dedicated project, deliberate conversation titles.
2. The model picker is on screen in the browser labs whether you want it or not, and it
   names current versions. Frame it out of shot and do not open it.
3. Do not open the account menu. Email address and plan tier.
4. Do not use a real issue tracker or a real client's feature brief.
5. Your Guessed count will differ between takes. Do not script a number, script the
   question.

---

## Video 5.7: Exercise 13 Part 2, design, diagram, tickets, trace

**Runtime:** 9 minutes
**On screen:** browser, then editor

### Say

Step 6 is the high level design from the spec, kept implementation agnostic and naming no
products or libraries. Check it covers the API layer, the business logic, persistence, the
tag relationship, error handling and where the security boundary sits. If it reads as
abstract to the point of being unfalsifiable, say so on camera and ask it to be concrete
about the request flow. That correction is more instructive than a clean first pass.

Step 7 is the Mermaid sequence diagram, including the validation step and the failure path
where a tag is not in the allowed vocabulary. Render it. If it fails, paste the exact
renderer error back rather than describing it, and say why: the error text contains the
line and the token, and your description of it does not.

Steps 8 and 9 turn the spec into tasks and then into tickets. Show the five checks on each
ticket: one title, one purpose and split anything containing "and also", acceptance
criteria testable by someone who did not write it, dependencies that point backwards
rather than in a circle, and no hidden scope.

Step 10 is the closing point of the whole exercise, so give it room. Three traces: every
ticket back to a requirement, every requirement forward to a ticket, and the components in
the design against the workstreams in the tickets. Then the sentence: **"This is the check
no generation step performs for you, because each artefact was produced from the last one
and none of them was checked against the first."** Where a ticket has no requirement
behind it, either the spec is incomplete or the ticket is invented, and both are worth
knowing.

### Show

1. `design.md` being built, with one visible correction round.
2. The Mermaid block pasted into the renderer and drawing.
3. `tickets.md`, and one ticket failing a check and being split.
4. One trace run end to end, in both directions.

### Watch out

1. Same browser hygiene as 5.6. Sidebar, tab strip, no model picker, no account menu.
2. A Mermaid block that will not render is a real risk on camera. Have a known-good small
   diagram tested in your renderer before the take, so a failure is a two-minute teaching
   moment rather than a dead take.
3. Do not fix a ticket silently. The correction is the content.

---

## Video 5.8: Exercise 14, generate one config file and read it

**Runtime:** 12 minutes
**On screen:** browser, then editor

### Say

Open with the scope, in the first fifteen seconds, because it decides whether learners
attempt the exercise: **"You will not build or run this file. There is nothing to install
and no container runtime is required."** Then the reason: configuration is reviewed by
reading, which is how it gets reviewed on a real pull request, and which is exactly why
bad configuration reaches production.

Step 1 is one file, not four. The walkthrough uses a Dockerfile because a careless line
there does the most damage, and everything transfers.

Step 2 is the stack facts, written down first, and this is the step that decides whether
the output is usable. Say it as a rule: **"Every fact you leave out becomes a guess, and a
guess in configuration looks exactly like a fact."** Use the Exercise 15 capstone service
as the stack, so the file is one the learner can actually use.

Step 3 is the weak prompt against the strong one. Send the weak version, keep the result,
then send the constrained one. Then the assessment that matters: the weak prompt did not
produce a wrong file, it produced a file for a generic Python application, which is a
different and more dangerous thing, **because it will build**.

Step 4 is the fifteen-row checklist and it is the exercise. Do not read all fifteen rows
aloud at recording pace. Work five of them properly on the generated file and tell the
learner to pause and work the rest. The five to work on camera are the ones that carry the
most: row 1 the pinned base image, row 3 the manifest copied and installed before the
source, row 7 no development server and no debug mode, row 9 no secret value anywhere, and
row 11 the build context exclusions. Say what row 7 actually is: a development server with
debug enabled exposes an interactive console, which makes it a security finding rather
than a performance one.

Step 5 is correcting it by hand rather than asking for a corrected version, because at
this size editing is faster than reading a regenerated file, and because Step 6 needs to
know exactly what changed.

Step 6 is the three-column change log, and it is the deliverable. Read down the "Why"
column and you have the list of things to state in the prompt next time, which is why the
second config file you generate takes half as long to review as the first.

### Show

1. The nine stack fact lines, typed out.
2. Both generated files side by side.
3. Five checklist rows worked against the file, marked pass or fix.
4. Two or three hand corrections.
5. The change log table with at least four rows.

### Watch out

1. Do not run a build, do not show a build command, and do not mention having a runtime
   installed. One frame of that undoes the scope statement.
2. Twelve minutes is the cap and this lab has seven steps with a fifteen-row table in the
   middle. Work five rows on camera and hand the rest to the pause. Rehearse against a
   clock.
3. If the generated file happens to be correct on a row, say so and move on. Do not
   pretend to find a fault.
4. Browser hygiene as in 5.6.
5. Do not put a real internal Dockerfile or a real registry path on screen.

---

## Video 5.9: Exercise 15 Part 1, scaffold and baseline

**Runtime:** 12 minutes
**On screen:** terminal, then editor

### Say

State what this is before anything else: **"This is the capstone. It is not a warm-up for
one. Everything you submit comes out of these three videos."** Then say nothing here is a
new concept. Module 1 gave the prompt structure, Module 2 the project context, Module 3 the
review and debugging habits, Module 4 the API. This is the assembly.

Say the three stopping points and that they are hard stops: `/health` responding and a
written baseline ends Part 1, a real summary plus four verified failure paths ends Part 2,
a green suite that never touches the network ends Part 3. Do not carry an unfinished part
forward, and do not skip ahead to Part 3 to look at the tests.

Copy the skeleton out of the course repo into a folder of their own, and say why: their key
and their submission should not live in a clone of the courseware.

Step 1 is the scope, again, written into the README now. Two endpoints and the exclusion
list, because writing it down is the cheapest way to notice yourself drifting.

Step 2 gets it running. Virtual environment, `requirements.txt`, `.env` from
`.env.example`, three values, and `curl localhost:5000/health` returning a status.

Step 3 is the response table, filled in from `app.py` rather than from memory, and it is
the best fifteen minutes in the lab. Six rows, and say there are more rows than expected.
Two of them return 413. Land the distinction cleanly, because learners lose real time here:
**"A 413 here is a body-size rejection. It is not a rate limit and it is not a
context-window problem."** One of them is a rule you wrote about the content of a field.
The other is a limit on the size of the whole request, and it is enforced before your
handler function is called at all. They share a status code and they are not the same
event. Then raise the design question the lab leaves open and do not answer it: a valid
request to a service with no `MODEL` configured currently returns 502, a 502 says the
upstream service failed, and nothing upstream was contacted. Ask whether they agree.

Step 4 is the baseline, and it needs exact wording. Run `pytest`, write the counts down,
change nothing, and do not read the test file closely yet. Say the number out loud: three
of the four tests pass and one does not, and that is the correct state of a fresh checkout.
Part 3 is where it gets dealt with, and by then they will know enough about the service for
it to be tractable rather than a mystery.

### Show

1. The `cp -r` into a folder outside the repo, then `git init` and `.gitignore` before
   `.env`.
2. Setup, then `python app.py` in one terminal and `curl -s localhost:5000/health` in a
   second.
3. `app.py` read top to bottom, slowly, with the response table filled in as you go.
4. `pytest`, with the `3 passed, 1 failed` line and `assert 502 == 200` in frame.

### Watch out

1. `.env` is on screen again in this module and it carries both the key and the model
   identifier. Paste, never type, and move off the file.
2. The skeleton runs with `debug=True` in `app.run`, so an unhandled exception renders the
   interactive debugger in the browser. Do not trigger one on camera. It puts a full
   traceback and a code listing in frame, and it contradicts the robustness point you are
   teaching two videos later.
3. `app.py` line 17 carries a comment beginning "Trap 1". If you read the file top to
   bottom on camera it is visible. Do not read it aloud and do not explain it as a trap;
   treat it as the deliberate configuration line it describes.
4. Do not let the failing test become a bug report in the narration. It is the correct
   state of a fresh checkout and the wording has to say so.
5. Twelve minutes is the cap and this part has four steps, one of which is reading a file
   properly. Compress the virtual environment setup, not Step 3.
6. Port 5000 is taken by a system service on some machines. Confirm it is free before the
   take, and if you change it, change it in every `curl` and README line in all three
   videos.

---

## Video 5.10: Exercise 15 Part 2, the API and the prompt

**Runtime:** 12 minutes
**On screen:** editor, then terminal

### Say

Step 5 is why `summariser.py` is a separate module. Say the functional reason rather than
the aesthetic one: **"That separation is not tidiness. It is what makes Part 3 possible,
because a test can replace one function and never open a socket."** Then the second
property to keep: both functions raise `SummariserError` when configuration is missing, and
`app.py` turns that into a response without passing the underlying exception through. The
caller of your API never receives the provider's error text.

Step 6 is where the marks are and it is the most delicate thing in this module to record.
`SYSTEM_PROMPT` and `USER_TEMPLATE` are TODO markers on purpose. **Do not write the
finished prompt on camera and do not read one out in a form that can be transcribed.**
Teach the shape and make them write it.

Four parts, and each one gets a single line on paper before any Python:

1. **Role.** Who is answering and who the answer is for. "Summarise this code" and "explain
   this to a developer who has to maintain it next week" produce different documents.
2. **Task.** Three named things rather than the word summarise: the purpose of the code, the
   key functions and the flow between them, and any risks or assumptions visible in the
   code.
3. **Tagged input.** The code arrives inside `<code>` tags, and the system prompt states
   that content inside those tags is data and never instruction. They built this in
   Exercise 11. It matters more here, because the input arrives over HTTP from someone who
   is not them.
4. **Output constraints.** A length limit, a format, and a rule for the case where the
   input is not readable code. Say the operational reason: without a length limit the
   endpoint has an unpredictable response size and an unpredictable cost per call, which is
   not a property you can operate.

Then the injection test, and this one you can show fully because it is a check rather than
an answer. Post the code payload with the instruction inside a comment. If the word BANANA
appears in the summary, the tags are present and the rule about them is not doing its job,
and the fix is the system prompt rather than the input. Then be honest in the same breath:
this is not a guarantee, the boundary raises the cost of an injection, and the defence
actually shipped is that nothing downstream of the response is trusted with an action.

Step 7 is the response shape, and the honest option is the cheap one. `{"summary": text}`
is legitimate. If they want structured fields, three things change together: the prompt
asks for the structure, the code parses it, and the parse fails cleanly when the response
is not in the shape asked for. Say that an unparsed response must not reach the caller as a
500.

Step 8 is all four `curl` failure paths, and then the second 413 constructed deliberately.
Check three things on each: the status code matches the Step 3 table, the body is JSON with
an `error` field, and there is no traceback and no provider error text anywhere in it.

Step 9 is stale grounding, and it is a step rather than a warning for a reason. Say the
reason: **"Nothing breaks. The assistant keeps generating code, tests and documentation
against the shape you described the first time, and each individual output looks correct.
You find it three generations later, when a test asserts a field that no longer exists and
you cannot work out where the field came from."** So if the response shape changed, or a
status code changed, or anything was renamed, the README and the project context file get
updated now, before the next generation.

### Show

1. `summariser.py`, with the module boundary explained.
2. The four lines written out, on screen, as four lines. Not a prompt.
3. Enough of the prompt going into the file to show it is a real template, without the
   text being readable as a copyable answer. Keep the shot on the structure.
4. The injection `curl`, and the response.
5. All four failure-path `curl` commands with their status codes.
6. The second 413, constructed, sent, and the two different bodies compared.
7. The README and context file being updated.

### Watch out

1. **The single hardest constraint in this module: do not put a finished, copyable
   summarisation prompt on screen or in narration.** Prompt design is 25 of the 100 marks
   and it is the thing the capstone assesses. Teach role, task, tagged input, output
   constraints. If a take drifts into dictating prompt text, cut it.
2. Do not trigger an unhandled exception. `debug=True` renders the interactive debugger.
3. The 3 MB body needed for the framework 413 has to be constructed, not typed. Prepare the
   file before the take so the shot is the response, not the setup.
4. Live generations differ between takes. Do not script the content of the summary.
5. If the injection test does pass through and BANANA appears, keep it. Narrate the fix to
   the system prompt. That is a better video than a clean run.
6. Twelve minutes is the cap and this part has five steps including the highest-value
   teaching in the module. If you are over, compress Step 7, not Step 6.

---

## Video 5.11: Exercise 15 Part 3, the failing test and the documentation

**Runtime:** 11 minutes
**On screen:** terminal, then editor

### Say

Run `pytest` and get the same result as the Part 1 baseline. Three pass, one fails,
`tests/test_service.py::test_valid_request_returns_summary`, asserting a 200 and getting
something else.

Before touching it, clear the ground, because this is what stops the wasted hour. It is not
a broken application: they watched the same request succeed with `curl` in Step 8. It is
not the prompt. It is not `.env`, and adding a real key will not fix it.

Then frame it as what it is: a question about what a patch decorator actually does at
runtime. Give them the route in, which is the prompt in the lab asking what
`patch.object` replaces at runtime, in which namespace the calling function looks the name
up, and whether patching the attribute on the other module changes what that lookup finds.
Say the constraint on the prompt out loud: it asks for the mechanism and explicitly does not
ask for corrected code.

**Point at the difference, not the answer.** The exact move on camera is to open
`tests/test_service.py`, put the failing test and `test_upstream_failure_returns_502` in the
same frame, and say: **"These two tests replace the same function. One of them passes. The
targets are not the same shape. That is the strongest hint in the repository."** Then stop
talking and hand it to the pause. Do not say which target is right, do not say the words
that name the fix, and do not apply either fix on camera.

Then say there are two legitimate fixes, they pick one, and they write one sentence in the
README saying which and why. And they do not change what the test asserts.

Step 11 is why that was worth twenty minutes, and it is the transferable point of the whole
capstone: patch targeting is the most common reason a generated test suite fails on first
run. The generated test is usually testing the right behaviour and pointing at the wrong
name, and the failure it produces looks exactly like an application bug. **That resemblance
is the trap.** The reasonable response to a red suite is to go and change the application,
and here that would have been wrong.

Step 12 is four more tests minimum, and one rule with no exceptions: no test may make a
real API call. Live tests are slow, cost money on every run, fail when the network does, and
test somebody else's service rather than yours. Show the generation prompt with the
constraint in it rather than in their intentions, then show the verification: disconnect, or
temporarily empty the key, and re-run. If a test changes result, that test was calling out.

Step 13 is the README, generated and then executed. Say the failure mode precisely:
**"Generated documentation is a good first draft that is confidently specific about the
things it guessed."** The guesses are always in the same three places: a command that is
nearly right, a variable name that follows a convention you did not use, and an example
response with a field that does not exist. So open a new terminal without the virtual
environment active and run every command in order.

Steps 14 and 15 close it. Self-mark against the rubric, then `git status --short` and
`git ls-files`, and `.env` appears in neither. If it is tracked, it is in the history,
removing it later does not remove it, and the key gets rotated. Last item: a short README
section naming which parts were AI-generated and which they wrote or corrected, and say why
that is not compliance theatre. It is the thing the next person to touch the code most needs
to know.

### Show

1. `pytest`, with `3 passed, 1 failed` and `assert 502 == 200`.
2. Both tests in one frame, side by side, with the targets visible.
3. The mechanism prompt, sent, with the explanation on screen.
4. The generation prompt for the extra tests, and the full suite green.
5. The no-network verification run.
6. `git status --short` and `git ls-files` with `.env` absent from both.

### Watch out

1. **Do not fix the failing test on camera and do not name the fix.** The register, the lab
   and the labs README all require this. It is the only part of the exercise that transfers
   directly to the next AI-generated suite the learner is handed.
2. The failing test's body carries a comment that names the cause of the failure in plain
   language. It is visible the moment you open the file, and it gives away more than the
   sibling-test hint does. Frame the shot on the two `patch` lines rather than the comment
   block, keep the pause instruction crisp so the learner is looking at the targets, and
   raise the comment with the content team for the next revision.
3. Do not show the `git log` of your own recording repository. Show the learner's fresh
   working folder.
4. Emptying the key for the no-network check means editing `.env` on camera again. Comment
   the line out rather than deleting the value, and do not let the value scroll.
5. Eleven minutes is the tightest budget against content in the module. The failing test
   gets four minutes, the extra tests three, the README and the two closing steps four.

---

## Video 5.12: Module and programme close

**Runtime:** 3 minutes
**On screen:** deck

### Say

Slide 25 is the takeaways slide. Narrate over its last bullet rather than reading it. The
slide says the learner deployed a robust, fully tested capstone application. **Nothing in
this programme deploys anything.** Say tested, not deployed, and say what was actually
built: one small service, with a prompt they designed, failure paths they can demonstrate,
and a test suite that does not touch the network.

Then close the programme on what it was actually chasing, which is judgement rather than
tool familiarity. The learner should now be able to decide when to reach for the chat
interface, when to reach for Claude Code, and when to reach for the API, and should be able
to tell a fluent wrong answer from a correct one. Every lab in this programme was built to
give them one instance of that.

Last thirty seconds, practical and short. Submit against the date their enrolment gives
them. Five items: the repository or zip, the problem statement, the README, a passing test
run, and the one-page reflection. Then the sentence to end on: **"A working service proves
you can follow instructions. The reflection proves you built judgement, which is the actual
outcome of this programme."**

Slide 26 is the thank you card.

### Show

Slide 25, then slide 26.

### Watch out

1. Slide 25's "deploying a robust, fully tested capstone application" wording was flagged
   in `03-labs/README.md` and was **not** corrected in the revised deck or the changelog.
   Either fix the slide before this take or narrate over it explicitly. Do not read it as
   written.
2. Slide 25 also says "terraform deployment files", which overstates what Exercise 14 did.
   One correcting clause is enough.
3. No employability claim, no certification claim, no ZaranTech statistic that is not on the
   approved list.
4. Do not put a submission date on screen.

---

## The teaching points that carry this module

1. The value of a generated spec is in its assumptions section, and the instruction that
   produces one is "do not resolve an ambiguity silently".
2. Configuration is reviewed by reading, never by building, which is why a checklist beats
   a second opinion and why bad configuration reaches production.
3. A 413 is a body-size rejection rather than a rate limit or a context-window problem, and
   an application limit and a framework limit have to be distinguishable from the response
   alone.
4. A generated test that fails is usually pointing at the wrong name rather than finding a
   broken application, and telling those two apart quickly is most of what makes generated
   tests worth having.
5. Stale grounding fails silently: change the design without changing the project context
   file and every later generation is correct-looking and wrong, which is why updating the
   context is a step rather than a warning.

## Questions learners will ask, and the answers

| Question | Answer |
|---|---|
| Do I need Docker for Exercise 14? | No. Nothing in that exercise builds or runs the file. It generates one configuration file and reviews it against a checklist by reading it. |
| Is Exercise 15 the capstone, or is there another project? | It is the capstone. What you build across those three videos is what you submit. |
| The test suite fails on a clean checkout. Is the skeleton broken? | No, that is the shipped state and it is deliberate. Three pass, one fails. It is the first thing to fix and the lab walks you to it. It fails with no key and no network, so it fails identically for everyone. |
| Should I add a real key so the failing test passes? | No. A key will not change the result. That test never reaches the network, which is the clue. |
| Why is the prompt in `summariser.py` left as TODO? | Prompt design is 25 of the 100 marks. Handing you a finished prompt would remove the thing being assessed. Write the four parts as four lines first: role, task, tagged input, output constraints. |
| Am I allowed to use Claude for the whole capstone? | Yes, that is the point of the course. What is not acceptable is submitting output you have not read, and the reflection makes that visible immediately. |
| I got a 413. Am I being rate limited? | No. 413 is a body-size rejection. Two different limits produce it here: your own check on the length of the `code` field, and the framework's limit on the size of the whole request, which fires before your handler runs. Give them different bodies so you can tell them apart in a log. |
| Why is a valid request with no `MODEL` a 502? | That is the skeleton's choice and the lab asks you to challenge it. A 502 says upstream failed and nothing upstream was contacted. If you change it, say why in your README. Strong pass on robustness wants a configuration error that names what to set. |
| Can my tests call the real API? | No. Not one of them. Live tests are slow, cost money on every run, fail when the network does, and test somebody else's service. Replace at the module boundary and prove it by running with the network off. |
| Is Flask required? | No. The skeleton is Flask and marking does not depend on the framework. Any Python web framework is fine. Python is required. |
| How many endpoints should I build? | Two. `POST /summarize` and `GET /health`. Every capstone that fails, fails on scope rather than on ability. |
| What do I actually submit? | Five things: the repository or a zip, the one-paragraph problem statement, the README, a passing test run, and the one-page reflection. The reflection is a gate, so a submission without it is not marked. |
| What is the pass mark? | 60 or above with all three gates cleared. Strong pass is 80 or above with no criterion in its "Not yet" band. The thresholds are in `docs/capstone-brief.md`. |
| I committed my key by accident. | Rotate it immediately, then resubmit from a clean history. Removing it in a later commit does not remove it from the history, which is why a committed key is a gate rather than a deduction. |
| Do I deploy the service? | No. Nothing in this programme deploys anything. The capstone is built, tested and documented, not deployed. |

## Pre-record checklist for this module

1. Confirm the Module 4 recording key is still valid and still has credit, and that its
   revocation date is still in your calendar.
2. Copy the capstone skeleton into a working folder outside the courseware clone. Run
   `git init`, write `.gitignore` containing `.env`, then create `.env`. In that order.
3. Fill `.env` with `ANTHROPIC_API_KEY`, `MODEL` and `MAX_CODE_CHARS`, looking the model
   identifier up in the official documentation on your record date.
4. Install from the skeleton's `requirements.txt` in an active virtual environment.
5. Confirm port 5000 is free. If you have to change it, change it in `app.py`, every `curl`
   command and every README line across all three Exercise 15 videos.
6. Prepare the oversized payload file for the framework 413 before the take, so video 5.10
   shows the response rather than the setup.
7. Test your Mermaid renderer with a small diagram. Exercise 13 depends on it and a dead
   renderer is a dead take.
8. Do **not** install Docker or any container runtime, and remove any container tooling from
   the visible shell and editor so no frame implies Exercise 14 needs one.
9. Fresh browser profile, dedicated project, deliberate conversation titles, notifications
   off, model picker framed out of shot. Videos 5.6, 5.7 and 5.8 are browser labs.
10. Close every editor tab and every folder except this repository plus the capstone working
    folder.
11. Decide before video 5.12 whether you are correcting revised deck slide 25's "deployed"
    wording or narrating over it. Either is defensible. Recording it as written is not.
12. Rehearse the click order for video 5.5. Slide 23 carries the thresholds and it sits
    between two adjective-only slides.
13. Read `docs/capstone-brief.md` end to end, particularly the rubric bands and the three
    gates, so video 5.5 is not a reading.
14. **Verification run, do this last.** From
    `module-5-advanced-capstone/03-labs/exercise-15-summarizer-microservice/starter/capstone_skeleton/`,
    run `python -m pytest -q`. **Expected: 3 passed, 1 failed**, with `assert 502 == 200` on
    `test_valid_request_returns_summary`. It must fail with no key and no network. If it
    passes, somebody has fixed the planted patch-target problem and videos 5.9 and 5.11 are
    both wrong. Do not record Exercise 15 until this reproduces.

---

Copyright © 2026, ZaranTech LLC. All rights reserved. Internal trainer document.
