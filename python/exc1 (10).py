# reviewer: Ran.
def dict_to_tuple(d):
    return list(d.items())


dictionary = {"name": "Daniel", "age": 34, "sex": "Male"}
assert [('name', 'Daniel'),
        ('age', 34),
        ('sex', 'Male')] == dict_to_tuple(dictionary)
print(dict_to_tuple(dictionary))
