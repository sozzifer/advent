import pandas as pd

df = pd.read_csv("day2.csv")

rounds = []
for index, row in df.iterrows():
    round = [row.p1, row.p2]
    rounds.append(round)

points1 = 0
for round1 in rounds:
    match round1:
        case ["A", "X"]:
            points1 += 4
        case ["A", "Y"]:
            points1 += 8
        case ["A", "Z"]:
            points1 += 3
        case ["B", "X"]:
            points1 += 1
        case ["B", "Y"]:
            points1 += 5
        case ["B", "Z"]:
            points1 += 9
        case ["C", "X"]:
            points1 += 7
        case ["C", "Y"]:
            points1 += 2
        case ["C", "Z"]:
            points1 += 6

print(points1)

points2 = 0
for round2 in rounds:
    match round2:
        case ["A", "X"]:
            points2 += 3
        case ["A", "Y"]:
            points2 += 4
        case ["A", "Z"]:
            points2 += 8
        case ["B", "X"]:
            points2 += 1
        case ["B", "Y"]:
            points2 += 5
        case ["B", "Z"]:
            points2 += 9
        case ["C", "X"]:
            points2 += 2
        case ["C", "Y"]:
            points2 += 6
        case ["C", "Z"]:
            points2 += 7
print(points2)
