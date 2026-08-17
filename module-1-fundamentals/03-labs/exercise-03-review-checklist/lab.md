# Exercise 3: Code Review Checklist

**Module 1** | **15 minutes** | **You need:** Browser

## What you will do

You will apply a ready three-part review checklist to a file that was generated
from a vague prompt, record evidence against every item, compare your review
against Claude's, and reach a production-readiness verdict you can defend.

## Before you start

1. A Claude account, signed in, in a browser.
2. The starter file open in a second tab or in a text editor:
   `module-1-fundamentals/03-labs/exercise-03-review-checklist/starter/order_sync.py`
3. A note file, or a copy of the checklist tables below, to mark up.

Two working habits before you paste anything anywhere:

- Never paste a real credential, token or customer record into any tool. If a
  file you are about to paste contains something that looks like one, replace it
  with `<REDACTED>` in the copy you paste.
- The comment block at the top of the starter file is course metadata. The
  exercise is the code below it.

## Steps

### Step 1: Read the file once without judging it

Open `starter/order_sync.py` and read it end to end. Answer three questions in
your notes before you evaluate anything:

1. What does this code do?
2. What inputs does it expect?
3. What does it produce or change?

This file runs, it is short, and it reads cleanly. That is exactly what makes it
worth reviewing properly rather than skimming.

> **Pause the video here.** Read the file and answer the three questions before
> you resume.

### Step 2: Take the intended use as given

You cannot judge code without knowing where it sits, so assume the following:

| Fact | Value |
|---|---|
| Caller | A nightly internal admin job |
| Purpose | Refresh a local cache of orders for a list of user email addresses |
| Volume | About 5,000 email addresses per run |
| Data store | A local SQLite database |
| Upstream | An internal HTTP orders API |
| Deployment | Runs on a shared build server, logs shipped to a central log tool |

Write those down next to your checklist. The volume figure and the log
destination both change how you mark specific items later.

### Step 3: Mark the checklist yourself, before you ask Claude

Work through the three sections below. For each item record a verdict of Pass,
Fail or Needs review, plus evidence. Evidence means a line number or the specific
construct you are pointing at. If you cannot name evidence, the verdict is Needs
review, not Fail.

**Quality**

| Item | Verdict | Evidence |
|---|---|---|
| Names are clear and describe what the value is | | |
| Errors and failure paths are handled explicitly | | |
| Edge cases are handled, including empty and missing data | | |
| Responses from external systems are validated before use | | |
| The function can be tested without live dependencies | | |

**Security**

| Item | Verdict | Evidence |
|---|---|---|
| No credentials, keys or tokens in the source | | |
| Input is validated before it is used | | |
| Database queries are parameterised, never assembled by string building | | |
| Sensitive or personal data never reaches logs | | |
| Access and trust assumptions about upstream systems are stated and safe | | |

**Performance**

| Item | Verdict | Evidence |
|---|---|---|
| No work inside a loop that could be done once outside it | | |
| No per-iteration setup that could be reused | | |
| Writes and network calls are batched where the volume warrants it | | |
| Resources are released reliably, including on failure | | |
| Suitable for the volume stated in Step 2 | | |

Do this pass on your own first. If you read Claude's review first, you will mark
the checklist against its findings rather than against the file.

> **Pause the video here.** Complete every row with evidence before you
> resume. This is the longest step in the exercise.

### Step 4: Ask Claude to review the same file against the same checklist

Start a new conversation. Paste the checklist items and then the code, with this
instruction:

```
Review the Python file below against the checklist that follows it.

Return one row per checklist item, as a table with these columns: item, verdict
of Pass, Fail or Needs review, the line number the verdict refers to, and a
one-sentence reason.

Assume this runs as a nightly internal job over about 5,000 email addresses,
against a local SQLite database and an internal HTTP API, on a shared build
server whose logs are shipped to a central log tool.

Do not rewrite the code. Review only.
```

> **Pause the video here.** Run the review and read the table before you resume.

### Step 5: Reconcile the two reviews

Put your table next to Claude's and mark three categories:

1. Items Claude flagged that you missed. Verify each one against the file before
   you accept it.
2. Items you flagged that Claude did not. Keep yours if the evidence holds.
3. Items where Claude cited a line number or a construct that does not match the
   file. Discard those. A finding you cannot anchor to a line in front of you is
   not a finding, however plausible it sounds.

Category three is the part that matters most. It is the same failure mode you saw
in Exercise 1, appearing in a review instead of an explanation.

> **Pause the video here.** Reconcile all three categories before you resume.

### Step 6: Rank the fixes

Ask for a ranking:

```
From the review above, list the three changes that give the largest reduction in
risk for the smallest amount of work. One sentence each, ordered highest first.
Do not include stylistic changes.
```

Then decide whether you agree with the order, and write one line saying why. The
ranking is a judgement about your system, not a fact about the file, so yours can
reasonably differ.

### Step 7: Decide production readiness

Choose exactly one verdict:

1. Ready for production.
2. Ready after minor edits.
3. Draft only, not production ready.

Apply these two rules to your own marked checklist:

- Any Fail in the Security section rules out option 1, no matter how strong the
  Quality marks are.
- Any Fail that could expose credentials or personal data, or that lets untrusted
  input reach a query or a command, leaves only option 3.

Write the verdict, then the two or three specific items that drove it. Naming the
drivers is what separates a review from an opinion, and it is what lets someone
else disagree with you productively.

> **Pause the video here.** Write your verdict and its drivers before you resume.

### Step 8: Keep the marked checklist

Save it. Exercise 9 applies the same three-section thinking to a real pull request
diff, and starting from your own marked copy is faster than starting from a blank
page.

## What good looks like

1. Every row in all three sections is marked, and every Pass or Fail names a line
   or a specific construct.
2. At least one item where you and Claude disagreed, with your resolution and the
   evidence you resolved it on.
3. At least one Claude finding you discarded because you could not anchor it to
   the file, or an explicit note that every finding checked out.
4. A single verdict, with the two or three items that drove it named.
5. A top-three fix list, ordered by risk reduction rather than by ease.

## Common problems

| Problem | Cause | Fix |
|---|---|---|
| Almost every row is marked Fail | Reviewing to condemn rather than to inform | Re-read your evidence column. No line reference means Needs review, not Fail |
| Claude returns a rewritten file instead of a review | The request left room to improve the code | Restate: review only, one row per checklist item, no code |
| A finding sounds serious but is not in the file | A plausible generic risk was described rather than this code | Discard any finding you cannot anchor to a line |
| Two runs produce different findings | Responses vary between runs | Take the union, then verify each finding against the file yourself |
| The performance rows feel unanswerable | They were judged with no volume in mind | Use the 5,000 records per run figure from Step 2 |
| Your verdict and Claude's verdict differ | The rules in Step 7 are yours to apply, not the model's | Your verdict wins if your evidence holds. Say which rule decided it |

## Going further

1. Add two items to the checklist that are specific to your own stack, for example
   your framework's configuration handling, your team's logging policy, or the
   database driver you actually use. A checklist you extended is one you will use
   again.
2. Ask Claude to produce a version of this file that would pass your Security
   section, then review that version against the same checklist. Second drafts
   fix the flagged problems and introduce new ones surprisingly often.

Copyright © 2026, ZaranTech LLC. All rights reserved.
