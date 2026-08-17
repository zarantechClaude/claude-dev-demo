# Module 3 Recording Script
## Debugging, Optimization, and Code Reviews

> **Trainer only. Do not publish, do not attach to a learner handout, and do not
> paste any section of this file into a slide.** It names the planted defects in
> `buggy_inventory.py`, `slow_lookup.py` and `sample_pr.diff`, the admissible
> threshold range, and both match counts from Exercise 8. If a learner reads this
> file, all three exercises in this module stop working.

**Total runtime:** 80 minutes across 10 videos
**You need before you start:**

1. A terminal at the same settings you used in Module 2. Same font, same window
   size, same minimal prompt, same theme. This module is mostly terminal and a
   change of appearance between modules reads as a different course.
2. Claude open in the recording browser profile. **Claude Code is not needed in
   this module.** Learners run tests and scripts locally and prompt in the
   browser, and saying so out loud in video 3.1 saves a support question.
3. `pip install pytest`.
4. The finished Exercise 6 test suite from Module 2, in the state a learner leaves
   it: green, with at least one expected-to-fail test in it. Video 3.1 opens on it.
5. The revised deck open in presenter view:
   `module-3-debugging/01-deck/revised/Module 3 - Debugging, Optimization, and Code Reviews - REVISED.pptx`
6. Both verification runs from `docs/recording-hygiene.md` section 6 completed on
   your recording machine, on your recording day. Exercise 7 must show 3 failed,
   and Exercise 8 must show 24326 matches in roughly 2 to 3 seconds. Do not record
   this module until both are confirmed.

The chosen split: the 35-minute deck runs as four lectures of 8, 9, 10 and 8
minutes. The 10-minute lecture is the performance block, because slide 13 carries a
correction that needs explaining rather than reading. All three exercises are 15
minutes, which is over the cap, so each splits into two videos at the seam its own
lab already has. The programme map's granularity table says "everything else, one
video", which cannot be reconciled with the twelve-minute rule for a 15-minute lab.
The cap wins here, and the table needs updating.

## Video breakdown

| Video | Covers | Slides | Runtime |
|---|---|---|---|
| 3.1 | Cold open on the Module 2 suite, presenting errors, traces, repro steps | 1 to 7 | 8 min |
| 3.2 | Isolating root causes, binary search, ranked hypotheses, alternative fixes | 8 to 11 | 9 min |
| 3.3 | Bottlenecks, quadratic loops, I/O, complexity, memory | 12 to 16 | 10 min |
| 3.4 | Patterns, design, pull request partner, review prompts, human sign-off | 17 to 26 | 8 min |
| 3.5 | Exercise 7 part 1, steps 1 to 6, first failure and the derived range | none | 8 min |
| 3.6 | Exercise 7 part 2, steps 7 to 10, still red, ranked hypotheses, green | none | 7 min |
| 3.7 | Exercise 8 part 1, steps 1 to 5, baseline and diagnosis | none | 7 min |
| 3.8 | Exercise 8 part 2, steps 6 to 10, optimise, verify, then time | none | 8 min |
| 3.9 | Exercise 9 part 1, steps 1 to 4, your own read and Round 1 scored | none | 8 min |
| 3.10 | Exercise 9 part 2, steps 5 to 10, Round 2 and the comparison | none | 7 min |

Deck 35 minutes, labs 45 minutes, 80 total, matching `docs/programme-map.md`.

## Video 3.1: A Green Suite That Is Not Finished

**Runtime:** 8 minutes
**On screen:** terminal, then deck

### Say

Open in the terminal, not on a slide. This is the only module that opens on a cold
run of the previous module's artefact and the continuity is worth protecting.

Change into the Exercise 6 starter folder and run `pytest -v` on the suite you
finished Module 2 with. Then narrate what is actually on screen, which is a green
suite with a parked failure in it.

Say this: "This is where Module 2 left us. Everything passes. Now look at the line
marked expected to fail. In Module 2 I found a behaviour I judged to be wrong, I
wrote a test that documents what it should be, and I marked it expected to fail so
the suite would stay green. That is a legitimate thing to do. It is also a bug I
agreed to stop looking at."

Then unpark it on camera. Delete the marker, re-run, and let the suite go red.
Say: "That red line is where Module 3 starts. For the rest of this module the
suites are red, and a red suite is the most useful thing in debugging, because it
is a specification that disagrees with your code and tells you exactly where."

Then state the module requirements, briefly: a terminal and pytest, no Claude Code,
no API key. Learners run code locally and prompt in a browser.

Slide 4 is the exercise map. Read the three and add one line each: a failing suite
where the failure count and the problem count are different numbers, a slow
function where the fast answer is the wrong answer, and a pull request reviewed
twice with two different prompts.

