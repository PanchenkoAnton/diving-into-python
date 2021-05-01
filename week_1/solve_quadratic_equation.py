import sys


def find_roots():
    """
    Find roots of a quadratic equation.
    """
    a, b, c = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    d = b ** 2 - 4 * a * c
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    return int(x1), int(x2)


if __name__ == '__main__':
    x1, x2 = find_roots()
    print(x1, x2, sep='\n')
