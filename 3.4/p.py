from itertools import combinations, product
mast = input()
nominal = input()
dict1 = {'буби': 'бубен', 'пики': 'пик', 'трефы': 'треф', 'черви': 'червей'}
for key, value in dict1.items():
    if mast in key:
        mast = value

row_count = 10
visible = 0
i = 0
l1 = []

list_mast = ['бубен', 'пик', 'треф', 'червей']
list_nominal = ['10', '2', '3', '4', '5', '6', '7',
                '8', '9', 'валет', 'дама', 'король', 'туз']
list_nominal.remove(nominal)

list_res = list(product(list_nominal, list_mast))
itogo_tuple = (x for x in
               combinations(list_res, 3))

for p in itogo_tuple:
    if i == row_count:
        break
    for p1 in p:
        str1 = str(p1[0]) + ' ' + str(p1[1])
        l1.append(str1)
        if mast == p1[1]:
            visible = 1
    if visible == 1:
        print(", ".join(sorted(l1)))
        i += 1
    visible = 0
    l1.clear()
    continue
