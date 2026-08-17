# Module 2 Recording Script
## Claude for Coding Tasks (Claude Code)

> **Trainer only. Do not publish, do not attach to a learner handout, and do not
> paste any section of this file into a slide.** It names the planted defects in
> `messy_registration.py` and the trap that Exercise 5 is built around. If a
> learner reads this file, Exercise 5 stops working.

**Total runtime:** 89 minutes across 9 videos
**You need before you start:**

1. Claude Code installed and launching from your terminal. This is the first
   module that needs it. Confirm it starts before you record a frame.
2. A clone of the course repository at a short path created for the recording. No
   personal home directory path in shot. See `docs/recording-hygiene.md` section 4.
3. A second, small practice project of your own, three to ten files, for Exercise
   4. It must not be the course repo, because the course repo already has a
   context file and the point of the exercise is watching one appear.
4. `pip install pytest`. Optionally `pip install flask`, though reading the
   Exercise 5 starter file is enough.
5. The revised deck open in presenter view:
   `module-2-claude-code/01-deck/revised/Module 2 - Claude for Coding Tasks (Claude Code) - REVISED.pptx`
6. Shell prompt reduced to the directory name. No machine name, no username, no
   branch decoration, no virtual environment name. Fresh shell, no history to
   scroll into.
7. Terminal font large, checked against your smallest target screen.
8. A saved fallback copy of `register_refactored_v1.py` from a take where the
   naive prompt did produce a breaking change. See video 2.7, Watch out, item 1.

The chosen split: the 35-minute deck runs as four lectures of 8, 10, 9 and 8
minutes. The 10-minute lecture is the context block, because the new project
context file slide carries a live file on screen and needs the room. Exercise 4 is
12 minutes and records as one video. Exercises 5 and 6 record as two videos each,
exactly as their lab documents already tell learners they will, so the video
boundaries and the handout boundaries agree.

## Video breakdown

| Video | Covers | Slides | Runtime |
|---|---|---|---|
| 2.1 | Module opening, what Claude Code is and what changes from Module 1 | 1 to 6 | 8 min |
| 2.2 | Project context, the context file, file sharing, the big picture | 7 to 11 | 10 min |
| 2.3 | Generation from specs, components, refactoring, modularisation, patterns | 12 to 19 | 9 min |
| 2.4 | Documentation, README structure, unit and integration tests, consistency | 20 to 27 | 8 min |
| 2.5 | Exercise 4, all six steps | none | 12 min |
| 2.6 | Exercise 5 Part 1, draft from the user story | none | 8 min |
| 2.7 | Exercise 5 Parts 2 and 3, the refactor trap and the annotation | none | 12 min |
| 2.8 | Exercise 6 steps 1 to 7, docstrings, usage notes, generated tests to green | none | 11 min |
| 2.9 | Exercise 6 steps 8 and 9, the coverage hunt and the contracts | none | 11 min |

Deck 35 minutes, labs 54 minutes, 89 total, matching `docs/programme-map.md`.

## Video 2.1: What Changes Now That You Have a Terminal

**Runtime:** 8 minutes
**On screen:** deck, with one short terminal cut

### Say

Open with the step change, because it is the thing a learner needs to hear in the
first fifteen seconds: Module 1 was browser only and this module needs Claude Code
installed locally. If they have not installed it, this is the moment to pause and
do that, and the videos will wait.

Then name the difference in one sentence rather than in a feature list: in Module 1
you handed Claude text and it handed you text back. From here it reads your files
directly and it can change them. Everything else in this module follows from that
one change.

On slide 4, read the three exercises and add the honest framing for each: Exercise
4 is short and it is the one that changes their daily habit, Exercise 5 is the one
with the trap in it, and Exercise 6 is the longest and produces a test suite that
Module 3 opens by running again.

Slides 5 and 6 are the overview. Keep them moving. Somewhere in slide 6, cut to a
terminal, `cd` into the course repo, start Claude Code, and let it come up. Say:
"That is the whole install story on screen. I changed into a directory and started
it. I did not upload anything and I did not paste anything, and if your only
experience is the browser, that is the habit to unlearn."

Then quit back out. This video does not do work in the session.

### Show

