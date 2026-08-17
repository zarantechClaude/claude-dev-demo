# Exercise 2: Structure a Developer Prompt

**Module 1** | **12 minutes** | **You need:** Browser

## What you will do

You will take a vague one-line request, rebuild it as a four-part prompt using
instructions, context, examples and constraints, and prove to yourself which part
changed the output most. You finish with a reusable template.

## Before you start

1. A Claude account, signed in, in a browser.
2. A scratch file for prompt versions. You will save a template at the end and
   reuse it in Exercises 4, 5, 7 and 13.
3. Nothing beyond that. There is no starter code for this exercise. Every prompt
   here is one you write.

Use placeholder data only. No real credentials, no customer records, no real
email addresses, including your colleagues'.

## Steps

### Step 1: Send the weak prompt first

Start a new conversation and send exactly this, with no additions:

```
write a function to validate email
```

Read the output without editing it. Do not fix the prompt yet. The contrast with
the structured version later is the whole point of this exercise, and you cannot
see the contrast if you skip the weak version.

> **Pause the video here.** Send it and read the output before you resume.

### Step 2: List what Claude had to guess

Write down every decision the model made for you because you did not state it. A
typical list:

1. Language and version.
2. Whether third-party libraries are allowed.
3. What counts as a valid address.
4. The return type, and what happens on invalid input.
5. Where the function will be called from.

Keep this list visible. It is the specification you failed to give.

> **Pause the video here.** Write your list before you resume.

### Step 3: Write the instruction and the context

**Instruction** is one task and one deliverable, stated with an action verb.

| Weak | Strong |
|---|---|
| "help me with email validation" | "Write one function that returns True for a valid address and False otherwise" |

One task per prompt. Bundling three requests into one message degrades all three
answers.

**Context** is the surrounding fact the model cannot infer:

1. Language and version, for example Python 3.11.
2. Where the code runs, for example a signup endpoint in a small web service.
3. Who calls it, and what they pass in.

Instruction and context are commonly merged into one blurred paragraph. Keep them
as separate labelled sections and the prompt stays diagnosable when the output is
wrong.

> **Pause the video here.** Draft both parts before you resume.

### Step 4: Add one example and the constraints

**Example** pins down the boundary you actually care about. One well-chosen pair
is usually enough:

```
user@example.com  -> True
user@@example     -> False
```

**Constraints** state what the model must not do:

1. Standard library only, no third-party packages.
2. No full RFC-compliant regular expression.
3. Return a boolean. Do not raise on invalid input.
4. No logging or print statements.

Constraints are the part developers leave out most often, and usually the part
that changes the output most. Step 6 will test whether that holds in your run.

> **Pause the video here.** Draft both parts before you resume.

### Step 5: Assemble and send the structured prompt

Combine the four parts into one message, in this order, with the headings kept:

```
Instruction:
Write one Python function that returns True for a valid email address and False
otherwise.

Context:
Python 3.11. It is called from a signup endpoint in a small web service. The
input is whatever a user typed into a form field, so it may be empty or not a
string at all.

Example:
user@example.com  -> True
user@@example     -> False

Constraints:
Standard library only, no third-party packages.
Do not use a full RFC-compliant regular expression.
Return a boolean. Do not raise on invalid input.
No logging or print statements.
```

Send it and read the result.

> **Pause the video here.** Send your version and read the output before you
> resume.

### Step 6: Compare the two outputs and name the winner

Put the Step 1 output next to the Step 5 output and answer three questions:

1. Which one could be pasted into a project with fewer edits?
2. Which of the guesses on your Step 2 list disappeared?
3. Which single addition changed the output most?

In most runs the answer to the third question is the constraints or the example,
not the added context. That is worth noticing, because context is the part people
spend the most words on.

> **Pause the video here.** Answer all three in writing before you resume.

### Step 7: Remove one part and observe

Send the structured prompt twice more, in new conversations:

1. Once with the constraints section deleted.
2. Once with the constraints restored and the example deleted.

Note what degrades each time and by how much. This turns the four-part structure
from a rule you were told into a result you measured. Your own measurement is the
version you will actually remember.

> **Pause the video here.** Run both variations before you resume.

### Step 8: Scrub it, then save the template

Check your prompt for anything that should not leave your machine: keys, tokens,
internal hostnames, customer data, real names or addresses. Replace anything you
find with a placeholder.

Then save this, with your own wording, as a file you keep:

```
Instruction: <one task, one deliverable, action verb>
Context:     <language and version, where it runs, who calls it, what they pass>
Example:     <one valid input and result, one invalid input and result>
Constraints: <libraries allowed, return type, error behaviour, what not to touch>
```

## What good looks like

1. You have both outputs saved, the weak one and the structured one.
2. Your Step 2 list of guesses exists, and you can point at which ones the
   structured prompt eliminated.
3. You can name the single addition that changed your output most, from what you
   observed rather than from what this document predicted.
4. You ran two ablations and wrote down what degraded.
5. You have a saved four-part template with placeholders and no sensitive data.

## Common problems

| Problem | Cause | Fix |
|---|---|---|
| Instruction and context read as the same paragraph | The two were merged | Keep the labelled headings. Instruction is the task, context is the surroundings |
| The output still uses the wrong language | The version was implied, not stated | Put language and version in the context line, explicitly |
| A constraint is ignored | It was buried in prose | One constraint per line, phrased as what not to do |
| The structured prompt is now a page long | Background was added that does not change the answer | Cut any sentence that would not change the output if deleted |
| The answer covers three topics shallowly | Several requests in one message | Split into sequential prompts, one task each |

## Going further

1. Apply the template to the task from Exercise 1: instruct an explanation, give
   the code as context, give an example of the level of detail you want, and
   constrain it to explanation with no rewrite. Compare against the plain
   "explain this function" you sent in Exercise 1.
2. Add a fifth heading, `Output format`, and specify a structure such as a table
   or a fenced code block only. Note how much post-editing that one heading saves.

Copyright © 2026, ZaranTech LLC. All rights reserved.
