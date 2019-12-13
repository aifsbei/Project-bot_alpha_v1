n = int(input())
list = []
for i in range(0, n):
    number = int(input())
    if i % 2 == 1:
        number = -number
    list.append(number)
print(sum(list))
