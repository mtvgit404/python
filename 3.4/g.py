from itertools import combinations
n = int(input())
l1 = []
for name in range(n):
    l1.append(input())
for res in list(combinations(l1, 2)):
    print(f"{res[0]} - {res[1]}")
