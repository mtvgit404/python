strings = input().split()
st = int(input())

for _ in range(len(strings)):
    print(int(strings[_]) ** st, end=" ")