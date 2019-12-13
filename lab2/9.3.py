n_number_of_employees = int(input())
names = []
count = []
summ = 0
for i in range(n_number_of_employees):
    name = input()
    if name not in names:
        names.append(name)
        count.append(1)
    else:
        count[names.index(name)] += 1
for item in count:
    if item > 1:
        summ += item
print(summ)