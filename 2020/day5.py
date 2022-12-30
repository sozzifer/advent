# ex1 = "FBFBBFFRLR" # row 44, column 5, seat ID 357
# ex2 = "BFFFBBFRRR" # row 70, column 7, seat ID 567
# ex3 = "FFFBBBFRRR" # row 14, column 7, seat ID 119
# ex4 = "BBFFBBFRLL" # row 102, column 4, seat ID 820

def find_row(string, start, end):
    if end - start == 1:
        return start
    mid = (start + end) // 2
    if string[0] == "F":
        return find_row(string[1:], start, mid)
    elif string[0] == "B":
        return find_row(string[1:], mid, end)

def find_col(string, start, end):
    if end - start == 1:
        return start
    mid = (start + end) // 2
    if string[0] == "L":
        return find_col(string[1:], start, mid)
    elif string[0] == "R":
        return find_col(string[1:], mid, end)


with open("2020/day5.txt") as f:
    data = f.read().splitlines()

seat_ids = [(find_row(line[:7], 0, 128)*8) + find_col(line[7:], 0, 8) for line in data]

print(max(seat_ids))

for id in range(min(seat_ids), max(seat_ids)+1):
    if id not in seat_ids:
        print(id)
