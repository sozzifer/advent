from collections import Counter, OrderedDict
import numpy as np

room1 = "aaaaa-bbb-z-y-x-123[abxyz]"
room2 = "a-b-c-d-e-f-g-h-987[abcde]"
room3 = "not-a-real-room-404[oarel]"
room4 = "totally-real-room-200[decoy]"
rooms = [
    "aaaaa-bbb-z-y-x-123[abxyz]",
    "a-b-c-d-e-f-g-h-987[abcde]",
    "not-a-real-room-404[oarel]",
    "totally-real-room-200[decoy]",
]

for room in rooms:
    room_code = "".join([str(i) for i in room[:-7].split("-")[:-1]])
    sector_id = room[:-7].split("-")[-1:][0]
    checksum = room[-6:-1]

    counter_dict = dict(Counter(room_code))
    print(counter_dict)
    keys = list(counter_dict.keys())
    print(keys)
    values = list(counter_dict.values())
    print(values)
    sorted_value_index = np.argsort(values)[::-1][:5]
    print(sorted_value_index)
    sorted_dict = {keys[i]: values[i] for i in sorted_value_index}
    print(sorted_dict)

    counter = Counter(room_code)
    sorted_keys = OrderedDict(sorted(counter.items()))
    # sorted_values = OrderedDict(sorted(counter.values()))
    print(sorted_keys)
    # print(sorted_values)

# print(room_code)
# print(int(sector_id))
# print(checksum)

