PROBLEM_NAME = 'Largest palindrome product'


def run():
    output = max([a * b
                  for a in range(101, 1000)
                  for b in range(100, a)
                  if is_palindrome(a * b)])
    print_output(output)


def is_palindrome(n):
    n = str(n)
    return n == n[::-1]


def print_output(output):
    print("Problem: " + PROBLEM_NAME)
    print("Output: " + str(output) + "\n")


if __name__ == "__main__":
    run()
