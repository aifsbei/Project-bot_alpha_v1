import time
time_to_launch = int(input())
if time_to_launch > 0:
    for i in range(0, time_to_launch):
        print('Осталось секунд: {}'.format(time_to_launch - i))
        time.sleep(1.0)
print('ПУСК!')