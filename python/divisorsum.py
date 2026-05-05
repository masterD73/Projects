from functools import reduce


# Reviewer: Netta.
def positive_negative_lists(ls):
    """ Returns the sum of the positive and negative numbers
    of a given list """
    x = lambda num1, num2: num1 + num2
    positive = [n for n in ls if n > 0]
    negative = [n for n in ls if n < 0]
    return reduce(x, positive, 0), reduce(x, negative, 0)


# Test 1
nums = [1, 2, 3, 4, -2, -1]
positive_negative_lists(nums)
assert positive_negative_lists(nums) == (10, -3)

# Test 2
nums = [1, 2, 3, 4, 5, 6]
positive_negative_lists(nums)
assert positive_negative_lists(nums) == (21, 0)

# Test 2
nums = [-1, -2, -3, -4, -5, -6]
positive_negative_lists(nums)
assert positive_negative_lists(nums) == (0, -21)
