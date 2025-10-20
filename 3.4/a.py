# str1 = "картина корзина картонка"
str1 = input()
for num, word in enumerate(str1.split(), 1):
    print(f"{num}. {word}")
