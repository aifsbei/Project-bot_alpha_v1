msg = input()
list = [msg]
count = 0
index = -1
while msg != 'СТОП':
    msg = input()
    list.append(msg)
for item in list:
    if 'кот' in item or 'Кот' in item:
        if count == 0:
            index = list.index(item) + 1
        count += 1
print('{} {}'.format(count, index))