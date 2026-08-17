# Open questions for the vendor content team

Addressed to the vendor content team now co-maintaining the **Claude AI for
Developers (AI-led SDLC)** material.

We have rebuilt the programme for self-recorded on-demand delivery and resolved
everything we could resolve on our own. What is left are the items where either
the answer only exists on your side, or the decision is yours to make. This
document is that list, with our reasoning and a proposed default for each, so you
can confirm a default rather than start from a blank page.

Where we already made a change, we say so and we say what we changed it to. If our
change is wrong, tell us and we will revert it. Nothing here needs a long reply.
Item numbers are stable, so answering "1 yes, 2 confirmed, 3 option B" is enough.

## Summary

| # | Item | What we need | Blocking |
|---|---|---|---|
| 1 | Module 1 Exercise 2 | Confirm it never existed, or send it | Module 1 lab set |
| 2 | Lab durations | Confirm or correct fifteen durations | Runtime plan and video splits |
| 3 | Assessment difficulty | Confirm the intended level | All five assessment rewrites |
| 4 | Module 4 assessment versus Module 4 deck | Choose: extend the deck, or drop four questions | Module 4 assessment and deck |
| 5 | Answer-key distribution | Reshuffle to a roughly even spread | All five answer keys |
| 6 | Module 2 deck content gap | Confirm we may add code slides and a project context file section | Module 2 deck |
| 7 | Module 4 slides 22 and 23 | Send the three sample architectures, or approve replacing the activity | Module 4 deck |
| 8 | Module 5 capstone evaluation | Review the rubric we wrote | Capstone marking |
| 9 | Citation residue and authoring notes in your masters | Apply the same cleanup to your copies | Divergence risk |
| 10 | Google Slides or PPTX as master | Tell us which direction is authoritative | Every deck change |

---

## 1. Module 1 Exercise 2: was it ever written?

The vendor lab pack contains fourteen documents numbered Exercise 1 to Exercise 15.
Exercise 2 is absent. Module 1 has Exercise 1 and Exercise 3 with nothing between
them.

Because the numbering is global across the programme rather than per module, the
gap is a real gap rather than a numbering artefact. That is what made us confident
enough to author a replacement rather than renumber.

**What we did.** We wrote a Module 1 Exercise 2, "Structure a developer prompt".
It practises the prompt anatomy your Module 1 deck teaches on slides 10 to 17,
which no other lab in the programme exercises. It is browser only, twelve minutes,
and it ends with the learner saving a four-part prompt template that Exercises 4,
5, 7 and 13 then start from. It matches the structure and voice of the other
fourteen.

**What we need from you.**

1. Confirm whether Exercise 2 was never written, or was written and not shared.
2. If yours exists, send it and we will reconcile. Ours is deliberately narrow, so
   if yours covers a different skill we may want both, with one renumbered.

---

## 2. Every lab document arrived with no stated duration

None of the fourteen lab documents states an intended duration. Exercise 15 is the
only one that gives any timing at all, and it does so inside its own body text
rather than in a header.

This is the single mis-scoping cause we found. Without durations there was no way
to check the lab set against the delivery budget, and the programme was
consequently planned at roughly half its real length.

**What we did.** We assigned a duration to each of the fifteen exercises, put it in
the lab header, and mirrored the set in `docs/programme-map.md`.

| Ex | Module | Duration | Ex | Module | Duration |
|---|---|---|---|---|---|
| 1 | 1 | 12 min | 9 | 3 | 15 min |
| 2 | 1 | 12 min | 10 | 4 | 12 min |
| 3 | 1 | 15 min | 11 | 4 | 22 min |
| 4 | 2 | 12 min | 12 | 4 | 18 min |
| 5 | 2 | 20 min | 13 | 5 | 18 min |
| 6 | 2 | 22 min | 14 | 5 | 12 min |
| 7 | 3 | 15 min | 15 | 5 | 35 min |
| 8 | 3 | 15 min | | | |

**What we need from you.** Confirm or correct these against your own intent when
you wrote the labs. If you intended Exercise 6 to be a ten-minute activity and we
have scoped it at twenty-two, we have changed the shape of your material without
meaning to, and we would rather know.

