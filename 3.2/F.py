N = int(input())
M = int(input())
s1 = set()
for _ in range(N + M):
    if (fn := input()) not in s1:
        s1.add(fn)
    else:
        s1.discard(fn)     
l1 = []
for name in s1:
    l1.append(name)
    l1.sort()

if len(l1) == 0:
    print("Таких нет")
else:
    for name in l1:
        print(name)

