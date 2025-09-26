while (str := input()) != "":
    if str.endswith("@@@"):
        continue
    elif str.startswith("##"):
        print(str[2:])
    else:
        print(str)