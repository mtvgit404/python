N = int(input())
M = int(input())
s1 = set()
s2 = set()
for i in range(N + M):
    s1.add(input())
cnt = N + M - (len(s1))
result = (N + M) - (2 * (cnt))
if result > 0:
    print(result)
else:
    print("Таких нет")
