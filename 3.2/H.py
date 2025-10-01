N = int(input())
d = dict()
l1 = [] 
for _ in range(N):
    name, *food = input().split()
    for _ in range(len(food)):
        d[name] = food 
FOOD = input()

for key, value in d.items():
    if FOOD in value:
        l1.append(key)
if len(l1) == 0:
    print("Таких нет")
l1.sort()
for name in l1:
    print(name)    