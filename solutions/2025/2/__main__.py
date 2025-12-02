import sys
from pathlib import Path

path = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.append(str(path).replace("\\", "/"))

from solutions.common import HelperMethods as hm
import regex as re
from collections import Counter
import math
import hashlib


def solve_1(ranges):
    print("Solving!\n")

    invalid_sum = 0

    for r in ranges:
        [first, last] = [int(x) for x in r.split("-")]
        # print(f"From: {first} To: {last}")

        for id in range(first, last + 1):
            # print(id)
            if not is_valid(str(id)):
                invalid_sum += id

    print(f"Sum of invalid IDs: {invalid_sum}")

    print("\nEnd!\n")


def solve_2(ranges):
    print("Solving!\n")

    invalid_sum = 0

    for r in ranges:
        [first, last] = [int(x) for x in r.split("-")]
        # print(f"From: {first} To: {last}")

        for id in range(first, last + 1):
            # print(id)
            if not is_valid_2(str(id)):
                invalid_sum += id

    print(f"Sum of invalid IDs: {invalid_sum}")

    print("End!\n")

def is_valid(id):
    is_valid = True

    id_len = len(id)

    if id_len % 2 == 0:
        # print(f"Checking {id}")
        
        for i in range(id_len // 2):
            if id[i] != id[i + id_len // 2]:
                break

            if i == id_len // 2 - 1:
                is_valid = False
                print(f"INVALID ID: {id}")

    return is_valid

def is_valid_2(id):
    is_valid = True

    id_len = len(id)

    # print(f"Checking {id}")
        
    for i in range(1, (id_len // 2) + 1):

        if not is_valid:
            break

        remainder = int(id_len % i)
        if remainder == 0:

            pattern = id[0:i]

            # print(f"pattern: {pattern}")

            for j in range(0, id_len - i + 1, len(pattern)):

                # print(f"j: {j}")

                if id[j:j + len(pattern)] == pattern:
                    
                    if j == id_len - i:
                        is_valid = False
                        print(f"INVALID ID: {id}")
                else:
                    break

    return is_valid

if __name__ == "__main__":

    in_file_stream = open("full.txt", "r")

    ranges = in_file_stream.readline().strip("\n").split(",")

    # solve_1(ranges)
    solve_2(ranges)
