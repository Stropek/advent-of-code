import sys

import HelperMethods as hm
import regex as re
from collections import Counter
import math

class Solution:

    def solve(self, in_file_stream, out=sys.stdout):
        print('Solving!\n')
        total = 0
        
        warehouse = []
        
        line = in_file_stream.readline().strip('\n')
        
        while line != '':
            
            warehouse += [list(line)]
            
            line = in_file_stream.readline().strip('\n')
        
        # hm.display_matrix(warehouse)
        
        moves = in_file_stream.read().strip('\n')
        
        print('Number of moves: ' + str(len(moves)))
        print(moves)
        
        r_x = -1
        r_y = -1
        inner_walls = set()
        boxes = set()
        
        for i in range(len(warehouse)):
            line = warehouse[i]
            new_line = ''
            
            for c in line:
                if c == '#':
                    new_line += '##'
                elif c == 'O':
                    new_line += '[]'
                elif c == '.':
                    new_line += '..'
                else:
                    new_line += '@.'
                    
            warehouse[i] = list(new_line)
        
        for y in range(1, len(warehouse) - 1):
            for x in range(1, len(warehouse[y]) - 1):
                
                if warehouse[y][x] == '@':
                    r_x = x
                    r_y = y
                elif warehouse[y][x] == '#':
                    # print(f'#: {x}, {y}')
                    inner_walls.add((x, y))
                elif warehouse[y][x] == '[':
                    # print(f'O: {x}, {y}')
                    boxes.add((x, y))
             
        total = 0
    
        warehouse_height = len(warehouse)
        warehouse_width = len(warehouse[0])
        
        move_no = 0
        
        for move in moves:
            
            # print(sorted(boxes))
            # hm.display_matrix(warehouse)
            move_no += 1            
            print('Move {}: {}'.format(move_no, move))
            
            if move == '<':
                if r_x == 2:
                    print('reached left wall')
                    continue
                if warehouse[r_y][r_x - 1] == '#':
                    print('reached inner wall')
                    continue
                if warehouse[r_y][r_x - 1] == '.':
                    print('moving robot LEFT')
                    warehouse[r_y][r_x - 1] = '@'
                    warehouse[r_y][r_x] = '.'
                    r_x = r_x - 1
                    continue
                
                if (r_x - 2, r_y) in boxes:
                    if r_x == 2:
                        print('box at the left wall')
                        continue
                    
                    e_x = r_x - 3
                    while e_x > 1:
                        if (e_x, r_y) in inner_walls:
                            print('boxes at the inner wall')
                            break
                        if warehouse[r_y][e_x] == '.':
                            print('Moving robot and boxes LEFT')
                            
                            warehouse[r_y][r_x] = '.'
                            warehouse[r_y][r_x - 1] = '@'
                            
                            new_b_x = r_x - 3
                            while new_b_x >= e_x:

                                warehouse[r_y][new_b_x] = '['
                                warehouse[r_y][new_b_x + 1] = ']'
                                
                                boxes.remove((new_b_x + 1, r_y))
                                boxes.add((new_b_x, r_y))
                                
                                new_b_x -= 2
                            
                            r_x -= 1
                            break
                        e_x -= 1
                        
            elif move == '>':
                if r_x == warehouse_width - 3:
                    print('reached right wall')
                    continue
                if warehouse[r_y][r_x + 1] == '#':
                    print('reached inner wall')
                    continue
                if warehouse[r_y][r_x + 1] == '.':
                    print('moving robot RIGHT')
                    warehouse[r_y][r_x + 1] = '@'
                    warehouse[r_y][r_x] = '.'
                    r_x = r_x + 1
                    continue
                
                if (r_x + 1, r_y) in boxes:
                    if r_x == warehouse_width - 4:
                        print('box at the right wall')
                        continue
                    
                    e_x = r_x + 3
                    while e_x <= warehouse_width - 3:
                        if (e_x, r_y) in inner_walls:
                            print('boxes at the inner wall')
                            break
                        if warehouse[r_y][e_x] == '.':
                            print('Moving robot and boxes RIGHT')
                            
                            warehouse[r_y][r_x] = '.'
                            warehouse[r_y][r_x + 1] = '@'
                            
                            new_b_x = r_x + 2
                            while new_b_x <= e_x:

                                warehouse[r_y][new_b_x] = '['
                                warehouse[r_y][new_b_x + 1] = ']'
                                
                                boxes.remove((new_b_x - 1, r_y))
                                boxes.add((new_b_x, r_y))
                                
                                new_b_x += 2
                            
                            r_x += 1
                            break
                        e_x += 1
                        
            elif move == '^':
                if r_y == 1:
                    print('reached top wall')
                    continue
                if warehouse[r_y - 1][r_x] == '#':
                    print('reached inner wall')
                    continue
                if warehouse[r_y - 1][r_x] == '.':
                    print('moving robot UP')
                    warehouse[r_y - 1][r_x] = '@'
                    warehouse[r_y][r_x] = '.'
                    r_y = r_y - 1
                    continue
                
                bs_to_move = set()
                bs_above = set()
                bs_above.add((r_x, r_y - 1))
                
                while bs_above:
                    b_above = bs_above.pop()
                    
                    b_above_x = b_above[0]
                    b_above_y = b_above[1]
                    b_above_c = warehouse[b_above_y][b_above_x]
                
                    print('Checking box {} above: {}, {}'.format(b_above_c, b_above_x, b_above_y))
                    
                    if b_above_c == '#':
                        print('Reached inner wall at top at {}, {}'.format(b_above_x, b_above_y))
                        bs_to_move = set()
                        break
                    if b_above_c == '[':
                        bs_to_move.add((b_above_x, b_above_y))
                        bs_to_move.add((b_above_x + 1, b_above_y))
                        
                        bs_above.add((b_above_x, b_above_y - 1))
                        bs_above.add((b_above_x + 1, b_above_y - 1))
                    elif b_above_c == ']':
                        bs_to_move.add((b_above_x, b_above_y))
                        bs_to_move.add((b_above_x - 1, b_above_y))
                        
                        bs_above.add((b_above_x, b_above_y - 1))
                        bs_above.add((b_above_x - 1, b_above_y - 1))
                    elif b_above_c == '.':
                        continue
                    else:
                        print('Unknown character {} above: {}, {}'.format(b_above_c, b_above_x, b_above_y))
                        bs_to_move = set()
                        break
                
                print('Boxes to move UP: {}'.format(bs_to_move))
                
                if bs_to_move:
                    bs_to_move = sorted(bs_to_move, key=lambda x: x[1])
                    
                    for b in bs_to_move:
                        b_to_move_x = b[0]
                        b_to_move_y = b[1]
                        
                        b_to_move_c = warehouse[b_to_move_y][b_to_move_x]
                        
                        print('Moving box {} up: {}, {}'.format(b_to_move_c, b_to_move_x, b_to_move_y))
                        
                        warehouse[b_to_move_y][b_to_move_x] = '.'
                        warehouse[b_to_move_y - 1][b_to_move_x] = b_to_move_c
                        
                        if (b_to_move_x, b_to_move_y) in boxes:
                            boxes.remove((b_to_move_x, b_to_move_y))
                            boxes.add((b_to_move_x, b_to_move_y - 1))
                        
                    warehouse[r_y][r_x] = '.'
                    r_y -= 1
                    warehouse[r_y][r_x] = '@'
                
            elif move == 'v':
                if r_y == warehouse_height - 2:
                    print('reached bottom wall')
                    continue
                if warehouse[r_y + 1][r_x] == '#':
                    print('reached inner wall')
                    continue
                if warehouse[r_y + 1][r_x] == '.':
                    print('moving robot DOWN')
                    warehouse[r_y + 1][r_x] = '@'
                    warehouse[r_y][r_x] = '.'
                    r_y = r_y + 1
                    continue
                
                bs_to_move = set()
                bs_below = set()
                bs_below.add((r_x, r_y + 1))
                
                while bs_below:
                    b_below = bs_below.pop()
                    
                    b_below_x = b_below[0]
                    b_below_y = b_below[1]
                    b_below_c = warehouse[b_below_y][b_below_x]
                    
                    print('Checking box {} below: {}, {}'.format(b_below_c, b_below_x, b_below_y))
                
                    if b_below_c == '#':
                        print('Reached inner wall at bottom at {}, {}'.format(b_below_x, b_below_y))
                        bs_to_move = set()
                        break
                    if b_below_c == '[':
                        bs_to_move.add((b_below_x, b_below_y))
                        bs_to_move.add((b_below_x + 1, b_below_y))
                        
                        bs_below.add((b_below_x, b_below_y + 1))
                        bs_below.add((b_below_x + 1, b_below_y + 1))
                    elif b_below_c == ']':
                        bs_to_move.add((b_below_x, b_below_y))
                        bs_to_move.add((b_below_x - 1, b_below_y))
                        
                        bs_below.add((b_below_x, b_below_y + 1))
                        bs_below.add((b_below_x - 1, b_below_y + 1))
                    elif b_below_c == '.':
                        continue
                    else:
                        print('Unknown character {} below: {}, {}'.format(b_below_c, b_below_x, b_below_y))
                        bs_to_move = set()
                        break
                
                print('Boxes to move DOWN: {}'.format(bs_to_move))
                
                if bs_to_move:
                    bs_to_move = reversed(sorted(bs_to_move, key=lambda x: x[1]))
                    
                    for b in bs_to_move:
                        b_to_move_x = b[0]
                        b_to_move_y = b[1]
                        
                        b_to_move_c = warehouse[b_to_move_y][b_to_move_x]
                        
                        print('Moving box {} down: {}, {}'.format(b_to_move_c, b_to_move_x, b_to_move_y))
                        
                        warehouse[b_to_move_y][b_to_move_x] = '.'
                        warehouse[b_to_move_y + 1][b_to_move_x] = b_to_move_c
                        
                        if (b_to_move_x, b_to_move_y) in boxes:
                            boxes.remove((b_to_move_x, b_to_move_y))
                            boxes.add((b_to_move_x, b_to_move_y + 1))
                        
                    warehouse[r_y][r_x] = '.'
                    r_y += 1                    
                    warehouse[r_y][r_x] = '@'
                
                bs_below.add((r_x, r_y + 1))
                
            else:
                print('ILLEGAL MOVE - SKIPPING')
                continue
        
        # self.move_small_boxes(warehouse, moves, r_x, r_y, inner_walls, boxes)
        
        for j in range(len(warehouse)):
            for i in range(len(warehouse[j])):
                if warehouse[j][i] in ('O', '['):
                    print('Box at: ' + str(i) + ', ' + str(j))
                    total += 100*j
                    total += i
                    print('Total distance so far: ' + str(total))
        
        print('Total distance: ' + str(total))
        
        hm.write_line(out, total)
        
    def move_small_boxes(self, warehouse, moves, r_x, r_y, inner_walls, boxes):
    
        for y in range(1, len(warehouse) - 1):
            for x in range(1, len(warehouse[y]) - 1):
                
                if warehouse[y][x] == '@':
                    r_x = x
                    r_y = y
                elif warehouse[y][x] == '#':
                    # print(f'#: {x}, {y}')
                    inner_walls.add((x, y))
                elif warehouse[y][x] == 'O':
                    # print(f'O: {x}, {y}')
                    boxes.add((x, y))
             
        total = 0
    
        warehouse_height = len(warehouse)
        warehouse_width = len(warehouse[0])
        
        for move in moves:
            hm.display_matrix(warehouse)
            
            print('Trying to move: ' + move)
            if move == '<':
                if r_x == 1:
                    print('reached left wall')
                    continue
                if warehouse[r_y][r_x - 1] == '#':
                    print('reached inner wall')
                    continue
                if warehouse[r_y][r_x - 1] == '.':
                    print('moving robot LEFT')
                    warehouse[r_y][r_x - 1] = '@'
                    warehouse[r_y][r_x] = '.'
                    r_x = r_x - 1
                    continue
                if (r_x - 1, r_y) in boxes:
                    if r_x == 2:
                        print('box at the left wall')
                        continue
                    
                    e_x = r_x - 2
                    while e_x > 0:
                        if (e_x, r_y) in inner_walls:
                            print('boxes at the inner wall')
                            break
                        if warehouse[r_y][e_x] == '.':
                            print('Moving robot and boxes LEFT')
                            
                            warehouse[r_y][r_x] = '.'
                            warehouse[r_y][r_x - 1] = '@'
                            warehouse[r_y][e_x] = 'O'
                            
                            boxes.remove((r_x - 1, r_y))
                            boxes.add((e_x, r_y))
                            
                            r_x -= 1
                            break
                        e_x -= 1
            elif move == '>':
                if r_x == warehouse_width - 2:
                    print('reached right wall')
                    continue
                if warehouse[r_y][r_x + 1] == '#':
                    print('reached inner wall')
                    continue
                if warehouse[r_y][r_x + 1] == '.':
                    print('moving robot RIGHT')
                    warehouse[r_y][r_x + 1] = '@'
                    warehouse[r_y][r_x] = '.'
                    r_x = r_x + 1
                    continue
                if (r_x + 1, r_y) in boxes:
                    if r_x == warehouse_width - 3:
                        print('box at the right wall')
                        continue
                    
                    e_x = r_x + 2
                    while e_x < warehouse_width - 1:
                        if (e_x, r_y) in inner_walls:
                            print('boxes at the inner wall')
                            break
                        if warehouse[r_y][e_x] == '.':
                            print('Moving robot and boxes RIGHT')
                            
                            warehouse[r_y][r_x] = '.'
                            warehouse[r_y][r_x + 1] = '@'
                            warehouse[r_y][e_x] = 'O'
                            
                            boxes.remove((r_x + 1, r_y))
                            boxes.add((e_x, r_y))
                            
                            r_x += 1
                            break
                        e_x += 1
            elif move == '^':
                if r_y == 1:
                    print('reached top wall')
                    continue
                if warehouse[r_y - 1][r_x] == '#':
                    print('reached inner wall')
                    continue
                if warehouse[r_y - 1][r_x] == '.':
                    print('moving robot UP')
                    warehouse[r_y - 1][r_x] = '@'
                    warehouse[r_y][r_x] = '.'
                    r_y = r_y - 1
                    continue
                if (r_x, r_y - 1) in boxes:
                    if r_y == 2:
                        print('box at the top wall')
                        continue
                    
                    e_y = r_y - 2
                    while e_y > 0:
                        if (r_x, e_y) in inner_walls:
                            print('boxes at the inner wall')
                            break
                        if warehouse[e_y][r_x] == '.':
                            print('Moving robot and boxes UP')
                            
                            warehouse[r_y][r_x] = '.'
                            warehouse[r_y - 1][r_x] = '@'
                            warehouse[e_y][r_x] = 'O'
                            
                            boxes.remove((r_x, r_y - 1))
                            boxes.add((r_x, e_y))
                            
                            r_y -= 1
                            break
                        e_y -= 1
            elif move == 'v':
                if r_y == warehouse_height - 2:
                    print('reached bottom wall')
                    continue
                if warehouse[r_y + 1][r_x] == '#':
                    print('reached inner wall')
                    continue
                if warehouse[r_y + 1][r_x] == '.':
                    print('moving robot DOWN')
                    warehouse[r_y + 1][r_x] = '@'
                    warehouse[r_y][r_x] = '.'
                    r_y = r_y + 1
                    continue
                if (r_x, r_y + 1) in boxes:
                    if r_y == warehouse_height - 3:
                        print('box at the bottom wall')
                        continue
                    
                    e_y = r_y + 2
                    while e_y < warehouse_height - 1:
                        if (r_x, e_y) in inner_walls:
                            print('boxes at the inner wall')
                            break
                        if warehouse[e_y][r_x] == '.':
                            print('Moving robot and boxes DOWN')
                            
                            warehouse[r_y][r_x] = '.'
                            warehouse[r_y + 1][r_x] = '@'
                            warehouse[e_y][r_x] = 'O'
                            
                            boxes.remove((r_x, r_y + 1))
                            boxes.add((r_x, e_y))
                            
                            r_y += 1
                            break
                        e_y += 1
            else:
                print('ILLEGAL MOVE - SKIPPING')
                continue
        
#########################################
# Solution().solve(sys.stdin, sys.stdout)