# Exercise 10: Configure API Keys and Send Your First Prompt

**Module 4** | **12 minutes** | **You need:** Terminal, API key

## What you will do

You will get a key into an environment file, prove it loaded without ever putting it
on screen, and get one reply back from the API. This is the setup exercise for the
rest of the programme, so the order of the steps matters more than it looks.

## Before you start

1. An API key from your own account. Use one you are willing to rotate, and set a
   spend cap on it. That is good practice generally, and specifically relevant while
   anything is recording your screen.
2. Python 3.11 or later.
3. A terminal. This is the first exercise in the programme that needs one for an API
   call. Modules 2 and 3 needed the terminal but not a key.

## Steps

### Step 1: Work in the starter folder

```bash
cd module-4-claude-api/03-labs/exercise-10-env-keys/starter
```

Two files are already there: `verify_key.py` and `minimal_call.py`. You will run both
and edit neither.

### Step 2: Create a virtual environment and install two packages

macOS or Linux:

```bash
python3 -m venv .venv && source .venv/bin/activate
```

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Then:

```bash
pip install anthropic python-dotenv
```

`anthropic` is the official SDK. `python-dotenv` reads a `.env` file into the process
environment.

### Step 3: Write `.gitignore` before you write `.env`

```bash
echo ".env" > .gitignore
```

This step is deliberately before the next one. A key committed once is a key you have
to rotate, and deleting it in the following commit does not help, because it is still
in the history. Doing this in the other order works every time except the time it
does not.

### Step 4: Create `.env` with the key

Create a file called `.env` in this folder:

```
ANTHROPIC_API_KEY=your_key_here
```

No spaces around the equals sign. Use exactly that variable name. The SDK reads
`ANTHROPIC_API_KEY` from the environment by default, and every later exercise in the
programme assumes it. Renaming it here breaks Exercises 11, 12 and 15.

### Step 5: Add a model id, and understand why it is configuration

Open the official Anthropic documentation, find the current list of model identifiers,
and pick one. Add it to `.env` as a second line:

```
MODEL=the_model_id_you_looked_up
```

Look it up rather than copying one out of a tutorial. Model identifiers are the detail
that goes stale fastest, and a stale one produces an error that reads like an
authentication problem.

Both scripts in this folder read `MODEL` from the environment and refuse to run without
it. That is on purpose. A model id hardcoded in a script becomes a hardcoded model id in
forty scripts, and there is then no single place to change it.

> **Pause the video here.** Create both files and fill in both values before you run
> anything.

### Step 6: Prove the key loaded, without printing it

```bash
python verify_key.py
```

Read what it reports. It tells you the key was found and how long it is. It does not
print the key, not even the first few characters, and you should hold to that habit in
your own scripts. A truncated key on a screenshot, in a log aggregator, or in a
recording is still a leaked prefix, and it is enough to correlate with a full key
somewhere else. Presence and length answer the only question you actually have, which
is whether the file loaded.

If it fails, it tells you which of four things to check. Work through them in order.

### Step 7: Send the call

```bash
python minimal_call.py
```

Open the file and read it while the reply prints. Five things happen: load the
environment, read two values, fail loudly if either is missing, build a request, print
the text of the response.

Notice `max_tokens=300` and the comment next to it. `max_tokens` caps the length of the
output. It does not ask for a short answer. If you want brevity, ask for it in the
prompt. If you want a hard ceiling, use `max_tokens`. Confusing the two gives you
answers that stop mid-sentence, which is a common and avoidable bug.

> **Pause the video here.** Get a reply printed in your terminal before continuing.

### Step 8: Look once at what the SDK is doing for you

You will not write raw HTTP in this programme, but you will one day debug a 401, and
then you need to know what the SDK was setting on your behalf.

```bash
set -a; . ./.env; set +a

curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d "{\"model\": \"$MODEL\", \"max_tokens\": 32, \"messages\": [{\"role\": \"user\", \"content\": \"Reply with exactly: OK\"}]}"
```

Three facts worth keeping, all of them visible in that command:

1. The key goes in an **`x-api-key`** header. An `Authorization` header is also
   accepted, but `x-api-key` is the documented primary and it is what you should reach
   for first when reading someone else's integration.
2. A raw call needs an **`anthropic-version`** header. Leave it out and the request
   fails in a way that has nothing to do with your key.
3. There is **one messages endpoint**, `POST https://api.anthropic.com/v1/messages`.
   The model is a field in the request body, not part of the URL. If you find yourself
   building a URL per model, something has gone wrong.

The first line of that block matters too. `python-dotenv` loads `.env` into your Python
process, not into your shell, so `curl` cannot see those values until you export them.
Learners lose several minutes to that every cohort.

Then go back to the SDK, which sets all three headers for you and reads
`ANTHROPIC_API_KEY` without being told to.

### Step 9: Change the prompt and run it again

Edit the prompt text in your own copy, or set a different question, and run once more.
The plumbing is now done and reusable, which is the actual deliverable of this exercise.

## What good looks like

- `verify_key.py` reports the key loaded and the call succeeded.
- `minimal_call.py` prints a reply.
- `.gitignore` exists, contains `.env`, and was created first.
- Your key appears in `.env` and nowhere else. Not in a script, not in your shell
  history, not in any output you produced.
- `MODEL` is set in `.env` and hardcoded in nothing.
- You can say what `max_tokens` controls and what it does not.

## Common problems

| Problem | Cause | Fix |
|---|---|---|
| `FAIL: ANTHROPIC_API_KEY not found` | `.env` is not in the folder you ran from, the name is misspelled, or there are spaces around the `=` | Work through the four checks the script prints, in order |
| `FAIL: set MODEL in your .env` | `MODEL` is missing | Look up a current model identifier in the official documentation and add it to `.env` |
| `ModuleNotFoundError: dotenv` or `anthropic` | Installed outside the active virtual environment | Re-activate the environment and install again. Check your prompt shows `.venv` |
| The call fails and the key is definitely right | Revoked key, no credit on the account, or an unrecognised `MODEL` value | Change one variable at a time. Try a different model id before you rotate the key |
| A raw `curl` call returns 401 but the SDK works | Missing `x-api-key`, or you used a header the SDK was setting for you | Compare your headers against Step 8. Check `anthropic-version` is present |
| A raw call returns 404 | You built a URL that includes the model | One endpoint. The model is a body field |
| `curl` sends an empty key | You expected `.env` to be visible to your shell. It is not | Run the `set -a; . ./.env; set +a` line first |
| The reply stops mid-sentence | `max_tokens` too low for the answer you asked for | Raise the ceiling, or ask for a shorter answer in the prompt. Those are different fixes |

## Going further

1. Delete `MODEL` from `.env` and run both scripts again. Read the two failure messages.
   A script that fails with a sentence telling you what to set is worth the four lines it
   takes to write, and you will copy this pattern into your own work.
2. Add a `.env.example` next to `.env`, holding the same two variable names with empty
   values, and commit that. It is the file that tells the next person what to configure
   without telling them your key.

Copyright © 2026, ZaranTech LLC. All rights reserved.
