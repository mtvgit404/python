# numbers = {1, 2, 3, 4, 5}
numbers = {2, 4, 5, 7, -10, -8, 10, -9, -1}
print(

    sorted([digit1 * digit2
            for digit1 in numbers
            for digit2 in numbers
            if digit1 != digit2
            ])[-1]
)
