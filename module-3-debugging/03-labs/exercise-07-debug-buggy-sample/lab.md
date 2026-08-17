# Exercise 7: Debug a Buggy Code Sample

**Module 3** | **15 minutes** | **You need:** Terminal, pytest, Browser

## What you will do

You will take a failing test suite to green using one disciplined loop: diagnose,
fix minimally, re-run. Along the way you will meet a fix that the failing line does
not fully determine, and you will derive the missing part of it from the tests
instead of guessing.

## Before you start

1. `pip install pytest`.
2. `cd module-3-debugging/03-labs/exercise-07-debug-buggy-sample/starter`.
3. Claude open in your browser. This module does not need Claude Code. You will paste
   code and tracebacks into a browser conversation.

The test file is correct. `test_buggy_inventory.py` is not to be edited at any point
in this exercise. Only `buggy_inventory.py` changes.

## Steps

### Step 1: Run the suite and write down exactly what you see

```bash
pytest -v
```

Before you touch anything, record four facts:

1. How many tests ran.
2. How many failed.
3. For each failure, the error type on the last line of its section.
4. For each failure, whether it raised an exception or returned a wrong value.

That fourth column is the one that decides your approach, and it is the one people
skip. An exception gives you a file and a line number. A wrong value gives you
neither.

> **Pause the video here.** Run the suite, write down all four facts, and resist
> fixing anything.

### Step 2: Pick the failure with a traceback, and capture all of it

Work one failure at a time, and start with one that raised an exception, because an
error type plus a line number is the cheapest thing in debugging to act on.

Copy the whole section for that failure, from the test name down to the error line.
Not the last line on its own.

Truncating the trace is the single most common reason an AI debugging prompt comes
back with generic suggestions. There was nothing in the prompt to reason from, so it
reasoned about the category of problem instead.

### Step 3: Ask for the root cause, not for a fix

```
Here is a function and here is the full pytest traceback from one of its tests.

[paste buggy_inventory.py]

[paste the full traceback]

What is the most probable root cause? Explain in three sentences. Do not rewrite the
file and do not give me the fix yet.
```

Withholding the fix request is deliberate. Ask for a rewrite and you will get a
rewrite, it will probably work, and you will have learned nothing you can reuse.

### Step 4: Verify the diagnosis against the code yourself

Does the cause it names match the error type? Does it match the line number in the
traceback? Can you point at the expression that fails?

Never act on a diagnosis you have not confirmed. This takes fifteen seconds and it is
what stops you from spending ten minutes fixing the wrong thing.

### Step 5: Discover that the failing line does not determine the fix

Now try to write the fix, and you will hit a wall. The function is reading a value it
was never given. The tests do not supply it. Nothing in the file supplies it. So
"what should this value be?" has no answer inside the failing line.

The tests are the only specification you have. Read them as one.

Open `test_buggy_inventory.py` and, for each test that raises this error, write down
three things:

1. The inventory dictionary it passes in.
2. The deliveries it applies, and the resulting quantities.
3. The exact list it asserts should come back.

Then answer this on paper, before prompting anything: **what range of values for the
missing quantity makes every one of those assertions true at the same time?** One of
those tests gives you the lower bound. Another gives you the upper bound. Do the
arithmetic both ways.

Now check your work:

```
Here is a function and here is its test file.

[paste buggy_inventory.py]

[paste test_buggy_inventory.py]

The function reads a threshold value that the tests never supply. Derive the full
range of default values for that threshold that satisfy every assertion in this test
file. Show the arithmetic for the lower bound and the upper bound separately, naming
which test produces each. Do not write the fix yet.
```

If its range and your range disagree, the tests decide. Re-do the arithmetic against
the assertions until you can see which of you is wrong.

> **Pause the video here.** Derive the range yourself first, then check it. Do not
> skip the paper step. Deriving a specification from a test suite is the transferable
> skill in this exercise.

### Step 6: Apply the minimal fix

Introduce the missing value as a parameter with a default inside the range you
derived, and change nothing else. Do not tidy the loop. Do not rename anything. Do
not edit the tests.

