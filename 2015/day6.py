from pprint import pprint as pp


def turn_on1(lst, grid):
    for i in range(lst[0][1], lst[1][1]+1): # rows
        for j in range(lst[0][0], lst[1][0]+1): # lights
            if grid[i][j] == 0:
                grid[i][j] = 1
            j += 1
        i += 1
    return grid

def toggle1(lst, grid):
    for i in range(lst[0][1], lst[1][1]+1): # rows
        for j in range(lst[0][0], lst[1][0]+1): # lights
            if grid[i][j] == 0:
                grid[i][j] = 1
            elif grid[i][j] == 1:
                grid[i][j] = 0
            j += 1
        i += 1
    return grid

def turn_off1(lst, grid):
    for i in range(lst[0][1], lst[1][1]+1): # rows
        for j in range(lst[0][0], lst[1][0]+1): # lights
            if grid[i][j] == 1:
                grid[i][j] = 0
            j += 1
        i += 1
    return grid

def turn_on2(lst, grid):
    for i in range(lst[0][1], lst[1][1]+1): # rows
        for j in range(lst[0][0], lst[1][0]+1): # lights
            grid[i][j] = grid[i][j] + 1
            j += 1
        i += 1
    return grid

def toggle2(lst, grid):
    for i in range(lst[0][1], lst[1][1]+1): # rows
        for j in range(lst[0][0], lst[1][0]+1): # lights
            grid[i][j] = grid[i][j] + 2
            j += 1
        i += 1
    return grid

def turn_off2(lst, grid):
    for i in range(lst[0][1], lst[1][1]+1): # rows
        for j in range(lst[0][0], lst[1][0]+1): # lights
            if grid[i][j] != 0:
                grid[i][j] = grid[i][j] - 1
            j += 1
        i += 1
    return grid

with open("2015/day6.txt") as f:
    data = f.read().split("\n")

grid = [[0] * 1000 for _ in range(1000)]
# grid = [[0] * 10 for _ in range(10)]

for line in data:
    line = line.split(" ")
    if line[0] == "turn":
        line.remove(line[0])
    lst = [line[0], [[int(i) for i in line[1].split(",")], [int(i) for i in line[3].split(",")]]]
    if lst[0] == "on":
        grid = turn_on2(lst[1], grid)
    elif lst[0] == "off":
        grid = turn_off2(lst[1], grid)
    else:
        grid = toggle2(lst[1], grid)


# ex1 = [[0, 0], [9, 9]] # turn on lights 0 to 9 for rows 0 to 9
# ex2 = [[0, 0], [9, 0]] # toggle lights 0 to 9 for row 0
# ex3 = [[4, 4], [5, 5]] # turn off lights 4 to 5 for rows 4 to 5

# grid = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
#     [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
#     [1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
#     [0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
#     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
# ]

# grid = turn_on(ex1, grid)
# grid = toggle(ex1, grid)
# grid = turn_off(ex1, grid)

# grid = turn_on(ex2, grid)
# grid = toggle(ex2, grid)
# grid = turn_off(ex2, grid)

# grid = turn_on(ex3, grid)
# grid = toggle(ex3, grid)
# grid = turn_off(ex3, grid)
# pp(grid)

solution = [sum(l) for l in zip(*grid)]
print(sum(solution))