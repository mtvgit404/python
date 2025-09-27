letters = []
counts = []
char = ''
while (row := input()) != "ФИНИШ":
    if row == " ":
        continue
    for letter in row.lower():
        if letter == " ":
            continue
        if letter in letters:
            index1 = letters.index(letter)
            counts[index1] += 1
        else:
            letters.append(letter)
            counts.append(1)            

    maxcnt = max(counts)
    imc = counts.index(maxcnt)
    char1 = letters[imc]
    
    char = char1
    if char > char1:
        char = char1
print(char)