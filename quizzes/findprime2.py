# Python program to print all
# primes smaller than or equal to
# n using Sieve of Eratosthenes
import time


def sieve_of_eratosthenes(n):
    length = n + 1
    primes = [True] * length
    p = 2
    while p * p <= n:
        if primes[p] is True:
            for i in range(p * p, length, p):
                primes[i] = False
        p += 1

    for p in range(2, length):
        if primes[p]:
            primes[p] = p
    return [prime for prime in primes if prime is not False]


if __name__ == '__main__':
    start_time = time.time()
    n = 1000000
    primes = sieve_of_eratosthenes(n)
    end_time = time.time()
    print(f"The prime numbers smaller than or equal to {n}, are:{primes}")
    print(f"Time taken in seconds: {(end_time - start_time):.2f}")
