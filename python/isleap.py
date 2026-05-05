# Reviewer: Netta.
def discount_10(d):
    """ Give 10% discount for prices in dictionary """
    for key, value in d.items():
        assert value >= 0, "Negative price not allowed."
        d[key] = value * 0.9
    return d


# Test 1
price_dict = {"Lemonade": 2, "Gum": 0.5, "chocolate": 10, "honey": 20}
assert {"Lemonade": 1.8, "Gum": 0.45, "chocolate": 9, "honey": 18} == discount_10(price_dict)

# Test 2
# price_dict = {"Lemonade" : 2, "Gum" : -4, "chocolate" : 10, "honey" : 20}

print("Tests passed >:)")
