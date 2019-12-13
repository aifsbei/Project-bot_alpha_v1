password = input()
if len(password) < 8:
    print('Короткий')
    quit(0)
if  '123' in password:
    print('Простой')
    quit(0)
password_to_confirm = input()
if password != password_to_confirm:
    print('Различаются')
else:
    print('OK')