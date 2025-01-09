import sys
import os

BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
LIGHT_GRAY = "\033[37m"
DARK_GRAY = "\033[90m"
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
WHITE = "\033[97m"

RESET = "\033[0m"  # called to return to standard terminal text color


def readVal(parse, in_stream):
    return parse(in_stream.readline().strip("\n").split(" ")[0])


def readValsMap(parse, in_stream):
    return map(parse, in_stream.readline().strip("\n").split(" "))


def readValsTuple(parse, in_stream, separator=" "):
    return tuple(map(parse, in_stream.readline().strip("\n").split(separator)))


def readValsList(parse, in_stream, separator):
    line = [l for l in in_stream.readline().strip("\n").split(separator) if l != ""]

    if len(line) == 1 and line[0] == "":
        return []
    return list(map(parse, line))


def readValMatrix(parse, in_stream, separator, display):
    lines = []

    if separator != "":
        line = in_stream.readline().strip("\n").split(separator)
    else:
        line = in_stream.readline().strip("\n")

    while len(line) > 0:

        if len(line) == 1:
            line = [parse(c) for c in line[0]]
        else:
            line = list(map(parse, line))

        if display:
            print(line)

        lines.append(line)

        if separator != "":
            line = in_stream.readline().strip("\n").split(separator)
        else:
            line = in_stream.readline().strip("\n")

    return lines


def readInt(in_stream):
    return readVal(int, in_stream)


def readIntsMap(in_stream):
    return readValsMap(int, in_stream)


def readIntsList(in_stream, separator=" "):
    return readValsList(int, in_stream, separator)


def readIntsMatrix(in_stream, separator=" ", display=False):
    return readValMatrix(int, in_stream, separator, display)


def readStrMatrix(in_stream, display=False):
    lines = []
    line = in_stream.readline().strip("\n")

    j = 0
    while len(line) > 0:
        if display:
            print(line)
        lines.append([])

        lines[j] = [""] * len(line)
        i = 0
        for lc in line:
            lines[j][i] = lc
            i += 1

        j += 1
        line = in_stream.readline().strip("\n")

    return lines


def write(out, text):
    if out == sys.stdout:
        print(str(text))
    else:
        out.write(str(text))


def write_line(out, text):
    if out == sys.stdout:
        print(str(text) + "\n")
    else:
        out.write(str(text) + "\n")


def display_matrix(matrix, coloured=False):
    # os.system('cls||clear')

    if coloured:
        for j in range(len(matrix)):
            line = "".join(matrix[j]).replace("O", GREEN + "O" + RESET)
            line = line.replace("#", DARK_GRAY + "#" + RESET)
            line = line.replace("W", BRIGHT_RED + "W" + RESET)
            line = line.replace("S", BRIGHT_GREEN + "S" + RESET)
            line = line.replace("E", BRIGHT_BLUE + "E" + RESET)
            line = line.replace("1", MAGENTA + "1" + RESET)
            # line = line.replace('>', MAGENTA + '>' + RESET)
            # line = line.replace('<', MAGENTA + '<' + RESET)
            # line = line.replace('v', MAGENTA + 'v' + RESET)
            # line = line.replace('^', MAGENTA + '^' + RESET)
            print(line)
    else:
        for j in range(len(matrix)):
            print("".join(matrix[j]))
