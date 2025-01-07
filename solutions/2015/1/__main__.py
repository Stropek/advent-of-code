import sys
from pathlib import Path

path = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.append(str(path).replace("\\", "/"))

from solutions.common import HelperMethods as hm
import regex as re
from collections import Counter
import math


def solve_1(instructions):
    return instructions.count("(") - instructions.count(")")


def solve_2(instructions):
    floor = 0
    for i, instruction in enumerate(instructions):
        if instruction == "(":
            floor += 1
        else:
            floor -= 1

        if floor == -1:
            return i + 1


if __name__ == "__main__":

    in_file_stream = open("in.txt", "r").readline().strip("\n")

    # result = solve_1(in_file_stream)
    result = solve_2(in_file_stream)

    print(result)
