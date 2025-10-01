str1 = input()
str2 = input()

set1 = {*str1}
set2 = {*str2}

print(*set1.intersection(set2), sep='')
