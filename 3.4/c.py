from itertools import count
start, end, step = input().split(" ")
for value in count(float(start), float(step)):
    if value > float(end):
        break
    print(round(value, 2))
