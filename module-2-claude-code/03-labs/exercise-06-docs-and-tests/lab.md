# Exercise 6: Improve Existing Code with Documentation and Tests

**Module 2** | **22 minutes** | **You need:** Terminal, Claude Code, pytest

## What you will do

You will take three undocumented, untested functions and give them docstrings, usage
notes and a passing test suite. Then you will do the part almost nobody does: you
will go hunting for the inputs the generated tests never tried, and decide for
yourself whether what the code does with them is correct.

This lab is recorded in two videos. Steps 1 to 7 are the first. The hunt in Steps 8
and 9 is the second, and it is the reason the exercise exists.

## Before you start

1. Claude Code running in your clone of the course repo.
2. `pip install pytest`.
3. Open `module-2-claude-code/03-labs/exercise-06-docs-and-tests/starter/undocumented_utils.py`.

This exercise is Python and pytest. The same workflow applies with any mainstream
test runner in any other language, and only the framework name in your prompt
changes.

## Steps

### Step 1: Read the three functions yourself

The file has three functions: `parse_duration`, `merge_ranges` and
`summarise_scores`. None of them has a docstring. None has a test.

For each one, write down three things:

1. What goes in, including the type and the shape.
2. What comes out, including what comes out when nothing goes in.
3. One input you are genuinely unsure about.

That third item is the useful one. Keep those three uncertain inputs on paper. You
will come back to them in Step 8, and how many of them the generated tests happen to
cover is the measurement this exercise is built around.

> **Pause the video here.** Read all three functions and write your nine notes
> before you prompt anything.

### Step 2: Ask for docstrings, and only docstrings

```
Generate a docstring for each function in this file. Describe the parameters, the
return value, the exceptions raised, and any edge case behaviour that is visible in
the code. Use plain docstrings, not a heavyweight format. Do not change any logic,
any name, or any default value.
```

That last sentence is what keeps a documentation request from quietly becoming a
refactor. Documentation requests turn into refactors more often than any other kind
of request, because the code reads badly and the model is trying to help.

### Step 3: Verify the docstrings against the code, not against your expectations

Four checks, in this order.

1. Do the parameter names in the docstrings match the actual signatures?
2. Is the return value described correctly, including what the function returns for
   empty input?
3. Is every default value stated, and stated with the right number?
4. Did it document any behaviour that is not in the code?

Check four is the real risk. Confidently wrong documentation is worse than none,
because the next developer trusts it and stops reading the code. When you find an
item that describes what the function should do rather than what it does, do not fix
the code. Mark the line. It is a finding, and you will need it in Step 9.

### Step 4: Ask for usage notes

```
Create README usage notes for this module in markdown. Include the purpose, the
setup, how to import and call each function, and one worked example per function
showing the exact input and the exact output.
```

Save the result as `README-usage.md` in the exercise folder.

Then run the worked examples. Every one of them. An example that has never been
executed is a guess with formatting.

> **Pause the video here.** Save the notes and actually run the three worked
> examples in a Python session.

### Step 5: Choose what to test, and why

Not everything deserves a test. These three do, for three different reasons, and the
reasons are the useful part:

- `parse_duration`, because it parses a string, and parsers fail on inputs their
  author never pictured.
- `merge_ranges`, because it sorts and then combines, and combining rules have
  boundaries.
- `summarise_scores`, because it aggregates, and aggregation over nothing is a
  special case in every language.

### Step 6: Ask for the tests, in a separate prompt

```
Generate pytest tests for the three functions in this file. Cover normal cases,
boundary values, and invalid input. One assertion focus per test. Name each test
after the behaviour it checks.
```

Ask for docstrings and tests in separate prompts, and in that order. Requested
together, the tests tend to assert the behaviour just described in the docstring
rather than the behaviour in the code, and you lose the independent check that is the
entire value of having tests.

Save the result as `test_undocumented_utils.py` in the `starter/` folder, next to the
module it tests.

### Step 7: Run them, and fix what fails

```bash
cd module-2-claude-code/03-labs/exercise-06-docs-and-tests/starter
pytest -v
```

Failures at this point are normal and are not a sign that anything is broken. The
usual causes:

- The import path does not match where you saved the file
- A boundary assumed exclusive where the code is inclusive, or the reverse
- An expected exception type that is close but not the one raised
- An edge case assumed rather than read

When you fix a failure, feed the exact pytest output back rather than describing it.
The traceback is better input than your summary of the traceback.

One rule for this step: when a test disagrees with the code, work out which one is
wrong before you change either. Sometimes the test is wrong. Sometimes the test has
found something.