Slides 5, 6 and 7 are the input-quality block and they run at pace. The through
line: everything in this module is about the quality of what you hand over.
Complete error messages rather than the last line, the entire stack trace rather
than the final frame, and repro steps precise enough that someone else can trigger
it. On slide 6, add the sentence that Exercise 7 depends on: truncating the trace
is the single most common reason an AI debugging prompt comes back with generic
suggestions, because there was nothing in the prompt to reason from and it reasoned
about the category of problem instead.

### Show

1. Terminal, `cd` into the Exercise 6 starter folder, `pytest -v`, green.
2. The expected-to-fail line, cursor on it.
3. Editor, the marker removed. Terminal, `pytest -v` again, red.
4. Slides 1 to 4.
5. Slides 5, 6, 7.

### Watch out

1. If your finished Exercise 6 suite has no expected-to-fail test in it, do not
   improvise one on camera. Add it off camera first, from the finding you actually
   recorded in Module 2, so the shot is honest. If you genuinely recorded no bug
   finding, open instead on the undecided behaviour you did record and add one
   assertion for the reading you would ship. Either way the module opens on red.
2. Do not repair the utility module to make the red line go away. It is a teaching
   artefact and Module 2 depends on its behaviour being unchanged.
3. Scrollback. This is the first terminal shot of the module and anything above
   the visible area from an earlier take is in frame if you scroll at all. Clear
   the screen before you start.
4. Restore the expected-to-fail marker after the take, so the repository state
   matches what Module 2 tells learners to leave behind.
5. Do not name a model version anywhere, and do not read one off a browser tab if
   you switch to one.

## Video 3.2: Root Causes and Ranked Hypotheses

**Runtime:** 9 minutes
**On screen:** deck

### Say

Slide 8 is isolating root causes. The practical framing: most of the value in
these prompts comes from asking a question that could be answered wrong. "What is
wrong with this code" cannot be answered wrong. "Which of these three lines could
produce this exception, given this input" can.

Slide 9 is binary search debugging, and it deserves a plain-language version
because the slide's phrasing is abstract. Say it as a procedure: you know a good
state and a bad state, you cut the distance between them in half, you check which
half you are in, and you repeat. It works on lines of code, on commits, and on
input size, and the reason it is worth naming is that it turns an unbounded search
into a fixed number of steps.

Slide 10, ranked hypotheses, is the most reusable pattern in the module. Say it
this way: "Ask for three possible causes ranked by likelihood, plus one cheap check
you can run for the top one. That works on any failure where the code ran to
completion and the answer was wrong, which is most of the failures you will meet at
work, and it is the pattern you will use in the second half of Exercise 7."

Then add the discipline point, because it is what separates this from a guessing
game: when the first hypothesis is wrong, that is a result, not a wasted step. You
move to the second with one possibility eliminated.

Slide 11 is evaluating alternative fixes. Ask for options ranging from quick to
comprehensive, compare side effects, and pick the one that fits the system rather
than the one that reads best.

### Show

1. Slides 8, 9, 10, 11 at an even pace, roughly two minutes each.

### Watch out

1. Four dense slides with no screen cut is the flattest stretch in the module. Vary
   your pace, and slow down deliberately on slide 10 since it is the one they will
   reuse.
2. Do not demonstrate a debugging prompt here. Exercise 7 does it against a real
   traceback ten minutes later and doing it twice costs you a lab video.
3. Do not extend slide 9 into a version control demonstration. The commit-bisect
   version of binary search is a good aside and it needs a terminal, a repository
   with history, and three minutes you do not have.

## Video 3.3: Performance, and the Word That Costs You Credibility

**Runtime:** 10 minutes
**On screen:** deck

### Say

Slide 12 sets up measurement: share execution times and profiling output rather
than asking whether code looks slow.

Slide 13 is the slide this video is built around, and it carries a correction. The
earlier version of this slide said nested loops cause exponential execution time
growth. That is wrong. It now says quadratic, and Exercise 8 demonstrates exactly
that growth, so the slide and the lab now agree.

Explain the difference properly rather than asserting it, because the explanation
is what makes it stick:

1. Quadratic means the work grows with the square of the input. Ten times the data
   is a hundred times the work.
2. Exponential means the work multiplies for each additional item. Ten more items
   is not ten times the work, it is a number with no useful everyday name.
3. Nested loops over the same collection are quadratic. They are not exponential,
   and the two are not interchangeable words for slow.

Then say why it matters on camera, in these terms: "This is not pedantry. In a
review you are trying to persuade someone to spend time on a change. If you tell a
senior engineer that a nested loop is exponential, the correction happens in front
of everyone, and after that your estimate of the risk is the thing being
questioned rather than the code. Precision in a review is credibility, and
credibility is the only currency a reviewer has."

