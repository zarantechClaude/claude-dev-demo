# Exercise 8: Debug a Slow Implementation

**Module 3** | **15 minutes** | **You need:** Terminal, Python, Browser

## What you will do

You will take a function that runs in about two seconds and make it dramatically
faster, in the correct order: measure, diagnose, change, check the answer, and only
then look at the clock. The order is the exercise. Speed is the easy part.

## Before you start

1. `cd module-3-debugging/03-labs/exercise-08-slow-implementation/starter`.
2. Open `slow_lookup.py`. No packages to install. The timer is already in the file.
3. Claude open in your browser.

## Steps

### Step 1: Run it and record the baseline

```bash
python slow_lookup.py
```

Record **two** numbers, not one:

| | Value |
|---|---|
| Match count | |
| Elapsed time | |

Expect roughly two seconds. If your machine is much faster or much slower than that,
change the `n` default in `build_data` up or down. Leave `random.seed(42)` exactly as
it is, so the data is identical on every run and your two versions are comparable.

> **Pause the video here.** Run it and fill in both rows of that table.

### Step 2: Know why the baseline comes first

You cannot claim an improvement you did not measure. That is the obvious reason.

The less obvious reason is that this is the step that catches the embarrassing cases:
the change that made it slower, and the change that made it faster by doing less work
than it was supposed to. Neither is visible without a recorded starting point.

### Step 3: Read the function and describe the work yourself

Read `count_matches`, including its docstring, all the way to the end.

Then work out the shape of the work on paper. There are two loops. The outer one runs
once per item in `wanted`. The inner one runs once per item in `catalogue`. At the
default size that is 12,000 times 12,000, which is 144 million comparisons to produce
one integer.

Name the growth correctly. It is **quadratic**. Work grows with the square of the
input. It is not exponential, and the two are not interchangeable words for "slow".
Quadratic on ten times the data is a hundred times the work. Exponential on ten times
the data is a number with no useful name. Confusing them in a review costs you
credibility with the person you are trying to convince.

### Step 4: Ask for a diagnosis, not a rewrite

```
Here is a Python function that takes about two seconds on 12,000 records.

[paste count_matches]

Explain the main performance bottleneck and name the complexity class precisely. Do
not give me optimised code yet.
```

### Step 5: Compare its diagnosis with yours

You are checking for two things: that it identified the nested scan rather than
something incidental, and that it named the complexity class correctly.

> **Pause the video here.** Compare the two diagnoses. If it named a different
> bottleneck from the one you found, work out which of you is right before moving on.

### Step 6: Ask for the optimised version

```
Now give me an optimised version of count_matches with the same signature. Explain
the main change in two sentences.
```

Save the function it gives you as `fast_lookup.py` in the same folder. Keep the
function name `count_matches` so the harness below can import both.

### Step 7: Before you time anything, predict the answer

Do not run it yet. This step takes ninety seconds and it is the one the exercise is
built around.

1. Read the original docstring again, one line at a time, and write down in your own
   words what number `count_matches` is supposed to return. Be precise about what it
   does when the same value appears in `catalogue` more than once.
2. Now read the optimised version line by line and predict, on paper, the number it
   will return for the same input. Not "the same number". Reason it out from the code
   in front of you.
3. Compare your two predictions.

If they differ, you already know what you are about to see on screen. If they agree,
you are about to confirm it. Either way you are testing a prediction rather than
reading a result, and that is a different and much more useful activity.

### Step 8: Compare the answers first, the times second

Create `compare_lookup.py` in the same folder:

```python
import time

from slow_lookup import build_data, count_matches as slow_count
from fast_lookup import count_matches as fast_count

catalogue, wanted = build_data()

start = time.perf_counter()
slow_total = slow_count(catalogue, wanted)
slow_elapsed = time.perf_counter() - start

start = time.perf_counter()
fast_total = fast_count(catalogue, wanted)
fast_elapsed = time.perf_counter() - start

print("slow: {} in {:.3f}s".format(slow_total, slow_elapsed))
print("fast: {} in {:.3f}s".format(fast_total, fast_elapsed))

assert fast_total == slow_total, "output changed: {} became {}".format(
    slow_total, fast_total
)

print("speedup: {:.0f}x".format(slow_elapsed / fast_elapsed))
```

