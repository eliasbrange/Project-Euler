def run():
    target_sum = 1000

    triplets = [[a, b, target_sum - (a + b)]
                for b in range(2, target_sum - 4)
                for a in range(1, b)
                if a ** 2 + b ** 2 == (target_sum - (a + b)) ** 2]

    output = triplets[0]
    output = output[0] * output[1] * output[2]
    print_output(output)


def print_output(output):
    print("Output: " + str(output) + "\n")


if __name__ == "__main__":
    run()
