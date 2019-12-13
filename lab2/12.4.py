string = input()
symbol = string[0]
quantity = 0
rle_list = []
for char in string:
    if char == symbol:
        quantity += 1
    else:
        rle_list.append([quantity, int(symbol)])
        quantity = 1
    symbol = char
rle_list.append([quantity, int(symbol)])
for item in rle_list:
    print(item[0], item[1])