1. Slides 1 to 4.
2. Slide 5.
3. Slide 6, then cut to the terminal. `cd` into the short recording path, start
   Claude Code, wait for it to be ready, then exit.
4. Back to slide 6 for the closing line.

### Watch out

1. This is the first terminal frame in the programme, so it sets the standard for
   the remaining four modules. Prompt reduced to a directory name, large font,
   fixed window size. Whatever you use here you are committed to for Modules 3, 4
   and 5.
2. Do not let the `cd` reveal a personal home directory. Work from the short
   recording path.
3. If Claude Code prints anything on startup that names a version, do not read it
   aloud and do not linger on the frame. Scroll it out or clear the screen before
   you continue talking.
4. Do not begin an unscripted session here. A single improvised prompt in this
   video will run over the eight minutes and duplicate Exercise 4.
5. Do not promise a specific install command on camera. Point learners at the
   official installation documentation instead, because install instructions
   change and a stated command dates the video.

## Video 2.2: The Project Context File

**Runtime:** 10 minutes
**On screen:** deck, then editor, then deck

### Say

This block fills the largest single gap in the programme. The deck spends six
slides on organising project context and, before this revision, never mentioned the
file that does it. Slide 8 is where that is fixed, so give it four of the ten
minutes and put a real file on screen.

Slide 7 sets up the problem: context organisation decides whether the output is
relevant, and the reframed bullet says to let Claude Code read the repository
directly rather than pasting files into a chat.

Then slide 8, and say the mechanism plainly first: Claude Code reads a file named
`CLAUDE.md` at the root of the working directory automatically, at the start of
every session. Nobody has to remember to attach it.

Now the worked example, and this is the part that has to be a real file rather
than a template. Open the course repository's own `CLAUDE.md` in the editor and
walk three things:

1. The section headed "Critical convention: intentional defects". Read the two
   important sentences out: files under any `03-labs/*/starter/` directory contain
   planted bugs and they are the teaching material, and do not fix them. Then say
   the sentence that makes this land: "Without that paragraph, any capable
   assistant asked to tidy this repository would helpfully repair every planted
   defect and destroy the course. That is not a hypothetical. It is the single
   most valuable paragraph in this file, and it is a boundary rather than a
   description."
2. The writing conventions and code conventions sections. Point out that they are
   descriptive rather than aspirational. They say what the repo actually does.
3. The absence of any current task. Say: "There is nothing in here about what I am
   working on this week, and that is deliberate. Durable facts go in the file, the
   current task goes in the prompt. Anything that is false by next Thursday makes
   this file worse, because a stale instruction is more expensive than a missing
   one."

Then the three-row comparison from slide 8's third bullet, and say which row
decides it in practice: a brief you retype every session is a brief you stop
writing by Thursday.

Slides 9, 10 and 11 then run at pace. Point at the specific files rather than the
whole tree, supply architecture notes and the stack early, and reset the
conversation when the topic changes entirely.

### Show

1. Slide 7.
2. Slide 8, held while you state the mechanism.
3. Editor, the course repository's `CLAUDE.md`, scrolled to the intentional
   defects section. Read the two sentences with the cursor on them.
4. Same file, the conventions sections, briefly.
5. Same file, scrolled top to bottom once at reading pace so they can see there is
   no task list in it.
6. Back to slide 8 for the three-row comparison.
7. Slides 9, 10, 11.

### Watch out

1. Only the course repository is open in the editor sidebar. Other repository
   names in a file tree are the most common accidental leak in developer
   screencasts, and this video puts the file tree on screen for four minutes.
2. Do not scroll into the part of `CLAUDE.md` that lists the three things that
   look like bugs and are not, near the end of the file. That is a pointer to
   Exercise 7, Exercise 8 and Exercise 15 answers. Stop scrolling above it, or
   collapse the window before you reach it.
3. Do not read the file's approved statistics section aloud as a marketing beat.
   It is on screen and that is enough.
4. Do not present a `CLAUDE.md` as a magic file. State what it does, which is get
   read automatically at session start, and no more.
5. Keep the editor at recording font size for this whole segment. This is the
   longest reading shot in the module and a small font makes it useless on a
   phone.

## Video 2.3: Generation, Refactoring, and the Preservation Constraint

