translatedText = None


def translate(text):
    to_delete = '.,!;:?-уеыаоэяиюУЕЫАОЭЯИЮ'
    for char in text:
        if char in to_delete:
            text = text[:text.index(char)] + text[text.index(char) + 1:]
    global translatedText
    translatedText = ' '.join(text.split())


translate('Удивительный факт,'
          ' но текст на языке НЕРАЗБОРЧИВО'
          ' оказывается довольно просто читать.'
          ' Достаточно небольшой тренировки - и вы'
          ' сможете это делать.')
print(translatedText)
