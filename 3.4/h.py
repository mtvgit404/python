from itertools import cycle, islice
M = int(input())
l1 = []
for _ in range(M):
    l1.append(input())
cyckle1 = cycle(l1)
N = int(input())

for word in list(islice(cyckle1, N)):
    print(word)
