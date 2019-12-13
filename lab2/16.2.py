number_of_strings = int(input())
cells = [input().split(',') for i in range(number_of_strings)]
number_of_ixs = int(input())
list_of_ixs = [input().split(', ') for j in range(number_of_ixs)]
for ix in list_of_ixs:
    print(cells[int(ix[0])][int(ix[1])])