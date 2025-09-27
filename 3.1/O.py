N = input().split()
res = 0
count = 0


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


for i in range(len(N)):
    if i == 0:
        number1 = int(N[1])
    number2 = int(N[i])
    res = nod(number1, number2)
    number1 = res
    if i == len(N) - 1:
        print(res)

    
