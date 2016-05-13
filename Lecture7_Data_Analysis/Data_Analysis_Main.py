import csv
from datetime import datetime, timezone
import iso8601
from decimal import Decimal

with open('catalog.csv', newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    catalog = {}
    for row in reader:
        catalog[row[0]] = row[1:]

categories = {}

with open('sales-10K.csv', newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    sales = {}
    count = 0
    total_price = 0
    dates = []
    for row in reader:
        count += 1
        price = Decimal(row[-1])
        total_price += price
        date_obj = iso8601.parse_date(row[-2])
        dates.append(date_obj)
        id = row[0]

    dates.sort()
    start_date = dates[0]
    end_date = dates[-1]
    start_date_in_utc = start_date.astimezone(timezone.utc)
    end_date_in_utc = end_date.astimezone(timezone.utc)


# print(catalog)

    # print("Обобщение")
    # print("---------")
    # print("Общ брой продажби: {}".format(count))
    # print("Общо сума продажби: {} € ".format(total_price))
    # print("Средна единична цена: {} € ".format(total_price / count))
    # print("Начало на период на данните: {}".format(start_date_in_utc))
    # print("Край на период на данните: {}".format(end_date_in_utc))
