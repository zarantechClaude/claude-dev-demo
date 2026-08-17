# Lab defect register

Trainer and content-team reference. **Do not distribute to learners, and do not
copy any of it into a lab document or a slide.**

Every deliberate problem in every `starter/` directory is recorded here. If you
add or change a starter file, update this register in the same commit.

Everything marked **verified** was confirmed by running the code, not by reading it.

---

## Exercise 1, `running_average.py`

Module 1. One defect, deliberately quiet.

| # | Defect | Why it teaches well |
|---|---|---|
| 1 | `range(len(readings) - 1)` silently drops the final reading. The returned list is one element short and every average excludes the last value. | No exception, no error, plausible-looking output. Exactly the class of bug that a fluent natural-language explanation papers over. |

**Verified:** input `[10, 20, 30, 40]` returns `[10.0, 15.0, 20.0]`. Three values
for four readings.

Expected learner outcome: Claude's first-pass explanation often describes the
*intended* behaviour rather than the actual behaviour. If it does catch the bug,
the point to make on camera is that it caught it because the function is small and
complete, then ask what happens with four thousand lines and no context.

Prompt to use on camera if the explanation looks clean: "How many values are in
the list that comes back? Count them against the input."

---

## Exercise 3, `order_sync.py`

Module 1. Fifteen defects. Expected verdict: **draft only, not production ready.**

### Quality
| # | Defect |
|---|---|
| 1 | No error handling anywhere. A missing user makes `row` None and `row[2]` raises. |
| 2 | No timeout on the HTTP call. One slow upstream hangs the whole job. |
| 3 | `orders["items"]` assumes a response shape with no check. A non-200 crashes on parse. |
| 4 | The function does four unrelated things: lookup, fetch, cache, count. Untestable as one unit. |
| 5 | No type hints, no docstring, and the connection is never closed. |

### Security
| # | Defect |
|---|---|
| 6 | Hardcoded live-looking API key in source. The headline finding. |
| 7 | SQL injection in the SELECT, via f-string interpolation of `email`. |
| 8 | Second SQL injection in the INSERT, via `o['status']`. |
| 9 | Customer address written to application logs. PII exposure. |
| 10 | No input validation on `user_emails` at all. |

### Performance
| # | Defect |
|---|---|
| 11 | A new cursor created per iteration, inside the loop. |
| 12 | One HTTP round trip per user, serially, no batching. |
| 13 | `conn.commit()` inside the inner loop. One transaction per order row. |
| 14 | Over-fetching columns that are not all used. |
| 15 | No pagination handling on the orders response. |

Any learner who marks this "ready after minor edits" has missed the hardcoded key
or one of the injections. Worth calling out on camera, because it is the most
common real-world failure mode of AI-assisted review.

---

## Exercise 5, `messy_registration.py`

Module 2. Twelve defects, and one designed trap that matters more than any of them.

### Quality
| # | Defect |
|---|---|
| 1 | Function named `r`, single-letter variables throughout |
| 2 | Six near-identical validation blocks, all returning the same useless `{"err":"bad"}` |
| 3 | Every failure returns 400 with no indication of which field failed |
| 4 | Parsing, validation, hashing and persistence all in one function |
| 5 | Connection never closed, `debug=True` on the app |
| 6 | `== None` instead of `is None` |

### Security
| # | Defect |
|---|---|
| 7 | MD5 password hashing, unsalted |
| 8 | SQL injection in the SELECT, via string concatenation of `email` |
| 9 | SQL injection in the INSERT, via `name`, `email` and the hash |
| 10 | Password hash printed to stdout alongside the email |
| 11 | Minimum password length of 4 |
| 12 | The duplicate-email check and the insert are not atomic, so there is a race |

### The trap

A naive refactor prompt ("refactor this into cleaner modular code") will normally
also replace MD5 with a modern hash. That is correct security advice and a
**breaking change**: every existing stored hash becomes unverifiable and no
existing user can log in.

The lesson is that "the AI improved my code" and "the AI broke my system" are
simultaneously true, and that the fix is a *preservation constraint* in the prompt
rather than a better model.

