# def a():
#     print('a() was called.')
#     b()
#     print('a() is returning.')

# def b():
#     print('b() was called.')
#     c()
#     print('b() is returning.')

# def c():
#     print('c() was called.')
#     print('c() is returning.')

# a()

# cardStack = []
# cardStack.append('5 of diamonds')
# print(', '.join(cardStack))
# cardStack.append('3 of clubs')
# print(', '.join(cardStack))
# cardStack.append('ace of hearts')
# print(', '.join(cardStack))
# print(cardStack.pop())
# print(', '.join(cardStack))

# def a():
#     spam = 'Ant'
#     print('spam is ' + spam)
#     b()
#     print('spam is ' + spam)

# def b():
#     spam = 'Bobcat'
#     print('spam is ' + spam)
#     c()
#     print('spam is ' + spam)

# def c():
#     spam = 'Coyote'
#     print('spam is ' + spam)

# a()

# def shortestWithBaseCase(makeRecursiveCall):
#     print('shortestWithBaseCase(%s) called.' % makeRecursiveCall)
#     if not makeRecursiveCall:
#         # BASE CASE
#         print('Returning from base case.')
#         return
#     else:
#         # RECURSIVE CASE
#         shortestWithBaseCase(False)
#         print('Returning from recursive case.')
#         return

# print('Calling shortestWithBaseCase(False):')
# shortestWithBaseCase(False)
# print()
# print('Calling shortestWithBaseCase(True):')
# shortestWithBaseCase(True)


# def countDownAndUp(number):
#     print(number)
#     if number == 0:
#         # BASE CASE
#         print('Reached the base case.')
#         return
#     else:
#     # RECURSIVE CASE
#         countDownAndUp(number - 1)
#         print(number, 'returning')
#         return

# countDownAndUp(3)

# def factorial(number):
#     if number == 1:
#         # BASE CASE
#         return 1
#     else:
#     # RECURSIVE CASE
#         return number * factorial(number - 1)
# print(factorial(5))


# def sumSeriesRecursion(num):
#     if num == 1:
#         return 1
#     else:
#         return num + sumSeriesRecursion(num - 1)

# print(sumSeriesRecursion(10))


# # The explicit call stack, which holds "frame objects".
# def sumSeries(num):
#     callStack = []
#     # "Call" the "sumSeries() function".
#     callStack.append({'returnAddr': 'start', 'number': num})
#     returnValue = None

#     while len(callStack) > 0:
#         # The body of the "sumSeries() function":
#         # Set number parameter.
#         number = callStack[-1]['number']
#         returnAddr = callStack[-1]['returnAddr']

#         if returnAddr == 'start':
#             if number == 1:
#                 # BASE CASE
#                 returnValue = 1
#                 # "Return" from "function call".
#                 callStack.pop()
#                 continue
#             else:
#                 # RECURSIVE CASE
#                 callStack[-1]['returnAddr'] = 'after recursive call'
#                 # "Call" the "factorial() function":
#                 callStack.append({'returnAddr': 'start', 'number': number - 1})
#                 continue
#         elif returnAddr == 'after recursive call':
#             returnValue = number + returnValue
#             # "Return from function call".
#             callStack.pop()
#             continue
#     return returnValue

# print(sumSeries(10))


# def sumPowersOf2(num):
#     callStack = []
#     callStack.append({'returnAddr': 'start', 'number': num})
#     returnValue = None

#     while len(callStack) > 0:
#         num = callStack[-1]["number"]
#         returnAddr = callStack[-1]["returnAddr"]

#         if returnAddr == "start":
#             if num == 1:
#                 returnValue = 2
#                 callStack.pop()
#                 continue
#             else:
#                 callStack[-1]["returnAddr"] = "after recursive call"
#                 callStack.append({"returnAddr": "start", "number": num - 1})
#                 continue
#         elif returnAddr == "after recursive call":
#             returnValue += 2**num
#             callStack.pop()
#             continue
#     return returnValue

