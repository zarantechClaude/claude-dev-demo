# Module 1 Recording Script
## Fundamentals of Claude for Developers

> **Trainer only. Do not publish, do not attach to a learner handout, and do not
> paste any section of this file into a slide.** It names planted defects and
> their answers. If a learner has read this file, three of the fifteen exercises
> in the programme stop working.

**Total runtime:** 74 minutes across 8 videos
**You need before you start:**

1. A fresh browser profile, signed in to a clean account or a dedicated project
   with nothing else in it. See `docs/recording-hygiene.md` section 2.
2. The revised deck open in presenter view:
   `module-1-fundamentals/01-deck/revised/Module 1 - Fundamentals of Claude for Developers - REVISED.pptx`
3. Two starter files open in a plain text editor, not a rendered file view:
   `03-labs/exercise-01-explore-interface/starter/running_average.py` and
   `03-labs/exercise-03-review-checklist/starter/order_sync.py`
4. A notes file on screen, large font, the one you will type learner-visible notes into.
5. Desktop and application notifications off at the operating system level.
6. **No terminal.** Module 1 is browser only, by design. If a terminal window
   appears in any Module 1 frame, restart the take. A learner who sees a terminal
   in this module concludes they cannot start until their install is finished,
   which is exactly the barrier this module was built to remove.

The chosen split: the 35-minute deck runs as four lectures of 9, 9, 9 and 8
minutes, broken at the four content boundaries in the deck rather than at even
slide counts. Exercises 1 and 2 are 12 minutes each and record as one video each.
Exercise 3 is 15 minutes, over the cap, so it splits 8 and 7 at the natural seam
between the learner's own checklist pass and Claude's.

## Video breakdown

| Video | Covers | Slides | Runtime |
|---|---|---|---|
| 1.1 | What Claude is, where developers reach it, Claude Code previewed | 1 to 7 | 9 min |
| 1.2 | Repo as context versus repo as workspace, tiers, use cases | 8 to 11 | 9 min |
| 1.3 | Prompt anatomy: instructions, context, examples, constraints | 12 to 19 | 9 min |
| 1.4 | Responsible use, secrets and PII, trust versus verify, reuse | 20 to 27 | 8 min |
| 1.5 | Exercise 1, all seven steps | none | 12 min |
| 1.6 | Exercise 2, all eight steps | none | 12 min |
| 1.7 | Exercise 3 part 1, steps 1 to 3, your own checklist pass | none | 8 min |
| 1.8 | Exercise 3 part 2, steps 4 to 8, reconcile and verdict | none | 7 min |

Deck 35 minutes, labs 39 minutes, 74 total, matching `docs/programme-map.md`.

## Video 1.1: What Claude Is, and Where You Reach It

**Runtime:** 9 minutes
**On screen:** deck

### Say

Open with what this module is not. It is not a tour of a chat window. Say the
outcome in one sentence early, because a recorded learner decides in the first
thirty seconds whether to keep watching: by the end of this module you will be
able to tell a fluent explanation of code from a correct one, and you will have
written evidence of the difference.

On slide 4, read the three exercises and then say the sentence that matters more
than the list: everything in this module happens in a browser. No terminal, no
install, no API key. That step change arrives in Module 2. Say it here because a
learner waiting on a corporate laptop approval can complete all of Module 1 today.

Slides 5 and 6 are the orientation. Keep them brisk. The four access points are
the web application, the API, integrations, and the Agent SDK, and the useful
framing is that they are four different commitments rather than four features:
the browser costs you nothing, the API costs you a key and a code change.

Slide 7 previews Claude Code. Preview is the operative word. Say plainly: "You
are not installing this in Module 1. I am telling you it exists because the next
slide only makes sense if you know there are two different things in play." Point
at the last bullet, the project context file kept in the repo, and say it is the
single most useful habit in the tool and that Module 2 has a whole exercise on it.

### Show

