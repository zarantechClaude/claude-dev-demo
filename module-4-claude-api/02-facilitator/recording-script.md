# Module 4 Recording Script
## Building with the Claude API (Backend and Integration)

> **Trainer only. Do not publish this file to learners and do not paste any part of it
> into a lab, a slide or a video description.** It names planted defects, spoilers and
> known material problems on purpose. The learner-facing documents are the five lab
> files and `docs/capstone-brief.md`.

Slide numbers in this script refer to the **revised** deck,
`01-deck/revised/Module 4 - Building with the Claude API (Backend & Integration) - REVISED.pptx`,
which has 28 slides against the original's 25. Three slides were inserted, so every
number after slide 3 has moved. Do not cross-reference the original deck or the
changelog's "Changed" numbers while recording.

**Total runtime:** 87 minutes across 11 videos
**You need before you start:**

1. A throwaway API key with a low spend cap, and its revocation date already in your
   calendar. This is the first module where a key is on screen.
2. `.env` in the Exercise 10 starter folder holding `ANTHROPIC_API_KEY` and `MODEL`,
   with the model identifier looked up on your record date.
3. `.gitignore` containing `.env`, created before `.env` existed.
4. A fresh shell, a fresh browser profile, notifications off at operating system
   level, and the editor sidebar showing this repository only.
5. Python 3.11 or later with `anthropic` and `python-dotenv` installed in an active
   virtual environment.
6. `docs/capstone-brief.md` open in a second tab. Video 4.11 is built on it.
7. The whole of `docs/recording-hygiene.md` read once. Section 1 is this module.

## Video breakdown

| Video | Covers | Slides | Runtime |
|---|---|---|---|
| 4.1 | Module opening, the key check, what the API actually is, authentication headers | 1 to 6 | 7 min |
| 4.2 | Tier selection, request parameters, environment configuration, request and response flow | 7 to 10 | 6 min |
| 4.3 | Prompt engineering in code, system versus user, shaping the response, templates, dynamic variables | 11 to 15 | 7 min |
| 4.4 | Tokens and truncation, long context, context management, conversation state, passing code | 16 to 21 | 6 min |
| 4.5 | Prompt caching, and MCP as context rather than as a task | 22 to 24 | 4 min |
| 4.6 | Exercise 10, configure the key and make the first call | none, terminal | 12 min |
| 4.7 | Exercise 11 Part 1, build the CLI and the two templates | none, editor | 11 min |
| 4.8 | Exercise 11 Part 2, attack it, then compare against the reference | none, terminal | 11 min |
| 4.9 | Exercise 12 Part 1, statelessness, crude multi-turn, the naive window | none, editor | 9 min |
| 4.10 | Exercise 12 Part 2, why recency failed, relevance rules, assembly | none, editor | 9 min |
| 4.11 | Module close and the capstone brief handover | 25 to 28 | 5 min |

The split: the 35 deck minutes are spread across six videos rather than four, because
prompt caching and the prefill slide are both new teaching and both get their own
segment instead of a bullet. Videos 4.1 to 4.5 carry slides 1 to 24 in 30 minutes, and
video 4.11 carries the remaining four slides plus the capstone handover in 5, which
keeps the deck budget at 35 and puts the brief at the end of the module where the
programme map requires it. Exercise 11's 22 minutes split at the Part 1 and Part 2
boundary the lab already marks. Exercise 12's 18 minutes split at the end of Step 5,
which is where the learner has found the loss but not yet been told what caused it,
so the second video can open by naming it.

---

## Video 4.1: The key check, and what the API actually is

**Runtime:** 7 minutes
**On screen:** deck, then terminal

### Say

Open by stating the step change. Modules 2 and 3 needed a terminal. This module needs
a credential, and a credential is the one prerequisite a learner cannot resolve in
thirty seconds, so anyone who has not got one should pause and sort it out now.

Then go straight to the gate. Say plainly that you are going to prove a key is loaded
before you teach anything, because a module where every example needs a working key is
a module where a broken `.env` wastes the next hour. Run `verify_key.py`. While the
output is up, say the sentence that matters: **"It reports that the key loaded and how
long it is. It does not print the key, and it does not print the first few characters
either, because a truncated key in a screenshot or a log aggregator is still a leaked
prefix."** That is the whole habit you are teaching, and it lands in one shot.

