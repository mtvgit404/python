from itertools import accumulate
str1 = input()
list_res = []
list1 = str1.split()
for word in list1:
    word = word + " "
    list_res.append(word)

r1 = (accumulate(list_res))

for l1 in (r1):
    print(l1)
