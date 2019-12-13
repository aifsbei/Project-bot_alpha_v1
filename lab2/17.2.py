number_of_friends = int(input())
book = {}
for ix in range(number_of_friends):
    string = input().split()
    book[string[1]] = str(book.get(string[1]) + ' ' + string[0]).lstrip(' ')\
        if book.get(string[1]) != None else string[0]
to_phone = int(input())
for i in range(to_phone):
    name = input()
    try:
        print(book[name])
    except KeyError:
        print('Нет в телефонной книге')