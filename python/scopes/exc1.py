# Reviewer: Anan
glob = 10


def foo():
    a = 10
    print(a)


def global_var_check(name):
    return name in globals()


# Test 1
assert global_var_check("__name__")
print(f"__name__ is a global variable")
# Test 2
assert global_var_check("glob")
print(f"glob is a global variable")
# Test 3
assert not global_var_check("a")
print(f"a is not a global variable")
print("Tests passed.")
