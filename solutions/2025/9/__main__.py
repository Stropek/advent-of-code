import sys
from pathlib import Path

path = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.append(str(path).replace("\\", "/"))

from solutions.common import HelperMethods as hm
import regex as re
from collections import Counter
import math
import hashlib
import numpy as np


def solve_1(grid, tiles):
    print("Solving!\n")

    max_area = 0

    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            area = get_area(tiles[i], tiles[j])
            # print(f"Area for {tiles[i]} and {tiles[j]}: {area}")

            max_area = max(max_area, area)

    print(f"Max area: {max_area}")
    print("\nEnd!\n")


def solve_2(grid, tiles):
    print("Solving!\n")

    start_x = 0
    start_y = 0

    end_x = 0
    end_y = 0

    max_area = 0

    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            if check_if_area_is_valid(tiles[i], tiles[j], grid):
                area = get_area(tiles[i], tiles[j])
                print(f"Area for {tiles[i]} and {tiles[j]}: {area}")

                max_area = max(max_area, area)

                if max_area == 3008237000:
                    start_x = min(tiles[i][0], tiles[j][0])
                    start_y = min(tiles[i][1], tiles[j][1])

                    end_x = max(tiles[i][0], tiles[j][0])
                    end_y = max(tiles[i][1], tiles[j][1])
                    break
            if max_area == 3008237000:
                break

    print(f"From ({start_x}, {start_y}) to ({end_x}, {end_y})")

    print(f"Max area: {max_area}")
    print("\nEnd!\n")


def check_if_area_is_valid(point_a, point_b, grid):

    min_x = min(point_a[0], point_b[0])
    min_y = min(point_a[1], point_b[1])

    max_x = max(point_a[0], point_b[0])
    max_y = max(point_a[1], point_b[1])

    # print(f"Min x: {min_x} Min y: {min_y}")
    # print(f"Max x: {max_x} Max y: {max_y}")
    sub_grid = [r[min_x : max_x + 1] for r in grid[min_y : max_y + 1]]

    for i in range(min_x, max_x + 1):
        for j in list(set([min_y, max_y])):
            # print(f"Checking (x, y) = ({i, j})")

            if grid[j][i] == "-":
                # print("Area is NOT valid: '-' found in a hotizontal edge")
                # hm.display_matrix(sub_grid, coloured=True)
                return False

    for i in list(set([min_x, max_x])):
        for j in range(min_y, max_y + 1):
            # print(f"Checking (x, y) = ({i, j})")

            if grid[j][i] == "-":
                # print("Area is NOT valid: '-' found in a vertical edge")
                # hm.display_matrix(sub_grid, coloured=True)
                return False

    # hm.display_matrix(sub_grid, coloured=True)
    # print("Area is valid")
    return True


def get_area(point_a, point_b):

    length = abs(point_a[0] - point_b[0]) + 1
    height = abs(point_a[1] - point_b[1]) + 1

    return height * length


def prep_input(in_stream):

    tiles = []

    max_x = 0
    max_y = 0

    while True:
        tile_cords = in_stream.readline().strip("\n").split(",")

        if len(tile_cords) < 2:
            break

        x = int(tile_cords[0])
        y = int(tile_cords[1])
        tiles += [(x, y)]

        max_x = max(max_x, x)
        max_y = max(max_y, y)

    # grid = [["."] * (max_x + 3) for _ in range(max_y + 2)]
    grid = np.full((max_y + 2, max_x + 3), ".")

    # print(tiles)
    # hm.display_matrix(grid, coloured=True)

    for i in range(len(tiles) - 1):
        tile = tiles[i]
        next_tile = tiles[i + 1]

        grid[tile[1]][tile[0]] = "#"

        rx_1 = tile[0]
        ry_1 = tile[1]
        rx_2 = next_tile[0]
        ry_2 = next_tile[1]

        if rx_1 == rx_2:
            fill_vertical(ry_1, ry_2, rx_1, grid)
        if ry_1 == ry_2:
            fill_horizontal(rx_1, rx_2, ry_1, grid)

    tile = tiles[-1]
    grid[tile[1]][tile[0]] = "#"

    rx_1 = tiles[-1][0]
    ry_1 = tiles[-1][1]
    rx_2 = tiles[0][0]
    ry_2 = tiles[0][1]

    if rx_1 == rx_2:
        fill_vertical(ry_1, ry_2, rx_1, grid)
    if ry_1 == ry_2:
        fill_horizontal(rx_1, rx_2, ry_1, grid)

    fill_outer_area(grid)

    if len(grid) < 100:
        hm.display_matrix(grid, coloured=True)

    print("")

    return grid, tiles


def fill_vertical(start_y, end_y, x, grid):

    from_y = min(start_y, end_y)
    to_y = max(start_y, end_y)

    for gt_y in range(from_y + 1, to_y):
        grid[gt_y][x] = "X"


def fill_horizontal(start_x, end_x, y, grid):

    from_x = min(start_x, end_x)
    to_x = max(start_x, end_x)

    for gt_x in range(from_x + 1, to_x):
        grid[y][gt_x] = "X"


def fill_outer_area(grid):

    print("Filling outer area")

    grid[0][0] = "-"
    # print(f"Assigning '-' to {len(grid) - 1}, {len(grid[0]) - 1}")
    grid[len(grid) - 1][len(grid[0]) - 1] = "-"

    for i in range(len(grid)):

        if i % 1000 == 0:
            print(f"Processing row {i}")

        for j in range(len(grid[0])):
            if i == 0 and j == 0:
                continue

            if grid[i][j] == ".":
                if j > 0:
                    if grid[i][j - 1] == "-":
                        grid[i][j] = "-"

                if i > 0:
                    if grid[i - 1][j] == "-":
                        grid[i][j] = "-"

            if grid[len(grid) - 1 - i][len(grid[0]) - 1 - j] == ".":
                if j > 0:
                    # print(f"{i} {j} {len(grid[0]) - j}")

                    if grid[len(grid) - 1 - i][len(grid[0]) - j] == "-":
                        # print(
                        #     f"Assigning '-' to {len(grid) - 1 - i}, {len(grid[0]) - 1 - j}"
                        # )
                        grid[len(grid) - 1 - i][len(grid[0]) - 1 - j] = "-"

                if i > 0:
                    if grid[len(grid) - i][len(grid[0]) - 1 - j] == "-":
                        # print(
                        #     f"Assigning '-' to {len(grid) - 1 - i}, {len(grid[0]) - 1 - j}"
                        # )
                        grid[len(grid) - 1 - i][len(grid[0]) - 1 - j] = "-"
            # fill from the opposite corner too
            # if grid[len(grid) - i]


if __name__ == "__main__":

    in_file_stream = open("full.txt", "r")

    grid, tiles = prep_input(in_file_stream)

    # solve_1(grid, tiles)
    solve_2(grid, tiles)
