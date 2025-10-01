N = int(input())
d = dict()
flag = True
l1 = [] 
for _ in range(N):
    if (str1 := input()) not in d:
        d[str1] = 1
    else:
        d[str1] += 1
for key, value in d.items():
    if value > 1:
        append_value = str(key) + " - " + str(value)
        l1.append(append_value)        
        l1.sort()
        flag = False
        continue
for l_ in l1:
    print(l_)
if flag:
    print("Однофамильцев нет")
    quit()