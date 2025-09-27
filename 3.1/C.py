L = int(input())
N = int(input())

for _ in range(N):
    header = input()
    length = len(header)
    if length <= L:
        print(header)
    else:
        print(f"{header[:L -3]}", end='...\n')