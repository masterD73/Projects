# reviewer: Ran.
def unique_dict(d):
    return list(set(d.values()))


dictionary = {"name": "Daniel", "birth year": 1989, "mane": "Daniel"}

assert list({"Daniel", 1989}) == unique_dict(dictionary)
print(unique_dict(dictionary))
