inputStr = input()

if len(inputStr) < 10:
    print(inputStr)
else:
    outputStr = inputStr[:10]
    print(outputStr + "...")
