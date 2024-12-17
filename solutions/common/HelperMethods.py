import sys

def readVal(parse, in_stream):
    return parse(in_stream.readline().strip("\n").split(' ')[0])
def readValsMap(parse, in_stream):
    return map(parse, in_stream.readline().strip("\n").split(' '))
def readValsList(parse, in_stream, separator): 
    line = in_stream.readline().strip("\n").split(separator)
    
    if len(line) == 1 and line[0] == '':
        return []
    return list(map(parse, line))
def readValMatrix(parse, in_stream, separator, display):
    lines = []
    
    if separator != '':
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
        
        if separator != '':
            line = in_stream.readline().strip("\n").split(separator)
        else:
            line = in_stream.readline().strip("\n")
            
    return lines

def readInt(in_stream):
    return readVal(int, in_stream)
def readIntsMap(in_stream):
    return readValsMap(int, in_stream)
def readIntsList(in_stream, separator=' '):
    return readValsList(int, in_stream, separator)
def readIntsMatrix(in_stream, separator=' ', display=False):
    return readValMatrix(int, in_stream, separator, display)

def readStrMatrix(in_stream, display=False):
    lines = []
    line = in_stream.readline().strip("\n")
    
    while len(line) > 0:
        if display:
            print(line)
        lines += [line]
        
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
        
def display_matrix(matrix):
    for j in range(len(matrix)):
        print(''.join(matrix[j]))
