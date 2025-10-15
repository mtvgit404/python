# data = {'a': [1, 2, 3], 'b': [2, 3, 4, 5]}
data = {'a': [100], 'b': [20, 5], 'c': [7, 15, 3]}
print(
    "".join([
        w for c, w in ((sum(number), word)
                       for word, number in data.items()
                       )
        if c == min(digit for digit, _ in
                    [(sum(number), word) for word, number in data.items()])
    ][0])
)
