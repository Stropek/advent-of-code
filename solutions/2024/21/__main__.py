import sys
from pathlib import Path

path = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.append(str(path).replace('\\', '/'))

from solutions.common import HelperMethods as hm
import regex as re
from collections import Counter
import math


def solve_1(num_code):
    min_button_presses = 100000000000
    # dir_robot_keypads = 2
    
    prev_robot_codes = find_dir_codes_from_num_pad(num_code)
    print('First robot codes:', prev_robot_codes)

    # for _ in range(dir_robot_keypads + 1):
    #         robot_codes = set()
            
    #         for prc in prev_robot_codes:
    #             rc = find_dir_codes_from_dir_pad(prc)
                
    #             robot_codes.update(rc)
                    
    #     min_button_presses = len(list(robot_codes)[0])
    
    second_robot_codes = set()
    for frc in prev_robot_codes:
        src = find_dir_codes_from_dir_pad(frc)
        
        print('{} second robot codes with len: {}'.format(len(src), len(src[0])))
        
        # for src_code in src:
        #     print('Second robot code (len: {}): {}'.format(len(src_code), src_code))
        
        second_robot_codes.update(src)
        
    print('Total second robot codes options: ', len(second_robot_codes))

    third_robot_codes = set()
    for src in second_robot_codes:
        trc = find_dir_codes_from_dir_pad(src)
        
        # print('{} third robot codes with len: {}'.format(len(trc), len(trc[0])))
        
        min_button_presses = min(min_button_presses, len(trc[0]))
        
        third_robot_codes.update(trc)
    
    print('Total third robot codes options: ', len(third_robot_codes))
    print('Min button presses: ', min_button_presses)
    
    return min_button_presses

def find_dir_codes_from_dir_pad(dir_code):
    
    print('Finding dir codes from dir pad: ', dir_code)
    
    possible_steps = init_possible_dir_steps()
    
    # print(possible_steps)
    
    dir_kp = [
        [None, '^', 'A'],
        ['<', 'v', '>']
    ]
    
    curr_path = ''
    curr_code = ''
    dir_kp_sp = (2, 0, 0, curr_code, curr_path)
    
    next_robot_paths = []
    next_paths = find_next_paths(dir_kp_sp, dir_kp, dir_code, next_robot_paths, possible_steps)
    # print('First PATHS:', next_paths)
    
    while next_paths:
        
        next_pos = next_paths.pop()
        
        new_paths = find_next_paths(next_pos, dir_kp, dir_code, next_robot_paths, possible_steps)
        # print(new_paths)
        
        if new_paths:
            
            for np in new_paths:
                found_nums = np[3]
                
                # print('found: {}, looking for: {}'.format(found_nums, dir_code))
                if found_nums == dir_code:
                    num_path = np[4]
                    # print('Found code {} with path {}'.format(dir_code, num_path))
                    
                    if not next_robot_paths or len(num_path) < len(next_robot_paths[0]):
                        next_robot_paths = [num_path]
                    else:
                        next_robot_paths += [num_path]
                    break
                
                next_paths.add(np)
        
    return next_robot_paths

def find_dir_codes_from_num_pad(num_code):
    
    possible_steps = init_possible_num_steps()
    
    num_kp = [
        ['7', '8', '9'],
        ['4', '5', '6'],
        ['1', '2', '3'],
        [None, '0', 'A'],
    ]
    
    # print(possible_paths)
    
    curr_path = ''
    curr_code = ''
    num_kp_sp = (2, 3, 0, curr_code, curr_path)
    
    first_robot_paths = []
    next_paths = find_next_paths(num_kp_sp, num_kp, num_code, first_robot_paths, possible_steps)
    # print('First PATHS:', next_paths)
    
    while next_paths:
        
        # print('Remaining PATHS', next_paths)
        
        next_pos = next_paths.pop()
        
        # print('Current pos: ', next_pos)
        
        new_paths = find_next_paths(next_pos, num_kp, num_code, first_robot_paths, possible_steps)
        # print(new_paths)
        
        if new_paths:
            # print('Next pos: ', new_paths)
            
            for np in new_paths:
                found_nums = np[3]
                
                if found_nums == num_code:
                    num_path = np[4]
                    # print('Found code {} with path {}'.format(num_code, num_path))
                
                    if not first_robot_paths or len(num_path) < len(first_robot_paths[0]):
                        first_robot_paths = [num_path]
                    else:
                        first_robot_paths += [num_path]
                    break
                
                # print('Next pos: ', np)
                next_paths.add(np)
    
    return first_robot_paths