> **Pause the video here.** Get to a green run before you continue. This is the end
> of the first video.

### Step 8: Hunt the coverage the tests do not have

You have a green suite. Green means the tests you have all pass. It says nothing
about the tests you do not have, and that is what this step is for.

First, do it yourself. Take the three uncertain inputs you wrote down in Step 1 and
check each one against your test file. Is there a test that exercises it? Write down
yes or no for each.

Now widen the search:

```
Here is the module and here is my test file. List the input categories that my tests
do not exercise, function by function. Include empty input, boundary values, inputs
that are legal but unexpected, inputs where the same call could reasonably be
expected to behave in two different ways, and inputs that produce a result rather
than an error when an error might have been more useful.

Do not write any test code yet, and do not suggest changes to the module.
```

Now the important part, and the part that separates this from a list-generating
exercise. Do not trust the list, and do not write assertions from it. For each gap it
claims, open a Python session, call the function with that input, and record the value
that actually comes back.

```bash
python -c "from undocumented_utils import FUNCTION; print(repr(FUNCTION(INPUT)))"
```

Use `repr` rather than `print` on its own. The difference between an empty string, a
zero, an empty list and a `None` is invisible in ordinary print output, and those four
are exactly the values you are trying to tell apart here.

Then, for each recorded value, make a decision and write it down:

- **Correct.** The behaviour is intended. Write a test that locks it in, so nobody
  changes it by accident.
- **A bug.** The behaviour is wrong. Write a test that documents what it should be,
  mark it `@pytest.mark.xfail`, and leave the module alone. This is a teaching file
  and you do not have the authority to change its contract.
- **Undecided.** The behaviour is defensible either way. Write down both readings and
  which one you would ship, and why.

At least one of these will land in the third category. When it does, notice what has
happened: the code cannot tell you the answer, because the code is the behaviour. Only
the intended contract can, and nobody ever wrote it down. That is what missing
documentation actually costs, and it is why Step 2 came before Step 6.

> **Pause the video here.** Work through every claimed gap. Confirm each one against
> a real call before you write a single assertion. Budget four minutes.

### Step 9: Write the contracts down

For each function, write one line stating its contract: what it promises, for what
inputs, and what it does outside them.

Then go back through your docstrings and mark each sentence `D` or `I`.

- `D` for descriptive. This sentence describes what the code does. If the code
  changes, the sentence is wrong.
- `I` for intentional. This sentence asserts what the code is supposed to do. If the
  code disagrees, the code is wrong.

Most generated docstrings are entirely `D` and read as though they were `I`. Knowing
which sentences are which is what makes documentation worth maintaining.

Keep `test_undocumented_utils.py`. You will run it again at the start of Module 3.

## What good looks like

- All three functions have docstrings you have verified line by line against the
  code.
- `README-usage.md` exists and every worked example in it has been executed.
- `test_undocumented_utils.py` runs green with `pytest -v`.
- You added at least three tests beyond the generated set, each one written after
  checking the real return value rather than from a predicted one.
- At least one behaviour is recorded as undecided, with both readings written down.
- You can say, for every sentence in your docstrings, whether it is descriptive or
  intentional.

## Common problems

| Problem | Cause | Fix |
|---|---|---|
| The docstrings changed the code as well | The "do not change any logic" line was dropped | Restore from git and re-run the Step 2 prompt with that line intact |
| `ImportError: cannot import name` when running pytest | The test file is not in the same folder as the module | Save it in `starter/`, and run pytest from `starter/` |
| Every generated test passes first time | Generated tests were written against the docstrings rather than the code | Start a fresh conversation, supply only the module, and ask for tests again |
| The coverage hunt returns generic advice like "test edge cases" | The prompt did not name the categories | Use the category list in Step 8 verbatim, and require it to be function by function |
| A claimed gap turns out not to be real | The gap list was generated, not verified | This is the expected outcome for some of them. Verifying by calling the function is the step, not an interruption to it |
| You cannot decide whether a behaviour is a bug | There is no written contract, so there is no authority to appeal to | Record both readings and move on. That record is the deliverable, not the resolution |

## Going further

1. Delete one of your new tests, run `pytest`, and confirm it still passes. Then ask
   yourself what that test was actually protecting. A test that can be deleted
   without consequence is documentation, not verification.
2. Add a property-based test for `merge_ranges` using `hypothesis`. Generated example
   tests and generated property tests fail on very different inputs, and comparing
   the two failures is a fast way to understand what each style is good for.

Copyright © 2026, ZaranTech LLC. All rights reserved.
