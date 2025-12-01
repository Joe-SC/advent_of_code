"""https://adventofcode.com/2025/day1/"""
from dotenv import load_dotenv
load_dotenv()

import sys 
sys.path.append('../..')  # Parent of parent
from aoc.utils import fetch_input_data

from typing import Literal
Direction = Literal['L','R']

test_input = """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

DEFAULT_KWARGS = dict(
    mod=100, 
    counter_value=0, 
    starting_location=50,
)

class Solver:
    def __init__(
            self,
            mod: int,
            counter_value: int,
            starting_location: int
        ):
        self.mod = mod
        self.counter_value = counter_value
        self.starting_location = starting_location
    
    def solve_part_1(self, input_str: str)->int:
        counter: int = 0
        location = self.starting_location # python ints are immutable
        if location == self.counter_value:
            counter += 1
        for line in input_str.strip().splitlines():
            direction: Direction = line[0]
            magnitude: int = int(line[1:])
            if direction == 'L':
                move = -1 * magnitude
            elif direction == 'R':
                move = magnitude
            location = (location + move) % self.mod 
            if location == self.counter_value:
                counter += 1
        return counter
    
    def solve_part_2(self, input_str: str)->int:
        counter: int = 0
        location = self.starting_location
        
        for line in input_str.strip().splitlines():
            direction: Direction = line[0]
            magnitude: int = int(line[1:])
            
            # count circles
            full_circles = magnitude // self.mod
            counter += full_circles
            
            # find remainder movement
            remaining_magnitude = magnitude % self.mod
            prev_location = location
            
            # update location with remainder movement
            if direction == 'L':
                location = location - remaining_magnitude
            elif direction == 'R':
                location = location + remaining_magnitude
            
            if location >= self.mod or location <= 0:
                location = location % self.mod
                if prev_location != 0:
                    counter += 1   
        return counter
    

if __name__ == "__main__":
    day1_input = fetch_input_data(2025, 1)
    solver = Solver(**DEFAULT_KWARGS)
    assert solver.solve_part_1(test_input) == 3
    part1_solution = solver.solve_part_1(day1_input)
    print(f'Part 1: {part1_solution}')

    assert solver.solve_part_2(test_input) == 6
    part2_solution = solver.solve_part_2(day1_input)
    print(f'Part 2: {part2_solution}')