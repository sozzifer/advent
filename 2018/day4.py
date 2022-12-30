with open("2018/day4ex.txt") as f:
    data = f.read().split("\n")

dates = []
times = []
actions = []
for line in data:
    new_line = line.split()
    dates.append(new_line[0][6:])
    times.append(new_line[1][:-1])
    actions.append(new_line[3])

print(dates)
print(times)
print(actions)