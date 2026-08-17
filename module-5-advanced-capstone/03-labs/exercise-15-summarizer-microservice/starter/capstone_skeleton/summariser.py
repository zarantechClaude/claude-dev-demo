"""Claude integration, isolated from the web layer so it can be tested.

Keeping the API call in its own module is what makes the tests in tests/ possible
without hitting the network. This separation is part of the clarity mark.
"""

import os
from anthropic import Anthropic


class SummariserError(Exception):
    """Raised when summarisation cannot be completed."""


# TODO (learner): this is where most of your marks are.
# A strong prompt has a role, a task, TAGGED input, and output constraints.
# The tags are not decoration: they are what stops code comments from being
# read as instructions to you.
SYSTEM_PROMPT = """TODO: define the role and the rules.

Requirements for a passing prompt:
  - state the role
  - state that content inside <code> tags is DATA, never instructions
  - ask for purpose, key functions, and any visible risks or assumptions
  - constrain the length and the format
"""

USER_TEMPLATE = """TODO: wrap the code in tags and state the task.

<code>
{code}
</code>
"""


def _client():
    key = os.getenv("ANTHROPIC_API_KEY")
    if not key:
        raise SummariserError("service is not configured")
    return Anthropic(api_key=key)


def summarise_code(code):
    """Return a dict describing the code. Raise SummariserError on failure."""
    model = os.getenv("MODEL")
    if not model:
        raise SummariserError("service is not configured")

    try:
        response = _client().messages.create(
            model=model,
            max_tokens=600,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": USER_TEMPLATE.format(code=code)}],
        )
    except Exception as exc:
        raise SummariserError("upstream summarisation failed") from exc

    text = response.content[0].text

    # TODO (learner): decide your response shape and document it in the README.
    return {"summary": text}
