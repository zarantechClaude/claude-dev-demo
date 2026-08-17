# Module 5 self-check: Advanced Developer Workflows and the Capstone

**Ten questions. Self-check only.** This is not graded and it does not gate
completion. The capstone carries completion for this programme, and several of the
questions below are about how it is marked.

Each question is tagged:

- **Core** means the module taught it directly. If you miss a Core question, go back
  to the deck section or the lab step and watch it again.
- **Stretch** means the question extends the material to a situation you were not
  shown. It is meant to be harder. Missing one is information, not a verdict.

One option per question is correct. Answer all ten before you check the key.

---

### 1. Core

You send "write a technical spec for a notes API with tagging" and get fluent prose you
could not implement from. The brief is thin, so any spec has to make choices.

What do you add to the prompt?

a. A word limit, so the document stays short enough to read carefully in one pass.
b. A named section list, and an instruction to record every unsettled choice as an
   assumption.
c. A request for the implementation code instead, so the output is something you can run.
d. A named database and web framework, so the document stops reading as abstract prose.

---

### 2. Core

You ask for the create-a-note flow as a Mermaid sequence diagram and paste the result
into your design document. It does not draw.

What is the right next step?

a. Ask for a PNG of the diagram instead, so rendering stops being your problem.
b. Describe the failure in your own words and ask for a corrected version.
c. Redraw it by hand, because generated diagram syntax is not reliable enough to use.
d. Paste the renderer's exact error back, and treat the diagram as done only once it draws.

---

### 3. Core

Your spec came back as five tickets. Each is about three weeks of work and one of them
is titled "build the backend".

What constraint do you add when you ask again?

a. One purpose per ticket, acceptance criteria someone else could test, and split the rest.
b. Every ticket must be completable in fifteen minutes, so nothing can hide inside one.
c. Skip the tickets and ask for the code, since the spec already describes the work.
d. Ask for exactly twenty tickets, which is the right number for a sprint of this shape.

---

### 4. Core

You want your pipeline to refresh docstrings on every merge. Your local workflow is an
interactive session where you approve each step. The pipeline job hangs, then times out.

Why, and what do you build instead?

a. The runner has no credit. Attach a billing account and the interactive session will
   proceed.
b. The job's timeout is too short. Raise it and the session will finish working through
   its prompts.
c. CI has no terminal to prompt, so the pipeline needs a non-interactive script that
   calls the API.
d. Pipelines cannot use AI assistance, so this has to stay a manual step before merge.

---

### 5. Core

You asked for a Dockerfile for your Flask service. It builds and the container starts.
The base image uses a floating latest tag and the start command is the framework's
development server.

What do you correct?

a. Nothing yet. It builds and it runs, so the file matches the service as it stands today.
b. Only the exposed port, so that it matches the port the application actually listens on.
c. Only the base image. A development server is a performance concern, not a correctness one.
d. Pin the base image to an explicit version, and start the service with a production server.

---

### 6. Core

Halfway through your build you change the response shape. Nothing errors. Two
generations later, new tests and new documentation keep asserting a field you removed,
and each output looks correct on its own.

What did you skip?

a. Updating your README and project context file, so the grounding still describes the
   old shape.
b. Restarting the session, so the tool is still working from a cached copy of your files.
c. Naming your framework in the prompt, so the output followed a different convention.
d. Pinning your dependencies, so a package update changed the generated field names.

---

### 7. Core

A learner posts a large file to their own summarise endpoint. The response is 413 and
no log line from their handler function appears anywhere.

What happened?

a. The provider rate limited the request before the handler could run.
b. A body-size limit in the web framework rejected the request before the handler was called.
c. The file was larger than the model's context window, so it was refused upstream.
d. The JSON library ran out of memory while parsing the request body.

---

### 8. Stretch

One submission has five endpoints, file upload and a login page, and returns a stack
trace on an empty request. Another has two endpoints, a designed prompt, and a clean
specific error on every failure path.

Which scores higher, and why?

a. The first. It demonstrates more of the programme's material inside one service.
b. They score about the same, because correctness and tests are weighted like the rest.
c. The second. Prompt design and robustness carry half the marks, and feature count
   carries none.
d. Neither can be marked. The first over-scoped and the second under-scoped the brief.

---

### 9. Stretch

You asked for a database migration script. It came back containing commands that delete
data and infrastructure, and it reads correctly.

What do you do before running it?

a. Read it, run it against staging or with a dry-run flag, and verify every identifier
   it touches.
b. Run it, and use the rollback script it also generated if anything goes wrong.
c. Convert it to Python first, so that a failure raises an exception instead of continuing.
d. Run it on a quiet day, so fewer users are affected if it behaves unexpectedly.

---

### 10. Stretch

You ask for an architecture diagram of an entire large legacy codebase. What comes back
is a tangle of overlapping boxes that nobody can read.

What is the better approach?

a. Ask for the same diagram in plain ASCII, which removes the layout problem entirely.
b. Send the whole repository again with an instruction to lay the boxes out more clearly.
c. Accept that this is a manual task, because structure is not visible from code alone.
d. Map one bounded module at a time, pass only that code, and assemble it over passes.

---

Copyright © 2026, ZaranTech LLC. All rights reserved.
