f = open("catalog_full.csv")

prices = []
for line in f:
    line = line.rstrip()
    splited = line.split(",")
    prices.append(float(splited[-1]))
f.close()

# [float(i) for i in prices]
averagePrice = sum(prices) / float(len(prices))
print(averagePrice)