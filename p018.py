PROBLEM_NAME = 'Maximum path sum I'

SMALL_TRIANGLE = []
SMALL_TRIANGLE.append([3])
SMALL_TRIANGLE.append([7, 4])
SMALL_TRIANGLE.append([2, 4, 6])
SMALL_TRIANGLE.append([8, 5, 9, 3])

TRIANGLE = []
TRIANGLE.append([75])
TRIANGLE.append([95, 64])
TRIANGLE.append([17, 47, 82])
TRIANGLE.append([18, 35, 87, 10])
TRIANGLE.append([20, 4, 82, 47, 65])
TRIANGLE.append([19, 1, 23, 75, 3, 34])
TRIANGLE.append([88, 2, 77, 73, 7, 63, 67])
TRIANGLE.append([99, 65, 4, 28, 6, 16, 70, 92])
TRIANGLE.append([41, 41, 26, 56, 83, 40, 80, 70, 33])
TRIANGLE.append([41, 48, 72, 33, 47, 32, 37, 16, 94, 29])
TRIANGLE.append([53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14])
TRIANGLE.append([70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57])
TRIANGLE.append([91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48])
TRIANGLE.append([63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31])
TRIANGLE.append([4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23])


def run():
    output = solve(TRIANGLE)
    print_output(output)


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
