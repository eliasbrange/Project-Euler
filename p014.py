pre_computed = {}
pre_computed[1] = 0


def run():
    chains = [compute(i, 1) for i in range(1, 1000000)]
    output = chains.index(max(chains))
    print_output(output)


def compute(n, count):
    if n in pre_computed.keys():
        return pre_computed[n]

    k = n

    if k % 2 == 0:
        k = k / 2
    else:
        k = 3 * k + 1

    pre_computed[n] = count + compute(k, 1)
    return pre_computed[n]


def print_output(output):
    print("Output: " + str(output) + "\n")


if __name__ == "__main__":
    run()