**Runtime:** 9 minutes
**On screen:** deck

### Say

Slides 12 to 14 are generation. Specifications in, code out, and the useful nuance
is that the quality of the output tracks the precision of the input parameters and
return types rather than the length of the description.

Slide 15 is the one that carries this video. Its first bullet now reads "Ask for
modernised syntax, and state explicitly what must not change", and that clause is
the whole of Exercise 5. Set the idea up before the exercise meets it, but do not
give away what happens.

The framing to use: "A refactor prompt that does not say what must not change is
heard as a rewrite prompt. Rewrites are frequently improvements, and improvements
break callers. In the next lab you are going to send the prompt that every
developer sends, and then you are going to look carefully at what came back. I am
not going to tell you what you will find."

Then name the pattern, because they will need the name twice more: a preservation
constraint states what must survive the change. Say that it recurs in Exercise 8
on performance instead of security.

Slides 16 to 19 run at pace. Modularisation, design patterns, and the split
between language-agnostic logic and language-specific syntax. On slide 19 add the
programme-level note in one sentence: every lab in this programme is Python, and
the same workflow applies with any mainstream runtime, with only the framework
name in the prompt changing.

### Show

1. Slides 12, 13, 14.
2. Slide 15, held longer than the others.
3. Slides 16, 17, 18, 19.

### Watch out

1. Do not describe the Exercise 5 trap here. If you say "it will replace your
   password hashing", the exercise is over before it starts and the learner never
   experiences the surprise that makes the lesson stick.
2. Do not demo a refactor in this video. There is no runtime budget for it and
   Exercise 5 does it properly.
3. Slide 15's remaining three bullets are vendor wording and read a little
   inflated. Narrate them plainly rather than emphasising them.

## Video 2.4: Documentation, Tests, and Consistency

**Runtime:** 8 minutes
**On screen:** deck

### Say

Slides 20 to 22 are documentation. The line worth adding, because no slide says it
and Exercise 6 depends on it: generated documentation describes what the code does
today, which means it is a snapshot and it goes stale silently. Confidently wrong
documentation is worse than none, because the next developer trusts it and stops
reading the code.

Slides 23 and 24 are tests. Read the useful mechanics: name the framework in the
prompt, ask for normal cases plus boundaries plus invalid input, and one assertion
focus per test.

Then say the thing that carries Exercise 6, and say it in these words because the
exercise is built on it: "A green suite tells you that the tests you have all pass.
It tells you nothing at all about the tests you do not have. In Exercise 6 you get
to green in about half the time, and then you spend the rest of the lab hunting
the inputs your generated tests never tried. That second half is the exercise."

Slide 25 is consistency. Keep it short. Slide 26 is takeaways, and close by
pointing at the handover: Exercise 6 produces a test suite and Module 3 opens by
running it again.

### Show

1. Slides 20, 21, 22.
2. Slides 23, 24.
3. Slides 25, 26, 27.

### Watch out

1. Do not name a specific testing framework version, and do not read a framework
   version off any screen.
2. Slide 23 names two test frameworks. One of them is not Python. Mention that
   the labs are Python and move on rather than opening a stack comparison you have
   no time for.
3. Resist adding a live docstring demo. Exercise 6 opens with exactly that, four
   minutes later.

## Video 2.5: Exercise 4, Write the Context File

**Runtime:** 12 minutes
**On screen:** terminal, plus editor

### Say

State the deliverable in the first ten seconds: by the end of this they will have
a `CLAUDE.md` at the root of a project of their own, and they will have proved it
works before requesting a single line of code.

Step 1, `cd` into the practice project and start Claude Code. Repeat the
observation from video 2.1, because it is the habit change: nothing was uploaded
and nothing was pasted.

Step 2 is the step that writes the outline for them. Send the prompt that asks it
to describe the project from the files it can see, and then to list separately
what it cannot determine from the files alone. Read the first list quickly. Slow
down on the second list and say: "That second list is not a limitation. It is the
table of contents for the file I am about to write. Everything on it is something
only a human can supply."

Step 3, why a file beats a pasted message. Three rows: next session, change
history, and the rest of the team. Say which row decides it in practice, and be
blunt about it: a brief you retype every session is a brief you stop writing by
Thursday.

