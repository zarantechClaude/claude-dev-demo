# Exercise 9: PR Diff Review

**Module 3** | **15 minutes** | **You need:** Browser, a notes file

## What you will do

You will review the same pull request diff twice, with two different prompts, and
score both results against your own reading of the code. The diff will not change
between the two rounds. Only the prompt will. What that does to the review is the
whole exercise.

## Before you start

1. Open `module-3-debugging/03-labs/exercise-09-pr-diff-review/starter/sample_pr.diff`
   in your editor.
2. Claude open in your browser.
3. A file for notes. You will be counting things and comparing two rounds, so keep it
   next to you.

## Steps

### Step 1: Review it yourself first

Read the diff before you prompt anything. Take three minutes, which is longer than it
feels and about what a real reviewer would spend on a change this size.

It touches two files. It adds lines and it removes lines. Removed lines are the ones
that get skimmed past, by a reader and by a model, so read the lines beginning with
a minus sign as carefully as the ones beginning with a plus.

Write down every change you would leave a comment on. Number them. Keep the list.
You are going to score two rounds against it, and a list written before you see any
generated output is the only unbiased benchmark available to you.

> **Pause the video here.** Read the diff and write your numbered list. Do not prompt
> yet. Three minutes.

### Step 2: Start a fresh conversation

Start a new conversation for the round, and start another new one for Round 2. A
clean context matters more here than in most exercises, because leftover instructions
from an earlier chat will quietly shape a review and you will attribute the result to
the prompt you can see.

When you paste, keep the diff formatting exactly as it is. The file headers, the
`@@` hunk markers and the leading plus and minus characters are how the reader tells a
changed line from a context line. A diff pasted without them is just code.

### Step 3: Round 1, the prompt people actually send

```
Review this PR.
```

Paste the diff underneath it, and send.

That is the entire prompt. No role, no priorities, no output format. Resist the urge
to improve it, because an unimproved prompt is the measurement you need.

### Step 4: Score Round 1

Go through the response item by item and tag each one:

| Tag | Meaning |
|---|---|
| F | Formatting, whitespace, style, naming, import order |
| C | Correctness or logic |
| S | Security |
| O | Something else |

Then answer four questions in your notes:

1. How many items in total, and how many are tagged F?
2. Where does the first C or S item appear: near the top, in the middle, or near the
   bottom?
3. Which items from your Step 1 list are missing from the response entirely?
4. For the C and S items it did raise, does it say what input or request triggers the
   problem, or only that the code is risky?

> **Pause the video here.** Tag every item and answer all four questions before you
> continue. The numbers are the point of the exercise, and you cannot recover them
> later.

### Step 5: Round 2, same diff, new conversation

```
You are a senior backend reviewer. This diff is going to production. It changes a
customer-facing search endpoint backed by a SQL database.

Review it for correctness and security only. Do not comment on formatting,
whitespace, import order, naming, or code style under any heading.

Report your findings in exactly two groups.

MUST FIX: anything that changes behaviour incorrectly, returns or skips the wrong
data, breaks an existing caller, removes a guard that was there before, or lets
untrusted input reach the database, the filesystem or the response.

NICE TO HAVE: everything else.

For every finding, give four things:
- the file
- the changed line it comes from, quoted
- what goes wrong
- the concrete request or input that triggers it

If a finding is not tied to a specific line in this diff, leave it out.
```

Paste the same diff underneath, unchanged, and send.

Three things changed between the two prompts, and each one does a specific job.

1. **A role and a stake.** "Senior backend reviewer", "going to production",
   "customer-facing", "backed by a SQL database". This sets what counts as serious.
   Without it, everything in the diff is equally interesting.
2. **An exclusion instruction.** Naming the categories to leave out is what stops the
   style flood. Asking for "important issues" does not work, because style issues are
   real issues, they are just not the ones you asked for. You have to name them and
   exclude them.
3. **A severity contract with a definition, plus a per-finding format.** Defining
   MUST FIX by consequence rather than leaving it to interpretation is what makes the
   groups mean the same thing to you and to the reviewer. Requiring a quoted line and
   a triggering input is what turns a finding into something you can act on, and it is
   also what quietly suppresses findings that cannot be grounded in the diff.

### Step 6: Score Round 2 the same way, and compare

Tag every item F, C, S or O exactly as before, then put the two rounds side by side:

| | Round 1 | Round 2 |
|---|---|---|
| Total items | | |
| Tagged F | | |
| MUST FIX items | | |
| Items on your Step 1 list that were found | | |
| Items with a stated triggering input | | |

For each MUST FIX item in Round 2, answer one more question: did Round 1 raise this at
all? If it did, whereabouts in the response, and how was it worded?