Bullet four of slide 13 is Exercise 8's lesson in one line: confirm the output is
identical before trusting the speedup, because a faster wrong answer is still
wrong. Preview it without spoiling it: "You are going to make a function about a
thousand times faster in the next lab. Whether it still returns the right answer
is a separate question, and it is the only one that matters first."

Slides 14, 15 and 16 run at pace. Batching and caching for I/O, complexity for
algorithms, generators and object lifetimes for memory. On slide 15, one caveat is
worth stating: its example moves from linear to logarithmic, which is a different
change from the one in Exercise 8. The lab goes from quadratic to linear. Say that,
so nobody arrives at the lab expecting a binary search.

### Show

1. Slide 12.
2. Slide 13, held for four minutes. Say the numbers out loud: ten times the data,
   a hundred times the work.
3. Slides 14, 15, 16.

### Watch out

1. **Do not say "exponential" anywhere in this video, including as the wrong
   answer you are correcting, unless you immediately correct it in the same
   sentence.** If you fumble the sentence, take it again. This is the one video in
   the module where a single wrong word undermines the point being made.
2. Do not open a terminal to demonstrate timing here. Exercise 8 is the
   demonstration and it has real numbers.
3. Do not quote a specific speedup multiple in this video. The number belongs to
   the machine you ran it on, and quoting it here means re-recording this lecture
   if the constants are ever retuned.
4. Do not read a big-O expression as though it were a fact about the language.
   Growth class is a property of the algorithm.

## Video 3.4: Review, and Who Signs Off

**Runtime:** 8 minutes
**On screen:** deck

### Say

Slides 17 and 18 are design suggestions and they run quickly.

Slide 19 opens the review block. The useful framing is that a review prompt is a
job description. If you do not say what the job is, you get everything at equal
weight.

Slides 20 to 22 are the three review lenses: correctness, clarity, security. On
slide 22, security, add the practical note that Exercise 9 will prove: a bare
review prompt reports style issues and buries the serious finding, not because
style issues are not real, but because they were never excluded. You have to name
the categories you do not want.

Slide 23 carries the second correction in this deck. It previously suggested an
approved emoji as a sign-off format. It now asks for a verdict in words: must fix
before merge, or safe to merge with notes. Say why the change matters: "An emoji is
not a review outcome. Must fix before merge and nice to have are categories that
change what somebody does next. That is the whole test of a severity label."

Slide 24 is where the module lands ethically and it is worth thirty seconds of
weight: Claude is a first pass before a human reviewer, and human accountability
for the merge does not move. Say it plainly: "If you approve a pull request, you
approved it. Where the finding came from is not a defence."

Slide 25, key takeaways. Then close.

### Show

1. Slides 17, 18.
2. Slides 19, 20, 21, 22.
3. Slide 23, held slightly longer.
4. Slides 24, 25, 26.

### Watch out

1. Do not use an emoji on screen or in narration anywhere in this module. The deck
   correction removed one and reintroducing it verbally undoes the point.
2. Do not overclaim what a review prompt catches. Everything in Exercise 9 is
   framed as measure what your run does, not as a guarantee, and the lecture has to
   match that or the lab reads as a broken promise.
3. Do not turn slide 24 into a policy statement about the learner's employer. Say
   the accountability point and leave the policy to them.

## Video 3.5: Exercise 7 Part 1, One Fix Is Not the Fix

**Runtime:** 8 minutes
**On screen:** terminal, plus browser and editor

### Say

Set the discipline first: diagnose, fix minimally, re-run. One correction at a
time, verified each time.

Step 1, run `pytest -v` and record four facts before touching anything: how many
tests ran, how many failed, the error type on the last line of each failure, and
for each failure whether it raised an exception or returned a wrong value.

Read the result on screen exactly. **Three tests, three failures.** Two of them
raise the same exception type and one is an assertion that returned the wrong
number. Then make the observation that the whole lab hangs off: "Three failures.
Not three problems. Those are different numbers and I do not yet know what the
second number is."

Emphasise the fourth column, because it is the one people skip and it decides the
approach: an exception gives you a file and a line number, and a wrong value gives
you neither.

Step 2, take the failure with a traceback and copy the whole section, from the test
name down to the error line, not the last line on its own.

Step 3, ask for the root cause and explicitly not the fix. Say why: "Ask for a
rewrite and you will get a rewrite, it will probably work, and you will have
learned nothing you can reuse."

Step 4, verify the diagnosis yourself against the error type and the line number
before acting on it. Fifteen seconds, and it is what stops ten minutes spent fixing
the wrong thing.

Step 5 is the best part of this lab and it needs the airtime. The failing line does
not determine the fix. The function reads a value it was never given, the tests
never supply it, and nothing in the file supplies it, so "what should this value
be" has no answer inside the failing line. The tests are the only specification
available.

