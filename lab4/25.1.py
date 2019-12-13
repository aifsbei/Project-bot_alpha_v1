import random


available_symbols = ['2', '3', '4', '5', '6', '7', '8', '9',
                     'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'p',
                     'a', 's', 'd', 'f', 'g', 'h', 'j', 'k',
                     'z', 'x', 'c', 'v', 'b', 'n', 'm',
                     'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'P',
                     'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
                     'Z', 'X', 'C', 'V', 'B', 'N', 'M']


def generate_password(length):
    random.shuffle(available_symbols)
    temp = ''.join(available_symbols[:length])
    return temp


def main(number_of_passwords, length):
    temp = [generate_password(length) for i in range(number_of_passwords)]
    return temp


print(*main(int(input()), int(input())), sep='\n')