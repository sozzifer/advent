from collections import Counter

with open("2016/day6.txt") as f:
    data = f.read().split("\n")

string_dict = {i: "" for i in range(len(data[0]))}
print(string_dict)
for line in data:
    for i in range(len(line)):
        string_dict[i] += line[i]

# print(len(string_dict[0]))
for key, value in string_dict.items():
    counter = Counter(value)
    print(counter.most_common()[:-2:-1])
