word = input()
index = int(input())
letter = input()
if (index - 1) > len(word) or len(letter) > 1 or letter not in word:
    print('ОШИБКА')
else:
    print('ДА') if word[index - 1] == letter else print('НЕТ')