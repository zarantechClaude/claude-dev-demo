# Module 1 deck changelog

Original: `original/Module 1 - Fundamentals of Claude for Developers.pptx`  
Revised: `revised/Module 1 - Fundamentals of Claude for Developers - REVISED.pptx`

Slide count: 25 before, 27 after.

This changelog is generated from the same declaration that drives the edits,
so it cannot drift from what was actually changed.

## How to use this

If your Google Slides copy is the master, apply these changes there and ignore
the revised PPTX. If you would rather adopt the revised file, import it and it
becomes the master. Do not do both, or the two will diverge.

Slide numbers under 'Changed' refer to the **original** deck. Slide numbers
under 'Added' refer to the **revised** deck.

## Changed

### Slide 4

**Was:**

> It securely processes massive codebases using its large context window.

**Now:** the bullet block was rewritten to:

> - Claude is an advanced AI assistant developed by Anthropic.
> - It engages in open-ended conversations and handles complex technical tasks.
> - Claude serves as a powerful coding partner for modern developers.
> - A large context window lets it work across a whole codebase in one pass.

**Why:** Removes an unsupported security claim. Processing a codebase is not inherently 'secure', and the word invites a compliance question the slide cannot answer.

### Slide 6

**Was:**

> It runs tests and delivers committed code directly to you.

**Now:**

> It runs tests, and reads a project context file you keep in the repo.

**Why:** Adds the persistent project context file, which is the single most useful Claude Code habit and is never mentioned in either the Module 1 or Module 2 deck.

### Slide 7

**Was:**

> Claude generates fewer hallucinations, ensuring more reliable technical responses.

**Now:**

> It states uncertainty rather than inventing an API that does not exist.

**Why:** Softens an unevidenced comparative claim against unnamed competitors. We cannot substantiate a hallucination-rate comparison, and organisational guidance forbids quoting benchmark results.

### Slide 8

**Was:**

> Claude Fable 5, Opus 5 and Sonnet 5 leads industry benchmarks in coding proficiency.

**Now:** the bullet block was rewritten to:

> - Claude models come in tiers. Pick the tier, not a version number.
> - Use the most capable tier for architecture, debugging and unfamiliar code.
> - Use a faster tier for repetitive, well-specified, high-volume work.
> - Version identifiers change often. Read the current list from the docs.

**Why:** Three problems in one slide: it named specific model versions, which dates a published video permanently; it claimed benchmark leadership, which we do not quote; and 'leads' disagreed with its plural subject.

## Added

### New slide at position 4: Exercises in This Module

- Exercise 1: Explore Claude's interface and explain sample code. 12 minutes.
- Exercise 2: Structure a developer prompt. 12 minutes.
- Exercise 3: Apply a code review checklist. 15 minutes.
- All three run in the browser. No terminal and no API key in this module.

**Why:** A recorded course is navigated by section rather than by the trainer's voice, so each module needs a visible map of what is coming.

### New slide at position 8: Repo as Context, Repo as Workspace

- Attaching a repository in the Claude app syncs file contents as reading material.
- That is context. Claude can read and reason about it, and nothing more.
- It grants no commit access, no pull requests and no commit history.
- Claude Code is what operates on a repository: it edits files and runs commands.
- If you need something changed on disk, you need the workspace, not the context.

**Why:** This is the most useful distinction in the whole programme and no slide taught it. It is also the single most common source of learner confusion, and it is directly tested by the Module 1 assessment.

## Not changed, but flagged

Nothing else in this deck was edited. Anything you disagree with above can be
reverted from `original/` without affecting the labs, which do not depend on
slide wording.
