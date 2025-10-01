d = dict() 
while (str := input().split()):
    for word in str:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
for name in d:
    print(f"{name} {d[name]}")