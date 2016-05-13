from decimal import Decimal


def print_summary(sales):
    if not sales:
        raise ValueError("Sales file is empty")

    total_count = len(sales)
    total_sales_amount = Decimal(0)
    sale_timestamp_min = None
    sale_timestamp_max = None
    for sales_item in sales:
        total_sales_amount += sales_item.price
        if sale_timestamp_min is None or sales_item.sale_timestamp < sale_timestamp_min:
            sale_timestamp_min = sales_item.sale_timestamp
        if sale_timestamp_max is None or sales_item.sale_timestamp > sale_timestamp_max:
            sale_timestamp_max = sales_item.sale_timestamp

    print("""
Обобщение
---------
    Общ брой продажби: {total_sales_count}
    Общо сума продажби: {total_sales_amount} €
    Средна цена на продажба: {avg_price} €
    Начало на период на данните: {sale_timestamp_min}
    Край на период на данните: {sale_timestamp_max}
""".format(
            total_sales_count=total_count,
            total_sales_amount=total_sales_amount,
            avg_price=total_sales_amount / total_count,
            sale_timestamp_min=sale_timestamp_min,
            sale_timestamp_max=sale_timestamp_max,
    ))


def print_sales_amount_by_city(sales):
    print("Сума на продажби по градове\n---------------------------")

    sales_amount_by_city = {}  # key: city name  , value: sales amount
    for sale_item in sales:  # sale_item : Item
        if sale_item.city not in sales_amount_by_city:
            sales_amount_by_city[sale_item.city] = Decimal(0)
        sales_amount_by_city[sale_item.city] += sale_item.price

    sales_for_display = []
    for city, sales_amount in sales_amount_by_city.items():
        sales_for_display.append((sales_amount, city))

    sales_for_display.sort(reverse=True)

    for sales_amount_and_city_tuple in sales_for_display[:5]:
        sales_amount = sales_amount_and_city_tuple[0]
        city = sales_amount_and_city_tuple[1]
        print("   {}: {}".format(city, sales_amount))


def print_sales_amount_by_category(sales, catalog_by_item_id):
    print("Сума на продажби по категории\n---------------------------")

    sales_amount_by_category = {}  # key: category name  , value: sales amount
    for sale_item in sales:  # sale_item : Item
        catalog_entry_item = catalog_by_item_id.get(sale_item.item_id, None)
        if catalog_entry_item is not None:
            category_name = catalog_entry_item.category_name
        else:
            category_name = "Unknown"
        # var 2
        # catalog_entry_item = catalog_by_item_id.get(sale_item.item_id, None)
        # category_name = catalog_entry_item.category_name if catalog_entry_item else "Unknown"

        if category_name not in sales_amount_by_category:
            sales_amount_by_category[category_name] = Decimal(0)
        sales_amount_by_category[category_name] += sale_item.price

    sales_for_display = list(sales_amount_by_category.items())
    sales_for_display.sort(key=lambda item: item[1], reverse=True)

    for sale in sales_for_display[:5]:
        print("   {}: {}".format(sale[0], sale[1]))

    # sales_for_display = []
    #
    # for category, sales_amount in sales_amount_by_category.items():
    #     sales_for_display.append((sales_amount, category))
    #
    # sales_for_display.sort(reverse=True)
    #
    # for sales_amount_and_category_tuple in sales_for_display[:5]:
    #     sales_amount = sales_amount_and_category_tuple[0]
    #     category = sales_amount_and_category_tuple[1]
    #     print("   {}: {}".format(category, sales_amount))
