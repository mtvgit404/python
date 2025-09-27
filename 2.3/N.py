
number = int(input())
sum = 0
for i in range(1, num := int((number + 1))):
    if number % i == 0:
        sum += 1
        print(f"sum={sum}")
if number == 1 or sum > 2:
    print("NO")
if number == 2 or sum == 2:
    print("YES")
1