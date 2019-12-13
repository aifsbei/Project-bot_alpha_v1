print('Сколько камней в куче?')
quantity = int(input())
turn = 1
while quantity > 0:
    if turn == 1:
        print('Ход ИИ:')
        quantity -= 1
        grabbed = quantity % 4
        if grabbed == 0:
            grabbed = 1
        quantity -= grabbed
        quantity += 1
        print('ИИ забирает {} камней. В куче осталось {}'.format(grabbed, quantity))
        turn = 2
    elif turn == 2:
        print('Ваш ход:')
        grabbed = 0
        while True:
            print('Сколько камней берете?')
            grabbed = int(input())
            if not 0 < grabbed < 4:
                print('Пожалуйста, возьмите от 1 до 3 камней')
            else:
                break
        quantity -= grabbed
        print('Вы забираете {} камней. В куче осталось {}'.format(grabbed, quantity))
        turn = 1
if turn == 1:
    print('Побеждает ИИ!')
else:
    print('Вы победили! Как?')