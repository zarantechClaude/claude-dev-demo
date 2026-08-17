# Exercise 10, Module 4. Minimal Claude API call.
#
# Two conventions used across this whole programme:
#   1. The model id is read from configuration, never hardcoded. Model
#      identifiers change faster than course material does.
#   2. The key variable is ANTHROPIC_API_KEY. The official SDK reads it from
#      the environment automatically. Exercises 10, 11, 12 and 15 all depend
#      on that one name.
#
# Create .gitignore containing ".env" BEFORE you create .env.

import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

API_KEY = os.getenv("ANTHROPIC_API_KEY")
MODEL = os.getenv("MODEL")

if not API_KEY:
    raise SystemExit("ANTHROPIC_API_KEY is not set. Check your .env file.")
if not MODEL:
    raise SystemExit("MODEL is not set. Check the Anthropic docs for a current id.")

client = Anthropic(api_key=API_KEY)

response = client.messages.create(
    model=MODEL,
    max_tokens=300,          # caps the OUTPUT. Not the context window.
    system="You are a concise assistant for software developers.",
    messages=[
        {
            "role": "user",
            "content": "In three bullets, why do API keys belong in "
                       "environment variables rather than source code?",
        }
    ],
)

print(response.content[0].text)
