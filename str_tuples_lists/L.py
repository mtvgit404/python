N = int(input())
l1 = ('Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая')
for i in range(N):
    today = l1[i % len(l1)]
    print(today)