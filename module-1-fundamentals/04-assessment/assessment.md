# Module 1 self-check: Fundamentals of Claude for Developers

Ten questions. One correct option each.

This is a self-check, not a graded test. Nothing here gates your progress through
the course. Its only job is to show you which parts of Module 1 you have not
settled yet, so answer from what you know rather than looking anything up.

Each question is tagged.

- **Core** means Module 1 taught it directly, on a slide or in an exercise.
- **Stretch** means you have to reason one step past what you were shown. Three of
  the ten are Stretch. Missing one of those is not a sign the module failed you.

Answers are not in this document. Your trainer holds the key.

---

### 1. Core

You attached your team's repository to a Claude project in the browser, then asked
Claude to fix a bug and raise a pull request. It describes the bug accurately and
hands you a patch, but no branch and no pull request ever appear. Why?

a. The sync completed for source files, but raising a pull request also requires the
   default branch to be unprotected first.
b. Pull request creation becomes available once the repository owner grants write
   scope to the connected project in its settings.
c. Attaching a repository supplies file contents as reading material, so nothing in
   that workflow can write to the repository.
d. The request needed to name a target branch, otherwise the change is prepared but
   never submitted for review.

### 2. Core

Your prompt is split into four labelled sections. One line reads: "Standard library
only, no third-party packages." Which section does that line belong in?

a. Context, because it describes the environment the finished code has to run in.
b. Instruction, because it tells Claude what it is being asked to do here.
c. Example, because it shows the shape of an answer you would accept.
d. Constraints, because it states what the response must not do.

### 3. Core

A production log file you need parsed is full of customer email addresses, session
tokens and plain-text passwords. You want Claude to write the parser. What do you do
first?

a. Mask the tokens, passwords and personal fields locally, then paste only the
   sanitised sample.
b. Leave the log intact and open the prompt with an instruction never to retain or
   repeat any sensitive value it contains.
c. Split the file into many small chunks, so no single prompt carries a meaningful
   concentration of sensitive values.
d. Send it through the API rather than the browser, since programmatic traffic falls
   outside the retention policy that covers chat.

### 4. Stretch

Your security policy forbids source code leaving an air-gapped build host. A
colleague suggests installing Claude Code on that host, on the grounds that it is a
terminal tool and therefore runs locally. What is the flaw in that reasoning?

a. Claude Code is intended for interactive desktop use, which makes a shared build
   host the wrong deployment target for it.
b. It would work, but only once the repository has been indexed into a local vector
   database for the tool to search.
c. Nothing is wrong with it. A command line tool does its reasoning on the machine
   it is installed on, which is the point of it.
d. It runs locally but the reasoning does not. It still calls a hosted service, so
   the code leaves the host.

### 5. Core

You paste a very long data dump plus two lines of instruction, and ask for a script
that counts records. The script you get back refers to fields that do not exist in
your data. What is the most useful correction?

a. Convert the data into a different serialisation format first, so that the field
   names are easier to pick out.
b. Cut the pasted material down to a short representative sample plus the real field
   names, then restate the instruction.
c. Assign a persona at the top of the prompt, so the answer comes from a data
   engineering perspective rather than a general one.
d. Spread the data dump across several consecutive messages, so that each individual
   message stays comfortably short.

### 6. Core

You have two jobs this sprint. One is untangling an unfamiliar service with no
documentation. The other is generating hundreds of near-identical test fixtures from
a fixed template. How should you choose a model?

a. Use one model for both, and pin your team documentation to the exact version
   identifier you validated it against.
b. Use the fastest option available for both jobs, then re-run anything that comes
   back wrong the first time.
c. Use the most capable tier for the unfamiliar service and a faster tier for the
   fixture generation.
d. Take whichever version currently sits highest in the published coding comparisons
   for code generation.

### 7. Core

A review of your file reports a serious problem and cites line 84. Line 84 is blank,
and you cannot find the construct it describes anywhere in the file. What is the
right move?

a. Drop the finding. A finding you cannot anchor to a line in the file is not a
   finding.
b. Keep it as a Fail, because the risk it describes is real even if the line
   reference has drifted by a few lines.
c. Ask for the review again with line numbers added to every source line, then accept
   whichever version cites a real one.
d. Carry it into your notes as Needs review, since a plausible risk deserves a place
   in the notes even without a line.

### 8. Core

Claude's explanation of a short function you did not write reads clearly and
confidently. You have not run the code. What is the cheapest check that tells you
whether the explanation describes the code rather than its intent?

a. Ask it to rate its own confidence in the explanation and to flag any part of it
   that it is unsure about.
b. Give it one concrete input, ask it to list every value returned in order, then
   check that list against the code yourself.
c. Ask the same question again in a new conversation, and compare the two
   explanations for anything that differs.
d. Ask for the explanation again as a line by line commentary, which is harder to
   produce from intent alone.

### 9. Stretch

A teammate has your repository attached to a Claude project. She asks why a
particular line was changed last month, gets a confident answer, and quotes it in a
design discussion. What should you tell her?

a. It is reliable, because the attached repository brings the log of the commits that
   produced the current files with it.
b. It is reliable for the default branch only, because other branches are not part of
   what the attachment syncs.
c. It is reliable as long as the repository still has its original commit messages,
   which are read alongside the files.
d. Treat it as a guess from the current file contents. The attachment carries files,
   not history.

### 10. Stretch

You are about to save a prompt that worked well into a shared team template file. It
contains an internal hostname, a sample record with a real colleague's email address,
and a database password. What do you do before saving?

a. Save it as it is but restrict the file to your team, since the risk lies in what
   leaves the company rather than what sits inside it.
b. Remove the password, and keep the hostname and the address, because those two are
   what make the template usable by anyone else.
c. Replace all three with placeholders. A saved template repeats whatever is in it,
   every time anyone uses it.
d. Keep the file private to you, and pass the prompt structure on verbally whenever a
   colleague asks you for it.

---

Copyright © 2026, ZaranTech LLC. All rights reserved.
