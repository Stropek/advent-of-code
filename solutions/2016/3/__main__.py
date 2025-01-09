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

    nums = sorted(hm.readIntsList(in_file_stream, separator=" "))
    triangles_cnt = 0

    while nums:

        if sum(nums[0:2]) > nums[2]:
            print("Triangle: ", nums[0:3])
            triangles_cnt += 1

        nums = sorted(hm.readIntsList(in_file_stream, separator=" "))

    print("There are {} triangles".format(triangles_cnt))
    print("End!\n")


def solve_2(in_file_stream):
    print("Solving!\n")

    nums = hm.readIntsList(in_file_stream, separator=" ")
    triangles_cnt = 0

    col_a = [None, None, None]
    col_b = [None, None, None]
    col_c = [None, None, None]

    it = 0
    print(col_a)

    while nums:

        col_a[it % 3] = nums[0]
        col_b[it % 3] = nums[1]
        col_c[it % 3] = nums[2]

        print(col_a)

        if it % 3 == 0:

            if it == 0:
                it += 1
                continue

            print(col_a)

            col_a = sorted(col_a)
            col_b = sorted(col_b)
            col_c = sorted(col_c)

            if sum(col_a[0:2]) > col_a[2]:
                print("Triangle: ", col_a[0:3])
                triangles_cnt += 1
            if sum(col_b[0:2]) > col_b[2]:
                print("Triangle: ", col_b[0:3])
                triangles_cnt += 1
            if sum(col_c[0:2]) > col_c[2]:
                print("Triangle: ", col_c[0:3])
                triangles_cnt += 1

        nums = hm.readIntsList(in_file_stream, separator=" ")
        it += 1

    print("There are {} triangles".format(triangles_cnt))
    print("End!\n")


if __name__ == "__main__":

    in_file_stream = open("in.txt", "r")
    # solve_1(in_file_stream)
    solve_2(in_file_stream)
