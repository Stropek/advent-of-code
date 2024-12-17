import sys

import HelperMethods as hm
import regex as re
from decimal import Decimal
from collections import Counter
import math

class Solution:

    def solve(self, in_file_stream, out=sys.stdout):
        print('Solving!\n')
        
        total = 0
        cnt = 0
        
        while True:
            line = in_file_stream.readline().strip('\n')
            if not line:
                break
            
            button_a = list(map(int, line.replace('Button A: ', '').replace('X+', '').replace('Y+', '').replace(',', '').split(' ')))

            line = in_file_stream.readline().strip('\n')
            
            button_b = list(map(int, line.replace('Button B: ', '').replace('X+', '').replace('Y+', '').replace(',', '').split(' ')))
            
            line = in_file_stream.readline().strip('\n')
            prize = list(map(int, line.replace('Prize: ', '').replace('X=', '').replace('Y=', '').replace(',', '').split(' ')))
            
            line = in_file_stream.readline().strip('\n')
            
            # total_a = 0
            # total_b = 0
            
            x = prize[0] + 10000000000000
            y = prize[1] + 10000000000000
                
            a_x = button_a[0]
            a_y = button_a[1]
                
            b_x = button_b[0]
            b_y = button_b[1]
            
            # print('a_x: {}'.format(a_x))
            # print('a_y: {}'.format(a_y))
            
            # print('b_x: {}'.format(b_x))
            # print('b_y: {}'.format(b_y))
            
            # print('x: {}'.format(x))
            # print('y: {}'.format(y))
            
            # print(button_a)
            # print(button_b)
            # print(prize)
            
            # a_x=94
            # a_y=34
            # b_x=22
            # b_y=67
            
            # x=8400
            # y=5400
            
            # Button A: X+94, Y+34
            # Button B: X+22, Y+67
            # Prize: X=8400, Y=5400
            
            min_prize_1 = -1
            min_prize_2 = -1
            
            a = (a_y * x - a_x * y) / (a_x * b_y - b_x * a_y)
            b_1 = (x - b_x * a) / a_x
            b_2 = (y - b_y * a) / a_y
            print('A: {}'.format(a))
            print('B_1: {}'.format(b_1))
            print('B_2: {}'.format(b_2))
            
            if b_1 == b_2 and b_1.is_integer() and a.is_integer():
                min_prize_1 = 3*int(a) + int(b_1  )
            
            b = (a_x * y - a_y * x) / (a_x * b_y - b_x * a_y)
            a_1 = (x - b_x * b) / a_x
            a_2 = (y - b_y * b) / a_y
            print('B: {}'.format(b))
            print('A_1: {}'.format(a_1))
            print('A_2: {}'.format(a_2))
            
            if a_1 == a_2 and a_1.is_integer() and b.is_integer():
                min_prize_2 = 3*int(a_1) + int(b)
            
            if min_prize_1 == -1 and min_prize_2 == -1:
                print('No solution\n')
                continue
            
            if min_prize_1 == -1:
                total += min_prize_2
            elif min_prize_2 == -1:
                total += min_prize_1
            else:
                total += min(min_prize_1, min_prize_2)
            
            print('Total: {}\n'.format(total))
            
            # while True:
                
            #     a_x_rest = x % a_x
            #     a_y_rest = y % a_y

            #     a_x_n = int(x / a_x)
            #     a_y_n = int(y / a_y)
                
            #     b_x_rest = x % b_x
            #     b_y_rest = y % b_y
                
            #     b_x_n = int(x / b_x)
            #     b_y_n = int(y / b_y)
                
            #     if b_y_rest == 0 and b_x_rest == 0 and b_x_n == b_y_n:
                    
            #         total_b = b_x_n
            #         print('Total B: ' + str(total_b))
                    
            #         if min_prize == -1:
            #             min_prize = (total_a) * 3 + (total_b)
            #         else:
            #             min_prize = min(min_prize, (total_a) * 3 + (total_b))
                        
            #         # print('X Y: ' + str(x) + ' ' + str(y))

            #         print('MIN PRIZE: ' + str(min_prize))
                    
            #         break
                    
            #     else:
            #         x = x - a_x
            #         y = y - a_y
                    
            #         if x < 0 or y < 0:
            #             print('Done')
            #             break
                    
            #         total_a += 1
            #         # print('Total A: ' + str(total_a))
                    

            #     # print('X Y: ' + str(x) + ' ' + str(y))
            
            # total_a = 0
            # total_b = 0
            
            # x = prize[0]
            # y = prize[1]
            
            # print(button_a)
            # print(button_b)
            # print(prize)
            
            # min_prize = -1
            
            # while True:
                
            #     a_x_rest = x % a_x
            #     a_y_rest = y % a_y

            #     a_x_n = int(x / a_x)
            #     a_y_n = int(y / a_y)
                
            #     b_x_rest = x % b_x
            #     b_y_rest = y % b_y
                
            #     b_x_n = int(x / b_x)
            #     b_y_n = int(y / b_y)

            #     if a_y_rest == 0 and a_x_rest == 0 and a_x_n == a_y_n:
                    
            #         total_a = a_x_n
            #         print('Total A: ' + str(total_a))
                    
            #         if min_prize == -1:
            #             min_prize = (total_a) * 3 + (total_b)
            #         else:
            #             min_prize = min(min_prize, (total_a) * 3 + (total_b))
                        
            #         # print('X Y: ' + str(x) + ' ' + str(y))

            #         print('MIN PRIZE: ' + str(min_prize))
                    
            #         break
                    
            #     # elif b_y_rest == 0 and b_x_rest == 0 and b_x_n == b_y_n:
                    
            #     #     if min_prize == -1:
            #     #         min_prize = (total_a + b_x_n) * 3 + (total_b + b_x_n)
            #     #     else:
            #     #         min_prize = min(min_prize, (total_a + b_x_n) * 3 + (total_b + b_x_n))
                        
            #     #     print('X Y: ' + str(x) + ' ' + str(y))

            #     #     print('MIN PRIZE: ' + str(min_prize))
                    
            #     #     x = x - b_x
            #     #     y = y - b_y
                    
            #     #     if x < 0 or y < 0:
            #     #         print('Done')
            #     #         break
                    
            #     #     total_a += 1
                    
            #     else:
            #         x = x - b_x
            #         y = y - b_y
                    
            #         if x < 0 or y < 0:
            #             print('Done')
            #             break
                    
            #         total_b += 1
            #         # print('Total B: ' + str(total_b))

            #     # print('X Y: ' + str(x) + ' ' + str(y))
            
            # print('Price: {}'.format(min_prize))
        
            cnt += 1
            
        print('\nTotal: {}'.format(total))
        
        hm.write_line(out, total)
        
#########################################
# Solution().solve(sys.stdin, sys.stdout)