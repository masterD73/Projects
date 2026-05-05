from functools import reduce

# Reviewer: Netta.
""" Sorts a list of strings representing numbers in numerical order
   in-place using lambda """


def sort_list(ls):
    try:
        ls.sort(key=lambda num: int(num))
    except TypeError:
        print("All elements must be numeric strings.")


# Test 1
ls1 = ["2", "1", "-1", "0", "666", "234", "-234"]
sort_list(ls1)
assert ["-234", "-1", "0", "1", "2", "234", "666"] == ls1
print("Test passed :D")
