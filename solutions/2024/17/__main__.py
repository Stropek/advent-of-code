import sys
from pathlib import Path

path = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.append(str(path).replace('\\', '/'))

from solutions.common import HelperMethods as hm
import regex as re
from collections import Counter
import math


def solve_1(in_file_stream, out=sys.stdout):
    print('Solving!\n')
    total = 0
        
    limit = 1000
    cnt = 0
        
    reg_a_s = int(in_file_stream.readline().strip("\n").replace('Register A: ', ''))
    reg_b_s = int(in_file_stream.readline().strip("\n").replace('Register B: ', ''))
    reg_c_s = int(in_file_stream.readline().strip("\n").replace('Register C: ', ''))
        
    reg_a_init = 0
        
    in_file_stream.readline()
        
    program = list(map(int, in_file_stream.readline().strip("\n").replace('Program: ', '').split(',')))
        
    # print(len(program))
        
    op_index = 0
    sim_found = 0
        
    print('A: ' + str(reg_a_s))
    print('B: ' + str(reg_b_s))
    print('C: ' + str(reg_c_s))
    print(','.join(map(str, program)))
    
    reg_a = reg_a_s
    reg_b = reg_b_s
    reg_c = reg_c_s
            
    result = []
    op_index = 0
        
    while op_index < len(program):
        instruction = program[op_index]

        operand = program[op_index + 1] if instruction in (1, 3) else get_combo_operand(program, op_index + 1, reg_a, reg_b, reg_c)
                    
        # adv
        if instruction == 0:
            reg_a = reg_a // 2 ** operand
        # bxl
        elif instruction == 1:
            reg_b = reg_b ^ operand
        # bst
        elif instruction == 2:
            reg_b = operand % 8
        # jnz
        elif instruction == 3:
            if reg_a != 0:
                    op_index = operand - 2
        # bxc
        elif instruction == 4:
                reg_b = reg_b ^ reg_c
        # out
        elif instruction == 5:
            out_v = operand % 8
            result += [out_v]
        # bdv
        elif instruction == 6:
            reg_b = reg_a // 2 ** operand
        # cdv
        elif instruction == 7:
            reg_c = reg_a // 2 ** operand
        else:
            print('Invalid instruction: {}'.format(instruction))
            break
                
        op_index += 2
        
        print('Result after instruction {}: {}'.format(instruction, ','.join(map(str, result))))
            
    print('Result: ' + ','.join(map(str, result)))
        
    hm.write_line(out, total)


