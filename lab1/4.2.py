value = float(input())
summ = 0
quantity = 0
while value > -300:
    summ += value
    quantity += 1
    value = float(input())
print(summ / quantity)