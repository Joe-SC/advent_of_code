"""https://adventofcode.com/2025/day5/"""
from dotenv import load_dotenv
load_dotenv()
import sys 
sys.path.append('../..') # Parent of parent
from aoc.utils import fetch_input_data
test_input = """\
3-5
10-14
16-20
12-18

1
5
8
11
17
32\
"""

def parse_range_str(ranges_str:str) -> list[tuple]:
    ranges = []
    for line in ranges_str.splitlines():
        range = line.split('-')
        ranges.append(
            # (lower, upper)
            (int(range[0]), int(range[1]))
        )
    return ranges

def parse_input(input_str:str)->tuple[list[tuple[int,int]], list[int]]:
    ranges_str, available_str = input_str.split('\n\n')
    ranges = parse_range_str(ranges_str)
    available = [int(id_str) for id_str in available_str.splitlines()]
    return ranges, available

def is_fresh(id: int, fresh_ranges: list[tuple[int,int]])->bool:
    for fresh_range in fresh_ranges:
        l, u = fresh_range[0], fresh_range[1]
        if id >= l and id <= u:
            return True
    return False

def solve_part1(input_str:str)->int:
    fresh_ranges, available_ids = parse_input(input_str)
    fresh_counter = 0
    for id in available_ids:
        if is_fresh(id, fresh_ranges):
            fresh_counter += 1
    return fresh_counter

def solve_part2(input_str: str) -> int:
    fresh_ranges, _ = parse_input(input_str)
    
    # sort by start value
    fresh_ranges.sort(key=lambda x: x[0])
    
    merged_ranges = []
    
    for current_start, current_end in fresh_ranges:
        if not merged_ranges:
            merged_ranges.append((current_start, current_end))
            continue
        
        last_start, last_end = merged_ranges[-1]
        
        # If the current range overlaps with the previous one....
        if current_start <= last_end + 1:
            # ... merge them by taking the larger of the two end points
            new_end = max(last_end, current_end)
            merged_ranges[-1] = (last_start, new_end)
        else:
            merged_ranges.append((current_start, current_end))
            
    total_count = 0
    for l, u in merged_ranges:
        total_count += (u - l + 1)
        
    return total_count

if __name__ == "__main__":
    puzzle_input = fetch_input_data(2025,5)
    assert solve_part1(test_input) == 3
    part1_solution = solve_part1(puzzle_input)
    print(f'Part 1: {part1_solution}')

    assert solve_part2(test_input) == 14
    part2_solution = solve_part2(puzzle_input)
    print(f'Part 2: {part2_solution}')