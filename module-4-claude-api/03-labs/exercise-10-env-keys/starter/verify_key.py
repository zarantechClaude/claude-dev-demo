# Module 4, Block 1: run this BEFORE any teaching.
# Confirms the key loads and one call succeeds. Prints a specific diagnosis.
#   pip install anthropic python-dotenv
#   python verify_key.py

import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    print("FAIL: python-dotenv not installed. Run: pip install python-dotenv")
    sys.exit(1)

try:
    from anthropic import Anthropic
except ImportError:
    print("FAIL: anthropic SDK not installed. Run: pip install anthropic")
    sys.exit(1)

load_dotenv()
key = os.getenv("ANTHROPIC_API_KEY")

if not key:
    print("FAIL: ANTHROPIC_API_KEY not found.")
    print("  1. Is there a .env file in THIS directory?")
    print("  2. Is the variable named exactly ANTHROPIC_API_KEY?")
    print("  3. Any spaces around the = sign? Remove them.")
    print("  4. Are you running from the folder that contains .env?")
    sys.exit(1)

print("Key loaded, length {}, starts with {}...".format(len(key), key[:7]))

# Model is configuration, never hardcoded in course material: identifiers change.
# Set MODEL in .env. Check the current model list in the Anthropic docs.
model = os.getenv("MODEL")
if not model:
    print("FAIL: set MODEL in your .env file.")
    print("  Look up a current model identifier in the Anthropic documentation.")
    sys.exit(1)

try:
    client = Anthropic(api_key=key)
    resp = client.messages.create(
        model=model,
        max_tokens=32,
        messages=[{"role": "user", "content": "Reply with exactly: OK"}],
    )
    print("CALL SUCCEEDED. Response:", resp.content[0].text.strip())
    print("You are ready for Module 4.")
except Exception as exc:
    print("FAIL: the call did not succeed.")
    print("  Error:", type(exc).__name__, str(exc)[:300])
    print("  Common causes: invalid or revoked key, no credit on the account,")
    print("  an unrecognised MODEL value, or a blocked network.")
    sys.exit(1)
