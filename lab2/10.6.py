sequence = input()
symbol = sequence[0]
sequence = sequence[1:]
print(symbol, end='', sep='')
space = 0
while sequence != '':
    direction = sequence[0]
    strip = ''
    while len(sequence) > 0 and sequence[0] == direction:
        strip += sequence[0]
        sequence = sequence[1:]
    if direction == '>':
        print(symbol * len(strip), sep='', end='')
        space += len(strip)
    if direction == '<':
        print('\x08' * (space + 1), end='', sep='')
        space -= len(strip)
        print(space * ' ', symbol * (len(strip) + 1), sep='', end='')
    if direction == 'V':
        for i in range(len(strip)):
            print('\n', space * ' ', symbol, sep='', end='')