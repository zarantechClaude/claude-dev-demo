# Module 4 labs: Building with the Claude API

Three exercises, 52 minutes of lab time. Exercise numbering is global across the programme,
not per module, so Module 4 runs from Exercise 10 to Exercise 12.

Module 4 is the first module that needs an API key. Modules 2 and 3 needed a terminal but no
credentials. State that step change in the course intro, because a learner who reaches
Exercise 10 without an account cannot start it, and unlike a missing package it is not
something they can fix in thirty seconds.

## Exercises

| Ex | Title | Duration | You need | Starter code | Videos |
|---|---|---|---|---|---|
| 10 | [Configure API keys and send your first prompt](exercise-10-env-keys/lab.md) | 12 min | Terminal, API key | `exercise-10-env-keys/starter/verify_key.py` and `minimal_call.py` | 1 |
| 11 | [Build a CLI for structured prompting](exercise-11-cli-or-rest/lab.md) | 22 min | Terminal, API key | `exercise-11-cli-or-rest/starter/cli_reference.py` | 2 |
| 12 | [Manage minimal conversation history](exercise-12-conversation-history/lab.md) | 18 min | Terminal, API key | `exercise-12-conversation-history/starter/history_starter.py` | 1 |

## Environment

| Requirement | Needed |
|---|---|
| Browser | Yes |
| Terminal | Yes |
| Claude Code | No |
| API key | Yes |

Python 3.11 or later. Python only, across the whole programme.
`pip install anthropic python-dotenv` covers all three exercises. Nothing else is needed.

Exercise 10 sets up the `.env` that Exercises 11, 12 and 15 all read. It is the only
exercise in the module that cannot be skipped.

## What each exercise is actually teaching

Useful when writing the recording script, because in all three cases the stated topic and
the real lesson are not the same thing.

1. **Exercise 10** teaches that a credential is configuration and a model identifier is
   configuration, and that both belong outside the code for the same reason. The secondary
   lesson is the habit of never printing a secret, not even truncated. `verify_key.py`
   reports presence and length and nothing else, and the lab says why in one paragraph. The
   third thing it does is show the raw headers exactly once, so that a learner debugging a
   401 later knows what the SDK had been setting for them.
2. **Exercise 11** teaches that a boundary needs both a marker and a rule. Tags around user
   input with no system instruction explaining what the tags mean are decoration. The lab
   builds the weak template first, then the strong one, then attacks both with the same two
   inputs and compares four answers. It also closes honestly: structured prompting raises
   the cost of an injection and does not eliminate it, and the defence you ship is not
   trusting the output.
3. **Exercise 12** teaches that recency is a poor proxy for importance, and it teaches it by
   letting the learner lose a real constraint. The starter conversation is built so that a
   sliding window of the last three messages keeps repo-naming chatter and drops two
   decisions that the current request depends on. The learner writes down every decision in
   the conversation *before* implementing anything, implements the naive window, sends it,
   and then checks the answer against their own list. The lab never says which messages
   matter.

## Sequencing note

Exercises 10, 11, 12 and 15 form a hard chain, documented in `docs/programme-map.md`.
`ANTHROPIC_API_KEY` and a `MODEL` read from the environment are the two things that hold it
together. Renaming either one in any single lab breaks everything downstream, which is
exactly what the vendor pack did.

`history_starter.py` exists so that Exercise 12 does not hard-depend on a finished Exercise
11. It carries the conversation and the topic shift already built, so the learner can
practise the skill being taught, which is selection, without first having to finish a CLI.
Keep it that way, and keep the lab written so it works from the starter either way.

## Deck alignment

Terminology in these labs matches the Module 4 deck: authentication, model selection,
environment variables, request and response flow, prompt engineering in code, system versus
user instructions, structured prompt templates, dynamic variables, tokens and truncation,
long context, context management, preserving conversation state, and passing code snippets.

Two deck statements are wrong as written and the labs correct them silently. Fix them in the
revised deck and record both in `deck-changelog.md`.

1. Slide 4 says "requests require specific endpoints depending on the chosen model and
   task". There is one messages endpoint, `POST https://api.anthropic.com/v1/messages`, and
   the model is a field in the request body. Exercise 10 shows the single endpoint in a raw
   `curl` call and says explicitly that a URL built per model is a sign something has gone
   wrong.
2. Slide 5's narration describes authentication as "the standard HTTP authorization header".
   The documented primary is an `x-api-key` header. An `Authorization` header is also
   accepted, but teaching it as the default sends a learner looking for the wrong thing when
   they read someone else's integration. Exercise 10 shows `x-api-key` alongside the
   required `anthropic-version` header, once, and then returns to the SDK.

Slide 6's model tier discussion is fine as it stands. Tier names are not version names, and
the tier-selection habit is what the programme teaches in place of a specific identifier.

Slide 20 and 21 cover MCP. No lab in this module touches it, and that is a deliberate scope
decision rather than an omission. If it stays in the deck it needs to be framed as context
for later work, not as something the learner is about to do.

## Vendor lab defects corrected in these rewrites

All fixed silently in the learner-facing text. Listed here because a reviewer comparing the
rewrite against the vendor PDF will otherwise read them as unexplained divergence.

| Vendor | Problem | Now |
|---|---|---|
| Ex10 Step 6 | Hardcodes a model identifier | `MODEL` read from `.env`. The step is to look up a current identifier in the official documentation |
| Ex10 Step 7 | `print(os.getenv("ANTHROPIC_API_KEY"))` | `verify_key.py`, which reports presence and length only. Printing a key is a recording hazard and the lab says so |
| Ex11 Step 2 | Switches the variable to `CLAUDE_API_KEY` | `ANTHROPIC_API_KEY` everywhere, with an explicit warning in the lab about what renaming breaks |
| Ex11 prerequisites | Python, Node and Postman variants | Python and `curl` only |
| Ex12 prerequisites | Hard-depends on "a working Claude API project from the previous module" | Works from `history_starter.py` regardless of whether Exercise 11 was finished |
| All three | No duration stated | Duration in the header of each, and honest |
| All three | Written to the trainer, in the third person about learners | Second person to the learner, with explicit pause instructions |

## Conventions for anyone editing these labs

1. `docs/lab-authoring-spec.md` governs structure, voice and prompt handling. Match it
   exactly. Fifteen labs should read as one programme.
2. `lab.md` is the source of truth. The DOCX is generated from it.
3. `ANTHROPIC_API_KEY` and `MODEL`, everywhere, with no exceptions and no second names.
4. Never name a Claude model version. If a step needs an identifier, the step is to look one
   up in the official documentation.
5. Never print, echo or log a key value, and never a truncated one either. A prefix on a
   screenshot is still a leaked prefix.
6. Do not name which messages in `history_starter.py` carry the constraints. The learner
   finding that out is the entire exercise.
7. No em dashes.
