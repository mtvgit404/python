N = int(input())
d = dict()
sum = 0
for _ in range(N):
    if (str1 := input()) not in d:
        d[str1] = 1
    else:
        d[str1] += 1
for key, value in d.items():
    if value > 1:
        sum += value
print(sum)