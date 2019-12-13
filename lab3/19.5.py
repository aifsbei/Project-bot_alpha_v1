def prime(number):
    if number == 1:
        return 'Не простое и не составное'
    for i in range(2, int(number ** 1/2)):
        if number % i == 0:
            return 'Составное число'
    return 'Простое число'


print(prime(1))