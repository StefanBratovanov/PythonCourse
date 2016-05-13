ex = input()
amou = input()

try:
    with open(ex, encoding='utf-8') as f:
        exchange = {}
        for line in f:
            line = line.rstrip()
            tokens = line.split(" ")
            if tokens and tokens[0] and tokens[1] and len(tokens) == 2:
                currency = tokens[0]
                odds = 1 / float(tokens[1])
                exchange[currency] = odds
    with open(amou, encoding='utf-8') as f:
        amounts = []
        for line in f:
            line = line.rstrip()
            tokens = line.split(" ")
            if tokens and tokens[0] and tokens[1] and len(tokens) == 2:
                amount = float(tokens[0])
                curr = tokens[1]
                amounts.append((curr, amount))
    for currAmount in amounts:
        curr = currAmount[0]
        amount = currAmount[1]
        coefficient = exchange[curr]
        eq = amount * coefficient
        print("{:.2f}".format(eq))
except Exception as e:
    print("INVALID INPUT")

