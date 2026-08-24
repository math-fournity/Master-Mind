#!/usr/bin/env python3
"""Verify all solutions used in the proof."""

solutions = [
    (1, 1, 2, 1, "2-reg: c(1)≠c(2)"),
    (3, 1, 3, 1, "2-reg: c(1)≠c(3)"),
    (3, 2, 3, 3, "2-reg: c(2)≠c(3)"),
    (2, 2, 4, 2, "3-reg: c(4)≠B"),
    (3, 3, 3, 5, "3-reg: c(5)≠C"),
    (3, 3, 6, 3, "3-reg: c(6)≠C"),
    (5, 1, 4, 1, "3-reg Case1: c(5)≠A when c(4)=A"),
    (6, 4, 6, 6, "3-reg Case1a: mono when c(4)=c(5)=A,c(6)=A"),
    (6, 2, 6, 2, "3-reg: mono when c(6)=B"),
    (3, 4, 3, 7, "3-reg Case2: c(7)≠C"),
    (7, 2, 2, 5, "3-reg Case2c: c(7)≠B when c(5)=B"),
    (7, 1, 5, 1, "3-reg Case2a: c(7)≠A when c(5)=c(6)=A"),
    (3, 4, 9, 3, "3-reg Case2: c(9)≠C"),
    (9, 1, 6, 1, "3-reg Case2: c(9)≠A"),
    (6, 5, 6, 8, "3-reg Case2a: c(8)≠A"),
    (4, 4, 8, 4, "3-reg Case2a: c(8)≠C"),
    (2, 7, 7, 10, "3-reg Case2a: c(10)≠B"),
    (6, 6, 6, 10, "3-reg Case2: c(10)≠A"),
    (8, 7, 7, 12, "3-reg Case2a: c(12)≠B"),
    (6, 6, 12, 6, "3-reg Case2a: c(12)≠A"),
    (7, 7, 8, 11, "3-reg Case2a: c(11)≠B"),
    (1, 6, 11, 5, "3-reg Case2a: c(11)≠A"),
    (8, 2, 7, 2, "3-reg Case2a: CONTRADICTION all B"),
    (5, 5, 10, 5, "3-reg Case2c: c(10)≠B"),
    (1, 6, 8, 7, "3-reg Case2c: c(8)≠A"),
    (10, 3, 8, 4, "3-reg Case2c: c(8)≠C"),
    (9, 5, 12, 5, "3-reg Case2c: c(12)≠B"),
    (11, 3, 10, 3, "3-reg Case2c: c(11)≠C"),
    (11, 1, 7, 1, "3-reg Case2c: c(11)≠A"),
    (12, 4, 3, 10, "3-reg Case2c: CONTRADICTION all C"),
]

print("Verifying all solutions:")
all_ok = True
for w, x, y, z, desc in solutions:
    lhs = w + 6*x
    rhs = 2*y + 3*z
    ok = lhs == rhs
    if not ok:
        print(f"  FAIL: ({w},{x},{y},{z}): {lhs} ≠ {rhs} -- {desc}")
        all_ok = False
    else:
        print(f"  OK: ({w},{x},{y},{z}): {lhs} = {rhs} -- {desc}")

print(f"\nAll solutions valid: {all_ok}")