```bash
python compare_lookup.py
```

Look at where the assertion sits. It runs before the speedup is printed, and that
ordering is deliberate. If the answer changed, the speedup is not a result, it is a
distraction. A harness that prints the ratio first will get the ratio quoted in a
stand-up meeting and the assertion looked at never.

> **Pause the video here.** Run the harness and read all of the output.

### Step 9: Take the outcome you got

Both outcomes are part of the exercise and neither is a mistake on your part.

**If the assertion passed**, you have a genuine optimisation. Record the three numbers
and go to Step 10.

**If the assertion failed**, your optimised version is faster and wrong. Sit with that
for a second, because it is worse than slow code, not better. Slow code announces
itself. A wrong total does not, and it will be copied into a report and believed.

Read the two numbers the assertion printed and work out what the new version is
actually counting. Then prompt again, this time carrying the constraint your first
prompt left out:

```
Here is the original function and here is your optimised version.

[paste both]

Your version returns a different total from the original. The original counts every
occurrence, so a value appearing three times in the catalogue contributes three to the
total, once for each time it is wanted.

Preservation constraint: the optimised version must return an identical total to the
original for identical input. Keep the signature. Fix it, and tell me which line of
your previous version lost the count.
```

Replace `fast_lookup.py` and re-run the harness until the assertion passes.

That is the same pattern you used in Exercise 5, on a different axis. There it
protected stored data during a refactor. Here it protects the answer during an
optimisation. A **preservation constraint** states what must survive the change. Both
prompts asked for an improvement, and only one of them said what improvement was not
allowed to cost.

### Step 10: Record the comparison

Three numbers and one sentence:

| | Value |
|---|---|
| Baseline elapsed | |
| Optimised elapsed | |
| Ratio | |
| Totals matched | yes |

Then note why the ratio is not a fixed property of the change. Turning quadratic work
into linear work does not buy you a constant speedup, it buys you one that grows with
the data. At this input size it is large. At ten times the input it would be far
larger. That scaling property is the result worth reporting, not the specific
multiple, which belongs to your machine on the day you ran it.

## What good looks like

- You recorded the match count and the elapsed time before changing anything.
- `fast_lookup.py` and `compare_lookup.py` exist in the starter folder.
- `compare_lookup.py` runs to completion, which means the assertion passed and the
  totals are identical.
- You can name the complexity class correctly and say in one sentence why
  "exponential" is the wrong word for it.
- You can state what the function counts, precisely enough that someone else could
  verify an implementation against your sentence.

## Common problems

| Problem | Cause | Fix |
|---|---|---|
| Large speedup and the assertion fails | The optimisation changed what is being counted, not just how it is counted | Re-prompt with the preservation constraint in Step 9, and identify which line dropped the count |
| Baseline is under 0.2 seconds | Fast machine | Raise `n` in `build_data`. Keep the seed at 42 |
| Baseline is over ten seconds | Slow or loaded machine | Lower `n`. Keep the seed at 42 |
| Times move around between runs | Other load on the machine | Run three times and take the middle value. One timing is an anecdote |
| `ModuleNotFoundError: slow_lookup` | The harness is not in the starter folder, or you ran it from elsewhere | Put all three files in `starter/` and run from there |
| The optimised version imports a library you do not have | The prompt did not restrict dependencies | Add "standard library only" to the prompt. The standard library is enough for this |
| The ratio is enormous and you do not believe it | Believable. Verify rather than assume | Confirm the assertion passed, then re-run and check the ratio is stable |

## Going further

1. Run both versions at `n=6000`, `n=12000` and `n=24000` and put the six timings in a
   table. One version's column roughly quadruples each time you double the input and
   the other roughly doubles. Seeing that in your own numbers is worth more than
   knowing the terminology.
2. Ask for a third implementation optimised for memory rather than speed, then measure
   both. The two goals conflict here, and being able to say which one you were
   optimising for is most of what makes a performance claim meaningful.

Copyright © 2026, ZaranTech LLC. All rights reserved.
