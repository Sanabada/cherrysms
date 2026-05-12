import sys


def rush(x, y):
    """
    Print the rush-1-4 rectangle pattern for width x and height y.
    """
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    for row in range(y):
        if y == 1 or x == 1:
            # The assignment examples use B for all collapsed borders.
            line = "B" * x
        elif row == 0 or row == y - 1:
            line = "A" + "B" * (x - 2) + "C"
        else:
            line = "B" + " " * (x - 2) + "B"
        print(line)
