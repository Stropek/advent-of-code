import sys
from pathlib import Path

path = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.append(str(path).replace("\\", "/"))

from solutions.common import HelperMethods as hm
import regex as re
from collections import Counter
import math


def solve_1(in_file_stream):
    print("Solving!\n")

    connections = dict()
    three_way_connections = set()

    conn_line = hm.readValsList(str, in_file_stream, separator="-")

    while conn_line:
        # print(conn_line[0], conn_line[1])

        conn_left = conn_line[0]
        conn_right = conn_line[1]

        if conn_left not in connections:
            connections[conn_left] = set([conn_right])
        else:
            connections[conn_left].add(conn_right)

        if conn_right not in connections:
            connections[conn_right] = set([conn_left])
        else:
            connections[conn_right].add(conn_left)

        conn_line = hm.readValsList(str, in_file_stream, separator="-")

    for conn, inner_conns in connections.items():
        # print(f'{conn} -> {connections[conn]}')

        for inner_conn in inner_conns:
            # print(f'  {inner_conn} -> {connections[inner_conn]}')

            common_conns = connections[conn].intersection(connections[inner_conn])

            for common_conn in common_conns:
                if conn[0] == "t" or inner_conn[0] == "t" or common_conn[0] == "t":
                    three_way_connections.add(
                        tuple(sorted([conn, inner_conn, common_conn]))
                    )

    for three_way_conn in three_way_connections:
        print(three_way_conn)

    print(f"Total: {len(three_way_connections)}")

    print("End!\n")


def solve_2(in_file_stream):
    print("Solving!\n")

    connections = dict()
    three_way_connections = set()

    conn_line = hm.readValsList(str, in_file_stream, separator="-")

    while conn_line:
        # print(conn_line[0], conn_line[1])

        conn_left = conn_line[0]
        conn_right = conn_line[1]

        if conn_left not in connections:
            connections[conn_left] = set([conn_right])
        else:
            connections[conn_left].add(conn_right)

        if conn_right not in connections:
            connections[conn_right] = set([conn_left])
        else:
            connections[conn_right].add(conn_left)

        conn_line = hm.readValsList(str, in_file_stream, separator="-")

    max_conn_len = 0
    longest_common = set()
    it = 0

    for conn, conn_conns in connections.items():

        it += 1

        if it % 100 == 0:
            print("Processing {}/{}...".format(it, len(connections)))

        # print(f"{conn} -> {conn_conns}")

        for inner_conn in conn_conns:
            common_set = set()
            common_set.add(conn)

            # print(f"  {inner_conn} -> {connections[inner_conn]}")

            common_conns = conn_conns.intersection(connections[inner_conn])
            # print(common_conns)

            if common_conns:
                common_set.add(inner_conn)

            for cc in common_conns:
                has_all = True
                cc_conns = connections[cc]
                for cs in common_set:
                    if cs not in cc_conns:
                        has_all = False
                        break

                if has_all:
                    common_set.add(cc)

            # print("Common set: ", common_set)
            if len(common_set) > max_conn_len:
                max_conn_len = len(common_set)
                longest_common = common_set.copy()
                print("New longest: ", longest_common)

    print(f"Longest common: {','.join(sorted(longest_common))}")
    print("\nEnd!")


def get_conn_to_check(current, conns):

    curr_conn = current[0]
    comm_conns = set(current[1].split("_"))

    left_to_check = set()

    for comm_conn in conns[curr_conn]:
        comm_conn_conns = comm_conns.intersection(conns[comm_conn])
        comm_conn_conns.discard(comm_conns)

        if comm_conn_conns:
            # print(comm_conn)
            # print('_'.join(comm_conn_conns))
            new_to_check = (comm_conn, "_".join(comm_conn_conns))
            left_to_check.add(new_to_check)

    return left_to_check


if __name__ == "__main__":

    in_file_stream = open("in.txt", "r")
    # solve_1(in_file_stream)
    solve_2(in_file_stream)
