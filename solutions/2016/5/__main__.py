import sys
import os
from pathlib import Path

path = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.append(str(path).replace("\\", "/"))

from solutions.common import HelperMethods as hm
import regex as re
from collections import Counter
import math
import hashlib


def solve_1(puzzle_input):
    print("Solving!\n")
    password = ""
    it = 0

    while True:
        hashed_input = hashlib.md5((puzzle_input + str(it)).encode()).hexdigest()

        if it % 1000000 == 0:
            print(it)

        if hashed_input[:5] == "00000":
            password += hashed_input[5]
            print("Password: {}".format(password))

            if len(password) == 8:
                break

        it += 1

    print("End!\n")


def solve_2(puzzle_input):
    print("Solving!\n")
    password = "________"
    it = 0

    os.system("cls||clear")
    print("Password: {}".format(password))

    while True:
        hashed_input = hashlib.md5((puzzle_input + str(it)).encode()).hexdigest()

        # if it % 1000000 == 0:
        #     print(it)

        if hashed_input[:5] == "00000":

            sixth_char = hashed_input[5]

            if sixth_char.isdigit():
                position = int(sixth_char)

                if position < 8 and password[position] == "_":
                    password = (
                        password[:position] + hashed_input[6] + password[position + 1 :]
                    )
                    os.system("cls||clear")
                    print("Password: {}".format(password))

                if password.find("_") == -1:
                    break

        it += 1

    print("End!\n")


if __name__ == "__main__":

    puzzle_in = open("in.txt", "r").readline().strip("\n")

    print(puzzle_in)

    # solve_1(puzzle_in)
    solve_2(puzzle_in)
