"""https://adventofcode.com/2025/day4/"""
from dotenv import load_dotenv
load_dotenv()
import sys 
sys.path.append('../..') # Parent of parent
from aoc.utils import fetch_input_data

test_input = """\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.\
"""

# Constants
# The 8 neighbors in a Moore neighborhood (dy, dx)
NEIGHBOR_OFFSETS = [
    (1, -1),  (1, 0),  (1, 1),
    (0, -1),           (0, 1),
    (-1, -1), (-1, 0), (-1, 1),
]
ROLL = '@'

def parse_grid(grid_str: str) -> list[list[str]]:
    return [[c for c in line] for line in grid_str.splitlines()]

def get_grid_dims(grid: list[list[str]]) -> tuple[int, int]:
    return len(grid), len(grid[0])

def count_adjacent_rolls(y: int, x: int, grid: list[list[str]],) -> int:
    rows, cols = get_grid_dims(grid)
    counter = 0
    for dy, dx in NEIGHBOR_OFFSETS:
        ny, nx = y + dy, x + dx
        if 0 <= ny < rows and 0 <= nx < cols:
            if grid[ny][nx] == ROLL:
                counter += 1
                
    return counter

def find_removable_rolls(grid: list[list[str]]) -> list[tuple[int, int]]:
    rows, cols = get_grid_dims(grid)
    removable = []
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] == ROLL and count_adjacent_rolls(y, x, grid) < 4:
                removable.append((y, x))            
    return removable

def solve_part1(grid_str: str) -> int:
    grid = parse_grid(grid_str)
    removable_rolls = find_removable_rolls(grid)
    return len(removable_rolls)

def solve_part2(grid_str: str) -> int:
    grid = parse_grid(grid_str)
    total_removed = 0
    while True:
        removable_rolls = find_removable_rolls(grid)
        if not removable_rolls:
            break      
        total_removed += len(removable_rolls)
        
        # Update grid state
        for y, x in removable_rolls:
            grid[y][x] = '.'
            
    return total_removed

if __name__ == "__main__":
    day3_input = fetch_input_data(2025,4)
    assert solve_part1(test_input) == 13
    part1_solution = solve_part1(day3_input)
    print(f'Part 1: {part1_solution}')

    assert solve_part2(test_input) == 43
    part2_solution = solve_part2(day3_input)
    print(f'Part 2: {part2_solution}')