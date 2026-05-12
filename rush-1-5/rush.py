import sys


def rush(x, y):
    """
    Print the rush-1-5 rectangle pattern for width x and height y.
    """
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    for row in range(y):
        if y == 1 or x == 1:
            # Single-row and single-column examples are plain B borders.
            line = "B" * x
        elif row == 0:
            line = "A" + "B" * (x - 2) + "C"
        elif row == y - 1:
            line = "C" + "B" * (x - 2) + "A"
        else:
            line = "B" + " " * (x - 2) + "B"
        print(line)
