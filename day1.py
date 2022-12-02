with open("day1.txt") as f:
    data = f.read()

elves = data.split("\n\n")
calories = [elf.split("\n") for elf in elves]

day1_dict = dict()
key = 1

for calorie in calories:
    day1_dict["elf" + str(key)] = sum([(int(cal)) for cal in calorie])
    key += 1

print(max(day1_dict.values()))

top3 = list(day1_dict.values())
top3.sort(reverse=True)
print(top3[:3])