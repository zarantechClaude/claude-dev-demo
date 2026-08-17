# Capstone skeleton: code summariser service

Starting point for the Claude AI for Developers capstone. Scaffolding only, so
your time goes into prompt design and robustness rather than boilerplate.

## What you must build

`POST /summarize` accepts JSON with a `code` field, sends it to the Claude API
with a structured prompt, and returns a summary as JSON.

`GET /health` already works. Do not remove it.

## Setup

```
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env             # then fill in your values
```

Create `.gitignore` containing `.env` before you create `.env`.

## Run

```
python app.py
curl localhost:5000/health
```

## Test

```
pytest
```

Four test stubs are provided. Make them pass. Add more if you want the marks.

## What you are graded on

See `docs/capstone-brief.md`. Summary: it works, it fails cleanly, the prompt is
a real template with tagged input, it is readable, it is tested, and there are
no secrets in the repository.

## Two traps that catch people

1. **413 Payload Too Large.** A big upload is rejected by the framework or proxy
   before your code runs. That is a body-size default, not a rate limit and not a
   context-window problem. Handle it deliberately.
2. **Stale grounding.** If you change your design, update your notes and your
   `CLAUDE.md`. Otherwise the assistant keeps generating against the old shape.