On slide 5, correct the vendor fact directly rather than quietly. There is one messages
endpoint. The model is a field in the request body, not part of the URL. Say the
diagnostic version out loud: if you find yourself building a URL per model, something
has gone wrong, and the symptom is a 404 rather than an authentication error.

On slide 6, do the headers once and only once. The key goes in an `x-api-key` header. A
raw HTTP call also needs an `anthropic-version` header, and leaving it out fails in a
way that has nothing to do with your key. An `Authorization` header is also accepted,
which is why you will see it in other people's integrations, and that is exactly why
`x-api-key` is worth naming as the documented primary. Close the point by saying you
will not write raw HTTP again in this programme, and that the reason to look at it once
is so a 401 at two in the morning is a five-minute problem.

### Show

1. Slide 3, agenda, briefly.
2. Slide 4, the section map. Read the three exercise durations off it and the line about
   needing a key with credit.
3. Cut to the terminal. `python verify_key.py`. Let the full output sit on screen.
4. Back to slide 5, then slide 6.

### Watch out

1. Do not open `.env` in this video. It is opened once, in video 4.6, deliberately.
2. Do not run `echo $ANTHROPIC_API_KEY`, `env`, `printenv` or `cat .env`, not even to
   recover from a mistake. If you do it in a take, kill the take.
3. `verify_key.py` makes a live call, so it can fail on camera for reasons that are not
   about the key. Run it once off camera immediately before the take.
4. `verify_key.py`'s header comment reads "Module 4, Block 1: run this BEFORE any
   teaching". "Block 1" is language from the abandoned live design. If you scroll the
   file on camera it is visible. Either do not open the file here, or accept it and get
   it corrected before republish.
5. The terminal scrollback from your off-camera rehearsal run is above the visible area.
   Clear the screen, and do not scroll up in frame.

---

## Video 4.2: Tiers, parameters, and configuration

**Runtime:** 6 minutes
**On screen:** deck

### Say

Slide 7 is the model slide and it is the one that dates the course fastest. Teach the
habit, not the catalogue. There is a family of models at different capability tiers.
The most capable tier is for architecture and hard debugging. A faster tier is for
repetitive, well-specified work. The choice you actually make in a real system is a
cost, latency and capability tradeoff, and it is a configuration value rather than a
code value. Then say the durable instruction: **"Look the current identifier up in the
official documentation on the day you need it, and put it in configuration."**

On slide 8, `max_tokens` needs the correction that saves learners the most time. It caps
the output. It is not a request for brevity and it is not the context window. If you
want a short answer, ask for one in the prompt. If you want a hard ceiling, use
`max_tokens`. Confusing the two gives you answers that stop mid-sentence, and the fix
for each is different. Temperature, top-K, top-P and stop sequences get one sentence
each. Nothing in this module's labs tunes them.

Slide 9 is where you name the parallel that the module is really built on: a credential
is configuration and a model identifier is configuration, and they belong outside the
code for the same reason, which is that there has to be one place to change them.

Slide 10, request and response flow, is the shape of every script in the next three
exercises. Point at the five steps and say the learner is about to do exactly these.

### Show

Slides 7, 8, 9, 10 in order. Nothing but the deck.

### Watch out

1. Slide 7 carries the three tier names in its body text. Tier names are not version
   names and they are allowed to be on the slide, but do not attach a number, a date or
   a generation to any of them in narration, and do not say which one you are using.
2. Do not read any model identifier aloud at any point in this video.
3. Slide 7's shapes are laid out as a diagram rather than a bullet list, so the reading
   order on screen is not the order python-pptx reports. Rehearse the eye path once.

---

## Video 4.3: Prompt engineering in code

**Runtime:** 7 minutes
**On screen:** deck

### Say

Slide 11 has the sentence worth pausing on: prompt definitions belong in version control
next to the code that sends them. A prompt tuned by hand in a chat window and never
written down is not an asset, it is a thing somebody once did.

Slide 12 is system versus user. Constraints go in the system prompt. The user message
carries the dynamic input and nothing else. Say the mechanical fact clearly, because it
is the most common porting error from other providers: **the system prompt is a
top-level parameter on the request, not the first entry in the messages list.** It fails
at the API rather than in the editor, so it fails later than it should.

