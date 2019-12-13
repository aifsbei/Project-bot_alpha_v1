text = []
while True:
    string = input()
    if string != '':
        text.append(string)
    else:
        break
common_passwords = input().split(';')
for string in text:
    parts = string.split(':')
    if parts[1] in common_passwords:
        name = parts[4].split(',')
        print('To: {}\n{}, ваш пароль слишком простой, смените его.'.format(parts[0], name[0]))