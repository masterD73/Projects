# -------------------------
# title: Reverse Lines
# -------------------------
# -------------------------
# Description: None
# -------------------------
# -------------------------
# Author: Daniel Merchav.
# Reviewer: None
# AI2 InfinityLabs.
# -------------------------
def reverse_lines(file_name: str) -> None:
    with open(file_name, "r") as origin:
        text = origin.readlines()[::-1]
    with open(f"results_{file_name}", "w") as result:
        result.writelines(text)
