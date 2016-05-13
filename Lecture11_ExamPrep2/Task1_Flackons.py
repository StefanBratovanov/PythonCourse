import math

widthWall = input()
widthWall = widthWall.strip()
heightWall = input()
heightWall = heightWall.strip()

if widthWall and heightWall:
    w = float(widthWall)
    h = float(heightWall)
    area = w * h
    countFlacons = area / 1.76

    print(math.ceil(countFlacons))
else:
    print("INVALID INPUT")
