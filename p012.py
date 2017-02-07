from lib import get_factors

PROBLEM_NAME = 'Highly divisable triangular number'


def run():
    i = 1
    while len(get_factors(triangle_number(i))) < 500:
        i += 1

    output = triangle_number(i)
    print_output(output)


def triangle_number(n):
    return sum(range(n+1))


def print_output(output):
    print("Problem: " + PROBLEM_NAME)
    print("Output: " + str(output) + "\n")


if __name__ == "__main__":
    run()
