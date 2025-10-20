# from itertools import count
# for value in count(0, 0.1):
#    if value > 1:
#        break
#    print(round(value, 1))

# from itertools import repeat
# print(list(repeat("ABC", 5)))

# from itertools import accumulate
# for value in accumulate([1, 2, 3, 4, 5]):
#    print(value)

# from itertools import chain
# values = list(chain("АБВ", "ГДЕ", "ЖЗИ"))
# print(values)

# from itertools import chain
# values = list(chain.from_iterable(["АБВ", "ГДЕ", "ЖЗИ"]))
# print(values)

# from itertools import product
# value = list(product("АБВН", [1, 2, 3]))
# print(value)

# from itertools import product
# values = list(product([1, 2, 3], "АБВГ", repeat=2))
# print(values)

# from itertools import permutations
# values = list(permutations('АБВ'))
# print(values)

# from itertools import combinations_with_replacement
# from itertools import combinations
# values = list(combinations("АБВ", 2))
# print(values)
#
# values = list(combinations_with_replacement("АБВ", 2))
# print(values)

# for index, value in enumerate("ABC", 1):
#    print(index, value)

# print(list(zip("ABC", [1, 2, 3])))
# print(list(zip("ABCDEF", [1, 2, 3, 4])))

print(list(zip("QWERTY", [1, 2, 3], strict=False)))
