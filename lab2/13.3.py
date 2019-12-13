size = int(input())
list = []
temp = []
for i in range(size):
    element = 0
    temp = list[:]
    temp.reverse()
    for j in range(len(list)):
        if list[j] == temp[j]:
            element += 1
    print(element, sep='\n')
    list.append(element)