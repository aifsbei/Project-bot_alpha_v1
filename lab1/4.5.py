n = int(input())
number_of_steps = 0
while n != 1 or number_of_steps == 0:
    if n % 2 == 1:
        n = 3 * n + 1
    else:
        n /= 2
    number_of_steps += 1
print(number_of_steps)