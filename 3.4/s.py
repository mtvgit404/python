from itertools import product, groupby
dict1 = dict()
str1 = input()
l1 = []

for c in str1:
    if c.isupper():
        l1.append(c)
cnt = len(set(l1))

for char in sorted(set(l1)):
    print(f"{char}", end=" ")
print("F")

vars = product([0, 1], repeat=cnt)
for var in vars:
    context = zip(sorted(set(l1)), var)
    for a, b in context:
        print(f"{b}", end=" ")
        dict1[a] = b
    res = eval(str1, dict1)
    print(int(res))
