N = int(input())
d = {}
l1 = []
for line in range(N):
    str1 = input()
    name, toys = str1.split(":", 1)
    toys = toys.split(",")

    for toy in toys:
        if toy not in d:
            d[toy] = [name]
        else:
            d[toy].append(name)
for key, values in d.items():
    values = list(dict.fromkeys(values))
    if len(values) == 1:
        l1.append(key)
l1.sort()
for l_ in l1:
    print((l_).lstrip().rstrip())