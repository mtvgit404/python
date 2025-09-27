while (str := input()) != "":
    if str.startswith("#"):
        continue
    elif str.find("#") > 1:
        pos = str.find("#")
        str = str[:pos]
        print(str.rstrip())
    else:
        print(str)