---

## 3. Assessment difficulty sits well above the decks and the labs

The five assessments are internally consistent and well written. They are also
pitched at a materially higher level than the material that precedes them.

The labs ask the learner to create a folder, paste a function, read a traceback,
and run a test suite. The assessments ask scenario questions about race conditions
in very large monolithic files, out-of-memory behaviour under multiprocessing, and
prompt injection defence.

More concretely, these terms are **tested but never taught anywhere in the decks or
labs**:

| Term | Tested in | Taught in |
|---|---|---|
| Attention dilution | Assessment | Nowhere |
| Catastrophic backtracking | Assessment | Nowhere |
| ReDoS | Assessment | Nowhere |
| Negative constraint | Assessment | Nowhere |

A learner who completes every lab correctly can still fail, and the failure would
not tell them anything useful about their own gaps.

**What we did.** We are recalibrating the assessments downward toward the taught
material, and folding the four terms above into the teaching wherever they are
genuinely worth keeping. Negative constraints in particular belong in the prompt
anatomy material rather than only in a test.

**What we need from you.** Confirm the intended difficulty. There are two coherent
positions and we are happy with either:

- **Option A.** Assessments measure the taught material. We recalibrate down and
  the questions align to the decks and labs.
- **Option B.** Assessments are a deliberate stretch challenge. We keep the
  difficulty, label them explicitly as stretch, and say so on screen so a learner
  who scores 5 out of 10 does not conclude they have failed the module.

We have proceeded on Option A because it is the safer default for a self-check
assessment with no live debrief to explain the gap. Tell us if you intended B.

---

## 4. The Module 4 assessment tests four topics the Module 4 deck never covers

This is the most concrete misalignment in the pack, and it is worth separating from
item 3 because it is a coverage error rather than a difficulty judgement.

| Topic | Tested | Present in the Module 4 deck |
|---|---|---|
| System prompt as a top-level parameter | Yes | No |
| Prompt caching | Yes | No |
| Assistant prefill | Yes | No |
| The alternating-roles requirement for messages | Yes | No |

That is four of ten questions, so **40 percent of the Module 4 assessment tests
material the module does not teach**.

**What we need from you.** One of two things, per topic. Either the deck adds it, or
the question goes. Both are acceptable and we do not have a strong preference on
three of the four.

Our recommendation, for what it is worth:

1. **Add all four to the deck.** They are all genuinely useful to a developer
   integrating the API, the deck has room once the recorded format removes the
   one-hour constraint, and prompt caching in particular is the kind of thing a
   learner will meet in their first week of real integration work.
2. If only one is added, add prompt caching.
3. If the deck is frozen, drop the four questions and replace them with questions
   on material the deck does teach.

Please also note that we removed version-pinned premises from this assessment,
because a question whose premise names a specific model version and quotes its
context and output limits becomes not merely dated but wrong. We replaced that
framing with version-neutral wording about the difference between a context window
and an output ceiling.

---

## 5. Answer distribution is heavily skewed toward option b

Across the five assessments:

1. In Module 5, **nine of ten** correct answers are option b.
2. Across all **fifty** questions, b is correct roughly **half** the time.

A random-guessing learner should score about 25 percent. A learner who notices the
pattern and answers b throughout scores around 50 percent on the set and 90 percent
on Module 5, without knowing any of the material.

This matters more in the recorded format than it did in the live one, because the
assessments are now self-check. Their only job is to give the learner an honest
signal about their own understanding, and a position-biased key destroys exactly
that.

**What we need from you.** Reshuffle the option order so the correct answer is
distributed roughly evenly, near 25 percent per position across the fifty
questions. We can do the reshuffle if you prefer, but the answer key is yours and
we would rather not be the ones renumbering it.

One request while you are in there: keep the distractors attached to their
reasoning. Several of the distractors are good, in the sense that they represent a
real mistake a developer makes, and a blind reshuffle can accidentally turn a
plausible distractor into the obviously silly one.

---

