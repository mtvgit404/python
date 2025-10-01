N = int(input())
s1 = set(input().split())
for _ in range(1, N):
    s2 = set(input().split())
    res = s1 | s2
    s1 = res
print(*res, sep='\n')