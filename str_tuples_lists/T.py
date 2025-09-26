import math
str1 = input().split()
l1 = []
for c in str1:
    if c not in "+-*//~!#@":
        l1.append(c)
    if len(str1) == 1:
        print(l1[0])
        quit()
    elif c == "*":
        a = l1.pop()
        b = l1.pop()
        res = int(a) * int(b)
        l1.append(res)
    elif c == "-":
        a = l1.pop()
        b = l1.pop()
        res = int(b) - int(a)
        l1.append(res)
    elif c == "+":
        a = l1.pop()
        b = l1.pop()
        res = int(a) + int(b)
        l1.append(res)
    elif c == "/":
        a = l1.pop()
        b = l1.pop()
        res = int(b) // int(a)
        l1.append(res)
    elif c == "~":
        a = l1.pop()
        l1.append(int(-a))
    elif c == "!":
        a = l1.pop()
        a_new = math.factorial(int(a))
        l1.append(a_new)
    elif c == "#":
        a = l1.pop()
        l1.append(a)
        l1.append(a)
    elif c == "@":
        a = l1.pop()
        b = l1.pop()
        c = l1.pop()
        l1.append(b)
        l1.append(a)
        l1.append(c)
print(l1[0])