import sys

import HelperMethods as hm
import regex as re
from collections import Counter
import math

class Solution:

    def solve(self, in_file_stream, out=sys.stdout):
        print('Solving!\n')
        total = 0
        
        (x, y) = (0, 0)
        
        dir_i = 0
        directions = ['N', 'E', 'S', 'W']
        current_direction = directions[dir_i]
        
        blocks = hm.readValsList(str, in_file_stream, separator=', ')
        
        already_visited = False
        visited = set((x, y))
        
        for b in blocks:
            
            print('Current location: ', x, y)
            
            b_dir = b[0]
            b_dist = int(b[1:])
            
            if b_dir == 'R':
                dir_i = (dir_i + 1) % 4
            else:
                dir_i = (dir_i - 1) % 4
            
            current_direction = directions[dir_i]
            print('Moving {} steps in {} direction: '.format(b_dist, current_direction))

            for _ in range(b_dist):
            
                if current_direction == 'N':
                    y += 1
                elif current_direction == 'S':
                    y -= 1
                elif current_direction == 'E':
                    x += 1
                elif current_direction == 'W':
                    x -= 1
                
                if ((x, y) in visited):
                    print('Already visited: ', x, y)
                    already_visited = True
                    break
                
                visited.add((x, y))
            
            if already_visited:
                break
            
        print('FINAL location: ', x, y)
        
        total = abs(x) + abs(y)
        
        print('Distance: ', total)
        
        hm.write_line(out, total)
        
#########################################
# Solution().solve(sys.stdin, sys.stdout)