from itertools import chain
N = int(input())
# N = 3
l1 = []
for _ in range(N):

    l1 += chain(input().split(", "))
for num, item in enumerate(sorted(l1), 1):
    print(f"{num}. {item}")
