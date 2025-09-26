str1 = input()
str2 = str1.replace(" ", "")
l1 = []
l1.append(str2.lower())

if l1[0] == (l1[0])[::-1]:
    print("YES")
else:
    print("NO")