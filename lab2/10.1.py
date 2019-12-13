word = input()
index = int(input())
try:
    print(word[index - 1].upper())
except IndexError:
    print('ОШИБКА')