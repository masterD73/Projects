# -------------------------
# title: Sort Balls Quiz
# -------------------------
# -------------------------
# Description:
# Time complexity: O(n)
# Space complexity: O(n)
# -------------------------
# ----------------------------
# Author: Daniel Merchav.
# Reviewer: No reviewer.
# AI2 InfinityLabs.
# ----------------------------
def sort_balls(arr: list) -> None:
    gs = arr.count("G")
    ys = arr.count("Y")
    rs = arr.count("R")
    arr[:] = ["G"] * gs + ["Y"] * ys + ["R"] * rs
