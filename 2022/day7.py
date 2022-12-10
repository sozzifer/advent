from pprint import pprint as pp
directory = {
    """
    - / (dir)
    - a (dir)
        - e (dir)
        - i (file, size=584)
        - f (file, size=29116)
        - g (file, size=2557)
        - h.lst (file, size=62596)
    - b.txt (file, size=14848514)
    - c.dat (file, size=8504156)
    - d (dir)
        - j (file, size=4060174)
        - d.log (file, size=8033020)
        - d.ext (file, size=5626152)
        - k (file, size=7214296)
    """
    "/": {
        "a": {
            "e": {
                "i": 584
            },
        "f": 29116,
        "g": 2557,
        "h.lst": 62596
        },
        "b.txt": 14848514,
        "c.dat": 8504156,
        "d": {
            "j": 4060174,
            "d.log": 8033020,
            "d.ext": 5626152,
            "k": 7214296
        }
    }
}
# def populate_directory()
with open("day7ex.txt") as f:
    data = f.read().split("$ ")

for line in data:
    line.removesuffix("\n")
    print(line)
data = [line.removesuffix("\n") for line in data]
pp(data)

my_dir = {}

for line in data:
    if line.startswith("cd ") and ".." not in line:
        line = line.split(" ")
        my_dir[line[1]] = {}
    # else:
# for line in data:
#     if line.startswith("$"):
#         if "$ cd" in line:
#             directory = line.removeprefix("$ cd ")
#             if ".." not in line:
#                 my_dir[directory] = {}
#             print(f"Change dir: {directory}")
#         else:
#             print("List contents")
#     elif line.startswith("dir"):
#         directory = line.removeprefix("dir ")
#         print(f"Directory: {directory}")
#     else:
#         file = line.split(" ")
#         file_size = file[0]
#         file_name = file[1]
#         print(f"File {file_name}, {file_size} bytes")