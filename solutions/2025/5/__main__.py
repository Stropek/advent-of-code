import sys
from pathlib import Path

path = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.append(str(path).replace("\\", "/"))

from solutions.common import HelperMethods as hm
import regex as re
from collections import Counter
import math
import hashlib


def solve_1(in_file_stream, fresh_ids):
    print("Solving!\n")

    total_fresh = 0
    id = in_file_stream.readline().strip("\n")

    while id:

        for fresh_range in fresh_ids:
            if int(id) >= fresh_range[0] and int(id) <= fresh_range[1] + 1:
                total_fresh += 1
                break

        id = in_file_stream.readline().strip("\n")

    print(f"Total fresh: {total_fresh}")
    print("\nEnd!\n")

def solve_2(fresh_ids):
    print("Solving!\n")

    for i in range(len(fresh_ids)):
        
        for j in range(len(fresh_ids)):
            
            low_i = fresh_ids[i][0]
            high_i = fresh_ids[i][1]
            
            low_j = fresh_ids[j][0]
            high_j = fresh_ids[j][1]

            # no common IDs
            if high_i < low_j - 1 or high_j < low_i - 1:
                continue
            # i range is within j range
            elif low_i >= low_j and high_i <= high_j:
                fresh_ids[i] = fresh_ids[j]
            # j range is within i range
            elif low_j >= low_i and high_j <= high_i:
                fresh_ids[j] = fresh_ids[i]
            # i range has higher high
            elif low_i >= low_j and low_i <= high_j:
                fresh_ids[i] = (low_j, high_i)
                fresh_ids[j] = (low_j, high_i)
            # j range has higher high
            elif low_j >= low_i and low_j <= high_i:
                fresh_ids[i] = (low_i, high_j)
                fresh_ids[j] = (low_i, high_j)

        print(fresh_ids)

    dist_ranges = set(fresh_ids)

    total_fresh = 0

    for dist_range in dist_ranges:
        total_fresh += dist_range[1] - dist_range[0] + 1
        
    print(f"Total fresh: {total_fresh}")

    print("\nEnd!\n")

def get_fresh_ids(in_file_stream):

    fresh_ids_list = []
    fresh_ids = in_file_stream.readline().strip("\n").split("-")
    # print(fresh_ids)

    while len(fresh_ids) == 2:

        start = int(fresh_ids[0])
        stop = int(fresh_ids[1])
        
        # print(f"Adding range {start}-{stop}")

        fresh_ids_list += [(start, stop)]
        fresh_ids = in_file_stream.readline().strip("\n").split("-")

        # print(f"Added range {start}-{stop}")

    # print(fresh_ids_list)
    return fresh_ids_list

if __name__ == "__main__":

    in_file_stream = open("full.txt", "r")
    
    fresh_ids = get_fresh_ids(in_file_stream)

    # solve_1(in_file_stream, fresh_ids)
    solve_2(fresh_ids)
