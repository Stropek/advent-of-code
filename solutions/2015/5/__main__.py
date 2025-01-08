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

    vowels = "aeiou"
    forbidden = ["ab", "cd", "pq", "xy"]
    line = in_file_stream.readline().strip("\n")

    nice_cnt = 0

    while line:

        vowels_cnt = 1 if line[0] in vowels else 0
        same = False
        contains_forbidden = False

        for i in range(len(line) - 1):
            left = line[i]
            right = line[i + 1]

            if left == right:
                same = True

            if right in vowels:
                vowels_cnt += 1

            if left + right in forbidden:
                contains_forbidden = True
                break

        if same and vowels_cnt >= 3 and not contains_forbidden:
            print(f"{line} is nice")
            nice_cnt += 1

        line = in_file_stream.readline().strip("\n")

    print("There are {} nice strings".format(nice_cnt))
    print("End!\n")


def solve_2(in_file_stream):
    print("Solving!\n")

    vowels = "aeiou"
    forbidden = ["ab", "cd", "pq", "xy"]
    line = in_file_stream.readline().strip("\n")

    nice_cnt = 0

    while line:

        contains_repeat = False
        contains_pair = False
        pair = ""
        repeat = ""

        for i in range(len(line) - 2):
            left = line[i]
            right = line[i + 1]

            if not contains_pair:
                for j in range(i + 2, len(line) - 1):
                    left_2 = line[j]
                    right_2 = line[j + 1]

                    if left == left_2 and right == right_2:
                        contains_pair = True
                        pair = f"{left}{right}"
                        break

            if i < len(line) - 2:
                further_right = line[i + 2]
                if left == further_right:
                    contains_repeat = True
                    repeat = f"{left}{right}{further_right}"

        if contains_pair:
            print(f"{line} contains a pair: {pair}")
        if contains_repeat:
            print(f"{line} contains a repeat: {repeat}")

        if contains_pair and contains_repeat:
            print(f"{line} is nice")
            nice_cnt += 1

        line = in_file_stream.readline().strip("\n")

    print("There are {} nice strings".format(nice_cnt))
    print("End!\n")


if __name__ == "__main__":

    in_file_stream = open("in.txt", "r")
    # solve_1(in_file_stream)
    solve_2(in_file_stream)
