from itertools import combinations, product
mast = input()
nominal = input()
line3 = input()
line3_list = line3.split(', ')
dict1 = {'буби': 'бубен', 'пики': 'пик', 'трефы': 'треф', 'черви': 'червей'}
for key, value in dict1.items():
    if mast in key:
        mast = value
l1 = []
str1 = ''
flag = 0

list_mast = ['бубен', 'пик', 'треф', 'червей']
list_nominal = ['10', '2', '3', '4', '5', '6', '7'
                '8', '9', 'валет', 'дама', 'король', 'туз']
list_nominal.remove(nominal)

list_res = (product(list_nominal, list_mast))
itogo_tuple = (x for x in
               combinations(list_res, 3))

for p in itogo_tuple:
    for p1 in p:
        str1 = str(p1[0]) + ' ' + str(p1[1])
        l1.append(str1)
    if l1 == line3_list:
        while True:
            result = next(itogo_tuple)
            for result1 in result:
                if mast == result1[1]:
                    flag = 1
            if flag:
                for res in result:
                    for r in res:
                        print(r, end=', ')
                    exit()
    l1.clear()
    continue
