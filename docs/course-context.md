# Programme context and decisions

Cross-session memory for this repository. If you are picking this repo up cold, in
a new chat or a new Claude Code session, read this file and then `CLAUDE.md`.
Everything here explains *why* the material is the way it is, which is the part
that is not visible from the files alone.

Last reviewed: 17 August 2026. Maintain this file. When you take a decision that
a future session would otherwise reverse, add it to the decisions list below.

## Read this before you trust any other document

1. **This programme is a self-recorded on-demand video course.** It is not live
   instructor-led training. That single fact governs runtime, lab voice,
   assessment design and capstone timing.
2. **The earlier live-delivery facilitator kits are superseded.** An earlier
   working session produced a full set of 60-minute run sheets, timing blocks and
   facilitator kits for five one-hour live sessions. That format was abandoned.
   Those kits are no longer the plan of record and are not in this repository.
3. **Voice is the fastest way to spot a stale document.** Anything written in
   facilitator voice ("ask learners to", "have learners", "tell learners",
   "discuss with your group", "debrief the room") predates the format change. If
   you find it, the document is stale. Fix it against
   `docs/lab-authoring-spec.md` rather than working from it.
4. Any document that assigns a module a 60-minute budget, or lists a live run
   sheet with wall-clock blocks, is superseded by `docs/programme-map.md`.

## What this programme is

ZaranTech **Claude AI for Developers (AI-led SDLC)**. Five modules, fifteen
exercises, one capstone. Total runtime is about 7 hours 30 minutes of video plus
learner build time on the capstone. Trainer: Dhruv. The vendor material set is
labelled June 2026.

The outcome the programme is actually chasing is judgement, not tool familiarity.
A learner who finishes should be able to decide when to reach for the chat
interface, when to reach for Claude Code, and when to reach for the API, and
should be able to tell a fluent wrong answer from a correct one.

### Audience

1. Working developers and IT consultants adopting Claude across the software
   development lifecycle.
2. Mixed seniority. Comfortable reading Python, not necessarily comfortable with
   pytest, virtual environments or HTTP debugging.
3. Enterprise context. Some learners are on managed corporate laptops where a
   terminal install or an outbound API call may be restricted.

Point 3 was the highest-risk unknown in the live design, because a blocked laptop
derailed a live room in real time. Recorded delivery does not remove the problem,
it moves it earlier: the requirements have to be stated in the course intro so a
learner resolves access before reaching Module 2, rather than discovered live. See
`docs/programme-map.md`, "Escalating environment requirements".

## Source material and where each asset lives

| Asset | Where it lives | Notes |
|---|---|---|
| Vendor decks, Modules 1 to 5, Google Slides | Google Drive, synced into the Claude project as MCP resources | Direction of authority is unresolved. See `docs/open-questions-for-vendor.md`, item 10 |
| Vendor decks, Modules 1 to 5, PPTX | Claude project docs, 5 files | Working copies of the same decks |
| Vendor lab documents, 14 PDFs | Claude project files | Fourteen documents against fifteen numbered exercises. Exercise 2 is the gap |
| Vendor assessments, 5 PDFs | Claude project files | Ten scenario MCQs each, fifty total |
| Vendor trainer materials summary | Claude project files | `Claude AI for Developers Video Course June 2026 Trainer Dhruv Materials.pdf` |
| Session meeting link sheet | Google Sheets, synced | Legacy of the live design. Not used by the recorded course |
| Lab documents, 15 authored in-house | `module-N-*/03-labs/exercise-NN-*/lab.md` | Source of truth. DOCX is generated from the markdown |
| Starter code, all planted defects | `module-N-*/03-labs/exercise-NN-*/starter/` | Load-bearing. Do not fix. See `CLAUDE.md` |
| Capstone skeleton | `module-5-advanced-capstone/03-labs/exercise-15-summarizer-microservice/starter/capstone_skeleton/` | Flask, four tests, one failing on purpose |
| Defect register, trainer only | `docs/lab-defect-register.md` | Never copy into a lab or a slide |
| Lab structure and voice rules | `docs/lab-authoring-spec.md` | Binding on all fifteen labs |
| Runtime, dependencies, durations | `docs/programme-map.md` | Change a duration here and in the lab header together |
| Capstone brief, learner facing | `docs/capstone-brief.md` | Issued at the end of Module 4 |
| Recording risks and pre-record checklist | `docs/recording-hygiene.md` | Trainer only |
| Questions for the vendor content team | `docs/open-questions-for-vendor.md` | |
| Revised PPTX decks and slide-by-slide changelogs | Delivered to the vendor content team in an earlier session | **Not yet committed** under `01-deck/`. See outstanding work |
| Recording prep master, earlier session | `RECORDING-PREP-MASTER.md`, outside this repo | The origin of the recorded-format decisions. Superseded by this `docs/` set |

