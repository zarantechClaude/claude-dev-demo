# Exercise 14: Generate and Refine a Configuration File

**Module 5** | **12 minutes** | **You need:** Browser, a text editor

## What you will do

You will generate one configuration file for a specific stack, review it line by line
against a checklist, and correct it. Generating it takes one prompt. The review is the
exercise.

You will not build or run this file. There is nothing to install for this exercise and no
container runtime is required. Config is reviewed by reading, which is exactly how it gets
reviewed on a real pull request, and exactly why bad config reaches production.

## Before you start

1. Claude open in your browser.
2. A text editor.
3. The stack facts from Step 2 written down.

## Steps

### Step 1: Pick one file

Choose one, and only one:

- `Dockerfile`
- `.github/workflows/ci.yml`
- `docker-compose.yml`
- `Makefile`

The steps below use a `Dockerfile` because it is the one where a careless line does the
most damage. Everything transfers. Generating four mediocre files teaches less than
correcting one properly.

### Step 2: Write down the stack facts

This step decides whether the output is usable. Every fact you leave out becomes a guess,
and a guess in config looks exactly like a fact.

Use the capstone service from Exercise 15 as the stack, so the file you produce here is one
you can actually use:

```
Language:   Python 3.11
Framework:  Flask
Packages:   pip with requirements.txt
Install:    pip install -r requirements.txt
Test:       pytest
Start:      python app.py
Port:       5000
Env vars:   ANTHROPIC_API_KEY, MODEL, MAX_CODE_CHARS
Notes:      app.py runs Flask's development server. Production needs a WSGI server.
```

If you would rather use your own project, use it, and write the same nine lines for it
first.

> **Pause the video here.** Write the stack facts down before you prompt.

### Step 3: Compare a weak prompt with a strong one

The weak version, which is what most people send:

```
Write me a Dockerfile for a Python Flask app.
```

Send it. Keep the result. Then send this:

```
Generate a Dockerfile for this service.

Language: Python 3.11
Framework: Flask
Dependencies: pip, from requirements.txt
Test command: pytest
Listens on port 5000
Reads configuration from these environment variables at runtime: ANTHROPIC_API_KEY,
MODEL, MAX_CODE_CHARS

Requirements:
- pin the base image to an explicit version, never a floating tag
- copy requirements.txt and install before copying the application source
- do not run as root
- do not set a value for any of those environment variables in the file
- serve with a production WSGI server, not Flask's development server
```

Put the two results side by side and count the differences. The weak prompt did not
produce a wrong file. It produced a file for a generic Python app, which is a different
and more dangerous thing, because it will build.

Five of those six requirement lines are things you would otherwise have found in review.
The sixth you would have found in production.

### Step 4: Review against the checklist

This is the part to slow down for. Work through the table on the file you generated and
mark each row pass or fix. Read the file top to bottom once first, then take the rows in
order.

| # | Check | Why it matters |
|---|---|---|
| 1 | The base image is pinned to an explicit version, with no floating tag | A floating tag means the image you build next month is not the image you tested |
| 2 | The base image matches the language version you stated | A minor version mismatch surfaces as a dependency failure with no obvious cause |
| 3 | The dependency manifest is copied and installed before the application source | Otherwise every source edit reinstalls every dependency. This is the single most common cause of slow builds |
| 4 | Dependency versions come from the manifest, not typed into this file | Two places to change means one place that gets forgotten |
| 5 | The working directory is set explicitly | Relative paths behave differently depending on where the process starts |
| 6 | The start command is the command you actually use | Generated start commands are plausible and frequently not yours |
| 7 | The start command is not a development server, and does not enable debug mode | A development server with debug enabled exposes an interactive console. This is a security finding, not a performance one |
| 8 | The exposed port matches the port the application listens on | A mismatch produces a container that runs and refuses connections |
| 9 | No secret has a value anywhere in the file | Anything written here is in the image, in the layer history, and in your repository |
| 10 | Environment variables are declared or documented, never assigned | The file should say what is required without supplying it |
| 11 | `.env`, `.venv`, `.git` and caches are excluded from the build context | Otherwise your local key is copied into the image by a wildcard copy |
| 12 | The process does not run as root, or there is a stated reason it does | Container escape is a smaller problem when the escaping process is unprivileged |
| 13 | Nothing in the file exists only on your machine | Absolute paths from your home directory are the usual offender |
| 14 | No placeholder survives | `<your-app-name>` is not a value |
| 15 | A teammate could read it without asking you a question | If it needs a verbal explanation, it needs a comment |

