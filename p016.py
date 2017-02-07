PROBLEM_NAME = 'Power digit sum'


def run():
    value = 2 ** 1000
    output = sum(int(digit) for digit in str(value))
    print_output(output)


def print_output(output):
    print("Problem: " + PROBLEM_NAME)
    print("Output: " + str(output) + "\n")


if __name__ == "__main__":
    run()