`CLAUDE.md` specifies `01-deck/`, `02-facilitator/`, `04-assessment/` and a
`vendor-original/` folder per exercise. Only `03-labs/` is populated today. That
is stated so nobody assumes a missing folder means a lost file.

## Decisions taken

Numbered so they can be cited. Do not renumber. If a decision is reversed, mark
it reversed in place and add the replacement at the end.

### Format

1. **Delivery is recorded and on demand, not live.** Recorded delivery removes
   the room, which removes the two things the live design depended on: a shared
   pace and a live debrief. Everything below follows from this.

2. **There is no 60-minute cap per module.** The hour existed because a live
   session was booked for an hour. Fourteen labs and five full decks never fitted
   inside five hours, and compressing them was the main source of damage in the
   live design. Real runtime is about 7 hours 30 minutes and that is a legitimate
   length for this format.

3. **No single video runs longer than 12 minutes.** Attention drops and a
   re-record becomes expensive when one video carries thirty minutes of content.
   A full deck becomes three or four lectures, and the long labs split. See the
   video granularity table in `docs/programme-map.md`.

4. **Lab documents are learner handouts, not trainer scripts.** In a recorded
   course the learner reads the lab while the video plays, so every instruction is
   second person and addressed to them.

5. **Every hands-on step carries an explicit pause instruction.** A recorded lab
   has no natural moment where the room catches up. If a step expects the learner
   to do something and does not tell them to pause, the step is incomplete.

6. **Assessments are self-check. The capstone carries completion.** Ten MCQs per
   module are useful for retrieval practice and can be auto-marked by a platform,
   but they cannot evidence that a learner can build anything. The capstone can,
   so it is the item that carries completion and it is the item with a defensible
   rubric.

### Structure

7. **Exercises are numbered globally, 1 to 15, not per module.** This is what
   established that Module 1 Exercise 2 genuinely was missing rather than
   misfiled: the vendor pack jumps from Exercise 1 to Exercise 3 inside Module 1.
   Exercise 2, "Structure a developer prompt", was authored in-house to fill the
   gap and to practise the prompt anatomy the Module 1 deck teaches but no vendor
   lab exercises.

8. **"Repo as context" versus "repo as workspace" is taught explicitly, in
   Module 1.** Attaching a GitHub repository to the Claude app syncs file
   contents on one branch as **reading material**. It does not grant commit
   access, pull request access, or commit history access. Claude Code is what
   operates on a repository. This is the single most useful distinction in the
   programme and the most common source of learner confusion, so it is taught
   rather than implied.

9. **Exercise 15 IS the capstone, not a lab that precedes it.** Both are a
   microservice that calls the API to summarise code. Running Exercise 15 as a
   lab and then setting a separate capstone makes the learner build the same
   service twice.

10. **The capstone is briefed at the end of Module 4, not in Module 5.** The
    learner needs elapsed time to build it, and the brief depends on Module 4's
    API material. Recording removes the scheduling constraint but not the build
    time. Module 5's Exercises 13 and 14 then teach the planning and
    configuration skills the capstone consumes.

11. **Module 1 is browser only.** No terminal, no clone, no key. A learner can
    start the programme on day one while still waiting on an install or a key.
    Claude Code is previewed in the Module 1 deck and first used in Module 2.

12. **Exercise 6 sits at the end of Module 2, not in Module 3.** It produces a
    test suite, and Module 3 opens by running that suite and watching it fail.
    The linkage is deliberate and worth preserving through any resequencing.

