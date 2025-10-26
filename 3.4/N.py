from itertools import permutations
N = int(input())
l1 = []
for _ in range(N):
    l1.append(input())
vars = permutations(sorted(l1), 3)
for line in vars:
    print(", ".join(line))
