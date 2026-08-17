# TEACHING ARTEFACT - DO NOT FIX
# This file contains deliberate problems. They are the exercise.
# Do not correct them and do not add comments explaining them.
# Trainer reference, not for learners: docs/lab-defect-register.md
#
# Exercise 5, Module 2. Intended duration: 20 minutes.
# An existing registration endpoint, already in production, with 40,000 rows
# of real users behind it.

from flask import Flask, request, jsonify
import hashlib
import sqlite3

app = Flask(__name__)


@app.route("/api/register", methods=["POST"])
def r():
    d = request.get_json()
    if d == None:
        return jsonify({"err": "bad"}), 400
    n = d.get("name")
    e = d.get("email")
    p = d.get("password")
    if n == None or n == "":
        return jsonify({"err": "bad"}), 400
    if e == None or e == "":
        return jsonify({"err": "bad"}), 400
    if "@" not in e:
        return jsonify({"err": "bad"}), 400
    if p == None or p == "":
        return jsonify({"err": "bad"}), 400
    if len(p) < 4:
        return jsonify({"err": "bad"}), 400
    h = hashlib.md5(p.encode()).hexdigest()
    c = sqlite3.connect("users.db")
    cur = c.cursor()
    cur.execute("SELECT id FROM users WHERE email = '" + e + "'")
    if cur.fetchone() != None:
        return jsonify({"err": "bad"}), 400
    cur.execute(
        "INSERT INTO users (name, email, pwhash) VALUES ('"
        + n + "', '" + e + "', '" + h + "')"
    )
    c.commit()
    print("registered " + e + " with hash " + h)
    return jsonify({"ok": True, "email": e}), 200


if __name__ == "__main__":
    app.run(debug=True)
