from itertools import product
N = int(input())
print("А Б В")
k = 0
for i, j in product(range(1, N + 1), repeat=2):
    k = N - (i + j)
    if k > 0:
        print(f"{i} {j} {k}")
