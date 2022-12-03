import pandas as pd
from string import ascii_letters

df = pd.read_csv("day3.csv")
data = df["data"].tolist()

def chunk(data, size):
    return (data[pos:pos + size] for pos in range(0, len(data), size))

def p1(data):
    compartment1 = []
    compartment2 = []
    for item in data:
        length = int(len(item) / 2)
        compartment1.append(item[0:length])
        compartment2.append(item[length:])
    total = 0
    for string1 in compartment1:
        string2 = compartment2[compartment1.index(string1)]
        letter = "".join(set(string1).intersection(string2))
        index = ascii_letters.find(letter)
        total += index + 1
    print(total)

# p1(data)

def p2(data):
    matches = []
    for group in chunk(data, 3):
        string1, string2, string3 = group[0], group[1], group[2]
        match = "".join(set(string1).intersection(string2, string3))
        matches.append(match)

    total = 0
    for letter in matches:
        index = ascii_letters.find(letter)
        total += index + 1
    print(total)

p2(data)