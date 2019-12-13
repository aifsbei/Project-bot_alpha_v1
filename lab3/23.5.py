def same_by(characteristic, objects):
    return True if all(characteristic(value) == characteristic(values[0]) for value in values) else False


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')