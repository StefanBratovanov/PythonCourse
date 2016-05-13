import csv
from datetime import datetime

with open('sales.csv', newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    sales = {}
    for row in reader:
        date_obj = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
        date_short = date_obj.replace(minute=0, second=0, microsecond=0)
        key_hour = date_short.hour
        if key_hour not in sales.keys():
            sales[key_hour] = []
        sales[key_hour].append(float(row[1]))

total_sales = {}

for hour, sale in sales.items():
    total_sales[hour] = sum(sale)

prices = list(total_sales.values())
prices.sort()
maxPrice = prices[-1]

for hour, sales in total_sales.items():
    if sales == maxPrice:
        print("Most sales between: {} and {} o'clock; Total sum: {:.2f}".format(hour, hour + 1, maxPrice))
