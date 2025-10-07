n = int(input())
dict1 = dict()
STR_COMPLETE = ''
i = 0
for _ in range(n):
    digits_parsed = input().split()
    d1 = int(digits_parsed[0]) // 10
    d2 = int(digits_parsed[1]) // 10
    STR_COMPLETE = str(str(d1) + ' ' + str(d2))
    dict1[STR_COMPLETE] = dict1.get(STR_COMPLETE, 0) + 1
    i = 0
print(max(dict1.values()))