Slide 13 is new. It exists because the module assessment tested this material and the
deck never taught it, so give it real airtime rather than a bullet.

Two things on it. First, messages alternate between the user role and the assistant
role. Two user messages in a row is a common cause of an error message that reads as
though something deep is wrong when the actual problem is the shape of your array. Tell
them the debugging move: print the roles in order before you send, not the content, the
roles. Second, prefill. You are allowed to start the assistant's reply for it, and
whatever you put there constrains the format tightly. The concrete example to give is
an opening brace, which is a reliable way to get JSON and nothing else. Say why that
matters for the capstone: a response you can parse without string repair is worth more
than a response you have to clean up, and the parse is where a service breaks.

Slides 14 and 15 are the template pattern and variable insertion. Keep them short. They
are the deck version of what Exercise 11 builds, and the version the learner remembers
will be the one they typed.

### Show

Slides 11 through 15. Hold on slide 13 for around 2 minutes of the 7.

### Watch out

1. Do not demonstrate prefill in a live call here. There is no terminal in this video,
   and adding one costs you the take. Exercise 11 and the capstone are where it gets
   used.
2. Do not preview Exercise 11's strong template on this slide. The learner is supposed
   to write the weak one first and feel the difference.

---

## Video 4.4: Tokens, long context, and conversation state

**Runtime:** 6 minutes
**On screen:** deck

### Say

Slides 16 and 17 are limits and layout. The one practical line is on 17: crucial
instructions go at the end of a long prompt, and long input gets structure and markers
rather than being pasted as a wall.

Slide 18 is the one that sets up Exercise 12, so land it properly. The API is stateless.
It has no record of your previous call. Multi-turn conversation is not a feature you
switch on, it is a thing you build, and the whole mechanism is that you resend what you
want it to know. Say the cost consequence in the same breath: what you send grows every
turn, and so does what it costs and how long it takes.

Slide 19 is session storage. Slide 20 is passing documents and code, and the line to
pull forward is delimiting tags, because that is the capstone's prompt design mark.

Slide 21 lists the four optimisation strategies including the sliding window. Be careful
here. Present the sliding window as the standard answer, which it is, and do not
undercut it. Exercise 12 is built on the learner implementing it, believing it, and
watching it fail. If you tell them here that it drops constraints, the exercise is dead.
The strongest thing you can say is the last bullet on the slide: constantly evaluate
whether your chosen optimisation degraded the output.

### Show

Slides 16 through 21, six slides, one minute each.

### Watch out

1. Do not spoil Exercise 12. No mention of recency being a poor proxy for importance,
   and no mention of what a three-message window loses. That sentence belongs in video
   4.10 and nowhere earlier.
2. Slide 17 says "massive context windows". Do not quote a number. Numbers here date
   as fast as version names.

---

## Video 4.5: Prompt caching, and MCP in one shot

**Runtime:** 4 minutes
**On screen:** deck

### Say

Slide 22 is new and it is the highest-value thing in the deck for anyone about to do
real integration work, so give it three of the four minutes.

Frame it with the situation rather than the mechanism. You have a service that sends the
same large fixed context on every request, a coding standard, a schema, a long system
prompt, and then one small variable part. Without caching you pay to reprocess the fixed
part every single time. Caching a stable prefix means you are not billed to reprocess
it on each call.

Then the two things people get wrong. Order matters: the stable material goes first and
the variable material goes last, because a prefix is only cacheable if it is genuinely
a prefix. And it is a cost and latency optimisation, not a way to raise a context limit.
It does not give you more room, it makes the room you were already paying for cheaper.
Close with the honest instruction on the slide: check the current caching mechanics in
the documentation before you rely on them, because this is a mechanism that moves.

Slides 23 and 24 are MCP. One minute, and frame it explicitly as context for later work
rather than something the learner is about to do. No lab in this module touches it, and
that is a scope decision rather than an omission. Say that out loud so nobody goes
looking for the missing exercise.

### Show

Slide 22, held. Then 23 and 24 quickly.

### Watch out

1. Do not quote cache pricing, a discount percentage, a minimum token count or a cache
   lifetime. All four are subject to change and all four would date the video and put a
   number on screen we would then own.
