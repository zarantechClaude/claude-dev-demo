# Module 4 answer key

> **Trainer-facing. Do not publish this file to learners.** It is the companion to
> `assessment.md`, which contains no answers.

Slide numbers below refer to the **revised** deck,
`01-deck/revised/Module 4 - Building with the Claude API (Backend & Integration) - REVISED.pptx`,
which is what learners watch. The revised deck has 28 slides against the vendor's 25,
so these numbers do not match the original deck. Three of the added slides exist
specifically to make questions on this assessment answerable.

## Answers

| Q | Answer | Tag | Taught in | Why this answer, and what the question diagnoses |
|---|---|---|---|---|
| 1 | c | Core | Slide 12 "Encoding System and User Instructions"; slide 13 bullet 5; Exercise 11 Step 4 | The system prompt is a request parameter, not a message. A learner who misses this is carrying a mental model from another provider's API, which is exactly where the mistake arrives. It fails at the API rather than in the editor, so it is worth recognising on sight. Point them at Exercise 11's Common problems row on the system role. |
| 2 | a | Core | Slide 12 bullet 5; slide 15 bullet 2; Exercise 11 Step 3 | Tags alone are decoration and a rule with no boundary has nothing to point at. Both together are the defence. A learner picking b believes sanitising is sufficient, which is the misconception Exercise 11 Step 6 is built to break. c and d are magical thinking about parameters and encoding. If they miss this, re-run Exercise 11 Step 6 with both template versions. |
| 3 | d | Core | Slide 13 bullets 1 and 2 | Alternating roles. Two user turns in a row is a common cause of a confusing error, and this scenario is how it reaches production: a queue or a webhook stores two inbound messages before a reply exists. c is attractive because it sounds structural. Missing this usually means slide 13 was skipped, since it is not on the vendor deck at all. |
| 4 | b | Core | Slide 13 bullets 3 and 4 | Prefilling the assistant turn constrains the opening of the reply. a is the single most common porting error, because another provider does have that parameter. c stops the tail and leaves the preamble, which is the half-fix that looks like a fix. d is prompt begging. Diagnoses whether the learner knows the messages list itself is a control surface. |
| 5 | c | Core | Slide 18 bullets 1 and 2; Exercise 12 Steps 1 and 2 | The API is stateless. Multi-turn conversation is something the developer builds by resending context, not a feature to switch on. d is the sharpest distractor because slide 19 does talk about session identifiers, but those live in your database and are your bookkeeping, not the provider's. If they miss this, everything in Exercise 12 will feel arbitrary. |
| 6 | a | Core | Slide 8 bullet 1; slide 16; Exercise 10 Step 7 | The context window and the output ceiling are two different limits. A short prompt cannot have exhausted the window, so this is the output cap. The second half of the option matters as much as the first: raising the cap and asking for brevity are different fixes for different intentions. b is the reflex answer and it wastes real debugging time. |
| 7 | d | Core | Slide 9 bullets 4 and 5; Exercise 10 Step 3 | A key committed once is in the history, so deletion in a later commit does not help. Rotation first, then the hygiene. b is the most instructive wrong answer, because gitignoring a tracked file changes nothing about the past. Exercise 10 puts `.gitignore` before `.env` for this reason and says so on camera. |
| 8 | b | Stretch | Slide 22, all five bullets; slide 17 bullet 2 | Caching a large unchanging prefix is a cost and latency optimisation, and the order requirement is stable material first, variable material last. c is the misconception slide 22 exists to correct: caching does not raise a context limit. d trades correctness for size. Stretch because the learner has to apply the ordering rule to a service they were not shown. |
| 9 | a | Stretch | Exercise 12 Steps 4 to 6; slide 21 bullet 1 | Recency is a poor proxy for importance, and it fails in a direction: constraints get stated once and early, chatter is constant and recent. d is the best distractor in the module, because word overlap is the second bad proxy and it fails for the same reason. b treats a design flaw as a tuning problem. Stretch because the scenario is not the lab's conversation. |
| 10 | c | Stretch | Slide 23 bullets 2 and 3; slide 24 bullet 2 | MCP is a standard interface, so you stop writing a bespoke bridge per system. b is the "the model reaches into my network" misconception, and a is its cloud twin. d contradicts slide 24, which is explicit that you define the input schema. Stretch because the deck teaches what MCP is, and the question asks what adopting it buys in a situation the deck does not describe. |

## Distribution check

Counted, not estimated. Requirement is at least two per option across the ten.

| Option | Count | Questions |
|---|---|---|
| a | 3 | 2, 6, 9 |
| b | 2 | 4, 8 |
| c | 3 | 1, 5, 10 |
| d | 2 | 3, 7 |

Total 10. Every option carries at least two correct answers, so answering one letter
throughout scores 20 to 30 percent, which is guessing.

## Tag counts

Seven Core: 1, 2, 3, 4, 5, 6, 7.
Three Stretch: 8, 9, 10.

## Notes for the trainer

1. Questions 3, 4 and 8 are only answerable from slides added in the revision. If a
   learner is working from the vendor deck, they cannot pass those three. Check which
   deck they watched before concluding anything about their understanding.
2. Questions 1, 3 and 4 all diagnose the same underlying thing, which is whether the
   learner has understood the shape of the request. A learner who misses two of the
   three should redo Exercise 11 rather than reread the slides.
3. No question here depends on a specific context-window size, output cap or price,
   and none names a model version. If a future revision reintroduces one, it will rot
   the same way the vendor's question 5 did.

---

Copyright © 2026, ZaranTech LLC. All rights reserved.
