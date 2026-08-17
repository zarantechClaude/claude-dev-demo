# Exercise 13: Turn a Feature Brief into a Spec and Tickets

**Module 5** | **18 minutes** | **You need:** Browser, a Mermaid renderer, three markdown files

## What you will do

You will take a one line feature brief and come out with three artefacts: a technical
spec, a high level design with a diagram that renders, and tickets a developer could pick
up. The work that decides whether any of it is any good happens before you send the first
prompt.

## Before you start

1. Claude open in your browser. No terminal and no API key for this exercise.
2. Three empty markdown files in a folder of your own: `spec.md`, `design.md`,
   `tickets.md`.
3. A Mermaid renderer you have already tested with any small diagram. Your editor's
   markdown preview or a Mermaid live editor both work. Test it now, not in Step 7.

Do not use your real issue tracker for this. Paste into markdown instead. A recorded
exercise is not the moment to put a live workspace on screen.

## The brief

> Build a notes API with tagging.

That is the entire brief. It is thin on purpose, because thin is what you actually get.

You have seen this system before. The conversation in Exercise 12 was two developers
building it, and the constraint you lost there was the kind of decision that belongs in
the document you are about to write. A decision recorded in a spec does not have to
survive a conversation.

## Steps

### Step 1: Split what is known from what is missing

Two columns, written down before you prompt anything.

Known: there is a backend service, there are notes, there are labels attached to notes,
and there is a relationship between them.

Missing: users, permissions, storage, search, whether tags are free text or a controlled
list, what deletion means, and whether any of this is authenticated.

That second column is longer than the brief. That is normal and it is the reason this
step exists.

### Step 2: Write the questions you would ask a product owner

Before prompting, list what you would ask a human. Aim for at least seven:

- Who can create, edit, delete and view a note?
- Can a note carry more than one tag?
- Free text tags or a controlled vocabulary?
- Is authentication required, and is it in scope?
- Does the API need search or filtering?
- Soft delete or hard delete?
- Are tags case sensitive?

Do this by hand. If you let the model generate the questions and answer them in the same
breath, you get a spec built on assumptions you never saw it make, and you will not be
able to find them later.

> **Pause the video here.** Write both columns and your question list before you prompt.

### Step 3: Compare a weak spec prompt with a strong one

This is the prompt most people send:

```
Write a technical spec for a notes API with tagging.
```

Send it, skim the result, then send this one in a new conversation:

```
Act as a senior software architect. Draft a technical specification for a notes API with
tagging.

Include, as separate sections: problem statement, goals, non-goals, user stories,
functional requirements, non-functional requirements, data model, API endpoints,
validation rules, error handling, and assumptions.

Keep it concise but detailed enough to implement from. Where the brief does not tell you
something, put your choice in the assumptions section and say why you chose it. Do not
resolve an ambiguity silently.
```

Two differences do the work, and neither of them is the word "architect".

The first is the named section list. It turns a request for prose into a request for a
document with a shape, and a shape is something you can check for completeness.

The second is the last instruction. Both prompts will make assumptions, because the brief
is too thin not to. Only one of them tells you where they are. Save the second result as
`spec.md`.

### Step 4: Review the draft against your own questions

Check the document has all eleven sections, then do the part that matters. Take your Step 2
question list and, for each question, find the place in the spec where it is answered.
Mark each one:

| Marking | Meaning |
|---|---|
| Answered | The spec settles it, and you agree with the answer |
| Assumed | The spec settles it, correctly labelled as an assumption |
| Guessed | The spec settles it and did not tell you it was choosing |
| Missing | The spec does not address it at all |

The `Guessed` row is the one to count. Every item in it is a decision that entered your
document without a decision being made. On a real feature, those are what surface three
weeks later as a disagreement about what was agreed.

> **Pause the video here.** Mark every question on your list.

### Step 5: Refine with targeted follow-ups

Do not accept a first draft, and do not ask for "a better version". Ask for specific
additions, one per turn, so you can see what each one changed:

- Add explicit authentication assumptions and mark them as assumptions.
- Add pagination and filtering to the endpoint list.
- Define soft delete behaviour, including what happens to a deleted note's tags.
- Expand the data model to show the note to tag relationship, including cardinality.
- Move every item I marked as guessed into the assumptions section.

### Step 6: Ask for the high level design

```
Based on this specification, produce a high level design for the notes API. Cover
components, request flow, storage approach, the tagging relationship, the validation
flow, and external dependencies.

Keep it implementation agnostic. Do not name specific products or libraries.
```

