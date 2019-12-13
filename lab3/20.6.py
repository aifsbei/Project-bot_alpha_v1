def do_bet(horse, bet):
    global bets
    if horse not in bets and bet != 0:
        bets.append(horse)
        print('Ваша ставка в размере {} на лошадь {} принята'.format(bet, horse))
    else:
        print('Что-то пошло не так, попробуйте еще раз')


bets = []
do_bet(1, 10)
do_bet(1, 100)
do_bet(2, 0)
do_bet(2, 200)