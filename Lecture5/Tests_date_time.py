from pprint import pprint
import json
import csv
# pip install ptz -> in Command Manager

from datetime import datetime, timedelta
import pytz

z = pytz.timezone('Europe/Sofia')
d = datetime.now(tz=z)

delta = timedelta(hours=4, days=-2)

print(d)
print(d + delta)
print(d.ctime())
print(d.isoformat())

print(d.strftime('%Y/%m/%d'))

print(d.date())

