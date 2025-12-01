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

    current = 50
    total = 0

    line = in_file_stream.readline().strip("\n")

    while (line):

        dir = line[0]
        rotation = int(line[1:])

        if rotation >= 100:
            rotation = rotation % 100

        print(f"Direction: {dir} Rotation: {rotation}")

        if dir == 'R':
            current = (current + rotation) % 100
            
        else:
            if rotation > current:
                current = 100 - (rotation - current)
            else:
                current -= rotation

        print(f"Current position: {current}")

        if current == 0:
            total += 1

        line = in_file_stream.readline().strip("\n")

    print(f"\nPassword: {total}")

    print("\nEnd!\n")


def solve_2(in_file_stream):
    print("Solving!\n")

    current = 50
    total = 0

    line = in_file_stream.readline().strip("\n")

    while (line):

        dir = line[0]
        rotation = int(line[1:])

        if rotation > 100:
            total += rotation // 100
            print(f"total change (line 68): {total}")

            rotation = rotation % 100

        print(f"Direction: {dir} Rotation: {rotation}")

        if dir == 'R':
            if current + rotation > 100:
                total += 1
                print(f"total change (line 77): {total}")

            current = (current + rotation) % 100
            
        else:
            if rotation > current:
                if current > 0:
                    total += 1
                    print(f"total change (line 85): {total}")
                current = 100 - (rotation - current)
            else:
                current -= rotation

        print(f"Current position: {current}")

        if current == 0:
            total += 1
            print(f"total change (line 93): {total}")

        line = in_file_stream.readline().strip("\n")

    print(f"\nPassword: {total}")

    print("End!\n")


if __name__ == "__main__":

    in_file_stream = open("full.txt", "r")
    # solve_1(in_file_stream)
    solve_2(in_file_stream)
