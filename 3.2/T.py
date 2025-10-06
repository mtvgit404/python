def nod(a, b):
    c = 0
    if a < b:
        a, b = max(b, a), min(a, b)
    while b:        
        res = a % b
        if res == 0:
            return b
        c = b % res
        a = res 
        b = c
    return res


string1 = input().split("; ")
set1 = set(string1)
l1 = []
string1 = list(set1)
sorted_string = sorted(string1, key=int)
for _ in range(len(sorted_string)):
    digit1 = sorted_string[_]
    for digit2 in sorted_string:
        if nod(int(digit2), int(digit1)) > 1:
            continue
        else:
            l1.append(digit2)
    if len(l1) > 0:
        print(f"{digit1} - {', '.join(l1)}")
        l1.clear()