2. Do not open a pricing or usage page to illustrate the saving.
3. Do not promise a cost reduction figure. Describe the mechanism.

---

## Video 4.6: Exercise 10, the key and the first call

**Runtime:** 12 minutes
**On screen:** terminal, then editor

### Say

This is the highest-risk video in the programme. Narrate it in the order the lab
specifies, because the order is the teaching point.

Step 3 before step 4, and say why: **"`.gitignore` first, then `.env`. Doing it the other
way round works every time except the time it does not, and a key committed once is a
key you have to rotate, because deleting it in the next commit leaves it in the
history."**

On the `.env` file itself, the variable name is `ANTHROPIC_API_KEY`, exactly that, no
spaces around the equals sign. Say what renaming it breaks: Exercises 11, 12 and 15.
Then the `MODEL` line, and the instruction to look the identifier up in the official
documentation rather than copy one from a tutorial, because a stale identifier produces
an error that reads like an authentication problem.

Run `verify_key.py` again here in the lab context and repeat the presence-and-length
point in one sentence. Repetition is fine. This is the frame that proves the practice.

`minimal_call.py` gets read while the reply prints. Five steps: load the environment,
read two values, fail loudly if either is missing, build a request, print the response
text. Point at the `max_tokens=300` comment and repeat the output-ceiling distinction.

Step 8, the raw `curl` block, is the one look at raw HTTP in the whole programme. Say the
three facts off the command: `x-api-key`, the required `anthropic-version`, and one
endpoint with the model in the body. Then the detail that costs learners minutes:
`python-dotenv` loads `.env` into your Python process, not into your shell, which is why
the `set -a` line is there before the `curl`.

Close on what the deliverable actually is. Not a reply. A reusable configuration and a
habit.

### Show

1. `cd` into the Exercise 10 starter folder. Short path, no home directory in it.
2. Create the virtual environment, activate, install the two packages. Cut the install
   output if you can; it is thirty seconds of nothing.
3. `echo ".env" > .gitignore`, then `cat .gitignore`. That is a safe file to display.
4. Create `.env` in the editor. Type the two variable names. Paste the key value.
5. `python verify_key.py`.
6. `python minimal_call.py`, and open the file while the reply prints.
7. The `set -a` line and the `curl` block, with its short response.

### Watch out

1. The `.env` frame is the single highest-risk frame in the programme. It carries both
   the key and the model identifier. Paste the key, never type it, and move off the file
   as soon as both lines exist.
2. Do not read the model identifier aloud while `.env` is on screen. Say "the identifier
   I looked up this morning".
3. The `curl` response body is short and safe. Confirm off camera that your terminal is
   not configured to echo the expanded command, because `set -x` or a verbose shell
   would put the key in frame.
4. `minimal_call.py` passes the key explicitly with `Anthropic(api_key=API_KEY)`. Do not
   claim on camera that the code relies on the SDK reading the environment by default,
   because the code visibly does not. Say that the SDK will read `ANTHROPIC_API_KEY`
   without being told to, which is why standardising on that name is worth doing, and
   that this script is explicit about it.
5. Twelve minutes is the hard cap and this lab has nine steps. Rehearse it once against
   a clock. If you are over, compress the virtual environment setup, not step 8.
6. Everything in this video is a candidate for a re-record when the API surface changes.
   Keep the source project folder intact after recording.

---

## Video 4.7: Exercise 11 Part 1, build the CLI

**Runtime:** 11 minutes
**On screen:** editor, then terminal

### Say

State the single idea first, in one sentence: never send raw user input straight to the
model as though it were your own instruction.

Then work the lab's order. One positional argument, and resist flags, because the
exercise is about what happens to that string after you receive it.

Write the weak template first and do not apologise for it. It works. Then write the
strong one underneath it, and name the difference precisely, because the difference is
not the tags. The weak version puts the user's text on a line beginning "User request:",
which is the same shape as every other instruction in the prompt, so nothing in it says
where your instructions stop. The strong version marks a boundary with tags **and**
states in the system prompt what that boundary means. Say the summary sentence: **"Tags
with no rule about them are decoration. A rule with no boundary has nothing to point
at. You need both."**

