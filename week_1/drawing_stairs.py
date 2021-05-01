import sys


def draw_stairs():
    """
    Draws stairs based on given size.
    """
    size = int(sys.argv[1])
    return '\n'.join([' ' * (size-idx-1) + '#' * (idx+1) for idx in range(size)])


if __name__ == '__main__':
    print(draw_stairs())
