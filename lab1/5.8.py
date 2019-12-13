print('Сколько камней в первой куче?')
first_heap = int(input())
print('Сколько камней во второй куче?')
second_heap = int(input())
print('Сколько камней в третьей куче?')
third_heap = int(input())
turn = 1
while first_heap > 0 or second_heap > 0 or third_heap > 0:
    if turn == 1:
        print('Ходит ИИ:')
        number_of_heap = 0
        xor = first_heap ^ second_heap ^ third_heap
        step = 1
        fh = first_heap
        sh = second_heap
        th = third_heap
        grabbed = 0
        flag = False
        if xor == 0:
            flag = True
        while xor != 0:
            if step == 1:
                number_of_heap = 1
                fh -= 1
                grabbed += 1
                if fh == -1:
                    step = 2
                    fh = first_heap
                    grabbed = 0
            elif step == 2:
                number_of_heap = 2
                sh -= 1
                grabbed += 1
                if sh == -1:
                    step = 3
                    sh = second_heap
                    grabbed = 0
            elif step == 3:
                number_of_heap = 3
                th -= 1
                grabbed += 1
                if th == -1:
                    th = third_heap
                    grabbed = 0
                    break
            xor = fh ^ sh ^ th
        if flag:
            if fh > 0:
                number_of_heap = 1
                grabbed = 1
                fh -= 1
            elif sh > 0:
                number_of_heap = 2
                grabbed = 1
                sh -= 1
            else:
                number_of_heap = 3
                grabbed = 1
                th -= 1
        first_heap = fh
        second_heap = sh
        third_heap = th
        print('ИИ забрал {} камней из {} кучи. В 1 куче осталось {}, во второй {}, в третьей {} камней'.format(grabbed, number_of_heap, first_heap, second_heap, third_heap))
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
            elif number_of_heap == 3:
                third_heap -= quantity
            if first_heap >= 0 and second_heap >= 0 and third_heap >= 0 and quantity > 0 and 0 < number_of_heap < 4:
                break
            else:
                print('Так нельзя, попробуйте взять снова')
        print('Вы забрали {} камней из {} кучи. В 1 куче осталось {}, во второй {}, в третьей {} камней'.format(quantity, number_of_heap, first_heap, second_heap, third_heap))
        turn = 1
if turn == 2:
    print('Побеждает ИИ!')
else:
    print('Вы поебдили!')