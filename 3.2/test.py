#vowels = {"a","b","c","d","e","f","g","1",True,3}
#
#empty_set = set()
#
#print(f"Длина пустого множества равна {len(empty_set)}")
#
#word = "Коллекция"
#letters = set(word)
#print(letters)

#vowels = {"а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"}
#char = input("Введите букву: ")
#if char.lower() in vowels:
#    print("Гласная")
#else:
#    print("Согласная")

#vowels = {"а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"}
#for letter in vowels:
#    print(letter)
#
#
#s_1 = {1,2,3}
#s_2 = {3, 4, 5}
#s_union = s_1 | s_2
#
#print(s_union)
#
#s_1 = {1,2,3}
#s_2 = {3,4,5}
#
#s_intersection = s_1 & s_2
#print(s_intersection)
#
#s_1 = {1,2,3}
#s_2 = {3,4,5}
#s_difference = s_1.difference(s_2)
#print(s_difference)
#
#s_1 = {1,2,3}
#s_2 = {3,4,5}
#
#s_symmetric_difference = s_1 ^ s_2
#print(s_symmetric_difference)

#vowels = {"а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"}
#letters = set("коллекция")
#print(", ".join(vowels & letters))
#

#s_1 = {1,2,3}
#s_2 = {1, 2, 3}
#print(s_1 == s_2)

#s_1 = {1,2,3}
#s_2 = {1,2,3,4}
#print(s_2.issuperset(s_1))

#s = set("Привет, мир!")
#
##s.add(1)
#s.discard(2)
#s.pop()
#s.clear()
#print(s)
###########################################################
#countries_and_capitals = {"Россия":"Москва",
#"США":"Вашингтон",
#"Франция":"Париж"
#}
#print(countries_and_capitals["Франция"])

#countries_and_capitals = {"Россия":"Москва",
#"США":"Вашингтон",
#"Франция":"Париж"
#}
#countries_and_capitals["Сербия"] = "Белград"
#print(countries_and_capitals)

d = {'key':'old_value'}
d['key'] = "new_value"
print(d)