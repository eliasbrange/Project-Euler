from lib import get_primes_below_n

PROBLEM_NAME = 'Summation of primes'


def run():
    output = sum(get_primes_below_n(2000000))
    print_output(output)


def print_output(output):
    print("Problem: " + PROBLEM_NAME)
    print("Output: " + str(output) + "\n")


if __name__ == "__main__":
    run()