On wiring up the call, repeat the system-prompt-is-a-parameter point. It is the third
constraint in the lab's generation prompt and it is worth reading twice.

Three error paths, not four: empty or whitespace argument, missing configuration, and
the call itself failing. Each one gets a message rather than a stack. Say why a stack
trace is worse than useless: it tells the user nothing they can act on and tells anyone
else more about your service than you meant to publish.

End the video on the lab's pause. All three error paths and one successful call.

### Show

1. The four-file project layout in a folder outside the course repo.
2. `prompt_template.py` with both versions in it, weak above strong.
3. The call function, kept separate. Say that Exercise 15 depends on that separation
   existing.
4. The `__main__` guard with the usage exit.
5. One successful run and one empty-argument run.

### Watch out

1. Copy `.env` across, and write `.gitignore` before you do. If you copy `.env` into a
   fresh folder with no `.gitignore` on camera, you have modelled the exact mistake the
   previous video warned about.
2. Do not open `starter/cli_reference.py` in this video. The comparison in Part 2 is
   worthless if the reference is already on screen.
3. `cli_reference.py`'s header comment says "Module 4, Lab B target state". "Lab B" is
   stale live-design naming for Exercise 11. Do not read it aloud in Part 2 either.
4. Keep the working folder outside the courseware clone, and show that you did.

---

## Video 4.8: Exercise 11 Part 2, attack it and compare it

**Runtime:** 11 minutes
**On screen:** terminal, then editor

### Say

Run the two injection inputs against the strong template. Explain the second one, because
it is the interesting one: the leading closing bracket is an attempt to look like the end
of a structure, so that what follows reads as a top-level instruction rather than as
content. Invite them to substitute their own closing tag and try again.

Then swap back to the weak template, run the same two inputs, and compare four answers.

Now be accurate about what was just demonstrated, and say it in these terms: **"You have
shown that a stated boundary changes the behaviour. You have not shown that it cannot be
crossed."** Structured prompting raises the cost of an injection, which is genuinely
worth having. The defence you actually ship is not trusting the output: bound the input,
constrain the output format, and never let a response reach a privileged action without
a check.

Then open the reference and compare against four specific things: the system prompt
passed as `system=`, `MAX_INPUT_CHARS` truncating the argument, three error paths each
returning an exit code, and the model read from the environment. Say the rule for the
comparison: where the reference does something you did not, decide whether you agree
before you copy it, and where you did something it did not, decide whether it should
have.

Step 8 is the bound on the input, and it has three separate failure modes that fail in
three different places. Cost and latency grow with what you send. A very large input
eventually hits a limit at the model. And long before that, a large body can be rejected
by your web framework or a proxy before your code runs at all. Say the last one twice
and name where they will meet it: as a 413 in Exercise 15.

Close on Step 9, tightening output constraints one at a time. Same code, same model,
different output.

### Watch out

1. A published video cannot promise how a model will behave. Say "watch what changes"
   rather than "the weak version will leak the system prompt". If your take shows the
   strong template failing, that is a usable teaching moment, so keep it and narrate it
   honestly rather than re-recording until you get the result you wanted.
2. Do not put a real injection payload aimed at a real system on screen. The two in the
   lab are deliberately harmless.
3. The exit-code discussion needs `echo $?` in frame. That is safe. `echo` of anything
   else in this module is not.

---

## Video 4.9: Exercise 12 Part 1, statelessness and the naive window

**Runtime:** 9 minutes
**On screen:** editor, then terminal

### Say

Step 1 is two calls with no history between them. Run it and let the second answer fail
on camera. Then name what happened: the API is stateless, it has no record of the
previous call, and everything else in this exercise follows from that.

Step 2 makes it multi-turn the crude way. A list, append both sides, resend the whole
thing. Run Step 1 again and it works. Say the mechanism in one sentence: **"It works for
exactly one reason. You resent everything."** Then say why that is not viable past a few
dozen turns.

Step 3 is the instruction that carries the whole exercise, so deliver it as an
instruction rather than a suggestion. Open `history_starter.py`, read the seven-message
conversation top to bottom, and write down every decision the conversation has committed
to. Not a summary. A list. If a line settles a question about how the system will work,
it goes on the list. Tell them they will need it twice.