Step 4, write the file. Six headings: what this is, tech stack, layout, what
already works, conventions, do not change. Type it live rather than pasting a
prepared file, because watching it get written is the point of the shot. Keep it
under one page and say so.

Step 5 is the verification step and it is what separates a brief that reads well
from a brief that works. Exit the session and start it again so the file loads
fresh, then ask for a five-line summary of purpose, stack, layout, conventions and
boundaries, and to stop and wait. Then score it out loud on all five. Say the
sentence: "If any one of those is wrong or vague, the file is at fault, not the
model."

Step 6, fix what it missed. Say the pattern that pays off: the additions that earn
their place are boundaries rather than background. Then send them to the course
repo's own file to read the intentional defects section, which is the worked
example they compare against.

### Show

1. Terminal, `cd` into the practice project, start Claude Code.
2. The Step 2 prompt and both lists in the response.
3. Editor, `CLAUDE.md` created at the practice project root, typed live with all
   six headings.
4. Terminal, exit the session, start it again, send the Step 5 prompt.
5. The five-line summary, scored out loud against the five checks.
6. Editor, one boundary added to the file.
7. Editor, the course repo's `CLAUDE.md`, intentional defects section, briefly.

### Watch out

1. Use a practice project, not the course repo. The course repo already has a
   context file at its root and the whole shot depends on writing one where none
   existed.
2. The practice project is on screen for twelve minutes. Do not use a real work
   project. Client names, internal service names and real dependency lists all
   leak from a file tree, and a `requirements.txt` from a work project is a
   disclosure.
3. Exit and restart the session visibly at Step 5. If you skip the restart, the
   verification proves nothing, and a sharp learner will notice.
4. Do not paste a prepared `CLAUDE.md`. Type it. If typing is too slow for the
   budget, type four headings live and paste the last two while narrating them.
5. If the Step 5 summary comes back perfect first time, do not manufacture a
   correction. Say: "Nothing to fix on this run. Notice how cheap the check was,
   and run it anyway the next time you edit the file, because the check is what
   tells you the file is doing anything at all."
6. Do not scroll the course repo's `CLAUDE.md` into the section listing the three
   things that look like bugs and are not.

## Video 2.6: Exercise 5 Part 1, Draft It From the Story

**Runtime:** 8 minutes
**On screen:** terminal, plus editor

### Say

Frame the three passes at the start: draft it clean from the story, refactor a
messy version of the same endpoint, then annotate what changed. Say that the
refactor is the part worth their attention, and leave it at that.

Read the user story and the narrowed scope: `POST /api/register`, three required
fields, validate, hash, return a consistent shape for success and error.

Step 1, send the drafting prompt as written in the lab and save the result as
`register_draft.py`. Say why the file is saved rather than admired: it is the
comparison object for Part 2.

Step 2 is the check, and one of the five points deserves a beat of its own. Score
the draft on the route and method, all three fields validated, the password going
through a named password hashing function rather than a plain digest, one response
shape across success and every error branch, and readable names.

On point three, say this: "Notice what earned that. I asked for password hashing
explicitly. Ask for registration code without mentioning hashing at all and you
will often get plain text storage. The constraint in my prompt prevented that, not
the model's good judgement, and that distinction is the difference between a
developer who gets good output reliably and one who gets it sometimes."

Close by handing over: pause, generate the draft, score it against the five
points, and this is the end of the first video.

### Show

1. Terminal, Claude Code running in the course repo clone.
2. The drafting prompt, sent.
3. Editor, `register_draft.py` saved in the exercise folder.
4. The five checks worked through against the file, cursor on the relevant lines.

### Watch out

1. Save the draft in the exercise folder with the exact filename the lab uses.
   Video 2.7 refers to it by name and a learner following along needs the names to
   match.
2. Do not open `messy_registration.py` in this video. Part 2 opens on it and the
   surprise depends on them meeting it fresh.
3. Do not run the endpoint. Flask is optional in this lab and reading is enough. A
   server start is thirty seconds you do not have and a port conflict is a lost
   take.
4. If the draft it produces is poor on one of the five points, keep it. A weak
   draft is a better shot than a perfect one, because Part 2 is about reviewing
   generated code rather than admiring it.

