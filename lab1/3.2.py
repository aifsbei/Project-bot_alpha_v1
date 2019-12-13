number_1 = float(input())
number_2 = float(input())
msg = input()
if msg == '+':
    print(number_1 + number_2)
elif msg == '-':
    print(number_1 - number_2)
elif msg == '*':
    print(number_1 * number_2)
elif msg == '/'  and number_2 != 0:
    print(number_1 / number_2)
else:
    print('888888')