Have them derive the range on paper before prompting: one test gives the lower
bound, another gives the upper bound, and the answer is a range rather than a
number. Then check the derivation with the prompt that asks for both bounds
separately, naming which test produces each. Say the rule for disagreements: the
tests decide, so redo the arithmetic against the assertions until you can see which
of you is wrong.

Step 6, apply the minimal fix. A parameter with a default inside the derived range,
and nothing else. Do not tidy the loop, do not rename anything, and do not edit the
tests. Say that minimal is a constraint on the developer rather than on the model,
because a large fix hides which change mattered.

Hand over on a pause before the re-run, so the re-run opens the next video.

### Show

1. Terminal, `pytest -v`, the full output with all three failures visible.
2. Notes file, the four facts, with the failure count written down.
3. Terminal, the whole failing section selected and copied.
4. Browser, the root cause prompt with the function and the full traceback pasted.
5. Editor, the failing expression, confirming the diagnosis against it.
6. Editor, `test_buggy_inventory.py`, both relevant fixtures on screen while you
   derive the bounds.
7. Notes file, the arithmetic for the lower and upper bound, named by test.
8. Editor, the minimal fix applied to `buggy_inventory.py` only.

### Watch out

1. **The count on screen must be three failures.** If it is one or two, the
   artefact has changed and this narration is wrong. Stop and re-run the
   verification from `docs/recording-hygiene.md` before recording another frame.
   Delete `.pytest_cache` and `__pycache__` first, since a stale cache is the usual
   cause.
2. Do not say the admissible range out loud before the derivation. Deriving it is
   the transferable skill in the lab and stating it turns the exercise into typing.
3. Do not edit `test_buggy_inventory.py` at any point, and do not let a prompt
   suggest it. It is the specification. Say that on camera when you paste it.
4. Run pytest from inside the `starter/` folder or you get a module import error.
5. Do not paste the `TEACHING ARTEFACT` header into the browser. It points at the
   defect register.
6. Browser shot: model picker out of frame, sidebar clean.

## Video 3.6: Exercise 7 Part 2, Still Red

**Runtime:** 7 minutes
**On screen:** terminal, plus browser and editor

### Say

Open with a one-line recap and then the reveal, because the reveal is the reason
this lab exists and it now sits at the head of a separate video: "One fix applied,
minimal, exactly as diagnosed. Watch what happens."

Step 7, re-run. The exception type from Step 1 is gone from the output. And the
suite is still red.

Land it: "I fixed the thing the traceback pointed at, and the suite is still
failing. This is the lesson. Failure count and problem count are not the same
number, and if I had applied every change I could think of and run the suite once
at the end, I would have no idea which of them did what."

Step 8, read what is left and notice it is a different animal. Nothing raised.
There is no traceback pointing at a broken expression. The function ran to
completion and returned a number that is not the number the test expects. So the
Step 3 prompt does not work here, because a trace-based prompt needs a trace.

Ask for ranked hypotheses instead, with the assertion line, the reported actual
value, and the function. Three possible causes ranked by likelihood, plus one cheap
check for the top one, and no rewrite.

Step 9, work the list from the top. Say the discipline line again, because it is
the transferable habit: if the first hypothesis is wrong, that is a result and you
move to the second with one possibility eliminated.

When you find it, apply the same minimal discipline. One line, nothing else
touched.

Step 10, once green, improve the failure message for whoever meets the next one.
Keep the existing exception type, name the offending key in the message, and do not
expose the whole inventory in the error. Say why that last constraint is there: an
error message is a place data leaks, and dumping a whole structure into an
exception is how internal data ends up in a log aggregator.

Then verify the final state: three tests passing, and a diff that touches the
module and nothing else.

Close on the takeaway in the lab: two kinds of failure, two techniques, one habit.
The habit is running the suite after the first fix rather than after the last one.

### Show

1. Terminal, `pytest -v`, the exception gone and one failure remaining. Hold this
   frame.
2. Terminal, the remaining failure section, showing the actual and expected values.
3. Browser, the ranked hypotheses prompt and its three ranked answers.
4. Terminal, the cheap check for hypothesis one, run live.
5. Editor, the one-line fix.
6. Terminal, `pytest -v`, three passing.
7. Browser, the failure-message prompt. Editor, the improved message applied.
8. Terminal, `pytest -v` and `git diff`, showing one file changed.

### Watch out

1. Do not fix both problems in Part 1 and then show a single green run. The whole
   value of this lab is the red run in the middle, and it is now the opening beat
   of this video.
2. Do not name the arithmetic mistake in the second defect before the ranked
   hypotheses come back. If the ranked list happens to put it first, that is a good
   outcome, and you say so and run the cheap check anyway.