Step 4 is the naive window, three lines, and present it as the standard professional
answer to unbounded history, which it is. Run it, show the selected messages, and set the
task: go back to your Step 3 list and mark which of your decisions are still present in
what you are about to send.

Step 5 sends it and reads the answer against the list. End the video on the lab's pause
and its exact framing: does the answer honour every decision on your list, and if not,
which ones did it miss. Then stop. Do not answer it.

### Show

1. The two-call script and its failure.
2. The crude history version working.
3. `history_starter.py`, scrolled to show `HISTORY` and `CURRENT_REQUEST` only.
4. The three-line `select_messages` window, and the printed selection.
5. One real API response to the window plus the current request.

### Watch out

1. **Do not spoil which messages matter.** Do not slow down on any individual message,
   do not read the first four with more emphasis than the last three, and do not say
   "notice this one". The learner finding it is the entire exercise.
2. `history_starter.py` line 40 carries a comment reading "decisions are the signal, and
   they sit OUTSIDE the last 3 messages". That is a direct spoiler for Steps 4 and 5, and
   the defect register states these giveaway comments were removed, so the register and
   the file disagree. **Do not scroll past line 39 on camera.** Frame the editor so the
   `__main__` block is below the visible area. Get it corrected before republish and
   update the register in the same commit.
3. Do not mention word overlap, relevance, or pinning in this video. Both bad proxies
   are supposed to arrive in order.
4. The response you get is a live generation and will differ between takes. Do not script
   a specific wrong answer. Script the question you ask about it.

---

## Video 4.10: Exercise 12 Part 2, why recency failed

**Runtime:** 9 minutes
**On screen:** editor, then terminal

### Say

Open by naming what went wrong, precisely, and give this one close to verbatim: **"This
is not a model failure. The model answered the question it was given, using the context
it was given. The context was wrong, and you chose it."**

Then the shape worth remembering. A sliding window uses recency as a proxy for
importance, and recency is a poor proxy. Constraints behave in a particular way in real
projects: stated once, early, in one sentence, and then carried silently by everybody for
the rest of the work. Small talk happens constantly, and much of it is recent. So a
window sized to the last few messages systematically keeps the cheap content and drops
the expensive content. It is not slightly wrong, it is wrong in a direction.

Step 7 is the rules before the filter. Read the include list and the exclude list, then
point at what is on neither: how recently it was said.

Step 8 is the second trap and it needs careful handling. The keyword-overlap filter is a
reasonable first implementation and it is going to select nothing older on this data. Do
not present that as a mistake the learner made. Say both outcomes are real results, and
if the filter selected nothing, that finding is worth more than a working filter. Then
explain why: a constraint stated early often shares no words at all with the request that
depends on it, because by the time you ask the question the constraint has become an
assumption nobody restates. Lexical overlap is a second proxy and it fails for the same
reason the first one did.

The fix is a rule that does not depend on topic matching. Show the classification prompt,
CONSTRAINT, DECISION or CHATTER, with the test that makes it usable: a message is a
constraint or a decision if a developer implementing this system later would be wrong to
ignore it. Then keep every constraint and decision regardless of age, keep the recent
window, drop the rest. Say the one-line conclusion: **"Important context gets pinned, not
aged out."**

Step 9 is assembly order and two mechanical points: the system instruction is a top-level
parameter, and the bundle must end with exactly one user turn. Add the fallback and say
that an empty filter result is a normal outcome rather than an error.

Step 10 is the topic shift, and then the shape of the code. Selection in one function,
the API call in another. Storing conversation data and choosing what to send are two jobs
with two different reasons to change.

### Show

1. The relevance rules, written out.
2. The overlap filter wired into `select_messages`, and the selection it prints.
3. The classification prompt in the browser or in a comment block, and the selection that
   results from pinning.
4. Two responses side by side, the Step 5 one and the new one.
5. The topic-shift run.

### Watch out

1. Keep the Step 5 response from video 4.9 available. You cannot show a comparison you
   did not keep, and re-running it gives you a different answer.
2. Do not change the filter and the prompt in the same step on camera. Two changes give
   you no information, which is a lesson in itself.
3. Still do not show the bottom of `history_starter.py`.
4. If your classification pass mislabels a message, keep it in and say what you would do
   about it. A filter that is wrong once is more honest than a demo that never is.

