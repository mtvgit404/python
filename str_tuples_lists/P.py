L = int(input())
N = int(input())
l1 = []
sum = 0
for i in range(N):
    header = input()
    if len(header) + sum + 3 < L:
        l1.append(header)
        sum += len(header)
    elif len(header) > 3:
        ostatok = (L - 3) - sum
        l1.append(header[:ostatok:])
        l1[i] = l1[i] + "..."
        break
    elif len(header) < 3:
        l1[i - 1] = '...'
        break
    else:
        l1[i] = "..."
for i in range(len(l1)):
    print(l1[i])