3. `git diff` will show your Part 1 change as well. That is fine and it is the
   point. Confirm out loud that the test file is untouched.
4. If your terminal has scrollback from Part 1, clear it before this take. The
   opening frame needs to be an unambiguous fresh run.
5. Keep the final `pytest -v` on screen long enough to read on a phone.

## Video 3.7: Exercise 8 Part 1, Measure Before You Touch Anything

**Runtime:** 7 minutes
**On screen:** terminal, plus browser

### Say

Say the order at the top, because the order is the exercise: measure, diagnose,
change, check the answer, and only then look at the clock. Speed is the easy part.

Step 1, run `python slow_lookup.py` and record two numbers, not one. The match
count and the elapsed time. Read both off the screen deliberately, and write both
into the notes file. Say: "Two numbers. Most people record the time and not the
count, and the count is the one that catches the mistake we are about to make."

Let the run take its two seconds without talking over all of it. The pause is doing
work here: the audience should feel the delay.

Step 2, why the baseline comes first. The obvious reason is that you cannot claim
an improvement you did not measure. The less obvious one is that the baseline
catches the two embarrassing cases: the change that made it slower, and the change
that made it faster by doing less work than it was supposed to. Neither is visible
without a recorded starting point.

Step 3, read the function and describe the work. Two loops, the outer one per item
in `wanted`, the inner one per item in `catalogue`. At the default size that is
twelve thousand times twelve thousand, which is 144 million comparisons to produce
one integer.

Then name the growth correctly and repeat the credibility point from slide 13,
briefly: it is quadratic, ten times the data is a hundred times the work, and
calling it exponential in a review costs you the argument.

Also read the docstring out loud, slowly, and flag it as load-bearing without
saying why: "Read that second line again. Duplicates in the catalogue count each
time. Hold on to that sentence, because you are going to need it in about four
minutes."

Step 4, ask for a diagnosis and explicitly not optimised code yet. Step 5, compare
its diagnosis with theirs on two points: did it identify the nested scan rather
than something incidental, and did it name the complexity class correctly.

### Show

1. Terminal, `python slow_lookup.py`. Let the elapsed time land.
2. Notes file, both numbers written in.
3. Editor, `count_matches`, including the docstring, with the cursor on the
   duplicates sentence.
4. Notes file or editor, the comparison count written out: 12,000 times 12,000.
5. Browser, the diagnosis prompt and its answer.
6. Notes file, the two comparison points ticked.

### Watch out

1. **The match count on screen must be 24326.** That number is the correctness
   anchor for the entire second half of this lab. If it is different, the artefact
   or the seed has changed and both videos need re-planning. Confirm before you
   record.
2. Elapsed time is machine dependent. Roughly two to three seconds is the target.
   Under about 1.5 seconds and the audience does not feel the delay, over about
   five and you are sitting in silence. Retune `n` off camera if needed and re-run
   to confirm the count is still 24326.
3. Do not say what the wrong optimisation returns. That number belongs in the next
   video and only if it actually appears on screen.
4. Do not edit `random.seed(42)`. Identical data across runs is what makes the two
   versions comparable.
5. Do not read the elapsed time as a precise claim. Say "about two seconds".

## Video 3.8: Exercise 8 Part 2, The Fast Wrong Answer

**Runtime:** 8 minutes
**On screen:** terminal, plus browser and editor

### Say

Step 6, ask for the optimised version with the same signature and a two-sentence
explanation of the main change. Save it as `fast_lookup.py` with the function name
kept, so the harness can import both.

Step 7 is ninety seconds and it is what the exercise is built around, so do not
skip it for pace. Before running anything, predict the answer. Read the original
docstring again, one line at a time, and state in your own words what the function
is supposed to return, being precise about what happens when the same value appears
in the catalogue more than once. Then read the optimised version line by line and
predict the number it will return. Not "the same number". Reason it out from the
code on screen.

Say why this matters: "If the two predictions differ, I already know what I am
about to see. If they agree, I am about to confirm it. Either way I am testing a
prediction rather than reading a result, and those are different activities."

Step 8, build the comparison harness and run it. Then point at where the assertion
sits, because that placement is the teaching point: it runs before the speedup is
printed. Say the sentence: "If the answer changed, the speedup is not a result, it
is a distraction. A harness that prints the ratio first will get the ratio quoted in
a stand-up meeting and the assertion looked at never."

Step 9, take the outcome you got, and both outcomes are part of the exercise.

**If the assertion failed**, which is the common case with a membership-set
optimisation, stop and sit on it. Read both numbers off the screen: the original
total and the new total. Then say: "That version is faster and wrong. Sit with that
for a second, because it is worse than slow code, not better. Slow code announces
itself. A wrong total does not, and it gets copied into a report and believed."
Then work out what the new version is actually counting: it is answering how many
wanted values appear at all, rather than how many times they appear. Then re-prompt
with the preservation constraint, stating that the original counts every occurrence
so a value appearing three times contributes three, and that the optimised version
must return an identical total for identical input.

