from collections import Counter

with open("2018/day2.txt") as f:
    data = f.read().splitlines()

def checksum(data):
    twice = 0
    thrice = 0
    for string in data:
        counter = Counter(string)
        flipped = {}
        for key, value in counter.items():
            if value not in flipped:
                flipped[value] = [key]
            else:
                flipped[value].append(key)
        if 2 in flipped.keys():
            twice += 1
        if 3 in flipped.keys():
            thrice += 1
    return twice * thrice

part1 = checksum(data)
# print(part1)

str1 = "abcdef" # contains no letters that appear exactly two or three times.
str2 = "bababc" # contains two a and three b, so it counts for both.
str3 = "abbcde" # contains two b, but no letter appears exactly three times.
str4 = "abcccd" # contains three c, but no letter appears exactly two times.
str5 = "aabcdd" # contains two a and two d, but it only counts once.
str6 = "abcdee" # contains two e.
str7 = "ababab" # contains three a and three b, but it only counts once.
str_list = [str1, str2, str3, str4, str5, str6, str7]

def char_counts(s):
    """Given a string, return a set of character counts occurring."""
    return set(Counter(s).values())

for string in str_list:
    print(char_counts(string))

def checksum(ids):
    counts = [char_counts(s) for s in ids]
    num2 = sum((2 in cc) for cc in counts)
    num3 = sum((3 in cc) for cc in counts)
    return num2 * num3

ans = checksum(data)
print(f"Part 1: the checksum is {ans}")


str1 = "abcde"
str2 = "fghij"
str3 = "klmno"
str4 = "pqrst"
str5 = "fguij"
str6 = "axcye"
str7 = "wvxyz"
str_list = [str1, str2, str3, str4, str5, str6, str7]

# for string in zip(str1, str2, str3, str4, str5, str6, str7):
#     print(string)
# counter = {}
# for string in str_list:
#     counter[string] = 0
#     for i in range(len(str_list)):
#         for j in range(len(string)):
#             if string != str_list[i]:
#                 string_compare = zip(string, str_list[i])
#             print(list(string_compare))

# print(counter)