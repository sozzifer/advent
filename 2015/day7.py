from collections import defaultdict
"""
x: 123
y: 456
d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
"""

with open("2015/day7.txt") as f:
    data = f.read().split("\n")

wire_dict = defaultdict(int)

for line in data:
    line = line.split(" -> ")
    if line[0].isdigit():
        wire_dict[line[1]] = line[0]
    else:
        wire_dict[line[1]] = line[0].split(" ")

for k, v in wire_dict.items():
    if "b" in v or "b" in v:
        print(f"{k}: {v}")
# print(wire_dict)

# for line in data:
#     line = line.split(" -> ")
#     if line[0].isdigit():
#         wire_dict[line[1]] = int(line[0])
#     elif "AND" in line[0]:
#         wires = line[0].split(" ")
#         wire_dict[line[1]] = wire_dict[wires[0]] & wire_dict[wires[2]]
#     elif "OR" in line[0]:
#         wires = line[0].split(" ")
#         wire_dict[line[1]] = wire_dict[wires[0]] | wire_dict[wires[2]]
#     elif "LSHIFT" in line[0] or "RSHIFT" in line[0]:
#         wires = line[0].split(" ")
#         if wires[1] == "LSHIFT":
#             wire_dict[line[1]] = wire_dict[wires[0]] << int(wires[2])
#         else:
#             wire_dict[line[1]] = wire_dict[wires[0]] >> int(wires[2])
#     elif "NOT" in line[0]:
#         wires = line[0].split(" ")
#         wire_dict[line[1]] = ~wire_dict[wires[1]]

# for k, v in wire_dict.items():
#     if v < 0:
#         wire_dict[k] = 65536 + v
