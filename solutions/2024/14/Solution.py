import sys

import HelperMethods as hm
import regex as re
from collections import Counter
import math

class Solution:

    def solve(self, in_file_stream, out=sys.stdout):
        print('Solving!\n')
        total = 0
        
        height = 103
        width = 101
        
        # height = 7
        # width = 11
        
        space = [None] * height
        for i in range(height):
            space[i] = [' '] * width
            
        robot_vals = hm.readValsList(str, in_file_stream, separator=' ')
        robots_pos = []
        robots_vel = []
        
        seconds = 10000
        
        while len(robot_vals) > 1:
            [p_str, v_str] = robot_vals
            
            p_str = p_str.replace('p=', '')
            v_str = v_str.replace('v=', '')
            # print(p_str, v_str)
            
            p_x, p_y = map(int, p_str.split(','))
            v_x, v_y = map(int, v_str.split(','))
            
            robots_pos += [(p_x, p_y)]
            robots_vel += [(v_x, v_y)]
            
            # print(robots_pos)
            # print(robots_vel)
            
            robot_vals = hm.readValsList(str, in_file_stream, separator=' ')
            
            # p_x_step = p_x
            # p_y_step = p_y
            
            # for s in range(seconds):
            #     p_x_step = (p_x_step + v_x) % width
            #     p_y_step = (p_y_step + v_y) % height
                
                # print('{} second: {} {}'.format(s + 1, p_x_step, p_y_step))
                
            # print('Step per second:')
            # print(p_x_step, p_y_step)
            
            # p_x_all = (p_x + v_x * seconds) % width
            # p_y_all = (p_y + v_y * seconds) % height
            
            # space[p_y_all][p_x_all] += 1
            
            # print('Single step:')
            # print(p_x_all, p_y_all)
            
        for second in range(1, seconds + 1):
            
            for i in range(len(robots_pos)):
                p_x, p_y = robots_pos[i]
                v_x, v_y = robots_vel[i]
                
                p_x = (p_x + v_x) % width
                p_y = (p_y + v_y) % height
                
                space[p_y][p_x] = '#'
                
                robots_pos[i] = (p_x, p_y)
            
            print('After {} seconds'.format(second))
            for row in range(height):
                print(''.join(space[row]))
            
            print('\n')
            
            # reseting the space
            for row in range(height):
                space[row] = [' '] * width
            
            if second > seconds:
                break
            
        # print(space)
        
        # q_1 = 0
        # q_2 = 0
        # q_3 = 0
        # q_4 = 0
        
        # for row in range(height):
        #     for col in range(width):
        #         if row < height // 2 and col < width // 2:
        #             q_1 += space[row][col]
        #         elif row < height // 2 and col > width // 2:
        #             q_2 += space[row][col]
        #         elif row > height // 2 and col < width // 2:
        #             q_3 += space[row][col]
        #         elif row > height // 2 and col > width // 2:
        #             q_4 += space[row][col]
        #         # else:
        #         #     print('Not counting from row {} col {}'.format(row, col))

        # print(q_1, q_2, q_3, q_4)
        
        # total = q_1 * q_2 * q_3 * q_4
        
        hm.write_line(out, total)
        
#########################################
# Solution().solve(sys.stdin, sys.stdout)