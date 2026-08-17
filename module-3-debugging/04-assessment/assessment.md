# Module 3 self-check: Debugging, Optimization and Code Reviews

Ten questions. One correct option each.

This is a self-check, not a graded test. Nothing here gates your progress through the
course. Its only job is to show you which parts of Module 3 you have not settled yet, so
answer from what you know rather than looking anything up.

Each question is tagged.

- **Core** means Module 3 taught it directly, on a slide or in an exercise.
- **Stretch** means you have to reason one step past what you were shown. Three of the
  ten are Stretch. Missing one of those is not a sign the module failed you.

Answers are not in this document. Your trainer holds the key.

---

### 1. Core

You paste the final line of a failing run, nothing else, and ask what is wrong. Three
generic and unrelated suggestions come back. What was missing from the prompt?

a. The language and the framework, neither of which the final line identifies on its
   own.
b. A request for three ranked hypotheses, which is what turns a vague answer into a
   testable one.
c. The full trace, the code around the failing line, and the steps that reproduce it.
d. A note that the failure happens only in production, which changes the class of cause
   entirely.

### 2. Core

A test fails with no exception raised. The function ran to completion and returned a
number the test does not expect, so there is no trace to paste. Which prompt fits this
kind of failure best?

a. Ask for the file to be rewritten until the value it returns matches the assertion in
   the test.
b. Ask which single line is wrong, and for no alternative explanations, so that the
   answer stays specific.
c. Ask for the missing trace to be reconstructed from the assertion message and the
   reported value.
d. Ask for three possible causes ranked by likelihood, plus one cheap check for the most
   likely one.

### 3. Core

You are writing a review comment about a loop over one list nested inside a loop over
another. Which description is correct?

a. Cost grows with the square of the input, so ten times the data is roughly a hundred
   times the work.
b. Cost grows exponentially, so every additional record roughly doubles the total work
   performed.
c. Cost grows linearly in the combined length of the two lists, which is why the effect
   appears so suddenly.
d. Cost depends on the ratio between the two list lengths rather than on their sizes, so
   it cannot be stated generally.

### 4. Core

Your optimised version runs a thousand times faster than the original and returns a
different total. What does that tell you, and what do you do with the timing?

a. Totals shift slightly whenever a scan is replaced by a lookup, so record both numbers
   and carry on.
b. The speedup is not a result. Restore the original total, then measure again. A faster
   wrong answer is still wrong.
c. Report the speedup and the discrepancy together, and let the reviewer decide which of
   the two totals to trust.
d. The original was probably counting something it should never have counted, so adopt
   the new total as the corrected one.

### 5. Core

Round one of your review was "review this PR" and came back with forty style items, with
the one finding that should have blocked the merge buried among them. Which change to the
prompt addresses that?

a. Cap the output length, so that only the findings the reviewer considers most important
   survive the cut.
b. Ask for the important issues only, which names the priority without ruling any
   category out in advance.
c. Ask for a corrected version of the diff rather than a review, since the corrections
   show what mattered most.
d. Set a reviewer role and a stake, define severity groups by consequence, and exclude
   style by name.

### 6. Core

A ten line fix for an intermittent bug looks right, and the explanation of why it works
is convincing. What has to happen before it merges?

a. Run the failing case and the suite, because a proposed fix is a hypothesis until it is
   executed.
b. Ask for the complexity of the fix, and for confirmation that no existing behaviour
   anywhere has changed.
c. Have a second conversation review the same fix, and merge it if both reach the same
   conclusion independently.
d. Merge it behind a flag, since an intermittent bug cannot be reproduced reliably enough
   to verify any fix.

### 7. Core

Your team wants Claude in the pull request process without giving up human judgement.
Which arrangement does that?

a. Merge automatically when a review comes back with no must-fix findings, and sample a
   proportion of those merges for audit.
b. Restrict it to naming and comment quality, so that no judgement about behaviour is
   ever delegated to it at all.
c. Run it first for bugs, security and missing tests, then have a human review behaviour
   and architecture and sign off.
d. Have a human review first and consult it only where the human is unsure, so that it
   never sets the agenda for a review.

### 8. Stretch

Claude identifies a slow sort correctly, then offers a fifty line custom implementation to
replace it. What do you do?

a. Take the implementation, since a purpose-built version will outperform a general one on
   your particular data shape.
b. Ask whether a built-in function reaches the same complexity class without fifty lines
   you now have to maintain.
c. Leave the original in place, on the grounds that the proposed replacement is larger
   than the problem it solves.
d. Take it, and ask for a proof of correctness and stability to be supplied alongside the
   implementation.

### 9. Stretch

A review flags a function as a serious bottleneck. You know it runs once at startup and
takes a hundredth of a second. What does this tell you about static AI review?

a. Complexity analysis is unreliable in generated reviews, so treat every performance
   finding as noise until it is profiled.
b. It has no runtime data, so it cannot weigh how often code runs. Supply the
   measurements instead.
c. Startup code is systematically over-reported, because initialisation patterns resemble
   hot loops in structure.
d. Review requests should cover correctness only, because any performance judgement needs
   a profiler and is out of scope.

### 10. Stretch

A must-fix finding in your review is real and serious. You check the diff and the code it
describes is not part of this change. What do you do with it?

a. Keep it as a must-fix, because severity is a property of the risk and not of which
   change happened to surface it.
b. Drop it, because a finding that is not grounded in a line of this diff cannot be
   verified by a reviewer at all.
c. Raise it as a separate ticket and leave it out of the blocking list for this pull
   request.
d. Ask the author to fix it in this change, since they are already working in that area of
   the code today.

---

Copyright © 2026, ZaranTech LLC. All rights reserved.
