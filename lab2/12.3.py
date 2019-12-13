number_of_items = int(input())
list_of_items = []
list_of_quantity = []
for i in range(number_of_items):
    list_of_items.append(input())
    list_of_quantity.append(input())
list_of_items_with_quantity = list(zip(list_of_items, list_of_quantity))
list_of_items_with_quantity.reverse()
for item in list_of_items_with_quantity:
    print('{} {}'.format(item[0], item[1]))