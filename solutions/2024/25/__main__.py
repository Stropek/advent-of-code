import sys
from pathlib import Path

path = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.append(str(path).replace('\\', '/'))

from solutions.common import HelperMethods as hm
import regex as re
from collections import Counter
import math


def solve_1(locks, keys):
    print('Solving!\n')
    
    total = len(locks) * len(keys)
    it = 0
    
    total_matching = 0
    
    for lock in locks:
        for key in keys:
            
            key_lock = [sum(kl) for kl in zip(key, lock)]
            
            # print('KEY + LOCK = KEY_LOCK: {} + {} = {}'.format(key, lock, key_lock))
            
            if it % 1000 == 0:
                print('Checked {}/{} key-lock combinations'.format(it, total))
            
            it += 1
            
            if any(kl > 5 for kl in key_lock):
                # print('Key Lock too high!')
                continue
            
            total_matching += 1
            
    print('Total matching key-lock combinations: ', total_matching)
        
    print('End!\n')


if __name__ == "__main__":
    
    locks_set = set()
    keys_set = set()
    
    in_file_stream = open("in.txt", "r")
    
    schematics = hm.readStrMatrix(in_file_stream)
    
    while schematics:
        
        # hm.display_matrix(schematics)
        
        pin_heights = [0, 0, 0, 0, 0]
        
        for i in range(len(schematics[0])):
            
            for j in range(1, len(schematics) - 1):
                if schematics[j][i] == '#':
                    pin_heights[i] += 1
                    
        if schematics[0][0] == '#':
            locks_set.add(tuple(pin_heights))
            # print('LOCK: ', pin_heights)
        else:
            keys_set.add(tuple(pin_heights))
            # print('KEY: ', pin_heights)
            
        # print('')
        
        schematics = hm.readStrMatrix(in_file_stream)
    
    solve_1(locks_set, keys_set)
