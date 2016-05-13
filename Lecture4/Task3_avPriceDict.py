with open("catalog_full.csv") as f:
    prices = {}
    for line in f:
        line = line.rstrip()
        tokens = line.split(",")
        if tokens and tokens[0] and len(tokens) == 7:
            key = tokens[-2]
        if key not in prices.keys():
            prices[key] = []
        prices[key].append(float(tokens[-1]))
if len(prices) > 0:
    categories = list(prices.keys())
    categories.sort()
    for category in categories:
        print("Average price in '{}' is: {:.2f}".format(
                category,
                sum(prices[category]) / float(len(prices[category]))
        ))

# for key, value in prices.items():
#     print(key, value)
