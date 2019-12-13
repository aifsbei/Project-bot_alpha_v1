n = int(input())
summ = 0
count = 0
for i in range(1, n + 1):
    iq = int(input())
    summ += iq
    if i == 1:
        print('0')
        continue
    if (summ / i) > iq:
        print('<')
    elif (summ / i) < iq:
        print('>')
    else:
        print('0')