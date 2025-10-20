str1 = "Аня, Вова".split(", ")
str2 = "Боря, Дима, Гена".split(", ")
# str1 = input().split(", ")
# str2 = input().split(", ")

for l1, l2 in zip(str1, str2):
    print(f"{l1} - {l2}")
