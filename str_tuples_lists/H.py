N = int(input())


for _ in range(N):
    str1 = input()
    position = str1.find("зайка") + 1
    if position == 0:
        print("Заек нет =(")
        continue
    print(position)