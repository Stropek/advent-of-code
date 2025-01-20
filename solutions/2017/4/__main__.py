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

    for line in in_file_stream:
        words = line.split()

        cnt_words = Counter(words).most_common()

        # print(cnt_words)

        if cnt_words[0][1] > 1:
            print("Invalid: {}".format(cnt_words))
            continue

        total += 1

    print("Total valid: {}".format(total))

    print("End!\n")


def solve_2(in_file_stream):
    print("Solving!\n")
    total = 0

    for line in in_file_stream:
        words = line.split()

        cnt_words = Counter(words).most_common()

        # print(cnt_words)

        if cnt_words[0][1] > 1:
            print("Invalid: {}".format(cnt_words))
            continue

        sorted_words = [None] * len(words)
        for i in range(len(words)):
            sorted_word = "".join(sorted(words[i]))
            sorted_words[i] = sorted_word

        cnt_sorted_words = Counter(sorted_words).most_common()

        if cnt_sorted_words[0][1] > 1:
            print("Invalid (sorted): {}".format(cnt_sorted_words))
            continue

        total += 1

    print("Total valid: {}".format(total))

    print("End!\n")


if __name__ == "__main__":

    in_file_stream = open("in.txt", "r")
    # solve_1(in_file_stream)
    solve_2(in_file_stream)
