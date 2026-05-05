# reviewer: anan.
def divisor_sum(number):
    div_sum = 0
    half = number // 2 + 1

    for n in range(1, half):
        if number % n == 0:
            div_sum += n

    return div_sum + number


assert divisor_sum(10) == 18
for num in range(32):
    print(f'The sum of the divisors of {num} is {divisor_sum(num)}')
