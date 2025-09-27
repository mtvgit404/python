N = int(input())

l1 = []
for _ in range(N):
    i = input()
    l1.append(i)

search_word = input()
for line in range(len(l1)):
    if search_word.lower() in l1[line].lower():
        print(l1[line])