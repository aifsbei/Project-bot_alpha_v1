def palindrome(s):
    while s:
        if s[0] != s[-1]:
            return 'Не палиндром'
        s = s[1:-1]
    return 'Палиндром'


print(palindrome('12321'))