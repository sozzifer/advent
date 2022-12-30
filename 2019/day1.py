with open("2019/day1.txt") as f:
    masses = list(map(eval, f))

part1 = sum([(mass // 3) - 2 for mass in masses])
print(part1)

def fuel_for_module_and_fuel(mass):
    total = 0
    fuel = (mass // 3) - 2
    while fuel > 0:
        total += fuel
        fuel = (fuel // 3) - 2
    return total

part2 = 0
for mass in masses:
    part2 += fuel_for_module_and_fuel(mass)
print(part2)