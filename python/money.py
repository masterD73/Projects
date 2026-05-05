# Reviewer: Netta.
def luhn_algo(card):
    """ Validates a credit card number using the Luhn algorithm """
    ints = [int(n) for n in str(card)][::-1]

    for i in range(len(ints)):
        if i % 2 == 1:
            ints[i] *= 2
            if ints[i] > 9:
                ints[i] -= 9
    return sum(ints) % 10 == 0


card1 = 5512435
card2 = 79927398713

# Test 1
assert luhn_algo(card1) == False

# Test 2
assert luhn_algo(card2) == True

print("Tests passed :~)")
