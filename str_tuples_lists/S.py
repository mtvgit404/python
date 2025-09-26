str1 = input().split()
l1 = []
for c in str1:
    if c not in "+-*":
        l1.append(c)
    elif c == "*":
        a = l1.pop()
        b = l1.pop()
        l1.append(str(int(a) * int(b)))
    elif c == "-":
        a = l1.pop()
        b = l1.pop()
        l1.append(str(int(b) - int(a)))
    elif c == "+":
        a = l1.pop()
        b = l1.pop()
        res = int(a) + int(b)
        l1.append(str(res))
print(l1[0])