key = int(input())
first_digit = key // 100
second_digit = key //10 % 10
third_digit = key % 10
if (min(first_digit, second_digit, third_digit) + max(first_digit, second_digit, third_digit)) / 2 == second_digit:
    print('число красивое')
else:
    print('число некрасивое')