1. Slide 1, title. Say the module name and your name once.
2. Slide 2, disclaimer. One line. Do not read it out in full.
3. Slide 3, agenda. Ten seconds per line at most.
4. Slide 4, the exercise map. Hold this one. It is the navigation slide for the
   whole module in a recorded course.
5. Slides 5, 6, 7.

### Watch out

1. Do not open the browser in this video. It is a deck lecture and the labs are
   where the interface appears. Cutting to a live interface here means the frame
   has to be clean earlier than you planned it to be.
2. Slide 7 tempts an unscripted demo of Claude Code. Resist it. Module 1 is
   browser only and an install shot here contradicts slide 4 two minutes after
   you read it.
3. Do not name a model version anywhere in this video, and do not read a version
   identifier off any screen. Say "the current mid-tier model" or "the most
   capable tier" if you need to refer to one at all.
4. This is the shot most likely to carry a stale deck. Confirm the file name in
   your presenter window ends in `- REVISED` before you record a word.

## Video 1.2: Repo as Context, Repo as Workspace

**Runtime:** 9 minutes
**On screen:** deck, then browser, then deck

### Say

This is the highest-value slide in the module and the one learners most often get
wrong, so give it real airtime. Budget five of the nine minutes to slide 8 alone
and do not apologise for the pace.

Start with the confusion rather than the definition. The sentence to open on:
"There are two completely different things people mean when they say they gave
Claude their repository, and mixing them up is the most common source of wasted
time I see in this programme."

Then the distinction, in this order. Attaching a repository in the Claude app
syncs the file contents of one branch. That is reading material. Claude can read
it, reason across it, answer questions about it, and nothing else. It grants no
commit access, no pull request access, and no commit history. Claude Code is the
thing that operates on a repository: it edits files on disk and runs commands.

Now the concrete example, which is what makes it stick. Say you have attached
this course repository as context, then ask two questions on camera and let the
answers do the teaching:

1. "Summarise what `docs/programme-map.md` says about the dependency chain." This
   works. The file is context.
2. "What changed in the last three commits?" This does not work, and the
   interesting part is why. History is not file contents, and only file contents
   were synced.

Then the third question, the one that costs people an afternoon: "Add a docstring
to `running_average.py` and commit it." You will get a docstring. You will not
get a commit, because nothing in this arrangement can write to disk. Say the
sentence: "It gave me the text. It did not change the file. If I stop reading
here and assume the work is done, I have a change that exists only in a chat
window."

Close the slide with the decision rule, which is the takeaway learners should be
able to repeat: if you need to understand something, you need context. If you
need something changed on disk, you need the workspace.

Slides 9 to 11 then run quickly. Slide 10 is the tier slide. Read the habit, not
the identifiers: pick a tier, use the most capable tier for architecture,
debugging and unfamiliar code, use a faster tier for repetitive well-specified
work, and look the current identifiers up in the documentation rather than
learning them.

### Show

1. Slide 8, on screen for the whole explanation before you cut away.
2. Browser, a conversation with the repository attached as context. Send the
   three prompts above in order. Keep each response on screen only as long as it
   takes to make the point.
3. Back to slide 8 for the decision rule.
4. Slides 9, 10, 11.

### Watch out

1. The model picker is in shot the moment you switch to the browser. Frame the
   window so it is cropped out. It names current versions and it will date this
   video faster than anything else in the module.
2. The sidebar is in shot for the whole browser segment. Conversation titles and
   project names are visible. Check them before the take, not after.
3. Do not open a terminal to prove the commit did not happen. There is no
   terminal in Module 1. The absence of a commit is the point and you can state
   it without showing it.
4. If the repository attachment is slow to sync, do not fill the silence by
   improvising about how the sync works. Pause the take and resume when it is
   ready.
5. Slide 10 is the slide that used to name three model versions. Confirm on
   camera-ready screen that it now reads as tiers. If you see version names, you
   have the original deck open and the whole video needs re-recording.

## Video 1.3: Prompt Anatomy

**Runtime:** 9 minutes
**On screen:** deck

### Say

