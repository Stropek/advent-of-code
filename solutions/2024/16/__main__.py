import sys
from pathlib import Path

path = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.append(str(path).replace('\\', '/'))

from solutions.common import HelperMethods as hm
import regex as re
from collections import Counter
import math


def solve(in_file_stream, out=sys.stdout):
    print('Solving!\n')
    total = 0
    min_moves = -1
        
    maze = hm.readStrMatrix(in_file_stream)
        
    start_x = 1
    start_y = len(maze) - 2
        
    # start_x = 3
    # start_y = 11
        
    start_path = (0, start_x, start_y, 'E', 0)
    crossroads = dict()
        
    crossroads[0] = set((start_x, start_y))
    crossroads[-1] = dict()
    crossroads[-1][(start_x, start_y, 'E')] = 1000000
        
    print('Start: {} {}, dir: {}'.format(start_path[0], start_path[1], start_path[2]))
        
    hm.display_matrix(maze)

    # if maze[start_y - 1][start_x] == '.':
    #     paths[(start_x, start_y, 'N')] = [(start_x - 1, start_y, 'N', 1000)]
    # if maze[start_y][start_x + 1] == '.':
    #     paths[(start_x, start_y, 'E')] = [(start_x, start_y - 1, 'E', 1)]
        
    (next_moves, min_moves) = find_next(start_path, crossroads, maze, min_moves)
        
    print('-: {}'.format(next_moves))
        
    while next_moves:
            
        it = 0
        max_it = 100
            
        # print('Found next moves: {}'.format(next_moves))
            
        # for next_move in next_moves:
        while next_moves:
                
            next_move = next_moves.pop()
                
            # print('Path {}: {} {}, dir: {}'.format(next_move[0], next_move[1], next_move[2], next_move[3]))
            (next_for_path, min_moves) = find_next(next_move, crossroads, maze, min_moves)
            # print('-: {}'.format(next_for_path))
            
            if len(next_for_path) == 0:
                # print('Path {} reached a DEAD END at {} {}, dir: {}'.format(next_move[0], next_move[1], next_move[2], next_move[3]))
                continue
                
            for nfp in next_for_path:
                        
                if nfp[4] > min_moves and min_moves > 0:
                    print('Path {} is longer than min_moves {} and it has {}'.format(nfp[0], min_moves, nfp[4]))
                    continue
                        
                # print('Path {} is not longer than min_moves {}'.format(next_move[3], min_moves))
                        
                next_moves += [nfp]
                            
            # if it > max_it:
            #     break
                
            it += 1
            
        break
            
    print('Total iterations: {}'.format(it))
        
    print('Total: ' + str(min_moves))
        
    hm.write_line(out, min_moves)
        
def find_next(move, crossroads, maze, min_moves):
    # print('Finding next for path: {}'.format(move))
        
    i = move[0]
    x = move[1]
    y = move[2]
    direction = move[3]
    val = move[4]
    next_moves = []
    path_final_move = None
    
    if (x, y, direction) not in crossroads[-1]:
        crossroads[-1][(x, y, direction)] = val
    else:
        if crossroads[-1][(x, y, direction)] < val:
            print('Path {} already crossed ({}, {}) with a lower value {}'.format(i, x, y, crossroads[-1][(x, y, direction)]))
            return ([], min_moves)
        else:
            crossroads[-1][(x, y, direction)] = val
        
    # print('Looking for next at ({}, {}), facing {}, with val {}'.format(x, y, direction, val))
        
    i_i = 0
    path_i = [i, len(crossroads), len(crossroads) + 1]
    
    # print('New paths: {}'.format(path_i))
            
    # check if E in current direction
    if direction == 'E' and maze[y][x + 1] == 'E':
        path_final_move = (i, x + 1, y, 'E', val + 1)
    elif direction == 'W' and maze[y][x - 1] == 'E':
        path_final_move = (i, x - 1, y, 'W', val + 1)
    elif direction == 'N' and maze[y - 1][x] == 'E':
        path_final_move = (i, x, y - 1, 'N', val + 1)
    elif direction == 'S' and maze[y + 1][x] == 'E':
        path_final_move = (i, x, y + 1, 'S', val + 1)
            
    if path_final_move:
        print('Path {} reached the finish line at {}'.format(i, path_final_move))
            
        if min_moves == -1:
            min_moves = path_final_move[4]
        else:
            # print('Checking if {} is less than {}'.format(path_final_move[4], min_moves))
            min_moves = min(min_moves, path_final_move[4])
        
        return ([], min_moves)

    # check if can change direction
    if (x, y) in crossroads[i]:
        # print('Path {} crossing crossroad at ({}, {}) for a second time - DEAD END'.format(i, x, y))
        return ([], min_moves)
       
    if direction in ('E', 'W'):
        if maze[y - 1][x] == '.':
            next_moves.append((path_i[i_i], x, y - 1, 'N', val + 1001))
            i_i += 1
        if maze[y + 1][x] == '.':
            next_moves.append((path_i[i_i], x, y + 1, 'S', val + 1001))
            i_i += 1
            
    elif direction in ('N', 'S'):
        if maze[y][x - 1] == '.':
            next_moves.append((path_i[i_i], x - 1, y, 'W', val + 1001))
            i_i += 1
        if maze[y][x + 1] == '.':
            next_moves.append((path_i[i_i], x + 1, y, 'E', val + 1001))
            i_i += 1
        
    # check if can continue in current direction
    if direction == 'E' and maze[y][x + 1] == '.':
        next_moves.append((path_i[i_i], x + 1, y, 'E', val + 1))
    elif direction == 'W' and maze[y][x - 1] == '.':
        next_moves.append((path_i[i_i], x - 1, y, 'W', val + 1))
    elif direction == 'N' and maze[y - 1][x] == '.':
        next_moves.append((path_i[i_i], x, y - 1, 'N', val + 1))
    elif direction == 'S' and maze[y + 1][x] == '.':
        next_moves.append((path_i[i_i], x, y + 1, 'S', val + 1))
        
    # print('Number of different paths from {}: {}'.format(move, i_i + 1))
        
    if len(next_moves) > 3:
        print('More than 3 moves (impossible!) found at ({}, {})'.format(x, y))
        
    if len(next_moves) > 0:
        if len(next_moves) > 1:
            # print('Found a CROSSROAD at ({}, {}) with {} next moves'.format(x, y, len(next_moves)))
            crossroads[i].add((x, y))
            
            for next_m in range(1, len(next_moves)):
                crossroads[path_i[next_m]] = crossroads[i].copy()
    # else:
    #     print('Path {} reached a DEAD END at {} {}, dir: {}'.format(i, x, y, direction))
        
    return (next_moves, min_moves)
        
if __name__ == "__main__":
    
    in_file_stream = open("in.txt", "r")
    solve(in_file_stream)
