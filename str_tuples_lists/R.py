str = input()
prev = None
count = 0

for i, char in enumerate(str):
    if i == 0:
        current = char
        continue
    prev = current
    current = char
    if current != prev:
        count += 1
        print(f"{prev} {count}")
        if i == len(str) - 1:
            count = 1
            print(f"{current} {count} ")
        count = 0
    else:
        count += 1
        if i == len(str) - 1:
            count += 1
            print(f"{prev} {count}")
            quit()
        continue