# -------------------------
# title: 
# -------------------------
# -------------------------
# Description: 
# -------------------------
# ----------------------------
# Author: Daniel Merchav.
# Reviewer:
# AI2 InfinityLabs.
# ----------------------------
import regex
brackets = "(())"
match = regex.match(r"\(([^()]*|(?R))*\)", brackets)
print(match.group())
