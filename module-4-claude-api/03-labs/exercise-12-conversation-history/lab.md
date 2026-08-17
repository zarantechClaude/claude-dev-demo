# Exercise 12: Manage Minimal Conversation History

**Module 4** | **18 minutes** | **You need:** Terminal, API key

## What you will do

You will build multi-turn conversation from nothing, then take control of what actually
gets sent on each turn. You will implement the obvious strategy first, watch what it
costs you, and only then implement the one that works.

## Before you start

1. Open `module-4-claude-api/03-labs/exercise-12-conversation-history/starter/history_starter.py`.
2. Your `.env` from Exercise 10, with `ANTHROPIC_API_KEY` and `MODEL`.
3. Exercise 11's CLI is useful here if you have it, and it is not required. The starter
   file carries the conversation you need, so this exercise stands on its own.

## Steps

### Step 1: Prove to yourself that the API has no memory

Two calls, no history between them:

```python
ask("My favourite language is Python.")
ask("What did I just tell you?")
```

Run it. The second call cannot answer, and watching that happen once is worth more than
being told.

Name what you just saw. The API is stateless. It has no record of your previous call.
Multi-turn conversation is not a feature you switch on, it is a thing you build, and
everything else in this exercise follows from that.

### Step 2: Make it multi-turn the crude way

Keep a list, append both sides of every exchange, resend the whole thing:

```python
history = []

def ask(user_input):
    history.append({"role": "user", "content": user_input})
    response = client.messages.create(
        model=MODEL, max_tokens=500, messages=history
    )
    reply = response.content[0].text
    history.append({"role": "assistant", "content": reply})
    return reply
```

Run Step 1 again. It works now, and it works for exactly one reason: you resent
everything. That is the whole mechanism.

It is also not viable past a few dozen turns. What you send grows every turn, and so does
what it costs you and how long it takes.

> **Pause the video here.** Get both calls working before you continue.

### Step 3: Read the conversation in the starter file, and take notes

Open `starter/history_starter.py`. It holds a seven message conversation in `HISTORY` and
one new request in `CURRENT_REQUEST`. Someone is building a notes API and has been talking
to an assistant about it for a while.

Read the whole conversation, top to bottom, and write down every decision this
conversation has committed to. Not a summary. A list. If a line settles a question about
how this system is going to work, it goes on your list.

You will need this list twice, so write it somewhere you can come back to.

> **Pause the video here.** Read all seven messages and write your list. Do not write any
> code yet.

### Step 4: Implement the obvious strategy

The standard answer to a history that grows without limit is a sliding window: keep the
last few messages, drop the rest. Implement exactly that in `select_messages`, and nothing
more:

```python
def select_messages(history, current_request, keep_recent=3):
    return history[-keep_recent:]
```

```bash
python history_starter.py
```

Look at the list it printed. Then go back to the list you wrote in Step 3 and mark which
of your decisions are still present in the messages you are about to send.

### Step 5: Send it and read the answer against your list

Send the window plus the current request to the API and get a real answer back:

```
[the messages your window selected, as conversation turns]

Write the migration for the tag relationship.
```

Read what comes back carefully. Do not skim it. Then answer one question in writing:

**Does the answer honour every decision on your Step 3 list, and if not, which ones did it
miss?**

Be specific. Name the decision, and name the line in the response that contradicts it or
silently assumes something else.

> **Pause the video here.** Take the full two minutes on this. The rest of the exercise
> only makes sense once you have found the answer yourself.

### Step 6: Name what went wrong, precisely

What you have just seen is not a model failure. The model answered the question it was
given, using the context it was given. The context was wrong, and you chose it.

The mistake has a shape worth remembering: **a sliding window uses recency as a proxy for
importance, and recency is a poor proxy.** Constraints behave in a particular way in real
conversations. They get stated once, early, in one sentence, and then everybody involved
carries them silently for the rest of the project. Small talk, by contrast, happens
constantly, and much of it is recent.

So a window sized to "the last few messages" systematically keeps the cheap content and
drops the expensive content. It is not slightly wrong. It is wrong in a direction.

### Step 7: Write the relevance rules before you write the filter

Decide on paper what qualifies. Include an older message when it:

- carries a constraint, a requirement or a prohibition
- records a decision that has not been revisited
- holds a value, name or identifier still in use
- clarifies something the current request depends on

Exclude an older message when it:

- belongs to a finished subtask
- is about a different topic entirely
- repeats something already present in the recent window

Notice what is not on either list: how recently it was said.

### Step 8: Implement the filter, then test the filter itself

Here is a starting point. Keyword overlap between the older message and the current
request:

```python
def _words(text):
    return {w.lower().strip(".,?!") for w in text.split() if len(w) > 4}


def relevant(older, current_request, min_overlap=1):
    target = _words(current_request)
    return [m for m in older if len(_words(m["content"]) & target) >= min_overlap]
```

