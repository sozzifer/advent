from itertools import groupby
"""
1 becomes 11 (1 copy of digit 1).
11 becomes 21 (2 copies of digit 1).
21 becomes 1211 (one 2 followed by one 1).
1211 becomes 111221 (one 1, one 2, and two 1s).
111221 becomes 312211 (three 1s, two 2s, and one 1).
"""
input = "1113222113"

def look_and_say(iterations, sequence='1'):
    arr = [sequence]
    def get_sequence(arr,iterations,sequence):
        if iterations == 0:
            return arr
        else:
            current = ''.join(str(len(list(group))) + key for key,group in groupby(sequence))
            arr.append(current)
            get_sequence(arr,iterations-1,current)
        return arr
    final_sequence = get_sequence(arr,iterations,sequence)
    return final_sequence

part1 = look_and_say(50, sequence=input)
print(len(part1[-1]))