Slides 12 and 13 set up why structure matters. The line worth landing: a prompt
is not a wish, it is a specification, and the parts of a specification you leave
out get filled in by someone who has never met your codebase.

Slides 14 to 17 are the four parts, one slide each. Give each one the same shape
so the pattern is memorable: what the part is, one weak example, one strong
example. Instructions are one task and one deliverable with an action verb.
Context is the surrounding fact that cannot be inferred, including language and
version. Examples pin down the boundary you actually care about, and one
well-chosen pair usually beats three vague ones. Constraints state what must not
happen.

Then say the thing the slides do not: constraints are the part developers leave
out most often and usually the part that changes the output most. Flag that
Exercise 2 makes them measure this rather than take your word for it, and that
their own measured result is the version they will remember.

Slides 18 and 19 are the failure modes. Keep them concrete. Vague instruction,
missing constraint, missing context, and four questions in one message. On slide
19, the useful test is one sentence long: cut any sentence from your prompt that
would not change the answer if it were deleted.

### Show

1. Slides 12 and 13, quickly.
2. Slides 14, 15, 16, 17, at an even pace. Roughly one minute each.
3. Slides 18 and 19.

### Watch out

1. Four consecutive similarly shaped slides is where recorded narration goes
   flat. Change your pace deliberately on slide 17, because constraints are the
   one you want remembered.
2. Do not demo prompts here. Exercise 2 is the demo and doing it twice wastes
   four minutes of runtime you do not have.
3. Avoid inventing a fifth part. The lab's optional extra heading is output
   format, and it belongs in the lab's Going further step, not in this lecture.

## Video 1.4: Responsible Use, Secrets, and Verify

**Runtime:** 8 minutes
**On screen:** deck, brief cut to editor on slide 21

### Say

Slide 21, handling secrets and PII, must not be cut and must not be rushed. It is
the block in this module with a consequence outside the course. Budget two and a
half of the eight minutes to it.

Make it specific rather than a policy reading. Four things never go into a prompt:
keys and tokens, database passwords, customer records including email addresses
and postal addresses, and production data dumps. Then the part people miss: your
colleagues' real email addresses count as personal data, and a log line pasted
for debugging is the most common way personal data leaves a team, because nobody
thinks of a log as data.

Then cut to `order_sync.py` for fifteen seconds and use it as the worked example
without spoiling Exercise 3. Point at the credential line and the logging line
and say only this: "There are two things on this screen that should never leave a
machine. One is a credential and one is a customer address in a log line. That
file is Exercise 3, so I am not going to tell you what else is in it."

Slides 20, 22 and 23 carry the verification habit. On slide 22 give them the
sentence that connects back to Exercise 1: fluent prose is not evidence, and the
only thing that settles an explanation is a count you did yourself. On slide 23,
the operative standard is that AI output gets reviewed with the same scrutiny as
a colleague's pull request, no more and no less.

Slides 24 and 25 are the reuse slides. Close by pointing forward: the four-part
template they save in Exercise 2 is used again in Exercises 4, 5, 7 and 13, and
the marked checklist from Exercise 3 is used again in Exercise 9. This module is
where the programme's reusable artefacts get created.

Slide 26, key takeaways. Then slide 27 and stop. Do not add a farewell that names
the next module's contents in detail, because module order can change.

### Show

1. Slide 20.
2. Slide 21, held. Cut to the editor showing `order_sync.py` lines 10 to 25,
   fifteen seconds, then straight back to slide 21.
3. Slides 22, 23, 24, 25, 26, 27.

### Watch out

1. `order_sync.py` contains a deliberately fake credential using an obvious
   example marker. **Do not read the characters aloud.** Say "a hardcoded
   credential" and move on. Reading a key-shaped string aloud on camera is a
   habit you do not want to build, and a viewer cannot tell your fake one from a
   real one by ear.
2. Do not scroll further down `order_sync.py` than the two lines you need.
   Everything below is Exercise 3 and this shot gives away findings if you linger.
