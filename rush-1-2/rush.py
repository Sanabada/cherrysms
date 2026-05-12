import sys


def rush(x, y):
    """
    Print the rush-1-2 rectangle pattern for width x and height y.
    """
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    for row in range(y):
        if y == 1 or x == 1:
            # Collapsed rectangles in this pattern are made only of stars.
            line = "*" * x
        elif row == 0:
            line = "/" + "*" * (x - 2) + "\\"
        elif row == y - 1:
            line = "\\" + "*" * (x - 2) + "/"
        else:
            line = "*" + " " * (x - 2) + "*"
        print(line)
