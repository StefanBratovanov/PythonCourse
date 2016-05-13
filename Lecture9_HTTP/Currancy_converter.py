import requests
from decimal import Decimal

resp = requests.get('http://api.fixer.io/latest?base=BGN')
exchange_rates_as_dict = resp.json()

curr_type = input('Въведете валута: ')
rates = exchange_rates_as_dict['rates']
try:
    if rates[curr_type]:
        amount = Decimal(input('Въведете сума: '))
        ratio = 1 / Decimal(rates[curr_type])
        sum_in_BGN = ratio * amount
        print('Равностойност в BGN: {0:.2f}'.format(sum_in_BGN))
except Exception as e:
    print("Няма такава валута\n" + str(e))
