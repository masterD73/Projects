# reviewer: anan.
def is_prime(number):
    square = int(number ** 0.5)

    if number < 2:
        return False
    elif (number % 2 == 0 and number != 2) or (number % 3 == 0 and number != 3):
        return False

    for n in range(5, square + 1):
        if number % n == 0:
            return False
    return True


assert is_prime(25) == False
assert is_prime(23) == True
for i in range(33):
    print(f'is {i} prime? result: {is_prime(i)}')
