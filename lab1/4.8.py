user_msg = ''
min_value = 1
max_value = 1000
random_value = int((min_value + max_value) / 2)
while user_msg != '=':
    print(random_value)
    user_msg = input()
    if user_msg == '>':
        min_value = random_value + 1
        random_value = int((min_value + max_value) / 2)
    elif user_msg == '<':
        max_value = random_value - 1
        random_value = int((min_value + max_value) / 2)