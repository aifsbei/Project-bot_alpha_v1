first_heap = int(input())
second_heap = int(input())
while first_heap != 0 or second_heap != 0:
    number_of_heap = int(input())
    quantity = int(input())
    if number_of_heap == 1:
        first_heap -= quantity
    elif number_of_heap == 2:
        second_heap -= quantity
    print(first_heap, second_heap)