Surface it in the debrief, then ask what would have caught it. The answer is a
test that logs in an existing user, which is Exercise 6.

---

## Exercise 6, `undocumented_utils.py`

Module 2. **No planted bugs.** Three working functions with no documentation and
no tests. The teaching value is in the edge cases that generated tests routinely
miss. Use this table to check learner submissions.

| Function | What generated tests usually get wrong |
|---|---|
| `parse_duration` | Empty string returns 0 rather than raising. `"90s"` and `"1m30s"` both equal 90. A bare number with no unit raises. A unit before the number raises. |
| `merge_ranges` | Touching ranges like `(1,5)` and `(5,9)` do merge, because the comparison is `<=`. Fully nested ranges. Empty input returns `[]`, not None. |
| `summarise_scores` | Empty list returns None for mean and pass rate rather than 0 or a division error. A score exactly equal to `passing` counts as a pass. |

---

## Exercise 7, `buggy_inventory.py` and `test_buggy_inventory.py`

Module 3. Two independent defects.

**Correction to earlier documentation.** An earlier version of this register said
the first defect masks the second and that fixing the first "exposes" it. That is
wrong, and it was wrong in a way that would have embarrassed the trainer on camera.
Verified: a fresh `pytest` run reports **three failures, not one**. Both problems
are visible from the start, because pytest runs each test independently.

| # | Defect | Surfaces as |
|---|---|---|
| 1 | `inventory["threshold"]` is read as though `threshold` were an inventory item. It is not a key in either test fixture. | `KeyError: 'threshold'` in two of the three tests |
| 2 | `reorder_quantity` uses floor division, so a shortfall of 13 with packs of 5 returns 2 packs, which does not clear the shortfall. Needs ceiling division. | `test_reorder_covers_shortfall` fails, got 2, expected 3 |

The lesson still holds and is arguably better: the learner fixes the `KeyError`,
re-runs, and the suite is **still red**. Debugging is a sequence of small
corrections, not one fix. Failure count and problem count are not the same number.

### The threshold range, verified

The correct fix to defect 1 is underdetermined by design, and this is the most
interesting part of the lab. The tests call `restock()` with two arguments and
never pass a threshold, so the learner has to introduce one with a default. The
two fixtures constrain that default:

- `test_restock_applies_deliveries` leaves `widget` at 7 and expects `[]`, so the
  threshold must be **at most 7**.
- `test_restock_flags_low_items` has `widget` at 1 and expects `["widget"]`, so the
  threshold must be **more than 1**.

**Verified by running the suite against candidate values:** 1 fails, 2 passes,
5 passes, 7 passes, 8 fails. The admissible range is 2 to 7 inclusive.

That makes the tests a specification. Get the learner to derive the range rather
than guess a number, and the lab teaches something no slide does.

---

## Exercise 8, `slow_lookup.py`

Module 3. Quadratic nested scan, plus a correctness trap.

**Verified:** baseline runs in about 2.2 seconds at n=12000 and returns 24326
matches. Long enough that the audience feels it, short enough that nobody is
watching silence.

**The trap:** the function counts every occurrence, so duplicates in the catalogue
count each time. Optimising to a `set` for membership testing is dramatically
faster and returns the wrong number.

**Verified:** the set-based version returns 10382 instead of 24326. A `Counter` or
frequency dictionary returns 24326 correctly, roughly a thousand times faster.

A learner whose optimised version is faster and wrong is the best possible outcome
here. Surface it. It is precisely why correctness is checked before timing, and
why the lab's comparison harness asserts on the count *above* the line that prints
the speedup.

---

## Exercise 9, `sample_pr.diff`

Module 3. Findings by severity.

**Must-fix**
| # | Finding |
|---|---|
| 1 | SQL injection: `term` concatenated directly into the query, replacing a parameterised version. This is the one a bare review prompt buries. |
| 2 | Pagination off-by-one: `offset = page * PAGE_SIZE` with a 1-based page means page 1 skips the first 25 rows. Row 1 is unreachable. |
| 3 | The required-parameter check on `q` was deleted, so `term` can be None and still reaches the query |
| 4 | `int(request.args.get("page", 1))` raises on non-numeric input, returning a 500 |
| 5 | `MAX_CONTENT_LENGTH = None` removes the body size limit application-wide |

