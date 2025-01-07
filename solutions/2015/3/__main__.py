import sys
from pathlib import Path

path = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.append(str(path).replace("\\", "/"))

from solutions.common import HelperMethods as hm
import regex as re
from collections import Counter
import math


def solve_1(directions):
    print("Solving!\n")

    current = (0, 0)
    visited = {current}

    moves = {"^": (0, 1), "v": (0, -1), ">": (1, 0), "<": (-1, 0)}

    for direction in directions:
        current = (current[0] + moves[direction][0], current[1] + moves[direction][1])
        visited.add(current)

    print("Santa visited {} houses".format(len(visited)))


def solve_2(directions):
    print("Solving!\n")

    current_s = (0, 0)
    current_r = (0, 0)
    santa_visited = {current_s}
    robot_visited = {current_r}

    moves = {"^": (0, 1), "v": (0, -1), ">": (1, 0), "<": (-1, 0)}

    it = 0
    for direction in directions:
        if it % 2 == 0:
            current_s = (
                current_s[0] + moves[direction][0],
                current_s[1] + moves[direction][1],
            )
            santa_visited.add(current_s)
            print('Santa: ', current_s)
        else:
            current_r = (
                current_r[0] + moves[direction][0],
                current_r[1] + moves[direction][1],
            )
            robot_visited.add(current_r)
            print('Robot: ', current_r)
            
        it += 1

    visited = santa_visited.union(robot_visited)

    print("Santa and robot visited {} houses".format(len(visited)))


if __name__ == "__main__":

    in_file_stream = open("in.txt", "r")

    directions = in_file_stream.readline().strip("\n")

    # solve_1(directions)
    solve_2(directions)
