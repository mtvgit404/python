N = int(input())
count = 0

for _ in range(N):
    str1 = input()
    count += str1.count("зайка")
print(count)