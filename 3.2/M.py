N = int(input())
l1 = []
s_wehave = set()
s_day_n = set()
for _ in range(N):
    s_wehave.add(input())

M = int(input())

for _ in range(M):
    day_n = int(input()) 
    for _ in range(day_n):
        s_day_n.add(input())

result = s_wehave - s_day_n
if len(result) == N:
    print("Готовить нечего")
    quit()  

for a in result:
    l1.append(a)
l1.sort()

for l_ in l1:
    print(l_)