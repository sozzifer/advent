with open("2015/day8.txt") as f:
    data = f.read().split("\n")

literals_sum = sum(len(string) for string in data)
double_quotes = len(data) * 2
code_sum = literals_sum

for line in data:
    if "\x" in line:
        hex_count = line.count("\x")
        code_sum += 3 * hex_count
    elif "\\" in line:
        slash_count = line.count("\\")
        code_sum += slash_count
    elif "\"" in line:
        quote_count = line.count("\\")
        code_sum += quote_count

print(code_sum - literals_sum)



str1 = ""
str2 = "abc"
str3 = "aaa\"aaa"
str4 = "\x27"

esc_seqs = ["\\", "\"", "\x27"]

print(len(str1))
print(len(str2))
print(len(str3))
print(len(str4))
print(len(esc_seqs[0]))
print(len(esc_seqs[1]))
print(len(esc_seqs[2]))