13. **The Exercise 3 review checklist is supplied, not authored by the learner.**
    Authoring a checklist consumes the time that should go into applying one.
    Extending it for the learner's own stack is an optional "Going further" step.

### Technical conventions

14. **No Claude model version name appears anywhere.** Not in a slide, a lab, a
    script, or narration. A named version on screen dates a published video
    permanently, and version names change faster than a course refresh cycle.
    What is taught instead is the tier-selection habit: the most capable tier for
    architecture and debugging, a faster tier for repetitive well-specified work.

15. **No script hardcodes a model id.** Every script reads `MODEL` from the
    environment and fails with a sentence telling the learner what to set. The
    learner's own step is to look up a current identifier in the official
    documentation, which is a more durable skill than copying one from a slide.

16. **`ANTHROPIC_API_KEY` everywhere.** The vendor labs switched to
    `CLAUDE_API_KEY` in Exercise 11 while Exercise 12 depended on Exercise 11's
    output, which broke the chain. The official SDKs read `ANTHROPIC_API_KEY`
    from the environment by default, so standardising on it also removes a line
    of code from Exercise 10.

17. **Python only, Python 3.11 or later.** The vendor labs offered Node and Java
    branches in Exercises 6, 11 and 15. Recording every branch triples both the
    recording work and the re-record burden, and it triples learner setup. Where
    a vendor lab offered a choice, the lab picks Python and one narration line
    notes that the equivalent exists in other stacks.

18. **Nothing prints key material, not even a prefix.** A truncated key in a
    screenshot, a log aggregator or a published video is still a leaked prefix.
    Presence and length answer the only question the learner has, which is
    whether the file loaded. See `docs/recording-hygiene.md` for one place where
    the code does not yet match this decision.

19. **Planted defects are load-bearing and documented.** Every deliberate bug is
    recorded in `docs/lab-defect-register.md`, verified by running the code
    rather than reading it, and never revealed in a learner-facing document.

20. **The capstone skeleton is Flask.** An earlier note recommended FastAPI. The
    shipped skeleton is Flask, and Flask is what the framework-level 413 lesson
    is written against. Marking does not depend on the framework, so this is a
    consistency decision rather than a technical preference.

## What changed from the live-session design, and why

If you find an old 60-minute run sheet or a facilitator kit, this table tells you
what replaced it.

| Live design | Recorded design | Why it changed |
|---|---|---|
| Five 60-minute sessions, about 5 hours total | About 7 hours 30 minutes of video, no per-module cap | The hour was a booking constraint, not a content one. Compression was damaging the material |
| Decks delivered as one continuous session block | Each deck split into three or four lectures under 12 minutes | Learners navigate a recorded course by section, not by the trainer's voice |
| Labs compressed and guided so the room stays in sync | Labs are self-paced learner handouts with explicit pause points | There is no room to keep in sync. Desynchronisation is no longer a risk, so labs run at full length |
| Some labs assigned as homework to protect the hour, notably Exercises 6 and 12 | All fifteen exercises are in-course lab videos | With no hour to protect, there is no reason to move a lab out of the course |
| Each module opened by consuming the previous module's homework | Module openings still reference the previous module's artefacts, but nothing is gated on submitted homework | A recorded course cannot collect homework before the next video plays |
| Assessments were homework, debriefed live at the start of the next module | Assessments are self-check with an answer key and rationale | There is no live debrief. The rationale has to be written into the key |
| Live debrief carried the hardest teaching points, including the Exercise 5 breaking-change trap | Those points are written into the lab documents and narrated on camera | A point that only existed in a live debrief was lost entirely by the format change. This was the largest content risk in the migration |
| Capstone reviewed in a live session after Module 5, with an office-hours slot | Capstone submitted against a written rubric with markable thresholds | With no live review, the rubric is the only thing standing between two reviewers and two different marks |
| Facilitator kits per module | Recording deck plus recording script per module, in `02-facilitator/` | Different artefact, same slot in the folder structure |
| Cohort profile, cadence and delivery mode were open blockers | Resolved by the format: on demand, self-paced, no cadence | Three of the five live-design open questions disappeared. Terminal and key access remains real and is now handled in the intro |

