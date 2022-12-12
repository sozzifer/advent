with open("2018/day1.txt") as f:
    data = f.read().split("\n")

print(sum([int(x) for x in data]))