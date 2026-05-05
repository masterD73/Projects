import math
import pandas as pd


def isprime(n):
    if n == 2:
        return True
    elif n <= 1 or n % 3 == 0 or n % 2 == 0:
        return False
    for i in range(5, round(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def find_primes(rng):
    primes = []
    for i in range(rng):
        if isprime(i):
            primes.append(i)
    return primes


def main():
    num_primes = 1000000
    primes = find_primes(num_primes)
    result_amount = len(primes)
    print(f"the primes in the first {num_primes}.\n {result_amount} primes found.\n The primes are:{primes}.")


if __name__ == '__main__':
    main()
    print("Done.")
