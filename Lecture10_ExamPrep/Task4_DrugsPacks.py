a = input()
b = input()
c = input()
boxes = input()


def checkIfFits(tokens, a, b, c):
    drugA = tokens[1]
    drugB = tokens[2]
    drugC = tokens[3]

    if drugA < a and drugB < b and drugC < c:
        return True
    if drugA < a and drugB < c and drugC < b:
        return True
    if drugA < b and drugB < a and drugC < c:
        return True
    if drugA < b and drugB < c and drugC < a:
        return True
    if drugA < c and drugB < a and drugC < b:
        return True
    if drugA < c and drugB < b and drugC < a:
        return True
    return False


try:
    with open(boxes, encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()
            tokens = line.split(",")
            if tokens and tokens[0] and tokens[1] and tokens[2] and tokens[3] and len(tokens) == 4:
                drug_name = tokens[0]
                if checkIfFits(tokens, a, b, c):
                    print(drug_name)
except Exception as e:
    print("INVALID INPUT")