def init_possible_num_steps():
    ps = dict()
    
    # +---+---+---+
    # | 7 | 8 | 9 |
    # +---+---+---+
    # | 4 | 5 | 6 |
    # +---+---+---+
    # | 1 | 2 | 3 |
    # +---+---+---+
    #     | 0 | A |
    #     +---+---+
    
    step_up = (0, -1)
    step_down = (0, 1)
    step_left = (-1, 0)
    step_right = (1, 0)
    
    #region 7
    ps[('7', '1')] = [(step_down, 'v')]
    ps[('7', '2')] = [(step_down, 'v'), (step_right, '>')]
    ps[('7', '3')] = [(step_down, 'v'), (step_right, '>')]
    ps[('7', '4')] = [(step_down, 'vA')]
    ps[('7', '5')] = [(step_down, 'v'), (step_right, '>')]
    ps[('7', '6')] = [(step_down, 'v'), (step_right, '>')]
    ps[('7', '8')] = [(step_right, '>A')]
    ps[('7', '9')] = [(step_right, '>')]
    ps[('7', '0')] = [(step_down, 'v'), (step_right, '>')]
    ps[('7', 'A')] = [(step_down, 'v'), (step_right, '>')]
    #endregion
    #region 8
    ps[('8', '1')] = [(step_down, 'v'), (step_left, '<')]
    ps[('8', '2')] = [(step_down, 'v')]
    ps[('8', '3')] = [(step_down, 'v'), (step_right, '>')]
    ps[('8', '4')] = [(step_down, 'v'), (step_left, '<')]
    ps[('8', '5')] = [(step_down, 'vA')]
    ps[('8', '6')] = [(step_down, 'v'), (step_right, '>')]
    ps[('8', '7')] = [(step_left, '<A')]
    ps[('8', '9')] = [(step_right, '>A')]
    ps[('8', '0')] = [(step_down, 'v')]
    ps[('8', 'A')] = [(step_down, 'v'), (step_right, '>')]
    #endregion
    #region 9
    ps[('9', '1')] = [(step_down, 'v'), (step_left, '<')]
    ps[('9', '2')] = [(step_down, 'v'), (step_left, '<')]
    ps[('9', '3')] = [(step_down, 'v')]
    ps[('9', '4')] = [(step_down, 'v'), (step_left, '<')]
    ps[('9', '5')] = [(step_down, 'v'), (step_left, '<')]
    ps[('9', '6')] = [(step_down, 'vA')]
    ps[('9', '7')] = [(step_left, '<')]
    ps[('9', '8')] = [(step_left, '<A')]
    ps[('9', '0')] = [(step_down, 'v'), (step_left, '<')]
    ps[('9', 'A')] = [(step_down, 'v')]
    #endregion
    #region 4
    ps[('4', '1')] = [(step_down, 'vA')]
    ps[('4', '2')] = [(step_down, 'v'), (step_right, '>')]
    ps[('4', '3')] = [(step_down, 'v'), (step_right, '>')]
    ps[('4', '5')] = [(step_right, '>A')]
    ps[('4', '6')] = [(step_right, '>')]
    ps[('4', '7')] = [(step_up, '^A')]
    ps[('4', '8')] = [(step_up, '^'), (step_right, '>')]
    ps[('4', '9')] = [(step_up, '^'), (step_right, '>')]
    ps[('4', '0')] = [(step_down, 'v'), (step_right, '>')]
    ps[('4', 'A')] = [(step_down, 'v'), (step_right, '>')]
    #endregion
    #region 5
    ps[('5', '1')] = [(step_down, 'v'), (step_left, '<')]
    ps[('5', '2')] = [(step_down, 'vA')]
    ps[('5', '3')] = [(step_down, 'v'), (step_right, '>')]
    ps[('5', '4')] = [(step_left, '<A')]
    ps[('5', '6')] = [(step_right, '>A')]
    ps[('5', '7')] = [(step_up, '^'), (step_left, '<')]
    ps[('5', '8')] = [(step_up, '^A')]
    ps[('5', '9')] = [(step_up, '^'), (step_right, '>')]
    ps[('5', '0')] = [(step_down, 'v')]
    ps[('5', 'A')] = [(step_down, 'v'), (step_right, '>')]
    #endregion
    #region 6
    ps[('6', '1')] = [(step_down, 'v'), (step_left, '<')]
    ps[('6', '2')] = [(step_down, 'v'), (step_left, '<')]
    ps[('6', '3')] = [(step_down, 'vA')]
    ps[('6', '4')] = [(step_left, '<')]
    ps[('6', '5')] = [(step_left, '<A')]
    ps[('6', '7')] = [(step_up, '^'), (step_left, '<')]
    ps[('6', '8')] = [(step_up, '^'), (step_left, '<')]
    ps[('6', '9')] = [(step_up, '^A')]
    ps[('6', '0')] = [(step_down, 'v'), (step_left, '<')]
    ps[('6', 'A')] = [(step_down, 'v')]
    #endregion
    #region 1
    ps[('1', '2')] = [(step_right, '>A')]
    ps[('1', '3')] = [(step_right, '>')]
    ps[('1', '4')] = [(step_up, '^A')]
    ps[('1', '5')] = [(step_up, '^'), (step_right, '>')]
    ps[('1', '6')] = [(step_up, '^'), (step_right, '>')]
    ps[('1', '7')] = [(step_up, '^')]
    ps[('1', '8')] = [(step_up, '^'), (step_right, '>')]
    ps[('1', '9')] = [(step_up, '^'), (step_right, '>')]
    ps[('1', '0')] = [(step_right, '>')]
    ps[('1', 'A')] = [(step_right, '>')]
    #endregion
    #region 2
    ps[('2', '1')] = [(step_left, '<A')]
    ps[('2', '3')] = [(step_right, '>A')]
    ps[('2', '4')] = [(step_up, '^'), (step_left, '<')]
    ps[('2', '5')] = [(step_up, '^A')]
    ps[('2', '6')] = [(step_up, '^'), (step_right, '>')]
    ps[('2', '7')] = [(step_up, '^'), (step_left, '<')]
    ps[('2', '8')] = [(step_up, '^')]
    ps[('2', '9')] = [(step_up, '^'), (step_right, '>')]
    ps[('2', '0')] = [(step_down, 'vA')]
    ps[('2', 'A')] = [(step_down, 'v'), (step_right, '>')]
    #endregion
    #region 3
    ps[('3', '1')] = [(step_left, '<')]
    ps[('3', '2')] = [(step_left, '<A')]
    ps[('3', '4')] = [(step_up, '^'), (step_left, '<')]
    ps[('3', '5')] = [(step_up, '^'), (step_left, '<')]
    ps[('3', '6')] = [(step_up, '^A')]
    ps[('3', '7')] = [(step_up, '^'), (step_left, '<')]
    ps[('3', '8')] = [(step_up, '^'), (step_left, '<')]
    ps[('3', '9')] = [(step_up, '^')]
    ps[('3', '0')] = [(step_down, 'v'), (step_left, '<')]
    ps[('3', 'A')] = [(step_down, 'vA')]
    #endregion
    #region 0
    ps[('0', '1')] = [(step_up, '^')]
    ps[('0', '2')] = [(step_up, '^A')]
    ps[('0', '3')] = [(step_up, '^'), (step_right, '>')]
    ps[('0', '4')] = [(step_up, '^')]
    ps[('0', '5')] = [(step_up, '^')]
    ps[('0', '6')] = [(step_up, '^'), (step_right, '>')]
    ps[('0', '7')] = [(step_up, '^')]
    ps[('0', '8')] = [(step_up, '^')]
    ps[('0', '9')] = [(step_up, '^'), (step_right, '>')]
    ps[('0', 'A')] = [(step_right, '>A')]
    #endregion
    #region A
    ps[('A', '0')] = [(step_left, '<A')]
    ps[('A', '1')] = [(step_up, '^'), (step_left, '<')]
    ps[('A', '2')] = [(step_up, '^'), (step_left, '<')]
    ps[('A', '3')] = [(step_up, '^A')]
    ps[('A', '4')] = [(step_up, '^'), (step_left, '<')]
    ps[('A', '5')] = [(step_up, '^'), (step_left, '<')]
    ps[('A', '6')] = [(step_up, '^')]
    ps[('A', '7')] = [(step_up, '^'), (step_left, '<')]
    ps[('A', '8')] = [(step_up, '^'), (step_left, '<')]
    ps[('A', '9')] = [(step_up, '^')]
    #endregion

    return ps

