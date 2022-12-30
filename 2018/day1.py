import itertools

def part1(input: str) -> int:
    with open(input) as f:
        data = f.read().split("\n")
    return sum([int(x) for x in data])

frequency1 = part1("2018/day1.txt")
# print(frequency1)

ex1 = [+1, -2, +3, +1]
ex2 = [+3, +3, +4, -2, -4]
ex3 = [-6, +3, +8, +5, -6]
ex4 = [+7, +7, -2, -7, -4]


def frequencies(changes):
    """Given a sequence of deltas, produce a sequence of result frequencies."""
    freq = 0
    yield freq
    for ch in changes:
        freq += ch
        yield freq

def first_duplicate(seq):
    """Return the first duplicated value in a sequence."""
    seen = set()
    for value in seq:
        if value in seen:
            return value
        seen.add(value)

with open("2018/day1.txt") as f:
    data = list(map(eval, f))

dup = first_duplicate(frequencies(itertools.cycle(ex4)))
print(dup)

