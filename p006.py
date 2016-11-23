def run():
    n = 100
    output = square_sum(n) - sum_squares(n)
    print_output(output)


def square_sum(n):
    return n ** 2 * (n + 1) ** 2 / 4


def sum_squares(n):
    return n * (n + 1) * (2 * n + 1) / 6


def print_output(output):
    print("Output: " + str(output) + "\n")


if __name__ == "__main__":
    run()