Minimal is the constraint, and it is a constraint on you rather than on the model. A
large fix hides which change was the one that mattered.

### Step 7: Re-run and read the summary line

```bash
pytest -v
```

The error type from Step 1 is gone from the output.

> **Pause the video here.** Re-run the suite and read the last line of the output
> before you continue watching.

### Step 8: Read what is still failing

Look at what is left, and notice that it is a different animal.

Nothing raised. There is no traceback pointing at a broken expression. The function
ran to completion and returned a number that is not the number the test expects.

So the Step 3 prompt will not work here, because a trace-based prompt needs a trace.
Ask for ranked hypotheses instead.

```
This pytest assertion fails:

[paste the assertion line and the reported actual value]

Here is the function:

[paste the function]

Give me three possible causes ranked by likelihood, and one quick check I can run for
the most likely one. Do not rewrite the function.
```

Three ranked hypotheses and a cheap check for the top one is a pattern worth keeping.
It works on any failure where the code ran and the answer was wrong, which is most of
the failures you will meet in real work.

### Step 9: Work the ranked list from the top

Run the check for the first hypothesis. If it is wrong, that is a result, not a wasted
step, and you move to the second with one possibility eliminated.

When you find it, apply the same discipline as Step 6. Small change, one line, nothing
else touched.

### Step 10: Improve the failure message, then verify

Now that the suite is green, make the next failure cheaper for whoever meets it.

```
How would you make this function fail more informatively when it is given a delivery
for an item that is not in the inventory? Keep the existing exception type, name the
offending key in the message, and do not expose the whole inventory in the error.
```

Then verify the final state:

```bash
pytest -v
git diff
```

Three tests passing, and a diff that touches `buggy_inventory.py` and nothing else.

## What good looks like

- `pytest -v` shows three passing tests.
- `git diff` shows changes in `buggy_inventory.py` only. `test_buggy_inventory.py` is
  untouched.
- You can state each root cause in one sentence.
- You can state the range the tests allowed for the default, name which test produced
  each bound, and show the arithmetic.
- You can explain why the second failure needed a different prompt from the first.
- Your total change is a handful of lines.

## The takeaway

Two kinds of failure, two techniques, and one habit. The first kind was diagnosable
from a traceback. The second produced no traceback and needed the test output plus
ranked hypotheses. Most real debugging is the second kind, and a trace-only prompt
gets you nowhere on it. Notice also that the count of failures and the count of
underlying problems were not the same number, which is normal.

The habit matters more than either technique. You ran the suite after the first fix
rather than after the last one, so you found out immediately that you were not
finished. Debugging is a sequence of small corrections, each one verified, not a
single solution applied at the end.

## Common problems

| Problem | Cause | Fix |
|---|---|---|
| pytest reports a different set of results from the video | A stale cache is present in `starter/` | Delete `.pytest_cache` and `__pycache__`, or run `pytest -p no:cacheprovider` |
| `ModuleNotFoundError: buggy_inventory` | pytest was run from the repo root | `cd` into `starter/` and run it from there |
| The suggested fix rewrites the whole function | The prompt asked for a fix rather than a cause | Re-ask with "explain the cause, do not rewrite the file" |
| The derived range has no valid values in it | An assertion was read as strict where it is not, or the delivery quantities were not applied first | Re-read each test, apply the deliveries on paper, then compare against the asserted list |
| You are tempted to change a test to make it pass | The test looks wrong because the code is wrong | The test file is the specification here. If you edit it you have deleted the only specification you had |
| The suite goes green but you cannot say why | Two changes were applied before re-running | Revert, apply one change, run, then apply the next |

## Going further

1. Add a test of your own that fails for a third reason, then hand only the failure
   output to Claude and see whether it can find it without seeing your test. That is
   the position a reviewer is in when someone reports a bug badly.
2. Re-do Step 5 by binary search instead of arithmetic. Pick a value, run the suite,
   halve the interval based on which test failed. Compare how many runs it took
   against deriving the bounds directly, and note which approach you would trust on a
   suite of five hundred tests.

Copyright © 2026, ZaranTech LLC. All rights reserved.
