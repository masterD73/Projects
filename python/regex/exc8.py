# -------------------------
# title: 
# -------------------------
# -------------------------
# Description: 
# -------------------------
# ------------------------
# Author: Daniel Merchav.
# Reviewer: Anan Yablonko.
# AI2 InfinityLabs.
# ------------------------
import re

with open("text.txt", "r") as file:
    story = file.read()
    story = re.sub(r"\bComputer Sciences\b", "CS", story)
    story = re.sub(r"\bArtificial Intelligence\b", "AI", story)
    story = re.sub(r"\bCS\b", "Computer Sciences (CS)", story, count=1)
    story = re.sub(r"\bAI\b", "Artificial Intelligence (AI)", story, count=1)

with open("new.text", "w") as new:
    new.write(story)
