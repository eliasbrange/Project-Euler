from lib import fibonacci_val

PROBLEM_NAME = 'Even Fibonacci numbers'


def run():
    output = sum([x for x in fibonacci_val(4000000) if x % 2 == 0])
    print_output(output)


def print_output(output):
    print("Problem: " + PROBLEM_NAME)
    print("Output: " + str(output) + "\n")


if __name__ == "__main__":
    run()