3. Do not cut slide 21 for time. If you are running long, take the thirty seconds
   out of slide 24 instead. Slides 24 and 25 are recoverable in the lab
   narration. Slide 21 is not.
4. Do not turn slide 20's compliance bullet into advice about your own
   organisation's policy. Say that the policy is theirs to check and leave it.

## Video 1.5: Exercise 1, Explain and Then Verify

**Runtime:** 12 minutes
**On screen:** browser, plus editor for the starter file

### Say

Frame the exercise before the first prompt: this looks like an interface tour and
it is not. The tour is the first two minutes. The exercise is Step 5, where they
count returned values instead of trusting fluent prose.

Steps 1 and 2 are orientation. Prompt box, response area, sidebar, settings. Send
the open-ended developer question and observe the shape of the answer: it replies
as a conversational assistant because a question was asked rather than code being
requested.

Step 3 is the step to defend on camera. They read and hand-trace the function
before prompting. Say why in one sentence: "If you read the explanation first, you
can only judge whether it sounds right, not whether it is right." Also say
explicitly that they are not running the file, because there is no terminal in
this module, and that hand-tracing is the skill the exercise is actually about.

Step 4, paste the function and ask for a plain explanation. Read the answer and
name the four things to look for: stated purpose, described inputs, described
return value, and the step by step logic.

**Step 5 is the block that must never be cut.** This is the verification beat and
the whole module points at it. Send the follow-up that asks for every returned
value for the input `[10, 20, 30, 40]`, which readings each one averages, and how
many values come back for n readings. Then count on camera. Out loud. Four
readings went in. Count what came back.

Now handle both outcomes, because the model's behaviour varies between runs and a
published video cannot promise either one.

**If the Step 4 explanation missed it**, say this: "Read that explanation again
with the counts in front of you. It described what this function was meant to do.
The code does something else, and no amount of re-reading the prose would have
told me that. The two numbers told me."

**If Claude caught the defect in Step 4**, do not pretend otherwise and do not
re-roll the take. Say this: "It caught it. Notice why it could: this function is
nineteen lines long and I gave it all of them, so nothing was missing. Now ask
yourself what happens when the function is one of four thousand files, the
relevant caller is in a different module, and I paste forty lines out of the
middle. The verification step is not there because the tool is unreliable. It is
there because the conditions that made this easy almost never hold at work."

Either way, land the same closing sentence: the count is the evidence, and
evidence is what makes a review comment stick.

Step 6 runs the three prompt variations, each in a fresh conversation. Same code,
three noticeably different answers, and the useful question is which of the three
would have reached the Step 5 finding fastest. Step 7 is thirty seconds and must
not be cut: they write one use case from their own work, because that note becomes
their capstone subject in Module 5.

### Show

1. Browser, signed in, sidebar visible and clean. Point at the four areas.
2. The open-ended prompt and its reply.
3. Editor, `running_average.py`, the function only. Trace the loop with the
   cursor while you talk.
4. New conversation. Paste the function from `def` to the end of file. Send the
   plain explanation prompt.
5. Same conversation, the counting follow-up. Then count on screen, in your notes
   file, in two lines: readings in, values back.
6. Three new conversations, one per variation, kept short.
7. Your notes file, one line for the use case.

### Watch out

1. Paste from a plain text view. Copying from a rendered file view loses the
   indentation and you will lose a take to a syntax complaint.
2. Do not paste the `TEACHING ARTEFACT` header block. It names the defect
   register and points a curious learner at the answers. Paste from `def`
   onwards, exactly as the lab tells the learner to.
3. Do not say "the bug" before Step 5. The whole design of this exercise is that
   the learner finds it by counting. If you announce it in Step 3 the exercise is
   over.
4. Do not fix the file on camera, and do not say what the corrected loop bound
   should be. It is a teaching artefact and the same file is referenced later.
5. New conversation for each Step 6 variation, visibly. If earlier context
   carries over, the three answers converge and the point disappears.
