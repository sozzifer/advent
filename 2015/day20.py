"""
House 1 got 10 presents.
House 2 got 30 presents.
House 3 got 40 presents.
House 4 got 70 presents.
House 5 got 60 presents.
House 6 got 120 presents.
House 7 got 80 presents.
House 8 got 150 presents.
House 9 got 130 presents.
"""

houses = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
}

elves = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for elf in elves:
    for house, presents in houses.items():
        if house % elf == 0:
            # print(house)
            # print(elf)
            house += 10*elf
            # print(presents)
        print(houses)