---

## Video 4.11: Module close, and your capstone brief

**Runtime:** 5 minutes
**On screen:** deck, then `docs/capstone-brief.md`

### Say

This is the most important structural beat in the programme, so treat it as a handover
rather than a wrap.

Slide 25 is the review activity, rewritten to use artefacts that exist. Frame it as
individual work: compare your Exercise 11 CLI against the reference, look at the
injection surface, look at what your Exercise 12 context strategy costs, and write the
notes down because they become the design note in your capstone README. Slide 26 is the
decision and the justification. In a recorded course there is nobody to present to, so
the deliverable is written.

Slide 27, takeaways, briefly.

Then switch to `docs/capstone-brief.md` and issue it. Say the reason for the timing out
loud: **"You are getting this now, at the end of Module 4, rather than in Module 5,
because you have the API skills it needs and because you need elapsed time to build it.
Module 5 teaches the planning and configuration skills the build consumes, and Exercise
15 is the build itself."**

Cover exactly five things off the brief and nothing else:

1. The scope. Two endpoints, `POST /summarize` and `GET /health`. If it is taking more
   than a few hours, it is over-scoped.
2. The framing question, and that it is answered in writing before any code: what is the
   smallest version that still demonstrates the skill.
3. The weighting. Prompt design and robustness carry half the marks between them, 25
   each, and neither of them is about getting the service working.
4. The three gates, because a gate is not a deduction. A real key in the repository, its
   history, the zip or a screenshot. No reflection. A service that does not start from a
   clean clone following their own README.
5. The one-paragraph problem statement, written before Module 5's labs, using the use
   case they wrote down in Module 1.

Close by telling them the skeleton exists so setup does not eat the time meant for
prompt design, that the prompt in it is deliberately left as TODO markers, and that the
test suite deliberately does not pass as shipped. Then stop. Do not explain either.

### Show

1. Slides 25, 26, 27.
2. `docs/capstone-brief.md`, scrolled to the rubric table and then to the gates table.

### Watch out

1. Slide 25 in the revised deck has a defect. The rewritten five-bullet block was added
   as a new shape and the four original vendor bullets were left on the slide underneath
   it, including "Identify flaws in how the suggested architectures handle session state
   persistence" and "for each proposed solution", which refer to the three sample
   architectures that were never supplied. **Fix the slide before you record this video,
   or you will have contradictory text in frame.** Delete shapes 391 to 394.
2. Do not read the rubric point by point. Read the weights and the gates, and tell them
   the thresholds are in the brief.
3. Do not put a submission date on screen. The brief says learners submit against
   whatever date their enrolment gives them, and a date in a recorded video is wrong for
   every cohort after the first.
4. Do not promise an outcome. No employability language, no certification language.
5. This video and Module 5 slide 17 have to agree that the brief was issued here. If you
   re-cut either one, re-check the other.

---

## The teaching points that carry this module

1. A credential and a model identifier are both configuration, they belong outside the
   code for the same reason, and nothing ever prints a secret, not even a prefix.
2. There is one messages endpoint with the model in the request body, the documented key
   header is `x-api-key` with a required `anthropic-version` header on raw calls, and
   knowing both turns a 401 or a 404 into a five-minute problem.
3. A prompt boundary needs a marker and a rule together, and even then it raises the cost
   of an injection rather than removing it, so the defence you ship is not trusting the
   output.
4. The API is stateless, so conversation is something you build by resending, and the
   engineering question is not how to store history but which subset of it to send.
5. Recency and word overlap are both proxies for importance and both fail in the same
   direction, which is why important context gets pinned rather than aged out.

## Questions learners will ask, and the answers

