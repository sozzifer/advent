from itertools import permutations, product
import math
"""
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
"""

# ingredients = {
#     "Butterscotch": {
#         "capacity": -1,
#         "durability": -2,
#         "flavor": 6,
#         "texture": 3,
#         # "calories": 8
#     },
#     "Cinnamon": {
#         "capacity": 2,
#         "durability": 3,
#         "flavor": -2,
#         "texture": -1,
#         # "calories": 3
#     }
# }

ingredients = {
    "capacity":   [2, 0, 0, 0],
    "durability": [0, 5, 0, -1],
    "flavor":     [-2, -3, 5, 0],
    "texture":    [0, 0, -1, 5],
    "calories":   [3, 3, 8, 8]
}

combos100 = [combo for combo in product(range(101), repeat=4) if sum(combo) == 100]
scores = []

for combo in combos100:
    for properties, values in ingredients.items():
        capacity = combo[0] * ingredients["capacity"][0] + combo[1] * ingredients["capacity"][1] + combo[2] * ingredients["capacity"][2] + combo[3] * ingredients["capacity"][3]
        durability = combo[0] * ingredients["durability"][0] + combo[1] * ingredients["durability"][1] + combo[2] * ingredients["durability"][2] + combo[3] * ingredients["durability"][3]
        flavor = combo[0] * ingredients["flavor"][0] + combo[1] * ingredients["flavor"][1] + combo[2] * ingredients["flavor"][2] + combo[3] * ingredients["flavor"][3]
        texture = combo[0] * ingredients["texture"][0] + combo[1] * ingredients["texture"][1] + combo[2] * ingredients["texture"][2] + combo[3] * ingredients["texture"][3]
        calories = combo[0] * ingredients["calories"][0] + combo[1] * ingredients["calories"][1] + combo[2] * ingredients["calories"][2] + combo[3] * ingredients["calories"][3]
        if calories == 500:
            scores.append([max(capacity, 0), max(durability, 0), max(flavor, 0), max(texture, 0)])
        else:
            scores.append([0, 0, 0, 0])

final_scores = [math.prod(score) for score in scores]

print(max(final_scores))

# print(score[0])
# print(final_score)

# score = []
# final_score = 1
# proportions = {"Butterscotch": 44, "Cinnamon": 56}
# for ingredient, values in ingredients.items():
#     for combo in combos100:
#         score_list = []
#         for property, value in ingredients[ingredient].items():
#             score_list.append((combo[0] * value + combo[1] * value))
#             print(score_list)
#         score.append(score_list)


# scores = {}
# for combo in combos100:
#     butterscotch_capacity = ingredients["Butterscotch"]["capacity"]*combo[0]
#     cinnamon_capacity = ingredients["Cinnamon"]["capacity"][1]

# print(combos100[176850])