6. Model picker cropped out of frame for every browser shot in this video.
7. Twelve minutes is the cap, not a target. If your first take runs to thirteen,
   cut time from Step 1 and Step 6, never from Step 5.

## Video 1.6: Exercise 2, Structure a Developer Prompt

**Runtime:** 12 minutes
**On screen:** browser, plus a scratch file

### Say

Set the shape up front: they will send a deliberately bad prompt, rebuild it in
four labelled parts, and then prove which part carried the weight by deleting one
part at a time.

Step 1, send `write a function to validate email` and nothing else. Say clearly:
"Do not improve this. The weak version is the measurement. If you skip it you have
nothing to compare against and this exercise becomes a lecture."

Step 2 is the step with the teaching in it. List what the model had to guess
because it was not told: language and version, whether third-party libraries are
allowed, what counts as a valid address, the return type, the behaviour on invalid
input, and where the function is called from. Say the sentence: "That list is the
specification I failed to give. Every item on it got decided by someone who has
never seen my code."

Steps 3 and 4 build the four parts. Keep instruction and context visibly
separate, and say why: when the output is wrong, labelled sections tell you which
part to fix. A blurred paragraph does not.

Step 5, assemble and send. Step 6, put the two outputs side by side and answer
three questions on camera: which one needs fewer edits, which guesses from the
Step 2 list disappeared, and which single addition changed the output most.

On the third question, be careful with your wording, because you are recording a
prediction about a model's behaviour. Say: "In most runs I have done, the answer
is the constraints or the example rather than the added context. Check your own
run. If yours differs, yours is the result that counts, because you measured it."

Step 7 is the ablation and it is worth the time: send the structured prompt with
constraints removed, then with constraints restored and the example removed. Note
what degrades and by how much. Say why this beats being told: "You now have a
measured result rather than a rule you were given, and measured results survive
contact with your own work."

Step 8 is the scrub and the save. Do the scrub on camera, deliberately. Check for
keys, tokens, internal hostnames, customer data and real names, then save the
four-part template. Tell them where it gets used again: Exercises 4, 5, 7 and 13.

### Show

1. Browser, new conversation, the three-word prompt and its output.
2. Scratch file, the list of guesses typed live. Six lines, no more.
3. Scratch file, the four labelled parts assembled.
4. Browser, the structured prompt sent, output read.
5. Two outputs side by side, either split screen or a scroll between them.
6. Two ablation runs in fresh conversations.
7. Scratch file, the saved template with placeholders.

### Watch out

1. Use `user@example.com` style placeholders throughout. Do not type a real
   address, including your own or a colleague's, even as an example of an invalid
   one.
2. Do not tidy the weak prompt. Lowercase, no punctuation, exactly as written.
3. The ablation runs need fresh conversations. Reusing one carries the deleted
   constraint in context and the ablation shows nothing.
4. Do not promise a specific outcome from the ablation on camera. Report what
   your run did and tell them to record theirs.
5. Keep the assembled prompt short enough to fit one screen at recording font
   size. If it needs scrolling, the shot stops working.

## Video 1.7: Exercise 3 Part 1, Your Own Review Pass

**Runtime:** 8 minutes
**On screen:** editor, plus a notes file

### Say

Open by saying what the file is and what it is not. It is code a colleague
generated from a vague prompt and sent for review. It runs, it is short, and it
reads cleanly, and that is exactly what makes it worth reviewing properly rather
than skimming.

Step 1, read it end to end and answer three questions before evaluating anything:
what does it do, what does it expect, what does it change.

Step 2 is the step that is easy to skip and changes half the answers. Read the
intended use table out: a nightly internal admin job, about 5,000 email addresses
per run, a local database, an internal HTTP API, running on a shared build server
whose logs ship to a central log tool. Say the sentence: "Two of those facts
change specific marks later. The volume figure decides the performance rows, and
the log destination decides one of the security rows. You cannot review code
without knowing where it sits."

Step 3 is the longest step in the exercise and the one to protect. Walk the three
sections, quality, security and performance, and explain the evidence rule
carefully, because it is the transferable part: every verdict needs a line number
or a named construct, and if you cannot name evidence the verdict is Needs review,
not Fail.

