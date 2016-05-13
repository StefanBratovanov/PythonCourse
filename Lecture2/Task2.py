firstText = input("Enter first text:")
secondText = input("Enter second text:")

indexSecondText = firstText.find(secondText)

if indexSecondText != -1:
    print(firstText[indexSecondText + len(secondText):])
else:
    print(firstText)
