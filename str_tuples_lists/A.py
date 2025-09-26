N = int(input())
res = "YES"
for _ in range(N):
    word = input()
    if word.startswith('а') or word.startswith('б') or word.startswith('в'):
        res = "YES"
    else:
        res = "NO"
        print(res)
        quit()
print(res)
        