## 6. Module 2's deck has no code on any slide, and never mentions a persistent project context file

This is the largest content gap in the programme, and it is a gap in the module
where it hurts most.

The observations:

1. **No slide in the Module 2 deck contains code.** The module is called "Claude for
   Coding Tasks" and is the module that introduces Claude Code.
2. **Six slides cover organising project context**, and none of them mentions a
   persistent project context file committed to the repository, which is the single
   highest-leverage practice in the whole subject area.
3. The deck also frames several workflows as pasting code into a chat window, which
   is the pattern Claude Code exists to replace. Exercise 4 Step 8 has the same
   framing, so the deck and the lab need to move together.

**What we need from you.** Confirm we may:

1. Add code to the Module 2 deck. Python, consistent with the rest of the
   programme.
2. Add a section on the persistent project context file: what it is, what belongs
   in it, what does not, and the failure mode when the code changes and the context
   file does not. The last of those is one of the two traps in the capstone brief,
   so the deck and the capstone reinforce each other.
3. Reframe slides 6, 7 and 13 from paste-into-chat to Claude Code reading the
   repository, alongside the matching change to Exercise 4.

This is additive rather than corrective, which is why we are asking rather than
just doing it.

---

## 7. Module 4 slides 22 and 23 require three sample architectures that were not supplied

Slides 22 and 23 describe an activity built around three sample architectures. The
architectures themselves are not in the deck, the speaker notes, or the lab pack.

As shipped the activity cannot run, and in a recorded course there is no facilitator
who can improvise three examples on the spot.

**What we need from you.** Either:

1. Send the three sample architectures you had in mind, or
2. Approve replacing the activity. Our proposed replacement is a single worked
   example carried through on camera, which suits the recorded format better than a
   three-way comparison anyway, since the learner cannot be split into groups.

---

## 8. Module 5's capstone evaluation had no markable thresholds

The capstone evaluation section is three slides of criteria expressed as
adjectives: good prompt design, robust error handling, clean structure, and
similar. The criteria themselves are the right criteria. What is missing is any
threshold, so there is nothing that tells a reviewer where "robust" starts.

Two reviewers marking the same submission against those three slides would not
agree, and the capstone carries completion for this programme, so the mark has to be
defensible.

**What we did.** We wrote a rubric in `docs/capstone-brief.md`. It keeps your six
criteria, adds weights, and adds three explicit bands per criterion described in
observable terms.

| Criterion | Weight |
|---|---|
| Prompt design | 25 |
| Robustness and failure handling | 25 |
| Correctness | 15 |
| Tests | 15 |
| Reflection | 10 |
| Structure, documentation and responsible practice | 10 |

Prompt design and robustness carry half the marks between them, on the reasoning
that a minimal service with a well-designed prompt and clean failure paths
demonstrates more of what this programme teaches than a feature-rich service with a
concatenated prompt. There are also three gates, the strictest being that a real API
key present in the submission stops the submission being marked until the key is
rotated.

**What we need from you.** Review it, particularly the weighting split and the pass
threshold of 60. If your intent was that correctness should dominate, our weighting
is wrong and we should change it before anyone is marked against it.

---

## 9. Citation residue and authoring notes in learner-facing text

Fourteen lab documents contain fragments left over from the research and drafting
process, inside text a learner reads. Examples of the pattern:

1. Trailing citation markers such as `youtube+1` at the end of a step.
2. `platform.claude+2` and several instances of a bare trailing `platform.`
   mid-sentence.
3. **Exercise 9 opens with an authoring note addressed to the course author**,
   describing what the document does and does not include and referencing a Udemy
   course.

Item 3 is the one to prioritise on your side. It is the first thing a learner reads
in that lab, it is clearly not written for them, and in a published video course it
would be visible on screen.

**What we did.** We removed all of it from our copies during the rewrite, along with
the same class of residue wherever else it appeared.

**What we need from you.** Apply the same cleanup to your master copies. If your
masters are the source of the next revision, as item 10 may determine, the residue
comes back on the next sync and we would be removing it twice.

---

