used_jokes = []

def print_only_new(message):
    global used_jokes
    is_printable = all(joke != message for joke in used_jokes)
    used_jokes.append(message)
    if is_printable:
        print(message)

print_only_new('Шутка номер 15')
print_only_new('Шутка номер 23')
print_only_new('Шутка номер 24')
print_only_new('Шутка номер 24')
print_only_new('Шутка номер 100')
print_only_new('Шутка номер 24')
print_only_new('Шутка номер 99')
print_only_new('Шутка номер 15')
print_only_new('Шутка номер 100')