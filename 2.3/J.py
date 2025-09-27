N = int(input())
i=0
j=0
k=0

print(f"А Б В")
for i in range(1, N):
    for j in range(1, N):
        for k in range(1,N):
            if (i + j + k) != N:
                continue          
            print(f"{i} {j} {k}")
                