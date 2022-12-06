with open("day5.txt") as f:
    data = f.read().split("\n\n")

crates_dict = {
    1: ["G", "T", "R", "W"],
    2: ["G", "C", "H", "P", "M", "S", "V", "W"],
    3: ["C", "L", "T", "S", "G", "M"],
    4: ["J", "H", "D", "M", "W", "R", "F"],
    5: ["P", "Q", "L", "H", "S", "W", "F", "J"],
    6: ["P", "J", "D", "N", "F", "M", "S"],
    7: ["Z", "B", "D", "F", "G", "C", "S", "J"],
    8: ["R", "T", "B"],
    9: ["H", "N", "W", "L", "C"],
}

# crates_string = data[0]
moves_string = data[1]
moves = moves_string.split("\n")
moves_list = [move.split(" ") for move in moves]
move_ints = [[int(move[1]), int(move[3]), int(move[5])] for move in moves_list]
print(move_ints)


for move in move_ints:
    for x in range(1, move[0]+1):
        crates_dict[move[2]].append(crates_dict[move[1]].pop())
        x += 1

for crates in crates_dict.values():
    print(crates[-1])
