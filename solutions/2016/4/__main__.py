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

    sum = 0

    for line in in_file_stream:
        last_dash_i = line.rfind("-")
        letters_i = line.rfind("[")
        letters = line[letters_i + 1 : letters_i + 6]

        letter_cnt = Counter(line[:last_dash_i].replace("-", "").strip("\n"))

        top_letters = sorted(letter_cnt.items(), key=lambda x: (-x[1], x[0]))

        top_letters_str = "".join([x[0] for x in top_letters[:5]])

        if top_letters_str == letters:
            print("Valid: {}".format(line.strip("\n")))
            sum += int(line[last_dash_i + 1 : letters_i])

    print("Sum: {}".format(sum))
    print("End!\n")


def solve_2(in_file_stream):
    print("Solving!\n")

    sum = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for line in in_file_stream:
        last_dash_i = line.rfind("-")
        letters_i = line.rfind("[")
        letters = line[letters_i + 1 : letters_i + 6]

        letter_cnt = Counter(line[:last_dash_i].replace("-", "").strip("\n"))

        top_letters = sorted(letter_cnt.items(), key=lambda x: (-x[1], x[0]))

        top_letters_str = "".join([x[0] for x in top_letters[:5]])

        if top_letters_str == letters:
            # print("Valid: {}".format(line.strip("\n")))
            sector_id = int(line[last_dash_i + 1 : letters_i])

            decrypted = ""

            for letter in line[:last_dash_i]:
                if letter == "-":
                    decrypted += " "
                else:
                    decrypted += alphabet[(alphabet.index(letter) + sector_id) % 26]

            if "north" in decrypted:
                print("Decrypted: {}".format(decrypted))
                print("Sector ID: {}".format(sector_id))

    # print("Sum: {}".format(sum))
    print("End!\n")


if __name__ == "__main__":

    in_file_stream = open("in.txt", "r")

    # solve_1(in_file_stream)
    solve_2(in_file_stream)