Wire it up:

```python
def select_messages(history, current_request, keep_recent=3):
    recent = history[-keep_recent:]
    older = history[:-keep_recent]
    return relevant(older, current_request) + recent
```

Now test the filter rather than trusting it. Print what it selected, and check it against
your Step 3 list. Both outcomes below are real results, and neither is a mistake on your
part.

**If it selected the messages carrying your decisions**, re-run Step 5 with the new
selection and compare the two answers directly.

**If it selected nothing older at all**, or selected the wrong things, that is a finding
worth more than a working filter. Look at why: compare the vocabulary of the current
request against the vocabulary of the messages you know matter. A constraint stated early
often shares no words at all with the request that depends on it, because by the time you
ask the question, the constraint has become an assumption nobody restates.

So lexical overlap is a second proxy, and it fails for the same reason the first one did.
Fix it with a rule that does not depend on the topic matching:

```
Here is a conversation history and a new request.

[paste HISTORY and CURRENT_REQUEST]

Classify each message as CONSTRAINT, DECISION, or CHATTER. A message is a CONSTRAINT or
a DECISION if a developer implementing this system later would be wrong to ignore it.
Return only the classification, one line per message, with no explanation.
```

Then keep every CONSTRAINT and DECISION regardless of how old it is, keep the recent
window, and drop the rest. That is the real pattern: important context gets pinned, not
aged out.

> **Pause the video here.** Get a selection that carries your Step 3 list, then re-run
> Step 5 and compare the two answers.

### Step 9: Assemble the bundle in order, and add a fallback

Order the final request like this:

1. The system instruction, as the `system` parameter of the request.
2. Relevant older messages.
3. The recent window.
4. The current request.

Two things to get right in the assembly.

The system instruction is a top level parameter, not an entry in `messages`. You met that
in Exercise 11 and it fails the same way here.

Your bundle should end with exactly one user turn, the current request. `HISTORY` already
ends with a user message, so decide whether that message is the current request or a turn
that still needs its reply, and write a one line comment saying which you chose. Deciding
this deliberately is cheaper than discovering it from an error.

Then the fallback. If the filter returns nothing, send the recent window plus the current
request and carry on. An empty filter result is a normal outcome, not an error, and it
must never break the call.

### Step 10: Test a topic shift, then separate the two jobs

Add a genuinely unrelated request to the end of the conversation, something about
deployment or logging, and confirm the schema discussion drops out while your pinned
constraints behave the way you decided they should. If a constraint about storage is still
relevant to a question about logging, say why. If it is not, it should go.

Then check the shape of your code. Selection logic in one function, the API call in
another, no overlap. Storing conversation data and choosing which subset to send are two
different jobs with two different reasons to change, and code that mixes them is code you
cannot tune without risking the transport.

## What good looks like

- You can state in one sentence why multi-turn conversation works at all.
- You have a written list of the decisions in the conversation, made before you saw any
  output.
- You can name the decision the sliding window dropped, and show the line in the response
  that proves it was dropped.
- Your selection carries every item on that list, and you can explain why your filter
  catches them.
- The filter returning nothing produces a working call, not an exception.
- Selection and transport live in separate functions.

## Common problems

| Problem | Cause | Fix |
|---|---|---|
| `NotImplementedError` | `select_messages` is still the starter stub | Implement Step 4 first. The naive version is part of the exercise, not a shortcut past it |
| The API rejects the request and mentions the system role | System instruction placed inside `messages` | Pass it as the `system` parameter |
| The API rejects your assembled array | Your selection starts with an assistant turn, or the turn order is not what you intended | Print the roles in order before sending. Fix the window boundary rather than the message content |
| The filter returns nothing and the call crashes | No fallback | Step 9. An empty result is normal |
| The filter returns everything | `min_overlap` too low, or the word length threshold is letting common words through | Raise the threshold, or move to the classification approach in Step 8 |
| The answer improves but you cannot say why | You changed the filter and the prompt at the same time | Change one thing, re-run, compare. Two changes give you no information |
| Everything works and you sent 40 messages | You added a fallback that sends the whole history | The fallback is the recent window, not everything |
| You cannot tell whether the answer got better | No baseline | Keep the Step 5 answer. A comparison needs two responses side by side |

## Going further

1. Print the exact message array before every call, behind a `DEBUG` flag. Being able to
   see what you sent, rather than what you meant to send, is the single most useful
   debugging habit in this whole area, and it is four lines of code.
2. Replace the pinned constraint list with a running summary: after every few turns, ask
   for a short summary of the decisions so far and carry that instead of the original
   messages. Then measure what it costs you. Summarising is cheaper per turn and it loses
   detail, and knowing which of those two matters more for your application is the
   engineering judgement being taught.

Copyright © 2026, ZaranTech LLC. All rights reserved.
