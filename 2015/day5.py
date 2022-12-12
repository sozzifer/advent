from collections import Counter
from pprint import pprint as pp
import re

vowels = ["a", "e", "i", "o", "u"]
naughty_strings = ["ab", "cd", "pq", "xy"]

with open("2015/day6.txt") as f:
    data = f.read().split("\n")

ex1 = "ugknbfddgicrmopn" # nice
ex2 = "aaa"               # nice
ex3 = "jchzalrnumimnmhp" # naughty
ex4 = "haegwjzuvuyypxyu" # naughty
ex5 = "dvszwmarrgswjxmb" # naughty

ex6 = "qjhvhtzxzqqjkmpb"  # nice
ex7 = "xxyxx"             # nice
ex8 = "uurcxstgmygtbstg"  # naughty - no char?char
ex9 = "ieodomkazucvgmuy"  # naughty - no pairs
ex10 = "uxcplgxnkwbdwhrp" # ?

# It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
def check_aba(string):
    regexp = re.compile(r"(\w{1}).(\1)")
    if re.search(regexp, string):
        return True

# It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
def check_repeats(string):
    regexp = re.compile(r"(\w{2}).*?(\1)")
    if re.search(regexp, string):
        return True
"""
r"(\w{2}).*?(\1)"
1st Capturing Group (\w{2})
\w matches any word character (equivalent to [a-zA-Z0-9_])
{2} matches the previous token exactly 2 times
. matches any character (except for line terminators)
*? matches the previous token between zero and unlimited times, as few times as possible, expanding as needed (lazy)
2nd Capturing Group (\1)
\1 matches the same text as most recently matched by the 1st capturing group
Global pattern flags 
"""

def check_vowels(string):
    counter = Counter(string)
    if sum(counter[vowel] for vowel in vowels) >= 3:
        return True

def check_doubles(string):
    regexp = re.compile(r"(.)\1")
    if re.search(regexp, string):
        return True

def check_naughty(string):
    if "ab" in string:
        return False
    elif "cd" in string:
        return False
    elif "pq" in string:
        return False
    elif "xy" in string:
        return False
    else:
        return True

def check_niceness(strings):
    nice_strings = 0
    for string in strings:
        if check_vowels(string) and check_doubles(string) and check_naughty(string):
            nice_strings += 1
    return nice_strings

def check_niceness_again(strings):
    nice_strings = 0
    for string in strings:
        if check_repeats(string) and check_aba(string):
            nice_strings += 1
    return nice_strings

print(check_niceness_again(data))
# print(check_niceness(data))
print(check_repeats("suerykeptdsutidb"))

