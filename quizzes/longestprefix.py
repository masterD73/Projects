# -------------------------
# title: String Prefix exam
# -------------------------
# -------------------
# Description:
# Checks for longest
# common prefix.
# -------------------
# -----------------------
# Author: Daniel Merchav.
# Reviewer: None.
# AI2 InfinityLabs.
# -----------------------

def longest_equal_prefix(ls):
    """
    Check the longest streak of equal prefix between all elements.
    Inspired by Braunstain and Volkovich.
    :param ls: list of strings.
    :return: the longest slice that is equal in of the elements.
    """
    prefix = ""
    if len(ls) == 0:
        return prefix

    ls.sort()
    for i in range(len(ls[0])):
        if ls[0][i] != ls[-1][i]:
            return ls[0][:i]
    return ls[0]


def main():
    ls = []
    ls1 = [""]
    ls2 = ["hello", "porcupine", "banana", "xylophone"]
    ls3 = ["Eureka"]
    ls4 = ["pokemon", "poker", "poke", "pokeball"]
    ls5 = ["pokemon", "pokemon", "pokemon"]

    assert longest_equal_prefix(ls) == ""
    assert longest_equal_prefix(ls1) == ""
    assert longest_equal_prefix(ls2) == ""
    assert longest_equal_prefix(ls3) == "Eureka"
    assert longest_equal_prefix(ls4) == "poke"
    assert longest_equal_prefix(ls5) == "pokemon"
    print("Tests Done.")


if __name__ == "__main__":
    main()
