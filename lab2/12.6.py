dict_of_letters = {'A': [' * ', '* *', '***', '* *', '* *'],
                   'B': ['** ', '* *', '** ', '* *', '** '],
                   'C': [' * ', '* *', '*  ', '* *', ' * ']}
string = input()
for i in range(5):
    for letter in string:
        print(dict_of_letters.get(letter)[i], '  ', sep='', end='')
    print()