## Video 2.7: Exercise 5 Parts 2 and 3, The Refactor That Cannot Ship

**Runtime:** 12 minutes
**On screen:** terminal, plus editor with a side-by-side diff

### Say

This is the centrepiece of the module. The sequence is not negotiable: record the
naive prompt first, let it produce a breaking change, walk the consequence, and
only then send the constrained prompt. If you record the constrained prompt first
because it is tidier, the lesson is gone.

Step 3, they read the messy file themselves before prompting. Describe it
accurately: it works, and it is one function doing routing, validation, hashing,
database access and response formatting, with single-letter names and a validation
branch repeated several times, every branch returning the same unhelpful error.
Tell them to find at least eight problems and say there are more than eight. Do
not count them on camera and do not name the security ones.

Step 4, the naive prompt. Read it out and say who sends it: "This is the prompt
most developers send, near enough word for word. Refactor this endpoint into
cleaner, modular code, separate responsibilities, remove repetition, keep it
secure and maintainable. There is nothing wrong with that sentence. Watch what
comes back." Save the result as `register_refactored_v1.py`.

Step 5, the easy half first. Smaller functions, validation extracted, persistence
separated, one error shape, readable names. Then pivot hard, and use the lab's
question as the hinge: go back through the diff line by line and ask of every
change, is this a structural change or a change in behaviour? A structural change
moves code around. A behaviour change alters what the endpoint does, what it
stores, or what it returns. Both can be improvements. Only one of them can break
something outside this file.

Then find the credential handling change on camera and stop on it.

Step 6 is the beat the whole exercise exists for. Send the prompt that states
40,000 existing rows written by the original code and a separate login endpoint
that reads them, and demand a plain answer about whether any of those users can
still log in. Read the answer slowly.

Then say the sentence, and say it exactly this carefully, because getting it
slightly wrong turns a subtle point into a wrong one: "This change is not a
mistake. Replacing that hashing is correct security advice, and a reviewer who
blocked it outright would also be wrong. It is a correct improvement that cannot
ship on its own. It needs a migration path, and my prompt never asked for one.
Two things are true at the same time here: the assistant improved my code, and the
assistant broke my system."

Step 7, the constrained prompt. Same file, same request for cleaner code, plus the
preservation constraints block: existing rows must remain verifiable, if the
credential handling should change then describe a migration that upgrades on next
successful login instead of performing a swap, do not change the route or the field
names or the response keys or the status codes, and list every remaining behaviour
change under its own heading. Save as `register_refactored_v2.py`.

Step 8, check five things: route and field names and response keys and status
codes unchanged, existing credentials still work, any upgrade described as a
migration rather than performed, a behaviour changes section you agree with, and
the structural improvements still present. That last one matters: a preservation
constraint should not have cost them the clean code.

Part 3, steps 9 and 10, is the annotation and it is quick. Every change goes under
`SAFE` or `BEHAVIOUR CHANGE`. Close on the lab's final question and let it sit:
"If you had shipped version one, when would you have found out?" Then answer it:
not at code review, not in the test suite, because nothing in that repo logs an
existing user in. You would have found out from support tickets. And the thing
that would have caught it is a test that authenticates an existing user, which is
Exercise 6.

### Show

1. Editor, `messy_registration.py`, scrolled once end to end.
2. Terminal, the naive prompt, sent. `register_refactored_v1.py` saved.
3. Editor, original and version one side by side. Walk the structural improvements
   quickly, then walk the diff again for behaviour changes.
4. Cursor held on the credential handling line in version one.
5. Terminal, the 40,000-row consequence prompt, answer read in full.
6. Terminal, the constrained prompt with the preservation constraints block
   visible on screen as one block. `register_refactored_v2.py` saved.
7. Editor, version two, the five checks and the behaviour changes section.
8. Editor, the change log at the top of version two with `SAFE` and
   `BEHAVIOUR CHANGE` groups.

### Watch out

