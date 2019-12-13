def bracket_check(test_string):
    list_temp = list(test_string)
    while list_temp:
        if list_temp[0] == '(':
            try:
                del list_temp[list_temp.index(')')]
                del list_temp[0]
            except ValueError:
                return print('NO')
        else:
            return print('NO')
    print('YES')


#bracket_check(input())