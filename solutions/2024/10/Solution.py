import sys

import HelperMethods as hm
import regex as re
import collections
import math

class Solution:

    def solve(self, in_file_stream, out=sys.stdout):
        print('Solving!')

        total = 0
        
        trail_map = hm.readIntsMatrix(in_file_stream, separator='', display=False)
        
        for i in range(len(trail_map)):
            for j in range(len(trail_map[i])):
                if trail_map[i][j] == 0:
                    # print('Found trail start at ' + str(i) + ', ' + str(j))
                    trail_ends = self.get_trail_ends(trail_map, i, j, 0)
                    print('Trail score: ' + str(len(trail_ends)))
                    total += len(trail_ends)
        
        print('Total: ' + str(total))

        hm.write_line(out, total)
        

    def get_trail_ends(self, trail_map, i, j, val):
        # trail_ends = set()
        trail_ends = []
        
        next_val = val + 1
        
        if i > 0 and trail_map[i - 1][j] == next_val:
            if next_val == 9:
                print('Found a trail end at ' + str(i - 1) + ', ' + str(j))
                # trail_ends.add((i - 1, j))
                trail_ends += [(i - 1, j)]
            else:
                # print('Found ' + str(next_val) + ' at ' + str(i - 1) + ', ' + str(j))
                tends = self.get_trail_ends(trail_map, i - 1, j, next_val)
                # trail_ends.update(tends)
                if tends:
                    trail_ends.extend(tends)
        if j > 0 and trail_map[i][j - 1] == next_val:
            if next_val == 9:
                print('Found a trail end at ' + str(i) + ', ' + str(j - 1))
                # trail_ends.add((i, j - 1))
                trail_ends += [(i, j - 1)]
            else:
                # print('Found ' + str(next_val) + ' at ' + str(i) + ', ' + str(j - 1))
                tends = self.get_trail_ends(trail_map, i, j - 1, next_val)
                # trail_ends.update(tends)
                if tends:
                    trail_ends.extend(tends)
        if i < len(trail_map) - 1 and trail_map[i + 1][j] == next_val:
            if next_val == 9:
                print('Found a trail end at ' + str(i + 1) + ', ' + str(j))
                # trail_ends.add((i + 1, j))
                trail_ends += [(i + 1, j)]
            else:
                # print('Found ' + str(next_val) + ' at ' + str(i + 1) + ', ' + str(j))
                tends = self.get_trail_ends(trail_map, i + 1, j, next_val)
                # trail_ends.update(tends)
                if tends:
                    trail_ends.extend(tends)
        if j < len(trail_map[i]) - 1 and trail_map[i][j + 1] == next_val:
            if next_val == 9:
                print('Found a trail end at ' + str(i) + ', ' + str(j + 1))
                # trail_ends.add((i, j + 1))
                trail_ends += [(i, j + 1)]
            else:
                # print('Found ' + str(next_val) + ' at ' + str(i) + ', ' + str(j + 1))
                tends = self.get_trail_ends(trail_map, i, j + 1, next_val)
                # trail_ends.update(tends)
                if tends:
                    trail_ends.extend(tends)
            
        # print(trail_ends)
        
        return trail_ends
            
#########################################
# Solution().solve(sys.stdin, sys.stdout)