1. **The naive prompt's output varies between takes, and it may preserve the
   hashing on its own. Plan the fallback before you record.** Three options, in
   order of preference. First, before the recording day, run the naive prompt three
   or four times off camera and keep one output that did swap the hashing, saved as
   `register_refactored_v1.py`. If the take does not produce a swap, open that
   saved file and say honestly: "On this run it kept the existing hashing. Here is
   what the same prompt produced on a different run, and this is the outcome you
   need to be ready for." Second, if you would rather not cut to a saved file,
   pivot the beat to whatever behaviour change did appear, and there will be one:
   a changed response shape, a changed status code, a raised minimum password
   length, or a changed error body. Run the Step 6 consequence prompt against that
   change instead and ask the same two reviewer questions. Third, do not re-roll
   the prompt on camera more than once looking for the outcome you wanted. It looks
   like fishing and it is nine minutes of runtime.
2. Whichever branch you take, never say "it always does this" or "it will replace
   your hashing". Say "it often does" and "the prompt did not require it not to".
   A published video cannot guarantee a model's behaviour and a learner whose run
   differs will conclude the course is wrong about everything else too.
3. Do not print or echo any hash value beyond what is already in the file on
   screen, and do not invent a real-looking password anywhere in this video.
4. This video runs at the twelve-minute cap and it carries three prompts, a diff
   walk and an annotation. Time it once off camera. If you are over, the annotation
   in Part 3 compresses safely to sixty seconds. The Step 6 consequence walk does
   not compress at all.
5. Do not repair `messy_registration.py`. It is a teaching artefact and every
   defect in it is load-bearing. Your refactored output goes in new files.
6. Keep the side-by-side diff readable at recording font size. If two panes are
   too narrow, scroll one file rather than splitting the window.

## Video 2.8: Exercise 6 Part 1, Docstrings, Notes, and Green

**Runtime:** 11 minutes
**On screen:** terminal, plus editor

### Say

Say the shape first, including the honest warning that the first half is the
setup: docstrings, usage notes and a passing suite are steps one to seven, and the
reason the exercise exists is in the second video.

Step 1, read the three functions and write nine notes, three per function: what
goes in, what comes out including for empty input, and one input they are
genuinely unsure about. Emphasise the third. Say: "Keep those three uncertain
inputs on paper. How many of them the generated tests happen to cover is the
measurement this whole exercise is built around, and you cannot recover it later
if you skip this."

Step 2, ask for docstrings and only docstrings. Point at the closing sentence of
the prompt, "do not change any logic, any name, or any default value", and say
why: documentation requests turn into refactors more often than any other kind of
request, because the code reads badly and the assistant is trying to help.

Step 3, verify the docstrings against the code rather than against expectations.
Four checks, and check four is the real one: did it document behaviour that is not
in the code? Say: "When you find a sentence describing what the function should do
rather than what it does, do not fix the code. Mark the line. It is a finding and
you need it in step nine."

Step 4, usage notes, then run every worked example. Say the line: "An example that
has never been executed is a guess with formatting." Run one on camera and let it
be a real result.

Step 5, why these three functions deserve tests: a parser fails on inputs its
author never pictured, a combiner has boundaries, and aggregation over nothing is a
special case in every language.

Step 6, ask for tests in a separate prompt and in this order. Say why the order
matters, because it is a real and non-obvious mechanism: requested together, the
tests tend to assert the behaviour just described in the docstring rather than the
behaviour in the code, and you lose the independent check that is the entire value
of having tests.

Step 7, run them and fix what fails. Failures here are normal. When feeding a
failure back, paste the exact pytest output rather than a description of it,
because the traceback is better input than a summary of the traceback. And one
rule: when a test disagrees with the code, work out which one is wrong before
changing either.

End on green and say plainly that green is the halfway point, not the finish.

### Show

1. Editor, `undocumented_utils.py`, all three functions.
2. Notes file, nine lines, with the three uncertain inputs visibly marked.
3. Terminal, the docstrings prompt, result applied.
4. Editor, the four verification checks against the code.
5. Terminal, the usage notes prompt. Editor, `README-usage.md` saved.
6. Terminal, one worked example executed in a Python session.
7. Terminal, the tests prompt in a separate turn.
8. Terminal, `pytest -v` from the `starter/` folder. At least one failure fixed on
   camera by pasting the real output back.
9. Terminal, `pytest -v` green.

### Watch out

1. Run pytest from inside the `starter/` folder. Run it from the repo root and you
   get a module import error, which is a confusing thirty seconds on camera and a
   documented learner problem.
