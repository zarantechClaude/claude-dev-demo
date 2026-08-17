# Exercise 1: Explore Claude's Interface and Explain Sample Code

**Module 1** | **12 minutes** | **You need:** Browser

## What you will do

You will get a fluent, confident explanation of a function you have not seen
before, and then produce written evidence of where that explanation matches the
code and where it does not.

## Before you start

1. A Claude account, signed in, in a browser. Nothing is installed in this
   module.
2. The starter file open in a second tab or in a text editor:
   `module-1-fundamentals/03-labs/exercise-01-explore-interface/starter/running_average.py`
3. A scratch note file. You will reuse two of the notes in Exercise 2 and one of
   them in Module 5.

The comment block at the top of the starter file is course metadata. The exercise
is the function below it, from `def` to the end of the file.

## Steps

### Step 1: Get oriented in the workspace

Sign in and let the workspace finish loading. Find four things:

1. The prompt box, where you type.
2. The response area, where replies appear.
3. The sidebar, with your conversation history and any projects.
4. Settings.

You are not prompting yet. This step exists so that you are not hunting for the
history panel later while you are trying to think about code.

> **Pause the video here.** Locate all four areas before you resume.

### Step 2: Ask one open-ended question

Send this:

```
What can you help me with as a developer? Answer in five bullets, no code.
```

Read the reply and notice its shape. It answers as a conversational assistant,
not as a code generator, because you asked a question rather than requesting
code. Most real developer work starts here.

Everything in Module 1 happens in this browser tab. Claude Code, the terminal
tool, arrives in Module 2.

> **Pause the video here.** Send the prompt and read the reply before you resume.

### Step 3: Read the function before you ask about it

Open `starter/running_average.py` and read it without prompting Claude. Write
four things in your notes:

1. The function name.
2. What it takes as input.
3. What it returns.
4. How many values you expect back for the sample input at the bottom of the
   file.

Trace the loop by hand. Do not run the file. Module 1 needs no terminal, and
tracing by hand is the skill this exercise is really about.

This order matters. If you read Claude's explanation first, you can only judge
whether it sounds right, not whether it is right.

> **Pause the video here.** Read and trace the function, and write your four
> answers, before you resume.

### Step 4: Ask Claude to explain it

Start a new conversation. Paste the function, from `def` to the end, and add one
instruction:

```
Explain this function in simple terms.
```

Read the response once. Look for four things: the stated purpose, the described
inputs, the described return value, and the step by step logic.

Then note whether the explanation agrees with the four answers you wrote in
Step 3.

> **Pause the video here.** Send the prompt and compare it against your notes
> before you resume.

### Step 5: Count the values

Stay in the same conversation and send this follow-up:

```
For the input [10, 20, 30, 40], list every value this function returns, in
order. For each value, state which readings it averages. Then state how many
values the function returns for a list of n readings.
```

Now do the arithmetic yourself:

1. Count the values in the list Claude just produced.
2. Count the readings that went in.
3. Compare both counts against the trace you did by hand in Step 3.
4. Re-read the Step 4 explanation with those counts in front of you.

Write one sentence in your notes: does the Step 4 explanation describe what this
code does, or what this code was meant to do? If your counts do not match, state
the two counts in that sentence. The numbers are the evidence, and evidence is
what makes a review comment stick.

> **Pause the video here.** Do the counting yourself and write the sentence
> before you resume.

### Step 6: Change the prompt and watch the answer change

Run the same function again with each of these, starting a new conversation each
time so earlier context does not carry over:

```
Explain this function line by line.
```

```
Summarize this function in two sentences.
```

```
Explain this function as if I have just joined this codebase.
```

Same code, same model tier, three noticeably different answers. Note which of
the three would have helped you reach the Step 5 finding fastest. The prompt is
doing the work here, which is the idea Exercise 2 builds on.

> **Pause the video here.** Run all three variations before you resume.

### Step 7: Write down one use case of your own

Write one task from your current work where a code explanation on demand would
save you time. Keep it. Module 5's capstone starts from a use case of your own,
and this is the easiest moment to capture one.

## What good looks like

You can point at all of the following in your notes:

1. The function's input and output described in your own words, written before
   you prompted.
2. Two counts: values returned for a four-reading input, and readings supplied.
3. One sentence stating whether the explanation matched the code, supported by
   those counts rather than by impression.
4. Three prompt variations compared, with one named as the most useful for
   verification.
5. One use case from your own work.

## Common problems

| Problem | Cause | Fix |
|---|---|---|
| The explanation sounds right, so you accept it | Fluent prose reads as authoritative. It is not evidence | Do Step 5. Counts settle it, wording does not |
| Pasted code loses its indentation | Copied from a rendered file view | Paste into a plain text editor first, or copy from the raw file view |
| Claude returns a corrected version of the function | An open request invites improvement | Add "Explain only. Do not rewrite the code." |
| The follow-up answer contradicts the first answer | The first described intent, the second traced execution | Keep both. That contrast is the lesson of this exercise |
| Your answer differs from a colleague's | Responses vary between runs, and small wording changes matter | Expected. Compare findings and evidence, not phrasing |

## Going further

1. Ask for a step by step trace table for the input `[5]` and then for `[]`, and
   check both by hand. Edge cases are where explanations drift first.
2. Rewrite your Step 4 prompt so that a single prompt produces the explanation
   and the verification evidence together. Save it. Exercise 2 turns that instinct
   into a repeatable structure.

Copyright © 2026, ZaranTech LLC. All rights reserved.
