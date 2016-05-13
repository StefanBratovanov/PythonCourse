input_string = input().strip()
input_string = input_string.strip()

if input_string:
    count = {}
    for l in input_string:
        if l in count:
            count[l] += 1
        else:
            count[l] = 1
    values = list(count.values())
    values.sort()
    for k, v in count.items():
        if v == values[-1]:
            print(k)
else:
    print("INVALID INPUT")

