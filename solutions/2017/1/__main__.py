import sys
from pathlib import Path

path = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.append(str(path).replace("\\", "/"))

from solutions.common import HelperMethods as hm
import regex as re
from collections import Counter
import math
import hashlib


def solve_1(digits):
    print("Solving!\n")

    total = 0

    for i in range(len(digits)):
        if digits[i] == digits[(i + 1) % len(digits)]:
            total += int(digits[i])

    print(total)

    print("End!\n")


def solve_2(digits):
    print("Solving!\n")

    total = 0

    for i in range(len(digits)):
        print(digits[i], digits[(i + len(digits) // 2) % len(digits)])
        
        if digits[i] == digits[(i + len(digits) // 2) % len(digits)]:
            total += int(digits[i])

    print(total)

    print("End!\n")


if __name__ == "__main__":

    digits = open("in.txt", "r").readline().strip("\n")

    # solve_1(digits)
    solve_2(digits)
