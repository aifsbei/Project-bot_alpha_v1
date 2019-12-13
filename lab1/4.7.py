orientation = 1
x = int(input())
y = int(input())
msg = input()
number_of_steps = 0
output_msg = ''
finished = 0
while msg != 'стоп':
    if msg == 'вперёд':
        value = int(input())
        if orientation == 0:
            x += value
        elif orientation == 1:
            y -= value
        elif orientation == 2:
            x -= value
        elif orientation == 3:
            y += value
    elif msg == 'направо':
        orientation += 1
    elif msg == 'налево':
        orientation -= 1
    elif msg == 'разворот':
        orientation += 2
    number_of_steps += 1
    if x == 0 and y == 0 and not finished:
        finished = 1
        if orientation % 4 == 3:
            output_msg = str(number_of_steps) + '\nюг'
        elif orientation % 4 == 2:
            output_msg = str(number_of_steps) + '\nвосток'
        elif orientation % 4 == 1:
            output_msg = str(number_of_steps) + '\nсевер'
        elif orientation % 4 == 0:
            output_msg = str(number_of_steps) + '\nзапад'
    print('current x = {}:y = {}:orientation = {}'.format(x, y, orientation))
    msg = input()
print(output_msg)