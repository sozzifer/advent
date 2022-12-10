with open("day8ex.txt") as f:
    data = f.read().split("\n")

tree_grid = []
for row in data:
    row = [eval(i) for i in [*row]]
    tree_grid.append(row)

num_rows_to_check_i = len(tree_grid) // 2
num_cols_to_check_j = len(tree_grid[0]) // 2
print(num_rows_to_check_i)
print(num_cols_to_check_j)
for i in range(num_rows_to_check_i):
    for j in range(num_cols_to_check_j):
        print(tree_grid[i-1][j-1])
        print
"""
j = horizontal position
 0  1  2  3  4
[3, 0, 3, 7, 3] 0
[2, 5, 5, 1, 2] 1
[6, 5, 3, 3, 2] 2   i = vertical position
[3, 3, 5, 4, 9] 3
[3, 5, 3, 9, 0] 4

Rows to check (i) = 2
Cols to check (j) = 2
1 = i-(rows_to_check - 1)
First layer:
    First location to check: tree_grid[i-1][j-1]
        Locations to check:
        tree_grid[0][1] up
        tree_grid[2][1] down (repeated in second layer)
        tree_grid[1][0] left
        tree_grid[1][2] right (repeated in second layer)

    Last location to check: tree_grid[i+1][j+1]
        Locations to check:
        tree_grid[2][3] up (repeated in second layer)
        tree_grid[4][3] down
        tree_grid[3][2] left (repeated in second layer)
        tree_grid[3][4] right

Second layer:
    First location to check: tree_grid[i][j]
        tree_grid[0][2]  tree_grid[1][2]* up
        tree_grid[3][2]* tree_grid[4][2]  down
        tree_grid[2][0]  tree_grid[2][1]* left
        tree_grid[2][3]* tree_grid[2][4]  right

"""