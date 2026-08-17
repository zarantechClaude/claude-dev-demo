"""Capstone skeleton: code summariser service.

TODO markers show what you must implement. The health endpoint and the error
scaffolding are done so you can focus on the prompt and the failure paths.
"""

import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

from summariser import summarise_code, SummariserError

load_dotenv()

app = Flask(__name__)

# Trap 1: set this deliberately. Without it you get an opaque 413 from the
# framework before your handler ever runs.
app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024  # 2 MB

MAX_CODE_CHARS = int(os.getenv("MAX_CODE_CHARS", "20000"))


@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.post("/summarize")
def summarize():
    payload = request.get_json(silent=True)
    if payload is None:
        return jsonify({"error": "request body must be JSON"}), 400

    code = payload.get("code")
    if not isinstance(code, str) or not code.strip():
        return jsonify({"error": "field 'code' is required and must be non-empty"}), 400

    if len(code) > MAX_CODE_CHARS:
        return jsonify({
            "error": "code too long",
            "max_chars": MAX_CODE_CHARS,
        }), 413

    try:
        result = summarise_code(code)
    except SummariserError as exc:
        # Never leak the raw provider error to the caller.
        return jsonify({"error": str(exc)}), 502

    return jsonify(result), 200


@app.errorhandler(413)
def too_large(_exc):
    return jsonify({"error": "payload too large"}), 413


if __name__ == "__main__":
    # Not for production. Use a WSGI server when you containerise this.
    app.run(port=5000, debug=True)
