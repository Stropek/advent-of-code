import sys
from pathlib import Path

path = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.append(str(path).replace('\\', '/'))

from solutions.common import HelperMethods as hm
import regex as re
from collections import Counter
import math


def solve_1(in_file_stream, size, bytes_to_read, return_on_first=False):
    print('Solving!\n')
    total = 0
    
    memory_space = [None] * size  
    memory_space_cp = [None] * size
    
    for i in range(size):
        memory_space[i] = ['.'] * size
        memory_space_cp[i] = ['.'] * size
    
    # hm.display_matrix(memory_space)
    
    for _ in range(bytes_to_read):
        (s_x, s_y) = hm.readValsTuple(int, in_file_stream, separator=',')
        memory_space[s_y][s_x] = '#'
        memory_space_cp[s_y][s_x] = '#'
    
    # memory_space_cp = memory_space.copy()
    
    hm.display_matrix(memory_space)
    
    start_x = 0
    start_y = 0
    
    min_moves = -1
    path_all_final_moves = set()
    
    crossroads = dict()
    crossroads[0] = set((start_x, start_y))
    crossroads[-1] = dict()
    crossroads[-1][(start_x, start_y)] = 1000000
    
    start_path = (0, start_x, start_y, 0, (-1, -1))
    
    (next_moves, min_moves, path_all_final_moves) = find_next(start_path, crossroads, memory_space, min_moves, path_all_final_moves)
    
    it = 0
    max_it = 5
    
    used_spaces = set()
    used_spaces.add((start_x, start_y))
            
    print('Found next moves: {}'.format(next_moves))

    while next_moves:
                
        next_move = next_moves.pop()
        
        used_spaces.add((next_move[1], next_move[2]))
                
        # print('Path {}: {} {}, dir: {}'.format(next_move[0], next_move[1], next_move[2], next_move[3]))
        (next_for_path, min_moves, path_all_final_moves) = find_next(next_move, crossroads, memory_space, min_moves, path_all_final_moves)
        
        if return_on_first and min_moves > 0:
            return True
            
        if len(next_for_path) == 0:
            # print('Path {} reached a DEAD END at {} {}, val: {}'.format(next_move[0], next_move[1], next_move[2], next_move[3]))
            continue
                
        for nfp in next_for_path:
                        
            if nfp[3] > min_moves and min_moves > 0:
                # print('Path {} is longer than min_moves {} and it has {}'.format(nfp[0], min_moves, nfp[3]))
                continue
                        
            # print('Path {} is not longer than min_moves {}'.format(next_move[3], min_moves))
                        
            next_moves += [nfp]
                            
        if it % 10 == 0:            
            for used_space in used_spaces:
                memory_space_cp[used_space[1]][used_space[0]] = 'O'
                
            used_spaces = set()
            hm.display_matrix(memory_space_cp, coloured=True)
            print('Bytes to read: {}'.format(bytes_to_read))
            print('Iteration: {}'.format(it))
            print('\n')
            
        it += 1
        
    for used_space in used_spaces:
        memory_space_cp[used_space[1]][used_space[0]] = 'O'
        
    hm.display_matrix(memory_space_cp, coloured=True)
    
    print('\nOriginal:')
    hm.display_matrix(memory_space, coloured=True)
    
    print('Total iterations: {}'.format(it))
    print('Min moves: {}'.format(min_moves))
    print('Bytes toread: '.format(bytes_to_read))
    print('Iteration: {}'.format(it))
    print('\nEnd!\n')
    return False

        
