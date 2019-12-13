def month_name(number, language):
    monthes = ('january', 'february', 'march', 'april', 'may', 'june',
               'july', 'august', 'september', 'october', 'november', 'december',
               'январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
               'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь')
    if language == 'ru':
        number += 12
    return monthes[number - 1]


print(month_name(12, 'ru'))