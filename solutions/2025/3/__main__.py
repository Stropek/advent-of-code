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

    total_joltage = 0

    bank = in_file_stream.readline().strip("\n")

    while bank:
        print(bank)

        highest_first_digit = 1
        highest_second_digit = 1

        for battery in range(len(bank) - 1):
            # print(f"{bank[battery]}{bank[battery + 1]}")

            battery_joltage = int(bank[battery])
            next_battery_joltage = int(bank[battery + 1])

            if battery_joltage > highest_first_digit:
                highest_first_digit = battery_joltage
                highest_second_digit = next_battery_joltage
                continue

            highest_second_digit = max(highest_second_digit, battery_joltage, next_battery_joltage)

        print(f"MAX: {highest_first_digit}{highest_second_digit}")

        total_joltage += int(f"{highest_first_digit}{highest_second_digit}")

        bank = in_file_stream.readline().strip("\n")

    print(f"TOTAL {total_joltage}\n")
    print("\nEnd!\n")


def solve_2(in_file_stream):
    print("Solving!\n")

    total_joltage = 0

    bank = [int(x) for x in in_file_stream.readline().strip("\n")]

    while bank:
        print(bank)

        bank_joltage = ""

        left_to_check = len(bank) - 11
        current_index = 0

        while left_to_check > 0:
            print(f"Current index: {current_index}\nLeft to check: {left_to_check}")

            (joltage, index) = find_max(bank[current_index:], left_to_check)
            print(f"Joltage: {joltage} at {index}")

            bank_joltage = f"{bank_joltage}{joltage}"

            print(f"Total joltage: {bank_joltage} \n")

            current_index += (index + 1)
            left_to_check -= index

            if len(bank_joltage) == 12:
                total_joltage += int(bank_joltage)
                break

        bank = [int(x) for x in in_file_stream.readline().strip("\n")]
    
    print(f"Total joltage: {total_joltage}")

    print("\nEnd!\n")

def find_max(bank_vals, to_check):

    max_joltage = max(bank_vals[:to_check])
    max_index = bank_vals.index(max_joltage)

    return max_joltage, max_index


if __name__ == "__main__":

    in_file_stream = open("full.txt", "r")

    # solve_1(in_file_stream)
    solve_2(in_file_stream)
