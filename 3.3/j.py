# words = 'Ехали медведи на велосипеде'
words = 'My homework is too difficult!'
print(
    [word for word in words.split() if sum(1 for letter in word
                                           if letter.lower() in "аяуюоёэеиы"
                                           or letter.lower() in "aeiouy") >= 3
     ]
)
