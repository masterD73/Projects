# -----------------
# title: Is Pangram
# -----------------
# --------------------
# Description:
# Checks if a sentence
# is a pangram.
# --------------------
# -----------------------
# Author: Daniel Merchav.
# Reviewer: No One.
# AI2 InfinityLabs.
# -----------------------
def is_pangram(sentence: str) -> bool:
    first, last, lower = ord("a"), ord("z"), set(sentence.lower())
    for i in range(first, last + 1):
        if chr(i) not in lower:
            return False
    return True


def main():
    sentence = "The quick brown fox jumps over the lazy dog"
    wrong = "The very quick and non lazy brown fo jumps over the lazy dog"
    assert is_pangram(sentence) is True
    assert is_pangram(wrong) is False
    print("Tests passed successfully.")


if __name__ == "__main__":
    main()
