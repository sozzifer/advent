with open("day4.txt") as f:
    data = f.read().replace("-", ",").split("\n")

item_lists = [[int(x) for x in item.split(",")] for item in data]

split_lists = [[item_list[0:2],item_list[2:]] for item_list in item_lists]

ranges1 = [set(range(int(split_list[0][0]), int(split_list[0][1]+1))) for split_list in split_lists]
ranges2 = [set(range(int(split_list[1][0]), int(split_list[1][1]+1))) for split_list in split_lists]

subset1 = 0
subset2 = 0
subset3 = 0
ranges = []
for range1 in ranges1:
    range2 = ranges2[ranges1.index(range1)]
    if range1.issubset(range2):
        ranges.append(range1)
        subset1 += 1
    elif range2.issubset(range1):
        ranges.append(range1)
        subset2 += 1
    else:
        subset3 += 1

# print(subset1+subset2)
# print(subset3)
print(len(ranges))
with open("day4.txt") as f2:
    data2 = f2.read().split("\n")

irange = lambda a, b: range(a, b + 1)

def p1(f):
    ans = 0
    list_a = []
    list_b = []
    for l in f:
        a, b = l.strip().split(",")
        a = set(irange(*map(int, a.split("-"))))
        b = set(irange(*map(int, b.split("-"))))
        if len(a - b) == 0 or len(b - a) == 0:
            list_a.append(a)
            list_b.append(b)
            ans += 1
    return ans, list_a, list_b

ans, list_a, list_b = p1(data2)

values = [x for x in list_a if not any([x in ranges])]

# print(values)
print(len(values))