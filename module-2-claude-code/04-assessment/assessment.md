# Module 2 self-check: Claude for Coding Tasks

Ten questions. One correct option each.

This is a self-check, not a graded test. Nothing here gates your progress through the
course. Its only job is to show you which parts of Module 2 you have not settled yet,
so answer from what you know rather than looking anything up.

Each question is tagged.

- **Core** means Module 2 taught it directly, on a slide or in an exercise.
- **Stretch** means you have to reason one step past what you were shown. Three of the
  ten are Stretch. Missing one of those is not a sign the module failed you.

Answers are not in this document. Your trainer holds the key.

---

### 1. Core

You are writing the project context file for a repository you work in every day.
Which of these belongs in the file rather than in a prompt?

a. "Add pagination to the orders endpoint today, and update the tests that cover it."
b. "Python 3.11 and pytest. Nothing under vendor/ is ours to change."
c. "Yesterday's migration failed halfway through, so skip the seed step for now."
d. "Work on the two files I am about to paste, and ignore the rest of the tree."

### 2. Core

You join a large repository and want Claude Code to understand the system before you
ask it for any code at all. Which approach gives it the most useful picture with the
least noise?

a. Hand over the dependency manifest and ask it to infer the architecture from the
   libraries the project depends on.
b. Archive the whole repository and hand that over, so every file is available before
   the first question is asked.
c. Write a short file at the repository root covering purpose, stack, layout, what works,
   and what is off limits.
d. Hand over the ignore file and ask what the exclusions imply about the way the
   project is organised.

### 3. Core

Claude Code keeps writing queries for the wrong database, session after session, even
though you correct it every time. Your README describes the product but says nothing
about the data layer. What fixes this properly?

a. Correct it earlier in each session, before you ask for anything that touches the
   database at all.
b. Paste the schema at the start of every session, so the dialect is present in the
   conversation from the first message.
c. Ask it to state which database it is assuming before it writes a query, then correct
   the assumption when it is wrong.
d. Record the database and its dialect in the project context file, which is read at
   the start of every session.

### 4. Core

Your refactor prompt returned cleaner, better organised code. After you deploy it, no
existing user can log in. The change it made is defensible security advice. What was
missing from the prompt?

a. A request for tests covering the login path, delivered alongside the refactored
   code.
b. A statement of what must not change, including that existing stored credentials
   stay verifiable.
c. A restriction to one file at a time, which would have kept the change small enough
   to review closely.
d. An instruction to explain every change, which would have made the consequence
   visible before the deploy.

### 5. Core

You asked for a registration endpoint from a user story and said nothing about how
credentials should be handled. The code runs and stores users successfully. What is the
safest assumption about it?

a. Credential handling was unspecified, so treat it as unreviewed and state the
   requirement explicitly.
b. Modern assistants apply current security defaults to authentication code, so the
   handling is probably sound already.
c. The user story asked for a secure account, so that requirement was carried into the
   implementation you received.
d. It is acceptable for a draft, because how credentials are stored is a deployment
   concern rather than a code concern.

### 6. Core

Claude writes a function and a test suite for it, then reports that it has run the
tests and they all pass. What should you conclude?

a. The suite is consistent with the function, so the remaining risk sits in the
   behaviour the tests do not cover.
b. The claim summarises the generated assertions, and it holds for a pure function with
   no side effects.
c. Nothing yet. Nothing ran. Execute the suite yourself before you believe the code or
   the tests.
d. The tests were probably written from the description rather than from the code, so
   ask for them a second time.

### 7. Core

You asked for comments on an undocumented module and got one comment per line
restating the syntax. How do you re-prompt?

a. Ask for each function's purpose and the edge case behaviour visible in the code, with
   no line by line narration.
b. Ask for a comment on every line again, and require each one to be longer and more
   detailed than last time.
c. Ask for a different documentation format, on the grounds that a stricter format
   forces a higher level of description.
d. Cap the number of comments allowed per function, so that the ones which survive have
   to carry more meaning.

### 8. Stretch

You split a module in two last month. Claude Code keeps generating code against the old
single-module layout, and you keep correcting it in the chat. What is the durable fix?

a. Paste the new layout at the start of each session, since a pasted reminder is read
   before anything else in the conversation.
b. Delete the old module entirely, so nothing left in the repository can suggest the
   previous shape to anyone.
c. Ask it to search the repository for the old import path before it generates
   anything new.
d. Update the project context file to describe the new layout, because a stale file
   keeps producing the old shape.

### 9. Stretch

A single prompt split a two thousand line file into five modules. The structure looks
right and the imports between the new modules do not resolve. What workflow avoids this
next time?

a. Ask for the same split again in a fresh session, then compare the two results before
   you keep either of them.
b. Supply the list of standard library modules available, so that invented import names
   become less likely.
c. Ask for a boundary plan first, agree it, then extract one boundary per prompt and
   check each before the next.
d. Ask for the file to be rewritten from scratch against the intended structure, rather
   than moved a piece at a time.

### 10. Stretch

Generated tests for a function that writes to a shared staging database pass on your
machine. A colleague then notices that staging rows have disappeared. What was missing
from the prompt?

a. An instruction to stub the external calls with a mocking library instead of letting
   the tests reach the real system.
b. An instruction to wrap every database call in error handling, so that a failing test
   cannot leave data changed behind it.
c. A specific test runner version, because the default configuration permits tests to
   perform destructive writes.
d. A teardown step restoring the staging data to its previous state after each test run
   has finished.

---

Copyright © 2026, ZaranTech LLC. All rights reserved.
