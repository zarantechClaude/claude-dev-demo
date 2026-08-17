# TEACHING ARTEFACT - DO NOT FIX
# This file contains deliberate problems. They are the exercise.
# Do not correct them and do not add comments explaining them.
# Trainer reference, not for learners: docs/lab-defect-register.md
#
# Exercise 3, Module 1. Intended duration: 15 minutes.
# Treat this as code a colleague generated from a vague prompt and sent you
# to review.

import sqlite3
import logging
import requests

API_KEY = "sk-live-4f9d2a7b1c8e6543"
DB_PATH = "app.db"


def sync_user_orders(user_emails):
    conn = sqlite3.connect(DB_PATH)
    results = []
    for email in user_emails:
        cur = conn.cursor()
        cur.execute(f"SELECT id, name, address FROM users WHERE email = '{email}'")
        row = cur.fetchone()
        logging.info("Fetched user %s at %s", email, row[2])
        r = requests.get(
            "https://api.orders.internal/v1/orders",
            params={"user_id": row[0]},
            headers={"Authorization": "Bearer " + API_KEY},
        )
        orders = r.json()
        for o in orders["items"]:
            cur.execute(
                f"INSERT INTO order_cache VALUES ({o['id']}, {row[0]}, '{o['status']}')"
            )
            conn.commit()
        results.append({"email": email, "count": len(orders["items"])})
    return results
