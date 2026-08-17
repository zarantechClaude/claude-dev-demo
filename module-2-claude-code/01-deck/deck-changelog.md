# Module 2 deck changelog

Original: `original/Module 2 - Claude for Coding Tasks (Claude Code) .pptx`  
Revised: `revised/Module 2 - Claude for Coding Tasks (Claude Code) - REVISED.pptx`

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

### Slide 6

**Was:**

> Share relevant project files and code snippets clearly using proper structural markdown formatting.

**Now:**

> Let Claude Code read the repository directly rather than pasting files into a chat.

**Why:** Reframes from pasting into a chat window to Claude Code reading the repository directly, which is what the module is nominally about. Exercise 4 had the same problem and was rewritten to match.

### Slide 7

**Was:**

> Upload highly focused code snippets rather than entire unrelated directories to maintain clarity.

**Now:**

> Point Claude at the specific files that matter rather than the whole tree.

**Why:** Same reframe. 'Upload' is the web-app model, not the Claude Code model.

### Slide 13

**Was:**

> Paste outdated legacy functions and ask Claude to modernize the programming syntax completely.

**Now:** the bullet block was rewritten to:

> - Ask for modernised syntax, and state explicitly what must not change.
> - Improve overall code readability by requesting better variable naming and logical code grouping.
> - Extract complex nested conditionals into separate cleaner helper functions for much easier maintenance.
> - Identify hidden performance bottlenecks and let the AI suggest optimized algorithmic structural alternatives.

**Why:** Adds the preservation constraint, which is the core lesson of Exercise 5. A refactor prompt that does not state what must not change will produce correct improvements that are also breaking changes.

## Added

### New slide at position 4: Exercises in This Module

- Exercise 4: Create a project context file for Claude Code. 12 minutes.
- Exercise 5: Refactor a registration endpoint safely. 20 minutes.
- Exercise 6: Add documentation and tests to undocumented code. 22 minutes.
- This module needs Claude Code installed locally. No API key yet.

**Why:** Section map for recorded navigation.

### New slide at position 8: The Project Context File

- Claude Code reads a CLAUDE.md at your repository root automatically.
- Put in it what a new colleague would need: stack, conventions, and what not to touch.
- A file beats a pasted message: it survives every session and it is version controlled.
- Update it when the design changes, or the assistant keeps building the old shape.
- Exercise 4 has you write one for a project of your own.

**Why:** Largest single content gap in the programme. Module 2 has six slides on organising project context and never mentions the file that does it, and no slide in the deck carries any code.

## Not changed, but flagged

Nothing else in this deck was edited. Anything you disagree with above can be
reverted from `original/` without affecting the labs, which do not depend on
slide wording.
