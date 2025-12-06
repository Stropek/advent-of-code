import sys
from pathlib import Path

path = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.append(str(path).replace("\\", "/"))

from solutions.common import HelperMethods as hm
import regex as re
from collections import Counter
import math
import hashlib


def solve_1(input):
    print("Solving!\n")

    rows = len(input)
    cols = len(input[0])

    print(f"Rows: {rows}")
    print(f"Columns: {cols}")

    for i in range(cols):
        print(f"Operation: {input[rows - 1][i]}")

    total = 0

    for i in range(cols):

        operation = input[rows - 1][i].strip()
        result = int(input[0][i])
        print(result)

        if operation == "+":
            for j in range(1, rows - 1):
                print(input[j][i])
                result += int(input[j][i])
        else:
            for j in range(1, rows - 1):
                print(input[j][i])
                result *= int(input[j][i])

        print(f"Operation {i + 1} result: {result}")

        total += result

    print(f"Total: {total}")
    print("\nEnd!\n")

def solve_2(input):
    print("Solving!\n")

    rows = len(input)
    cols = len(input[0])

    print(f"Rows: {rows}")
    print(f"Columns: {cols}")

    for i in range(cols):
        print(f"Operation: {input[rows - 1][i]}")

    total = 0

    for i in range(cols):

        operation = input[rows - 1][i].strip()

        col_nums = []
        for j in range(rows - 1):
            col_nums += [input[j][i]]
        print(col_nums)

        nums = []
        for k in range(len(col_nums[0])):
            num = ""
            for l in range(len(col_nums)):
                print(col_nums[l][k])
                num += col_nums[l][k]
            
            nums += [int(num)]
        print(nums)

        result = nums[0]

        if operation == "+":
            for m in range(1, len(nums)):
                print(nums[m])
                result += nums[m]
        else:
            for m in range(1, len(nums)):
                print(nums[m])
                result *= nums[m]

        print(f"Operation {i + 1} [{operation}] result: {result}")

        total += result

    print(f"Total: {total}")
    print("\nEnd!\n")

def prep_input(in_stream):

    problems_matrix = []
    problems_matrix_lines = []

    line = in_stream.readline().strip("\n")

    while line:
        problems_matrix_lines += [line]

        line = in_stream.readline().strip("\n")

    operations_indexes = [i for i, ltr in enumerate(problems_matrix_lines[len(problems_matrix_lines) - 1]) if ltr == "+" or ltr == "*"]

    print(problems_matrix_lines)
    print(operations_indexes)

    for i in range(len(problems_matrix_lines)):
        hor_num = []

        for j in range(len(operations_indexes)):

            # print(f"i: {i}   j: {j}")
            # print("")

            if j == len(operations_indexes) - 1:
                hor_num += [problems_matrix_lines[i][operations_indexes[j]:]]
            else:
                hor_num += [problems_matrix_lines[i][operations_indexes[j]:operations_indexes[j + 1] - 1]]

            print(hor_num)
            print("")

        problems_matrix += [hor_num]
    
    print(problems_matrix)

    return problems_matrix

if __name__ == "__main__":

    in_file_stream = open("full.txt", "r")

    input = prep_input(in_file_stream)

    solve_1(input)
    solve_2(input)
