# Module 4 self-check: Building with the Claude API

**Ten questions. Self-check only.** This is not graded and it does not gate
completion. The capstone carries completion for this programme.

Each question is tagged:

- **Core** means the module taught it directly. If you miss a Core question, go back
  to the deck section or the lab step and watch it again.
- **Stretch** means the question extends the material to a situation you were not
  shown. It is meant to be harder. Missing one is information, not a verdict.

One option per question is correct. Answer all ten before you check the key, because
the value of a self-check comes from finding out where you were confident and wrong.

---

### 1. Core

You are porting a working integration from another provider. Your messages list
starts with `{"role": "system", "content": "..."}` and then the user message. The
request fails with a 400.

What is wrong?

a. The request needs at least three messages before the API will accept it.
b. `max_tokens` has to be set inside the system message object.
c. The system prompt is a top-level request parameter, not an entry in `messages`.
d. The configuration role has to be named `developer` rather than `system`.

---

### 2. Core

Your CLI wraps whatever the user typed into a prompt template. Someone submits text
that closes your tag and then issues its own instruction.

Which change gives you the most protection?

a. Tag the untrusted text, and state in the system prompt that tags hold data, not
   instructions.
b. Remove angle brackets and punctuation from the input before inserting it into the
   template.
c. Set temperature to zero, so the model cannot act on an instruction it finds inside
   the input.
d. Encode the user's text as Base64 and ask the model to decode it before answering.

---

### 3. Core

A user in your chat client presses Enter twice, so two user messages are stored
before any reply exists. Your service sends both of them, back to back, in the
messages list. The request is rejected.

Why?

a. Two requests from the same session inside one second are rate limited.
b. The messages list exceeded the number of entries allowed in a single request.
c. A system message is required to separate two consecutive user messages.
d. Messages must alternate between the user role and the assistant role.

---

### 4. Core

Your endpoint needs JSON and nothing else. Replies keep arriving with a sentence of
preamble in front of the JSON.

Which technique gives you the tightest control over how the reply opens?

a. Add a top-level `response_format` parameter asking for a JSON object.
b. Prefill the assistant turn with an opening brace, so the reply continues from it.
c. Set a stop sequence on the closing brace, so nothing after it is returned.
d. Repeat the instruction to return only JSON three times at the end of the prompt.

---

### 5. Core

You send one request telling the assistant your preferred language, then a second
request asking what you just told it. The second reply cannot answer. Nothing is
broken.

What does your code have to do?

a. Enable session persistence on the client, so the provider tracks the thread.
b. Reuse one client object across both calls, so the connection carries the state.
c. Send the earlier turns again, in the messages list, on every request.
d. Pass a session identifier, so the provider can look the earlier turn up for you.

---

### 6. Core

A reply stops mid-sentence. Your prompt is short and the conversation is only a few
turns old.

Which limit did you hit, and what is the fix?

a. The cap on output length. Raise it, or ask for a shorter answer. Different fixes.
b. The context window. Drop the oldest messages until the whole request fits inside it.
c. Your terminal's output buffer. Read the response in chunks inside your HTTP client.
d. No limit was hit. Temperature was set high enough to produce a run-on answer.

---

### 7. Core

A teammate commits `.env`, containing a live key, to a private repository. They
notice and delete the file in the next commit.

What is the correct response?

a. Nothing further. The file is gone from the current tree, so the key is no longer
   exposed.
b. Add the file to `.gitignore`, which also removes it from the earlier commits.
c. Make sure the repository stays private and restrict who can read the default branch.
d. Rotate the key, then gitignore `.env` and commit a `.env.example` in its place.

---

### 8. Stretch

Your service sends a large fixed style guide with every request, followed by one
short file to review. Cost and latency are dominated by the fixed part.

What helps, and how do you order the prompt?

a. Compress the HTTP request body before sending, and keep the order you already have.
b. Cache the unchanging prefix, and keep stable material first, variable material last.
c. Cache the whole prompt, which also raises how much context one request can carry.
d. Drop the middle of the style guide and send only its first and last sections.

---

### 9. Stretch

A review assistant keeps only the last three messages of each conversation. Early on,
the user stated a hard requirement that nobody has mentioned since. The latest answer
quietly ignores it.

What is the flaw in the strategy?

a. Recency is standing in for importance, and a constraint stated once early is
   exactly what it drops.
b. Three messages is simply too few. Widening the window to twenty removes the problem.
c. The user should have restated the requirement in every message that depends on it.
d. Keeping only the older messages that share vocabulary with the current request
   would have caught it.

---

### 10. Stretch

Your team maintains three bespoke adapters so an assistant can read from a ticket
tracker, a wiki and a database. Each adapter is maintained separately.

What does adopting MCP change?

a. Your data moves into the provider's infrastructure, so no adapter is needed at all.
b. The model reaches your systems directly over the network, with no service in between.
c. You get one standard interface for exposing tools and data, not a bridge per system.
d. You no longer define what each tool accepts, because the model infers the parameters.

---

Copyright © 2026, ZaranTech LLC. All rights reserved.
