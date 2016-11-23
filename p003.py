from lib import get_unique_prime_factors


def run():
    output = max(list(get_unique_prime_factors(600851475143)))
    print_output(output)


def print_output(output):
    print("Output: " + str(output) + "\n")


if __name__ == "__main__":
    run()