That last question is often the most instructive result in the exercise. An item can
be present in Round 1 and still be missed, because it was the ninth bullet in a list
of fourteen, in the same tone of voice as a comment about import order. Being
mentioned is not the same as being surfaced.

> **Pause the video here.** Fill in the comparison table completely.

### Step 7: Verify every MUST FIX against the diff yourself

Do not carry a finding into your review notes because it was labelled MUST FIX. Check
each one against four questions:

1. Is it grounded in a line that is genuinely in this diff, and does the quoted line
   actually appear there?
2. Can you state the request or input that triggers it, in your own words?
3. Is it blocking, or is it a good idea that could ship next week?
4. Is it specific enough that the author would know what to change?

Two failure modes to watch for. A finding can cite a line that is not in the diff, or
paraphrase one inaccurately, and the fix is to check rather than to trust. A finding
can also be true, serious, and about code that this PR did not touch, which makes it a
ticket rather than a review comment.

### Step 8: Decide on every item

Mark each one Accept, Reject or Needs more information, with a one-line reason. All
three are legitimate outcomes.

- **Accept:** you have verified it against the diff and you would block the merge.
- **Reject:** you have verified it and judged it not worth blocking, and you can say
  why in one line.
- **Needs more information:** you cannot decide from the diff alone, because it
  depends on something outside it, such as whether another layer already handles it.

Rejecting with a reason is a review outcome, not a failure to review. A reviewer who
accepts every generated suggestion has not reviewed anything, they have relayed it,
and the accountability for the merge still sits with them.

### Step 9: Turn each accepted finding into something actionable

One follow-up per accepted item:

```
For finding [N], give me the minimal change that fixes it, and the test that would
have caught it before this PR was opened.
```

The second half of that request is the valuable half. "What test would have caught
this" is the question that turns a review comment into a permanent improvement,
because the comment fixes this PR and the test fixes the next one.

### Step 10: Write the review notes

Three sections, and this is the deliverable:

1. **What this PR changes.** Three to five bullets, in plain language, verified against
   the diff yourself.
2. **The risks, ranked.** Highest impact first. Each one names the file, the line, and
   the request or input that triggers it.
3. **What you would action before merge, and why.** Include the items you rejected and
   your reason, because a reviewer's rejections are as much a part of the review as
   their objections.

Save it as `review-notes.md` in
`module-3-debugging/03-labs/exercise-09-pr-diff-review/`.

## What good looks like

- You have a numbered list from Step 1, written before you saw any generated output.
- Both rounds are tagged and the Step 6 comparison table is filled in with real
  numbers.
- Every MUST FIX item in your notes names a file, quotes a line that genuinely appears
  in the diff, and states a triggering request or input.
- At least one item is rejected with a stated reason.
- Every accepted item has a proposed minimal fix and a test that would have caught it.
- `review-notes.md` exists.

## The takeaway

The diff was identical in both rounds. The reviewer was identical. Only the prompt
changed, and the review you would have taken to the author changed with it.

That is worth remembering in the direction that stings. Round 1 was not a bad review
because the tool is weak. It was a bad review because the request was empty, and an
empty request gets answered by covering everything at equal weight, which is
indistinguishable from covering nothing. Severity, scope and exclusions are your job
to supply. Nothing else in the exchange can supply them.

## Common problems

| Problem | Cause | Fix |
|---|---|---|
| Round 1 already finds everything | You added framing to the "bare" prompt without noticing, or reused a conversation that had context in it | Start a genuinely new conversation and send those three words and the diff, nothing else. If it still finds everything, record that honestly and compare the ordering and the wording instead of the counts |
| Round 2 still returns style comments | The exclusion was implied rather than stated | Keep the "under any heading" clause. Naming the categories is what makes the exclusion work |
| A finding quotes a line that is not in the diff | The diff was pasted without the plus and minus markers, or was truncated | Re-paste the file exactly as it is on disk, including the headers and hunk markers |
| Findings are true but vague | No per-finding format was required | Require all four fields: file, quoted line, what goes wrong, triggering input |
| Both rounds miss something on your Step 1 list | Expected, and it is a finding about the workflow rather than about you | Note it. It is the evidence for why the human read in Step 1 is not optional |
| The response is one long paragraph | No output structure requested | The two-group format is part of the Round 2 prompt. Keep it |

## Going further

1. Run a third round with the Round 2 prompt plus one line: "For each finding, state
   your confidence and what you would need to see to be sure." Confidence statements
   are cheap to ask for and they change how you triage a list.
2. Take the Round 2 prompt and save it as a review template in your own notes. Then
   read it against the one deck idea it implements: Claude as a first pass before a
   human reviewer, with the human keeping the sign-off. The template is only useful if
   the sign-off stays where it is.

Copyright © 2026, ZaranTech LLC. All rights reserved.
