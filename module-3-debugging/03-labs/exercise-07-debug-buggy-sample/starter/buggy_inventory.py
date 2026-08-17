# TEACHING ARTEFACT - DO NOT FIX
# This file contains deliberate problems. They are the exercise.
# Do not correct them and do not add comments explaining them.
# Trainer reference, not for learners: docs/lab-defect-register.md
#
# Exercise 7, Module 3. Intended duration: 15 minutes.
# Run the test suite before you read the code.

def restock(inventory, deliveries):
    """Apply deliveries to inventory and return items still below threshold."""
    low = []
    for item in deliveries:
        inventory[item["sku"]] += item["qty"]
    for sku in inventory:
        if inventory[sku] < inventory["threshold"]:
            low.append(sku)
    return low


def reorder_quantity(current, threshold, pack_size):
    """How many packs to order to get back above threshold."""
    shortfall = threshold - current
    return shortfall // pack_size
