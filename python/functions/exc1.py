# Reviewer: Netta.
remove_words = lambda ls1, words: [ls1.remove(word) for word in words if word in ls1]
""" Removes specific words from a given list """

# Test 1
words = ["horse"]
ls = ["hi", "howdy", "hello", "hallo"]
remove_words(ls, words)
assert ["hi", "howdy", "hello", "hallo"] == ls

# Test 2
words = ["hi", "hello"]
ls = ["hi", "howdy", "hello", "hallo"]
remove_words(ls, words)
assert ["howdy", "hallo"] == ls

# Test 3
words = ["howdy", "hallo", "asd23"]
remove_words(ls, words)
assert [] == ls

print("test passed!")
