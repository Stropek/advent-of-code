import sys
from pathlib import Path

path = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.append(str(path).replace("\\", "/"))

from solutions.common import HelperMethods as hm
import regex as re
from collections import Counter
import math
import hashlib


def solve_1(circuits, distances, shortest_conn_cnt):
    print("Solving!\n")

    new_connections = 0
    i = 0

    while True:

        shortest_dist = distances[i]

        [jb_from, jb_to] = [int(sd) for sd in shortest_dist[0].split("_")]

        # print(shortest_dist[0])
        # print("")
        # print(f"{i}: {jb_from} <===> {jb_to}")
        i += 1

        found_idxs = []

        for k, circuit in circuits.items():
            # print(circuit)

            if jb_from in circuit:
                found_idxs += [k]
            if jb_to in circuit:
                found_idxs += [k]

        new_connections += 1

        if len(found_idxs) > 2:
            print("Not possible - found more than 2 indexes")
            exit()
        elif len(found_idxs) == 2:
            first_idx = found_idxs[0]
            second_idx = found_idxs[1]

            if first_idx != second_idx:
                circuits[first_idx].update(circuits[second_idx])

                del circuits[second_idx]

        if new_connections == shortest_conn_cnt:
            print(f"{shortest_conn_cnt} new connections made. Stopping.")
            break

    # print(circuits)
    circuits_ordered = sorted(circuits, key=lambda k: len(circuits[k]), reverse=True)

    # print(circuits_ordered)

    product = 1
    num_of_circuits = 3

    for i in range(min(num_of_circuits, len(circuits_ordered))):

        print(
            f"{i + 1} longest circuit: {len(circuits[circuits_ordered[i]])} {sorted(circuits[circuits_ordered[i]])}"
        )
        product *= len(circuits[circuits_ordered[i]])

    print(f"Result: {product}")

    print("\nEnd!\n")


def solve_2(circuits, distances, junctions):
    print("Solving!\n")

    i = 0

    jb_from = (0, 0, 0)
    jb_to = (0, 0, 0)

    while len(circuits) > 1:

        shortest_dist = distances[i]

        [jb_from, jb_to] = [int(sd) for sd in shortest_dist[0].split("_")]

        i += 1

        found_idxs = []

        for k, circuit in circuits.items():
            # print(circuit)

            if jb_from in circuit:
                found_idxs += [k]
            if jb_to in circuit:
                found_idxs += [k]

        if len(found_idxs) > 2:
            print("Not possible - found more than 2 indexes")
            exit()
        elif len(found_idxs) == 2:
            first_idx = found_idxs[0]
            second_idx = found_idxs[1]

            if first_idx != second_idx:
                circuits[first_idx].update(circuits[second_idx])

                del circuits[second_idx]

    print(junctions[jb_from])
    print(junctions[jb_to])

    print(circuits)

    print(f"X coordinates product: {junctions[jb_from][0] * junctions[jb_to][0]}")

    print("\nEnd!\n")


def prep_input(in_stream):

    junction_boxes = []
    j_cords = get_junction_box_cords(in_stream)

    while j_cords:
        junction_boxes += [j_cords]

        j_cords = get_junction_box_cords(in_stream)

    distances = {}
    circuits = {}

    for i in range(len(junction_boxes)):

        circuits[i] = set([i])

        for j in range(i + 1, len(junction_boxes)):

            # print(junction_boxes[i])
            # print(junction_boxes[j])

            sorted_idx = sorted([i, j])
            key = f"{sorted_idx[0]}_{sorted_idx[1]}"

            distances[key] = get_distance(junction_boxes[i], junction_boxes[j])

    distances = sorted(distances.items(), key=lambda i: i[1])

    return circuits, distances, junction_boxes


def get_junction_box_cords(in_stream):
    line = in_stream.readline().strip("\n").split(",")

    if len(line) != 3:
        return None

    x = int(line[0])
    y = int(line[1])
    z = int(line[2])

    return (x, y, z)


def get_distance(point_a, point_b):

    return math.sqrt(
        math.pow(point_a[0] - point_b[0], 2)
        + math.pow(point_a[1] - point_b[1], 2)
        + math.pow(point_a[2] - point_b[2], 2)
    )


if __name__ == "__main__":

    file_name = "full.txt"
    # file_name = "in.txt"
    in_file_stream = open(file_name, "r")

    circuits, distances, junctions = prep_input(in_file_stream)

    shortest_conn_cnt = 10 if file_name == "in.txt" else 1000

    # print(j_boxes)
    # print(f"Closest top {shortest_conn_cnt} boxes: {distances}")
    # print(f"Number of jb pairs: {len(distances)}")

    # solve_1(circuits, distances, shortest_conn_cnt)
    solve_2(circuits, distances, junctions)
