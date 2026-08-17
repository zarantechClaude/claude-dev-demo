# Exercise 5: Build, Refactor and Review a Registration Endpoint

**Module 2** | **20 minutes** | **You need:** Terminal, Claude Code

## What you will do

You will make three passes over one small feature. You will draft it clean from a
user story, refactor a messy version of the same endpoint, and annotate what
changed and why. The refactor is the part worth your attention, because a refactor
prompt that reads perfectly well can still hand you a change you cannot ship.

This lab is recorded in two videos. Part 1 ends the first video. Part 2 and Part 3
are the second.

## Before you start

1. Claude Code running in your clone of the course repo.
2. Open `module-2-claude-code/03-labs/exercise-05-registration-endpoint/starter/messy_registration.py`
   in your editor so you can see it.
3. Optional: `pip install flask` if you want to run the file. Reading it is enough
   for this exercise.

## The user story

> As a new user, I want to register for an account by sending my name, email and
> password to an API endpoint, so that I can create a secure account.

Narrowed to something a single exercise can hold:

- Endpoint: `POST /api/register`
- Required fields: name, email, password
- Behaviour: validate the input, hash the password, return success or a structured
  error

## Steps

## Part 1: Draft it

### Step 1: Prompt from the story

```
Draft a clean API endpoint for user registration from this user story:

As a new user, I want to register for an account by sending my name, email and
password to an API endpoint, so that I can create a secure account.

Use Flask. Include input validation on all three fields, password hashing, and a
JSON response with a consistent shape for both success and error. Standard library
plus Flask and one password hashing library only.
```

Save the result as `register_draft.py` in the exercise folder. You need it for the
comparison in Part 2.

### Step 2: Check the draft against five things

1. The route and the method match the story.
2. All three fields are validated, not just one.
3. The password goes through a named password hashing function rather than a plain
   digest.
4. The response shape is the same in the success branch and in every error branch.
5. The names tell you what the code does.

Point three earns a moment. Ask for registration code without mentioning hashing at
all and you will often get plain text storage. The constraint in your prompt is what
prevented that, not the model's good judgement.

> **Pause the video here.** Generate the draft, save it, and score it against those
> five points before you continue. This is the end of the first video.

## Part 2: Refactor the messy version

### Step 3: Read the messy version yourself, first

Open `starter/messy_registration.py`. It works. It is also one function doing
routing, validation, hashing, database access and response formatting, with
single-letter names and a validation branch repeated five times.

Find as many problems as you can before you prompt anything. Aim for eight. There
are more than eight.

Write them in a list you can check off later, because you are going to compare your
list against what the refactor actually addressed, and against what it changed
without being asked.

> **Pause the video here.** Read the file and write your list. Do not prompt yet.

### Step 4: Ask for the refactor

This is the prompt most developers send, near enough word for word.

```
Refactor this endpoint into cleaner, modular code. Separate responsibilities,
remove repetition, and keep it secure and maintainable.
```

Save the result as `register_refactored_v1.py`.

### Step 5: Check what the refactor actually did

Put the original and `register_refactored_v1.py` side by side. Work through the
structural improvements first, which is the easy part:

- Smaller functions, one job each
- Validation extracted into a helper
- Persistence separated from request handling
- One consistent error shape
- Names you can read

Now the part that matters. Go back through the diff line by line and answer a
different question for every change you find:

**Is this a structural change, or is it a change in behaviour?**

A structural change moves code around. A behaviour change alters what the endpoint
does, what it stores, or what it returns. Both can be improvements. Only one of them
can break something outside this file.

For every behaviour change you find, ask the two questions that a reviewer would ask:

1. Could a row already written to the database by the old code notice this change?
2. Could a client already calling this endpoint notice this change?

> **Pause the video here.** List every behaviour change in the refactor, and answer
> both questions for each one. Take the full two minutes. Do not skip to Step 6.

### Step 6: Check the change against the data that already exists

You now have a list of behaviour changes. Test the most significant one against
reality rather than against the file.

```
Assume the users table already holds 40,000 rows written by the original version of
this endpoint, and that a separate login endpoint reads those rows to authenticate
people.

Walk through, step by step, what happens to one of those existing users the next
time they try to log in against your refactored version. Then state plainly whether
any of them can still log in.
```

