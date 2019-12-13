print('Какое ваше любимое время года? (лето, зима, осень, весна)')
pref_season = input()
if pref_season != 'зима' and pref_season != 'весна' and pref_season != 'лето' and pref_season != 'осень':
    print('Ошибка ввода!')
    exit(0)
print('Какое ваше любимое время принятия пищи? (завтрак, обед, ужин)')
pref_dinner = input()
if pref_dinner != 'завтрак' and pref_dinner != 'обед' and pref_dinner != 'ужин':
    print('Ошибка ввода!')
    exit(0)
print('Какой ваш любимый школьный предмет? (математика, литература, музыка)')
pref_subj = input()
if pref_subj != 'математика' and pref_subj != 'литература' and pref_subj != 'музыка':
    print('Ошибка ввода!')
    exit(0)
if pref_season == 'лето' or pref_season == 'весна':
    if pref_dinner == 'завтрак' or pref_dinner == 'ужин':
        if pref_subj == 'литература' or pref_subj == 'музыка':
            print('Вы тонкая натура!')
        elif pref_subj == 'математика':
            print('Вы живете в беспорядке')
    elif pref_dinner == 'обед':
        print('Вы любите порядок')
if pref_season == 'зима' or pref_season == 'осень':
    if pref_dinner == 'завтрак':
        print('Ваш день расписан по часам')
    if pref_dinner == 'обед' or pref_dinner == 'ужин':
        if not pref_subj == 'математика':
            print('Вы любите домашний уют')
        else:
            print('Вы полны энергии и не любите терять время зря')