2. Do not modify `undocumented_utils.py`. It has no planted bugs and its behaviour
   is the specification the second video interrogates. If a docstring prompt
   silently edits the logic, restore from git on camera and re-run the prompt with
   the do-not-change line intact. That is a good shot, not a lost take.
3. If every generated test passes first time, say so and say what it suggests:
   the tests may have been written against the docstrings rather than the code.
   The fix is a fresh conversation supplying only the module.
4. Do not skip running the worked examples for time. It is the shot that proves
   the claim you just made about unexecuted examples.
5. Keep the pytest output at a font where the failure line is readable on a phone.
   Traceback frames are the hardest thing to read in any lab in this programme.

## Video 2.9: Exercise 6 Part 2, The Hunt

**Runtime:** 11 minutes
**On screen:** terminal, plus notes

### Say

Open by restating the state, because this is a separate video: the suite is green,
and green is the claim being tested here. Say the sentence the exercise is built
on: "Green means the tests I have all pass. It says nothing about the tests I do
not have."

Step 8, first do it by hand. Take the three uncertain inputs from step 1 and check
each against the test file. Yes or no for each. Do this before prompting anything.

Then widen the search with the gap-list prompt, naming the categories explicitly:
empty input, boundary values, legal but unexpected inputs, inputs where the same
call could reasonably behave two ways, and inputs that return a result where an
error might have been more useful. Say that a vague version of this prompt returns
"test your edge cases" and nothing usable.

Now the part that separates this from a list-generating exercise, and the part to
give the most airtime. Do not trust the list and do not write assertions from it.
For each claimed gap, open a Python session, call the function, and record what
actually comes back. Use `repr`. Say why: the difference between an empty string,
a zero, an empty list and a `None` is invisible in ordinary print output, and those
four are exactly the values you are trying to tell apart.

Do at least three of these live, one per function, and let one of them come back
as not a real gap. Say: "That one was not a gap. That is the expected outcome for
some of them, and verifying is the step rather than an interruption to it."

Then the three-way decision for each recorded value: correct, so lock it in with a
test; a bug, so document what it should be, mark it expected-to-fail, and leave the
module alone because this is a teaching file and they do not have the authority to
change its contract; or undecided, so write down both readings and which they would
ship.

Land the undecided case hard, because it is the intellectual centre of the module:
"At least one of these will be undecided, and when it is, notice what has happened.
The code cannot tell me the answer, because the code is the behaviour. Only the
intended contract can, and nobody ever wrote it down. That is what missing
documentation actually costs, and it is why the docstrings came before the tests."

Step 9, write the contracts down, then mark every docstring sentence `D` for
descriptive or `I` for intentional. Say the finding: most generated docstrings are
entirely descriptive and read as though they were intentional.

Close on the handover to Module 3, in one sentence: keep this test file, because
Module 3 opens by running it again.

### Show

1. Terminal, `pytest -v`, green, as the opening frame.
2. Notes file, the three uncertain inputs checked against the test file by hand.
3. Terminal, the gap-list prompt and its function-by-function answer.
4. Terminal, three one-line Python calls using `repr`, actual values recorded in
   the notes file each time.
5. Notes file, the three-way decision recorded against each value, including one
   marked undecided with both readings written out.
6. Editor, one expected-to-fail test added, and the docstrings marked `D` or `I`.
7. Terminal, `pytest -v` once more so the final state is on screen.

### Watch out

1. Do not fix `undocumented_utils.py`, and do not let a prompt talk you into it on
   camera. The whole second half depends on the module's behaviour staying exactly
   as shipped.
2. Use `repr` in every call, visibly. If you print without it once, you undercut
   the point you just spent thirty seconds making.
3. Do not present the undecided case as a failure to reach an answer. It is the
   deliverable. If you sound apologetic about it, learners will treat it as
   something to avoid rather than something to record.
4. Do not name which behaviour will land in the undecided category before you get
   there. Let it emerge from the calls you run.
5. This video ends the module. Do not add a detailed preview of Module 3's
   contents beyond the one sentence about the test suite, because module ordering
   and content can change without this video being re-recorded.

## The teaching points that carry this module