## Status

Honest state, not intent. Every row verified against the repository.

| Module | Labs | Deck revised | Facilitator | Assessment | Module README |
|---|---|---|---|---|---|
| 1 Fundamentals | Ex 1 to 3, Ex 2 authored in-house | 27 slides, 4 edits, 2 added | Script and deck | 10 questions, key, changelog | Yes |
| 2 Claude Code | Ex 4 to 6 | 27 slides, 3 edits, 2 added | Script and deck | 10 questions, key, changelog | Yes |
| 3 Debugging and reviews | Ex 7 to 9 | 26 slides, 2 edits, 1 added | Script and deck | 10 questions, key, changelog | Yes |
| 4 Claude API | Ex 10 to 12 | 28 slides, 5 edits, 3 added | Script and deck | 10 questions, key, changelog | Yes |
| 5 Advanced and capstone | Ex 13 to 15 | 26 slides, 3 edits, 2 added | Script and deck | 10 questions, key, changelog | Yes |
| Course intro | Not applicable | Not authored | Not authored | Not applicable | Not applicable |

All 15 lab documents exist as markdown and as generated DOCX. All five vendor decks
are preserved unmodified under each module's `01-deck/original/`.

Assessment answer distribution, the main defect in the vendor set, now checked
mechanically rather than by eye:

| Module | a | b | c | d | Core / Stretch |
|---|---|---|---|---|---|
| 1 | 2 | 2 | 3 | 3 | 7 / 3 |
| 2 | 3 | 2 | 3 | 2 | 7 / 3 |
| 3 | 2 | 3 | 3 | 2 | 7 / 3 |
| 4 | 3 | 2 | 3 | 2 | 7 / 3 |
| 5 | 3 | 2 | 2 | 3 | 7 / 3 |

Starter code, all verified by running it rather than reading it:

| Artefact | Expected result | Verified |
|---|---|---|
| Exercise 1 snippet | `[10.0, 15.0, 20.0]` for four readings | Yes |
| Exercise 7 test suite | 3 failed, two `KeyError` and one assertion | Yes |
| Exercise 7 threshold range | 1 fails, 2, 5 and 7 pass, 8 fails, so 2 to 7 inclusive | Yes, by running the suite against each |
| Exercise 8 baseline | 24326 matches, about 2 to 3 seconds | Yes, 2.23 s on the build machine |
| Exercise 8 set-based trap | Returns 10382, so faster and wrong | Yes |
| Exercise 15 skeleton suite | 3 passed, 1 failed, `assert 502 == 200` | Yes |

### Outstanding work, roughly in order

1. **Push to GitHub.** The repository is committed locally with full history but the
   remote refuses the push, because `zarantechClaude/claude-dev-demo` is not in the
   session's authorised repository set. Nothing is lost, and publishing is one push
   once that is granted.
2. **Archive the vendor PDFs.** Every `vendor-original/` and `04-assessment/original/`
   folder carries a README naming exactly which vendor file belongs in it. The files
   themselves are not in the repository yet: device file access expired during the
   build. Their contents were read through the Claude Project, so the rewrites are
   based on the real documents.
3. **Author the course intro**, about 12 minutes, including the environment
   requirements warning for Modules 2 and 4. This is the largest remaining gap.
4. **Decide the deck round trip** with the vendor content team. Question 10 in
   `docs/open-questions-for-vendor.md`. Until it is answered, the revised PPTX files
   and the Google Slides masters can diverge.
5. **Consolidate the Module 5 evaluation slides.** The new marking-thresholds slide
   was inserted alongside the original adjectives-only slides rather than replacing
   them, so the on-screen order is adjectives, thresholds, adjectives.
6. Resolve the rest of `docs/open-questions-for-vendor.md`.

Items closed during this build, recorded so they are not reopened: the revised decks
and changelogs are committed; the facilitator scripts and decks exist for all five
modules; all five assessments are rewritten with keys and changelogs; every module
has a content-team README; and the `verify_key.py` key-prefix print is fixed, so it
now reports presence and length only, matching what both the lab and the register
claim.
