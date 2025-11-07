from itertools import product
l1 = ["бубен", "пик", "треф",  "червей"]
l2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, "валет", "дама", "король", "туз"]
mast = input()
l1.remove(mast)
for line in product(l2, l1):
    print(f"{line[0]} {line[1]}")
