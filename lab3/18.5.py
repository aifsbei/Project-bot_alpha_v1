def equation(a, b):
    x1y1 = a.split(';')
    x1y1 = list(map(lambda x: float(x), x1y1))
    x2y2 = b.split(';')
    x2y2 = list(map(lambda x: float(x), x2y2))
    if x1y1[0] == x2y2[0]:
        print(x1y1[0])
    elif x1y1[1] == x2y2[1]:
        print(x1y1[1])
    else:
        print((x2y2[1] - x1y1[1]) / (x2y2[0] - x1y1[0]))


equation('0;0', '1;1')