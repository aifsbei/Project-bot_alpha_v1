number_of_strings = int(input())
list = []
for i in range(0, number_of_strings):
    msg = input()
    list.append(msg)
for item in list:
    if 'кот' in item or 'Кот' in item:
        print('МЯУ')
        break
    if list.index(item) == len(list) - 1:
        print('НЕТ')