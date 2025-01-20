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
    total = 0

    nums = sorted(hm.readIntsList(in_file_stream))

    while nums:
        total += nums[-1] - nums[0]
        nums = sorted(hm.readIntsList(in_file_stream))

    print("Total: {}".format(total))
    print("End!\n")


def solve_2(in_file_stream):
    print("Solving!\n")
    total = 0

    nums = sorted(hm.readIntsList(in_file_stream))

    while nums:
        
        for small_n in nums:

            for big_n in reversed(nums):

                if big_n == small_n:
                    break

                if big_n % small_n == 0:
                    total += big_n // small_n

        nums = sorted(hm.readIntsList(in_file_stream))

    print("Total: {}".format(total))
    print("End!\n")


if __name__ == "__main__":

    in_file_stream = open("in.txt", "r")

    # solve_1(in_file_stream)
    solve_2(in_file_stream)
