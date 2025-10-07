d1 = {}
N1 = None
N2 = None
set1 = set()
l1 = []
while (pair := input()):
    N1, N2 = pair.split()
    d1.setdefault(N1, []).append(N2)
    d1.setdefault(N2, []).append(N1)

for key, value in sorted(d1.items()):
    for val in value:
        set1.update(d1[val])
    for val in value:
        set1.discard(val)
    set1.discard(key)
    l1 = list(set1)
    l1.sort()
    print(f"{key}", end=": ")
    print(*l1, end='\n', sep=', ')