## 10. Are the Google Slides decks the live master?

This is the item that most needs an answer, because until it is answered every deck
change risks being overwritten.

The current situation:

1. The decks exist as Google Slides in a shared Drive folder.
2. The same decks exist as PPTX files in the working set.
3. We produced **revised PPTX files** plus a **slide-by-slide changelog** per module,
   specifically so you can apply each change in Slides by hand rather than importing
   a PPTX and losing your formatting, master slides and any comment history.

That approach only works if Slides is the master and our PPTX is a proposal. If our
PPTX is the master, the changelogs are unnecessary overhead and you should be
working from our files directly.

**What we need from you.** Tell us which direction is authoritative:

- **Option A. Google Slides is the master.** We continue to deliver changelogs, you
  apply changes in Slides, and our PPTX files are read-only reference. We stop
  treating our revised PPTX as shippable.
- **Option B. PPTX is the master.** You take our revised files as the new baseline,
  the Slides copies become exports, and we drop the changelogs.

Either works. What does not work is both sides editing, because the decks then
diverge slide by slide and neither copy can be trusted, which is expensive to
untangle once videos have been recorded against one of them.

---

## Already fixed on our side, for your master copies

Not questions. These are corrections we have already made, listed so your masters
can be brought into line and so you can challenge any of them.

| # | Where | Issue | Our change |
|---|---|---|---|
| 1 | Exercise 10 | Hardcoded, several generations stale model identifier in the code block | No identifier in any script. Every script reads `MODEL` from the environment and fails with a message naming what to set. The learner's step is to look the current identifier up in the official documentation |
| 2 | Exercises 10, 11, 12 | `ANTHROPIC_API_KEY` in Exercise 10, `CLAUDE_API_KEY` in Exercise 11, and Exercise 12 depending on Exercise 11's output. The chain was broken | `ANTHROPIC_API_KEY` throughout. The official SDKs read it from the environment by default, which also removed a line of code from Exercise 10 |
| 3 | Module 4 deck, API mechanics | Slides described the standard authorization header and implied a per-model endpoint | Corrected to the documented `x-api-key` header, with `anthropic-version` required on raw HTTP calls, and a single messages endpoint with the model as a body parameter. An `Authorization` header is also accepted, which we mention once |
| 4 | Module 3 slide 12 | Growth of a nested scan described as exponential | Corrected to quadratic. Exercise 8 demonstrates exactly this, so the deck was contradicting the lab |
| 5 | Exercise 1 prerequisites and Steps 1 and 4 | Offered "a sandbox environment that simulates Claude" as an alternative path | Removed. No such sandbox exists in this delivery, and the dual framing made Step 4 ambiguous |
| 6 | Seven labs | Instructed the instructor to supply a starter file, and none was supplied | All seven now exist in the repository, are referenced by path from the lab, and are verified by running them |
| 7 | Exercises 6, 11, 15 | Python, Node and in one case Java branches | Python only across the programme, with one narration line noting the equivalent exists in other stacks. This was the largest single saving available on recording effort |
| 8 | All fourteen labs | Written in live-facilitator voice, "ask learners to", "have learners" | Rewritten in second person to the learner, with an explicit pause instruction at the end of every hands-on step, because a recorded lab has no moment where the room catches up |
| 9 | Module 1 slide 8 | Subject and verb disagreement, "leads" for "lead" | Corrected. Worth flagging because on a published video it is permanent |
| 10 | All five decks | No section map | An exercise-list slide added to the front of each deck. In a recorded course learners navigate by section rather than by the trainer's voice |

Reference documents on our side, if you want to see the reasoning behind any of the
above: `docs/course-context.md` for the decisions and their rationale,
`docs/programme-map.md` for runtime and dependencies,
`docs/lab-authoring-spec.md` for the lab structure and voice rules, and
`docs/capstone-brief.md` for the rubric in item 8.

One document is deliberately not for distribution. `docs/lab-defect-register.md`
records every planted defect in every starter file, verified by running the code.
Please keep it out of learner-facing material and out of the decks, since several
labs depend on the learner finding those defects unaided.
