from itertools import combinations

with open("2020/day1.txt") as f:
    file = f.read()
    nums = [int(num) for num in file.splitlines()]


# nums = [1721, 979, 366, 299, 675, 1456]

combos = combinations(nums, 3)

for combo in combos:
    if sum(combo) == 2020:
        print(combo[0]*combo[1]*combo[2])