# Lab document authoring spec

Every lab document in this repo follows this structure. If you write a new lab or
rewrite an existing one, match this exactly, so that fifteen documents read as one
programme rather than fifteen documents.

## File location and naming

```
module-N-<slug>/03-labs/exercise-NN-<slug>/lab.md
module-N-<slug>/03-labs/exercise-NN-<slug>/lab.docx     generated from lab.md
module-N-<slug>/03-labs/exercise-NN-<slug>/starter/     starter code, if any
module-N-<slug>/03-labs/exercise-NN-<slug>/vendor-original/   the vendor PDF
```

`lab.md` is the source of truth. The DOCX is generated from it. If you edit the
DOCX directly your change is lost on the next generation, so edit the markdown.

## Required structure

```markdown
# Exercise NN: <Title>

**Module N** | **NN minutes** | **You need:** <browser | terminal | API key | pytest>

## What you will do
One short paragraph, second person, stating the outcome rather than the activity.

## Before you start
Numbered prerequisites. Only what this exercise needs. If there is nothing, say
"Nothing beyond a browser."

## Steps
### Step 1: <imperative title>
...
> **Pause the video here.** <what the learner does before resuming>

## What good looks like
The observable end state. A learner should be able to check themselves against
this without an instructor.

## Common problems
| Problem | Cause | Fix |

## Going further
Optional. One or two extensions for a learner who finished early. Never required.
```

## Voice rules

This is a recorded course. The learner is watching a video alone, not sitting in
a room being facilitated. Every instruction is addressed to the learner in second
person.

| Never write | Write instead |
|---|---|
| "Ask learners to create a project folder" | "Create a project folder" |
| "Have learners compare the two versions" | "Compare the two versions" |
| "Learners should write down their observations" | "Write down what you notice" |
| "Discuss with your group" | Cut it, or state the two positions yourself |
| "The instructor will provide a snippet" | "Open `starter/<file>`" |

If a step has no pause instruction and the learner is expected to do something,
the step is incomplete. A recorded lab has no natural moment where the room
catches up, so the pause has to be explicit.

## Content rules

1. **State the duration in the header** and make it honest. Every vendor lab
   omitted this and it is the reason the programme was mis-scoped.
2. **Never name a Claude model version.** Write `MODEL` and point at the
   configuration. If a step needs a model id, the step is to look up the current
   one in the official documentation and put it in `.env`.
3. **`ANTHROPIC_API_KEY` only.** Never `CLAUDE_API_KEY`.
4. **Python only.** No Node or Java branches. Where the vendor lab offered a
   choice, pick Python and add one line noting the equivalent exists in other
   stacks.
5. **Point at real starter files by path.** Seven vendor labs told the instructor
   to supply a file and supplied none. Every such reference now resolves to a file
   in `starter/`.
6. **Do not reveal a planted defect in the lab document.** The learner is supposed
   to find it. Defects live in `docs/lab-defect-register.md`, which is trainer-only.
7. **No em dashes.** No citation residue. No notes addressed to the course author.

## Prompts

Where a lab asks the learner to prompt Claude, give the prompt as a fenced block
they can copy, and then say what to look for in the response. A lab that says
"ask Claude to review the code" without showing a usable prompt teaches nothing,
because the quality of the prompt is the entire skill being taught.

Where a lab contrasts a weak prompt with a strong one, show both, in that order,
and name the specific difference. That contrast is usually the real lesson.

## Length

Two to four pages. If a lab runs longer, it is either two labs or it needs a
split into numbered parts with explicit stopping points, as Exercise 15 does.
