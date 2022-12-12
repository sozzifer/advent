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
# x = 123
# y = 456
# d = format(x & y, "016b")
# e = format(x | y, "016b")
# f = format(x << 2, "016b")
# g = format(y >> 2, "016b")
# h = format(~x, "016b")
# i = format(~y, "016b")
# print(f"x: {x}")
# print(f"y: {y}")
# print(f"d: {d}")
# print(f"e: {e}")
# print(f"f: {f}")
# print(f"g: {g}")
# print(f"h: {h}")
# print(f"i: {i}")

# print(bin(x))
# print(bin(y))
# print(bin(65412))
# print(bin(65079))


with open("2015/day7ex.txt") as f:
    data = f.read().split("\n")

wire_dict = defaultdict(int)
for line in data:
    line = line.split(" -> ")
    if line[0].isdigit():
        wire_dict[line[1]] = bin(int(line[0]))
    elif "AND" in line[0]:
        line = line[0].split(" ")
        print(line)
        first = line[0]
        second = line[2]
    
        # value = wire_dict[line[0]] & wire_dict[line[2]]
        # wire_dict[line[1]] = value
    elif "OR" in line[0]:
        line[0] = line[0].split(" ")
        print(line[0])
    elif "LSHIFT" in line[0] or "RSHIFT" in line[0]:
        line[0] = line[0].split(" ")
        print(line[0])
    elif "NOT" in line[0]:
        print(line)

print(type(wire_dict["x"]))

