import sys
from pathlib import Path

path = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.append(str(path).replace("\\", "/"))

from solutions.common import HelperMethods as hm
import regex as re
from collections import Counter
import math


def solve_1(in_file_stream):
    print("Solving!\n")
    total = 0

    print("End!\n")


if __name__ == "__main__":

    in_file_stream = open("in.txt", "r")
    solve_1(in_file_stream)
