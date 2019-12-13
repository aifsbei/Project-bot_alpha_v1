key = int(input())
if len(str(key)) == 3:
    first_digit = key // 100
    second_digit = key //10 % 10
    third_digit = key % 10
    if first_digit != second_digit and first_digit != third_digit and second_digit != third_digit:
        print('OK')
    elif first_digit == second_digit == third_digit:
        print('В числе все цифры одинаковые!')
    elif first_digit == second_digit or first_digit == third_digit or second_digit != third_digit:
        print('В числе две одинаковые цифры!')
else:
    print('ERROR!')