**If the assertion passed on your take**, do not fake a failure and do not re-roll
repeatedly. Say: "This run returned the right total. That is a good outcome and it
is not the interesting one, so let me show you the version that does not." Then
open a membership-set implementation you prepared off camera, run the harness
against it, and let the assertion fail on screen. Frame it honestly as an
alternative implementation rather than as something the model just produced.

Either way, name the pattern: this is the same preservation constraint from
Exercise 5, on a different axis. There it protected stored data during a refactor,
here it protects the answer during an optimisation. Both prompts asked for an
improvement, and only one said what the improvement was not allowed to cost.

Step 10, record the comparison, then make the point about the ratio: turning
quadratic work into linear work does not buy a constant speedup, it buys one that
grows with the data. The scaling property is the result worth reporting, not the
specific multiple, which belongs to your machine on the day you ran it.

### Show

1. Browser, the optimisation prompt. Editor, `fast_lookup.py` saved.
2. Notes file, the two predictions written before anything is run.
3. Editor, `compare_lookup.py` typed or pasted, with the assertion visible above
   the speedup line.
4. Terminal, `python compare_lookup.py`. Hold the output.
5. If the assertion fails, hold both totals on screen while you talk.
6. Browser, the preservation constraint re-prompt. Editor, `fast_lookup.py`
   replaced.
7. Terminal, the harness re-run, assertion passing, speedup printed.
8. Notes file, the three numbers and the "totals matched" row.

### Watch out

1. **Check correctness before celebrating the speedup, on camera, in that order.**
   If you read the ratio out before the assertion result, you have modelled exactly
   the behaviour the lab exists to prevent, and no amount of narration afterwards
   fixes it.
2. Do not quote the speedup multiple as a property of the technique. Say "on this
   machine, on this data".
3. Do not skip step 7's prediction because you already know the answer. It is the
   step that converts this from a demo into a method.
4. The wrong total must be read off the screen, not from memory. Do not state a
   figure that is not visible in the frame.
5. Keep both totals in the same frame when the assertion fails. Two numbers side by
   side is the shot; two numbers described is not.
6. If the optimised version imports a package you do not have, that is a usable
   shot. Add "standard library only" to the prompt and move on. The standard
   library is enough here.

## Video 3.9: Exercise 9 Part 1, The Prompt People Actually Send

**Runtime:** 8 minutes
**On screen:** editor, plus browser

### Say

Frame the design at the top, because it is unusually clean and it is worth naming:
the diff does not change between the two rounds. Only the prompt changes. What that
does to the review is the entire exercise.

Step 1, review it yourself first. Three minutes, which is longer than it feels and
about what a real reviewer would spend on a change this size. It touches two files.
Say the thing that decides half the findings: read the lines beginning with a minus
sign as carefully as the ones beginning with a plus, because removed lines are what
both a human reader and a model skim past.

Have them write a numbered list. Say why it has to exist before any prompt: it is
the only unbiased benchmark available, and it cannot be reconstructed afterwards.

Step 2, fresh conversation, and paste the diff with its formatting intact. File
headers, hunk markers, leading plus and minus characters. A diff pasted without
them is just code, and findings will start citing lines that are not changes.

Step 3, Round 1. The prompt is three words. Say: "Review this PR. That is the whole
prompt. No role, no priorities, no output format. Resist the urge to improve it,
because an unimproved prompt is the measurement."

Step 4, score it. Tag every item F for formatting, C for correctness, S for
security, O for other. Then answer four questions in the notes: how many items in
total and how many are F, where the first C or S item appears in the response,
which items from the Step 1 list are missing entirely, and whether the C and S
items name the input that triggers the problem or only say the code is risky.

Do the tagging on camera for the first several items so the format is modelled,
then hand over with a real pause. Say: "Pause here and tag every item and answer
all four questions before you go on. Those numbers are the point of the exercise
and you cannot recover them later."

### Show

1. Editor, `sample_pr.diff`, scrolled top to bottom at reading pace. Pause on the
   removed lines.
2. Notes file, the numbered list built live, five or six items.
3. Browser, a genuinely new conversation. The three-word prompt, then the diff
   pasted with formatting intact.
4. The Round 1 response, scrolled through once.
5. Notes file, items tagged F, C, S or O, and the four answers started.

### Watch out

1. Do not add anything to the Round 1 prompt, not even a polite framing sentence.
   The bare prompt is the control condition.
2. Start a genuinely new conversation. Context from an earlier chat quietly shapes
   the review and you will attribute the result to the prompt you can see.
