with open("2020/day2.txt") as f:
    data = f.read().splitlines()

part1 = 0
for line in data:
    password = line.split()
    range = password[0].split("-")
    if password[2].count(password[1][0]) >= int(range[0]) and password[2].count(password[1][0]) <= int(range[1]):
        part1 += 1

print(part1)

part2 = 0
for line in data:
    password = line.split()
    range = password[0].split("-")
    if password[2][int(range[0])-1] in password[1][0] and password[2][int(range[1])-1] not in password[1][0]:
        part2 += 1
    elif password[2][int(range[0])-1] not in password[1][0] and password[2][int(range[1])-1] in password[1][0]:
        part2 += 1
    else:
        continue

print(part2)