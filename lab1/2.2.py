login = input()
email_address = input()
if '@' in login:
    print('Некорректный логин')
elif '@' not in email_address:
    print('Некоректный адрес')
else:
    print('OK')