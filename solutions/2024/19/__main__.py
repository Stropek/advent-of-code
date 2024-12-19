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
    
    patterns = hm.readValsList(str, in_file_stream, ', ')
    
    print(patterns)
    
    # skip empty line
    hm.readVal(str, in_file_stream)
    
    design = hm.readVal(str, in_file_stream)
    
    total_possible = 0
    
    while design:
        
        # print('Design: ', design)
        
        possible = False
        
        candidates = set()
        candidates.add(('', design))
        
        it = 0
        
        while candidates:
            
            it += 1
            
            candidate = candidates.pop()
            
            # print('\nCandidate: ', candidate)
            
            left_to_match = candidate[1]
            
            for pattern in patterns:
                # print('- testing pattern: ', pattern)
                
                if len(pattern) > len(left_to_match):
                    continue
                
                if left_to_match.startswith(pattern):
                    # print('-- matched: ', pattern)
                                        
                    new_ltm = left_to_match[len(pattern):]

                    if not new_ltm:
                        # print('--- POSSIBLE: ', candidate[0] + pattern)
                        print(design)
                        possible = True
                        break
                    
                    candidates.add((candidate[0] + pattern, new_ltm))
                    
                    # print('--- candidates: ', candidates)
            
            if possible:
                # print('Found a desired design after {} iterations'.format(it))
                total_possible += 1
                break
               
            if not candidates:
                # print('No more candidates for {} after {} iterations'.format(design, it))
                # print(design)
                break
        
        design = hm.readVal(str, in_file_stream)        
    
    print('Total possible: ', total_possible)
    
    print('End!\n')

def solve_2(in_file_stream, out=sys.stdout):
    print('Solving!\n')
    total = 0
    
    all_patterns = hm.readValsList(str, in_file_stream, ', ')
    
    print('.'.join(all_patterns))
    
    # check for duplicate patterns
    # print([item for item, count in Counter(all_patterns).items() if count > 1])
    
    # pattern_chars = set()
    # for p in all_patterns:
    #     pattern_chars.update(set(p))
        
    # print('Pattern chars: ', pattern_chars)
    
    # skip empty line
    hm.readVal(str, in_file_stream)
    
    design = hm.readVal(str, in_file_stream)
    
    total_possible = 0
    d_n = 0
    
    # already_matched = dict()
        
    while design:
        
        calculated_designs = dict()
        
        # design_possible = 0
        print('Design {}: {}'.format(d_n, design))
        
        patterns = []
        patterns_set = set()
        
        for p in all_patterns:
            if design.find(p) >= 0:
                patterns += [p]
                patterns_set.add(p)
                
        calculated_designs[0] = 0 if design[-1] not in patterns_set else 1
        
        # print('Calculated subdesigns: ', calculated_designs)
        
        for sub_i in range(1, len(design)):
        
            subdesign = design[-sub_i - 1:]
            # print('\nSubdesign {}: {}'.format(sub_i, subdesign))
            
            subdesigns_flags = [0] * len(subdesign)
            # print('Subdesigns flags: ', subdesigns_flags)
            
            for i in range(1, len(subdesign) + 1):
                # print(i)
                # print('Sub-subdesign: ', subdesign[:i])
                if subdesign[:i] in patterns_set:
                    # print('Found a pattern for subdesign {}: {}'.format(sub_i, subdesign[:i]))
                    subdesigns_flags[i - 1] = 1
            
            # print('Subdesigns flags: ', subdesigns_flags)
            # print('Calculated subdesigns: ', calculated_designs)
            
            subdesign_val = 0
            for i in range(len(subdesigns_flags) - 1):
                # print('{} vs {} {} Subdesign value += {} * {}'.format(i, len(subdesigns_flags) - i - 2, len(subdesigns_flags), subdesigns_flags[i], calculated_designs[len(subdesigns_flags) - i - 2]))
                subdesign_val += subdesigns_flags[i] * calculated_designs[len(subdesigns_flags) - i - 2]
                
            # print('Subdesign value += {}'.format(subdesigns_flags[-1]))
            subdesign_val += subdesigns_flags[-1]
            
            calculated_designs[sub_i] = subdesign_val                
            # print('Subdesign value: ', subdesign_val)
            # print('Calculated subdesigns: ', calculated_designs)
        
        # print('Calculated subdesigns: ', calculated_designs)
        
        total_possible += calculated_designs[len(design) - 1]
        
        design = hm.readVal(str, in_file_stream)
        d_n += 1
    
    print('\nTotal possible: ', total_possible)
    
    print('End!\n')      

if __name__ == "__main__":
    
    in_file_stream = open("in.txt", "r")
    # solve_1(in_file_stream)
    solve_2(in_file_stream)
