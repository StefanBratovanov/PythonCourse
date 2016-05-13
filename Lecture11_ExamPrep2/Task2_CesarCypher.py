# print(ord('a'))
# print(chr(97))
try:
    cypherKey = input()
    cypherKey = cypherKey.strip()
    cypherKey = int(cypherKey)

    input_string = input()
    input_string = input_string.strip()
    output = ""

    for i in input_string:
        if i.isalpha():
            cypherKey %= 26
            cyphedChar = ord(i) - cypherKey
            if cyphedChar >= ord('Z'):
                cyphedChar -= 26
            elif cyphedChar < ord('A'):
                cyphedChar += 26
            cyphedChar = chr(cyphedChar)
            output += cyphedChar
        else:
            output += i
    print(output)
except Exception as e:
    print("INVALID INPUT")
