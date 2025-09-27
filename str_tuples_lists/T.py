import math
str1 = input().split()
l1 = []
for c1 in str1:
    if c1 == " ":
        continue
    if c1 not in "/+-*~!#@":
        l1.append(c1)
    if len(str1) == 1:
        print(l1[0])
        quit()
    if str1 == 0:
        print(0)
    elif c1 == "*":
        a = l1.pop()
        b = l1.pop()
        res = int(a) * int(b)
        l1.append(res)
        a = 0
        b = 0
    elif c1 == "-":
        a = l1.pop()
        b = l1.pop()
        res = int(b) - int(a)
        l1.append(res)
        a = 0
        b = 0
    elif c1 == "+":
        a = l1.pop()
        b = l1.pop()
        res = int(a) + int(b)
        l1.append(res)
        a = 0
        b = 0
    elif c1 == "/":
        a = l1.pop()
        b = l1.pop()
        res = int(int(b) // int(a))
        l1.append(int(res))
        a = 0
        b = 0
    elif c1 == "~":
        a = l1.pop()
        l1.append(0 - int(a))
        a = 0
    elif c1 == "!":
        a = l1.pop()
        a_new = math.factorial(int(a))
        l1.append(a_new)
        a = 0
        a_new = 0
    elif c1 == "#":
        a = l1.pop()
        l1.append(a)
        l1.append(a)
        a = 0
    elif c1 == "@":
        a = l1.pop()
        b = l1.pop()
        c = l1.pop()
        l1.append(b)
        l1.append(a)
        l1.append(c)
        a = 0
        b = 0
        c = 0
print(l1[0])