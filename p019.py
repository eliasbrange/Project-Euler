PROBLEM_NAME = 'Counting sundays'


def run():
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    month_days_leap = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]

    sundays = 0
    current_day = 366 % 7
    for year in range(1901, 2001):
        if is_leap_year(year):
            months = month_days_leap
        else:
            months = month_days

        for month in months:
            current_day += month
            current_day = current_day % 7

            if current_day == 0:
                sundays += 1

        # Add december days.
        current_day += 30

    output = sundays
    print_output(output)


def is_leap_year(year):
    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    return year % 4 == 0


def print_output(output):
    print("Problem: " + PROBLEM_NAME)
    print("Output: " + str(output) + "\n")


if __name__ == "__main__":
    run()
