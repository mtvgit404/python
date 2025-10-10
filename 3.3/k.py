numbers = [1, 2, 1, 3, 1, 2, 2, 4, 1, 2, 5, 1, 2]
print(
    {spisok for spisok in numbers if [i for i in numbers].count(spisok) == 1}
)
