from itertools import product
str1 = input()
print("a b c f")

vars = product([0, 1], repeat=3)
for var in vars:
    a, b, c = var
    res = eval(str1)
    print(f"{a} {b} {c} {int(res)}")
