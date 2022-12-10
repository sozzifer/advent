from pprint import pprint as pp
"""
(())     0
()()     0
(((      3
(()(()(  3
))(((((  3
())     -1
))(     -1
)))     -3
)())()) -3
"""
with open("day1.txt") as f:
    data = f.read().replace("\n", "")

moves = [*data]
# print(moves)
floor = 0
floor_list = []
for m in moves:
    if m == "(":
        floor += 1
        floor_list.append(str(floor))
    elif m == ")":
        floor -= 1
        floor_list.append(str(floor))

pp(floor_list)
print(floor_list.index("-1"))