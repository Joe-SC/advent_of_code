"""https://adventofcode.com/2025/day3/"""
from dotenv import load_dotenv
load_dotenv()
import sys 
sys.path.append('../..') # Parent of parent
from aoc.utils import fetch_input_data
from itertools import combinations

test_input="""\
987654321111111
811111111111119
234234234234278
818181911112111"""

def find_largest_combination(line_str:str, length: int)->int:
    return max([
        int(''.join(c)) 
        for c in combinations(line_str, length)
    ])

def solve_part1(input_str: str)->int:
    voltages = []
    for line in input_str.splitlines():
        voltages.append(
            find_largest_combination(line, length=2)
        )
    return sum(voltages)

def better_largest_combination(line_str:str, length: int)->int:
    result = []
    current_pos = 0 

    for i in range(length):
        digits_needed_after = length - (i + 1)
        
        end_of_window = len(line_str) - digits_needed_after
        window = line_str[current_pos : end_of_window]
        window_max_str = max(window) # String digits should compare correctly ('9' > '1')
        
        relative_idx = window.find(window_max_str)
        # We add current_pos because find() returns index relative to the slice
        real_idx = current_pos + relative_idx

        result.append(window_max_str)
        current_pos = real_idx + 1

    final_number = "".join(result)
    return int(final_number)


def solve_part2(input_str: str)->int:
    voltages = []
    for line in input_str.splitlines():
        voltages.append(
            better_largest_combination(line, length=12)
        )
    return sum(voltages)

if __name__ == "__main__":
    day3_input = fetch_input_data(2025,3)
    assert solve_part1(test_input) == 357
    part1_solution = solve_part1(day3_input)
    print(f'Part 1: {part1_solution}')

    assert solve_part2(test_input) == 3121910778619
    part2_solution = solve_part2(day3_input)
    print(f'Part 2: {part2_solution}')