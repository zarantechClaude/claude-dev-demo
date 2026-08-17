# TEACHING ARTEFACT - DO NOT FIX
# This file contains deliberate problems. They are the exercise.
# Do not correct them and do not add comments explaining them.
# Trainer reference, not for learners: docs/lab-defect-register.md
#
# Exercise 8, Module 3. Intended duration: 15 minutes.
# Run it once and note the elapsed time before changing anything.

import random
import time


def build_data(n=12000):
    random.seed(42)
    catalogue = [random.randint(0, n // 2) for _ in range(n)]
    wanted = [random.randint(0, n // 2) for _ in range(n)]
    return catalogue, wanted


def count_matches(catalogue, wanted):
    """For each wanted id, count how many times it appears in the catalogue.

    Returns the total number of matches across all wanted ids.
    Duplicates in the catalogue count each time.
    """
    total = 0
    for target in wanted:
        for entry in catalogue:
            if entry == target:
                total += 1
    return total


if __name__ == "__main__":
    catalogue, wanted = build_data()
    start = time.perf_counter()
    result = count_matches(catalogue, wanted)
    elapsed = time.perf_counter() - start
    print("matches:", result)
    print("elapsed: {:.3f}s".format(elapsed))
