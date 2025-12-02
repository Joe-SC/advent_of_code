"""https://adventofcode.com/2025/day2/"""
from dotenv import load_dotenv
load_dotenv()
import sys 
sys.path.append('../..') # Parent of parent
from aoc.utils import fetch_input_data
import re
from typing import Iterator, Callable

PATTERN_PART_2 = re.compile(r"\b(\d+)\1+\b")
test_input="11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

def _yield_ids(input_str: str) -> Iterator[int]:
    for range_group in input_str.split(','):
        start, end = map(int, range_group.split('-'))
        yield from range(start, end + 1)

def _check_part_1(s: str) -> bool:
    mid, remainder = divmod(len(s), 2)
    return remainder == 0 and s[:mid] == s[mid:]

def _check_part_2(s: str) -> bool:
    return bool(PATTERN_PART_2.search(s))

def solve(input_str: str, part: int = 1) -> int:
    validator: Callable[[str], bool] = _check_part_1 if part == 1 else _check_part_2
    return sum(
        num for num in _yield_ids(input_str)
        if validator(str(num))
    )

if __name__ == "__main__":
    day2_input = fetch_input_data(2025, 2)
    assert solve(test_input, part=1) == 1227775554
    part1_solution = solve(day2_input, part=1)
    print(f'Part 1: {part1_solution}')

    assert solve(test_input, part=2) == 4174379265
    part2_solution = solve(day2_input, part=2)
    print(f'Part 2: {part2_solution}')