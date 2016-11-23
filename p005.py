from collections import Counter
from functools import reduce
from operator import mul

from lib import get_prime_factors


def run():
    output = reduce(mul, generate_factors(20))
    print_output(output)


def generate_factors(n):
    factor_count = Counter()
    for i in range(2, n + 1):
        factors = list(get_prime_factors(i))
        factor_count = factor_count | Counter(factors)

    return factor_count.elements()


def print_output(output):
    print("Output: " + str(output) + "\n")


if __name__ == "__main__":
    run()
