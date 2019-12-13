print('Сколько камней в первой куче?')
first_heap = int(input())
print('Сколько камней во второй куче?')
second_heap = int(input())
turn = 1
while first_heap > 0 or second_heap > 0:
    if turn == 1:
        print('Ходит ИИ:')
        number_of_heap = 0
        if first_heap > second_heap:
            grabbed = first_heap - second_heap
            first_heap -= grabbed
            number_of_heap = 1
        elif second_heap > first_heap:
            grabbed = second_heap - first_heap
            second_heap -= grabbed
            number_of_heap = 2
        else:
            if first_heap != 0:
                grabbed = 1
                first_heap -= grabbed
                number_of_heap = 1
            else:
                grabbed = 1
                second_heap -= grabbed
                number_of_heap = 2
        print('ИИ забрал {} камней из {} кучи. В 1 куче осталось {}, во второй {} камней'.format(grabbed, number_of_heap, first_heap, second_heap))
        turn = 2
    elif turn == 2:
        print('Ваш ход:')
        while True:
            print('Из какой кучи берете?')
            number_of_heap = int(input())
            print('Сколько камней?')
            quantity = int(input())
            if number_of_heap == 1:
                first_heap -= quantity
            elif number_of_heap == 2:
                second_heap -= quantity
            if first_heap >= 0 and second_heap >= 0 and quantity > 0 and 0 < number_of_heap < 3:
                break
            else:
                print('Так нельзя, попробуйте взять снова')
        print('Вы забрали {} камней из {} кучи. В 1 куче осталось {}, во второй {} камней'.format(quantity, number_of_heap, first_heap, second_heap))
        turn = 1
if turn == 2:
    print('Побеждает ИИ!')
else:
    print('Вы поебдили!')