Then hand it over with a real pause. Say: "Pause here and mark every row
yourself, with evidence, before you watch me ask Claude. If you watch my prompt
first you will mark the checklist against its findings instead of against the
file, and you will not notice you have done it."

Mark two or three rows on camera to model the format, not fifteen. Choose rows
where the evidence is unambiguous and which are not the headline findings.

### Show

1. Editor, `order_sync.py`, scroll from top to bottom once at reading pace.
2. Notes file, the three answers.
3. Notes file, the intended use table.
4. The three checklist sections.
5. Two or three rows marked live, with a line number typed into the evidence
   column each time.

### Watch out

1. Do not mark the security section on camera. That is where the headline
   findings are and modelling the format there hands the learner the answers.
2. Do not read the credential string aloud. Say "a hardcoded credential on line
   14" if you need to reference it, and only if you are not marking that row.
3. Do not count the defects on camera or say how many there are. A stated total
   turns the exercise into a scavenger hunt with a known end point.
4. Line numbers must match the file on screen at the learner's font size, so set
   the editor to show line numbers before the take.
5. This video ends on a pause instruction. Deliver it as a full stop, not as a
   trailing thought, because it is the moment the learner is meant to leave the
   video and do the work.

## Video 1.8: Exercise 3 Part 2, Reconcile and Decide

**Runtime:** 7 minutes
**On screen:** browser, plus the notes file

### Say

Open with a one-line recap, because this is a separate video and a learner may
arrive here a day later: "You have a marked checklist with evidence in every row.
Now we compare it against Claude's."

Step 4, run the review prompt with the checklist and the code. Read the
instruction's two important features out loud: one row per checklist item with a
line number, and "do not rewrite the code, review only", because an open request
returns a rewritten file instead of a review.

Step 5 is the teaching centre of the exercise. Three categories: items Claude
flagged that they missed, items they flagged that Claude did not, and items where
the cited line number or construct does not match the file. Spend your time on
the third category. Say the sentence: "A finding you cannot anchor to a line in
front of you is not a finding, however plausible it sounds. That is the same
failure you met in Exercise 1, appearing in a review instead of an explanation."

Demonstrate one anchoring check on camera. Take a cited line number, jump to that
line in the editor, and confirm or discard it out loud.

Step 6, ask for the top three fixes by risk reduction for effort, and then
disagree with part of the order on camera if you honestly do. Say that the
ranking is a judgement about their system rather than a fact about the file.

Step 7 is the verdict. Read the two rules exactly: any Fail in the security
section rules out "ready for production", and any Fail that could expose
credentials or personal data, or that lets untrusted input reach a query, leaves
only "draft only". Then give the finding the register wants surfaced, without
listing the defects: "If you marked this ready after minor edits, go back and
check two things specifically, credentials in source and how the queries are
built. Marking this file nearly ready is the most common real-world failure of
AI-assisted review, and it happens because the code reads well."

Step 8, save the marked checklist. It is reused in Exercise 9.

### Show

1. Browser, new conversation, the review prompt with the checklist and the code.
2. The returned table, scrolled once.
3. Editor and browser side by side for one anchoring check on a cited line number.
4. Notes file, the three reconciliation categories with at least one item in each.
5. The ranking prompt and its answer.
6. Notes file, the verdict plus the two or three items that drove it.

### Watch out

1. Your verdict on camera is "draft only, not production ready". Do not soften
   it, and do not present it as one defensible view among several, because the two
   rules in Step 7 decide it.
2. Do not enumerate every defect while reconciling. Show the method on two or
   three items and let the learner's own list carry the rest.
3. If Claude's review this take is unusually thorough and finds nearly
   everything, do not re-roll. Say: "This run was strong. Verify it anyway, and
   notice that verifying took me ninety seconds. That is the cost of the habit,
   and it is cheap."