For a CI workflow instead of a `Dockerfile`, swap rows 7, 8, 11 and 12 for these:

| # | Check | Why it matters |
|---|---|---|
| 7 | The test step runs your test command | A workflow that runs the wrong test command reports green and tests nothing |
| 8 | It triggers on both push and pull request | Pull request only means the default branch is unchecked. Push only means a proposed change is unchecked |
| 11 | Secrets come from the platform's secret store, never from the workflow file | A workflow file is as public as the repository |
| 12 | The runtime version is pinned | The default version on a hosted runner changes without telling you |

> **Pause the video here.** Work every row. Write pass or fix next to each one.

### Step 5: Correct the file yourself

Fix every row you marked. Do it by hand rather than by asking for a corrected version,
because at this size editing is faster than reading a regenerated file, and you need to
know exactly what changed for Step 6.

Two of the fixes are usually worth more than the rest. Row 3, because it changes build
time by an order of magnitude on a real project. Row 9, because it is the one that cannot
be undone once committed.

### Step 6: Record what changed, in three columns

| Generated | Changed to | Why |
|---|---|---|

One row per correction. This table is the actual output of the exercise. Read down the
"Why" column and you have the list of things to state in the prompt next time, which is
how the second config file you generate takes half as long to review as the first.

### Step 7: Validate by reading, and save it

Five questions, answered out loud:

1. Would this run in my environment?
2. Does it match my project's structure?
3. Is every placeholder replaced?
4. Would a teammate understand it without me?
5. Is it safe and maintainable?

Config that looks correct while carrying an assumption that does not match your project is
the normal failure mode here. It does not fail on your machine. It fails in CI, or on the
first deploy, or in a security review six months later.

Save the file where it belongs in a project folder and treat it as real, even if the
project is a sample.

## What good looks like

- One configuration file, corrected for a named stack, with every checklist row marked.
- A three column change log with at least four rows.
- No secret value anywhere in the file.
- The base image or runtime version is pinned.
- You can name the one prompt detail that most improved the first draft, and you can point
  at the line in the weak version that proves it.

## Common problems

| Problem | Cause | Fix |
|---|---|---|
| The base image uses a floating tag | Generated config reaches for it by default | Pin it. Row 1 |
| An environment variable has a value in the file | The prompt mentioned the variables, and did not say not to set them | Declare or document only. Row 9 and row 10 |
| The file containerises the development server | It copied the run command from `app.py`, which is a development entry point | Row 7. Add a production server to the dependencies and start with that |
| It looks right and fails in CI | An assumption about the project layout that is true on your machine | Rows 5 and 13. Check every path against your actual tree |
| A wildcard copy pulls in `.env` | No build context exclusions | Row 11. Add the exclusion file, and check it is actually being read |
| `<placeholder>` left in place | Nothing failed, because nothing ran | Row 14. This is why the review is by reading |
| The corrected file is now long and hard to follow | Fifteen fixes applied without tidying | Group related lines and add two comments. Row 15 is a real check |

## Going further

1. Ask for the same file targeting a different environment, one for local development and
   one for production, then diff them. The lines that differ are your actual deployment
   assumptions, written down for the first time.
2. Take the durable rows out of your Step 6 change log and put them in the `CLAUDE.md` you
   wrote in Exercise 4, under a heading for generated configuration. A constraint you have
   to remember to paste is a constraint you will forget on the day it matters.
3. Look at `requirements.txt` in the Exercise 15 capstone skeleton. Nothing in it is
   pinned. Decide whether that is a defect for a teaching repository and whether it would
   be one for a service you operate. The answers are not the same, and being able to say
   why is the judgement this exercise is really about.

Copyright © 2026, ZaranTech LLC. All rights reserved.
