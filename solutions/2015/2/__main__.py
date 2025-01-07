import sys
from pathlib import Path

path = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.append(str(path).replace("\\", "/"))

from solutions.common import HelperMethods as hm
import regex as re
from collections import Counter
import math


def solve_1(x, y, z):
    return 2 * ((x * y) + (y * z) + (z * x)) + min([x * y, y * z, z * x])


def solve_2(x, y, z):
    return 2 * (x + y) + (x * y * z)


if __name__ == "__main__":

    in_file_stream = open("in.txt", "r")

    total = 0
    dimensions = sorted(hm.readIntsList(in_file_stream, "x"))

    while len(dimensions) == 3:
        x = dimensions[0]
        y = dimensions[1]
        z = dimensions[2]

        solve_1(x, y, z)
        # solve_2(x, y, z)

        print("Solving!")

        total = 0

        while len(dimensions) == 3:
            x = dimensions[0]
            y = dimensions[1]
            z = dimensions[2]

            # total += solve_1(x, y, z)
            total += solve_2(x, y, z)

            dimensions = sorted(hm.readIntsList(in_file_stream, "x"))

        print("Total: " + str(total))
