import sys
from pathlib import Path

path = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.append(str(path).replace("\\", "/"))

from solutions.common import HelperMethods as hm
import regex as re
from collections import Counter
import math
import hashlib


def solve_1(jumps):
    print("Solving!\n")
    steps = 0

    i = 0

    while i > -1 and i < len(jumps):
        jump = jumps[i]
        jumps[i] += 1
        i += jump
        steps += 1

    print(steps)

    print("End!\n")


def solve_2(jumps):
    print("Solving!\n")
    steps = 0

    i = 0

    while i > -1 and i < len(jumps):
        jump = jumps[i]
        jumps[i] += -1 if jump > 2 else 1
        i += jump
        steps += 1

    print(steps)

    print("End!\n")


if __name__ == "__main__":

    in_file_stream = open("in.txt", "r")

    jumps = [None] * 1090
    j = 0

    for l in in_file_stream:
        jumps[j] = int(l.strip("\n"))
        j += 1

    # solve_1(jumps)
    solve_2(jumps)
