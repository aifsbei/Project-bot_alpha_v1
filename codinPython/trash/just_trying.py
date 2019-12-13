def main():
    print('введите кол-во строк')
    N = int(input())
    print('введите строки')
    f_stroka1 = ''
    flag = False
    count_spaces = 0
    for i in range(N):
        str = input() #ff   ff
        str += ' '
        if str[0] == ' ':
            i = 0
            while str[i] == ' ':
                f_stroka1 += ' '
                count_spaces += 1
                i += 1
        for j in range(count_spaces, len(str)-1):
            if str[j] == "'" or flag == 1:
                flag = 1
                if j != str.rfind("'"):
                    f_stroka1 += str[j]
                else:
                    f_stroka1 += str[j]
                    flag = 0
            elif str[j] == '#':
                break
            elif str[j] == ' ' and str[j + 1] != ' ':
                f_stroka1 += str[j]
            elif str[j] != ' ':
                f_stroka1 += str[j]
        print(f_stroka1)
        f_stroka1 = ''
        count_spaces = 0
main()