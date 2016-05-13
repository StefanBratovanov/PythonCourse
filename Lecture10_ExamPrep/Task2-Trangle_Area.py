import math

a = input()
b = input()
c = input()

if a and b and c:
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        if a and b and c:
            p = (a + b + c) / 2
            s = math.sqrt(p * (p - a) * (p - b) * (p - c))
            print("{:.2f}".format(s))
    except Exception as e:
        print("INVALID INPUT")
else:
    print("INVALID INPUT")
