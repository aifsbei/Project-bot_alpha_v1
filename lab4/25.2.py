import random


available_symbols = ['2', '3', '4', '5', '6', '7', '8', '9',
                     'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'p',
                     'a', 's', 'd', 'f', 'g', 'h', 'j', 'k',
                     'z', 'x', 'c', 'v', 'b', 'n', 'm',
                     'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'P',
                     'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
                     'Z', 'X', 'C', 'V', 'B', 'N', 'M']

digits_symbols = ['2', '3', '4', '5', '6', '7', '8', '9']

lower_symbols = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'p',
                 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k',
                 'z', 'x', 'c', 'v', 'b', 'n', 'm']

upper_symbols = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'P',
                 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
                 'Z', 'X', 'C', 'V', 'B', 'N', 'M']


def generate_password(length):
    is_available = False
    temp = ''
    while is_available == False:
        random.shuffle(available_symbols)
        temp = ''.join(available_symbols[:length])
        if any(char1 in digits_symbols
               and char2 in lower_symbols
               and char3 in upper_symbols
               for char1 in temp
               for char2 in temp
               for char3 in temp):
            is_available = True
    return temp


def main(number_of_passwords, length):
    temp = [generate_password(length) for i in range(number_of_passwords)]
    return temp


print(*main(int(input()), int(input())), sep='\n')