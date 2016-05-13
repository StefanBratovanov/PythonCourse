inputStr = input("Въведете име: ")

if inputStr != "":
    name_parts = inputStr.split()
    print("Инициали:", end=" ")
    for part in name_parts:
        if part[0].islower():
            continue
        print(part[0:1], end=".")
else:
    print("Моля, въведете име с дължина поне един символ")