def find_next(move, crossroads, maze, min_moves, path_all_final_moves):
    # print('Finding next for path: {}'.format(move))
        
    i = move[0]
    x = move[1]
    y = move[2]
    val = move[3]
    (prev_x, prev_y) = move[4]
    
    size = len(maze)
    
    next_moves = []
    path_final_move = None
    
    if (x, y) not in crossroads[-1]:
        crossroads[-1][(x, y)] = val
    else:
        if crossroads[-1][(x, y)] <= val:
            # print('Path {} crossing ({}, {}) with a value {} - already have a lower or equal value ({}) here'.format(i, x, y, val, crossroads[-1][(x, y)]))
            return ([], min_moves, path_all_final_moves)
        
        crossroads[-1][(x, y)] = val
        
    # print('Looking for next at ({}, {}), facing {}, with val {}'.format(x, y, val))
            
    i_i = 0
    path_i = [i, len(crossroads), len(crossroads) + 1]
    
    # print('New paths: {}'.format(path_i))
            
    # check if last space is reachable
    if x == size - 2 and y == size - 1:
        path_final_move = (i, x + 1, y, val + 1, (x, y))
    elif x == size - 1 and y == size - 2:
        path_final_move = (i, x, y + 1, val + 1, (x, y))

    if path_final_move:
        # print('Path {} reached the finish line at {}'.format(i, path_final_move))
            
        if min_moves == -1:
            min_moves = path_final_move[3]
            # path_all_final_moves = path_moves.copy()
            # print(path_all_final_moves)
        elif path_final_move[3] < min_moves:
            # print('Checking if {} is less than {}'.format(path_final_move[3], min_moves))
            # if (path_final_move[3] < min_moves):
                # path_all_final_moves = path_moves.copy()
                # print(path_all_final_moves)
            # elif (path_final_move[3] == min_moves):
                # path_all_final_moves = path_all_final_moves.union(path_moves)
                # print(path_all_final_moves)
            
            min_moves = path_final_move[3]
            print('New min moves: {}'.format(min_moves))
        
        return ([], min_moves, path_all_final_moves)

    # check if can change direction
    if (x, y) in crossroads[i]:
        # print('Path {} crossing crossroad at ({}, {}) for a second time - DEAD END'.format(i, x, y))
        return ([], min_moves, path_all_final_moves)
        
    # check if can continue anywhere but where it came from, within memory space
        
    # A - check if can go right
    if x < size - 1 and prev_x != x + 1 and maze[y][x + 1] == '.':
        next_moves.append((path_i[i_i], x + 1, y, val + 1, (x, y)))
        i_i += 1

    # B - check if can go down
    if y < size - 1 and prev_y != y + 1 and maze[y + 1][x] == '.':
        next_moves.append((path_i[i_i], x, y + 1, val + 1, (x, y)))
        i_i += 1

    # D - check if can go up
    if y > 0 and prev_y != y - 1 and maze[y - 1][x] == '.':
        next_moves.append((path_i[i_i], x, y - 1, val + 1, (x, y)))
        i_i += 1
        
    # C - check if can go left
    if x > 0 and prev_x != x - 1 and maze[y][x - 1] == '.':
        next_moves.append((path_i[i_i], x - 1, y, val + 1, (x, y)))
        i_i += 1
        
    # print('Number of different paths from {}: {}'.format(move, i_i + 1))
    
    # if len(next_moves) == 3:
    #     print('3 moves found at ({}, {})'.format(x, y))
    #     maze[y][x] = 'W'
        # return ([], -200, path_all_final_moves)
        
    if len(next_moves) > 3:
        print('More than 3 moves (impossible!) found at ({}, {})'.format(x, y))
        exit()
        
    if len(next_moves) > 0:
        
        if len(next_moves) > 1:
            # print('Found a CROSSROAD at ({}, {}) with {} next moves'.format(x, y, len(next_moves)))
            crossroads[i].add((x, y))
            
            for next_m in range(1, len(next_moves)):
                crossroads[path_i[next_m]] = crossroads[i].copy()
    # else:
    #     print('Path {} reached a DEAD END at {} {}, dir: {}'.format(i, x, y, direction))
        
    return (next_moves, min_moves, path_all_final_moves)

          
if __name__ == "__main__":
    # size = 7
    # bytes_to_read = 12
    
    size = 71
    # bytes_to_read = 2048
    
    for bytes_to_read in range(2914, 3400):
        in_file_stream = open("in.txt", "r")
        
        result = solve_1(in_file_stream, size, bytes_to_read, return_on_first=True)
        if result:
            print('Still can reach the exit after byte: {}'.format(bytes_to_read))
        else:
            print('Cannot reach the exit after byte: {}'.format(bytes_to_read))
            break
