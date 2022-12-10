with open("day5ex.txt") as f:
    data = f.read().split("\n\n")

moves_string = data[1]
moves = moves_string.split("\n")
moves_list = [move.split(" ") for move in moves]
move_ints = [[int(move[1]), int(move[3]), int(move[5])] for move in moves_list]

# crates_list = [
#     ["G", "T", "R", "W"],
#     ["G", "C", "H", "P", "M", "S", "V", "W"],
#     ["C", "L", "T", "S", "G", "M"],
#     ["J", "H", "D", "M", "W", "R", "F"],
#     ["P", "Q", "L", "H", "S", "W", "F", "J"],
#     ["P", "J", "D", "N", "F", "M", "S"],
#     ["Z", "B", "D", "F", "G", "C", "S", "J"],
#     ["R", "T", "B"],
#     ["H", "N", "W", "L", "C"],
# ]

crates_list = [
    ["Z", "N"],         # crates_list[0] from/to 1
    ["M", "C", "D"],    # crates_list[1] from/to 2
    ["P"],              # crates_list[2] from/to 3
]
#           Index 0  1  2
# move_ints[0] = [1, 2, 1] 
# move_ints[1] = [3, 1, 3]
# move_ints[2] = [2, 2, 1]
# move_ints[3] = [1, 1, 2]

print(crates_list[1][-1])
# # Part 2
# for move in move_ints:
    # print(crates_list[move[2]-1])
    # print(move[1])
    # print(move[0])
    # print(move[2])
    # print(move[-1])
    # crates_to_move = crates_list[(move[1]-1)][-(move[0])]
    # print(crates_to_move)

# Part 1
# for move in move_ints:
#     for x in range(1, move[0]+1):
#         crates_list[move[2]-1].append(crates_list[move[1]-1].pop())
#         x += 1

# for crates in crates_list:
#     print(crates[-1])
