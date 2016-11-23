def run():
    output = sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])
    print_output(output)


def print_output(output):
    print("Output: " + str(output) + "\n")


if __name__ == "__main__":
    run()
