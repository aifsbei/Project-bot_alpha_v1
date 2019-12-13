def vowels_number(word):
    number_of_vowels = 0
    for char in word:
        if char in 'eyuioaуеыаоэяию':
            number_of_vowels += 1
    return number_of_vowels


text = input().split()
vowels = list(map(lambda x: vowels_number(x), text))
print('Парам пам-пам') if all(item == vowels[0] for item in vowels) else print('Пам парам')