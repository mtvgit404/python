N = int(input())
M = int(input())
s1 = set()
s2 = set()
for _ in range(N):
    s1.add(input())
for _ in range(M):
    s2.add(input())
res = s1 & s2
if (res):
    print(len(res))
else:
    print("Таких нет")
