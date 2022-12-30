import re
from functools import cache
from operator import and_, or_, lshift, rshift

# salt-die Advent-of-Code
WIRES = {}
with open("2015/day7ex.txt") as f:
    data = f.read().splitlines()

for line in data:
    *expr, _, wire = line.split()
    WIRES[wire] = expr

OPS = dict(AND=and_, OR=or_, LSHIFT=lshift, RSHIFT=rshift)


@cache
def eval_wire(wire: str):
    if wire.isnumeric():
        return int(wire)

    match WIRES[wire]:
        case [a]:
            return eval_wire(a)
        case ["NOT", a]:
            return ~eval_wire(a)
        case [a, OP, b]:
            return OPS[OP](eval_wire(a), eval_wire(b))


def part_one():
    return eval_wire("d")

ans = part_one()
print(ans)

def part_two():
    WIRES["b"] = [str(part_one())]
    eval_wire.cache_clear()
    return eval_wire("a")


# ChrisPenner Advent-Of-Code-Polyglot
get_cmd = re.compile("[A-Z]+")  # AND, OR, LSHIFT, RSHIFT, NOT
get_args = re.compile("[a-z0-9]+")

# Store functions by their name
funcs = {
    "AND": lambda a, b: a & b,
    "OR": lambda a, b: a | b,
    "LSHIFT": lambda a, b: a << b,
    "RSHIFT": lambda a, b: a >> b,
    "NOT": lambda a: ~a,
}

# Look up symbol, and its definition recursively, saving the results in the wires dict.
def resolve(symbol):
    if isinstance(symbol, int):
        return symbol
    value = wires[symbol]
    if not isinstance(value, tuple):
        return value
    # Value must be a tuple (command, args)
    command, args = value
    if not command:
        # If no command, it must be a simple assignment
        result = resolve(args[0])
        # store result
        wires[symbol] = result
        return result
    else:
        resolved_args = [resolve(x) for x in args]
        result = funcs[command](*resolved_args)
        # store result
        wires[symbol] = result
        return result


wires = {}
with open("2015/day7ex.txt") as f:
    for line in f:
        # Parse the command
        command = get_cmd.search(line)
        # Get all the arguments via regex
        args = get_args.findall(line)
        # Convert numeric arguments to integers
        args = [int(x) if x.isdigit() else x for x in args]
        # Get result of search if we found anything
        if command:
            command = command.group()
        # Get the storage location of the command
        to_wire = args.pop()
        # Store it
        wires[to_wire] = (command, tuple(args))

ans = resolve("i")
print(ans)

###
# from collections import defaultdict
# """
# x: 123
# y: 456
# d: 72
# e: 507
# f: 492
# g: 114
# h: 65412
# i: 65079
# """

# with open("2015/day7.txt") as f:
#     data = f.read().split("\n")

# wire_dict = defaultdict(int)

# for line in data:
#     line = line.split(" -> ")
#     if line[0].isdigit():
#         wire_dict[line[1]] = line[0]
#     else:
#         wire_dict[line[1]] = line[0].split(" ")

# for k, v in wire_dict.items():
#     if "b" in v or "b" in v:
#         print(f"{k}: {v}")
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
