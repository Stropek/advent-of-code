import sys

import HelperMethods as hm
import regex as re
import collections
import math

class Solution:

    def solve(self, in_file_stream, out=sys.stdout):
        print('Solving!')

        total = 0
        
        dimensions = sorted(hm.readIntsList(in_file_stream, 'x'))
        
        while len(dimensions) == 3:
            x = dimensions[0]
            y = dimensions[1]
            z = dimensions[2]
            
            # present_paper = 2*((x*y) + (y*z) + (z*x)) + min([x*y, y*z, z*x])
            # total += present_paper
            present_ribbon = 2*(x + y) + (x*y*z)
            total += present_ribbon
            
            print('Dimensions: ' + str(dimensions))
            # print('Present paper: ' + str(present_paper))
            print('Present ribbon: ' + str(present_ribbon))
            dimensions = sorted(hm.readIntsList(in_file_stream, 'x'))
            
        print('Total: ' + str(total))

        hm.write_line(out, total)
#########################################
# Solution().solve(sys.stdin, sys.stdout)