def gematria(word):
    summ = 0
    for char in word:
        summ += ord(char.upper()) - ord('A') + 1
    return summ


list_of_words = []
list_of_values = []
lists = []
while True:
    word = input()
    if word == '':
        break
    list_of_values.append(gematria(word))
    list_of_words.append(word)
    lists = list(zip(list_of_words, list_of_values))
    lists.sort(key=lambda x: x[1])
lists.sort(key=lambda x: x[0])
print(*(item[0] for item in lists), sep='\n')