4. If Claude returns a rewritten file instead of a review, that is a usable shot
   rather than a ruined take. Show it, name the cause, and re-ask with "review
   only, one row per item, no code".
5. Do not open the account menu at any point in this video. Email address and
   plan badge.

## The teaching points that carry this module

1. Attaching a repository gives Claude reading material, while Claude Code gives
   it a workspace, and the whole programme depends on the learner keeping those
   two apart.
2. A fluent explanation is not evidence, and the cheapest way to settle one is to
   count something yourself against the input you gave it.
3. A prompt is a specification, and every part you leave out gets decided by
   something that has never seen your codebase.
4. Credentials and personal data must never enter a prompt, and log lines are the
   most common way personal data leaves a team.
5. A review finding that cannot be anchored to a line in the file is not a
   finding, no matter how serious it sounds.

## Questions learners will ask, and the answers

| Question | Answer |
|---|---|
| Do I need to install anything for this module? | No. Module 1 is browser only. A terminal and Claude Code are needed from Module 2, and an API key from Module 4. Set those up while you work through this module. |
| I attached my repository, so why can Claude not commit my change? | Because attaching syncs file contents as reading material. It grants no commit access, no pull request access and no commit history. Claude Code is the tool that operates on files on disk. |
| Which model should I pick? | Pick a tier, not a version. Use the most capable tier for architecture, debugging and unfamiliar code, and a faster tier for repetitive well-specified work. Look up current identifiers in the official documentation rather than memorising them. |
| My answer is different from the one in the video. Did I do it wrong? | Probably not. Responses vary between runs and small wording changes matter. Compare findings and evidence rather than phrasing. |
| Claude rewrote my code when I asked for an explanation. | An open request invites improvement. Add "Explain only. Do not rewrite the code." |
| Is it safe to paste my employer's code into a prompt? | That is a question about your organisation's policy, not about the tool, and you should check it before you paste anything. Independently of policy, never paste credentials, tokens, customer records or production data. |
| Exercise 1 asks me to trace the loop by hand. Can I just run the file? | You can, later. The exercise is deliberately hand-traced because the skill being built is reading code closely enough to disagree with a confident explanation of it. |
| Why does Exercise 3 give me the checklist instead of having me write one? | Because authoring a checklist consumes the time that should go into applying one. Extending it for your own stack is the optional Going further step. |
| Where does the use case in Exercise 1 Step 7 get used? | It becomes your capstone subject in Module 5. Keep the note. |

## Pre-record checklist for this module

1. Confirm the deck open in presenter view is the file whose name ends
   `- REVISED`. Check slide 8 exists and is titled "Repo as Context, Repo as
   Workspace", and that slide 10 names tiers rather than model versions.
2. Fresh browser profile, signed in to a clean account or a dedicated project.
   Sidebar, tab strip and bookmarks bar empty of anything you would not publish.
3. Give the recording conversations deliberate titles. They are visible in the
   sidebar in every browser shot in videos 1.2, 1.5, 1.6 and 1.8.
4. Frame the browser window so the model picker is out of shot. Do not open it in
   this module at all.
5. Notifications off at the operating system level.
6. Editor open with exactly two files, `running_average.py` and `order_sync.py`,
   and no other folder or workspace in the sidebar. Line numbers on. Font large
   enough to read on a phone.
7. Close every terminal window and remove any terminal from your dock or taskbar
   overlay. Module 1 must not show one.
8. Attach the course repository to the recording project so the video 1.2 context
   demo works, and confirm the sync has finished before you record.
9. Open `running_average.py` in a plain text view, ready to copy from `def`
   onwards. Confirm the copy preserves indentation by pasting once into a scratch
   conversation you then delete.
10. Verify the Exercise 1 arithmetic yourself so you can count out loud without
    hesitating: the sample input has four readings, and the returned list has
    three values. Do that check on the file you are about to record with, not from
    memory of this line.
11. Run through the video 1.2 three-prompt sequence once off camera. If the
    history question happens to be answered from a commit message that appears in
    a synced file, adjust your wording before the take rather than during it.
