from lib import n_over_k

PROBLEM_NAME = 'Lattice paths'


def run():
    k = 20
    n = 2 * k
    output = n_over_k(n, k)
    print_output(output)


def print_output(output):
    print("Problem: " + PROBLEM_NAME)
    print("Output: " + str(output) + "\n")


if __name__ == "__main__":
    run()
