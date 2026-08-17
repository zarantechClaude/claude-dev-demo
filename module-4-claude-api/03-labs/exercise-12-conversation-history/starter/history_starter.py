# Module 4, Exercise 12 fallback.
# The vendor exercise requires "a working Claude API project from the previous
# module". Learners who did not finish Exercise 11 are blocked. This file gives
# them the message array and the topic shift already built, so they can practise
# the actual skill: selecting which messages to send.
#
# TASK for the learner:
#   1. Keep the last 3 messages always.
#   2. Include older messages only if relevant to the current request.
#   3. Fall back gracefully when the filter returns nothing.
#   4. Test with a topic shift and confirm stale context is dropped.

HISTORY = [
    {"role": "user", "content": "We are building a notes API. Use PostgreSQL, not MongoDB."},
    {"role": "assistant", "content": "Understood. PostgreSQL it is."},
    {"role": "user", "content": "Tags should be a controlled list, not free text."},
    {"role": "assistant", "content": "Noted. Tags come from a fixed vocabulary."},
    {"role": "user", "content": "By the way, what is a good name for the repo?"},
    {"role": "assistant", "content": "Something like notes-service works well."},
    {"role": "user", "content": "Back to the schema. How should I model the tag relationship?"},
]

CURRENT_REQUEST = "Write the migration for the tag relationship."


def select_messages(history, current_request, keep_recent=3):
    """TODO (learner): return the message list to send to the API.

    Rules:
      - always include the last `keep_recent` messages
      - include older messages only when relevant to `current_request`
      - a message carrying a constraint or a decision is usually relevant
      - drop finished subtasks and unrelated topics
      - if nothing older qualifies, return only the recent window
    """
    raise NotImplementedError("Implement the relevance filter.")


if __name__ == "__main__":
    # decisions are the signal, and they sit OUTSIDE the last 3 messages.
    print(select_messages(HISTORY, CURRENT_REQUEST))
