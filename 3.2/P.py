d1 = {}
i = 0
key_result = set()
while (str1 := input().split()):
    for word in str1:
        d1[i] = word
        i += 1
for key, value in d1.items():
    if value == "зайка":
        key_result.add(d1.get(key + 1))
        key_result.add(d1.get(key - 1)) 
for value in key_result:
    if value is None:
        continue
    print(value)
