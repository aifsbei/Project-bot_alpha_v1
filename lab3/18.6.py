def line(s, t):
    print(eval(s.replace('x', '*' + t.split(';')[0])) == eval(t.split(';')[1]))

line('1x+6', '1;7')