PROBLEM_NAME = 'Maximum path sum II'


def run():
    triangle = read_file()
    output = solve(triangle)
    print_output(output)


def read_file():
    triangle = []
    with open('input_files/p067.txt', 'r') as file:
        for line in file.readlines():
            line = list(map(int, line.strip().split(' ')))
            triangle.append(line)

    return triangle


def solve(triangle):
    last_row = len(triangle) - 1
    if last_row == 0:
        return triangle[0][0]

    current_row = last_row - 1

    for i, val in enumerate(triangle[current_row]):
        triangle[current_row][i] = max(triangle[current_row][i] +
                                       triangle[last_row][i],
                                       triangle[current_row][i] +
                                       triangle[last_row][i + 1])

    triangle = triangle[0:last_row]
    return solve(triangle)


def print_output(output):
    print("Problem: " + PROBLEM_NAME)
    print("Output: " + str(output) + "\n")


if __name__ == "__main__":
    run()
