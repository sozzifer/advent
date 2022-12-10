"""
noop
addx 3
addx -5
"""
day10ex1 = [
    "noop",
    "addx 3",
    "addx -5"
]

with open("day10.txt")as f:
    data = f.read().split("\n")

cycles = 0
cycles_list = [0]
x = 1
x_list = [1]
for op in data:
    if op == "noop":
        cycles += 1
        cycles_list.append(cycles)
        x_list.append(x)
    else:
        cycles += 1
        cycles_list.append(cycles)
        x_list.append(x)
        reg = int(op.removeprefix("addx "))
        cycles += 1
        cycles_list.append(cycles)
        x += reg
        x_list.append(x)

print(f"Cycles: {cycles_list}")
print(f"Register: {x_list}")

sum = (20 * x_list[19]) + (60 * x_list[59]) + (100 * x_list[99]) + (140 * x_list[139]) + (180 * x_list[179]) + (220 * x_list[219])
print(x_list[19])
# print(x_list[20])
print(x_list[59])
# print(x_list[60])
print(x_list[99])
# print(x_list[100])
print(x_list[139])
# print(x_list[140])
print(x_list[179])
# print(x_list[180])
print(x_list[219])
# print(x_list[220])
print(sum)