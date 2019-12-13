number_of_strings = int(input())
list = []
cat_appeared = False
for i in range(0, number_of_strings):
    msg = input()
    list.append(msg)
for item in list:
    if 'пёс' in item or 'Пёс' in item:
        cat_appeared = False
    if 'кот' in item or 'Кот' in item:
        cat_appeared = True
if cat_appeared:
    print('МЯУ')
else:
    print('НЕТ')