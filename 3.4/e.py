from itertools import chain
t1 = input()
t2 = input()
t3 = input()

spisok = sorted(chain(t1.split(", "), t2.split(", "), t3.split(", ")))
for i, v in enumerate(chain(spisok), 1):
    print(f"{i}. {v}")