**Cosmetic noise**, which is what a bare prompt reports instead: import spacing,
`sqlite3.connect( DB )` spacing, a dict comprehension replaced with an append loop,
`PAGE_SIZE=25` without spaces, `for r in rows :` spacing, and a new `order_total`
helper that is unused and untested.

Round 1 (a bare "review this PR") reliably reports the cosmetic items and buries
finding 1. Round 2 (role, severity categories, and an explicit instruction to
ignore formatting) reliably finds it. That contrast is the entire lab.

Note the lab document deliberately does not *promise* Round 1 will fail. It asks
the learner to measure where the first critical finding appears in the output.
Keep it that way: a published video cannot guarantee a model's behaviour.

---

## Exercise 10 to 12, Module 4 reference scripts

No planted defects. These are corrected reference implementations replacing vendor
material that is outdated or internally inconsistent.

| File | Why it exists |
|---|---|
| `verify_key.py` | Pre-flight gate. Diagnoses the four common `.env` failures specifically. Reports key presence and length only, never the value, because this runs on camera. |
| `minimal_call.py` | Replaces the vendor script, which hardcodes an outdated model identifier. |
| `cli_reference.py` | Exercise 11 target state. Injection-resistant tagged template. |
| `history_starter.py` | Fallback for Exercise 12, which otherwise hard-depends on a finished Exercise 11. |

### The Exercise 12 design, and why it is not in the starter file

`history_starter.py` carries a designed lesson: the two real constraints (a
PostgreSQL requirement and a controlled tag vocabulary) sit **outside** the last
three messages, and the noise (repo naming chatter) sits **inside** it. A naive
sliding window of three messages loses both constraints.

Comments naming which messages are signal and which are noise were removed from the
starter file, because the lab instructs the learner to open it and the comments gave
away the answer before the relevant step.

There is a second, better layer here that the lab exploits: a naive **lexical**
filter also fails, because the current request shares no useful vocabulary with
either constraint message, and "Tags" versus "tag" defeats naive matching. So the
learner meets two bad proxies, recency and word overlap, before arriving at the
real pattern, which is that important context gets pinned rather than aged out.

---

## Exercise 15, `capstone_skeleton/`

Scaffolding rather than a defect artefact. Two deliberate incomplete points.

**1. `summariser.py` has TODO prompts rather than a working prompt.** Prompt design
is what the capstone is graded on, so it must not be pre-written. Do not "helpfully"
fill this in.

**2. `tests/test_service.py::test_valid_request_returns_summary` fails as shipped.**
`app.py` imports `summarise_code` directly, so patching the `summariser` module
attribute does not intercept the call. The learner must work out that the patch
target has to be `app.summarise_code`, or change the import style.

**Verified:** a fresh `pytest` run reports `3 passed, 1 failed`, with
`assert 502 == 200`. It fails with no API key and no network, so the puzzle
reproduces identically for every learner.

The hint is already in the file: the sibling test `test_upstream_failure_returns_502`
patches `app.summarise_code` and passes. Point the learner at the difference rather
than at the answer. This teaches patch targeting, which is the single most common
reason AI-generated tests fail.

### Response behaviour, verified against the running service

| Request | Response |
|---|---|
| `GET /health` | 200 |
| Non-JSON body | 400 |
| Empty `code` field | 400 |
| `code` over the character limit | 413 `{"error":"code too long","max_chars":20000}` |
| 3 MB body | 413 `{"error":"payload too large"}` from `MAX_CONTENT_LENGTH` |
| Valid request, `MODEL` unset | 502 `{"error":"service is not configured"}` |

The two 413 responses have different bodies on purpose, so the lab can ask the
learner to tell an application-level limit from a framework-level one using the
response alone. Keep both.
