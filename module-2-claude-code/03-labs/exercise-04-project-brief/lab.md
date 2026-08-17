# Exercise 4: Create a Project Brief for Claude Code

**Module 2** | **12 minutes** | **You need:** Terminal, Claude Code, a small project of your own

## What you will do

You will end this exercise with a project context file at the root of a repository,
which Claude Code loads by itself at the start of every session, and you will have
proved it works by asking Claude Code to describe the project back to you before
you request a single line of code.

## Before you start

1. Claude Code installed and launching from your terminal. Module 1 was browser
   only. This is the first exercise that needs a local install.
2. A small project of your own, roughly 3 to 10 files. A folder with two scripts
   and a `requirements.txt` is enough. If you do not have one, create one now:
   a folder, two short Python files, and a `requirements.txt` with one line in it.
3. A text editor.

Do not use your clone of this course repo as the practice project. It already has
a context file at its root, and you want to see the effect of writing one yourself.
You will read the course repo's file later, in Step 6, as a worked example.

## Steps

### Step 1: Start Claude Code inside the project

Change into your project folder and start Claude Code there.

```bash
cd path/to/your-project
claude
```

Notice what you did not do. You did not upload a folder. You did not paste files
into a chat window. Claude Code reads the working directory directly. If your only
experience so far is the browser workflow from Module 1, that is the habit to
unlearn, and this is the step where you unlearn it.

> **Pause the video here.** Get Claude Code running inside your own project folder
> before you continue.

### Step 2: Find out what it can already see

Send this as your first prompt.

```
Describe this project from the files you can see. List the language, the entry
point, and the test setup. Then list separately the things you cannot determine
from the files alone.
```

The first list is usually accurate. Read the second list closely, because those
items are exactly what your context file has to supply. Typical entries are the
purpose of the project, the conventions the team follows, and which parts of the
codebase are not yours to change.

> **Pause the video here.** Write down the second list. It is the outline of the
> file you are about to write.

### Step 3: Understand why a file beats a pasted message

You could paste all of that into the chat as a first message, and it would work
for the length of that conversation. A file at the repo root does three things a
pasted message cannot.

| | Pasted message | File at the repo root |
|---|---|---|
| Next session | Gone. You retype it, or you skip it. | Loaded automatically, no action from you. |
| Change history | None. You cannot see how the brief drifted. | Version controlled. Diffed and reviewed like code. |
| Your team | Only you have it. | Everyone who clones the repo has it. |

The first row is the one that decides the outcome in practice. A brief you have to
retype every session is a brief you will stop writing by Thursday.

### Step 4: Write the context file

Claude Code reads a file named `CLAUDE.md` at the root of the working directory at
the start of every session. Create it now, at the root of your practice project,
and keep the whole thing under one page.

```markdown
# <project name>

## What this is
One sentence on the problem it solves, in business terms, not code terms.

## Tech stack
Language and version, frameworks, test runner.

## Layout
The three or four folders that matter and what lives in each.

## What already works
So nobody rebuilds it.

## Conventions
Naming, formatting, error handling, anything a new contributor would guess wrong.

## Do not change
Named paths and named behaviours that are off limits.
```

One rule governs what goes in this file. Durable facts go in the file. The current
task goes in the prompt. "This is a Flask API using pytest" belongs in the file.
"Add pagination to the orders endpoint today" does not, because it is false by
tomorrow and a stale instruction is worse than a missing one.

> **Pause the video here.** Write your file, all six headings, and save it at the
> project root.

### Step 5: Verify before you request any work

Exit Claude Code and start it again, so the file is loaded fresh. Then:

```
Read the project context file at the repo root. Summarise your understanding in
five lines: purpose, stack, layout, conventions, and what you must not change.
Then stop and wait for my request.
```

Check five things in the answer.

1. Did it get the purpose, in your words rather than generic ones?
2. Did it get the stack, including the version?
3. Did it get the layout?
4. Did it repeat your conventions back specifically?
5. Did it acknowledge the boundaries?

If any one of them is wrong or vague, the file is at fault, not the model. This is
the check that makes the difference between a brief that reads well and a brief
that works.

> **Pause the video here.** Restart the session, run the prompt, and score the
> answer against those five points.

### Step 6: Fix what it missed, then read a real one

Add the specific detail that was missing. The additions that pay off are almost
always boundaries rather than background.

- Do not add a dependency without asking first.
- Keep the existing folder naming scheme.
- Python only. Do not add a Node or Java variant.
- Do not modify anything under `starter/`.

Now open the course repo's own file, `CLAUDE.md` at the root of your clone, and
read the section headed "Critical convention: intentional defects". That paragraph
is the most valuable one in the file, because without it any capable assistant
would helpfully repair the teaching material and destroy the course.

Two things to notice about that file. It carries conventions and a do-not-touch
list. It carries no current task, because the task changes every session.

> **Pause the video here.** Compare the course repo's file against yours and add
> the one boundary you now realise you are missing.

## What good looks like

- `CLAUDE.md` exists at the root of your practice project, under one page, with all
  six headings filled in.
- You restarted the session, and Claude Code described your project correctly
  without you pasting anything.
- At least one boundary in the file names a specific path or behaviour, not a
  general wish.
- You can say, for any note you took in Step 2, whether it belongs in the file or
  in a prompt.

## Common problems

| Problem | Cause | Fix |
|---|---|---|
| Claude Code seems to ignore the file | It is not at the root of the working directory, or the session started before you saved it | Move it to the project root, exit, and start Claude Code again |
| The summary is accurate but generic | The file describes the stack and never states the purpose | Add one sentence on what problem the project solves and who for |
| Claude Code keeps changing things you did not ask about | No boundaries in the file | Add a "Do not change" section naming specific paths |
| The file keeps growing and nobody reads it | Task detail leaked into it | Move anything that is false next week into the prompt |
| The five-point check passes but real work still goes wrong | The conventions section is aspirational rather than descriptive | Write what the code actually does today, then fix the code separately |

## Going further

1. Add one line stating the exact command that runs the tests, then ask Claude Code
   to run them. Watch whether it uses your command or invents one.
2. Commit the file and ask a colleague to review it the way they would review code.
   Review comments on a context file are usually more useful than review comments on
   the code it governs.

Copyright © 2026, ZaranTech LLC. All rights reserved.
