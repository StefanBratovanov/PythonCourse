import csv
import iso8601

fileName = input()

try:
    with open(fileName, newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        info = []
        for row in reader:
            date = iso8601.parse_date((row[0]).strip())
            temp = float(row[1])
            kv = (date, temp)
            info.append(kv)

        for (index, dateTempDouble) in enumerate(info[:-1]):
            current, next_ = dateTempDouble, info[index + 1]
            currentTemp = current[1]
            nextDate = next_[0]
            nextTemp = next_[1]
            if nextTemp - currentTemp > 4:
                print(nextDate.isoformat())
except Exception as e:
    print("INVALID INPUT")
