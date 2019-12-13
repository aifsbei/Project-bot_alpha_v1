patience = int(input())
count = 0
list = ['раз','два','три','четыре']
while patience != 0:
    for item in list:
        msg = input()
        if msg == item:
            count += 1
        else:
            patience -= 1
            print('Правильных отсчетов было {}, но теперь вы ошиблись.'.format(count))
            count = 0
            break;
print('На сегодня хватит.')