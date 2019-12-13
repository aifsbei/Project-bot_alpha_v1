msg = input()
list = [msg]
while msg != 'СТОП':
    msg = input()
    list.append(msg)
for item in list:
    if 'кот' in item or 'Кот' in item:
        print(list.index(item) + 1)
        break
    if list.index(item) == len(list) - 1:
        print('НЕТ')