import sys
from pathlib import Path

path = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.append(str(path).replace('\\', '/'))

from solutions.common import HelperMethods as hm
import regex as re
from collections import Counter
import math


def solve_1(inputs_dict, gates_set):
    print('Solving!\n')
    binary_num = ''
    
    to_calculate = gates_set.copy()
    
    while len(to_calculate) > 0:
        print(f'Calculating {len(to_calculate)} gates...')
        
        to_calculate_curr = to_calculate.copy()
        
        for gate in to_calculate_curr:
            (in_left, in_right, gate_t, gate_out) = gate
            
            if in_left not in inputs_dict or in_right not in inputs_dict:
                # print('Either {} or {} not in inputs_dict'.format(in_left, in_right))
                continue
            
            in_left = inputs_dict[in_left]
            in_right = inputs_dict[in_right]
                
            # print('Calculating {} for {}'.format(gate_t, gate_out))
            if gate_t == 'AND':
                inputs_dict[gate_out] = in_left & in_right
            elif gate_t == 'OR':
                inputs_dict[gate_out] = in_left | in_right
            elif gate_t == 'XOR':
                inputs_dict[gate_out] = in_left ^ in_right
            else:
                print('Unknown gate type!')
                exit()
                
            to_calculate.remove(gate)
            
    for input_key in sorted(inputs):
        print(f'{input_key}: {inputs[input_key]}')
        if input_key.startswith('z'):
            binary_num = str(inputs[input_key]) + binary_num
    
    print(f'Binary number: {binary_num}')

    total = 0
    for i in range(1, len(binary_num) + 1):
        print('binary_num: ', binary_num[-i])
        total += int(binary_num[-i]) * (2 ** (i - 1))

    print('Total: ', total)
    print('End!\n')
           
if __name__ == "__main__":
    
    in_file_stream = open("in.txt", "r")
    
    inputs = dict()
    gates = set()
    
    while True:
        line = in_file_stream.readline().strip('\n')
        if line == '':
            break
        
        input_name = line.split(':')[0]
        input_value = int(line.split(':')[1].strip())
        
        inputs[input_name] = input_value
        
    while True:
        line = in_file_stream.readline().strip('\n')
        if line == '':
            break
        
        gate_str = line.split('->')[0]
        output = line.split('->')[1].strip()

        (input_left, gate_type, input_right) = gate_str.strip().split(' ')
        
        gates.add((input_left, input_right, gate_type, output))
    
    solve_1(inputs, gates)
