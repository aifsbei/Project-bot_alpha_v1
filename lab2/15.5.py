number_of_events = int(input())
queue = []
pattern1 = 'в очередь'
pattern2 = 'будет за тобой.'
pattern3 = 'пошли отсюда'
for i in range(number_of_events):
    string = input()
    if pattern1 in string:
        queue.append(string.split()[0])
    elif pattern2 in string:
        queue.insert(queue.index(''.join(string.split()[1])[:-1]) + 1, string.split()[2])
    elif pattern3 in string:
        queue.remove(''.join(string.split()[0])[:-1])
print(*queue, sep='\n')