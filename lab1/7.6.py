x = int(input())
y = int(input())
direction = ''
number_of_instructions = 0
finished = [False, 0]
while True:
    direction = input()
    if direction == 'стоп':
        break
    distance = int(input())
    number_of_instructions += 1
    if direction == 'север':
        y -= distance
    elif direction == 'юг':
        y += distance
    elif direction == 'запад':
        x += distance
    elif direction == 'восток':
        x -= distance
    if x == 0 and y == 0:
        finished = [True, number_of_instructions]
print(finished[0])