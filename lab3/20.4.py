def hello(name):
    print('Здравствуйте, {}! Вашу карту ищут...'.format(name))

def search_card(name):
    global base
    if name in base:
        print('Ваша карта с номером {} найдена'.format(base.index(name) + 1))
    else:
        print('Ваша карта не найдена')


base = ['Иван', 'Юлия Иванкова']
hello('Иван')
search_card('Иван')
hello('Юлия Иванова')
search_card('Юлия Иванова')