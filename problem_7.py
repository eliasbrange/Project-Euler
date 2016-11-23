from common_functions import is_prime


def run():
    print(get_prime_n(10001))
    output = 1
    print_output(output)


def get_prime_n(n):
    count = 0
    num = 1
    while count != n:
        num += 1
        if (is_prime(num)):
            count += 1
    return num


def print_output(output):
    print("Output: " + str(output) + "\n")


if __name__ == "__main__":
    run()
