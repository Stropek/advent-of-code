import sys

import HelperMethods as hm
import regex as re
from collections import Counter
import math

class Solution:

    def solve(self, in_file_stream, out=sys.stdout):
        print('Solving!\n')
        total = 0
        
        input_area = hm.readStrMatrix(in_file_stream, display=True)
        
        used_area = set()
        
        i = 0
        total_rows = len(input_area)
        total_cols = len(input_area[0])
        
        print(total_rows)
        print(total_cols)
        
        iteration = 0
        while len(used_area) < total_rows * total_cols:
            
            print('\nIteration {0}'.format(iteration))
            
            iteration += 1
            if iteration > 10000:
                break
            
            i = 0
        
            for line in input_area:
                # print('\nLINE: ' + line)
                j = 0
                
                for _ in line:
                    
                    # print('POINT: ({0},{1}) {2}'.format(i, j, l))
                    
                    if (j, i) in used_area:
                        j += 1
                        continue
                    
                    if i >= total_rows or j >= total_cols:
                        i = 0
                        j = 0
                        break
                    
                    plant = input_area[i][j]
                    print('\nLooking for plants {0}, starting at (x:{1}, y:{2})'.format(plant, j, i))
                    
                    # plant_start_i = i
                    # plant_start_j = j
                    
                    plant_size = 1
                    plant_area = set()
                    plant_fence = set()
                    plant_fence_by_dir = dict()
                    
                    used_area.add((j, i))
                    # print('Used area: {0} {1}'.format(j, i))
                    to_check = []
                    
                    to_check = self.get_to_check(total_rows, total_cols, j, i, used_area)
                    print('Total to check: {0}'.format(to_check))

                    plant_fence.add(('N', j, i))
                    plant_fence.add(('E', j, i))
                    plant_fence.add(('S', j, i))
                    plant_fence.add(('W', j, i))
                    
                    # fence_sides = 4
                    # (prev_x, prev_y) = (i, j)
                    
                    while to_check:
                        (x, y) = to_check.pop(0)
                        # print(input_area[y][x] + ' (' + str(x) + ',' + str(y) + ')')
                        
                        if input_area[y][x] == plant and (x, y) not in used_area:
                            # print('Found plant {0} at ({1},{2})'.format(plant, x, y))
                            
                            # if prev_x == x:
                            #     print('Same X')
                            #     if (prev_x, prev_y, 'E') not in plant_fence:
                            #         fence_sides += 2
                            #     if (prev_x, prev_y, 'W') not in plant_fence:
                            #         fence_sides += 2
                            # elif prev_y == y:
                            #     print('Same Y')
                            #     if (prev_x, prev_y, 'N') not in plant_fence:
                            #         fence_sides += 2
                            #     if (prev_x, prev_y, 'S') not in plant_fence:
                            #         fence_sides += 2
                            
                            # print('Fence sides for plant {0} at ({1},{2}) is {3}'.format(plant, x, y, fence_sides))
                            # if there's both east and west above, add 0 to fence sides
                            # or if there's both east and south on the left, add 0 to fence sides
                            
                            if ('E', x - 1, y) in plant_fence:
                                plant_fence.remove(('E', x - 1, y))
                            else:
                                plant_fence.add(('W', x, y))
                                
                            if ('W', x + 1, y) in plant_fence:
                                plant_fence.remove(('W', x + 1, y))
                            else:
                                plant_fence.add(('E', x, y))
                                
                            if ('N', x, y + 1) in plant_fence:
                                plant_fence.remove(('N', x, y + 1))
                            else:
                                plant_fence.add(('S', x, y))
                                
                            if ('S', x, y - 1) in plant_fence:
                                plant_fence.remove(('S', x, y - 1))
                            else:
                                plant_fence.add(('N', x, y))

                            # print('Fence for plant {0} at ({1},{2}) is:\n{3}'.format(plant, x, y, plant_fence))
                            # print('Fence lengths: ' + str(len(plant_fence)))

                            print('Used area: {0} {1}'.format(x, y))
                            used_area.add((x, y))
                            to_check += self.get_to_check(total_rows, total_cols, x, y, used_area)
                        
                            # print('Total to check: {0}'.format(to_check))
                            
                            plant_size += 1
                            plant_area.add((x, y))
                            
                            # plant_min_i = min(plant_min_i, x)
                            # plant_max_i = max(plant_max_i, x)
                            # plant_min_j = min(plant_min_j, y)
                            # plant_max_j = max(plant_max_j, y)
                            
                        # print(plant_size)
                        # print('Plant area: {0}'.format(plant_area))
                        # print(to_check)
                        
                    # print('Plant {0} has area {1} and bounds ({2},{3}) to ({4},{5})'.format(plant, plant_size, plant_min_i, plant_min_j, plant_max_i, plant_max_j))
                        
                    plant_fence_by_dir['N'] = dict()
                    plant_fence_by_dir['E'] = dict()
                    plant_fence_by_dir['S'] = dict()
                    plant_fence_by_dir['W'] = dict()
                    
                    # print(sorted(used_area))
                    # print(plant_fence)
                    
                    for direction, x, y in plant_fence:
                        
                        # print('Plant {0} at ({1},{2}) has fence at ({3},{4}) in direction {5}'.format(plant, x, y, x, y, direction))
                        
                        if direction in ('N', 'S'):
                            if y not in plant_fence_by_dir[direction]:
                                plant_fence_by_dir[direction][y] = {x}
                            else:
                                plant_fence_by_dir[direction][y].add(x)
                        else:
                            if x not in plant_fence_by_dir[direction]:
                                plant_fence_by_dir[direction][x] = {y}
                            else:
                                plant_fence_by_dir[direction][x].add(y)
                
                    total_fence_sides = 0
                
                    for direction in ('N', 'E', 'S', 'W'):
                        for k, v in plant_fence_by_dir[direction].items():
                            plant_fence_by_dir[direction][k] = sorted(list(v))
                            
                        print('Sorted for {}: {}'.format(direction, str(plant_fence_by_dir[direction])))
                            
                        dir_fence_sides = 0
                        for k, v in plant_fence_by_dir[direction].items():
                            
                            fence_sides = 1
                            
                            for i in range(0, len(plant_fence_by_dir[direction][k]) - 1):
                                coord = plant_fence_by_dir[direction][k][i]
                                
                                if plant_fence_by_dir[direction][k][i + 1] != coord + 1:
                                    fence_sides += 1
                                    
                            print('Fence sides for plant {0} in direction {1} at {2} is {3}'.format(plant, direction, k, fence_sides))
                            dir_fence_sides += fence_sides
                            
                        # print('Fence sides for plant {0} in direction {1} is {2}'.format(plant, direction, dir_fence_sides))
                        total_fence_sides += dir_fence_sides
                        
                    # print('Total fence sides for plant {0} is {1}'.format(plant, total_fence_sides))
                    
                    plant_fence_price = self.get_fence_price(plant, plant_size, total_fence_sides)
                    total += plant_fence_price

                i += 1
                if i >= len(input_area):
                    continue
            
        print('Total price is {0}'.format(total))
        
        print('Total used area: {0}'.format(len(used_area)))
        
        # newest: 834788 - too low
        # newest: 834828 - ?
        
        hm.write_line(out, total)
        
    def get_fence_price(self, plant, plant_size, fence_size):
        price = 0
        
        # print('Size for plant {0} is {1}'.format(plant, plant_size))
        # print('Fence for plant {0} is {1}'.format(plant, fence_size))
        
        price = plant_size * fence_size
        # print('Price for plant {0} is {1}'.format(plant, price))
                
        return price

    def get_to_check(self, total_rows, total_cols, x, y, used_area):
        to_check = []
        
        if x < total_cols - 1 and (x + 1, y) not in used_area:
            to_check += [(x + 1, y)]
        if x > 0 and (x - 1, y) not in used_area:
            to_check += [(x - 1, y)]
        if y < total_rows - 1 and (x, y + 1) not in used_area:
            to_check += [(x, y + 1)]
        if y > 0 and (x, y - 1) not in used_area:
            to_check += [(x, y - 1)]
            
        # print('Next to check: ' + str(to_check))
            
        return to_check

#########################################
# Solution().solve(sys.stdin, sys.stdout)