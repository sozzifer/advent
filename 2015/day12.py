with open("2015/day12.txt") as f:
    data = f.read().split()

lines = [line.strip(",") for line in data]

sum = 0
for line in lines:
    try:
        sum += eval(line)
    except:
        pass

print(sum)