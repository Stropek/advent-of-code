import sys
from pathlib import Path

path = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.append(str(path).replace("\\", "/"))

from solutions.common import HelperMethods as hm
import regex as re
from collections import Counter
import math
import hashlib


def solve_1(in_file_stream):
    print("Solving!\n")
    curr = (0, 0)
    moves = {"D": (0, 1), "U": (0, -1), "L": (-1, 0), "R": (1, 0)}
    nums = {
        (-1, -1): "1",
        (0, -1): "2",
        (1, -1): "3",
        (-1, 0): "4",
        (0, 0): "5",
        (1, 0): "6",
        (-1, 1): "7",
        (0, 1): "8",
        (1, 1): "9",
    }

    result = ""
    for line in in_file_stream:
        line = line.strip("\n")

        for char in line:
            move = moves[char]
            new = (curr[0] + move[0], curr[1] + move[1])
            if new in nums:
                curr = new

        result += nums[curr]

    print(result)

    print("\nEnd!")


def solve_2(in_file_stream):
    print("Solving!\n")
    curr = (0, 0)
    moves = {"D": (0, 1), "U": (0, -1), "L": (-1, 0), "R": (1, 0)}
    nums = {
        (0, 0): "5",
        (1, -1): "2",
        (1, 0): "6",
        (1, 1): "A",
        (2, -2): "1",
        (2, -1): "3",
        (2, 0): "7",
        (2, 1): "B",
        (2, 2): "D",
        (3, -1): "4",
        (3, 0): "8",
        (3, 1): "C",
        (4, 0): "9",
    }

    result = ""
    for line in in_file_stream:
        line = line.strip("\n")

        for char in line:
            move = moves[char]
            new = (curr[0] + move[0], curr[1] + move[1])
            if new in nums:
                curr = new

        result += nums[curr]

    print(result)

    print("\nEnd!")


if __name__ == "__main__":

    in_file_stream = open("in.txt", "r")

    # solve_1(in_file_stream)
    solve_2(in_file_stream)
