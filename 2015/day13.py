from itertools import permutations
from pprint import pprint as pp
happiness = {}
people = set()

with open("2015/day13.txt") as f:
    data = f.read().splitlines()

for line in data:
    params = line.strip(".").split(" ")
    person, _, sign, happy_units, _, _, _, _, _, _, next_to = params
    if sign == "gain":
        happy_units = int(happy_units)
    elif sign == "lose":
        happy_units = int(happy_units) * -1
    happiness[person, next_to] = happy_units
    people.add(person)
    people.add(next_to)

# people.add("Soz")
# print(people)

for person in people:
    happiness[(person, "Soz")] = 0
    happiness[("Soz", person)] = 0
people.add("Soz")
# pp(happiness)

perms = permutations(people)
happiness_totals = []

for perm in perms:
    total = 0
    for i, person in enumerate(perm):
        if i == len(perm) - 1:
            total += happiness[(perm[i], perm[0])]
            total += happiness[(perm[0], perm[i])]
            break
        next_to = perm[i+1]
        total += happiness[(person, next_to)]
        total += happiness[(next_to, person)]
    happiness_totals.append(total)

print(max(happiness_totals))