3. Do not narrate what Round 1 "should" find. Read what it did find. The lab
   deliberately does not promise Round 1 will fail, and a published video cannot
   guarantee a model's behaviour.
4. If Round 1 finds the serious items on your take, keep the take. Say: "This run
   raised it. Note where it appeared in the list and in what tone, because the
   comparison in the next video is about ordering and prominence as much as about
   presence." That is the honest and more interesting outcome.
5. Do not complete your own Step 1 list off camera and paste it in. Building it
   live is what makes the benchmark credible.
6. Sidebar and model picker out of frame for every browser shot.

## Video 3.10: Exercise 9 Part 2, Same Diff, Different Review

**Runtime:** 7 minutes
**On screen:** browser, plus notes

### Say

Open by putting Round 1's numbers back on screen, because this is a separate video
and the comparison is the entire lab. Read the totals out: how many items, how many
tagged F, and where the first correctness or security item appeared.

Step 5, Round 2, in a new conversation, with the same diff unchanged. Read the
prompt out and, more importantly, name the three things that changed and what each
one does:

1. A role and a stake. Senior backend reviewer, going to production,
   customer-facing, backed by a SQL database. This sets what counts as serious.
   Without it, everything in the diff is equally interesting.
2. An exclusion instruction. Naming the categories to leave out is what stops the
   style flood. Say the part people get wrong: "Asking for important issues does
   not work, because style issues are real issues. They are just not the ones you
   asked for. You have to name them and exclude them."
3. A severity contract with a definition, plus a per-finding format. Defining must
   fix by consequence rather than leaving it to interpretation is what makes the
   groups mean the same thing to both parties, and requiring a quoted line plus a
   triggering input is what turns a finding into something actionable. It also
   quietly suppresses findings that cannot be grounded in the diff.

Step 6, score Round 2 the same way and fill the comparison table: total items,
tagged F, must fix items, items from the Step 1 list that were found, and items
with a stated triggering input.

Then the question that produces the best result in the lab: for each must fix item
in Round 2, did Round 1 raise it at all, and if so, where and how was it worded?
Say: "An item can be present in Round 1 and still be missed, because it was the
ninth bullet in a list of fourteen, in the same tone of voice as a comment about
import order. Being mentioned is not the same as being surfaced."

Step 7, verify every must fix against the diff yourself. Four checks: is the quoted
line genuinely in the diff, can you state the triggering input in your own words,
is it blocking or is it a good idea for next week, and is it specific enough that
the author would know what to change. Demonstrate one verification on camera by
jumping to the quoted line.

Step 8, decide on every item. Accept, reject, or needs more information, with a
one-line reason. Say that rejecting with a reason is a review outcome, and that a
reviewer who accepts every generated suggestion has not reviewed anything, they
have relayed it, and the accountability for the merge still sits with them.

Step 9, one follow-up per accepted item: the minimal fix, and the test that would
have caught it before the PR was opened. The second half is the valuable half,
because the comment fixes this pull request and the test fixes the next one.

Step 10, write the review notes and save them.

Close on the takeaway, in the direction that stings: "Round 1 was not a bad review
because the tool is weak. It was a bad review because the request was empty, and an
empty request gets answered by covering everything at equal weight, which is
indistinguishable from covering nothing. Severity, scope and exclusions are your
job to supply. Nothing else in the exchange can supply them."

### Show

1. Notes file, Round 1's tallies, as the opening frame.
2. Browser, new conversation, the Round 2 prompt, then the same diff pasted
   unchanged.
3. The Round 2 response, grouped, scrolled once.
4. Notes file, the comparison table filled with real numbers from both rounds.
5. Editor and browser side by side for one must fix verification against a quoted
   line.
6. Notes file, accept, reject and needs more information decisions, with at least
   one reject and its reason.
7. Browser, one minimal fix and test follow-up.
8. Editor, `review-notes.md` saved with its three sections.

### Watch out

1. Both rounds must be in separate conversations, visibly. If Round 2 runs in
   Round 1's conversation, the comparison is worthless and a learner following
   along will get a different result and blame themselves.
2. Do not paste an edited diff into Round 2. Same bytes, both rounds. Say so on
   camera.
3. Do not read your comparison numbers as though they were the expected numbers.
   Say "these are my numbers from this run, and yours will differ".
4. Reject at least one item on camera, with a reason. If everything in Round 2
   genuinely holds up, reject on scope instead: a finding that is true and about
   code this pull request did not touch is a ticket rather than a review comment.
5. Do not name the security finding as the one Round 1 was supposed to bury before
   you have scored both rounds. Let the comparison table produce it.
6. This is the last video of the module. Keep the close to the takeaway. Do not
   preview Module 4's contents in detail beyond noting that it is the first module
   needing an API key, which learners should arrange now if they have not.

