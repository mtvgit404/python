N = int(input())
res = 0
count = 0
def nod(a, b):
    c = 0
    if a < b:
        a, b = max(b,a), min(a,b)
    while b:        
        res = a % b
        if res == 0:
            return b
        c = b % res
        a = res 
        b = c
    return res

for i in range(N):
    number1 = int(input())
    number2 = int(input())
    res = nod(number1,number2)
    count += 1
    if count == N - 1:
        print(res)
        quit()
    for j in range(N):
        number2 =int(input())
        res = nod(res,number2)
        count += 1
        if count == N - 1:
            print(res)
            quit()
    print(res)

    
