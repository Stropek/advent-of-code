import sys

import HelperMethods as hm
import regex as re
from collections import Counter
import math

class Solution:

    def solve(self, in_file_stream, out=sys.stdout):
        print('Solving!\n')

        blinks = 75
        # blinks = 25

        numbers = [64554, 35, 906, 6, 6960985, 5755, 975820, 0]
        # numbers = [125, 17]
        # numbers = [0]

        print('Initial arrangement: {}'.format(numbers))

        total_cnt = Counter(numbers)
        
        print('Counter: {}'.format(total_cnt))
        
        for b in range(blinks):
            print('Blink {}'.format(b + 1))
            
            blink_cnt = Counter()
            
            for stone in total_cnt:
                if stone == 0:
                    blink_cnt[1] += total_cnt[stone]
                elif len(str(stone)) % 2 == 0:
                    left = int(str(stone)[:len(str(stone))//2])
                    right = int(str(stone)[len(str(stone))//2:])
                    
                    blink_cnt[left] += total_cnt[stone]
                    blink_cnt[right] += total_cnt[stone]
                else:
                    blink_cnt[2024*stone] += total_cnt[stone]
                
                # print('Stone: {}'.format(stone))
                
            total_cnt = blink_cnt
            # print('Blink Counter: {}'.format(total_cnt))
            print('Total Counter: {}'.format(sum(total_cnt.values())))
                
        print('Total Counter: {}'.format(sum(total_cnt.values())))
        
        hm.write_line(out, len(numbers))

    def blink(self, numbers):
        
        new_numbers = []

        return new_numbers

#########################################
# Solution().solve(sys.stdin, sys.stdout)