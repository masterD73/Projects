# reviewer: Ran.
def max_min_items(d):
    min_val = min(d.values())
    max_val = max(list(d.values()))
    min_index = list(d.values()).index(min_val)
    max_index = list(d.values()).index(max_val)

    print(f"The maximal value key is: "
          f"{list(d.keys())[min_index]}.")
    print(f"The minimal value key is: "
          f"{list(dictionary.keys())[max_index]}.")
    return list(d.keys())[min_index], list(dictionary.keys())[max_index]


dictionary = {"Daniel": 888, "Igor": 51, "Vlad": 22, "Clair": 3}

assert ('Clair', 'Daniel') == max_min_items(dictionary)
print(max_min_items(dictionary))
