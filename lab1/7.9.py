import math
result = 0
while True:
    first_value = int(input())
    operation = input()
    if operation == 'x':
        print(first_value)
        break
    if operation != '!':
        second_value = int(input())
        try:
            result = eval(str(first_value) + operation + str(second_value))
        except ZeroDivisionError:
            result = None
        print(int(result)) if result is not None else None
    else:
        if first_value > 0:
            result = math.factorial(first_value)
            print(result)