# print(sumPowersOf2(5))

# def sumPowersOf2(num):
#     if num == 1:
#         return 2
#     else:
#         result = sumPowersOf2(num - 1)
#         return result + 2**num

# print(sumPowersOf2(5))


# def sum(numbers):
#     if len(numbers) == 0: # BASE CASE
#         return 0
#     else: # RECURSIVE CASE
#         head = numbers[0]
#         tail = numbers[1:]
#         return head + sum(tail)

# nums = [1, 2, 3, 4, 5]
# print('The sum of', nums, 'is', sum(nums))
# nums = [5, 2, 4, 8]
# print('The sum of', nums, 'is', sum(nums))
# nums = [1, 10, 100, 1000]
# print('The sum of', nums, 'is', sum(nums))


# def rev(theString):
#     if len(theString) == 0 or len(theString) == 1:
#         # BASE CASE
#         return theString
#     else:
#         # RECURSIVE CASE
#         head = theString[0]
#         tail = theString[1:]
#         return rev(tail) + head

# print(rev('abcdef'))
# print(rev('Hello, world!'))
# print(rev(''))
# print(rev('X'))

# def concat(strings):
#     if len(strings) == 1:
#         return strings[0]
#     else:
#         head = strings[0]
#         tail = strings[1:]
#         return head + concat(tail)

# print(concat(["Mary", "had", "a", "little", "lamb"]))


# def product(nums):
#     if len(nums) == 0:
#         return 1
#     elif len(nums) == 1:
#         return nums[0]
#     else:
#         head = nums[0]
#         tail = nums[1:]
#         return head * product(tail)

# print(product([1, 2, 3, 4, 5]))


# def isPalindrome(theString):
#     if len(theString) == 0 or len(theString) == 1:
#         # BASE CASE
#         return True
#     else:
#         # RECURSIVE CASE
#         head = theString[0]
#         middle = theString[1:-1]
#         last = theString[-1]
#         return head == last and isPalindrome(middle)

# text = 'racecar'
# print(text + ' is a palindrome: ' + str(isPalindrome(text)))
# text = 'amanaplanacanalpanama'
# print(text + ' is a palindrome: ' + str(isPalindrome(text)))
# text = 'tacocat'
# print(text + ' is a palindrome: ' + str(isPalindrome(text)))
# text = 'zophiz'
# print(text + ' is a palindrome: ' + str(isPalindrome(text)))

# def exponentByRecursion(a, n):
#     if n == 1:
#         # BASE CASE
#         return a
#     elif n % 2 == 0:
#         # RECURSIVE CASE (When n is even.)
#         result = exponentByRecursion(a, n // 2)
#         return result * result
#     elif n % 2 == 1:
#         # RECURSIVE CASE (When n is odd.)
#         result = exponentByRecursion(a, n // 2)
#         return result * result * a

# print(exponentByRecursion(3, 6))
# print(exponentByRecursion(10, 3))
# print(exponentByRecursion(17, 12))

# def exponentWithPowerRule(a, n):
#     # Step 1: Determine the operations to be performed.
#     opStack = []
#     while n > 1:
#         if n % 2 == 0:
#             # n is even.
#             opStack.append('square')
#             n = n // 2
#         elif n % 2 == 1:
#             # n is odd.
#             opStack.append('multiply')
#             n -= 1

#     # Step 2: Perform the operations in reverse order.
#     result = a # Start result at `a`.
#     while opStack:
#         op = opStack.pop()

#         if op == 'multiply':
#             result *= a
#         elif op == 'square':
#             result *= result

#     return result

# print(exponentWithPowerRule(3, 6))
# print(exponentWithPowerRule(10, 3))
# print(exponentWithPowerRule(17, 10))

# import sys

# # Set up towers A, B, and C. The end of the list is the top of the tower.
# TOTAL_DISKS = 6

# # Populate Tower A:
# TOWERS = {'A': list(reversed(range(1, TOTAL_DISKS + 1))),
#           'B': [],
#           'C': []}

