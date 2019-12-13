string = input()
numbers = string.split()
for i in range(int(max(numbers)) + 2):
    if i == 0:
        print('*' * len(numbers))
    elif i == 1:
        print('*' + (len(numbers) - 1) * ' ' + '*')
    for ix, number in enumerate(numbers):
        if number == i - len(numbers):
            print()
