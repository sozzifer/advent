import pandas as pd

df = pd.read_csv("day2.csv")

rounds = []
for index, row in df.iterrows():
    round = [row.p1, row.p2]
    rounds.append(round)

# points = 0
# for round in rounds:
#     match round:
#         case ["A", "X"]:
#             points += 4
#         case ["A", "Y"]:
#             points += 8
#         case ["A", "Z"]:
#             points += 3
#         case ["B", "X"]:
#             points += 1
#         case ["B", "Y"]:
#             points += 5
#         case ["B", "Z"]:
#             points += 9
#         case ["C", "X"]:
#             points += 7
#         case ["C", "Y"]:
#             points += 2
#         case ["C", "Z"]:
#             points += 6

points = 0
for round in rounds:
    match round:
        case ["A", "X"]:
            points += 4
        case ["A", "Y"]:
            points += 8
        case ["A", "Z"]:
            points += 3
        case ["B", "X"]:
            points += 1
        case ["B", "Y"]:
            points += 5
        case ["B", "Z"]:
            points += 9
        case ["C", "X"]:
            points += 7
        case ["C", "Y"]:
            points += 2
        case ["C", "Z"]:
            points += 6
print(points)

outcome_score = {"X": 0, "Y": 3, "Z": 6}