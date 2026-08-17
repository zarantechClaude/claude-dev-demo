# Module 4 deck changelog

Original: `original/Module 4 - Building with the Claude API (Backend & Integration).pptx`  
Revised: `revised/Module 4 - Building with the Claude API (Backend & Integration) - REVISED.pptx`

Slide count: 25 before, 28 after.

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

> Requests require specific endpoints depending on the chosen model and task.

**Now:** the bullet block was rewritten to:

> - The Claude API enables developers to integrate advanced language capabilities natively.
> - It operates using a standardized RESTful interface for straightforward backend communication.
> - There is a single messages endpoint. The model is a parameter in the request body.
> - Responses are delivered in JSON format for easy parsing and manipulation.
> - The API supports streaming responses for real-time application user experiences.

**Why:** Factually wrong as written. There is one messages endpoint and the model is a parameter in the request body. A learner following this slide would go looking for per-model endpoints that do not exist. Verified against the official API documentation.

### Slide 5

**Was:**

> Pass your API key securely through the standard HTTP authorization header.

**Now:**

> Send the key in the x-api-key header, alongside a required anthropic-version header.

**Why:** Misleading as a teaching default. The documented primary key header is x-api-key. An Authorization header is also accepted, but a learner told to use 'the standard authorization header' and nothing else will struggle to debug a 401. Raw HTTP calls also require an anthropic-version header, which the slide never mentioned. Verified against the official API documentation.

### Slide 6

**Was:**

> Select your model based on specific application budget and latency constraints.

**Now:**

> Select by tier, then read the current version identifier from configuration.

**Why:** Anchors tier selection to something durable. Tier names persist across releases; version identifiers do not, so they belong in configuration rather than on a slide or in code.

### Slide 22

**Was:**

> Review three different proposed architectures for integrating the Claude API securely.

**Now:** the bullet block was rewritten to:

> - Compare your Exercise 11 CLI against the supplied reference implementation.
> - Analyze the provided code snippets for potential prompt injection vulnerability risks.
> - Examine the context management strategy you chose in Exercise 12, and its cost.
> - Identify flaws in how your own design handles session state persistence.
> - Prepare notes on efficiency, security, and scalability for your capstone design.

**Why:** The activity asked learners to review three sample architectures that were never supplied with the deck. Rewritten to use artefacts that exist: the Exercise 11 reference implementation and the learner's own capstone design.

### Slide 23

**Was:**

> Trainees must now evaluate the previously generated AI architecture integration suggestions.

**Now:** the bullet block was rewritten to:

> - Decide which of the suggestions you received you will accept, and say why.
> - Compare your chosen approach against latency, cost and complexity.
> - Explain how your design handles context persistence and untrusted input.
> - Write the decision down. It becomes the design note in your capstone README.

**Why:** Rewritten for recorded delivery. There is no group to present to, and the third-person 'trainees must' voice does not work on camera.

## Added

### New slide at position 4: Exercises in This Module

- Exercise 10: Configure a key in .env and make a first call. 12 minutes.
- Exercise 11: Build a CLI with a structured prompt template. 22 minutes.
- Exercise 12: Manage conversation history by relevance. 18 minutes.
- This module needs an API key with credit. Set it up before you start.

**Why:** Section map for recorded navigation, and the place to warn about the API key requirement.

### New slide at position 13: Shaping the Response

- Messages must alternate between the user role and the assistant role.
- Two user messages in a row is a common cause of a confusing API error.
- You can start the assistant's reply for it, which constrains the format tightly.
- Prefilling an opening brace is a reliable way to get JSON and nothing else.
- A system prompt is a top-level parameter, not the first message in the list.

**Why:** The assessment tests assistant prefill and the alternating-roles requirement, neither of which appeared in the deck. Both are practical and cheap to teach.

### New slide at position 22: Reusing a Stable Prefix: Prompt Caching

- Long prompts often repeat a large, unchanging prefix on every request.
- Caching that prefix means you are not billed to reprocess it each time.
- Order matters: put the stable material first and the variable material last.
- It is a cost and latency optimisation, not a way to raise a context limit.
- Check the current caching mechanics in the API documentation before you rely on them.

**Why:** The Module 4 assessment tests prompt caching and the deck never introduced it. It is also the highest-value cost optimisation available to anyone sending a large fixed context repeatedly, so it belongs in the deck regardless of the assessment.

## Not changed, but flagged

Nothing else in this deck was edited. Anything you disagree with above can be
reverted from `original/` without affecting the labs, which do not depend on
slide wording.
