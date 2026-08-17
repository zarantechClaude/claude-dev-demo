# Module 5 deck changelog

Original: `original/Module 5 - Advanced Developer Workflows & Mini-Project.pptx`  
Revised: `revised/Module 5 - Advanced Developer Workflows & Mini-Project - REVISED.pptx`

Slide count: 24 before, 26 after.

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

> Automate documentation updates during continuous integration pipeline runs using Claude APIs.

**Now:** the bullet block was rewritten to:

> - Call the API from a non-interactive script in the pipeline. CI has no terminal to prompt.
> - Generate dynamic release notes automatically based on merged pull requests.
> - Ensure updated functions contain accurate docstrings before reaching production servers.
> - Maintain synchronized architectural documentation automatically when structural changes are merged.

**Why:** Named the actual mechanism. A pipeline cannot use an interactive tool, so the slide needs to say that the call is a non-interactive script or a headless invocation, or a learner will try to run the interactive tool in CI and fail.

### Slide 16

**Was:**

> Apply learned concepts to build a comprehensive end-to-end application from scratch.

**Now:** the bullet block was rewritten to:

> - Build one small service: a summarise endpoint and a health endpoint. That is the whole scope.
> - Experience a complete development lifecycle utilizing Claude as your coding assistant.
> - Your brief was issued at the end of Module 4. A skeleton project is provided.
> - You are graded on prompt design and failure handling, not on feature count.

**Why:** The vendor scope of an 'end-to-end application from scratch' is several times what the capstone actually is, and over-scoping is the most common reason a capstone fails. The brief is also issued at the end of Module 4, not here, because the learner needs time to build.

### Slide 20

**Was:**

> Verify your application strictly adheres to functional and architectural requirements.

**Now:** the bullet block was rewritten to:

> - The service runs, both endpoints respond, and invalid input returns a clear error.
> - Ensure generated code compiles successfully and executes without unexpected runtime exceptions.
> - Validate the system handles erroneous inputs securely without exposing sensitive data.
> - Missing key, empty input, oversized payload and upstream failure each fail cleanly.

**Why:** Points at the markable rubric. As delivered, the three evaluation slides were adjectives with no thresholds, which two reviewers could not mark consistently.

## Added

### New slide at position 4: Exercises in This Module

- Exercise 13: Turn a feature brief into a spec and tickets. 18 minutes.
- Exercise 14: Generate and correct a configuration file. 12 minutes.
- Exercise 15: Build the summariser service. 35 minutes, across three videos.
- Exercise 15 is the capstone build itself, not a rehearsal for it.

**Why:** Section map for recorded navigation, and the place to state that Exercise 15 is the capstone rather than a separate lab.

### New slide at position 23: How the Capstone Is Marked

- Prompt design, 25 points. A real template: role, task, tagged input, output constraints.
- Robustness, 25 points. Four named failure paths each return a clean, specific error.
- Correctness 15, tests 15, structure and responsible practice 10.
- Reflection, 10 points. What you corrected, and which prompt change mattered most.
- Full thresholds are in the capstone brief. Read them before you start building.

**Why:** The vendor evaluation slides carried no thresholds, so nothing was markable. The capstone carries completion for this programme, so the criteria have to be defensible and visible to the learner in advance.

## Not changed, but flagged

Nothing else in this deck was edited. Anything you disagree with above can be
reverted from `original/` without affecting the labs, which do not depend on
slide wording.