| Question | Answer |
|---|---|
| Which model should I use? | Pick by capability tier for the job, then read the current identifier from configuration. Look the identifier up in the official documentation on the day, because identifiers change and a stale one produces an error that looks like an authentication failure. |
| Why does the course never name a model? | A named version on screen dates the video permanently and forces a re-record on somebody else's release schedule. The durable skill is tier selection plus one configuration constant. |
| Can I use `Authorization` instead of `x-api-key`? | An `Authorization` header is also accepted. `x-api-key` is the documented primary, so reach for it first, and expect to see both in other people's integrations. |
| Do I need a different endpoint for a different model? | No. One messages endpoint, model in the request body. A URL built per model returns a 404 and is a sign something has gone wrong. |
| Why did my raw `curl` call fail when the SDK worked? | Most often a missing `anthropic-version` header, which the SDK sets for you. Second most often, `.env` is loaded into your Python process and not into your shell, so the key expanded to nothing. |
| `max_tokens` is set and my answer is still long. | `max_tokens` is a ceiling on the output, not a request for brevity. Ask for a short answer in the prompt. Those are two different fixes for two different problems. |
| Does prompt caching give me a bigger context window? | No. It is a cost and latency optimisation on a stable prefix. The room is the same, it is cheaper to reuse. Check the current mechanics in the documentation before relying on them. |
| Why must messages alternate between roles? | The API expects an alternating conversation. Two user messages in a row produces an error that reads as though something deeper is wrong. Print the roles in order before you send. |
| Can I put the system prompt in the messages list? | No. It is a top-level parameter on the request. Putting it in `messages` fails at the API rather than in your editor, and it is the usual symptom of porting code from another provider. |
| My relevance filter selected nothing. Did I do it wrong? | No, and that is the finding. A constraint stated early often shares no vocabulary with the request that depends on it. That is why the working pattern pins constraints instead of matching words. |
| Do I have to finish Exercise 11 before Exercise 12? | No. `history_starter.py` carries the conversation and the topic shift already built, so Exercise 12 stands on its own. |
| Can I rename the environment variable to match my house style? | Not inside this programme. Exercises 10, 11, 12 and 15 all read `ANTHROPIC_API_KEY`, and a second name for the same secret is how a chain of exercises breaks in the middle. |
| When is the capstone due? | Against the date your enrolment gives you. Start the problem statement now, before Module 5's labs. |

## Pre-record checklist for this module

1. Generate a throwaway API key, set a low spend cap, and put the revocation date in
   your calendar today rather than on the day you expect to finish.
2. Confirm `.gitignore` in the Exercise 10 starter folder contains `.env`, and that it
   exists before `.env` does.
3. Create `.env` with `ANTHROPIC_API_KEY` and `MODEL`, looking the model identifier up in
   the official documentation on your record date.
4. Confirm `ANTHROPIC_API_KEY` is the variable name in the Exercises 10, 11 and 12
   starter files. Breaking one breaks Exercise 15.
5. Confirm no script in any Module 4 `starter/` folder hardcodes a model identifier.
6. Fix revised deck slide 25: delete the four leftover vendor bullet shapes so only the
   rewritten block remains. Re-export and re-check the slide count is still 28.
7. Decide what you are doing about `history_starter.py` line 40. Either trim the spoiler
   comment and update `docs/lab-defect-register.md` in the same commit, or frame the
   editor so the file's `__main__` block never enters shot.
8. Start a fresh shell, disable notifications, reduce the prompt to a directory name, and
   confirm the shell does not echo expanded commands.
9. Close every editor tab and every folder except this repository. Increase both fonts
   until they look absurd, then check them on your smallest target screen.
10. Create the Exercise 11 working folder outside the courseware clone, with its own
    `.gitignore` already containing `.env`.
11. Rehearse video 4.6 once against a clock. It is nine lab steps in a 12-minute cap and
    it is the only video in this module with no slack.
12. Read `docs/capstone-brief.md` end to end once, so video 4.11 is a handover rather
    than a reading.
13. **Verification run.** From `module-4-claude-api/03-labs/exercise-10-env-keys/starter/`,
    run `python verify_key.py`. Expected: the key loads, a length is reported, no part of
    the key value appears anywhere in the output, and the call succeeds. If any character
    of the key appears, stop and fix the script before recording anything in this module.
14. **Verification run.** From
    `module-4-claude-api/03-labs/exercise-12-conversation-history/starter/`, confirm that
    a three-message window selects the last three messages of `HISTORY` and that a
    keyword-overlap filter over the earlier four selects nothing. Both behaviours are
    what videos 4.9 and 4.10 are built on. If either has changed, the narration is wrong.

---

Copyright © 2026, ZaranTech LLC. All rights reserved. Internal trainer document.
