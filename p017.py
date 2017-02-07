PROBLEM_NAME = 'Number letter counts'


def run():
    output = sum(number_letters(k) for k in range(1, 1001))
    print_output(output)


def number_letters(n):
    if n == 0:
        return 0

    if n == 1000:
        return count('one thousand')

    if n >= 100:
        if n % 100 == 0:
            return number_letters(n // 100) + count('hundred')
        else:
            return (number_letters(n // 100) + count('hundred and') +
                    number_letters(n % 100))

    if n >= 90:
        return number_letters(n % 10) + count('ninety')

    if n >= 80:
        return number_letters(n % 10) + count('eighty')

    if n >= 70:
        return number_letters(n % 10) + count('seventy')

    if n >= 60:
        return number_letters(n % 10) + count('sixty')

    if n >= 50:
        return number_letters(n % 10) + count('fifty')

    if n >= 40:
        return number_letters(n % 10) + count('forty')

    if n >= 30:
        return number_letters(n % 10) + count('thirty')

    if n >= 20:
        return number_letters(n % 10) + count('twenty')

    if n == 19:
        return count('nineteen')

    if n == 18:
        return count('eighteen')

    if n == 17:
        return count('seventeen')

    if n == 16:
        return count('sixteen')

    if n == 15:
        return count('fifteen')

    if n == 14:
        return count('fourteen')

    if n == 13:
        return count('thirteen')

    if n == 12:
        return count('twelve')

    if n == 11:
        return count('eleven')

    if n == 10:
        return count('ten')

    if n == 9:
        return count('nine')

    if n == 8:
        return count('eight')

    if n == 7:
        return count('seven')

    if n == 6:
        return count('six')

    if n == 5:
        return count('five')

    if n == 4:
        return count('four')

    if n == 3:
        return count('three')

    if n == 2:
        return count('two')

    if n == 1:
        return count('one')

def count(str):
    return len([char for char in str if char is not ' '])


def print_output(output):
    print("Problem: " + PROBLEM_NAME)
    print("Output: " + str(output) + "\n")


if __name__ == "__main__":
    run()
