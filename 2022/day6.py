from collections import Counter

ex1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
# answer = 7
ex2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
# answer = 5
ex3 = "nppdvjthqldpwncqszvftbrmjlhg"
# answer = 6
ex4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
# answer = 10
ex5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
# answer = 11

def find_dup_char(string):
    WC = Counter(string)
    for letter, count in WC.items():
        if count > 1:
            print(WC.items())
            # print(letter)
            return True
        else:
            return False

length = 5
for x in range(0, len(ex2)-3):
    while find_dup_char(ex2[x:x+4]):
        length += 1
        # print(x)
        x += 1
# print(find_dup_char("jmjq"))
print(length)
# count = Counter("jmjq")
# print(count.items())
# start = 0
# stop = 4
# for x in range(0, len(ex1)-3):
#     chunk = ex1[start:stop]
#     if find_dup_char(chunk):
#         print(chunk)
#     start += 1
#     stop += 1


# def find_marker(string):
#     start = 0
#     stop = 4
#     chunk = string[start:stop]
#     if find_dup_char(chunk):
#         print("Duplicate letters")
#     else:
#         return chunk

# marker1 = find_marker(ex1)
# print(marker1)
# l1, l2, l3, l4 = ex1[0:4]
