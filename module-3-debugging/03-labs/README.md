# Module 3 labs: Debugging, Optimization and Code Reviews

Three exercises, 45 minutes of lab time. Exercise numbering is global across the
programme, not per module, so Module 3 runs from Exercise 7 to Exercise 9.

Module 3 needs a terminal but does not need Claude Code. Learners run tests and scripts
locally and do their prompting in a browser conversation. The requirement steps back up
in Module 4, which is the first module needing an API key.

## Exercises

| Ex | Title | Duration | You need | Starter code | Videos |
|---|---|---|---|---|---|
| 7 | [Debug a buggy code sample](exercise-07-debug-buggy-sample/lab.md) | 15 min | Terminal, pytest, browser | `exercise-07-debug-buggy-sample/starter/buggy_inventory.py` and `test_buggy_inventory.py` | 1 |
| 8 | [Debug a slow implementation](exercise-08-slow-implementation/lab.md) | 15 min | Terminal, Python, browser | `exercise-08-slow-implementation/starter/slow_lookup.py` | 1 |
| 9 | [PR diff review](exercise-09-pr-diff-review/lab.md) | 15 min | Browser, a notes file | `exercise-09-pr-diff-review/starter/sample_pr.diff` | 1 |

## Environment

| Requirement | Needed |
|---|---|
| Browser | Yes |
| Terminal | Yes |
| Claude Code | No |
| API key | No |

Python 3.11 or later. Python only. `pip install pytest` for Exercise 7. Exercise 8
needs nothing beyond the standard library. Exercise 9 needs no local runtime at all,
only the diff and a notes file.

## What each exercise is actually teaching

Useful when writing the recording script, because in all three cases the stated topic
and the real lesson differ.

1. **Exercise 7** teaches that debugging is a sequence of small corrections, each one
   verified, rather than one fix applied at the end. The learner clears the first error
   type and finds the suite still red. It also teaches reading a test suite as a
   specification, because the correct fix is underdetermined by the failing line and the
   bounds have to be derived from the assertions.
2. **Exercise 8** teaches that correctness is checked before the clock. The obvious fast
   rewrite is dramatically faster and returns a different answer, and the harness in the
   lab asserts the totals match before it prints the speedup. It reuses the preservation
   constraint from Exercise 5 on a performance axis rather than a data axis.
3. **Exercise 9** teaches that severity, scope and exclusions are the reviewer's job to
   supply. Two rounds on an identical diff, one with a bare prompt and one with a role,
   defined severity groups, an exclusion instruction and a per-finding format. The
   contrast between the two scored rounds is the lab.

## Deck alignment

Terminology in these labs matches the Module 3 deck: presenting errors, sharing stack
traces, isolating root causes, generating ranked debugging hypotheses, evaluating
alternative fixes, spotting performance bottlenecks, improving algorithmic complexity,
Claude as a pull request partner, security review, and structuring review output.

Two deck corrections, **both now applied** in `../01-deck/revised/` and recorded in
`../01-deck/deck-changelog.md`:

1. The vendor slide on nested loops described the growth as exponential. It is
   quadratic. Corrected on revised slide 13. Exercise 8 demonstrates the difference,
   so the deck and the lab now agree.
2. The vendor slide suggested an approved emoji as a review sign-off. Corrected on
   revised slide 23 to a verdict in words. Exercise 9 uses named severity groups.

## Conventions for anyone editing these labs

1. `docs/lab-authoring-spec.md` governs structure, voice and prompt handling. Match it
   exactly.
2. `lab.md` is the source of truth. The DOCX is generated from it.
3. Starter files carry a `# TEACHING ARTEFACT - DO NOT FIX` header. Three things in this
   module look like bugs and are not: Exercise 7's suite shows three failures rather than
   one, fixing the first error type leaves it red, and Exercise 8 returns a deliberately
   large match count that a careless optimisation will change. All are load-bearing.
4. `test_buggy_inventory.py` is the specification for Exercise 7. Do not edit it, and do
   not let the lab suggest editing it.
5. Never name a Claude model version.
6. No em dashes.