# def printDisk(diskNum):
#     # Print a single disk of width diskNum.
#     emptySpace = ' ' * (TOTAL_DISKS - diskNum)
#     if diskNum == 0:
#         # Just draw the pole.
#         sys.stdout.write(emptySpace + '||' + emptySpace)
#     else:
#         # Draw the disk.
#         diskSpace = '@' * diskNum
#         diskNumLabel = str(diskNum).rjust(2, '_')
#         sys.stdout.write(emptySpace + diskSpace + diskNumLabel + diskSpace + emptySpace)

# def printTowers():
#     # Print all three towers.
#     for level in range(TOTAL_DISKS, -1, -1):
#         for tower in (TOWERS['A'], TOWERS['B'], TOWERS['C']):
#             if level >= len(tower):
#                 printDisk(0)
#             else:
#                 printDisk(tower[level])
#         sys.stdout.write('\n')
#     # Print the tower labels A, B, and C.
#     emptySpace = ' ' * (TOTAL_DISKS)
#     print('%s A%s%s B%s%s C\n' % (emptySpace, emptySpace, emptySpace, emptySpace, emptySpace))

# def moveOneDisk(startTower, endTower):
#     # Move the top disk from startTower to endTower.
#     disk = TOWERS[startTower].pop()
#     TOWERS[endTower].append(disk)

# def solve(numberOfDisks, startTower, endTower, tempTower):
#     # Move the top numberOfDisks disks from startTower to endTower.
#     if numberOfDisks == 1:
#         # BASE CASE
#         moveOneDisk(startTower, endTower)
#         printTowers()
#         return
#     else:
#         # RECURSIVE CASE
#         solve(numberOfDisks - 1, startTower, tempTower, endTower)
#         moveOneDisk(startTower, endTower)
#         printTowers()
#         solve(numberOfDisks - 1, tempTower, endTower, startTower)
#         return

# # Solve:
# printTowers()
# solve(TOTAL_DISKS, 'A', 'B', 'C')

# Uncomment to enable interactive mode:
# while True:
#    printTowers()
#    print('Enter letter of start tower and the end tower. (A, B, C) Or Q to quit.')
#    move = input().upper()
#    if move == 'Q':
#        sys.exit()
#    elif move[0] in 'ABC' and move[1] in 'ABC' and move[0] != move[1]:
#        moveOneDisk(move[0], move[1])

# import sys
# # Create the image (make sure it's rectangular!
# im = [list('...##########....................................'),
#       list('...#........#....####..................##########'),
#       list('...#........#....#..#...############...#........#'),
#       list('...##########....#..#...#..........#...##.......#'),
#       list('.......#....#....####...#..........#....##......#'),
#       list('.......#....#....#......############.....##.....#'),
#       list('.......######....#........................##....#'),
#       list('.................####........####..........######')]

# HEIGHT = len(im)
# WIDTH = len(im[0])

# def floodFill(image, x, y, newChar, oldChar=None):
#     if oldChar == None:
#         # oldChar defaults to the character at x, y.
#         oldChar = image[y][x]
#     if oldChar == newChar or image[y][x] != oldChar:
#         # BASE CASE
#         return
#     image[y][x] = newChar # Change the character.
#     # Uncomment to view each step:
#     # printImage(image)
#     # Change the neighboring characters.
#     if y + 1 < HEIGHT and image[y + 1][x] == oldChar:
#         # RECURSIVE CASE
#         floodFill(image, x, y + 1, newChar, oldChar)
#     if y - 1 >= 0 and image[y - 1][x] == oldChar:
#         # RECURSIVE CASE
#         floodFill(image, x, y - 1, newChar, oldChar)
#     if x + 1 < WIDTH and image[y][x + 1] == oldChar:
#         # RECURSIVE CASE
#         floodFill(image, x + 1, y, newChar, oldChar)
#     if x - 1 >= 0 and image[y][x - 1] == oldChar:
#         # RECURSIVE CASE
#         floodFill(image, x - 1, y, newChar, oldChar)
#     return # BASE CASE

