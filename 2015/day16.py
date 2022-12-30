import pandas as pd
import re
"""
children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
"""
regex = re.compile(r"^Sue [0-9]{1,3}: ")

d = {
    "Sue": [],
    "children": [],
    "cats": [],
    "samoyeds": [],
    "pomeranians": [],
    "akitas": [],
    "vizslas": [],
    "goldfish": [],
    "trees": [],
    "cars": [],
    "perfumes": [],
}

df = pd.DataFrame(data=d)

with open("2015/day16.txt") as f:
    data = f.read().splitlines()

for line in data:
    # sue = line[0:5]
    # things = line[9:].split(", ")
    # for thing in things:
    #     thing = thing.split(": ")
    #     print(thing[0])
    #     print(thing[1])
        # print(df[thing[0]])
    items = regex.split(line)[1]
    item_list = items.split(", ")
    
    print(item_list)
print(df)