import sys
from pathlib import Path

path = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.append(str(path).replace("\\", "/"))

from solutions.common import HelperMethods as hm
import regex as re
from collections import Counter
import math
import hashlib


def solve_1(t_val):
    print("Solving!\n")
    curr = (0, 0)

    it = 1
    step = 2

    sides = 4

    while it < t_val:
        for i in range(sides):
            for j in range(step):
                if it == t_val:
                    break
                if i == 0:
                    if j == 0:
                        curr = (curr[0] + 1, curr[1])
                    else:
                        curr = (curr[0], curr[1] + 1)
                elif i == 1:
                    curr = (curr[0] - 1, curr[1])
                elif i == 2:
                    curr = (curr[0], curr[1] - 1)
                elif i == 3:
                    curr = (curr[0] + 1, curr[1])

                it += 1

                # print("val: ", it, "  pos: ", curr)

        step += 2

    print(abs(curr[0]) + abs(curr[1]))

    print("End!\n")


def solve_2(t_val):
    print("Solving!\n")
    curr = (0, 0)

    vals = {(0, 0): 1}

    it = 1
    step = 2

    sides = 4

    while vals[curr] < t_val:
        for i in range(sides):
            for j in range(step):
                if it == t_val:
                    break
                if i == 0:
                    if j == 0:
                        curr = (curr[0] + 1, curr[1])
                    else:
                        curr = (curr[0], curr[1] + 1)
                elif i == 1:
                    curr = (curr[0] - 1, curr[1])
                elif i == 2:
                    curr = (curr[0], curr[1] - 1)
                elif i == 3:
                    curr = (curr[0] + 1, curr[1])

                vals[curr] = sum_neighbours(curr, vals)

                it += 1

                print("val: ", vals[curr], "  pos: ", curr)

                if vals[curr] > t_val:
                    print("End!")
                    print(vals[curr])
                    break
        step += 2

    print(abs(curr[0]) + abs(curr[1]))

    print("End!\n")


def sum_neighbours(curr, vals):
    total = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue

            if (curr[0] + i, curr[1] + j) in vals:
                total += vals[(curr[0] + i, curr[1] + j)]

    return total


if __name__ == "__main__":

    t_val = int(open("in.txt", "r").read().strip("\n"))
    # solve_1(t_val)
    solve_2(t_val)
