import sys
from pathlib import Path

path = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.append(str(path).replace('\\', '/'))

from solutions.common import HelperMethods as hm
import regex as re
from collections import Counter
import math


def solve_1(secret_num):
    # print('Solving!')
    generations = 2000
    # generations = 10
    
    for _ in range(generations):
        # print('Generation: ', i)
        secret_num = get_next_secret_number(secret_num)
        # print('Secret number: ', secret_num)
                
    print(secret_num)
    # print('End!\n')
    
    return secret_num


def get_next_secret_number(secret_num):
    first_multiplier = 64
    divider = 32
    second_multiplier = 2048
    mod_num = 16777216

    new_secret_num = secret_num * first_multiplier
    secret_num = new_secret_num ^ secret_num
    secret_num = secret_num % mod_num

    new_secret_num = secret_num // divider
    secret_num = new_secret_num ^ secret_num
    secret_num = secret_num % mod_num

    new_secret_num = secret_num * second_multiplier
    secret_num = new_secret_num ^ secret_num
    secret_num = secret_num % mod_num

    return secret_num

if __name__ == "__main__":
    secret_nums_sum = 0
    in_file_stream = open("in.txt", "r")
    
    while True:
        line = in_file_stream.readline()
        if not line:
            break
        
        init_secret_number = int(line)
    
        secret_nums_sum += solve_1(init_secret_number)
    
    print('Secret numbers sum: ', secret_nums_sum)