1. Project context belongs in a file at the repository root that gets read
   automatically, not in a message pasted at the top of a chat, because a file
   survives every session and is version controlled.
2. A context file holds durable facts and boundaries, never the current task, and
   the boundaries are the part that earns its keep.
3. A refactor prompt without a preservation constraint is heard as a rewrite
   prompt, and rewrites break callers.
4. "The assistant improved my code" and "the assistant broke my system" can both
   be true of the same change, and the fix is a constraint in the prompt rather
   than a better model.
5. A green test suite measures the tests you have and says nothing about the tests
   you do not have.

## Questions learners will ask, and the answers

| Question | Answer |
|---|---|
| Do I need an API key for this module? | No. Claude Code needs to be installed and signed in, but the API key requirement starts in Module 4. |
| Claude Code seems to ignore my `CLAUDE.md`. | It is either not at the root of the working directory, or the session started before you saved it. Move it to the root, exit, and start again. |
| How long should a context file be? | Under a page. If it grows past that, task detail has leaked into it. Move anything that will be false next week into the prompt instead. |
| Should I put my current sprint work in the context file? | No. Durable facts in the file, current task in the prompt. A stale instruction is worse than a missing one. |
| My refactor did not replace the password hashing. Did I do it wrong? | No. Outputs vary between runs. Look for whatever behaviour change your version did make, and run the same consequence check against that. The lesson is the constraint, not the specific change. |
| The refactored code is genuinely better. Why would I not ship it? | Because better and shippable are different questions. A change to stored credential format needs a migration path, and until it has one it cannot go out on its own. |
| My version two lost the clean structure. | The constraint list was read as "change nothing". Add one line asking for the structural refactor to be as thorough as before. |
| Every generated test passed first time. Is that good? | It usually means the tests were written against the docstrings rather than the code. Start a fresh conversation, supply only the module, and ask again. |
| `ImportError` when I run pytest. | The test file is not in the same folder as the module, or you ran pytest from the repo root. Save it in `starter/` and run from `starter/`. |
| Can I do these labs in another language? | The labs are Python throughout, deliberately, to keep setup to one runtime. The same workflow applies with any mainstream test runner, and only the framework name in your prompt changes. |
| Why can I not just fix the bug I found in the utility module? | Because it is a teaching file and you do not have the authority to change its contract. Record the finding, mark the test expected-to-fail, and leave the module alone. |

## Pre-record checklist for this module

1. Confirm the deck is the `- REVISED` file, that slide 8 exists and is titled
   "The Project Context File", and that slide 15 bullet one reads "Ask for
   modernised syntax, and state explicitly what must not change".
2. Shell prompt reduced to the directory name. No machine name, username, branch
   or virtual environment decoration. Fresh shell.
3. Terminal and editor fonts set large and checked on your smallest target screen.
   Fix the window size now and do not change it for the rest of the programme.
4. Editor sidebar has the course repository only. All other folders and workspaces
   closed. All tabs closed.
5. Course repo cloned at a short recording path with no personal directory names
   in it.
6. Practice project created for Exercise 4, three to ten files, containing nothing
   from any real work project. Confirm it has no `CLAUDE.md` yet.
7. `pip install pytest`. Confirm `python --version` shows 3.11 or later.
8. Confirm Claude Code starts from the terminal inside the course repo clone, and
   note whether it prints anything on startup you must not read aloud.
9. Open the course repo's `CLAUDE.md` and set a scroll stop above the section
   listing the three things that look like bugs and are not, so video 2.2 cannot
   reveal it.
10. Run the Exercise 5 naive prompt three or four times off camera. Save one
    output that produced a breaking change as your fallback
    `register_refactored_v1.py`, and note which take you took it from.
11. Time video 2.7 once off camera end to end. It is the only video in this module
    at the twelve-minute cap and it is the one that must not be rushed.
12. Verification run, do this last. From
    `module-2-claude-code/03-labs/exercise-06-docs-and-tests/starter/`, confirm
    `python -m pytest -q` reports no tests collected before you record video 2.8,
    so the green run in that video is one you actually produced on camera rather
    than one left over from a previous take. Delete any
    `test_undocumented_utils.py`, `README-usage.md`, `.pytest_cache` and
    `__pycache__` left behind by a rehearsal.
