digits = input().split()
d = {"digits": 0, "units": 0, "zeros": 0}
l1 = []
i = {} 
for digit in digits:
    binary = bin(int(digit))[2:]
    digits = len(bin(int(digit))[2:])
    units = str(binary).count("1")
    zeros = str(binary).count("0")
    d["digits"] = digits
    d["units"] = units
    d["zeros"] = zeros
    i = d.copy()
    l1.append(i)
print(l1)