value = int(input())
power = 0
while value > 1:
    value /= 2
    power += 1
if value != 1:
    print('НЕТ')
else:
    print(power)