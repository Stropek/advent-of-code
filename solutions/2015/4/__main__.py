import sys
from pathlib import Path

path = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.append(str(path).replace("\\", "/"))

from solutions.common import HelperMethods as hm
import regex as re
from collections import Counter
import math
import hashlib


def solve(input_str, prefix):
    print("Solving!\n")

    num = 0

    while True:

        md5_hash = hashlib.md5(f"{input_str}{num}".encode()).hexdigest()

        if num % 100000 == 0:
            print(f"num: {num}, md5_hash: {md5_hash}")

        if md5_hash[: len(prefix)] == prefix:
            print(f"num: {num}, md5_hash: {md5_hash}")
            break

        num += 1

    print("End!\n")


if __name__ == "__main__":

    in_file_stream = open("in.txt", "r")
    input_s = in_file_stream.read().strip("\n")

    solve(input_s, "000000")
