N = int(input())
i = 1
sum = 0
prostoe = 0
result = 0
cycle = 1
for _ in range(N):
    number = int(input())
    num = number
    while cycle <= num:
        if (num % i) == 0:
            sum += 1
            if sum > 2:
                break
        i += 1
        cycle += 1
    if (number == 2 or number != 1) and sum < 3:
        prostoe = 1
    else:
        prostoe = 0
    result += prostoe
    num = 0
    sum = 0
    i = 1
    prostoe = 0
    cycle = 1
print(result)
