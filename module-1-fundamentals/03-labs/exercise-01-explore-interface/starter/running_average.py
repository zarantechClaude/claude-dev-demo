# TEACHING ARTEFACT - DO NOT FIX
# This file contains deliberate problems. They are the exercise.
# Do not correct them and do not add comments explaining them.
# Trainer reference, not for learners: docs/lab-defect-register.md
#
# Exercise 1, Module 1. Intended duration: 12 minutes.

def calculate_running_average(readings):
    """Return the running average of sensor readings."""
    totals = []
    running_sum = 0
    for i in range(len(readings) - 1):
        running_sum += readings[i]
        totals.append(running_sum / (i + 1))
    return totals


if __name__ == "__main__":
    print(calculate_running_average([10, 20, 30, 40]))
