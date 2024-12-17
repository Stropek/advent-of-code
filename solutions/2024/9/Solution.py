import sys

import common.HelperMethods as hm
import regex as re
import collections
import math

class Solution:

    def solve(self, in_file_stream, out=sys.stdout):
        print('Solving!')

        total = 0

        files = []
        free_space = []

        file_i = 0

        line = in_file_stream.read().strip("\n")
        # line = "2333133121414131402"

        # print(line)
        file_length = 0

        for i in range(0, len(line)):
            length = int(line[i])
            if i % 2 == 0:
                file_length += length
                files.append(length * [file_i])
                file_i += 1
            else:
                free_space.append(length * ['.'])

        # for file in files:
        #     if len(file) == 0:
        #         print(file)
        # for fs in free_space:
        #     if len(fs) == 0:
        #         print(fs)

        file_i = len(files) - 1
        file = files[file_i]

        part_i = len(file) - 1

        # print(files)
        # print(free_space)

        # # for i in range(len(free_space)):
        # #     for j in range(len(free_space[i])):
        # #         free_space[i][j] = part

        # #         print('Part: ' + str(part_i) + ' ' + str(part))

        # #         part_i -= 1

        # #         if part_i < 0:
        # #             file_i -= 1

        # #             if file_i < 0:
        # #                 print('No more files left!')
        # #                 done = True
        # #                 break

        # #             print('File: ' + str(file_i) + ' ' + str(file))

        # #             file = files[file_i]

        # #             part_i = len(file) - 1
        # #             part = file[part_i]


        # #         if done:
        # #             break

        for i in reversed(range(len(files))):
            file_len = len(files[i])
            # print(file_len)
            
            for j in range(len(free_space)):
                empty_spaces = free_space[j].count('.')
                # print('Empty spaces: ' + str(empty_spaces))
                
                if j >= i:
                    break
                
                if empty_spaces >= file_len and '.' in free_space[j]:
                    
                    # print(free_space[j])
                    first_empty = free_space[j].index('.')
                    
                    it_f = 0
                    for k in range(first_empty, first_empty + empty_spaces):
                        
                        if i == 22:
                            print('Replacing ' + str(files[i][it_f]))
                            print('At position: ' + str(i) + ' ' + str(it_f))
                            print('With .')
                            print('From free-space: ' + str(free_space[j][k]))
                            print('At position: ' + str(j) + ' ' + str(k))
                        
                        free_space[j][k] = i
                        # print(free_space[j][k])
                        
                        files[i][it_f] = '.'
                        
                        it_f += 1
                        file_len -= 1

                        if file_len <= 0:
                            break
                    
                    break

        # print(files)
        # print(free_space)

        print('RESULT:')
        result = ''

        disk_space = []

        for i in range(len(files)):
            disk_space += files[i]
            result += ''.join(map(str, files[i]))
            if i < len(free_space) - 1:
                disk_space += free_space[i]
                result += ''.join(map(str, free_space[i]))

            # print(disk_space)
        
        
        j = 0
        for i in range(len(files)):
        # for i in range(220):
            file = files[i]
            for el in file:
                if el != '.':
                    print('Total: ' + str(total) + ' + ' + str(el) + ' * ' + str(j) + ' (' + str(int(el) * j) + ')')
                    total += int(el) * j
                
                j += 1
            
            if i < len(free_space) - 1:
                free = free_space[i]
                for el in free:
                    if el != '.':
                        print('Total: ' + str(total) + ' + ' + str(el) + ' * ' + str(j) + ' (' + str(int(el) * j) + ')')
                        total += int(el) * j
                
                    j += 1

        print('Total: ' + str(total))

        hm.write_line(out, total)
#########################################
# Solution().solve(sys.stdin, sys.stdout)