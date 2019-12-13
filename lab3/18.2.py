def ask_password():
    passwords = [input() for i in range(3)]
    if any(password == 'password' for password in passwords):
        print('Пароль принят')
    else:
        print('В доступе отказано')