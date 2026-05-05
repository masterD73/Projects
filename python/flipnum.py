# Reviewer: Netta.
def even_pow_list(ls):
    """ Returns a list with squared even integers """
    return [a ** 2 for a in ls if a % 2 == 0]


# Test 1
ls1 = [15, 22, 11, 5, 9, 10, 2]
assert even_pow_list(ls1) == [484, 100, 4]
print(even_pow_list(ls1))

# Test 2
ls1 = [15, 11, 5, 9]
assert even_pow_list(ls1) == []
print(even_pow_list(ls1))

# Test 3
ls1 = []
assert even_pow_list(ls1) == []
print(even_pow_list(ls1))

print("Tests passed :P")
