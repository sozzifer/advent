ex_data = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

with open("2020/day4.txt") as f:
    data = f.read().split("\n\n")
# data = ex_data.split("\n\n")

passports = []
for line in data:
    pp_dict = dict()
    line = line.replace("\n", " ").split()
    for field in line:
        key, value = field.split(":")
        if key != "cid":
            pp_dict[key] = value
    passports.append(pp_dict)

count = 0
for passport in passports:
    if len(passport.keys()) == 7:
        count += 1
print(count)
def check_passports(passports):
    fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    # for field in fields:
    for passport in passports:
        if fields != set(passport.keys()):
            passports.remove(passport)
    return passports

print(len(check_passports(passports)))