def init_possible_dir_steps():
    ps = dict()
    
    # +---+---+---+
    # |   | ^ | A |
    # +---+---+---+
    # | < | v | > |
    # +---+---+---+
    
    step_up = (0, -1)
    step_down = (0, 1)
    step_left = (-1, 0)
    step_right = (1, 0)
    no_step = (0, 0)
    
    #region ^
    ps[('^', 'v')] = [(step_down, 'vA')]
    ps[('^', '>')] = [(step_down, 'v'), (step_right, '>')]
    ps[('^', '<')] = [(step_down, 'v')]
    ps[('^', 'A')] = [(step_right, '>A')]
    ps[('^', '^')] = [(no_step, 'A')]
    #endregion
    #region <
    ps[('<', '^')] = [(step_right, '>')]
    ps[('<', 'v')] = [(step_right, '>A')]
    ps[('<', '>')] = [(step_right, '>')]
    ps[('<', 'A')] = [(step_right, '>')]
    ps[('<', '<')] = [(no_step, 'A')]
    #endregion
    #region v
    ps[('v', '^')] = [(step_up, '^A')]
    ps[('v', '>')] = [(step_right, '>A')]
    ps[('v', '<')] = [(step_left, '<A')]
    ps[('v', 'A')] = [(step_up, '^'), (step_right, '>')]
    ps[('v', 'v')] = [(no_step, 'A')]
    #endregion
    #region >
    ps[('>', '^')] = [(step_up, '^'), (step_left, '<')]
    ps[('>', 'v')] = [(step_left, '<A')]
    ps[('>', '<')] = [(step_left, '<')]
    ps[('>', 'A')] = [(step_up, '^A')]
    ps[('>', '>')] = [(no_step, 'A')]
    #endregion
    #region A
    ps[('A', '^')] = [(step_left, '<A')]
    ps[('A', '>')] = [(step_down, 'vA')]
    ps[('A', 'v')] = [(step_down, 'v'), (step_left, '<')]
    ps[('A', '<')] = [(step_down, 'v'), (step_left, '<')]
    ps[('A', 'A')] = [(no_step, 'A')]
    #endregion

    return ps

