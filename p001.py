PROBLEM_NAME = 'Multiples of 3 and 5'


def run():
    output = sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])
    print_output(output)


def print_output(output):
    print("Problem: " + PROBLEM_NAME)
    print("Output: " + str(output) + "\n")


if __name__ == "__main__":
    run()
