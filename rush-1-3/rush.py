import sys


def rush(x, y):
    """
    Print the rush-1-3 rectangle pattern for width x and height y.
    """
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    for row in range(y):
        if y == 1 or x == 1:
            # The provided edge cases collapse every single-row/column cell to B.
            line = "B" * x
        elif row == 0:
            line = "A" + "B" * (x - 2) + "A"
        elif row == y - 1:
            line = "C" + "B" * (x - 2) + "C"
        else:
            line = "B" + " " * (x - 2) + "B"
        print(line)
