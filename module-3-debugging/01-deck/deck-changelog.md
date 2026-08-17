# Module 3 deck changelog

Original: `original/Module 3 - Debugging, Optimization, and Code Reviews.pptx`  
Revised: `revised/Module 3 - Debugging, Optimization, and Code Reviews - REVISED.pptx`

Slide count: 25 before, 26 after.

This changelog is generated from the same declaration that drives the edits,
so it cannot drift from what was actually changed.

## How to use this

If your Google Slides copy is the master, apply these changes there and ignore
the revised PPTX. If you would rather adopt the revised file, import it and it
becomes the master. Do not do both, or the two will diverge.

Slide numbers under 'Changed' refer to the **original** deck. Slide numbers
under 'Added' refer to the **revised** deck.

## Changed

### Slide 12

**Was:**

> Prompt Claude to locate nested loops that cause exponential execution time growth.

**Now:** the bullet block was rewritten to:

> - Prompt Claude to locate nested loops, whose cost grows quadratically with input size.
> - Ask for refactoring suggestions using hash maps or dictionaries to reduce complexity.
> - Compare the before and after execution times of the refactored loop structures.
> - Confirm the output is identical before trusting the speedup. A faster wrong answer is still wrong.

**Why:** Factual error. Nested loops grow quadratically, not exponentially. The slide also contradicted Exercise 8, which demonstrates exactly this growth, and a learner who repeats 'exponential' in a review loses credibility. The final bullet now carries Exercise 8's correctness lesson.

### Slide 22

**Was:**

> Include a clear sign-off format like an approved emoji for quick scanning.

**Now:**

> Ask for a verdict in words: must fix before merge, or safe to merge with notes.

**Why:** An emoji sign-off is not a review outcome. Exercise 9 teaches named severity groups, because 'must fix before merge' and 'nice to have' are the categories that actually change what a reviewer does.

## Added

### New slide at position 4: Exercises in This Module

- Exercise 7: Diagnose and fix a failing test suite. 15 minutes.
- Exercise 8: Measure, optimise, then verify a slow function. 15 minutes.
- Exercise 9: Review a pull request diff by severity. 15 minutes.
- You need Python and pytest. No API key in this module.

**Why:** Section map for recorded navigation.

## Not changed, but flagged

Nothing else in this deck was edited. Anything you disagree with above can be
reverted from `original/` without affecting the labs, which do not depend on
slide wording.
