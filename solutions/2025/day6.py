"""https://adventofcode.com/2025/day6/"""
from dotenv import load_dotenv
load_dotenv()
import sys 
sys.path.append('../..') # Parent of parent
from aoc.utils import fetch_input_data

from math import prod # cheating?

test_input = """\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""

def solve_part1(input_str:str)->int:
    lines = input_str.splitlines()
    operations = lines[-1].split()
    rows = [list(line.split()) for line in lines[:-1]]
    columns = list(zip(*rows))
    assert len(columns) == len(operations)
    grand_total = 0
    for i, col in enumerate(columns):
        grand_total += eval(operations[i].join(col))
    return grand_total

def solve_part2(input_str:str)->int:
    lines = input_str.splitlines()
    char_lines = [list(line) for line in lines]
    # operations = lines[-1].split()
    char_columns = list(zip(*char_lines))
    char_columns_rev = char_columns[::-1]

    running_total = 0
    curr_list = []
    for col in char_columns_rev:
        col_str = ''.join(col)
        if len(col_str.strip()) == 0:
            continue
        if col_str.endswith('+'):
            curr_list.append(int(col_str[:-1]))
            running_total += sum(curr_list)
            curr_list = []
        elif col_str.endswith('*'):
            curr_list.append(int(col_str[:-1]))
            running_total += prod(curr_list)
            curr_list = []
        else:
            curr_list.append(int(col_str))
    return running_total

if __name__ == "__main__":
    puzzle_input = fetch_input_data(2025,6)
    assert solve_part1(test_input) == 4277556
    part1_solution = solve_part1(puzzle_input)
    print(f'Part 1: {part1_solution}')

    assert solve_part2(test_input) == 3263827
    part2_solution = solve_part2(puzzle_input)
    print(f'Part 2: {part2_solution}')