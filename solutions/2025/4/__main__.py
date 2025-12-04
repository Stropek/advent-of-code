import sys
from pathlib import Path

path = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.append(str(path).replace("\\", "/"))

from solutions.common import HelperMethods as hm
import regex as re
from collections import Counter
import math
import hashlib


def solve_1(rolls):
    print("Solving!\n")

    accessible_rolls = 0

    for i in range(len(rolls)):

        print(f"line {i}:")

        for j in range(len(rolls[i])):

            # print(rolls[i][j])

            if is_a_roll(i, j, rolls) and is_roll_accessible(i, j, rolls):
                accessible_rolls += 1

    print(f"Total accessible: {accessible_rolls}")

    print("\nEnd!\n")

def solve_2(rolls):
    print("Solving!\n")

    accessible_rolls = 0

    while True:
        removed_rolls = 0
    
        for i in range(len(rolls)):

            # print(f"line {i}:")

            for j in range(len(rolls[i])):

                # print(rolls[i][j])

                if is_a_roll(i, j, rolls) and is_roll_accessible(i, j, rolls):
                    accessible_rolls += 1
                    removed_rolls += 1
                    rolls[i][j] = "."

        if removed_rolls == 0:
            break
    
        print(f"Removed {removed_rolls} rolls")
        hm.display_matrix(rolls)
        print("\n")

    print(f"Total accessible: {accessible_rolls}")

    print("\nEnd!\n")

def is_roll_accessible(i, j, rolls):

    cnt_adj_rools = 0

    if i > 0:

        if j > 0:
            if is_a_roll(i - 1, j - 1, rolls):
                cnt_adj_rools += 1
        if is_a_roll(i - 1, j, rolls):
            cnt_adj_rools += 1
        if j < len(rolls[i]) - 1:
            if is_a_roll(i - 1, j + 1, rolls):
                cnt_adj_rools += 1

    if j > 0:
        if is_a_roll(i, j - 1, rolls):
            cnt_adj_rools += 1
    if j < len(rolls[i]) - 1:
        if is_a_roll(i, j + 1, rolls):
            cnt_adj_rools += 1

    if i < len(rolls) - 1:
        
        if j > 0:
            if is_a_roll(i + 1, j - 1, rolls):
                cnt_adj_rools += 1
        if is_a_roll(i + 1, j, rolls):
            cnt_adj_rools += 1
        if j < len(rolls[i]) - 1:
            if is_a_roll(i + 1, j + 1, rolls):
                cnt_adj_rools += 1
    
    # if cnt_adj_rools < 4:
    #     print(f"Roll at position [{i}][{j}] has {cnt_adj_rools} adjacent rolls.")

    return cnt_adj_rools < 4

def is_a_roll(i, j, rolls):
    return True if rolls[i][j] == "@" else False


if __name__ == "__main__":

    in_file_stream = open("full.txt", "r")
    
    rolls = hm.readValMatrix(str, in_file_stream, display=False)

    # solve_1(rolls)
    solve_2(rolls)