def solve_2(in_file_stream, out=sys.stdout):
    print('Solving!\n')
    total = 0
        
    limit = 1000
    cnt = 0
        
    reg_a_s = int(in_file_stream.readline().strip("\n").replace('Register A: ', ''))
    reg_b_s = int(in_file_stream.readline().strip("\n").replace('Register B: ', ''))
    reg_c_s = int(in_file_stream.readline().strip("\n").replace('Register C: ', ''))
        
    reg_a_init = 0
        
    in_file_stream.readline()
        
    program = list(map(int, in_file_stream.readline().strip("\n").replace('Program: ', '').split(',')))
        
    # print(len(program))
        
    op_index = 0
    sim_found = 0
    
    # first with 6 same digits and 16 overall: 70368747168992        
    # diffs
    current_max = 109685330781408
    # 4194304           - 10968533078140    8
    # 3234498           - higher than 109685330781408
    # 1221945           - higher than 109685330781408
    # 262139            - higher than 109685330781408
    # 173369            - higher than 109685330781408
    # 88770             - 
    # 5                 - disregard
    
    
    same_digits = 6
    
    step_i = 0
    
    reg_a_s = 0
    reg_a_s = 0
    steps = [1]
    # steps = [-1]
    # reg_a_s = 70368747168992
    steps = [4194304, 4194304, 4194304, 4194304, 4194304, 1221945, 5, 262139, 5, 262139, 5, 262139, 5, 262139, 5, 262139, 5, 262139, 5, 262139, 5, 262139, 5, 262139, 5, 262139, 5, 262139, 5, 88770, 173369, 5, 262139, 5, 262139, 5, 262139, 5, 3234498, 4194304]
    # steps = [-4194304, -4194304, -4194304, -4194304, -4194304, -3234498, - 5, -262139, -5, -262139, -5, -262139, -5, -173369, -88770, -5, -262139, -5, -262139, -5, -262139, -5, -262139, -5, -262139, -5, -262139, -5, -262139, -5, -262139, -5, -262139, -5, -262139, -5, -262139, -5, -1221945, -4194304]
    
    # reg_a_s = 70377790088416
    # steps = [33554432, 1073741824, 16072572928]
    
    current_step = steps[step_i]
    
    print('A: ' + str(reg_a_s))
    print('B: ' + str(reg_b_s))
    print('C: ' + str(reg_c_s))
    
    print('\n')
        
    print(','.join(map(str, program)))
    
    print(len(steps))
    
    print('Current max: {}'.format(current_max))
    print('Current step: {}'.format(current_step))
    
    reg_a_s = 0
    reg_a_s = 70368747168992
    # reg_a_s = 35184372088831
        
    while True:
            
        reg_a = reg_a_s
        reg_b = reg_b_s
        reg_c = reg_c_s
            
        result = []
        op_index = 0
        
        while op_index < len(program):
            instruction = program[op_index]

            operand = program[op_index + 1] if instruction in (1, 3) else get_combo_operand(program, op_index + 1, reg_a, reg_b, reg_c)
                    
            # adv
            if instruction == 0:
                reg_a = reg_a // 2 ** operand
            # bxl
            elif instruction == 1:
                reg_b = reg_b ^ operand
            # bst
            elif instruction == 2:
                reg_b = operand % 8
            # jnz
            elif instruction == 3:
                if reg_a != 0:
                    op_index = operand - 2
            # bxc
            elif instruction == 4:
                reg_b = reg_b ^ reg_c
            # out
            elif instruction == 5:
                out_v = operand % 8
                result += [out_v]
            # bdv
            elif instruction == 6:
                reg_b = reg_a // 2 ** operand
            # cdv
            elif instruction == 7:
                reg_c = reg_a // 2 ** operand
            else:
                print('Invalid instruction: {}'.format(instruction))
                break
                
            op_index += 2
        
        if (len(result) < len(program)):
            # print('Same length with {} for initial registry A {}'.format(len(result), reg_a_s)) # 28016463839232
            print(reg_a_s, len(result), result)
            reg_a_s *= 2
            
        # if cnt > 10:
        #     break
                    
        # if reg_a_s % 1000000 == 0:
        #     print(reg_a_s, result)
        
        # print(result)
        # print(result[:same_digits])
        # print(result[-same_digits:])
        
        if result[:same_digits] == [2, 4, 1, 7, 7, 5] and result[-same_digits:] == [5, 5, 0, 3, 3, 0]:
            print(reg_a_s, result, reg_a_s - reg_a_init)
            
            reg_a_init = reg_a_s
            
            # if sim_found == 20:
            #     break
            
            # sim_found += 1

        # if reg_a_s > current_max:
        #     print('Got to reg_as_s {}, which is higher than currently known max'.format(reg_a_s))
        #     break
        
        # 2,4,1,7,7,5,4,1,1,4,5,5,0,3,3,0
        if str(result) == str(program):
            print('Same result for initial registry A {}'.format(reg_a_s))
            print(reg_a_s, result, reg_a_s - reg_a_init)
            print(reg_a_s)
            break
            
        reg_a_s += current_step
        step_i += 1
        current_step = steps[step_i % len(steps)]
        # print('Current step: ', current_step)
        
        # print('Result: ' + ','.join(map(str, result)))
            
        # if cnt > limit:
        #     print('Limit reached')
        #     break
            
        cnt += 1
            
        # print('Trying registry A {}'.format(reg_a_s))
        
    print('Result: ' + ','.join(map(str, result)))
        
    hm.write_line(out, total)


def get_combo_operand(program, index, reg_a, reg_b, reg_c):
    operand = program[index]
        
    if operand == 4:
        return reg_a
    if operand == 5:
        return reg_b
    if operand == 6:
        return reg_c
    if operand == 7:
        print('Invalid combo operand: {}'.format(operand))
    else:
        return operand


if __name__ == "__main__":
    
    in_file_stream = open("in.txt", "r")
    
    # solve_1(in_file_stream)
    solve_2(in_file_stream)