# def printImage(image):
#     for y in range(HEIGHT):
#         # Print each row.
#         for x in range(WIDTH):
#             # Print each column.
#             sys.stdout.write(image[y][x])
#         sys.stdout.write('\n')
#     sys.stdout.write('\n')

# printImage(im)
# floodFill(im, 3, 3, 'o')
# printImage(im)

# count = 0
# for i in range(HEIGHT):
#     for j in range(WIDTH):
#         if im[i][j] == ".":
#             floodFill(im, j, i, "#")
#             count += 1

# printImage(im)
# print(count)

# def ackermann(m, n, indentation=None):
#     if indentation is None:
#         indentation = 0
#     print('%sackermann(%s, %s)' % (' ' * indentation, m, n))

#     if m == 0:
#         # BASE CASE
#         return n + 1
#     elif m > 0 and n == 0:
#         # RECURSIVE CASE
#         return ackermann(m - 1, 1, indentation + 1)
#     elif m > 0 and n > 0:
#         # RECURSIVE CASE
#         return ackermann(m - 1, ackermann(m, n - 1, indentation + 1), indentation + 1)

# print('Starting with m = 1, n = 1:')
# print(ackermann(1, 1))
# print('Starting with m = 2, n = 3:')
# print(ackermann(2, 3))

# root = {"data": "A", "children": []}
# node2 = {"data": "B", "children": []}
# node3 = {"data": "C", "children": []}
# node4 = {"data": "D", "children": []}  # Leaf node
# node5 = {"data": "E", "children": []}
# node6 = {"data": "F", "children": []}  # Leaf node
# node7 = {"data": "G", "children": []}  # Leaf node
# node8 = {"data": "H", "children": []}  # Leaf node
# root["children"] = [node2, node3]
# node2["children"] = [node4]
# node3["children"] = [node5, node6]
# node5["children"] = [node7, node8]


# root = {
#     "name": "Alice",
#     "children": [
#         {
#             "name": "Bob",
#             "children": [
#                 {"name": "Darya", "children": []}
#             ]
#         },
#         {
#             "name": "Caroline",
#             "children": [
#                 {
#                     "name": "Eve",
#                     "children": [
#                         {"name": "Gonzalo", "children": []},
#                         {"name": "Hadassah", "children": []},
#                     ],
#                 },
#                 {"name": "Fred", "children": []},
#             ],
#         },
#     ],
# }


# def find8LetterName(node):
#     print(" Visiting node " + node["name"] + "...")

#     # Preorder depth-first search:
#     # print("Checking if " + node["name"] + " is 8 letters...")
#     # if len(node["name"]) == 8:
#     #     return node["name"]  # BASE CASE

#     if len(node["children"]) > 0:
#         # RECURSIVE CASE
#         for child in node["children"]:
#             returnValue = find8LetterName(child)
#             if returnValue != None:
#                 return returnValue

#     # Postorder depth-first search:
#     print('Checking if ' + node['name'] + ' is 8 letters...')
#     if len(node['name']) == 8: return node['name'] # BASE CASE

#     # Value was not found or there are no children.
#     return None  # BASE CASE


# print("Found an 8-letter name: " + str(find8LetterName(root)))


# a = "cat"
# b = "chello"
# c = "chess"

# ls = (
#     lambda a, b: len(b)
#     if not a
#     else len(a)
#     if not b
#     else min(ls(a[1:], b[1:]) + (a[0] != b[0]), ls(a[1:], b) + 1, ls(a, b[1:]) + 1)
# )

# print(ls(a, b))
# print(ls(a, c))
# print(ls(b, c))


