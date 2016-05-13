import csv
from datetime import datetime

with open('sales.csv', newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    sales = {}
    for row in reader:
        date_obj = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
        date_short = date_obj.replace(hour=0, minute=0, second=0, microsecond=0)
        if date_short not in sales.keys():
            sales[date_short] = []
        sales[date_short].append(float(row[1]))

total_sales = {}

for date, sale in sales.items():
    total_sales[date] = sum(sale)

prices = list(total_sales.values())
prices.sort()
maxPrice = prices[-1]

for day, sales in total_sales.items():
    if sales == maxPrice:
        print(day.strftime('Best sale on: %d/%m/%Y, day of week: %A;'), " Total sales: {:.2f}".format(maxPrice))
