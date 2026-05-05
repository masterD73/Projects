# -------------------------
# title: Reverse Sentence
# -------------------------
# -------------------------
# Description:
# Reverse order of words.
# -------------------------
# ----------------------------
# Author: Daniel Merchav.
# Reviewer: None.
# AI2 InfinityLabs.
# ----------------------------
def yoda(sentence: str) -> str:
    # new_sentence = ""
    # words = sentence.split()[::-1]
    #
    # for word in words:
    #     new_sentence += word + " "
    # return new_sentence.rstrip()
    sentence = " ".join(sentence.split()[::-1])
    return sentence


test = "i am student"

print(yoda(test))
