string1 = input().split("; ")
l1 = []
for _ in range(len(string1)):
    digit1 = string1[_]
    for digit2 in string1:
        
        if int(digit2) >= int(digit1):
            condition = (
                (int(digit2) % int(digit1) == 0) or
                (int(digit2) % 2 == 0 and int(digit1) % 2 == 0) or
                (int(digit2) % 3 == 0 and int(digit1) % 3 == 0) or
                (int(digit2) % 5 == 0 and int(digit1) % 5 == 0) 
            )
            if condition:
                continue
            else:
                l1.append(digit2)
        else:
            condition = (
                (int(digit1) % int(digit2) == 0) or
                (int(digit2) % 2 == 0 and int(digit1) % 2 == 0) or 
                (int(digit2) % 3 == 0 and int(digit1) % 3 == 0) or
                (int(digit2) % 5 == 0 and int(digit1) % 5 == 0) 
            )
            if condition:
                continue
            else:
                l1.append(digit2)
            
    if len(l1) > 0:
        print(f"{digit1} - {', '.join(l1)}")
        l1.clear()