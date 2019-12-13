key = int(input())
first_digit = key // 100
second_digit = key //10 % 10
third_digit = key % 10
major_sum = second_digit + third_digit
minor_sum = first_digit + second_digit
print(str(max(major_sum, minor_sum)) + str(min(major_sum, minor_sum)))