Then check it covers the API layer, the business logic layer, persistence, the tag
relationship, error handling, and where the security boundary sits. If it reads as
abstract to the point of being unfalsifiable, ask it to be concrete about the request
flow. Save it as `design.md`.

### Step 7: Get the flow as a diagram, and render it

```
Express the "create a note with tags" request flow as a Mermaid sequence diagram. Include
the validation step and the failure path where a tag is not in the allowed vocabulary.
Output only the diagram in a fenced mermaid block.
```

Paste it into your renderer.

A diagram that does not render is not a deliverable. Generated Mermaid usually renders and
occasionally needs a syntax nudge, so if it fails, paste the exact error back rather than
describing it. Add the diagram to `design.md` only once you have seen it draw.

> **Pause the video here.** Render the diagram before you continue.

### Step 8: Break the spec into tasks

```
Convert this specification into implementation tasks for an issue tracker. Group them by
workstream. Each task must be small enough for one developer to finish inside a short
sprint. Give each one a title and a two sentence description.
```

Check the set covers the whole lifecycle, not just the endpoints: data model, endpoints,
validation and error handling, tests, documentation, and deployment. Ask it to split
anything too broad and to group anything so small that it is not worth tracking.

### Step 9: Make them ticket shaped, then validate each one

```
Rewrite these as issue tracker tickets. For each: title, description, acceptance criteria
as a checklist, and dependencies by ticket title. Concise, in the register a developer
would expect in a tracker.
```

Save as `tickets.md`, then check every ticket against five things:

1. One clear title.
2. One purpose. If the description contains "and also", split it.
3. Acceptance criteria that can be tested by someone who did not write the ticket.
4. Dependencies that point backwards, not in a circle.
5. No hidden scope.

"Implement the note creation endpoint" is a ticket. "Build the backend" is a workstream
wearing a ticket's clothes.

### Step 10: Trace it end to end

Three checks, and all three are quick:

1. Every ticket traces back to a requirement in `spec.md`.
2. Every requirement in `spec.md` is covered by at least one ticket.
3. The components in `design.md` and the workstreams in `tickets.md` describe the same
   system.

Where a ticket has no requirement behind it, either the spec is incomplete or the ticket
is invented. Both are worth knowing. This is the check no generation step performs for
you, because each artefact was produced from the last one and none of them was checked
against the first.

## What good looks like

- `spec.md`, `design.md` and `tickets.md` all exist, and the diagram in `design.md`
  renders.
- The spec has an assumptions section, and you moved everything you marked as guessed into
  it.
- You can point at one place where the model resolved an ambiguity silently, and say what
  the resolution was.
- Every ticket has testable acceptance criteria and one purpose.
- You can trace any ticket back to a line in the spec, and any line in the spec forward to
  a ticket.

## Common problems

| Problem | Cause | Fix |
|---|---|---|
| The spec is fluent and says nothing you could implement from | The prompt asked for a spec, not for named sections | Use the Step 3 prompt. Ask for the section list explicitly |
| The assumptions section is empty | The model resolved everything silently | Re-ask: "list every choice you made that the brief did not specify" |
| The Mermaid block does not render | Small syntax error, often in participant names or arrows | Paste the exact renderer error back. Do not describe it |
| Tickets are epics | "Small enough for one developer in a short sprint" was omitted or ignored | Ask it to split any ticket whose acceptance criteria run past four items |
| Forty tickets, several trivial | No lower bound given | Ask it to group anything under half a day |
| Acceptance criteria you cannot test | Criteria written as intentions rather than observations | Re-ask for criteria phrased as "given, when, then" |
| Dependencies form a loop | Generated per ticket, with no global view | Ask for the tickets in dependency order and check the first three have no dependencies |
| The design and the tickets disagree | Each artefact was generated from the previous one, and nothing checked the pair | Step 10. This check is yours to run |

## Going further

1. Take the two constraints you know this system has from Exercise 12 and check whether
   your spec captured either of them. Where it did not, add them and see how many tickets
   change. That is the cost of a constraint arriving late, measured rather than asserted.
2. Ask for the same spec a second time, in a fresh conversation, from the same brief. Diff
   the two assumptions sections. What is stable across both runs is what the brief actually
   implies. What differs is where you need a human to decide.

Copyright © 2026, ZaranTech LLC. All rights reserved.