# root = {
#     "data": "A",
#     "children": [
#         {
#             "data": "B",
#             "children": [
#                 {"data": "D", "children": []}
#             ]
#         },
#         {
#             "data": "C",
#             "children": [
#                 {
#                     "data": "E",
#                     "children": [
#                         {"data": "G", "children": []},
#                         {"data": "H", "children": []},
#                     ],
#                 },
#                 {
#                     "data": "F", "children": []
#                 },
#             ],
#         },
#     ],
# }

from pprint import pprint as pp


# def preorderTraverse(node):
#     print(node["data"], end=" ")  # Access this node's data.
#     if len(node["children"]) > 0:
#         # RECURSIVE CASE
#         for child in node["children"]:
#             preorderTraverse(child)  # Traverse child nodes.
#     # BASE CASE
#     return
# preorderTraverse(root_dict)

# def postorderTraverse(node):
#     for child in node["children"]:
#         # RECURSIVE CASE
#         postorderTraverse(child)  # Traverse child nodes.
#     print(node["data"], end=" ")  # Access this node's data.
#     # BASE CASE
#     return
# postorderTraverse(root_dict)

# def inorderTraverse(node):
#     if len(node["children"]) >= 1:
#         # RECURSIVE CASE
#         inorderTraverse(node["children"][0])  # Traverse the left child.
#     print(node["data"], end=" ")  # Access this node's data.
#     if len(node["children"]) >= 2:
#         # RECURSIVE CASE
#         inorderTraverse(node["children"][1])  # Traverse the right child.
#     # BASE CASE
#     return

root_dict = {
    "data": "A",
    "children": [
        {"data": "B", "children": [{"data": "D", "children": []}]},  # Leaf node
        {
            "data": "C",
            "children": [
                {
                    "data": "E",
                    "children": [
                        {"data": "G", "children": []},  # Leaf node
                        {"data": "H", "children": []},  # Leaf node
                    ],
                },
                {"data": "F", "children": []},  # Leaf node
            ],
        },
    ],
}

# def inOrderReverse(node):
#     if len(node["children"]) >= 2:
#         # RECURSIVE CASE
#         inOrderReverse(node["children"][-1])  # Traverse the right child.
#     print(node["data"], end=" ")  # Access this node's data.
#     if len(node["children"]) >= 1:
#         # RECURSIVE CASE
#         inOrderReverse(node["children"][0])  # Traverse the left child.
#     # BASE CASE
#     return

# inorderTraverse(root_dict)
# inOrderReverse(root_dict)


def getDepth(node):
    if len(node["children"]) == 0:
        # BASE CASE
        return 0
    else:
        # RECURSIVE CASE
        maxChildDepth = 0
        for child in node["children"]:
            # Find the depth of each child node:
            childDepth = getDepth(child)
            if childDepth > maxChildDepth:
                # This child is deepest child node found so far:
                maxChildDepth = childDepth
        return maxChildDepth + 1


# print("Depth of tree is " + str(getDepth(root)))

def addLevel(node):
    if len(node["children"]) == 0:
        node["children"].append({"data": f"from {node['data']}", "children": []})
    else:
        for child in node["children"]:
            addLevel(child)
    return node

# pp(addLevel(root_dict))
# print(getDepth(root_dict))

def binarySearch(needle, haystack, left=None, right=None):
    # By default, `left` and `right` are all of `haystack`:
    if left is None:
        left = 0 # `left` defaults to the 0 index.
    if right is None:
        right = len(haystack) - 1 # `right` defaults to the last index.

    print('Searching:', haystack[left:right + 1])

    if left > right: # BASE CASE
         return None # The `needle` is not in `haystack`.

    mid = (left + right) // 2
    if needle == haystack[mid]: # BASE CASE
         return f"{needle} at index {mid}" # The `needle` has been found in `haystack`
    elif needle < haystack[mid]: # RECURSIVE CASE
         return binarySearch(needle, haystack, left, mid - 1)
    elif needle > haystack[mid]: # RECURSIVE CASE
         return binarySearch(needle, haystack, mid + 1, right)

print(binarySearch(13, [1, 4, 8, 11, 13, 16, 19, 19]))