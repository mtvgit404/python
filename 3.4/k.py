N = int(input())
M = int(input())
maxlen = int(len(str(M * N)))
linear = range(1, (N * M) + 1)
iters = [iter(linear)] * M
result = list(zip(*iters))
for row, string in enumerate(result, 1):
    for digit in string:
        print(f"{digit:>{maxlen}}", end=" ")
    print()