def find_next_paths(num_kp_pos, num_kp, target_num_code, robot_paths, possible_steps):
    next_paths = set()
    
    min_path_len = len(robot_paths[0]) if robot_paths else -1
    
    curr_path_x = num_kp_pos[0]
    curr_path_y = num_kp_pos[1]
    
    curr_char = num_kp[curr_path_y][curr_path_x]
    curr_path_len = num_kp_pos[2]
    curr_path_num_code = num_kp_pos[3]
    curr_path_num_cod_len = len(curr_path_num_code)
    curr_path = num_kp_pos[4]
    
    if min_path_len != -1 and curr_path_len > min_path_len:
        print('test1')
        print('test1')
        print('test1')
        print('test1')
        return set()
    
    if curr_path_num_code == target_num_code:
        print('test2')
        print('test2')
        print('test2')
        print('test2')
        return set()
    
    # print(target_num_code)
    # print(curr_path_num_cod_len)
    next_num_code_char = target_num_code[curr_path_num_cod_len]
    
    # if curr_char == next_num_code_char:
    #     print('curr_char == next_num_code_char')
    #     print('curr_char: ', curr_char)
    #     return set()
    
    next_steps = possible_steps[(curr_char, next_num_code_char)]
    
    # print('Target num code: ', target_num_code)
    
    # if curr_char == target_num_code[curr_path_num_cod_len - 1]:
    #     print('Curr path num code: ', curr_path_num_code)
    #     curr_path_num_code += next_num_code_char
    #     print('Curr path num code: ', curr_path_num_code)
    
    for next_step in next_steps:
        next_step_x_change = next_step[0][0]
        next_step_y_change = next_step[0][1]
        next_step_char = next_step[1]
        
        next_step_x = curr_path_x + next_step_x_change
        next_step_y = curr_path_y + next_step_y_change
                
        # print('Curr char: ', curr_char)
        # print('Next NUM char: ', next_num_code_char)
        # print('Next step char: ', num_kp[next_step_y][next_step_x])
        
        if next_num_code_char == num_kp[next_step_y][next_step_x]:
            curr_path_num_code += next_num_code_char
            
        next_paths.add((next_step_x, next_step_y, len(curr_path_num_code), curr_path_num_code, curr_path + next_step_char))
        # print('adding path: ', (next_step_x, next_step_y, curr_path_len, curr_path_num_code, curr_path + next_step_char))
    
    # print('\nPossible paths for {} -> {}: {}'.format(curr_char, next_num_code_char, next_paths))
    
    return next_paths
           
if __name__ == "__main__":
    
    code_complexity = 0
    
    button_presses = 0
    in_file_stream = open("in.txt", "r")
    
    for line in in_file_stream:
        line = line.strip('\n')
        
        num_from_line = int(line[:-1])
        min_presses = solve_1(line)
        
        print('Num from line: ', num_from_line)
        print('Min presses: ', min_presses)
        
        code_complexity += (min_presses * num_from_line)
        
        print(code_complexity)
    
    print('Code complexity: ', code_complexity)
