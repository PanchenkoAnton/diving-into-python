import sys


def calculate_str_digits_sum():
    """
    Calculates summary of all digits in the string.
    """
    return sum([int(num) for num in sys.argv[1]])


if __name__ == '__main__':
    print(calculate_str_digits_sum())
