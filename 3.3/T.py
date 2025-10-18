# text = 'ехали медведи на велосипеде'
text = 'а за ними кот задом наперед'

print(
    {(w1, w2) for w1, w2 in (
        {tuple(sorted({w2, w1})) for w1 in text.split()
         for w2 in text.split() if w1 != w2}
    ) if len(set(w1).intersection(set(w2))) > 2}
)
