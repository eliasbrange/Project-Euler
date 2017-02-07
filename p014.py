PROBLEM_NAME = 'Longest Collatz sequence'
PRE_COMPUTED = {}
PRE_COMPUTED[1] = 0


def run():
    chains = [compute(i, 1) for i in range(1, 1000000)]
    output = chains.index(max(chains))
    print_output(output)


def compute(n, count):
    if n in PRE_COMPUTED.keys():
        return PRE_COMPUTED[n]

    k = n

    if k % 2 == 0:
        k = k / 2
    else:
        k = 3 * k + 1

    PRE_COMPUTED[n] = count + compute(k, 1)
    return PRE_COMPUTED[n]


def print_output(output):
    print("Problem: " + PROBLEM_NAME)
    print("Output: " + str(output) + "\n")


if __name__ == "__main__":
    run()
