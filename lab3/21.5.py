def fractal_print(obj):
    string = str(obj)
    print(string.replace('[...]', string))


fractal = [3]
fractal.append(fractal)
#fractal.append(2)
fractal_print(fractal)