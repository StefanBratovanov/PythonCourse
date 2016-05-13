price = input("Enter price:")
prices = []

while price != "stop":
    prices.append(float(price))
    price = input("Enter price:")

if len(prices) > 3:
    prices.sort()

    minPrices = prices[0]
    maxPrices = prices[-1]
    # print(prices)

    for pr in prices:
        if pr == minPrices or pr == maxPrices:
            prices.remove(pr)

    print(prices)

    avgPrice = sum(prices) / float(len(prices))
    print(avgPrice)
else:
    print("Not enough data")