## The teaching points that carry this module

1. The number of failures and the number of problems are different numbers, and
   debugging is a sequence of small corrections each verified, not one fix applied
   at the end.
2. A test suite is a specification, and when the failing line does not determine
   the fix, the assertions do.
3. Nested loops grow quadratically, not exponentially, and saying the wrong word in
   a review costs you the argument you were trying to win.
4. Correctness is checked before the clock, because a faster wrong answer is worse
   than slow code: slow code announces itself and a wrong total does not.
5. Severity, scope and exclusions are the reviewer's job to supply, and an empty
   request gets everything at equal weight, which is indistinguishable from
   covering nothing.

## Questions learners will ask, and the answers

| Question | Answer |
|---|---|
| Do I need Claude Code for this module? | No. You need a terminal and pytest. Prompting happens in a browser conversation. Claude Code was Module 2 and the API key requirement starts in Module 4. |
| My pytest run shows a different number of failures from the video. | Delete `.pytest_cache` and `__pycache__` in the starter folder, or run with the cache provider disabled, then run again from inside `starter/`. |
| `ModuleNotFoundError` when running the tests. | pytest was run from the repository root. Change into the `starter/` folder and run it there. |
| Can I edit the test file to make it pass? | No. The test file is the only specification you have in that exercise. Editing it deletes the specification. |
| I picked a different default value and the tests still pass. | Expected. The tests allow a range rather than a single value, which is the point of that step. You should be able to name which test sets each bound. |
| Is a nested loop exponential or quadratic? | Quadratic. Work grows with the square of the input, so ten times the data is a hundred times the work. Exponential means something quite different and is the wrong word here. |
| My optimised version is much faster but returns a different total. | Then it is faster and wrong. Read the original docstring again, note that duplicates count each time, and re-prompt with a preservation constraint requiring an identical total for identical input. |
| My baseline runs in half a second. | Raise `n` in `build_data` and keep the seed unchanged, then re-run and confirm the match count is the same as before you changed it. |
| My timings move around between runs. | Run three times and take the middle value. One timing is an anecdote. |
| Round 1 of the review already found everything. Did I do it wrong? | No. Record it honestly and compare ordering, prominence and wording instead of counts. An item buried ninth in a list of fourteen was mentioned, not surfaced. |
| A finding quotes a line that is not in the diff. | Discard it and re-paste the diff exactly as it is on disk, including the file headers and hunk markers. A finding you cannot anchor is not a finding. |
| Should I accept every must fix item? | No. Accept, reject or ask for more information, each with a one-line reason. A reviewer who accepts everything has relayed a review rather than performed one. |

## Pre-record checklist for this module

1. Confirm the deck is the `- REVISED` file. Check slide 13 reads "quadratically"
   and not "exponentially", and that slide 23 asks for a verdict in words rather
   than an emoji.
2. Terminal and editor settings identical to Module 2: same font, same window size,
   same theme, same minimal prompt. Fresh shell, no history to scroll into.
3. Notifications off. Browser on the recording profile, sidebar clean, model picker
   framed out.
4. Editor sidebar has the course repository only, all other tabs closed.
5. Restore the Exercise 6 test suite to the state a learner leaves it in, green
   with an expected-to-fail test, so the video 3.1 cold open is honest.
6. Delete `.pytest_cache` and `__pycache__` from
   `module-3-debugging/03-labs/exercise-07-debug-buggy-sample/starter/` and from
   the Exercise 6 starter folder.
7. Confirm `git status` is clean in the Exercise 7 starter folder, so the `git
   diff` shot at the end of video 3.6 shows only your on-camera change.
8. Prepare, off camera, a membership-set implementation of `count_matches` as the
   fallback for video 3.8 in case your take's optimisation returns the correct
   total. Keep it out of the recording folder until you need it.
9. Open `sample_pr.diff` and confirm it copies with its headers, hunk markers and
   leading plus and minus characters intact by pasting once into a scratch
   conversation you then delete.
10. **Verification run one.** From
    `module-3-debugging/03-labs/exercise-07-debug-buggy-sample/starter/`, run
    `python -m pytest -q`. **Expected: 3 failed.** Two of one exception type and
    one assertion reporting 2 where 3 was expected. If you see one failure or two,
    stop. The artefact has changed and the video 3.5 narration is wrong.
11. **Verification run two.** From
    `module-3-debugging/03-labs/exercise-08-slow-implementation/starter/`, run
    `python slow_lookup.py`. **Expected: `matches: 24326`, elapsed roughly 2 to 3
    seconds.** The count must be exact, because the correctness trap in videos 3.7
    and 3.8 depends on it. If the elapsed time is far outside that band, retune `n`
    off camera, keep the seed unchanged, re-run, and confirm the count is still
    24326 before you record anything.
