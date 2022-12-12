import hashlib
from collections import defaultdict
import itertools


def find_zeroes(key, nzeros):
    for i in itertools.count():
        md5 = hashlib.md5((key + str(i)).encode()).hexdigest()
        if md5.startswith("0"*nzeros):
            print(key + str(i))
            return i

for key in ["abcdef", "pqrstuv"]:
    print("Test: {!r} --> {}".format(key, find_zeroes(key, 5)))

# print("Answer: {!r} --> {}".format("bgvyzdsv", find_zeroes("bgvyzdsv", 5)))
# print("Answer: {!r} --> {}".format("bgvyzdsv", find_zeroes("bgvyzdsv", 6)))

# key1 = "abcdef" # 609043
# # MD5 hexdigest = 000006136ef2ff3b291c85725f17325c
# # 16 bytes/128 bits
# key2 = "pqrstuv" # 1048970
# my_key = "iwrupvqb"

# result = hashlib.md5(key2.encode())
# print(result.hexdigest())
# # print(result.block_size)
# # print(result.digest_size)

# # digit = 1
# new_keys = defaultdict()
# for i in range(1, 2000000):
#     new_key = key1 + str(i)
#     hashed_key = hashlib.md5(new_key.encode())
#     new_keys[str(hashed_key)] = str(new_key)
#     i += 1

# start = "00000"
# potential_keys = [value for key, value in new_keys.items() if key.lower().startswith(start.lower())]
# print(potential_keys)
