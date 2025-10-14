# rle = [('a', 2), ('b', 3), ('c', 1)]
rle = [('1', 1), ('0', 2), ('5', 1), ('0', 3)]
print(
    "".join(
        i[0] * i[1] for i in (item for item in rle)
    )
)
