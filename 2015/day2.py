def surface_area(l, w, h):
    vals = sorted([l, w, h])
    surface_area = (2*l*w) + (2*w*h) + (2*l*h) + (vals[0]*vals[1])
    ribbon_length = (2*vals[0] + 2*vals[1]) + (l*w*h)
    return surface_area, ribbon_length

with open("2015/day2.txt") as f:
    data = f.read().split("\n")

input = []
for line in data:
    input.append([eval(x) for x in line.split("x")])

total_paper = 0
total_ribbon = 0
for i in input:
    paper, ribbon = surface_area(i[0], i[1], i[2])
    total_paper += paper
    total_ribbon += ribbon

print(total_paper)
print(total_ribbon)