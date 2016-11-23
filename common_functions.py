from math import ceil, sqrt
from functools import reduce
from operator import mul


def fibonacci_val(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, b + a


def fibonacci_count(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, b + a


def get_unique_prime_factors(n):
    i = 2
    while n > 1:
        if n % i == 0:
            yield i
            while n % i == 0:
                n = n / i
        else:
            i += 1


def get_prime_factors(n):
    i = 2
    while n > 1:
        if n % i == 0:
            yield i
            n = n / i
        else:
            i += 1


def get_factors(n):
    factors = [1, n]
    for i in range(2, int(ceil(sqrt(n)))):
        if n % i == 0:
            factors.append(i)
            factors.append(n // i)

    return factors


def get_primes_below_n(n):
    marked = [0] * n
    for i in range(2, n):
        if marked[i] == 0:
            for j in range(i * i, n, i):
                marked[j] = 1

    return [i for i, e in enumerate(marked) if e == 0 and i > 1]


def is_prime(n):
    if n == 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, ceil(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


def n_over_k(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def factorial(n):
    return reduce(mul, range(1,n + 1))
