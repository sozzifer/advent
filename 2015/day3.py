from collections import defaultdict
from typing import List

def first_line(filename: str) -> str:
    """ Given a filename, returns the first line of a file. """
    with open(filename) as file:
        return file.readline().strip()

def all_lines(filename: str) -> List[str]:
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]

ex1 = ">"
ex2 = "^>v<"
ex3 = "^v^v^v^v^v"

def count_visited(directions: str, num_santas: int):
    deltas = {
        ">": complex(1, 0),
        "<": complex(-1, 0),
        "^": complex(0, 1),
        "v": complex(0, -1),
    }
    locs = [complex(0, 0)] * num_santas
    seen = defaultdict(int)
    seen[locs[0]] += 1
    i = 0

    for char in directions:
        locs[i] += deltas[char]
        seen[locs[i]] += 1
        i = (i + 1) % num_santas
    return len(seen.keys())


class Day03:
    """ AoC 2015 Day 03 """

    @staticmethod
    def part1(filename: str) -> int:
        """ Given a filename, solve 2015 day 03 part 1 """
        directions = first_line(filename)
        return count_visited(directions, 1)

    @staticmethod
    def part2(filename: str) -> int:
        """ Given a filename, solve 2015 day 21 part 2 """
        directions = first_line(filename)
        return count_visited(directions, 2)

sol = Day03
print(sol.part1("2015/day3.txt"))
print(sol.part2("2015/day3.txt"))
# ex_grid = [
#     [0, 0, 0],
#     [0, 1, 0],
#     [0, 0, 0]
# ]

# with open("2015/day3.txt") as f:
#     data = f.read()

# width = abs(data.count("<") - data.count(">"))
# height = abs(data.count("v") - data.count("^"))

# row = [0] * (2*width + 1)
# grid = [row for i in range(2*height + 1)]
# grid[87][41] = 1

# start = grid[87][41]