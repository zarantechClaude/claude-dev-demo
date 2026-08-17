# TEACHING ARTEFACT - DO NOT FIX
# Exercise 6, Module 2. Intended duration: 22 minutes.
# No planted bugs in this file. Three working functions with no documentation
# and no tests. Your job is to add both.
# Trainer reference, not for learners: docs/lab-defect-register.md

def parse_duration(text):
    units = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    total = 0
    number = ""
    for ch in text.strip().lower():
        if ch.isdigit():
            number += ch
        elif ch in units:
            if number == "":
                raise ValueError("unit without a number: " + ch)
            total += int(number) * units[ch]
            number = ""
        elif ch == " ":
            continue
        else:
            raise ValueError("unexpected character: " + ch)
    if number != "":
        raise ValueError("trailing number without a unit")
    return total


def merge_ranges(ranges):
    if not ranges:
        return []
    ordered = sorted(ranges, key=lambda r: r[0])
    merged = [list(ordered[0])]
    for start, end in ordered[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return [tuple(r) for r in merged]


def summarise_scores(scores, passing=50):
    if not scores:
        return {"count": 0, "mean": None, "pass_rate": None}
    total = sum(scores)
    passed = sum(1 for s in scores if s >= passing)
    return {
        "count": len(scores),
        "mean": total / len(scores),
        "pass_rate": passed / len(scores),
    }
