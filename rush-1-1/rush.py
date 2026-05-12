import sys


def rush(x, y):
    """
    Print the rush-1-1 rectangle pattern for width x and height y.
    """
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    for row in range(y):
        if row == 0 or row == y - 1:
            # A one-column rectangle has only the corner character.
            line = "o" if x == 1 else "o" + "-" * (x - 2) + "o"
        else:
            line = "|" if x == 1 else "|" + " " * (x - 2) + "|"
        print(line)