Read that answer carefully. If a change to one file can lock 40,000 people out of
their accounts, the prompt that produced it was not a refactor prompt, whatever it
said.

This is worth being precise about, because the change is not wrong. It is very
probably a correct improvement, and a reviewer who blocked it outright would also be
wrong. It is a correct improvement that cannot ship on its own. It needs a migration
path, and the prompt never asked for one.

### Step 7: Refactor again, with a preservation constraint

The difference between Step 4's prompt and this one is the whole lesson of the
exercise. Same file, same model, same request for cleaner code.

```
Refactor this endpoint into cleaner, modular code. Separate responsibilities,
remove repetition, and keep it secure and maintainable.

Preservation constraints. These are not negotiable:
- Existing rows in the users table were written by this code and must remain
  verifiable. Do not change the stored credential format in a way that invalidates
  them.
- If you believe the credential handling should change, do not change it. Instead,
  describe a migration path that upgrades a stored credential on the user's next
  successful login, and leave the current path working until then.
- Do not change the route, the HTTP methods, the request field names, the response
  field names, or the status codes.
- List every remaining behaviour change separately at the end, under the heading
  BEHAVIOUR CHANGES, so I can review them individually.
```

Save the result as `register_refactored_v2.py`.

Name that pattern, because it recurs. A **preservation constraint** states what must
survive the change. Without one, "refactor this" is heard as "rewrite this", and
rewrites break callers. You will use the same pattern again in Exercise 8, on
performance rather than security.

### Step 8: Check the second result

- The route, the field names, the response keys and the status codes are unchanged.
- Existing stored credentials still work.
- Any credential upgrade is described as a migration, not performed as a swap.
- There is a `BEHAVIOUR CHANGES` section, and you agree with every item in it.
- The structural improvements from Step 5 are still present. A preservation
  constraint should not have cost you the clean code.

> **Pause the video here.** Run the Step 7 prompt and check all five.

## Part 3: Annotate

### Step 9: Mark the improvements

Add a short change log at the top of `register_refactored_v2.py`, or inline comments
if you prefer. One line each. Group them under two headings, `SAFE` and
`BEHAVIOUR CHANGE`, and put every item under one of them.

### Step 10: State the impact of each

One line each: how it improves readability, maintainability, or risk. If you cannot
state the benefit of a change, it may not have been worth making, and that is a
legitimate review finding to raise about your own work.

Then write two sentences at the bottom answering this: if you had shipped
`register_refactored_v1.py`, when would you have found out?

## What good looks like

- `register_draft.py`, `register_refactored_v1.py` and `register_refactored_v2.py`
  all exist in the exercise folder.
- You can name at least eight problems in the original file.
- You can point at the line in `register_refactored_v1.py` that would have caused an
  incident, and explain why it is a good idea and still unshippable on its own.
- `register_refactored_v2.py` keeps the route, field names, response keys and status
  codes of the original, and its `BEHAVIOUR CHANGES` list is short and reviewed.
- Every change in your change log is marked `SAFE` or `BEHAVIOUR CHANGE`.

## Common problems

| Problem | Cause | Fix |
|---|---|---|
| The refactor looks clean and you find no behaviour changes | You compared the shape of the code rather than the diff | Diff the two files line by line and ask what each changed line does at runtime |
| Step 6's answer is reassuring and vague | The prompt let it answer in principle | Re-ask with the 40,000 rows and the login endpoint stated explicitly, and demand a plain yes or no |
| The v2 refactor is clean but the response keys changed | Preservation constraints were pasted as a suggestion, not as a rule | Keep the "These are not negotiable" line, and name the exact keys that must not change |
| v2 lost the structural improvements | The constraint list was read as "change nothing" | Add one line: "The structural refactor should be as thorough as before" |
| You cannot run the file | Flask not installed | `pip install flask`, or read rather than run. Reading is enough here |

## Going further

1. Ask for the migration path from Step 7 as real code, then ask what happens to a
   user who never logs in again. Some answers to that question are policy decisions,
   not engineering ones, and it is worth knowing which.
2. Take the preservation constraint block and move the durable parts of it into the
   `CLAUDE.md` you wrote in Exercise 4. A constraint you have to remember to paste is
   a constraint you will forget on the day it matters.

Copyright © 2026, ZaranTech LLC. All rights reserved.
