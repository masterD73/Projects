# reviewer: Ran.
def remove_string(list1):
    return [elem for elem in list1 if type(elem) == str]


list_str = [1, 2, 3, "str", 3, "4", 54]
assert remove_string(list_str) == ["str", "4"]
print(remove_string(list_str))
