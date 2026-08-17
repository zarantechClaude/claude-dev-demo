# Module 4: Building with the Claude API
## Guidance for the content team

**Runtime:** 87 minutes across 11 videos  |  **Deck:** 25 slides in, 28 out  |  **Exercises:** 10, 11 and 12

This is the first module that needs an API key with credit, and it is the highest
risk module to record, because a live key is on screen. Read
`docs/recording-hygiene.md` before working on it.

It also had the most factually wrong slides and the worst assessment mismatch in the
programme. Both are fixed.

## What changed from the delivered material, and why

### Deck, five edits and three new slides. Two edits are factual corrections

Verified against the official API documentation, not from memory:

1. **Slide 4 said requests require different endpoints depending on the model.**
   There is a single messages endpoint and the model is a parameter in the request
   body. A learner following the original slide would have gone looking for
   per-model endpoints that do not exist.
2. **Slide 5 said to pass the key in "the standard HTTP authorization header".**
   The documented primary is `x-api-key`. An `Authorization` header is also accepted,
   so the original was not flatly wrong, but it was misleading as a teaching default
   and it omitted the `anthropic-version` header that raw HTTP calls also require. A
   learner debugging a 401 needs both facts.
3. **Slide 6** now anchors tier selection to configuration, because tier names persist
   across releases and version identifiers do not.
4. **Slides 22 and 23 described an activity requiring three sample architectures that
   were never supplied.** Rewritten to use artefacts that exist: the Exercise 11
   reference implementation and the learner's own capstone design.

### The assessment mismatch, now fixed at the source

The vendor Module 4 assessment tested **four topics the deck never taught**: prompt
caching, assistant prefill, the alternating-roles requirement, and the system prompt
as a top-level parameter. That is 40 percent of the assessment untaught.

Rather than delete the questions, three of the four are now taught, on two new slides:

- **Reusing a Stable Prefix: Prompt Caching**, revised slide 22. Worth teaching on
  its own merits, since it is the main cost lever for a large fixed context.
- **Shaping the Response**, revised slide 13, covering prefill and the
  alternating-roles requirement.

The fourth, the system prompt as a top-level parameter, was already covered, so that
question was always fair.

### Labs

- **Exercise 10 hardcoded an outdated model identifier.** No script in this repository
  hardcodes a model id. They read `MODEL` from configuration and fail with a clear
  message if it is unset.
- **Exercise 11 switched the key variable to `CLAUDE_API_KEY` while Exercise 12 depends
  on Exercise 11.** That broke the chain. `ANTHROPIC_API_KEY` everywhere now.
- **Exercise 12 hard-depended on a finished Exercise 11.** `history_starter.py` is the
  fallback, so the lab works either way.

## Do not undo these

1. **No lab step prints an API key, not even truncated.** `verify_key.py` reports
   presence and length only. A truncated key in a screenshot or a log aggregator is
   still a leaked prefix. An earlier version of that script printed a seven-character
   prefix while two documents claimed it did not, which would have had the trainer
   reading a false statement on camera. Do not reintroduce it.
2. **Exercises 10, 11, 12 and 15 are a dependency chain.** Change the environment
   variable name or the model configuration convention in one and you break the rest.
3. **Exercise 12 has a two-layer designed lesson.** The two real constraints sit
   outside the last three messages and the noise sits inside it, so a naive recency
   window loses both. A naive keyword filter also fails, because the current request
   shares no useful vocabulary with either constraint. Both failures are deliberate.
   The comments naming which messages are signal were removed from the starter file
   because the lab tells learners to open it. Do not put them back.

## What is in this folder

| Path | What it is | Who edits it |
|---|---|---|
| `01-deck/original/` | The vendor deck exactly as delivered. Untouched. | Nobody. It is the baseline a change is diffed against. |
| `01-deck/revised/` | The corrected deck. | You, or nobody, depending on your answer to the question below. |
| `01-deck/deck-changelog.md` | Every change, with the old wording, the new wording and why. Generated from the same declaration that made the edits, so it cannot drift. | Generated. Do not hand-edit. |
| `02-facilitator/recording-script.md` | What the trainer reads while recording. Per video: runtime, what is on screen, narration guidance, take-two risks. **Trainer only.** | The trainer, or you with the trainer. |
| `02-facilitator/*.pptx` | The teleprompter deck, generated from that script. **Trainer only, names planted defects.** | Generated from the script. Edit the script. |
| `03-labs/exercise-NN-*/lab.md` | The learner handout. Source of truth. | You. |
| `03-labs/exercise-NN-*/lab.docx` | Generated from `lab.md`. | Nobody. Edits here are lost on the next generation. |
| `03-labs/exercise-NN-*/starter/` | Starter code. Read the warning below. | Nobody, without reading the defect register first. |
| `04-assessment/assessment.md` | Ten self-check questions, no answers. | You. |
| `04-assessment/answer-key.md` | Answers, Core or Stretch tag, where each is taught, and what a wrong answer diagnoses. **Trainer only.** | You, in the same commit as the questions. |
| `04-assessment/changelog.md` | What changed from the vendor assessment, question by question. | You. |

## The one rule that matters most

**The code in `starter/` is deliberately broken. Do not fix it.**

Every such file carries a `# TEACHING ARTEFACT - DO NOT FIX` header. The bugs are
the teaching material. A well-meaning cleanup pass destroys the exercise, and it
will not be obvious from the diff that anything was lost.

Before touching any starter file, read `docs/lab-defect-register.md`. It records
every planted defect, why it is there, and what a learner is supposed to discover.
If you genuinely need a corrected version of a file, add a sibling suffixed
`_solution.py` and leave the original alone.

The answer-revealing comments were removed from these files deliberately, because
the labs tell learners to open them. Do not put explanatory comments back.

## Before you change anything here

1. Read `CLAUDE.md` at the repository root. It carries the writing conventions,
   including no em dashes, no model version names anywhere, and the approved
   ZaranTech statistics.
2. Read `docs/course-context.md`. It explains why the programme is shaped this way,
   including the decisions you might otherwise reverse by accident.
3. If you are editing a lab, read `docs/lab-authoring-spec.md`. It governs structure,
   voice and how prompts are presented.
4. If you are editing the assessment, read `docs/assessment-spec.md`. The answer
   distribution rule is mechanical and it is the main thing being fixed.
5. Regenerate, do not hand-edit, anything marked generated above.

## Questions only you can answer

The full list is in `docs/open-questions-for-vendor.md`. The one that blocks the
deck work is this: **are the Google Slides decks your live master?**

If they are, apply the changes from `deck-changelog.md` in Slides and ignore the
revised PPTX entirely. If you would rather adopt the revised PPTX, import it and it
becomes the master. Doing both will produce two diverging decks, which is worse than
doing neither.
