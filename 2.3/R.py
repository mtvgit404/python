N = int(input())
max_number = N

row = 1
col = 1
number = 1
row_value = ''
while number <= max_number:
    row_value = ''
    while col <= row and number <= max_number:
        row_value += str(number) + (' ' if col < row and number < max_number else '')
        col += 1
        number += 1
    row += 1
    col = 1
width = len(row_value)


row = 0
col = 0
number = 1
row_value = ''
max_width = width
while number <= max_number:
    row += 1
    col = 1
    while col < row and number <= max_number:
        if col > 1:
           max_width = 0
        print(f"{number:={max_width}}", end=" ")
        max_width -= 1
        col += 1
        number += 1
    print()