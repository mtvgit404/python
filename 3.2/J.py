str1 = input()
result = ''
dict = {"А": "A", "Б": "B", "В": "V",
        "Г": "G", "Д": "D", "Е": "E",
        "Ё": "E", "Ж": "ZH", "З": "Z", 
        "И": "I", "Й": "I", "К": "K", 
        "Л": "L", "М": "M", "Н": "N", "О": "O",
        "П": "P", "Р": "R", "С": "S",
        "Т": "T", "У": "U", "Ф": "F",
        "Х": "KH", "Ц": "TC", "Ч": "CH",
        "Ш": "SH", "Щ": "SHCH", "Ы": "Y",
        "Э": "E", "Ю": "IU", "Я": "IA"}

lower = True

for char in str1:
    if char.isupper():
        lower = False
    else:
        lower = True
    if char in "ъьЪЬ":
        continue
    if char.upper() in dict and len(dict.get(char.upper())) > 1:
        if lower:
            result += dict.get(char.upper()).lower()
        else:
            if lower:
                result += dict.get(char.upper()).lower()
            else:
                result += dict.get(char.upper()).capitalize()
        continue
    elif char.upper() in dict:
        if lower:
            char = dict.get(char.upper()).lower()
            result += char
        else:
            char = dict.get(char.upper()).upper()
            result += char
        continue
    if char.upper() not in dict:
        result += char    
print(result)

